"""Deterministic coordinator acceptance audit for Task 05 completion evidence."""
import hashlib
import json
from collections import Counter
from pathlib import Path


def sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    # 1. Original pilot records, seal, pipeline, and approved contracts unchanged
    rec_sha = sha256("work/task-04-runs/pilot-first-pass-001/records.json")
    seal_sha = sha256("work/task-04-runs/pilot-first-pass-001/seal.json")
    assert rec_sha == "10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90", rec_sha
    assert seal_sha == "eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2", seal_sha

    m04 = json.loads(Path("work/task-04-runs/pilot-first-pass-001/manifest.json").read_text(encoding="utf-8"))
    assert sha256("research_pipeline.py") == m04["tool"]["source_sha256"], "research_pipeline.py changed"
    assert sha256("data/apps.json") == m04["contracts"]["roster"]["sha256"], "data/apps.json changed"
    assert sha256("schemas/record.json") == m04["contracts"]["schema"]["sha256"], "schemas/record.json changed"
    assert sha256("docs/evidence-rules.md") == m04["contracts"]["rules"]["sha256"], "docs/evidence-rules.md changed"
    print("CHECK 1 PASS: Original pilot records/seal, pipeline, and approved contracts unchanged.")

    # 2. Frozen 92-question inventory vs task05-review-002 adjudications
    inv = json.loads(Path("work/task-04-runs/pilot-first-pass-001/inventory.json").read_text(encoding="utf-8"))
    elig = {(i["app_id"], i["claim_id"]): i["status"] for i in inv if i["eligible"]}
    non_elig = {(i["app_id"], i["claim_id"]): i["status"] for i in inv if not i["eligible"]}
    assert len(elig) == 92, f"Expected 92 eligible, got {len(elig)}"

    recs = json.loads(Path("work/task-04-runs/task05-review-002/records.json").read_text(encoding="utf-8"))
    judg_map = {}
    for r in recs:
        aid = r["identity"]["id"]
        rev = r["review"]
        assert rev["status"] == "completed", f"App {aid} not completed"
        assert rev["reviewer"]["type"] == "ai", f"App {aid} not ai"
        assert rev["reviewer"]["id"] == "gemini-task05-independent"
        assert rev["reviewer"]["id"] != m04["producer"]["id"]
        for a in rev["adjudications"]:
            assert a["original_run_id"] == "pilot-first-pass-001"
            assert len(a["evidence"]) >= 1, f"Empty evidence on {a['claim_id']}"
            judg_map[(aid, a["claim_id"])] = a["judgment"]

    assert set(judg_map.keys()) == set(elig.keys()), "Adjudicated claim set != frozen 92 eligible set"
    non_elig_counts = Counter(non_elig.values())
    print(f"CHECK 2 PASS: All 92 eligible claims accounted for (0 pending, 0 extra); non-eligible excluded ({len(non_elig)}: {dict(non_elig_counts)}).")

    # 3. Accuracy arithmetic C/(C+I+U), denominators, separate review coverage, observed vs inferred
    counts = Counter(judg_map.values())
    c, i_cnt, u = counts["correct"], counts["incorrect"], counts["unsupported"]
    unres, na = counts["unresolved"], counts["not_applicable"]
    denom = c + i_cnt + u
    acc = c / denom
    cov = denom / len(elig)

    obs_c = sum(v == "correct" for k, v in judg_map.items() if elig[k] == "observed")
    obs_u = sum(v == "unsupported" for k, v in judg_map.items() if elig[k] == "observed")
    obs_d = sum(elig[k] == "observed" for k in judg_map)
    inf_c = sum(v == "correct" for k, v in judg_map.items() if elig[k] == "inferred")
    inf_u = sum(v == "unsupported" for k, v in judg_map.items() if elig[k] == "inferred")
    inf_d = sum(elig[k] == "inferred" for k in judg_map)

    met = json.loads(Path("work/task-05-agent/metrics.json").read_text(encoding="utf-8"))
    assert met["overall"]["correct"] == c == 87
    assert met["overall"]["incorrect"] == i_cnt == 0
    assert met["overall"]["unsupported"] == u == 5
    assert met["overall"]["unresolved"] == unres == 0
    assert met["overall"]["not_applicable"] == na == 0
    assert met["overall"]["pending"] == 0
    assert met["overall"]["denominator"] == denom == 92
    assert abs(met["overall"]["accuracy"] - acc) < 1e-12
    assert abs(met["overall"]["review_coverage"] - cov) < 1e-12
    assert met["by_basis"]["observed"]["correct"] == obs_c == 62 and met["by_basis"]["observed"]["denominator"] == obs_d == 66
    assert met["by_basis"]["inferred"]["correct"] == inf_c == 25 and met["by_basis"]["inferred"]["denominator"] == inf_d == 26
    print(f"CHECK 3 PASS: Overall {c}/{denom} ({acc:.4%}), coverage {cov:.1%}; observed {obs_c}/{obs_d} ({obs_c/obs_d:.4%}, U={obs_u}); inferred {inf_c}/{inf_d} ({inf_c/inf_d:.4%}, U={inf_u}).")

    # 4. Verify task05-review-001 failure receipt preserved cleanly
    assert Path("work/task-04-runs/task05-review-001/failure.json").exists()
    print("CHECK 4 PASS: AI review labelling, non-empty anchored evidence, and preserved rejected attempt verified.")

    # 5. Check report mentions required issues
    report = Path("outputs/task-05/verification-report.md").read_text(encoding="utf-8")
    for token in (
        "31.production.partner_approval_required",
        "31.auth.developer_token_requirement",
        "developers.freshdesk.com/api/",
        "151-165",
        "166",
        "58.mcp",
        "not_found_in_checked_sources",
        "gemini-task05-independent",
    ):
        assert token in report, f"Missing {token} in verification-report.md"
    print("CHECK 5 PASS: All required Google Ads, Freshdesk, NotebookLM, and Sherlock issues explicitly addressed.")


if __name__ == "__main__":
    main()
