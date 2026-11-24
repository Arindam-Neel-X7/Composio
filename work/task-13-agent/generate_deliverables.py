"""Generate outputs/task-13/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task13-first-pass-003"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-13"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Three Datadog HTML captures returned gzip-corrupt/garbled content and were replaced by
# readable .md captures in task13-capture-003; preserved in archive, excluded from citations.
EXCLUDED_CORRUPT_URLS = {
    "https://docs.datadoghq.com/account_management/api-app-keys/",
    "https://docs.datadoghq.com/mcp_server/",
    "https://docs.datadoghq.com/account_management/api-app-keys/?_task13=identity",
}


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

    # Verify all 10 IDs, no synthetic flags, all evidence resolves, no excluded URLs cited, all reviews pending
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(61, 71)), f"Unexpected IDs: {ids}"
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
                        assert ev["source_url"] not in EXCLUDED_CORRUPT_URLS, f"Excluded URL cited: {ev['source_url']}"
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
        "task13-first-pass-002/records.json": (
            ROOT / "work/research-runs/task13-first-pass-002/records.json",
            "474543d125f452ea94437a2089d8694770ece9f9bd5e01dd54f6ee5f82920527",
        ),
        "task13-first-pass-002/seal.json": (
            ROOT / "work/research-runs/task13-first-pass-002/seal.json",
            "56d77082e4e5cc75a34d1bb5e6e22d773be443dea2d6d8bec65e9d7c59be35dc",
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
        "# Task 13: Source Index (Developer, Infra and Data platforms, IDs 61–70)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`; 3 Datadog HTML captures with gzip-corrupt output are preserved in the run archive and excluded from claim citations in favor of readable `.md` captures)",
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
        note = " *(excluded: gzip-corrupt HTML)*" if c["spec"]["url"] in EXCLUDED_CORRUPT_URLS else ""
        src_lines.append(
            f"| {aid} | {app_names[aid]} | `{c['spec']['kind']}` | `{envs}` | {c['line_count']} | "
            f"{c['captured_on']} | {c['spec']['url']}{note} | `{c['content_sha256'][:12]}` |"
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
        f"Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence (`{len(failed_rows)}` uncaptured source URLs across IDs 68 and 69).",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Concise Findings Matrix
    mat_lines = [
        "# Task 13: Findings Matrix (Developer, Infra and Data platforms, IDs 61–70)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        "- **Frozen 20-App Sample Members in Batch**: App `64` (Cloudflare) and App `65` (Supabase)",
        "- **Pilot Overlap in Batch**: None (`pilot-first-pass-001` covers IDs `2, 13, 31, 58, 91`)",
        "- **Note**: Documentary observations and feasibility inferences only; no authenticated API/MCP calls or human checks were performed.",
        "",
        "| ID | App | One-Line Purpose | Auth Methods (Observed) | Testing Access | Production Access | API Surface & Breadth | MCP Discovery | Buildability (Inferred) | Key Cited Sources |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    def fmt_elig(env_obj):
        parts = []
        for k in (
            "free_access", "trial_access", "sandbox_access", "paid_required",
            "admin_approval_required", "vendor_approval_required",
            "partner_approval_required", "contact_sales_required", "self_serve",
        ):
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

    # 4. Batch Report
    rep_lines = [
        "# Task 13: Batch 7 Research Report (Developer, Infra and Data platforms, IDs 61–70)",
        "",
        "- **Date**: 2026-11-23 / 2026-11-24",
        "- **Category**: Developer, Infra and Data platforms (`data/apps.json` IDs `61–70`)",
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
        "| `task13-capture-001` | `null` | Initial live capture | Sealed (`41` captures) | Initial public documentation and official repository captures across IDs 61–70. |",
        "| `task13-capture-002` | `task13-capture-001` | Expanded capture (v2) | Sealed (`45` captures) | Added Vercel auth/welcome docs, Netlify pricing, and Datadog identity check. |",
        "| `task13-capture-003` | `task13-capture-002` | Expanded capture (v3) | Sealed (`51` captures) | Added Vercel deployment/account pages and readable Datadog `.md` sources (`api-app-keys.md`, `mcp_server.md`, `mcp_server/setup.md`) replacing gzip-corrupt HTML captures. |",
        "| `task13-capture-004` | `task13-capture-003` | Final capture (v4) | Sealed (`52` captures) | Added `vercel.com/docs/limits/fair-use-guidelines`; attempted `mongodb.com/docs/atlas/api/api-resources/` (HTTP 404, recorded in `fetches`). |",
        "| `task13-first-pass-001` | `task13-capture-004` | Initial ingest attempt | Incomplete / Rejected (preserved) | Rejected during pipeline intake validation; preserved untouched. |",
        "| `task13-first-pass-002` | `task13-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewer (`NEEDS FIXES`, 7 Contract v1.1 defects); preserved untouched. |",
        f"| `{RUN_ID}` | `task13-first-pass-002` | **Final Task 13 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`, `{ev_checked}` verified evidence refs; all 7 independent review defects and 2 polish items in `outputs/task-13-review.md` remediated). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        "- **Selected Apps**: `10 / 100` (IDs `61–70`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures; 3 gzip-corrupt Datadog HTML snapshots preserved in archive and excluded from claim citations); `{len(failed_rows)}` uncaptured fetch declarations recorded in `fetches` telemetry",
        f"- **Eligible Research Assertions (Frozen Inventory)**: `{metrics['overall']['eligible']}` total (`{metrics['by_basis']['observed']['eligible']}` observed documentary, `{metrics['by_basis']['inferred']['eligible']}` inferred; excludes 10 identity claims)",
        f"- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `{metrics['overall']['pending']}` pending, `accuracy: null`",
        "",
        "| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for area in ("identity", "purpose", "auth", "credentials", "api", "mcp", "buildability"):
        st = metrics["research_coverage"][area]["claim_status_counts"]
        rep_lines.append(
            f"| `{area}` | {st.get('observed', 0)} | {st.get('inferred', 0)} | {st.get('unknown', 0)} | "
            f"{st.get('not_researched', 0)} | {st.get('not_found_in_checked_sources', 0)} | "
            f"{metrics['research_coverage'][area]['apps_with_assertions']}/10 |"
        )

    rep_lines += [
        "",
        "## 3. Sample Integrity & Shared Baseline Verification",
        "",
        "- **Shared Baseline Status**: Task 06 (`outputs/task-06-review.md` PASS, pipeline `v0.2.0`, contract `v1.1`) confirmed accepted with no shared pipeline blockers encountered.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Developer, Infra and Data platforms were researched to the same documentary standard without preferential treatment for sample apps (`64` Cloudflare, `65` Supabase).",
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
        "Rebuild extraction JSON from sealed capture `task13-capture-004` and regenerate `outputs/task-13/` deliverables:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-13-agent/build_extraction.py",
        ".venv\\Scripts\\python.exe -B work/task-13-agent/generate_deliverables.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 13: Exceptions, Contradictions & Reviewer Notes (Developer, Infra and Data platforms, IDs 61–70)",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (Developer, Infra and Data platforms, IDs 61–70). No correctness judgments or accuracy claims are made here.",
        "",
        "1. **Datadog (ID 69) — Gzip-Corrupt HTML Captures Replaced by Readable `.md` Sources & Failed Fallback Probes**:",
        "   - Three HTML captures in `task13-capture-001`/`002` (`docs.datadoghq.com/account_management/api-app-keys/`, `docs.datadoghq.com/mcp_server/`, and `docs.datadoghq.com/account_management/api-app-keys/?_task13=identity`) produced garbled/gzip-corrupt text. They remain preserved in the immutable capture archive and are **excluded from all claim citations**.",
        "   - Readable official Markdown endpoints (`docs.datadoghq.com/account_management/api-app-keys.md`, `docs.datadoghq.com/mcp_server.md`, `docs.datadoghq.com/mcp_server/setup.md`) were captured cleanly in `task13-capture-003` and used for all Datadog auth/MCP citations. Six intermediate fallback probes (timeout on `/mcp_server/setup/` and HTTP 404 on guessed `.md` / GitHub paths) remain recorded in `fetches` telemetry.",
        "   - Datadog's remote MCP server uses site-specific URLs (e.g., `https://mcp.datadoghq.com/v1/mcp` for US1) and is explicitly **not GovCloud compatible**.",
        "2. **MongoDB Atlas (ID 68) — Administration Plane vs. Data Plane, 404 on `/api-resources/`, and Delegated Admin Toggle Scope**:",
        "   - Atlas Administration API v2 authentication (recommended OAuth2 client-credentials service accounts; legacy HTTP Digest public/private API keys) is strictly separated from database connection credentials and grants **no cluster data access**.",
        "   - `https://www.mongodb.com/docs/atlas/api/api-resources/` returned HTTP 404 in `task13-capture-004` (recorded in `fetches`); consequently REST protocol classification is not asserted directly from that page, while `CLI` and `SDK` (Go SDK) are asserted independently from `mongodb.com/docs/atlas/api/`.",
        "   - **Remediated in `task13-first-pass-003`**: `68.production.admin_approval_required` is set to `unknown` (`value: null`) on the shared Admin API + MCP context, preserving the evidence and rationale distinguishing user-delegated Atlas App Connections org opt-in from programmatic Admin API/CLI service accounts.",
        "3. **GitHub (ID 61) — Organization PAT Approval Policy vs. Personal PAT Self-Serve**:",
        "   - Scope is explicitly bounded to `GitHub.com` REST API (visible docs version `2026-03-10`) and official remote GitHub MCP (`https://api.githubcopilot.com/mcp/`), excluding GitHub Enterprise Server.",
        "   - **Remediated in `task13-first-pass-003`**: `61.production.admin_approval_required` is set to `unknown` (`value: null`) on the shared personal+organization context, preserving the evidence explaining optional org-admin fine-grained PAT approval policies alongside self-serve personal PATs (`61.production.self_serve=true`).",
        "4. **Vercel (ID 62) — Hobby Commercial-Use Restriction Unconfirmed in Captured Excerpts & CIMD Scope**:",
        "   - Commercial-use restrictions on Vercel's free Hobby plan were noted as discovery leads but not established inside the captured `vercel.com/docs/plans/hobby` and `vercel.com/docs/limits/fair-use-guidelines` text; therefore `62.production.free_access` and `62.production.paid_required` remain `unknown`.",
        "   - **Remediated in `task13-first-pass-003`**: `62.production.vendor_approval_required` is set to `unknown` (`value: null`) on the shared REST+MCP context, preserving the evidence distinguishing CIMD MCP clients (no review) from non-CIMD/listed MCP clients (Vercel review required).",
        "5. **Supabase (ID 65) — Data REST API vs. Management API, Legacy JWT Keys, and Branching Scope**:",
        "   - Separates Supabase's auto-generated Postgres/PostgREST Data API (`apikey` header with non-JWT publishable/secret keys; secret key bypasses RLS; legacy `anon`/`service_role` JWT keys coexist) from the Management API (`Authorization: Bearer` scoped/classic PAT or delegated OAuth2).",
        "   - **Remediated in `task13-first-pass-003`**: `65.production.paid_required` is set to `unknown` (`value: null`) on the shared context, preserving the evidence that only optional features such as experimental hosted Branching require a paid plan while standard production projects have a Free Plan path (`65.production.free_access=true`).",
        "6. **Neo4j (ID 66) — HTTP Transport Label (`other`) and Community Basic vs. Enterprise/Aura SSO**:",
        "   - Neo4j Query API (`Introduced in 5.19`; ungrounded `v2` label removed in `task13-first-pass-003`) executes Cypher over HTTP/HTTPS (`api.protocol.http = other`, intentionally not labeling it `REST` or `SQL` from Cypher/HTTP alone). Basic username/password auth covers Community Edition and development, whereas Bearer SSO token forwarding applies only to Enterprise/Aura configured with SSO/OAuth/OIDC. Official Neo4j MCP requires a running database and the APOC plugin.",
        "7. **Snowflake (ID 67) — SQL Trial vs. AI/MCP Card Gate and Independent RBAC Grants**:",
        "   - Snowflake's 30-day self-service SQL trial requires no credit card or contract, but **AI features are disabled until a card is added**, and trial accounts suspend after expiry or credit depletion (`67.production.paid_required=true`). Snowflake-managed MCP servers require independent RBAC grants for both the server and underlying tools; account-specific MCP URLs are intentionally not invented (`server_url: null`).",
        "8. **Netlify (ID 63) — Personal PAT vs. OAuth2 Public Integration & Local `npx` MCP**:",
        "   - Personal scripts may use self-serve PATs (`Authorization: Bearer`), while public multi-user integrations must use OAuth2 and SAML teams require SSO authorization. Official `@netlify/mcp` is documented as a local `npx` server requiring Node.js 22+ (`server_url: null`, `repository_url: null` because normalized README text does not print a literal hosted endpoint).",
        "9. **Cloudflare (ID 64) — Scoped Account/Zone Tokens & Feature-Specific Paid Plans**:",
        "   - Scoped user/account API tokens (`Authorization: Bearer`) are self-serve for existing accounts, while product/feature plan entitlements (e.g., paid Workers plan requirements for certain MCP features) are preserved without asserting app-wide free or paid status.",
        "10. **Sentry (ID 70) — Hosted Web API v0 (`other`) vs. Developer-Focused Remote MCP & Plan Split**:",
        "    - Hosted Sentry Web API v0 (`api.protocol.http = other`; REST not inferred beyond HTTPS resource examples) distinguishes user tokens from internal-integration organization tokens and third-party OAuth2. Free Developer plan (`$0`, 1 user) explicitly includes MCP access (`https://mcp.sentry.dev/mcp`), whereas API/third-party integrations are listed separately under Team, so universal free REST access is not inferred. Self-hosted parity is excluded.",
        "11. **Operational Checks Unresearched**:",
        "    - All 10 nested MCP `operational_check` claims across IDs 61–70 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all 6 deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 5 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
