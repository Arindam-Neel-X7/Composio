"""Generate outputs/task-15/ deliverables and verify evidence & baseline integrity."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task15-first-pass-002"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-15"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def fmt_ev_short(ev_list):
    seen = []
    for e in ev_list:
        u = e["source_url"].replace("https://", "")
        if len(u) > 48:
            u = u[:45] + "..."
        tag = f"`{u}` ({e['locator']})"
        if tag not in seen:
            seen.append(tag)
    return "; ".join(seen[:3]) + (f" (+{len(seen)-3} more)" if len(seen) > 3 else "")


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

    # Integrity checks
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(81, 91)), f"Unexpected IDs: {ids}"
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

    # 2. Cited findings matrix
    matrix_lines = [
        "# Task 15: Cited Findings Matrix (Finance and Fintech, IDs 81–90)",
        "",
        f"- **Run ID**: `{RUN_ID}` (`work/research-runs/{RUN_ID}`)",
        "- **Contract / Pipeline**: Contract `v1.1`, `research_pipeline.py` `v0.2.0`",
        "- **Review Status**: **Pending independent review** (`accuracy: null`, `review_coverage: 0.0%`). All MCP `operational_check` fields remain `not_researched`.",
        "",
        "| ID | App | Identity & Purpose | Auth Methods | Testing vs Production Credentials | API Surface & Breadth | MCP (Provenance & Direction) | Scoped Buildability & Key Blockers |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in records:
        aid = r["identity"]["id"]
        app = r["identity"]["app"]
        if r["purpose"]["status"] == "observed":
            purpose_cell = f"{r['purpose']['value']} ({fmt_ev_short(r['purpose']['evidence'])})"
        else:
            purpose_cell = f"`{r['purpose']['status']}` — {r['purpose']['rationale']}"

        if r["auth"]["items"]:
            auth_parts = [f"**{a['value']['method']}** (`{a['claim_id']}`): {a['value']['context']} ({fmt_ev_short(a['evidence'])})" for a in r["auth"]["items"]]
            auth_cell = "<br>".join(auth_parts)
        else:
            auth_cell = f"`{r['auth']['coverage_status']}` — {r['auth']['notes']}"

        def summarize_elig(env_dict):
            obs = []
            for k in ("free_access", "trial_access", "sandbox_access", "paid_required", "admin_approval_required", "vendor_approval_required", "partner_approval_required", "contact_sales_required", "self_serve"):
                c = env_dict[k]
                if c["status"] == "observed":
                    obs.append(f"`{k}={str(c['value']).lower()}`")
            return ", ".join(obs) if obs else "`all unknown`"

        cred_cell = f"**Test**: {summarize_elig(r['credential_eligibility']['testing'])}<br>**Prod**: {summarize_elig(r['credential_eligibility']['production'])}"

        protos = [p_c["value"] for p_c in r["api_surface"]["protocols"]["items"]]
        br = r["api_surface"]["breadth"]
        if protos:
            api_cell = f"Protocols: {', '.join(protos)}; Public docs: `{r['api_surface']['public_documentation']['value']}`; Groups: {len(r['api_surface']['resource_groups']['items'])}; Breadth: **`{br['value']}`** (`inferred`)"
        else:
            api_cell = f"Protocols: `{r['api_surface']['protocols']['coverage_status']}`; Breadth: `{br['status']}`"

        if r["mcp"]["entries"]:
            mcp_parts = []
            for m in r["mcp"]["entries"]:
                mv = m["value"]
                ep = f" (`{mv['server_url']}`)" if mv["server_url"] else " (local stdio)"
                mcp_parts.append(f"**{mv['origin']}** {mv['name']}{ep} ({fmt_ev_short(m['evidence'])})")
            mcp_cell = "<br>".join(mcp_parts)
        else:
            mcp_cell = f"`{r['mcp']['discovery']['status']}`"

        b = r["buildability"]
        if b["status"] == "inferred":
            bv = b["value"]
            blockers_str = "; ".join(bv["blockers"][:2])
            build_cell = f"**`{bv['verdict']}`** (`inferred`): {blockers_str}"
        else:
            build_cell = f"`{b['status']}` — {b['rationale']}"

        # Escape pipes inside cells
        row = [str(aid), app, purpose_cell, auth_cell, cred_cell, api_cell, mcp_cell, build_cell]
        row = [c.replace("|", "\\|").replace("\n", " ") for c in row]
        matrix_lines.append("| " + " | ".join(row) + " |")

    (OUT_DIR / "findings-matrix.md").write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")

    # 3. Source index
    src_lines = [
        "# Task 15: Source Index (Finance and Fintech, IDs 81–90)",
        "",
        f"- **Run ID**: `{RUN_ID}` (`work/research-runs/{RUN_ID}`)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures)",
        f"- **Verified Evidence References in Records**: `{ev_checked}` (100% snapshot & SHA-256 verified)",
        "",
        "## Captured Snapshots",
        "",
        "| App ID | App | Kind | Lines | Captured On | URL | Snapshot Ref | SHA-256 (prefix) |",
        "| ---: | --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for c in captures:
        s = c["spec"]
        src_lines.append(
            f"| {s['app_id']} | {app_names[s['app_id']]} | `{s['kind']}` | {c['line_count']} | {c['captured_on']} | {s['url']} | `{c['snapshot_ref']}` | `{c['content_sha256'][:16]}` |"
        )

    src_lines += [
        "",
        "## Failed Fetch Attempts (Preserved in `records.json` `fetches`)",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    fail_count = 0
    for r in records:
        for f in r["fetches"]:
            if f["status"] != "fetched":
                fail_count += 1
                src_lines.append(
                    f"| {r['identity']['id']} | {r['identity']['app']} | `{f['status']}` | `{f['http_status']}` | {f['source_url']} | `{f['error']}` |"
                )
    if fail_count == 0:
        src_lines.append("| — | — | — | — | None | — |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 4. Batch report
    cov = metrics["research_coverage"]
    def cov_row(area):
        c_counts = cov[area]["claim_status_counts"]
        return (
            f"| `{area}` | {c_counts.get('observed', 0)} | {c_counts.get('inferred', 0)} | "
            f"{c_counts.get('unknown', 0)} | {c_counts.get('not_researched', 0)} | "
            f"{c_counts.get('not_found_in_checked_sources', 0)} | "
            f"{cov[area]['apps_with_assertions']}/{cov[area]['selected_app_denominator']} |"
        )

    report_lines = [
        "# Task 15: Batch 9 Research Report (Finance and Fintech, IDs 81–90)",
        "",
        "- **Date**: 2026-11-24",
        "- **Category**: Finance and Fintech (`data/apps.json` IDs `81–90`)",
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
        "| `task15-capture-001` | `null` | Initial live capture | Sealed (preserved) | Initial primary docs and product pages across IDs 81–90. |",
        "| `task15-capture-002` | `task15-capture-001` | Follow-up capture | Sealed (preserved) | Added Plaid Trial/MCP, Binance/iPayX MCP READMEs, Xero FAQs/SDK, Brex `mcp.md`, Ramp `llms-guides/*.txt`. |",
        "| `task15-capture-003` | `task15-capture-002` | Alternate host capture | Sealed (`55` captures, preserved) | Added Ramp `sandbox-access.txt`; retried QBO `all-entities` (403) and PitchBook `www.pitchbook.com` (403). |",
        "| `task15-capture-004` | `task15-capture-003` | Sandboxed capture attempt | Sealed (`55` captures, unused branch) | Ran in network-isolated sandbox; 7 new URLs did not fetch; preserved untouched. |",
        "| `task15-capture-005` | `task15-capture-003` | Final live capture | Sealed (`62` captures) | Added Stripe Connect OAuth, Binance README, official QBO MCP README, official Xero MCP & OpenAPI READMEs, Ramp `llms.txt` & `llms-api.txt` (35,019L). |",
        "| `task15-first-pass-001` | `task15-capture-005` | Initial ingest attempt | Rejected (preserved) | Rejected by community-source guard on `83.buildability` and `85.buildability`; preserved untouched. |",
        f"| `{RUN_ID}` | `task15-capture-005` | **Final Task 15 first-pass run** | **Sealed & Validated** | `structure_and_grounding: {validation['structure_and_grounding']}` (`{validation['backend']}`, `10` records, `synthetic: false`, `{ev_checked}` verified evidence refs). |",
        "",
        "## 2. Source-Capture and Claim-Coverage Counts",
        "",
        f"- **Selected Apps**: `10 / 100` (IDs `81–90`; `8` apps with asserted non-identity research; `2` apps honestly preserved as `unknown`: ID `84` Paygent Connect unresolved identity, ID `90` PitchBook blocked HTTP 403)",
        f"- **Captured Snapshots**: `{len(captures)}` live public snapshots (`0` synthetic fixtures); `{fail_count}` failed fetch attempts preserved in `records.json` `fetches`",
        f"- **Eligible Research Assertions (Frozen Inventory)**: `{metrics['overall']['eligible']}` total (`{metrics['by_basis']['observed']['eligible']}` observed documentary, `{metrics['by_basis']['inferred']['eligible']}` inferred; excludes 10 identity claims)",
        f"- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `{metrics['overall']['pending']}` pending, `accuracy: null`",
        "",
        "| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for area in ("identity", "purpose", "auth", "credentials", "api", "mcp", "buildability"):
        report_lines.append(cov_row(area))

    report_lines += [
        "",
        "## 3. Shared Baseline & Sample Integrity Verification",
        "",
        "- **Task 06 Shared Baseline**: Accepted (`research_pipeline.py` `v0.2.0`, Contract `v1.1`, `outputs/task-06/sampling-manifest.json` frozen). No shared pipeline/contract blockers encountered.",
        "- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`) verified byte-for-byte unchanged. Sample apps in this batch (`83` Binance, `84` Paygent Connect) were researched under the same evidence standard as all other apps.",
        "- **Baseline Hashes Verified Unchanged**: `data/apps.json`, `outputs/task-06/sampling-manifest.json`, `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, and `task05-review-002/seal.json`.",
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
        "Rebuild extraction JSON and Task 15 deliverables from sealed capture `task15-capture-005`:",
        "",
        "```powershell",
        ".venv\\Scripts\\python.exe -B work/task-15-agent/build_extraction.py",
        ".venv\\Scripts\\python.exe -B work/task-15-agent/generate_deliverables.py",
        "```",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    # 5. Exceptions for reviewer
    exc_lines = [
        "# Task 15: Exceptions, Unknowns & Review Notes (IDs 81–90)",
        "",
        f"- **Run ID**: `{RUN_ID}`",
        "- **Independent Review**: Pending (no accuracy or human-verification claims).",
        "",
        "## 1. Unresolved Identity — ID 84 (Paygent Connect)",
        "- `data/apps.json` flags Paygent Connect as `identity_status: \"unresolved\"` with original hint `paygent (NMI-powered)` and explicitly warns that legacy lead `paygentglobal.com` has no established identity match.",
        "- Primary web search and captures of `https://www.nmi.com/` and `https://docs.nmi.com/` confirm NMI is a general white-label gateway platform and do **not** link NMI to a product named \"Paygent Connect\" (Japanese Paygent Co., Ltd. is a separate NTT DATA / MUFG NICOS gateway and is not substituted).",
        "- Per `docs/evidence-rules.md`, `84.identity.resolution` and all product-specific claims remain `unknown`.",
        "",
        "## 2. Complete Primary Capture Block — ID 90 (PitchBook)",
        "- All 7 official PitchBook URLs (`pitchbook.com` and `www.pitchbook.com` help/product pages) returned **HTTP 403 (`blocked`)** across `task15-capture-001` through `task15-capture-003` (`fetches[0..6]`).",
        "- Per `docs/evidence-rules.md`, HTTP 403 is not proof of no API/MCP, and third-party/search snippets cannot establish vendor product claims. All PitchBook claims remain `unknown` pending an approved browser/receipt capture path.",
        "",
        "## 3. JS SPA Shells & Attribution Nuance — ID 85 (iPayX)",
        "- Static HTTP captures of `ipayx.ai/docs`, `/docs/api`, `/docs/mcp`, `/api-terms`, and `www.ipayx.ai/` returned a single-line SPA title (`iPayX Protocol — FINTRAC-registered FX forensic audit layer`), and `/pricing` timed out.",
        "- `raw.githubusercontent.com/iPAYX-Technologies/mcp-fx-audit/main/README.md` (105 lines) documents a remote streamable-HTTP MCP server at `https://mcp.ipayx.ai/mcp` (v1.4.0, 4 tools, Bearer key for `full_forensic_fx_report`). Because the vendor-domain SPA did not render a link verifying ownership of the GitHub org, it is conservatively tagged `community_repository` (`origin: \"community\"`) and cited **only** for MCP claims, leaving primary REST API, auth, and pricing as `unknown`.",
        "",
        "## 4. Partial Capture Gaps on Other Apps",
        "- **ID 83 (Binance)**: `developers.binance.com` HTML returned `empty_readable_content` (3 failed fetches); resolved via official GitHub repository `binance/binance-spot-api-docs` (`rest-api.md`, `testnet/general-info.md`, `README.md`). Global production KYC/jurisdictional eligibility remains `unknown`; only a community MCP (`mujeeb8/Binance-MCP`) was found in checked sources.",
        "- **ID 86 (QuickBooks)**: `all-entities` HTML failed (timeout / HTTP 403) and `tos.html` timed out; API resource groups were grounded in Intuit's official `intuit/quickbooks-online-mcp-server` README (29 CRUD entities + 11 financial reports), while API ToS/billing terms remain `unknown`. Note: `mcp-connector.html` describes the \"Intuit Developer Plugin\" AI onboarding assistant rather than a runtime QBO data MCP server.",
        "- **ID 87 (Xero)**: 4 `developer.xero.com/documentation/*` pages rendered as 1-line JS SPA shells; resolved via non-SPA `developer.xero.com/pricing`, `/faq/remote-mcp`, `/faq/custom-integration`, `/faq/getting-started`, and official `XeroAPI/Xero-OpenAPI`, `XeroAPI/xero-node`, and `XeroAPI/xero-mcp-server` repositories. Note upcoming deprecation: new Custom Connection creation closes 1 December 2026.",
        "- **ID 88 (Brex)**: `developer.brex.com/docs/mcp-server` returned HTTP 404; resolved via official `developer.brex.com/docs/mcp.md`. Own-account customers have no sandbox (`api.brex.com` production only), while partner staging (`api-staging.brex.com`) requires partner approval and Unilateral API Access Agreement.",
        "- **ID 89 (Ramp)**: HTML pages under `docs.ramp.com/developer-api/v1/*` are 16-line JS shells; resolved via official `llms.txt`, `llms-api.txt`, and `llms-guides/*.txt`. However, `llms-guides/sandbox-access.txt` had an empty body (4 lines), leaving sandbox approval policy `unknown`. Ramp also references a second `Ramp Data MCP` (benchmarks) in `llms.txt` L55/61 without a captured server URL.",
        "",
        "## 5. Preserved Rejected / Unused Runs",
        "- `task15-capture-004`: network-isolated sandbox capture attempt (unused branch; `task15-capture-005` branched cleanly from `task15-capture-003`).",
        "- `task15-first-pass-001`: rejected ingest where community MCP READMEs were accidentally attached to `83.buildability` and `85.buildability`; fixed in `task15-first-pass-002`.",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    print(f"Generated Task 15 deliverables in {OUT_DIR}")
    print(f"Verified {ev_checked} evidence refs, {len(captures)} captures, {fail_count} failed fetches, 5 baseline hashes.")


if __name__ == "__main__":
    main()
