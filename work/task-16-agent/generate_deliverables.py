"""Generate outputs/task-16/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task16-first-pass-001"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-16"
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

    # Verify all 10 IDs, no synthetic flags, all evidence resolves, all reviews pending
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(91, 101)), f"Unexpected IDs: {ids}"
    assert manifest["synthetic"] is False
    assert metrics["synthetic"] is False
    assert metrics["overall"]["accuracy"] is None
    assert metrics["overall"]["review_coverage"] == 0.0

    ev_checked = 0
    for r in records:
        assert r["review"]["status"] == "pending", f"Review not pending for {r['identity']['id']}"
        for entry in r["mcp"]["entries"]:
            op = entry["value"]["operational_check"]
            assert op["status"] == "not_researched", f"MCP operational check not not_researched: {op}"

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

    records_sha = sha256_file(RUN_DIR / "records.json")
    seal_sha = sha256_file(RUN_DIR / "seal.json")
    app_names = {r["identity"]["id"]: r["identity"]["app"] for r in records}

    # 2. Source Index
    src_lines = [
        "# Task 16: Source Index (AI, Research and Media-native, IDs 91–100)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}` (parent `task16-capture-007`)",
        f"- **Captured Sources**: {len(captures)} live public HTTP snapshots (`synthetic: false`)",
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
        f"Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence. (`{len(failed_rows)}` uncaptured source URLs across capture history.)",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Cited Findings Matrix
    mat_lines = [
        "# Task 16: Findings Matrix (AI, Research and Media-native, IDs 91–100)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        "- **Frozen 20-App Sample Members in Batch**: App `97` (higgsfield) and App `98` (Mermaid CLI)",
        "- **Pilot Overlap in Batch**: App `91` (NotebookLM — original Task 04/05 pilot baseline `pilot-first-pass-001` and `task05-review-002` preserved untouched)",
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
            elif c["status"] == "not_applicable":
                short = k.replace("_access", "").replace("_required", "_req").replace("approval", "appr")
                parts.append(f"`{short}=n/a`")
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

    # 4. Batch Report
    rep_lines = [
        "# Task 16: Batch 10 Research Report (AI, Research and Media-native, IDs 91–100)",
        "",
        "- **Date**: 2026-11-23",
        "- **Category**: AI, Research and Media-native (`data/apps.json` IDs `91–100`)",
        f"- **Final Sealed Run ID**: `{RUN_ID}` (`work/research-runs/{RUN_ID}`)",
        f"- **Records SHA-256**: `{records_sha}`",
        f"- **Seal SHA-256**: `{seal_sha}`",
        "- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`",
        "- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.",
        "",
        "## 1. Run Lineage & Validation Results",
        "",
        "| Run ID | Parent | Role | Status | Notes |",
        "| --- | --- | --- | --- | --- |",
        "| `task16-capture-001` .. `task16-capture-007` | chained | Live public HTTP capture sequence | Sealed (`55` captures in `task16-capture-007`) | Iterative primary-source HTTP capture across IDs 91–100 (`synthetic: false`), culminating in `task16-capture-007`. |",
        f"| `{RUN_ID}` | `task16-capture-007` | **Task 16 first-pass extraction** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`, `{ev_checked}` verified evidence refs, review pending). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        "- **Selected Apps**: `10 / 100` (IDs `91–100`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures); `{len(failed_rows)}` uncaptured fetch URLs preserved in telemetry",
        f"- **Eligible Research Assertions (Frozen Inventory)**: `{metrics['overall']['eligible']}` total (`{metrics['by_basis']['observed']['eligible']}` observed documentary, `{metrics['by_basis']['inferred']['eligible']}` inferred; excludes 10 identity claims)",
        f"- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `{metrics['overall']['pending']}` pending, `accuracy: null`",
        "",
        "| Research Area | Observed | Inferred | Unknown | Not Researched | Not Applicable | Not Found (Bounded) | Apps w/ Assertions |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for area in ("identity", "purpose", "auth", "credentials", "api", "mcp", "buildability"):
        st = metrics["research_coverage"][area]["claim_status_counts"]
        rep_lines.append(
            f"| `{area}` | {st.get('observed',0)} | {st.get('inferred',0)} | {st.get('unknown',0)} | "
            f"{st.get('not_researched',0)} | {st.get('not_applicable',0)} | {st.get('not_found_in_checked_sources',0)} | "
            f"{metrics['research_coverage'][area]['apps_with_assertions']}/10 |"
        )

    rep_lines += [
        "",
        "## 3. Pilot Overlap (NotebookLM ID 91), Sample Integrity & Baseline Verification",
        "",
        "- **Pilot Overlap (App 91 — NotebookLM)**:",
        "  - In Task 05, NotebookLM Enterprise had edition-conflation and citation-attachment findings that motivated Contract v1.1's edition-matching rule for `mcp.discovery` and per-claim locator reinforcement.",
        f"  - In `task16-capture-007` and `{RUN_ID}`, NotebookLM Enterprise (now renamed **Gemini Notebook Enterprise** on Google Cloud) is freshly captured under pipeline v0.2.0 and contract v1.1 with strict edition separation: the personal `developers.google.com/notebook/docs/authentication` Public Preview is explicitly excluded from Enterprise scope, and `91.mcp.discovery` is `not_found_in_checked_sources` rather than conflating personal/community MCPs.",
        "  - Original sealed Task 04/05 pilot runs (`pilot-first-pass-001` and `task05-review-002`) remain byte-for-byte untouched.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in AI, Research and Media-native were researched to the same documentary standard without preferential treatment for sample apps (`97` higgsfield, `98` Mermaid CLI).",
        "- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.",
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
        "Rebuild extraction JSON and Task 16 deliverables from sealed capture `task16-capture-007`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-16-agent/build_extraction.py",
        ".venv\\Scripts\\python.exe -B work/task-16-agent/generate_deliverables.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 16: Exceptions, Contradictions & Reviewer Notes (AI, Research and Media-native, IDs 91–100)",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (AI, Research and Media-native, IDs 91–100). No correctness judgments or accuracy claims are made here.",
        "",
        "1. **NotebookLM (ID 91) — Enterprise Rename & Personal-Edition Exclusion**:",
        "   - Google Cloud docs (`set-up-licensing` lines 140–144) state NotebookLM Enterprise has been renamed **Gemini Notebook Enterprise** while the subscription name remains NotebookLM Enterprise. The API (`discoveryengine.googleapis.com` v1alpha) is Preview/Pre-GA and requires a licensed user with `roles/discoveryengine.notebookLmUser` plus customer tenant admin setup (`admin_approval_required=true`).",
        "   - Captured `developers.google.com/notebook/docs/authentication` (lines 51–54) restricts its separate Public Preview to personal Google Accounts; its scopes, endpoints, and any personal/community MCP are excluded from this Enterprise scope (`91.mcp.discovery=not_found_in_checked_sources`).",
        "2. **Otter AI (ID 92) — OAuth MCP vs. Account-Manager-Gated Enterprise Public API & Single-Line JSON Capture**:",
        "   - Otter MCP (`https://mcp.otter.ai/mcp`) uses OAuth browser authorization (`35287607569687-Otter-MCP-Server`) and explicitly states no public API key is used for MCP setup, whereas the separate Enterprise Public API (`https://api.otter.ai/v1/`, Zendesk Help Center JSON `36130822688279.json`) uses `Authorization: Bearer YOUR_API_KEY` and requires contacting an Otter account manager to enable access (`4412365535895`).",
        "   - Because Zendesk Help Center's JSON API response normalizes to a single line (`lines:1-1`), observations cite exact JSON/HTML sections (`article.body`, `#authentication`, `#endpoints`) without fabricating line splits. MCP plan eligibility and Enterprise pricing remain `unknown`.",
        "3. **Fathom (ID 93) — Identity Match, User-Level Sharing Boundaries & Public OAuth Review**:",
        "   - Matched to `fathom.video` / `developers.fathom.ai` (`help.fathom.video/en/articles/8368641` links directly to `developers.fathom.ai`), excluding unrelated Fathom products.",
        "   - Internal user API keys (`X-Api-Key`) are self-serve in User Settings and strictly respect user/team sharing (even admin keys never grant private meeting access). Multi-user public OAuth apps (`public_api` scope) are separately subject to vendor review (`oauth.md` lines 7–8); plan/free-tier eligibility remains `unknown`.",
        "4. **Consensus (ID 94) — Roster Hint Reconciliation & Rate-Limit Discrepancy**:",
        "   - Reconciles roster hint `consensus.app (OAuth requested)`: REST `/v1` uses self-serve `x-api-key` on every plan including Free (`30` calls/month, `20` papers/request; pagination, full-text, and beta citation/reference endpoints require paid plans). Per-user MCP (`https://mcp.consensus.app/mcp`) uses self-serve OAuth2 PKCE S256 with Dynamic Client Registration for public clients; only confidential enterprise OAuth clients require manual provisioning/contact sales.",
        "   - Rate-limit descriptions differ between `api-plans-and-access.md` and `enterprise/connection-reference.md`; no global rate-limit claim is asserted.",
        "5. **Reducto (ID 95) — Free Account Signup vs. Unspecified Free Page Quota**:",
        "   - `quickstart/index.md` (line 12) invites users to sign up for a free account at `studio.reducto.ai`, and `studio-account/index.md` (line 14) states all roles can create API keys (only Owners/Admins can edit/delete keys). However, `credit-usage/index.md` documents per-1,000-page list pricing (`$1`–`$60`) without specifying a free starter page allowance; therefore `95.testing.free_access` and `95.testing.paid_required` remain `unknown`.",
        "   - Official hosted MCP (`https://mcp.reducto.ai/mcp`, Bearer API key) only accepts public URLs; local filesystem uploads require the official local server (`uvx mcp-server-reducto`, OAuth device-code login).",
        "6. **Devin (ID 96) — Principal/Token Model, Enterprise PAT Policy, and Outgoing vs. Callable MCP**:",
        "   - Distinguishes `cog_` Service User API keys (org- or enterprise-scoped, RBAC roles, provisioned by Admin) from `cog_` Personal Access Tokens (disabled by default on Enterprise pending enterprise admin policy) and deprecated `apk_`/`apk_user_` keys (which work only on DeepWiki repo wiki tools on MCP and are rejected by session/platform tools).",
        "   - Explicitly separates Devin's **callable** MCP server (`https://mcp.devin.ai/mcp`, requiring a Devin account and `X-Org-Id` for enterprise keys/PATs) from Devin's **outgoing** MCP client/marketplace management (`devin_mcp_server_manage`) and from the separate free public-repo-only DeepWiki MCP (`https://mcp.deepwiki.com/`). Devin account pricing/free-tier eligibility remains `unknown`.",
        "7. **higgsfield (ID 97 — Frozen 20-App Sample) — Strict Commercial Separation Between API vs. CLI/MCP**:",
        "   - Higgsfield operates two completely separate billing/auth paths: (a) **Higgsfield API** (`open.higgsfield.ai` / `api.higgsfield.ai`, API key, REST/Python/TS SDK, prepaid USD balance with `$5` minimum top-up expiring in 1 year, no web subscription required, 7+ day file retention), and (b) **Higgsfield CLI & MCP** (`@higgsfield/cli` and `https://mcp.higgsfield.ai/mcp`, browser sign-in with no API key, requiring a **paid Higgsfield subscription** and deducting plan credits; web Unlimited and free generations explicitly do not apply).",
        "8. **Mermaid CLI (ID 98 — Frozen 20-App Sample) — Local MIT CLI & Non-Semver Node.js API**:",
        "   - Open-source MIT-licensed local CLI (`mmdc`, npm/npx/Docker/Podman) with no vendor auth (`auth.method=none`) and `trial_access`/`sandbox_access` marked `not_applicable`. The programmatic Node.js API (`run()`) is explicitly not covered by semver (`README.md` line 138). Bounded check of official repo/README found no official MCP server (`98.mcp.discovery=not_found_in_checked_sources`).",
        "9. **YouTube Transcript (ID 99) — Third-Party TranscriptAPI.com Scope & Mixed Credit Pricing**:",
        "   - Matched to `transcriptapi.com` per roster hint (third-party YouTube transcript service, not an official Google/YouTube API). Provides REST v2 (`sk_` Bearer key) and hosted MCP (`https://transcriptapi.com/mcp`, OAuth 2.1 DCR/Static or `sk_` Bearer key). New accounts get `100` free no-card starter credits (verified email required) and 2 tools cost `0` credits; ongoing transcript/search calls require paid plans (`$5/mo` for 1,000 credits, `402 Payment required` when exhausted), so `99.production.free_access` remains `unknown`.",
        "10. **Grain (ID 100) — Personal vs. Workspace Token Scopes, Verified OAuth & Admin MCP Enablement**:",
        "    - Strictly separates **Personal Access Tokens** (`grain_pat_...`, Free+ plans, self-serve, works on REST v2 and headless MCP `https://api.grain.com/_/mcp`) from **Workspace Access Tokens** (workspace admin only, Business/Enterprise only, full workspace access, **rejected by MCP**) and **OAuth2** (`workspace` scope restricted to Grain-verified clients; server-side Client ID/Secret requested manually; public/MCP clients use Client ID Metadata Documents).",
        "    - `support.grain.com/.../export-meetings` (line 93) states a workspace admin enables the Grain MCP connector for the workspace while Personal API tokens are self-serve for any user; therefore `admin_approval_required` and `vendor_approval_required` remain `unknown` across mixed paths. Deals and Sales Coaching MCP tools require Business/Enterprise.",
        "11. **Operational Checks Unresearched**:",
        "    - All 8 nested MCP `operational_check` claims across the 8 MCP-enabled apps in IDs 91–100 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 5 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
