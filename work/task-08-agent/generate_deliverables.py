"""Generate outputs/task-08/ deliverables and run integrity verification."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task08-first-pass-003"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-08"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
    captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
    manifest = json.loads((RUN_DIR / "manifest.json").read_text(encoding="utf-8"))
    validation = json.loads((RUN_DIR / "validation.json").read_text(encoding="utf-8"))

    # Save metrics JSON via pipeline
    metrics_proc = subprocess.run(
        [sys.executable, "-B", "research_pipeline.py", "--store", "work/research-runs",
         "metrics", "--run-id", RUN_ID, "--target", RUN_ID],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    metrics = json.loads(metrics_proc.stdout)
    (OUT_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")

    # 1. Exact copy of ten app records
    shutil.copyfile(RUN_DIR / "records.json", OUT_DIR / "records.json")

    # Verify all 10 IDs, no synthetic flags, all evidence resolves
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(11, 21)), f"Unexpected IDs: {ids}"
    assert manifest["synthetic"] is False
    assert metrics["synthetic"] is False

    ev_checked = 0
    for r in records:
        def walk_ev(obj):
            nonlocal ev_checked
            if isinstance(obj, dict):
                if "evidence" in obj and isinstance(obj["evidence"], list):
                    for ev in obj["evidence"]:
                        snap = RUN_DIR / ev["snapshot_ref"]
                        assert snap.exists(), f"Missing snapshot {snap}"
                        assert sha256_file(snap) == ev["content_sha256"], f"Hash mismatch {snap}"
                        ev_checked += 1
                for v in obj.values():
                    walk_ev(v)
            elif isinstance(obj, list):
                for item in obj:
                    walk_ev(item)
        walk_ev(r)

    # Verify sealed Task 04/05/06/07 baselines untouched
    baseline_checks = {
        "pilot-first-pass-001/records.json": (
            ROOT / "work/task-04-runs/pilot-first-pass-001/records.json",
            "10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90",
        ),
        "pilot-first-pass-001/seal.json": (
            ROOT / "work/task-04-runs/pilot-first-pass-001/seal.json",
            "eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2",
        ),
        "task05-review-002/seal.json": (
            ROOT / "work/task-04-runs/task05-review-002/seal.json",
            "9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f",
        ),
        "outputs/task-06/sampling-manifest.json": (
            ROOT / "outputs/task-06/sampling-manifest.json",
            "7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327",
        ),
        "data/apps.json": (
            ROOT / "data/apps.json",
            "6e3aada149102c2e5539c126aa556c1ceaca3d9d25ca6e0a8f56b3a569f81c19",
        ),
        "task07-first-pass-003/records.json": (
            ROOT / "work/research-runs/task07-first-pass-003/records.json",
            "e22d6ce79075aa0cef21928ad30f6d61f4c32d024fd98ada2428dff1a70c57b7",
        ),
        "task07-first-pass-003/seal.json": (
            ROOT / "work/research-runs/task07-first-pass-003/seal.json",
            "0fe78d44c22f228294eb6592b7f2790c44d70a6e1417d6aaa94cc49c35069118",
        ),
    }
    for label, (path, expected) in baseline_checks.items():
        actual = sha256_file(path)
        assert actual == expected, f"Baseline modified: {label} ({actual} != {expected})"

    # 2. Source Index
    src_lines = [
        "# Task 08: Source Index (Support and Helpdesk, IDs 11–20)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`; note 4 `developer.helpscout.com` snapshots returned compressed binary bytes and were excluded from claim citations)",
        f"- **Resolved Evidence Observations Verified**: {ev_checked} (100% snapshot existence & SHA-256 match)",
        "",
        "## Captured Sources",
        "",
        "| App ID | App | Kind | Envs | Lines | Captured On | URL | Snapshot SHA-256 (prefix) |",
        "| ---: | --- | --- | --- | ---: | --- | --- | --- |",
    ]
    app_names = {r["identity"]["id"]: r["identity"]["app"] for r in records}
    for c in sorted(captures, key=lambda x: (x["spec"]["app_id"], x["spec"]["url"])):
        aid = c["spec"]["app_id"]
        envs = ",".join(c["spec"]["environments"]) or "none"
        src_lines.append(
            f"| {aid} | {app_names[aid]} | `{c['spec']['kind']}` | `{envs}` | {c['line_count']} | "
            f"{c['captured_on']} | {c['spec']['url']} | `{c['content_sha256'][:12]}` |"
        )

    cap_keys = {(c["spec"]["app_id"], c["spec"]["url"]) for c in captures}
    failed_rows = []
    for r in records:
        aid = r["identity"]["id"]
        seen = set()
        for f in r["fetches"]:
            u = f["source_url"]
            if (aid, u) not in cap_keys and u not in seen:
                latest = [x for x in r["fetches"] if x["source_url"] == u][-1]
                seen.add(u)
                failed_rows.append((aid, app_names[aid], latest["status"], latest["http_status"], u, latest["error"]))

    src_lines += [
        "",
        "## Uncaptured / Failed Fetch Attempts (Network Runs)",
        "",
        "Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence.",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Concise Findings Matrix
    mat_lines = [
        "# Task 08: Findings Matrix (Support and Helpdesk, IDs 11–20)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        "- **Note**: Documentary observations and feasibility inferences only; no authenticated API/MCP calls or human checks were performed.",
        "",
        "| ID | App | One-Line Purpose | Auth Methods (Observed) | Testing Access | Production Access | API Surface & Breadth | MCP Discovery | Buildability (Inferred) | Key Cited Sources |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    def fmt_elig(env_obj):
        parts = []
        for k in ("free_access", "trial_access", "sandbox_access", "paid_required", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required", "self_serve"):
            c = env_obj[k]
            if c["status"] in ("observed", "inferred") and c["value"] is not None:
                short = k.replace("_access", "").replace("_required", "_req").replace("approval", "appr")
                parts.append(f"`{short}={str(c['value']).lower()}`")
        return ", ".join(parts) if parts else "`all unknown`"

    for r in records:
        aid = r["identity"]["id"]
        app = r["identity"]["app"]
        purp = r["purpose"]["value"]
        auths = ", ".join(f"`{a['value']['method']}` ({a['value']['context']})" for a in r["auth"]["items"])
        test_s = fmt_elig(r["credential_eligibility"]["testing"])
        prod_s = fmt_elig(r["credential_eligibility"]["production"])
        protos = ", ".join(f"`{x['value']}`" for x in r["api_surface"]["protocols"]["items"])
        br = r["api_surface"]["breadth"]["value"]
        api_s = f"{protos}; breadth=`{br}`"
        if r["mcp"]["discovery"]["status"] == "observed":
            mcp_s = "; ".join(f"`{e['value']['origin']}`: {e['value']['name']}" for e in r["mcp"]["entries"])
        else:
            mcp_s = f"`{r['mcp']['discovery']['status']}`"
        bld = f"`{r['buildability']['value']['verdict']}`"
        cited = sorted({ev["source_url"] for ev in (r["purpose"]["evidence"] + r["buildability"]["evidence"])})
        cite_s = "; ".join(cited[:3])
        mat_lines.append(
            f"| {aid} | **{app}** | {purp} | {auths} | {test_s} | {prod_s} | {api_s} | {mcp_s} | {bld} | {cite_s} |"
        )

    (OUT_DIR / "findings-matrix.md").write_text("\n".join(mat_lines) + "\n", encoding="utf-8")

    # 4. Batch Report (Coverage, Lineage, Validation, Reproduction)
    rec_sha = sha256_file(RUN_DIR / "records.json")
    seal_sha = sha256_file(RUN_DIR / "seal.json")
    rep_lines = [
        "# Task 08: Batch 2 Research Report (Support and Helpdesk, IDs 11–20)",
        "",
        "- **Date**: 2026-11-23",
        "- **Category**: Support and Helpdesk (`data/apps.json` IDs `11–20`)",
        f"- **Final Sealed Run ID**: `{RUN_ID}` (`work/research-runs/{RUN_ID}`)",
        f"- **Records SHA-256**: `{rec_sha}`",
        f"- **Seal SHA-256**: `{seal_sha}`",
        "- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`",
        "- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.",
        "",
        "## 1. Run Lineage & Validation Results",
        "",
        "| Run ID | Parent | Role | Status | Notes |",
        "| --- | --- | --- | --- | --- |",
        "| `task08-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |",
        "| `task08-capture-002` | `task08-capture-001` | Network capture recovery (v1) | Sealed (`37` captures) | Approved-network HTTP capture including 31,897-line `developers.freshdesk.com/api/` via `--max-bytes 10000000`. |",
        "| `task08-capture-003` | `task08-capture-002` | Expanded capture (v2) | Sealed (`54` captures) | Added Zendesk community MCP, Intercom OAuth, Front `.md` auth/MCP/Admin MCP, Pylon `.md` auth/API/MCP, LiveAgent MCP, Plain `developer.txt`, Gorgias OAuth/review/community MCP. |",
        "| `task08-capture-004` | `task08-capture-003` | Final capture (v3) | Sealed (`58` captures) | Added exact Plain GraphQL `introduction.md`, `authentication.md`, `oauth.md`, and `integrations/mcp-server.md`. |",
        "| `task08-first-pass-001` | `task08-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by JSON Schema validator (lowercase auth/protocol enums); preserved untouched. |",
        "| `task08-first-pass-002` | `task08-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer; superseded by `task08-first-pass-003` to tighten per-claim attachments/locators and downgrade `20.production.contact_sales_required` to `unknown`. |",
        f"| `{RUN_ID}` | `task08-capture-004` | **Final Task 08 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `11–20`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures; 4 `developer.helpscout.com` snapshots returned compressed binary bytes and were not cited); `{len(failed_rows)}` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)",
        f"- **Eligible Research Assertions (Frozen Inventory)**: `{metrics['overall']['eligible']}` total (`{metrics['by_basis']['observed']['eligible']}` observed documentary, `{metrics['by_basis']['inferred']['eligible']}` inferred; excludes 10 identity claims)",
        f"- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `{metrics['overall']['pending']}` pending, `accuracy: null`",
        "",
        "| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for area in ("identity", "purpose", "auth", "credentials", "api", "mcp", "buildability"):
        st = metrics["research_coverage"][area]["claim_status_counts"]
        rep_lines.append(
            f"| `{area}` | {st.get('observed',0)} | {st.get('inferred',0)} | {st.get('unknown',0)} | "
            f"{st.get('not_researched',0)} | {st.get('not_found_in_checked_sources',0)} | "
            f"{metrics['research_coverage'][area]['apps_with_assertions']}/10 |"
        )

    rep_lines += [
        "",
        "## 3. Pilot Continuity & Integrity Verification",
        "",
        "- **Freshdesk (ID 13) Pilot Provenance**: Freshdesk was previously researched in `work/task-04-runs/pilot-first-pass-001` and verified `20/20` in `task05-review-002`, with one disclosed capture gap: `developers.freshdesk.com/api/` failed under the v0.1.0 2 MB cap. Using pipeline v0.2.0 (`--max-bytes 10000000`), Task 08 freshly captured all 5 pilot URLs plus `developers.freshdesk.com/api/` (31,897 lines) and `www.freshworks.com/freshdesk/pricing/`, directly grounding Freshdesk's HTTP Basic (`apikey:X`) wire format, plan-tiered rate limits, and GA MCP allowances. Original Task 04/05 sealed runs remain byte-for-byte unchanged.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Support and Helpdesk were researched to the same documentary standard.",
        "- **Baseline Hash Verification**: `pilot-first-pass-001` (`records.json` & `seal.json`), `task05-review-002` (`seal.json`), `outputs/task-06/sampling-manifest.json`, `data/apps.json`, and `task07-first-pass-003` (`records.json` & `seal.json`) all verified byte-for-byte unchanged.",
        "",
        "## 4. Reproduction Instructions",
        "",
        "Offline validation and metrics replay (no network or API keys required):",
        "",
        "```powershell",
        f".venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs validate --run-id {RUN_ID}",
        f".venv\\Scripts\\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id {RUN_ID} --target {RUN_ID}",
        "```",
        "",
        "Rebuild extraction JSON from sealed capture `task08-capture-004`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-08-agent/build_extraction.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 08: Exceptions List for Independent Reviewer",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (Support and Helpdesk, IDs 11–20). No correctness judgments are made here.",
        "",
        "1. **Help Scout (ID 18) — Compressed Binary Responses on `developer.helpscout.com` & MCP Blog 404**:",
        "   - All four `developer.helpscout.com` URLs (`/`, `/mailbox-api/`, `/mailbox-api/overview/authentication/`, `/docs-api/`) returned HTTP `200` with compressed binary payloads that `research_pipeline.py`'s `urllib` collector did not decompress, yielding unreadable snapshots. None of those 4 snapshots are cited in any claim.",
        "   - `www.helpscout.com/blog/mcp-server/` returned HTTP `404`. Consequently, only readable `www.helpscout.com/pricing/` evidence is cited (`18.identity`, `18.purpose`, `18.auth.oauth_apps`, `18.api.protocol.api_access`, pricing/trial eligibility, and `conditional` buildability), while `api.public_docs`, `resource_groups`, `api.breadth`, and `mcp.discovery` remain `unknown`. This is a collector/content-encoding limitation to flag for future pipeline handling.",
        "2. **Zendesk (ID 11) — Official MCP Client Article 404 & Community MCP Server Scope**:",
        "   - `support.zendesk.com/hc/en-us/articles/8244243105178-...` (Zendesk MCP client) returned HTTP `404` and `4408828617370-Testing-changes-in-your-sandbox` returned a 14-line shell. Zendesk's sandbox availability is cited from `www.zendesk.com/pricing/` (Suite Enterprise + Copilot), and MCP discovery cites community repo `github.com/reminia/zendesk-mcp-server` (`origin: community`, not vendor-endorsed). No official Zendesk MCP server claim was promoted.",
        "3. **Intercom (ID 12) — Vendor App Store Review vs. Private Self-Serve Scope**:",
        "   - `12.production.vendor_approval_required=true` (contract v1.1) applies specifically to public multi-tenant OAuth apps submitted to the Intercom App Store, whereas private workspace Access Token apps are self-serve without review (`12.production.self_serve=true`). Reviewer should verify this dual-path scope clarity.",
        "4. **Freshdesk (ID 13) — Pilot Refresh & Tenant-Templated MCP URL**:",
        "   - Resolves the Task 04 pilot capture gap by capturing `developers.freshdesk.com/api/` (31,897 lines) under `--max-bytes 10000000`. Because the official Freshdesk MCP endpoint is tenant-templated (`https://<subdomain>.freshdesk.com/mcp`), `server_url` is set to `null` (to satisfy strict URI format validation) with the exact template documented in `scope`.",
        "5. **Front (ID 14) — Dual Official MCP Servers & No DCR**:",
        "   - Records two distinct official hosted MCP servers (`https://mcp.frontapp.com/mcp` for user-scoped conversations and `https://mcp.frontapp.com/admin-mcp` open beta for admin configuration), both requiring confidential OAuth 2.1 + PKCE (no Dynamic Client Registration).",
        "6. **Pylon (ID 15) — No Public Free Trial / Self-Serve Checkout Captured**:",
        "   - `usepylon.com/pricing` lists annual per-seat contracts ($89/$139/Enterprise) without a public free tier or cardless trial CTA; testing `free_access` / `trial_access` / `self_serve` remain `unknown`, leading to `conditional` buildability.",
        "7. **LiveAgent (ID 16) — `liveagent.com/api/` 404 & v1 vs. Tenant-Hosted v3 Docs**:",
        "   - `www.liveagent.com/api/` returned HTTP `404`. The captured `support.liveagent.com/061754-Complete-API-reference` reflects REST API v1 PHP examples (`narrow` breadth from captured public text), while LiveAgent's v3 Swagger/OpenAPI reference is tenant-hosted. Built-in MCP server (`https://<your-liveagent-domain>/api/mcp`) is captured from `support.liveagent.com/647358-MCP-Integration-for-Agents` with `server_url: null` (tenant-templated).",
        "8. **Gorgias (ID 19) — Partner Approval for Sandbox/OAuth & Community MCP Only**:",
        "   - `19.testing.partner_approval_required=true` and `19.production.partner_approval_required=true` reflect explicit `techpartners@gorgias.com` Sandbox conversion and tech partnership team review. MCP records community repo `github.com/mattcoatsworth/Gorgias-MCP-Server` (`origin: community`); no official Gorgias MCP doc was captured in `developers.gorgias.com/llms.txt`.",
        "9. **Gladly (ID 20) — Help Subpage 404s & Bounded MCP Not Found**:",
        "   - `developer.gladly.com/lookup/` and two `help.gladly.com` articles returned HTTP `404`, but the 5,595-line `developer.gladly.com/rest/` ReDoc snapshot fully documents REST API, Lookup API, `.gladly.qa` sandbox, and Admin-gated API User Basic auth. `20.mcp` is `not_found_in_checked_sources` (bounded to checked Gladly docs; does not prove no MCP exists).",
        "10. **Operational Checks Unresearched**:",
        "   - All 9 nested MCP `operational_check` claims across IDs 11–20 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 7 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
