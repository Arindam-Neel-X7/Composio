"""Deterministic verification for Task 20 self-contained HTML case study."""
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
OUT_HTML = ROOT / "outputs" / "task-20" / "index.html"
ROOT_HTML = ROOT / "index.html"


def main():
    assert OUT_HTML.exists(), f"Missing {OUT_HTML}"
    assert ROOT_HTML.exists(), f"Missing {ROOT_HTML}"

    html_text = OUT_HTML.read_text(encoding="utf-8")
    root_text = ROOT_HTML.read_text(encoding="utf-8")
    assert html_text == root_text, "Root index.html does not match outputs/task-20/index.html"

    # 1. Verify zero external asset references (CSS, JS, images)
    ext_refs = re.findall(r'<(?:script|link|img)[^>]+(?:src|href)=["\']https?://', html_text, re.I)
    assert not ext_refs, f"Found external asset refs: {ext_refs}"

    # 2. Extract and parse embedded APPS JSON
    m = re.search(r"const APPS = (\[.*?\]);\n", html_text, re.S)
    assert m, "Embedded APPS JSON not found"
    apps = json.loads(m.group(1).replace("<\\/", "</"))
    assert len(apps) == 100, f"Expected 100 apps, got {len(apps)}"
    assert len({a["id"] for a in apps}) == 100, "Duplicate app IDs found"

    # 3. Verify exact queue counts match Task 19 aggregates
    q_counts = Counter(a["queue"] for a in apps)
    expected_q = {"build_now": 44, "conditional": 50, "outreach_required": 4, "unknown": 2}
    assert dict(q_counts) == expected_q, f"Queue mismatch: {dict(q_counts)} != {expected_q}"

    # 4. Verify exact MCP category counts match Task 19
    mcp_counts = Counter(a["mcp_category"] for a in apps)
    expected_mcp = {
        "official_only": 66,
        "community_only": 15,
        "official_and_community": 4,
        "not_found_bounded": 11,
        "unknown": 4,
    }
    assert dict(mcp_counts) == expected_mcp, f"MCP mismatch: {dict(mcp_counts)} != {expected_mcp}"

    # 5. Verify exact sample count & Task 18 transitions
    sample_apps = [a for a in apps if a["in_sample"]]
    assert len(sample_apps) == 20, f"Expected 20 sample apps, got {len(sample_apps)}"
    total_transitions = sum(len(a["transitions"]) for a in apps)
    assert total_transitions == 50, f"Expected 50 Task 18 transitions, got {total_transitions}"

    # 6. Verify required acceptance sections & truthful disclosures
    required_strings = [
        "2-Min Overview",
        "100-App Matrix",
        "Headline Findings",
        "Verification",
        "Unknowns",
        "Roadmap",
        "Run Instructions",
        "Limitations",
        "ARINDAM KARMAKAR",
        "84.71%",
        "100.00%",
        "Sample Reuse",
        "not_researched",
        "composio-20app-sample-v1",
    ]
    for needle in required_strings:
        assert needle in html_text, f"Missing expected content: {needle}"

    print("ALL TASK 20 VERIFICATION CHECKS PASSED!")
    print(f"  File size: {OUT_HTML.stat().st_size:,} bytes")
    print(f"  External assets: {len(ext_refs)}")
    print(f"  Embedded apps: {len(apps)}")
    print(f"  Queue counts: {dict(q_counts)}")
    print(f"  MCP counts: {dict(mcp_counts)}")
    print(f"  Sample apps: {len(sample_apps)}, Total Task 18 transitions: {total_transitions}")


if __name__ == "__main__":
    main()
