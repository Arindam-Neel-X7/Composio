"""Generate outputs/task-07/ deliverables and run integrity verification."""
import hashlib
import json
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task07-first-pass-003"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-07"
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
    assert ids == list(range(1, 11)), f"Unexpected IDs: {ids}"
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

    # Verify sealed Task 04/05/06 baselines untouched
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
    }
    for label, (path, expected) in baseline_checks.items():
        actual = sha256_file(path)
        assert actual == expected, f"Baseline modified: {label} ({actual} != {expected})"

    # 2. Source Index
    src_lines = [
        "# Task 07: Source Index (CRM and Sales, IDs 1–10)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`)",
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

    # Failed / uncaptured URLs (excluding sandbox DNS errors from capture-001)
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
        "# Task 07: Findings Matrix (CRM and Sales, IDs 1–10)",
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
        "# Task 07: Batch 1 Research Report (CRM and Sales, IDs 1–10)",
        "",
        "- **Date**: 2026-11-23",
        "- **Category**: CRM and Sales (`data/apps.json` IDs `1–10`)",
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
        "| `task07-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |",
        "| `task07-capture-002` | `task07-capture-001` | Network capture recovery (v1) | Sealed (`32` captures) | Approved-network HTTP capture of initial 39 public URLs. |",
        "| `task07-capture-003` | `task07-capture-002` | Expanded capture (v2) | Sealed (`53` captures) | Added Trailhead/forcedotcom, HubSpot OAuth, Pipedrive `.md`, Attio/Close/Twenty `llms.txt`, Zoho v8, Copper auth, DealCloud MCP. |",
        "| `task07-capture-004` | `task07-capture-003` | Final capture (v3) | Sealed (`58` captures) | Added exact Attio OAuth/MCP `.md` and Close OAuth/MCP `.md` pages discovered from `llms.txt`. |",
        "| `task07-first-pass-001` | `task07-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by validator (`MCP scope must explicitly identify callable server direction`); preserved untouched. |",
        "| `task07-first-pass-002` | `task07-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer; superseded by `task07-first-pass-003` to tighten claim-level citations/locators and null Zoho `server_url`. |",
        f"| `{RUN_ID}` | `task07-capture-004` | **Final Task 07 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `1–10`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures); `{len(failed_rows)}` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)",
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
        "- **HubSpot (ID 2) Pilot Provenance**: HubSpot was previously researched in `work/task-04-runs/pilot-first-pass-001` and verified `22/22` in `task05-review-002` with a Task 05 caveat that `2.production.*` relied on sunset legacy private apps (new creation ended 2026-10-26). In Task 07, all 5 HubSpot pilot URLs were freshly captured on `2026-11-23` alongside `working-with-oauth`, so `2.production.admin_approval_required` now cites current OAuth installation requirements (Super Admin or HubSpot Marketplace Access) in addition to legacy private apps, while `2.production.free_access` / `paid_required` remain explicitly scoped to existing legacy private apps. Original Task 04/05 sealed runs remain byte-for-byte unchanged.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps (including sampled IDs `4 Attio` and `8 Close`) were researched to the same documentary standard.",
        "- **Baseline Hash Verification**: `pilot-first-pass-001` (`records.json` & `seal.json`), `task05-review-002` (`seal.json`), `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.",
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
        "Rebuild extraction JSON from sealed capture `task07-capture-004`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-07-agent/build_extraction.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 07: Exceptions List for Independent Reviewer",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (CRM and Sales, IDs 1–10). No correctness judgments are made here.",
        "",
        "1. **Salesforce (ID 1) — HTTP 403 Bot-Block on `developer.salesforce.com` & Local MCP EOL**:",
        "   - Five `developer.salesforce.com` / `salesforce.com/form/developer-signup/` URLs returned HTTP `403` (`blocked`), and `help.salesforce.com` returned a 5-line JS loading shell. Consequently, Salesforce OAuth 2.0 Connected App / External Client App flows and exact edition-level API gating (e.g., Professional add-on vs. Enterprise/Developer Edition) could not be cited from captured primary docs and remain `unknown`.",
        "   - Captured `github.com/salesforcecli/mcp` documents that the official local Salesforce DX MCP server (`@salesforce/mcp`) reached **End of Life on November 2, 2026**; Salesforce hosted MCP server documentation was not capturable due to the `developer.salesforce.com` 403.",
        "2. **HubSpot (ID 2) — Pricing JS Shell & Legacy Private App Sunset**:",
        "   - `www.hubspot.com/pricing/crm` returned a 1-line JS shell (`Free Tools | HubSpot`). `2.production.admin_approval_required` is now grounded in current `working-with-oauth` (Super Admin / Marketplace Access) plus legacy private apps, while `2.production.free_access` and `2.production.paid_required` remain explicitly scoped to existing legacy private apps (new creation ended 2026-10-26).",
        "3. **Pipedrive (ID 3) — Pricing HTTP 403 & Native MCP Doc Not Captured**:",
        "   - `www.pipedrive.com/en/pricing` returned HTTP `403` (`blocked`), so production paid/free tier thresholds remain `unknown`.",
        "   - Community MCP repository `github.com/Wirasm/pipedrive-mcp` was captured (`origin: community`). Although search leads indicate a native Pipedrive MCP connector, no primary vendor MCP doc URL was captured in `task07-capture-004`, so no official Pipedrive MCP claim was promoted.",
        "4. **Twenty (ID 5) — Community MCP Only & Self-Hosted vs. Cloud Scope**:",
        "   - `github.com/jezweb/twenty-mcp` (`origin: community`) is recorded for MCP; no official Twenty MCP doc page was captured in `task07-capture-004`.",
        "   - Production `free_access=true` / `paid_required=false` explicitly reflect open-source self-hosting (`github.com/twentyhq/twenty`), whereas Twenty Cloud production plans are paid (Pro `$9/user/mo+`). Reviewer should verify scope clarity.",
        "5. **Podio (ID 6) — Bounded MCP Not Found**:",
        "   - `6.mcp` is `not_found_in_checked_sources` across official Podio developer/pricing docs; reviewer should confirm this bounded negative is not over-claimed as universal absence.",
        "6. **Zoho CRM (ID 7) — Sandbox KB Capture Failure**:",
        "   - `help.zoho.com/.../sandbox-overview` failed with `Capture failed: empty_readable_content`, so `7.testing.sandbox_access` remains `unknown` (testing is supported via Free Edition and paid-edition trials).",
        "7. **Close (ID 8) — Paid Production & Vendor Public-OAuth Approval**:",
        "   - `8.production.vendor_approval_required=true` uses the new v1.1 field for Close's public OAuth app publication process (`create-an-oauth-app.md` lines 20–21: private by default; making public requires requesting publication). Reviewer should verify this distinction against `partner_approval_required`.",
        "8. **Copper (ID 9) — OAuth & MCP Blog 404s**:",
        "   - `developer.copper.com/oauth/overview.html` and `www.copper.com/blog/copper-mcp-server` returned HTTP `404`. OAuth 2.0 existence is confirmed from `introduction/authentication.html`, while `9.mcp` remains `not_found_in_checked_sources`.",
        "9. **DealCloud (ID 10) — REST Auth Subpage 404s & Enterprise Gating**:",
        "   - `api.docs.dealcloud.com` REST `api-keys` and `authorization-token` subpages returned HTTP `404`, so REST token-exchange details remain `unknown` while MCP OAuth 2.0 (`.well-known` discovery, user-scoped permissions, Celeste license + admin capability) is observed from `mcp/getting-started` and `mcp/authentication`.",
        "10. **Operational Checks Unresearched**:",
        "   - All 8 nested MCP `operational_check` claims remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 5 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
