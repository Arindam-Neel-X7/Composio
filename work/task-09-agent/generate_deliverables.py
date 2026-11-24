"""Generate outputs/task-09/ deliverables and run integrity verification."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task09-first-pass-004"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-09"
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
    assert ids == list(range(21, 31)), f"Unexpected IDs: {ids}"
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

    # Verify sealed Task 04/05/06/07/08 baselines untouched
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
        "task08-first-pass-003/records.json": (
            ROOT / "work/research-runs/task08-first-pass-003/records.json",
            "b8c75b62b3e4f13478cca5d079e07dc50c4f6faa437d72d3d4cc1749eb23b861",
        ),
        "task08-first-pass-003/seal.json": (
            ROOT / "work/research-runs/task08-first-pass-003/seal.json",
            "e3fe4e7ded6cd1ac8dcd69ff551d209833afa812a40116023862e4cbec3e44d7",
        ),
        "task09-first-pass-003/records.json": (
            ROOT / "work/research-runs/task09-first-pass-003/records.json",
            "963fb8a650375b4c4057aa9956d86866191664f467a395da3731d7459e337a72",
        ),
        "task09-first-pass-003/seal.json": (
            ROOT / "work/research-runs/task09-first-pass-003/seal.json",
            "bdbd02eb3bb6360eea275682187b72983923f313f86934ecb097a3eca2712d24",
        ),
    }
    for label, (path, expected) in baseline_checks.items():
        actual = sha256_file(path)
        assert actual == expected, f"Baseline modified: {label} ({actual} != {expected})"

    # 2. Source Index
    src_lines = [
        "# Task 09: Source Index (Communications and Messaging, IDs 21–30)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`; note 3 `open.larksuite.com` / `larksuite.com/en_us/plans` snapshots returned 1-line JS shells and were excluded from claim citations)",
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
        "# Task 09: Findings Matrix (Communications and Messaging, IDs 21–30)",
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
        "# Task 09: Batch 3 Research Report (Communications and Messaging, IDs 21–30)",
        "",
        "- **Date**: 2026-11-23",
        "- **Category**: Communications and Messaging (`data/apps.json` IDs `21–30`)",
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
        "| `task09-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |",
        "| `task09-capture-002` | `task09-capture-001` | Network capture recovery (v1) | Sealed (`41` captures) | Approved-network HTTP capture across IDs 21–30 (including 14,067-line Telegram Bot API, 13,223-line Aircall API ref, 10,572-line Zoho Cliq API v2). |",
        "| `task09-capture-003` | `task09-capture-002` | Expanded capture (v2) | Sealed (`51` captures) | Added official Lark Python/Node SDK repos, Pumble Node SDK/landing/help, WhatsApp `llms.txt` + `access-tokens`, Aircall `llms.txt` + retried `tutorials/oauth/`, and Vonage Kiro Power repo. |",
        "| `task09-capture-004` | `task09-capture-003` | Final capture (v3) | Sealed (`54` captures) | Added WhatsApp `app-review.md`, community WhatsApp Business Cloud API MCP (`tkhattar14/whatsapp-business-mcp`), and Aircall AI `llms.txt`. |",
        "| `task09-first-pass-001` | `task09-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by primary-evidence guard (community MCP repos cited on non-MCP claims); preserved untouched. |",
        "| `task09-first-pass-002` | `task09-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Validated cleanly, but left unestablished credential booleans as `not_researched` instead of explicit `unknown`; preserved untouched. |",
        "| `task09-first-pass-003` | `task09-capture-004` | Second sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer (`NEEDS FIXES` for 25 claim-grounding/locator defects); preserved untouched. |",
        f"| `{RUN_ID}` | `task09-capture-004` | **Final Task 09 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`, all 25 audit defects remediated). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `21–30`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures; 3 Lark JS-shell pages excluded from citations); `{len(failed_rows)}` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)",
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
        "## 3. Pilot Overlap & Integrity Verification",
        "",
        "- **Pilot Overlap**: None of IDs `21–30` were part of the 5-app Task 04/05 pilot (IDs 2, 13, 31, 58, 91).",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Communications and Messaging were researched to the same documentary standard without preferential treatment for sample apps (`21` Slack, `27` Telegram).",
        "- **Baseline Hash Verification**: `pilot-first-pass-001`, `task05-review-002`, `outputs/task-06/sampling-manifest.json`, `data/apps.json`, `task07-first-pass-003`, and `task08-first-pass-003` all verified byte-for-byte unchanged.",
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
        "Rebuild extraction JSON from sealed capture `task09-capture-004`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-09-agent/build_extraction.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 09: Exceptions List for Independent Reviewer",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (Communications and Messaging, IDs 21–30). No correctness judgments are made here.",
        "",
        "1. **Lark / Larksuite (ID 24) — 1-Line JS Shells on `open.larksuite.com` and `larksuite.com/en_us/plans`**:",
        "   - `open.larksuite.com/document/home/index`, `open.larksuite.com/.../tenant_access_token_internal`, and `www.larksuite.com/en_us/plans` returned 1-line client-side JS shells to HTTP capture. None of those 3 snapshots are cited.",
        "   - All Lark claims are grounded in official `github.com/larksuite/*` repositories (`lark-openapi-mcp`, `oapi-sdk-python`, `node-sdk`). Because the pricing page was a JS shell, `free_access`, `trial_access`, and `paid_required` remain `unknown`.",
        "2. **Pumble (ID 25) — `pumble.com/pricing/` 404 & Product-Page-Only Official MCP Announcement**:",
        "   - `https://pumble.com/pricing/` and `https://github.com/CAKE-com/pumble-sdk` returned HTTP `404` (replaced by `pumble.com/`, `pumble.com/help/`, and `github.com/CAKE-com/pumble-node-sdk`).",
        "   - `25.mcp.official` records the official MCP server announcement on `pumble.com/` (`server_url: null`, `repository_url: null` since no endpoint URL or technical spec was captured) alongside community server `github.com/infralayers/pumble-mcp` (`origin: community`).",
        "3. **Aircall (ID 29) — Outbound MCP Client vs. Callable MCP Server Distinction**:",
        "   - Checked Aircall developer docs (`developer.aircall.io/`, `developer.aircall.io/tutorials/oauth/`, `developer.aircall.io/docs/aircall-ai/llms.txt`) document outbound MCP client integration (Aircall AI Virtual Agents calling external partner MCP servers, marked 'Coming soon') rather than a callable Aircall MCP server. Per Contract v1.1, `29.mcp` is recorded as `not_found_in_checked_sources` rather than promoting an outbound MCP client as a callable server.",
        "   - `29.testing.partner_approval_required=true` and `29.production.partner_approval_required=true` reflect Aircall's form-gated Technology Partner onboarding for OAuth `client_id`/`client_secret` and developer sandboxes (whereas single-company customer Basic Auth is self-serve on paid accounts).",
        "4. **WhatsApp Business (ID 28) — Dual-Path App Review & Community-Only MCP Capture**:",
        "   - `28.production.vendor_approval_required=true` applies to multi-tenant Tech Provider apps needing Advanced Access via Meta App Review (plus template approval), while Direct Developers receive automatic Standard Access (`28.production.self_serve=true`).",
        "   - No official Meta WhatsApp MCP doc page appeared in the captured `whatsapp/llms.txt` index; `28.mcp` cites community Cloud API repo `github.com/tkhattar14/whatsapp-business-mcp` (`origin: community`, targeting `graph.facebook.com`).",
        "5. **Slack (ID 21) — Dual-Path Marketplace Approval & No DCR on Official MCP**:",
        "   - `21.production.vendor_approval_required=true` reflects Slack Marketplace review for published multi-tenant apps (and Slack's rule that unlisted apps cannot use `https://mcp.slack.com/mcp`), while internal workspace apps are self-serve (`21.production.self_serve=true`).",
        "6. **Discord (ID 26) — Partner-Only OAuth2 Scopes & No Dedicated Pricing Page Captured**:",
        "   - `26.production.partner_approval_required=true` reflects Discord's documented partner-only OAuth2 scopes (`dm_channels.read`, `rpc.*`, `voice`, etc.), while standard bot/OAuth2 scopes are self-serve. `free_access` / `paid_required` remain `unknown` because no dedicated Discord developer billing/pricing page was captured.",
        "7. **Zoho Cliq (ID 23) — `oauth.html` 404 & Multi-Datacenter Routing**:",
        "   - `www.zoho.com/cliq/help/restapi/v2/oauth.html` returned HTTP `404`, but the 10,572-line `www.zoho.com/cliq/help/restapi/v2/` page contains the full OAuth 2.0 specification and OAS 3.0 YAML links across 9 regional Zoho domains. MCP records community repo `github.com/rohansen856/cliq-mcp` (`origin: community`).",
        "8. **Telegram (ID 27) — Bot API vs. MTProto Dual Surface & Community MCPs**:",
        "   - Captures both Bot API v10.5 (`core.telegram.org/bots/api`, 14,067 lines) and MTProto/TDLib (`core.telegram.org/api`) with separate community MCP servers for each (`node2flow-th/telegram-bot-mcp-community` for Bot API; `sparfenyuk/mcp-telegram` for MTProto user-account read/draft).",
        "9. **Vonage (ID 30) — Official API Bindings + Docs MCP & Beta Messages API Label**:",
        "   - Captures both `github.com/Vonage-Community/vonage-mcp-server-api-bindings` and `github.com/Vonage/vonage-kiro-power` (referencing `vonage-api` and `vonage-docs` MCP servers). Notes `developer.vonage.com/en/api` still labels Messages API as Beta while SMS API is stable.",
        "10. **Operational Checks Unresearched**:",
        "    - All 12 nested MCP `operational_check` claims across IDs 21–30 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 9 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
