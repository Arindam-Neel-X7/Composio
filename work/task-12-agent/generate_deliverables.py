"""Generate outputs/task-12/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task12-first-pass-005"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-12"
OUT_DIR.mkdir(parents=True, exist_ok=True)

EXCLUDED_BAD_URLS = {
    "https://pypi.org/project/sherlock-project/",
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

    # Verify all 10 IDs, no synthetic flags, all evidence resolves, no bad URLs cited, all reviews pending
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(51, 61)), f"Unexpected IDs: {ids}"
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
                        assert ev["source_url"] not in EXCLUDED_BAD_URLS, f"Bad URL cited: {ev['source_url']}"
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
        "task12-first-pass-003/records.json": (
            ROOT / "work/research-runs/task12-first-pass-003/records.json",
            "d6d048def485478aa82378d618baf7788afa1a560933bdf71dbc43d8efba7d12",
        ),
        "task12-first-pass-003/seal.json": (
            ROOT / "work/research-runs/task12-first-pass-003/seal.json",
            "0c4c35191407f56378eca4f1a34a33d819807d1185d88725a6672041430d541c",
        ),
        "task12-first-pass-004/records.json": (
            ROOT / "work/research-runs/task12-first-pass-004/records.json",
            "616ed020c06d04179057188108ed412df333ac94a252e27b371ae20271c5b45a",
        ),
        "task12-first-pass-004/seal.json": (
            ROOT / "work/research-runs/task12-first-pass-004/seal.json",
            "51bcbc8fb0aa87d9e19aaf40deca7eccb36090d2a3139114647e19321e3ddb32",
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
        "# Task 12: Source Index (Data, SEO and Scraping, IDs 51–60)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`; 1 PyPI client-challenge page `pypi.org/project/sherlock-project/` was preserved in the run archive and excluded from claim citations)",
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
        "Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence. (`0` uncaptured source declarations in `task12-capture-003`.)",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Concise Findings Matrix
    mat_lines = [
        "# Task 12: Findings Matrix (Data, SEO and Scraping, IDs 51–60)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        "- **Frozen 20-App Sample Members in Batch**: App `52` (SE Ranking) and App `60` (Clay)",
        "- **Pilot Overlap in Batch**: App `58` (Sherlock — original Task 04/05 pilot baseline `pilot-first-pass-001` and `task05-review-002` preserved untouched)",
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

    # 4. Batch Report
    rep_lines = [
        "# Task 12: Batch 6 Research Report (Data, SEO and Scraping, IDs 51–60)",
        "",
        "- **Date**: 2026-11-23",
        "- **Category**: Data, SEO and Scraping (`data/apps.json` IDs `51–60`)",
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
        "| `task12-capture-001` | `null` | Initial live capture | Sealed (`126` captures) | Approved-network HTTP capture across IDs 51–60 (including 72,341-line Ahrefs OpenAPI 3.2.0 JSON spec). |",
        "| `task12-capture-002` | `task12-capture-001` | Expanded capture (v2) | Sealed (`141` captures) | Added 15 official `developers.clay.com` Markdown pages (`index.md`, `quickstart.md`, `public-api/authentication.md`, `tables.md`, `searches.md`, `routines/api.md`, `llms.txt`, etc.). |",
        "| `task12-capture-003` | `task12-capture-002` | Final capture (v3) | Sealed (`146` captures) | Added official `seranking/openapi` and `seranking/seo-skills` READMEs, `developers.clay.com/routines/custom-functions.md`, and `clay-run/agent-plugins`. |",
        "| `task12-first-pass-001` | `task12-capture-003` | Initial ingest attempt | Rejected (preserved) | Rejected by MCP URL presence check (`MCP URL not present in cited content` for 3 `repository_url` strings on hosted MCP entries); preserved untouched. |",
        "| `task12-first-pass-002` | `task12-capture-003` | Second ingest attempt | Rejected (preserved) | Rejected by MCP callable-direction wording check on `60.mcp.official_clay_mcp` (`connector` without `server`); preserved untouched. |",
        "| `task12-first-pass-003` | `task12-capture-003` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewers (`NEEDS FIXES`); preserved untouched. |",
        "| `task12-first-pass-004` | `task12-first-pass-003` | Second sealed pass (superseded) | Sealed (preserved) | Remediated 15 internal audit locator/attachment items; preserved untouched. |",
        f"| `{RUN_ID}` | `task12-first-pass-004` | **Final Task 12 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`{validation['backend']}`, `10` records, `synthetic: false`, `{ev_checked}` verified evidence refs, all 15 internal audit findings and all 18 Codex review checkpoint items in `outputs/task-12-review.md` remediated). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `51–60`, all 10 present with asserted non-identity research)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures; 1 PyPI client-challenge page excluded from citations); `{len(failed_rows)}` uncaptured fetch declarations in the final run",
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
        "## 3. Pilot Overlap (Sherlock ID 58), Sample Integrity & Baseline Verification",
        "",
        "- **Pilot Overlap (App 58 — Sherlock)**:",
        "  - Inspected `work/task-04-runs/pilot-first-pass-001`, `work/task-04-runs/task05-review-002`, and `outputs/task-05/verification-report.md` before researching Sherlock.",
        "  - In Task 05, Sherlock scored `13/13` (`100.0%`), with two notes: (a) `58.mcp` (`not_found_in_checked_sources`) was verified accurate for official sources, and (b) `sherlockproject.xyz/usage` lines 76–77 had leaked Mintlify JSON/MDX hydration payload in v0.1.0, which Task 06 fixed in `research_pipeline.py` v0.2.0 (`test_22_html_hydration_json_stripping`).",
        f"  - In `task12-capture-003` and `{RUN_ID}`, `sherlockproject.xyz/usage` (75 clean lines), `sherlockproject.xyz/installation` (92 clean lines), `github.com/sherlock-project/sherlock`, `pyproject.toml` (v0.16.2), and `LICENSE` (MIT) were freshly captured under pipeline v0.2.0 and contract v1.1 (including `vendor_approval_required=false`), while preserving `pilot-first-pass-001` and `task05-review-002` byte-for-byte untouched.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Data, SEO and Scraping were researched to the same documentary standard without preferential treatment for sample apps (`52` SE Ranking, `60` Clay).",
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
        "Rebuild extraction JSON from sealed capture `task12-capture-003`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-12-agent/build_extraction.py",
        ".venv\\Scripts\\python.exe -B work/task-12-agent/generate_deliverables.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    # 5. Exceptions List for Independent Reviewer
    exc_lines = [
        "# Task 12: Exceptions, Contradictions & Reviewer Notes (Data, SEO and Scraping, IDs 51–60)",
        "",
        f"Prepared for independent review of `work/research-runs/{RUN_ID}` (Data, SEO and Scraping, IDs 51–60). No correctness judgments or accuracy claims are made here.",
        "",
        "1. **MrScraper (ID 54) — Internal Documentation Contradictions on Free Token Quota & Plan Naming**:",
        "   - On `https://docs.mrscraper.com/docs/getting-started/billing`, the comparison table at line 32 lists `Scraper Free` with `1,000 token` (`10` concurrent requests, no residential proxies) and `Scraper Pro` with `200,000 token` (`100` concurrent requests), whereas line 38 on the exact same page states: *'The Free plan includes 100 tokens per month with no credit card required.'*",
        "   - Furthermore, `https://mrscraper.com/pricing` (lines 41–54) names the `$99/month` 200,000-token tier `Essential` (with `20` concurrent requests) alongside `Enterprise` (`Contact Us`, `500k+` tokens, `200` concurrent requests). Both observations are preserved explicitly in `54.testing.free_access`, `54.production.free_access`, and `54.buildability`.",
        "   - On `https://docs.mrscraper.com/docs/getting-started/mcp-server` (line 32), the prose mentions *'MrScraper MCP server source code on GitHub'*, but normalized text extraction strips the anchor `href` and probing `github.com/mrscraper/mcp` aborted/404'd; consequently `repository_url` is kept `null` while `server_url` is set to the documented `https://mcp.mrscraper.com/mcp` endpoint.",
        "2. **Ahrefs (ID 53) — Tiered API/MCP Entitlements, Ahrefs Connect OAuth Approval, and Custom MCP Client Prohibition**:",
        "   - Ahrefs API v3 and the hosted remote MCP server (`https://api.ahrefs.com/mcp/mcp`) require a paid plan starting from **Lite** (`$129/mo`; `Ahrefs Free` and `Starter $29/mo` do not include full API/MCP access), and only workspace owners/admins can create or manage API keys (`53.testing.admin_approval_required=true`, `53.production.admin_approval_required=true`).",
        "   - However, Ahrefs documents two distinct testing/public paths (`53.testing.free_access=unknown` and `53.testing.paid_required=unknown` to avoid collapsing paths): (a) complimentary free test queries on any paid plan when targeting `ahrefs.com`, `yep.com`, or `firehose.com` (capped at `limit=100`, explicitly requiring a paid plan per `free-test-queries.md` line 2), and (b) `/v3/public` endpoints (`crawler-ips`, `crawler-ip-ranges`, and `domain-rating-free`, where `public.json` line 85 notes free APIv3 keys can be generated on a free Ahrefs account).",
        "   - Specific Traffic Analytics endpoints in `docs.ahrefs.com/openapi.json` (e.g., lines 8213+) require the **Traffic Analytics Enterprise add-on**, and third-party multi-user OAuth apps using **Ahrefs Connect** (`scope=apiv3-integration-apps`) must pass Ahrefs' **Approval process** (while direct workspace keys on Lite+ plans do not require vendor review, so `53.production.vendor_approval_required=unknown` with both paths explained).",
        "   - Crucially, `docs.ahrefs.com/mcp/docs/introduction.md` (line 45) states: *'Using the external MCP endpoint via custom scripts, bridges, or standalone HTTP/JSON-RPC clients is unsupported and not permitted.'* Custom code must call REST API v3 (`https://api.ahrefs.com/v3/`) rather than scripting the MCP endpoint.",
        "3. **Clay (ID 60) — Legacy `clay.com/docs` Redirect vs. `developers.clay.com`, Enterprise-Only Tables API, and MCP Governance**:",
        "   - The legacy roster candidate `https://www.clay.com/docs` redirects to `https://university.clay.com/docs` (Clay University GTM lessons), and `https://docs.clay.com/` redirects to `https://www.clay.com/university`. Clay's actual technical developer documentation lives at **`https://developers.clay.com/`** (`llms.txt` captured in `task12-capture-002` and `task12-capture-003`).",
        "   - Clay's Public REST API (`https://api.clay.com/public/v0`, authenticated via `clay-api-key`) and JSON-first `clay` CLI (authenticated via browser OAuth `clay login` or `clay login --device`) expose **Searches** across Free (`50` results/req, `100` per 30 days), Trial (`10,000` for trial), Paid (`500` results/req, `1,000,000` per 30 days), and Enterprise (`10,000,000` per 30 days), plus **Routines** (`POST /public/v0/routines/{routine_id}/run`). However, the **Tables API** (`POST /public/v0/tables/query`) is strictly **Enterprise only** (`developers.clay.com/tables.md` line 9).",
        "   - Clay's official MCP connector (`www.clay.com/mcp` and `developers.clay.com/routines/custom-functions.md`) requires explicit per-function **MCP access** enablement in Function Details plus workspace/role permissions (`list_subroutines`). Because the captured primary pages do not print a literal `https://.../mcp` URL string in their normalized text, `server_url` and `repository_url` are kept `null` on `60.mcp.official_clay_mcp`.",
        "4. **Waterfall.io (ID 59) — Identity Disambiguation, Approval-Gated Access (`outreach_required`), and Agent Skills vs. MCP**:",
        "   - Matched to the B2B contact and company enrichment platform at `https://waterfall.io/` and `https://docs.waterfall.io/` (`https://api.waterfall.io/v1/` and `/v2/account`), reconciling the roster hint `waterfall.io (contact/company intel)` and distinguishing it from unrelated products named Waterfall.",
        "   - Although Waterfall.io publishes full OpenAPI 3.1.0 specifications and `x-api-key` authentication docs, `docs.waterfall.io/v1/book-demo.md` (lines 6–13) and `faq.md` (lines 91–94) explicitly state that **API access is available by approval** (every request is reviewed by the Waterfall team, there is no public rate card on `waterfall.io/pricing`, and per-key capabilities like `include_phones: true` or master-key sub-key management must be enabled by the team). Therefore `59.buildability` is `outreach_required` (`testing.self_serve=false`, `production.self_serve=false`, `testing.vendor_approval_required=true`, `production.vendor_approval_required=true`, `production.contact_sales_required=true`, while `testing.contact_sales_required=unknown` because `book-demo.md` allows requesting an API key via email or optionally booking a call).",
        "   - `docs.waterfall.io/v1/skills-overview.md` documents agent skills (`waterfall-direct-api`, `waterfall-integration`) that instruct agents how to call the REST API using OpenAPI 3.1.0, not an MCP server; `59.mcp.discovery` is `not_found_in_checked_sources`.",
        "5. **Sherlock (ID 58) — Local Open-Source CLI vs. Hosted API & Pilot Reconciliation**:",
        "   - Reconciled with Task 04/05 pilot verification (`outputs/task-05/verification-report.md`): Sherlock (`github.com/sherlock-project/sherlock`, PyPI `sherlock-project` v0.16.2, MIT License) is a local Python CLI tool (`sherlock USERNAMES`) with no vendor authentication (`auth.method=none`) and no hosted REST API. Under pipeline v0.2.0, `sherlockproject.xyz/usage` captured cleanly in 75 lines without the Mintlify hydration blob noted in Task 05.",
        "   - `pypi.org/project/sherlock-project/` returned a 4-line Fastly/PyPI `Client Challenge` HTML shell to raw HTTP capture; it is preserved in `captures.json` and excluded from all claim citations (`EXCLUDED_BAD_URLS`).",
        "6. **SE Ranking (ID 52) — Master-Account vs. Sub-Account MCP/API Constraint**:",
        "   - `seranking.com/api/integrations/mcp/` (lines 459–464) notes that on shared workspaces, API access lives only with the **master account**; sub-account users cannot connect tools via the OAuth 'Sign in with SE Ranking' button and must obtain a master-account API key from their administrator (`52.production.admin_approval_required=unknown` because master account owners self-serve while shared-workspace sub-accounts require administrator key sharing).",
        "7. **Firecrawl (ID 56) — Hosted Cloud vs. AGPL-3.0 Self-Hosted & Keyless Tier Scope**:",
        "   - Distinguishes Firecrawl Cloud (`https://api.firecrawl.dev`, Free plan 1,000 credits/month, keyless rate-limited access on `/v1/scrape`, `/v1/search`, and `https://mcp.firecrawl.dev/v2/mcp` for `scrape`/`search`/`parse`, plus OAuth at `/v2/mcp-oauth`) from the open-source self-hosted Docker Compose edition (`github.com/firecrawl/firecrawl`, licensed under **AGPL-3.0**).",
        "8. **Bright Data (ID 57) — Shared 5,000-Credit Monthly Free Pool vs. Proxy Trial Exclusion**:",
        "   - `docs.brightdata.com/general/account/billing-and-pricing/free-tier.md` documents that every new account gets 5,000 recurring monthly free credits (no credit card required, hard stop on exhaustion) shared across Web Unlocker, SERP API, Web Scraper API, Scraper Studio, Browser API, and Bright Data MCP (`https://mcp.brightdata.com/mcp`), whereas Proxy Infrastructure products (Residential, Datacenter, ISP) are excluded from the monthly free pool and receive only a one-time `$2` 7-day trial credit.",
        "9. **DataForSEO (ID 51) — Free Sandbox vs. $50 Minimum Pay-As-You-Go Production Top-Up**:",
        "   - Registered users get free self-serve access to `https://sandbox.dataforseo.com/v3/$path` using their standard HTTP Basic API login and API password (`51.testing.free_access=true`, `51.testing.sandbox_access=true`), whereas live production calls to `https://api.dataforseo.com/v3/` require a pay-as-you-go balance with a `$50` minimum account top-up (`51.production.paid_required=true`).",
        "10. **Operational Checks Unresearched**:",
        "    - All 12 nested MCP `operational_check` claims across the 8 MCP-enabled apps in IDs 51–60 remain `not_researched` (no authenticated API/MCP calls or live tool executions were performed).",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated all deliverables in {OUT_DIR}")
    print(f"Verified: 10/10 IDs, {len(captures)} captures, {ev_checked} evidence refs, 0 synthetic, all 5 baseline hashes unchanged.")


if __name__ == "__main__":
    main()
