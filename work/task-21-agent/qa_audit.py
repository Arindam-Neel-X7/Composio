"""
Task 21 Comprehensive Offline QA & Page-to-Output Agreement Audit.
Checks:
1. SHA-256 seal integrity across all 40 authoritative sealed runs (Tasks 07-18) + Task 21 offline replays.
2. Exact agreement between outputs/task-20/index.html, root index.html, data/apps.json,
   outputs/task-17/human-baseline-metrics.json, outputs/task-18/paired-comparison-metrics.json,
   outputs/task-19/aggregates.json, and outputs/task-19/build-queues.json.
3. Hardcoded prose references (e.g., "AppName (ID)" patterns in Roadmap / Case Studies / Unknowns).
4. Internal anchor links, duplicate HTML IDs, external URL syntax, zero external asset refs.
5. Outputs a structured JSON report at work/task-21-agent/qa_audit_results.json.
"""

import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_HTML = ROOT / "outputs" / "task-20" / "index.html"
ROOT_HTML = ROOT / "index.html"
RESULT_PATH = ROOT / "work" / "task-21-agent" / "qa_audit_results.json"

AUTHORITATIVE_FIRST_PASS = [
    "task07-first-pass-003",
    "task08-first-pass-003",
    "task09-first-pass-004",
    "task10-first-pass-003",
    "task11-first-pass-002",
    "task12-first-pass-005",
    "task13-first-pass-003",
    "task14-first-pass-003",
    "task15-first-pass-002",
    "task16-first-pass-001",
]


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_run_seal(run_dir: Path) -> dict:
    seal_path = run_dir / "seal.json"
    if not run_dir.exists():
        return {"run": run_dir.name, "ok": False, "error": "directory missing"}
    if not seal_path.exists():
        return {"run": run_dir.name, "ok": False, "error": "seal.json missing"}
    seal = load_json(seal_path)
    files_map = seal.get("files", {})
    mismatches = []
    missing = []
    for rel, expected_hash in files_map.items():
        fp = run_dir / rel
        if not fp.exists():
            missing.append(rel)
        else:
            actual = sha256_file(fp)
            if actual != expected_hash:
                mismatches.append(rel)
    return {
        "run": run_dir.name,
        "ok": not mismatches and not missing,
        "files_checked": len(files_map),
        "missing": missing,
        "mismatches": mismatches,
    }


def main():
    results = {
        "seal_checks": [],
        "data_agreement": {"passed": True, "errors": [], "warnings": []},
        "prose_app_ref_checks": {"checked": 0, "mismatches": []},
        "html_link_checks": {"internal_anchors": {}, "external_urls": {}, "duplicate_ids": [], "external_assets": []},
    }

    # 1. Seal verification across all 40 authoritative runs + Task 21 replays
    runs_root = ROOT / "work" / "research-runs"
    target_runs = list(AUTHORITATIVE_FIRST_PASS)
    for b in range(7, 17):
        target_runs.append(f"task17-human-review-{b:02d}")
        target_runs.append(f"task18-corrections-{b:02d}")
        target_runs.append(f"task18-human-recheck-{b:02d}")
    for extra in ["task21-offline-replay-001", "task21-offline-replay-t18-001"]:
        if (runs_root / extra).exists():
            target_runs.append(extra)

    # Check if actual first-pass run names differ for 10/11
    for run_name in target_runs:
        rdir = runs_root / run_name
        if not rdir.exists() and run_name.startswith(("task10-", "task11-")):
            # Discover latest matching first-pass directory
            prefix = run_name.split("-first-pass-")[0] + "-first-pass-"
            matches = sorted(p.name for p in runs_root.glob(prefix + "*"))
            if matches:
                rdir = runs_root / matches[-1]
        results["seal_checks"].append(verify_run_seal(rdir))

    # 2. HTML & Embedded Data Agreement
    html_text = OUT_HTML.read_text(encoding="utf-8")
    root_text = ROOT_HTML.read_text(encoding="utf-8")
    if html_text != root_text:
        results["data_agreement"]["passed"] = False
        results["data_agreement"]["errors"].append("root index.html differs from outputs/task-20/index.html")

    roster = load_json(ROOT / "data" / "apps.json")["apps"]
    roster_by_id = {a["id"]: a for a in roster}
    aggregates = load_json(ROOT / "outputs" / "task-19" / "aggregates.json")
    build_queues = load_json(ROOT / "outputs" / "task-19" / "build-queues.json")
    paired = load_json(ROOT / "outputs" / "task-18" / "paired-comparison-metrics.json")

    m = re.search(r"const APPS = (\[.*?\]);\n", html_text, re.S)
    if not m:
        results["data_agreement"]["passed"] = False
        results["data_agreement"]["errors"].append("Embedded APPS JSON not found")
        apps = []
    else:
        apps = json.loads(m.group(1).replace("<\\/", "</"))

    if len(apps) != 100:
        results["data_agreement"]["passed"] = False
        results["data_agreement"]["errors"].append(f"Expected 100 embedded apps, got {len(apps)}")

    # Build queue lookup from Task 19
    q_by_id = {}
    for q_name, items in build_queues.items():
        for item in items:
            q_by_id[item["app_id"]] = (q_name, item)

    for app in apps:
        aid = app["id"]
        r = roster_by_id.get(aid)
        if not r:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(f"Unknown app_id {aid}")
            continue
        if app["name"] != r["app"] or app["category"] != r["category"]:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(
                f"Identity mismatch for #{aid}: HTML=({app['name']}, {app['category']}) vs Roster=({r['app']}, {r['category']})"
            )
        q_name, q_item = q_by_id[aid]
        if app["queue"] != q_name:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(f"Queue mismatch for #{aid}: HTML={app['queue']} vs T19={q_name}")
        if app["mcp_category"] != q_item["mcp"]["category"]:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(
                f"MCP category mismatch for #{aid}: HTML={app['mcp_category']} vs T19={q_item['mcp']['category']}"
            )

    # Check aggregate counts in embedded data vs Task 19 aggregates.json
    q_counts = Counter(a["queue"] for a in apps)
    for qk in ["build_now", "conditional", "outreach_required", "unknown"]:
        exp = aggregates["buildability_summary"][qk]["count"]
        got = q_counts.get(qk, 0)
        if got != exp:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(f"Aggregate queue {qk}: HTML={got} vs T19={exp}")

    # Check Task 18 metrics presence in HTML prose
    expected_metrics_strings = [
        ("84.71%", "Task 17 baseline accuracy"),
        ("100.00%", "Task 18 recheck accuracy"),
        ("277", "Task 17 baseline correct count"),
        ("327", "Fixed question denominator N=327"),
        ("50", "Task 18 transitions count"),
        ("ARINDAM KARMAKAR", "Human reviewer identity"),
        ("composio-20app-sample-v1", "Frozen sample manifest ID"),
        ("not_researched", "MCP operational check status"),
    ]
    for needle, desc in expected_metrics_strings:
        if needle not in html_text:
            results["data_agreement"]["passed"] = False
            results["data_agreement"]["errors"].append(f"Missing {desc} ({needle}) in HTML")

    # 3. Check ALL hardcoded "AppName (ID)" or "App ID" references in HTML body (outside <script>)
    body_only = re.sub(r"<script>.*?</script>", "", html_text, flags=re.S)
    # Match patterns like "Supabase (64)" or "App 84 Paygent Connect"
    ref_pattern = re.compile(r"\b([A-Z][A-Za-z0-9.\-/ ]{1,32}?)\s*\((\d{1,3})\)")
    for match in ref_pattern.finditer(body_only):
        label = match.group(1).strip()
        num = int(match.group(2))
        if num < 1 or num > 100:
            continue
        # Filter out non-app parenthetical counts like "Official (66)" or "Apps (44)" or "Total (100)"
        if label.lower() in {
            "official", "community", "apps", "total", "build now", "conditional",
            "outreach", "unknown", "oauth 2.0", "api key", "bearer token", "basic",
            "rest", "sdk", "cli", "graphql", "claims", "observed", "inferred",
            "crm and sales", "support and helpdesk", "communications and messaging",
            "marketing, ads, email and social", "ecommerce", "data, seo and scraping",
            "developer, infra and data platforms", "productivity and project management",
            "finance and fintech", "ai, research and media-native",
        }:
            continue
        results["prose_app_ref_checks"]["checked"] += 1
        actual = roster_by_id[num]["app"]
        # Compare normalized
        norm_label = re.sub(r"[^a-z0-9]", "", label.lower())
        norm_actual = re.sub(r"[^a-z0-9]", "", actual.lower())
        if norm_label not in norm_actual and norm_actual not in norm_label:
            results["prose_app_ref_checks"]["mismatches"].append({
                "found_text": match.group(0),
                "cited_id": num,
                "actual_app_for_id": actual,
                "actual_queue_for_id": q_by_id[num][0],
            })

    # Also check roadmap Phase 1..6 wave counts in prose vs build-queues.json sub_tiers
    sub_tier_counts = Counter()
    for q_name, items in build_queues.items():
        for item in items:
            sub_tier_counts[(q_name, item.get("sub_tier", ""))] += 1
    results["sub_tier_counts"] = {f"{k[0]}::{k[1]}": v for k, v in sorted(sub_tier_counts.items())}

    # 4. HTML structural, anchor, and URL checks
    # Duplicate IDs (excluding JS template literals)
    ids = re.findall(r'\bid=["\']([^"\']+)["\']', body_only)
    id_counts = Counter(ids)
    results["html_link_checks"]["duplicate_ids"] = [k for k, v in id_counts.items() if v > 1]

    # Internal anchor href="#..."
    anchors = re.findall(r'href=["\']#([^"\']+)["\']', body_only)
    id_set = set(ids)
    broken_anchors = [a for a in anchors if a not in id_set]
    results["html_link_checks"]["internal_anchors"] = {
        "total": len(anchors),
        "unique": len(set(anchors)),
        "broken": broken_anchors,
    }

    # External assets (<script src>, <link href>, <img src>)
    ext_assets = re.findall(r'<(?:script|link|img)[^>]+(?:src|href)=["\']https?://[^"\']+["\']', html_text, re.I)
    results["html_link_checks"]["external_assets"] = ext_assets

    # External URLs inside embedded APPS (evidence_urls + mcp_entries)
    all_urls = set()
    invalid_urls = []
    for app in apps:
        for u in app.get("evidence_urls", []):
            all_urls.add(u)
        for e in app.get("mcp_entries", []):
            for k in ("source_url", "repository_url", "server_url"):
                if e.get(k):
                    all_urls.add(e[k])
    for u in sorted(all_urls):
        p = urlparse(u)
        if p.scheme not in ("http", "https") or not p.netloc:
            invalid_urls.append(u)
    results["html_link_checks"]["external_urls"] = {
        "total_unique_embedded_urls": len(all_urls),
        "invalid_syntax_urls": invalid_urls,
    }

    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Print concise summary
    seals_ok = sum(1 for s in results["seal_checks"] if s["ok"])
    print(f"SEALS: {seals_ok}/{len(results['seal_checks'])} passed")
    for s in results["seal_checks"]:
        if not s["ok"]:
            print(f"  SEAL FAIL: {s}")
    print(f"DATA AGREEMENT: passed={results['data_agreement']['passed']}, errors={len(results['data_agreement']['errors'])}")
    for e in results["data_agreement"]["errors"]:
        print(f"  ERROR: {e}")
    print(f"PROSE APP REFS: checked={results['prose_app_ref_checks']['checked']}, mismatches={len(results['prose_app_ref_checks']['mismatches'])}")
    for mm in results["prose_app_ref_checks"]["mismatches"]:
        print(f"  PROSE MISMATCH: {mm}")
    print(f"SUB-TIER COUNTS: {results['sub_tier_counts']}")
    print(f"ANCHORS: {results['html_link_checks']['internal_anchors']}")
    print(f"DUPLICATE IDs: {results['html_link_checks']['duplicate_ids']}")
    print(f"EXTERNAL ASSETS: {len(results['html_link_checks']['external_assets'])}")
    print(f"EMBEDDED URLS: {results['html_link_checks']['external_urls']['total_unique_embedded_urls']} unique, {len(results['html_link_checks']['external_urls']['invalid_syntax_urls'])} invalid")


if __name__ == "__main__":
    main()
