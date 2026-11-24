"""Generate outputs/task-11/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task11-first-pass-004"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-11"
OUT_DIR.mkdir(parents=True, exist_ok=True)

EXCLUDED_BAD_URLS = {
    "https://gumroad.com/api",
    "https://help.gumroad.com/article/280-create-application-api",
    "https://developer-docs.amazon.com/sp-api/docs/onboarding-as-a-developer",
    "https://developer-docs.amazon.com/sp-api/docs/connect-to-the-sp-api",
    "https://commasdocs.com/",
    "https://commasdocs.com/llms.txt",
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
    assert ids == list(range(41, 51)), f"Unexpected IDs: {ids}"
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
    }
    for label, (path, expected) in baseline_checks.items():
        actual = sha256_file(path)
        assert actual == expected, f"Baseline modified: {label} ({actual} != {expected})"

    records_sha = sha256_file(RUN_DIR / "records.json")
    seal_sha = sha256_file(RUN_DIR / "seal.json")
    app_names = {r["identity"]["id"]: r["identity"]["app"] for r in records}

    # 2. Source Index
    src_lines = [
        "# Task 11: Source Index (Ecommerce, IDs 41–50)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} snapshots (all live HTTP captures, `synthetic: false`; 6 JS-shell / 404 snapshots were preserved in the run archive and excluded from claim citations)",
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
        "Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence.",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 3. Findings Matrix
    mat_lines = [
        "# Task 11: Findings Matrix (Ecommerce, IDs 41–50)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        f"- **Frozen 20-App Sample Members in Batch**: App `46` (Squarespace) and App `50` (fanbasis / Commas)",
        "",
        "| ID | App | Auth Methods (Observed) | Testing / Sandbox | Production Access | Protocols & Breadth | MCP Discovery | Buildability |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in records:
        aid = r["identity"]["id"]
        app = r["identity"]["app"]
        auths = ", ".join(x["value"]["method"] for x in r["auth"]["items"] if x["value"]) or "unknown"
        t_el = r["credential_eligibility"]["testing"]
        t_parts = [k for k in ("free_access", "trial_access", "sandbox_access", "self_serve", "vendor_approval_required", "partner_approval_required") if t_el[k]["value"] is True]
        t_str = ", ".join(t_parts) or "unknown"
        p_el = r["credential_eligibility"]["production"]
        p_parts = []
        for k in ("free_access", "paid_required", "self_serve", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required"):
            v = p_el[k]["value"]
            if v is True:
                p_parts.append(k)
            elif v is False:
                p_parts.append(f"!{k}")
        p_str = ", ".join(p_parts) or "unknown"
        protos = ", ".join(x["value"] for x in r["api_surface"]["protocols"]["items"] if x["value"]) or "unknown"
        br = r["api_surface"]["breadth"]["value"] or r["api_surface"]["breadth"]["status"]
        mcp_d = r["mcp"]["discovery"]["value"] or r["mcp"]["discovery"]["status"]
        if r["mcp"]["entries"]:
            origins = sorted({e["value"]["origin"] for e in r["mcp"]["entries"]})
            mcp_str = f"`{mcp_d}` ({'/'.join(origins)}, {len(r['mcp']['entries'])})"
        else:
            mcp_str = f"`{mcp_d}`"
        bld = r["buildability"]["value"]["verdict"] if r["buildability"]["value"] else r["buildability"]["status"]
        mat_lines.append(f"| {aid} | {app} | {auths} | {t_str} | {p_str} | {protos} ({br}) | {mcp_str} | `{bld}` |")

    (OUT_DIR / "findings-matrix.md").write_text("\n".join(mat_lines) + "\n", encoding="utf-8")

    # 4. Exceptions for Reviewer
    exc_lines = [
        "# Task 11: Exceptions, Unknowns & Reviewer Notes (Ecommerce, IDs 41–50)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        "- **Review Status**: `pending` (`accuracy: null`, `review_coverage: 0.0%`). No independent review or human check has been performed.",
        "",
        "## 1. Frozen 20-App Sample Members in This Batch",
        "- **App 46 (Squarespace)**: Included in `outputs/task-06/sampling-manifest.json`. `developers.squarespace.com/commerce-apis` top navigation lists `MCP`, but no MCP doc page was captured in this pass, so `46.mcp.discovery` is preserved as `unknown`.",
        "- **App 50 (fanbasis)**: Included in `outputs/task-06/sampling-manifest.json`. Official homepage `www.fanbasis.com` redirects/displays `FanBasis is now Commas!` (Commas Inc.) with `Enterprise & APIs` and `MCP (beta)`. Legacy `dev-docs.fanbasis.com` (`FanBasis API Docsv3`) is password-protected (`Sign in to access API Docs`), and `commasdocs.com` rendered only a 2-line JS `Unpacking...` shell. Auth methods, credential eligibility booleans, wire protocol, and API breadth remain honestly `unknown` / `partial` pending accessible documentation or vendor outreach.",
        "",
        "## 2. HTTP 403 / 404 / Timeout / JS-Shell Captures",
        "- **App 41 (Shopify)**: `shopify.dev/docs/apps/build/authentication`, `authorization-code-grant`, `ai-toolkit`, `customer-accounts/mcp`, and `github.com/Shopify/dev-mcp` returned HTTP 404. Client credentials grant, GraphQL Admin API (`X-Shopify-Access-Token`), Dev stores, Pricing, and Shop MCP (`shopify.dev/docs/agents`) were captured cleanly.",
        "- **App 44 (Salesforce Commerce Cloud)**: `developer.salesforce.com/docs/commerce/commerce-api/guide/*` returned HTTP 403 (`blocked`). Findings are grounded in official `SalesforceCommerceCloud` GitHub repos (`commerce-sdk`, `commerce-sdk-isomorphic`, `b2c-developer-tooling`) and `salesforce.com/commerce/pricing/`. `44.api.public_docs` is kept `unknown` rather than inferred.",
        "- **App 45 (Magento / Adobe Commerce)**: `business.adobe.com/products/magento/pricing.html` timed out and `gs-authentication-token` returned HTTP 404. REST, GraphQL, Authentication overview, and `github.com/magento/magento2` (OSL 3.0) were captured cleanly.",
        "- **App 46 (Squarespace)**: `developers.squarespace.com/commerce-apis/orders-api` returned HTTP 404 (replaced by `orders-overview`) and `support.squarespace.com` article timed out (`squarespace.com/pricing` captured 774 lines cleanly).",
        "- **App 47 (Ecwid)**: `docs.ecwid.com/api-reference/rest-api/authentication` returned HTTP 404; OAuth 2.0 model and 600 req/min rate limit are confirmed on `docs.ecwid.com/api-reference/rest-api/overview`.",
        "- **App 48 (Gumroad)**: `gumroad.com/api` and `help.gumroad.com/article/280-create-application-api` rendered 1-line JS shells and are excluded from all claim citations. Findings are grounded in `gumroad.com/pricing`, official `github.com/antiwork/gumroad`, official `github.com/antiwork/gumroad-cli` (`gumroad mcp`), and community `github.com/rmarescu/gumroad-mcp` (MCP entry only). `48.api.public_docs` is kept `unknown`.",
        "- **App 49 (Amazon Selling Partner)**: Legacy URLs `onboarding-as-a-developer` and `connect-to-the-sp-api` returned 21-line `Page Not Found` pages and are excluded from all citations. Active SP-API docs (`what-is-the-selling-partner-api`, `registering-as-a-developer`, `authorizing-selling-partner-api-applications`, `connecting-to-the-selling-partner-api`, `the-selling-partner-api-sandbox`), official `amzn/selling-partner-agentic-toolkit` (`https://sellingpartner-ai.amazon.com/mcp`), and community `jay-trivedi/amazon_sp_mcp` were captured cleanly.",
        "",
        "## 3. Immutable Run History",
        "- `task11-capture-001`: failed pre-check under global Python (lacked `jsonschema`); preserved untouched.",
        "- `task11-capture-002`: sandboxed run under `.venv` (DNS blocked, 0 captures); preserved untouched.",
        "- `task11-capture-003`: initial live capture (42 captures); preserved untouched.",
        "- `task11-capture-004`: supplementary live capture (57 captures total); parent of extraction.",
        "- `task11-first-pass-001`: rejected by runtime validator (community repo attached to App 48 product claims); preserved untouched.",
        "- `task11-first-pass-002`: rejected by runtime validator (App 50 MCP scope wording lacked explicit 'server'); preserved untouched.",
        "- `task11-first-pass-003`: initial sealed first-pass run (remediated after independent AI audit identified 4 locator line-range defects on Apps 44, 46, and 50); preserved untouched.",
        "- `task11-first-pass-004`: sealed, validated, remediated first-pass deliverable run.",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    # 5. Batch Completion Report
    rep_lines = [
        "# Task 11 Completion Report: Ecommerce (IDs 41–50)",
        "",
        "- **Assigned Task**: Task 11 (Research batch 5: Ecommerce, app IDs 41–50)",
        "- **Producer**: `task11-research-agent-gemini` (AI)",
        "- **Pipeline / Contract**: `research_pipeline.py` v0.2.0 / Contract v1.1 (`schemas/record.json`, unchanged)",
        f"- **Sealed Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **`records.json` SHA-256**: `{records_sha}`",
        f"- **`seal.json` SHA-256**: `{seal_sha}`",
        "- **Synthetic**: `false` (live public HTTP captures only; no authenticated app calls, paid accounts, or signups)",
        "- **Independent Review Status**: `pending` (`accuracy: null`, `review_coverage: 0.0%`; AI review pending; no human review performed)",
        "",
        "## Validation & Metrics Summary",
        "",
        f"- **Validator**: `{validation['backend']}` → `{validation['structure_and_grounding']}` (`10/10` records matching `data/apps.json` IDs 41–50)",
        f"- **Captured Sources**: `{len(captures)}` live snapshots (`{ev_checked}` verified evidence observations; 0 citations to excluded 404/JS-shell snapshots)",
        f"- **Eligible Assertions (`inventory.json`)**: `{metrics['overall']['eligible']}` (`{metrics['by_basis']['observed']['eligible']}` observed, `{metrics['by_basis']['inferred']['eligible']}` inferred; `{metrics['overall']['pending']}` pending)",
        "- **Nested MCP Operational Checks**: `10/10` remain `not_researched`",
        "- **Baseline Immutability**: Verified unchanged for `pilot-first-pass-001`, `task05-review-002`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json`.",
        "",
        "## Buildability & MCP Highlights (First-Pass, Unreviewed)",
        "",
        "- **`build_now` (4 apps)**: Shopify (41), WooCommerce (42), BigCommerce (43), Gumroad (48)",
        "- **`conditional` (4 apps)**: Magento / Adobe Commerce (45 — edition-dependent PaaS/Open Source vs SaaS), Squarespace (46 — Commerce Advanced plan for API keys / vendor review for OAuth), Ecwid (47 — paid plans / missing OAuth endpoint doc), Amazon Selling Partner (49 — mandatory SP-API developer & role approval + Professional account)",
        "- **`outreach_required` (2 apps)**: Salesforce Commerce Cloud (44 — enterprise sales-quoted licensing + 403-blocked dev docs), fanbasis / Commas (50 — rebranded to Commas; legacy `dev-docs.fanbasis.com` password-gated, `commasdocs.com` JS unpacking shell)",
        "- **Official MCP Servers Observed (7 apps)**: Shopify (`Shop MCP`), WooCommerce (`WordPress MCP Adapter` dev preview), BigCommerce (`Docs MCP Server` at `https://docs.bigcommerce.com/_mcp/server` + Store Management/Storefront/WebMCP), Salesforce Commerce Cloud (`b2c-dx-mcp`), Gumroad (`gumroad mcp` in `antiwork/gumroad-cli` + community `rmarescu/gumroad-mcp`), Amazon SP-API (`Amazon Selling Partner Connector` at `https://sellingpartner-ai.amazon.com/mcp` + community `jay-trivedi/amazon_sp_mcp`), FanBasis / Commas (`Commas MCP` beta).",
        "- **MCP `not_found_in_checked_sources` / `unknown` (3 apps)**: Magento / Adobe Commerce (45, `not_found_in_checked_sources`), Ecwid (47, `not_found_in_checked_sources`), Squarespace (46, `unknown` — nav lists `MCP` without captured MCP doc page).",
        "",
        "## Deliverables Written",
        "",
        "- `outputs/task-11/records.json`",
        "- `outputs/task-11/source-index.md`",
        "- `outputs/task-11/findings-matrix.md`",
        "- `outputs/task-11/exceptions-for-reviewer.md`",
        "- `outputs/task-11/batch-report.md`",
        "- `outputs/task-11/metrics.json`",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    print(f"OK: Generated outputs/task-11/ deliverables from {RUN_ID}")
    print(f"  records.json SHA-256: {records_sha}")
    print(f"  seal.json    SHA-256: {seal_sha}")
    print(f"  captures: {len(captures)}, verified evidence refs: {ev_checked}, eligible assertions: {metrics['overall']['eligible']}")


if __name__ == "__main__":
    main()
