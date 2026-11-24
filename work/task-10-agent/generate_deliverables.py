"""Generate outputs/task-10/ deliverables and run integrity verification."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN_STORE = ROOT / "work/research-runs"
RUN_ID = "task10-first-pass-003"
RUN_DIR = RUN_STORE / RUN_ID
OUT_DIR = ROOT / "outputs/task-10"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
    captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
    manifest = json.loads((RUN_DIR / "manifest.json").read_text(encoding="utf-8"))
    validation = json.loads((RUN_DIR / "validation.json").read_text(encoding="utf-8"))

    # 1. Metrics JSON via pipeline
    metrics_proc = subprocess.run(
        [
            sys.executable, "-B", "research_pipeline.py", "--store", "work/research-runs",
            "metrics", "--run-id", RUN_ID, "--target", RUN_ID,
        ],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    metrics = json.loads(metrics_proc.stdout)
    (OUT_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")

    # 2. Exact copy of ten app records
    shutil.copyfile(RUN_DIR / "records.json", OUT_DIR / "records.json")

    # Verify all 10 IDs, no synthetic flags, all evidence resolves and matches SHA-256
    ids = [r["identity"]["id"] for r in records]
    assert ids == list(range(31, 41)), f"Unexpected IDs: {ids}"
    assert manifest["synthetic"] is False
    assert metrics["synthetic"] is False

    ev_checked = 0
    for r in records:
        assert r["review"]["status"] == "pending", f"Review must be pending for {r['identity']['id']}"

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

    # Verify sealed baseline files untouched (read-only check)
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

    # 3. Source Index
    src_lines = [
        "# Task 10: Source Index (Marketing, Ads, Email and Social, IDs 31–40)",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **Captured Sources**: {len(captures)} live public HTTP snapshots (`synthetic: false`, 0 binary/corrupted snapshots)",
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
        "## Uncaptured / Failed Fetch Attempts (Preserved Telemetry)",
        "",
        "Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence.",
        "",
        "| App ID | App | Status | HTTP | URL | Error |",
        "| ---: | --- | --- | --- | --- | --- |",
    ]
    for aid, name, st, http_st, u, err in failed_rows:
        src_lines.append(f"| {aid} | {name} | `{st}` | `{http_st}` | {u} | {err} |")

    (OUT_DIR / "source-index.md").write_text("\n".join(src_lines) + "\n", encoding="utf-8")

    # 4. Findings Matrix
    mat_lines = [
        "# Task 10: Findings Matrix (Marketing, Ads, Email and Social, IDs 31–40)",
        "",
        f"- **Run ID**: `{RUN_ID}` (contract `v1.1`, pipeline `v0.2.0`, **independent review pending**, `accuracy: null`)",
        f"- **Eligible Assertions**: `{metrics['overall']['eligible']}` (`{metrics['by_basis']['observed']['eligible']}` observed, `{metrics['by_basis']['inferred']['eligible']}` inferred)",
        "",
        "| ID | App | Auth Methods | Testing Access | Production Access | API Protocols / Breadth | MCP Discovery | Buildability |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in records:
        aid = r["identity"]["id"]
        name = r["identity"]["app"]
        auths = ", ".join(x["value"]["method"] for x in r["auth"]["items"] if x["value"])
        t_el = r["credential_eligibility"]["testing"]
        p_el = r["credential_eligibility"]["production"]

        def fmt_el(el):
            parts = []
            for k, lbl in [
                ("free_access", "free"),
                ("trial_access", "trial"),
                ("sandbox_access", "sandbox"),
                ("paid_required", "paid_req"),
                ("vendor_approval_required", "vendor_appr"),
                ("admin_approval_required", "admin_appr"),
                ("self_serve", "self_serve"),
            ]:
                v = el[k]["value"]
                if v is True:
                    parts.append(f"{lbl}=yes")
                elif v is False:
                    parts.append(f"{lbl}=no")
            return ", ".join(parts) or "unknown"

        protos = "/".join(x["value"] for x in r["api_surface"]["protocols"]["items"] if x["value"])
        br = r["api_surface"]["breadth"]["value"] or "unknown"
        if r["mcp"]["discovery"]["status"] == "observed":
            mcp_str = "found (" + ", ".join(f"{e['value']['origin']}" for e in r["mcp"]["entries"]) + ")"
        else:
            mcp_str = r["mcp"]["discovery"]["status"]
        bld = r["buildability"]["value"]["verdict"] if r["buildability"]["value"] else r["buildability"]["status"]
        mat_lines.append(
            f"| {aid} | {name} | {auths} | {fmt_el(t_el)} | {fmt_el(p_el)} | {protos} / `{br}` | `{mcp_str}` | `{bld}` |"
        )

    (OUT_DIR / "findings-matrix.md").write_text("\n".join(mat_lines) + "\n", encoding="utf-8")

    # 5. Exceptions & Unknowns for Independent Reviewer
    exc_lines = [
        "# Task 10: Exceptions, Unknowns & Notes for Independent Reviewer",
        "",
        f"- **Target Run**: `work/research-runs/{RUN_ID}` (independent review **pending**, `accuracy: null`)",
        "- **Frozen 20-App Sample Overlap Disclosure**: Apps **31 (Google Ads)** and **40 (SendGrid)** are in the frozen Task 06 20-app stratified sample (`outputs/task-06/sampling-manifest.json`), and App **31 (Google Ads)** also overlapped with the Task 04/05 pilot (preserved separately under contract v1.0). All Task 10 claims were freshly captured and authored under contract v1.1.",
        "",
        "## 1. Failed / Incomplete HTTP Captures (Telemetry Preserved)",
        "",
        "1. **`task10-capture-001` (sandbox DNS isolation)**: Initial sandboxed run recorded 102 `dns_error` attempts with 0 captures; preserved untouched as parent of live recovery chain `task10-capture-002` -> `task10-capture-005`.",
        "2. **`task10-first-pass-001` (failed intake)**: Rejected by `research_pipeline.py` grounding validator (`MCP URL not present in cited content` on Apps 32, 33, 39). Preserved untouched; fixed locators/URLs ingested into fresh immutable run `task10-first-pass-002`.",
        "3. **4 HTTP 404 URLs preserved in `fetches`**:",
        "   - App 35 (Mailchimp): `https://mailchimp.com/developer/transactional/docs/mcp-server/` (HTTP 404). Note: Mailchimp's Marketing quick-start nav (`L68`) lists an `MCP server` item, but no official Marketing API MCP doc was captured; only the community `AlexlaGuardia/mcp-mailchimp` repository is recorded.",
        "   - App 36 (Klaviyo): `https://developers.klaviyo.com/en/docs/retrieve_api_credentials` (HTTP 404) and `https://raw.githubusercontent.com/klaviyo/klaviyo-mcp-server/main/README.md` (HTTP 404). API key auth and official MCP server are fully grounded in `api_overview` (`912L`), `set_up_oauth` (`592L`), and `klaviyo_mcp_server` (`212L`). Because the literal remote MCP URL did not appear in `klaviyo_mcp_server`, `server_url` is kept `null`.",
        "   - App 38 (Pinterest): `https://raw.githubusercontent.com/terryso/mcp-pinterest/main/README.md` (HTTP 404). Additionally, `https://developers.pinterest.com/docs/api/v5/` rendered as a 9-line JS SPA shell and is **not cited** for any claim; REST/OpenAPI, OAuth, and Trial/Standard tiers are grounded in static `getting-access/`, `access-tiers/`, `set-up-authentication-and-authorization/`, and `pinterest/api-description`.",
        "",
        "## 2. Preserved Unknowns, Path-Dependent Rules & Vendor Doc Discrepancies",
        "",
        "- **125 `unknown` credential eligibility claims preserved** across the 10 apps where primary docs are silent (e.g., `partner_approval_required`, `contact_sales_required`, or pricing/API fee statements for ad networks whose primary revenue is ad spend rather than API subscriptions).",
        "- **App 31 (Google Ads) vendor doc lag**: `access-levels` (`L68-L73`) and `mcp-server` (`L486-L489`) state developer tokens were sunset on September 9, 2026 and access levels are now managed per Google Cloud project, while `oauth/overview` (`L430`) still contains a legacy summary mention of a developer token. Disclosed in `31.auth` notes.",
        "- **App 34 (GoHighLevel) path-dependent vendor approval**: `34.production.vendor_approval_required` is intentionally left `unknown` with explanatory evidence because Public Marketplace OAuth apps require HighLevel approval (`OAuth2.0` `L84`) while Private Integration Tokens are self-generated by agency admins without vendor review (`PrivateIntegrationsToken` `L80-L91`).",
        "- **App 38 (Pinterest) MCP discovery**: Set to `not_found_in_checked_sources` (bounded search of checked Pinterest developer docs and OpenAPI repo; does not assert no MCP exists).",
        "- **Operational checks**: All 10 nested `mcp.*.operational` claims remain `not_researched` (`value: null`); no authenticated API or MCP calls were executed.",
    ]
    (OUT_DIR / "exceptions-for-reviewer.md").write_text("\n".join(exc_lines) + "\n", encoding="utf-8")

    # 6. Batch Completion Report
    rep_lines = [
        "# Task 10: Batch Completion Report (Marketing, Ads, Email and Social, IDs 31–40)",
        "",
        "- **Status**: **Ready for independent review** (`review.status: pending`, `accuracy: null`, `review_coverage: 0.0%`; AI review pending, no human review)",
        f"- **Sealed Target Run**: `work/research-runs/{RUN_ID}`",
        f"- **`records.json` SHA-256**: `{records_sha}`",
        f"- **`seal.json` SHA-256**: `{seal_sha}`",
        f"- **Contract & Pipeline**: Contract `v1.1`, Pipeline `v0.2.0`, `synthetic: false`",
        "",
        "## 1. Run Lineage",
        "",
        "| Run ID | Type | Outcome | Notes |",
        "| --- | --- | --- | --- |",
        "| `task10-capture-001` | Collect (sandbox) | Sealed (0 captures) | Preserves 102 sandbox `dns_error` attempts |",
        "| `task10-capture-002` | Collect (live) | Sealed (48 captures) | Initial live HTTP capture across IDs 31–40 |",
        "| `task10-capture-003` | Collect (live) | Sealed (54 captures) | Added Meta `llms.txt`, Pinterest OpenAPI/tiers, Mailchimp MCP, Threads posts/insights |",
        "| `task10-capture-004` | Collect (live) | Sealed (58 captures) | Added official Meta Ads MCP docs and systeme.io `llms.txt`/getting-started |",
        "| `task10-capture-005` | Collect (live) | Sealed (59 captures) | Added official systeme.io `docs/mcp-server.md` |",
        "| `task10-first-pass-001` | Ingest | Rejected (preserved) | Grounding check caught 3 MCP repo URL mismatches |",
        "| `task10-first-pass-002` | Ingest | Sealed (superseded, preserved) | Initial first-pass extraction; audited by independent AI reviewer |",
        f"| `{RUN_ID}` | Ingest | **Sealed & Validated** | Remediated all 26 audit locator/attachment items; 10 records, 191 eligible assertions, {ev_checked} verified evidence refs |",
        "",
        "## 2. Validation & Metrics Summary",
        "",
        f"- **Schema & Grounding Validation**: `{validation['structure_and_grounding']}` via `{validation['backend']}` (`10/10` records).",
        f"- **Evidence Integrity**: `{ev_checked}` evidence observations verified (`100%` snapshot file existence and SHA-256 match).",
        f"- **Eligible Assertions**: `{metrics['overall']['eligible']}` (`{metrics['by_basis']['observed']['eligible']}` observed, `{metrics['by_basis']['inferred']['eligible']}` inferred); `accuracy: null`, `review_coverage: 0.0%`.",
        f"- **Research Coverage**: 10/10 apps have observed identity, purpose, auth (18 methods), credentials (55 observed, 125 unknown), API surface (69 observed + 10 inferred breadth), and inferred buildability (5 `build_now`, 5 `conditional`); 9/10 apps have `mcp.discovery=found` (5 official + 5 community MCP entries, all 10 `operational_check=not_researched`) and 1/10 (`38 Pinterest`) is `not_found_in_checked_sources`.",
        "- **Baseline Immutability**: Verified `pilot-first-pass-001`, `task05-review-002`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json` SHA-256 hashes unchanged.",
        "",
        "## 3. Deliverables Written",
        "",
        "- `outputs/task-10/records.json`",
        "- `outputs/task-10/metrics.json`",
        "- `outputs/task-10/source-index.md`",
        "- `outputs/task-10/findings-matrix.md`",
        "- `outputs/task-10/exceptions-for-reviewer.md`",
        "- `outputs/task-10/batch-report.md`",
        "- `work/task-10-agent/` (source lists, inspection helpers, `build_extraction.py`, `extracted-001.json`, `generate_deliverables.py`)",
    ]
    (OUT_DIR / "batch-report.md").write_text("\n".join(rep_lines) + "\n", encoding="utf-8")

    print(f"OK: Generated outputs/task-10/ deliverables.")
    print(f"  RUN_ID: {RUN_ID}")
    print(f"  records.json SHA-256: {records_sha}")
    print(f"  seal.json    SHA-256: {seal_sha}")
    print(f"  captures: {len(captures)} | verified evidence refs: {ev_checked} | eligible: {metrics['overall']['eligible']}")


if __name__ == "__main__":
    main()
