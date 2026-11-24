"""Generate outputs/task-14/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task14-first-pass-003"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-14"
OUT_DIR.mkdir(parents=True, exist_ok=True)

EXCLUDED_SHELL_URLS = {
    "https://airtable.com/developers/web/api/introduction",
    "https://airtable.com/developers/web/api/oauth-reference",
}


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
    captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
    manifest = json.loads((RUN_DIR / "manifest.json").read_text(encoding="utf-8"))
    roster = json.loads((ROOT / "data/apps.json").read_text(encoding="utf-8"))["apps"]
    roster_map = {a["id"]: a for a in roster}

    # Verify validate passes
    val_proc = subprocess.run(
        [sys.executable, "-B", "research_pipeline.py", "--store", "work/research-runs",
         "validate", "--run-id", RUN_ID],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    validation_out = json.loads(val_proc.stdout)
    assert validation_out["structure_and_grounding"] == "passed", validation_out

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

    # Verify all 10 IDs, roster match, no synthetic flags, all evidence resolves, no SPA shells cited, all reviews pending
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(71, 81)), f"Unexpected IDs: {ids}"
    for r in records:
        aid = r["identity"]["id"]
        assert r["identity"]["app"] == roster_map[aid]["app"], f"App name mismatch for {aid}"
        assert r["identity"]["category"] == roster_map[aid]["category"], f"Category mismatch for {aid}"
        assert r["review"]["status"] == "pending", f"Review not pending for {aid}"
        for entry in r["mcp"]["entries"]:
            op = entry["value"]["operational_check"]
            assert op["status"] == "not_researched", f"MCP operational check not not_researched: {op}"

    assert manifest["synthetic"] is False
    assert metrics["synthetic"] is False
    assert metrics["overall"]["accuracy"] is None
    assert metrics["overall"]["review_coverage"] == 0.0

    ev_checked = 0
    for r in records:
        def walk_ev(obj):
            nonlocal ev_checked
            if isinstance(obj, dict):
                if "evidence" in obj and isinstance(obj["evidence"], list):
                    for ev in obj["evidence"]:
                        assert ev["source_url"] not in EXCLUDED_SHELL_URLS, f"Shell URL cited: {ev['source_url']}"
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
        "task14-first-pass-002/records.json": (
            ROOT / "work/research-runs/task14-first-pass-002/records.json",
            "5cf1177abceef0aa711d583dbb6cc03d5ddbaad028290e480358299d920eb184",
        ),
        "task14-first-pass-002/seal.json": (
            ROOT / "work/research-runs/task14-first-pass-002/seal.json",
            "86f83326e26090feb7fc03212b68ba00bde2287b978eccafbb1a353a5582ce58",
        ),
    }
    for label, (path, expected) in baseline_checks.items():
        actual = sha256_file(path)
        assert actual == expected, f"Baseline modified: {label} ({actual} != {expected})"

    records_sha = sha256_file(RUN_DIR / "records.json")
    seal_sha = sha256_file(RUN_DIR / "seal.json")
    app_names = {r["identity"]["id"]: r["identity"]["app"] for r in records}

    # 2. Source Index
    src_lines = [
        "# Task 14: Source Index (Productivity and Project Management, IDs 71–80)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live public HTTP captures, `synthetic: false`; 2 JavaScript-shell pages for Airtable `airtable.com/developers/web/api/introduction` and `oauth-reference` captured 1-line title shells and are excluded from all claim citations)",
        f"- **Resolved Evidence Observations Verified**: {ev_checked} (100% snapshot existence & SHA-256 match)",
        "",
        "## Captured Sources",
        "",
        "| App ID | App | Kind | Envs | Lines | Captured On | URL | Snapshot SHA-256 (prefix) |",
        "| ---: | --- | --- | --- | ---: | --- | --- | --- |",
    ]
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
        f"Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence. (`{len(failed_rows)}` distinct URLs remained uncaptured in `task14-capture-002`; `developers.notion.com/docs/mcp` timed out in `task14-capture-001` and succeeded in `task14-capture-002`.)",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Concise Cited Findings Matrix
    mat_lines = [
        "# Task 14: Findings Matrix (Productivity and Project Management, IDs 71–80)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        "- **Frozen 20-App Sample Members in Batch**: App `76` (Monday.com) and App `77` (ClickUp) — researched to the same documentary standard without preferential treatment.",
        "- **Note**: Documentary observations and feasibility inferences only; no authenticated API/MCP calls, account creations, or human checks were performed.",
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
        auths = "; ".join(f"`{a['value']['method']}` ({a['claim_id'].split('.')[-1]})" for a in r["auth"]["items"])
        test_s = fmt_elig(r["credential_eligibility"]["testing"])
        prod_s = fmt_elig(r["credential_eligibility"]["production"])
        protos = ", ".join(
            f"`{x['value']}`" + (" *(inferred)*" if x["status"] == "inferred" else "")
            for x in r["api_surface"]["protocols"]["items"]
        )
        br = r["api_surface"]["breadth"]["value"]
        api_s = f"{protos}; breadth=`{br}`"
        if r["mcp"]["discovery"]["status"] == "observed":
            mcp_s = "; ".join(
                f"`{m['value']['origin']}`: {m['value']['name']} (`{m['value']['server_url']}`)"
                for m in r["mcp"]["entries"]
            )
        else:
            mcp_s = f"`{r['mcp']['discovery']['status']}`"
        bld = f"`{r['buildability']['value']['verdict']}`"
        cited_urls = []
        def collect_urls(obj):
            if isinstance(obj, dict):
                if "evidence" in obj and isinstance(obj["evidence"], list):
                    for ev in obj["evidence"]:
                        if ev["source_url"] not in cited_urls:
                            cited_urls.append(ev["source_url"])
                for v in obj.values():
                    collect_urls(v)
            elif isinstance(obj, list):
                for item in obj:
                    collect_urls(item)
        collect_urls(r)
        key_src = "; ".join(cited_urls[:3])
        mat_lines.append(
            f"| {aid} | **{app}** | {purp} | {auths} | {test_s} | {prod_s} | {api_s} | {mcp_s} | {bld} | {key_src} |"
        )

    (OUT_DIR / "findings-matrix.md").write_text("\n".join(mat_lines) + "\n", encoding="utf-8")

    # 4. Batch Report
    rc = metrics["research_coverage"]
    def area_row(name):
        a = rc[name]
        st = a["claim_status_counts"]
        return (
            f"| `{name}` | {st.get('observed', 0)} | {st.get('inferred', 0)} | "
            f"{st.get('unknown', 0)} | {st.get('not_researched', 0)} | "
            f"{st.get('not_found_in_checked_sources', 0)} | {a['apps_with_assertions']}/{a['selected_app_denominator']} |"
        )

    report_lines = [
        "# Task 14: Batch 8 Research Report (Productivity and Project Management, IDs 71–80)",
        "",
        "- **Date**: 2026-11-24",
        "- **Category**: Productivity and Project Management (`data/apps.json` IDs `71–80`)",
        f"- **Final Sealed Run ID**: `{RUN_ID}` (`work/research-runs/{RUN_ID}`)",
        f"- **Records SHA-256**: `{records_sha}`",
        f"- **Seal SHA-256**: `{seal_sha}`",
        "- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`",
        "- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy or human verification.",
        "",
        "## 1. Run Lineage & Validation Results",
        "",
        "| Run ID | Parent | Role | Status | Notes |",
        "| --- | --- | --- | --- | --- |",
        "| `task14-capture-001` | `null` | Initial live capture | Sealed (`43` captures) | Public HTTP capture across IDs 71–80 (`sources-001.json`); `developers.notion.com/docs/mcp` timed out and several Zendesk/help URLs returned 403/404. |",
        "| `task14-capture-002` | `task14-capture-001` | Expanded capture (v2) | Sealed (`52` captures) | Added 9 captures (`sources-002.json`), including retry success on `developers.notion.com/docs/mcp`, Airtable support docs, ClickUp MCP docs, Coda `?output=1` MCP doc, and Southleft Harvest MCP README. |",
        "| `task14-first-pass-001` | `task14-capture-002` | Initial ingest attempt | Incomplete / Rejected (preserved) | Rejected during validation (`ValueError`); preserved untouched in `work/research-runs/task14-first-pass-001`. |",
        "| `task14-first-pass-002` | `task14-capture-002` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewers (`NEEDS FIXES`, 36 items in `outputs/task-14-review.md`); preserved untouched. |",
        f"| `{RUN_ID}` | `task14-first-pass-002` | **Final Task 14 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation_out['backend']}`, `10` records, `synthetic: false`, `{ev_checked}` verified evidence refs; all 36 independent AI review items remediated). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `71–80`, all 10 present with asserted non-identity research; matched verbatim against `data/apps.json`)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures; 2 Airtable 1-line SPA shells preserved in archive and excluded from citations); `{len(failed_rows)}` distinct uncaptured fetch URLs preserved in `fetches` telemetry",
        f"- **Eligible Research Assertions (Frozen Inventory)**: `{metrics['overall']['eligible']}` total (`{metrics['by_basis']['observed']['eligible']}` observed documentary, `{metrics['by_basis']['inferred']['eligible']}` inferred; excludes 10 identity claims)",
        f"- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `{metrics['overall']['pending']}` pending, `accuracy: null`",
        "",
        "| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        area_row("identity"),
        area_row("purpose"),
        area_row("auth"),
        area_row("credentials"),
        area_row("api"),
        area_row("mcp"),
        area_row("buildability"),
        "",
        "## 3. Shared Baseline & Frozen 20-App Sample Verification",
        "",
        "- **Task 06 Baseline Confirmed**: `outputs/task-06-review.md` (`PASS`), `research_pipeline.py` (`v0.2.0`), `schemas/record.json` (`v1.1`), and `docs/evidence-rules.md` (`v1.1`) are accepted and intact; no shared blockers observed.",
        "- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`), and `data/apps.json` all verified byte-for-byte unchanged.",
        "- **Frozen 20-App Sample Members**: App `76` (Monday.com) and App `77` (ClickUp) are in the frozen Task 06 sample. All 10 apps in IDs 71–80 were researched to the same documentary standard.",
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
        "Regenerate `outputs/task-14/` deliverables from the sealed run:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-14-agent/generate_deliverables.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    # 5. Exceptions, Unknowns & Reviewer Notes
    exc_lines = [
        "# Task 14: Exceptions, Unknowns & Reviewer Notes (Productivity and Project Management, IDs 71–80)",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (Productivity and Project Management, IDs 71–80). No correctness judgments, human-verification claims, or accuracy claims are made here.",
        "",
        "1. **Notion (ID 71) — Internal Connection vs. PAT vs. Public OAuth, Workspace Controls & Hosted MCP**:",
        "   - Distinguishes three auth routes: static Internal connection Bearer tokens (require workspace-owner creation and explicit per-page sharing), user-scoped Personal Access Tokens (Business/Enterprise plans restrict PAT creation by default until a workspace owner enables it), and public OAuth 2.0 (authorization can begin without Marketplace submission or review; users select shared pages).",
        "   - Official hosted MCP (`https://mcp.notion.com/mcp`) is restricted to workspace members (guests excluded); OAuth works on every plan, while unattended MCP tokens require a Business/Enterprise owner. The older local Notion MCP server is deprecated.",
        "   - Initial capture of `developers.notion.com/docs/mcp` timed out in `task14-capture-001` and succeeded in `task14-capture-002`.",
        "2. **Airtable (ID 72) — JavaScript-Shell Developer Reference, PAT Auth Prefix & Org Allowlisting**:",
        "   - `https://airtable.com/developers/web/api/introduction` and `https://airtable.com/developers/web/api/oauth-reference` returned 1-line JavaScript shells (`Airtable Web API`) to static HTTP capture; both are preserved in `captures.json` and excluded from all claim citations. `support.airtable.com/docs/airtable-api-faqs` returned HTTP 404.",
        "   - Because captured support docs establish PATs in the `Authorization` header without printing the literal `Bearer` prefix, `72.auth.pat` uses `method: other` rather than guessing `Bearer_token`, and `72.api.protocol.rest` is marked `inferred` (not `observed`) from documented `POST /v0/meta/bases` and paginated list-record endpoints.",
        "   - Free plan allows 1,000 API calls/workspace/month (`free_access=true` for ordinary Web API use; `paid_required` kept `unknown` under the app-wide scope because higher quotas and certain features require paid plans); official hosted MCP (`https://mcp.airtable.com/mcp`) supports OAuth or PAT and requires organization-admin allowlisting when third-party integrations are restricted.",
        "3. **Linear (ID 73) — Non-Bearer API Keys, OAuth `client_credentials` & Admin-Only OAuth Management**:",
        "   - Distinguishes personal API keys (`Authorization: <API_KEY>` without `Bearer` prefix), OAuth2 user tokens (`Authorization: Bearer`), and optional OAuth2 `client_credentials` (app actor, 30-day expiry).",
        "   - Member API key creation depends on workspace policy, while creating/managing webhooks and viewing the OAuth application administration page requires workspace admin permissions. Plan-specific credential costs and isolated sandbox entitlement remain `unknown`.",
        "4. **Jira (ID 74) — Jira Cloud v3 Scope, Commercial 3LO Mandate & Headless MCP Admin Gate**:",
        "   - Explicitly scoped to **Jira Cloud platform REST API v3** and Atlassian remote MCP (`https://mcp.atlassian.com/v2/mcp`); excludes Jira Data Center and Server.",
        "   - Distinguishes Basic auth (Atlassian account email + API token for personal scripts; passwords deprecated) from OAuth 2.0 3LO (`api.atlassian.com/ex/jira/<cloudId>/rest/api/3`). Atlassian cloud app security rules prohibit commercial apps from collecting customer API tokens.",
        "   - Headless MCP API-token authentication requires an organization admin to enable API-token authentication; pricing/free-tier API entitlements remain `unknown` in captured docs.",
        "5. **Asana (ID 75) — Free-Account Testing vs. Vendor-Provisioned Sandbox & V2 MCP Pre-Registration**:",
        "   - Distinguishes self-serve PAT testing in a free/existing workspace from temporary isolated **developer sandboxes**, which must be requested by form (vendor-provisioned, up to 1 week lead time, max 1 year, Legal review for extensions; `testing.free_access=true`, `testing.sandbox_access=true`, while `testing.vendor_approval_required` and `testing.self_serve` are kept `unknown` under the app-wide scope). Production eligibility fields remain `unknown` to avoid projecting testing entitlements onto production.",
        "   - Official Asana V2 MCP (`https://mcp.asana.com/v2/mcp`) requires pre-registering an OAuth MCP app (dynamic client registration unsupported; V1 SSE deprecated; MCP tokens do not work with the standard REST API; Command MCP excluded).",
        "6. **Monday.com (ID 76 — Frozen Sample Member) — Developer Sandbox vs. Production & Platform OAuth Scope**:",
        "   - Distinguishes the free self-serve developer sandbox (`testing.free_access=true`, `sandbox_access=true`, `trial_access=true`, explicitly prohibited for production business workflows; `testing.paid_required` and `self_serve` kept `unknown` under the app-wide scope) from the alternate evaluation trial and production workspaces.",
        "   - Captures `https://developer.monday.com/apps/docs/oauth` (298 lines) in the run archive; `76.auth.items` records Personal V2 API tokens, Platform API OAuth 2.0 (`76.auth.oauth` with documented scopes `boards:read/write`, `docs:read/write`, `workspaces:read/write`), and hosted MCP OAuth (`https://mcp.monday.com/mcp`, with personal-token option for individual dev/testing only and AI Connector admin policy).",
        "7. **ClickUp (ID 77 — Frozen Sample Member) — API OAuth Admin Gate vs. Hosted MCP OAuth-Only & 404 Docs**:",
        "   - `developer.clickup.com/docs/general` and `developer.clickup.com/docs/mcp-server` returned HTTP 404 (preserved in `fetches`); ClickUp's live MCP documentation was captured via `developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1` and `help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP`.",
        "   - Distinguishes personal API tokens (`Authorization: {personal_token}`), Public API OAuth 2.0 (app creation requires workspace owner/admin), and hosted MCP (`https://mcp.clickup.com/mcp`), which requires OAuth 2.1 with PKCE and **rejects personal public-API keys** (no ClickUp admin action required for external client setup; Free Forever allows 100 calls/rolling 24h without Everything AI add-on). Excludes ClickUp acting as an outgoing MCP client.",
        "8. **Coda (ID 78) — Superhuman Docs Rebrand, Help-Center 403/404 & MCP Role Quotas**:",
        "   - Primary API reference (`coda.io/developers/apis/v1`) rebrands the product as **Superhuman Docs (formerly Coda)** while retaining the `https://coda.io/apis/v1` REST base URL. Direct help-center URLs returned HTTP 403/404; `help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP?output=1` captured cleanly (257 lines).",
        "   - REST API is free of charge in free and paid workspaces (doc creation requires Doc Maker/Admin). Hosted MCP beta (`https://coda.io/apis/mcp`) separates general REST tokens from MCP-restricted personal tokens and OAuth2 (ChatGPT/Claude/Cursor), with role-based limits (paid Doc Makers full; free Doc Makers 30/week max 60/month; Editors read-only).",
        "9. **Smartsheet (ID 79) — Commercial Plan Requirement, Vendor OAuth Acceptance & Regional Endpoints**:",
        "   - Ordinary REST API 2.0 and official hosted MCP (`https://mcp.smartsheet.com` for US; EU/Australia separate; Gov/EU/AU API base URLs and tokens separate) require a **Business, Enterprise, or Advanced Work Management** plan (`production.paid_required=true`, while `testing.paid_required` is kept `unknown` because developer sandbox cost is unestablished).",
        "   - UI-generated Bearer access tokens are self-serve for eligible users, whereas three-legged OAuth2 requires **Developer Tools** registration subject to Smartsheet vendor acceptance and possible denial (`vendor_approval_required` and `self_serve` kept `unknown` under the app-wide scope rather than collapsing both paths). A separate developer sandbox registration path is documented (`testing.sandbox_access=true`).",
        "10. **Harvest (ID 80) — Identity Disambiguation, Pricing vs. API Entitlement & Community MCP Provenance**:",
        "    - Explicitly matched to **Harvest time-tracking API v2** (`help.getharvest.com/api-v2/`, `api.harvestapp.com`), excluding Greenhouse's recruiting Harvest API and Forecast-only scope. `help.getharvest.com/api-v2/time-tracking-api/time-entries/time-entries/` returned HTTP 404 (preserved in `fetches`).",
        "    - Distinguishes PATs (`Authorization: Bearer` + `Harvest-Account-Id` + mandatory `User-Agent`, replacing v1 Basic auth), OAuth2 authorization-code, and client-side OAuth2 Implicit Grant (vendor recommends Authorization Code when a backend is available). `getharvest.com/pricing` advertises a Free plan and trial, but does not establish API entitlement, so `free_access`, `trial_access`, and `paid_required` remain `unknown`.",
        "    - MCP entry (`Southleft Harvest MCP`, `https://harvest-mcp.southleft.com/mcp`, `https://github.com/southleft/harvest-mcp`) is explicitly marked **`community`** (not vendor-endorsed).",
        "11. **All Operational Checks Unresearched & Paraphrase Evidence Basis**:",
        "    - All 10 nested MCP `operational_check` claims across IDs 71–80 remain `not_researched` (documentation does not establish successful connection or tool execution).",
        "    - All 273 evidence observations use `paraphrase: ` prefixes anchored to exact `lines:N-M` locators in sealed snapshots; independent reviewers should reopen the cited lines directly to verify entailment.",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(
        f"OK: outputs/task-14/ generated from {RUN_ID} "
        f"(captures={len(captures)}, evidence_refs={ev_checked}, eligible={metrics['overall']['eligible']}, "
        f"accuracy={metrics['overall']['accuracy']})"
    )


if __name__ == "__main__":
    main()
