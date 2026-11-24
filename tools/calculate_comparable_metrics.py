"""
Comparative metrics calculation utility for Task 18.
Compares Task 17 human baseline review with Task 18 post-correction recheck review
on the exact same frozen 327 claims from composio-20app-sample-v1.
Discloses sample reuse and ensures no accuracy improvement is claimed without measured results.
"""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from research_pipeline import read_json, require, today


def calculate_paired_comparison(baseline_payload: dict, recheck_payload: dict, manifest: dict):
    """Calculate paired before/after metrics on the frozen question inventory."""
    require(isinstance(baseline_payload, dict), "Baseline payload must be a dict")
    require(isinstance(recheck_payload, dict), "Recheck payload must be a dict")

    base_records = baseline_payload.get("records", {})
    recheck_records = recheck_payload.get("records", {})

    # Flatten decisions
    base_decisions = {}
    for app_id, adjs in base_records.items():
        for adj in adjs:
            base_decisions[(int(app_id), adj["claim_id"])] = adj

    recheck_decisions = {}
    for app_id, adjs in recheck_records.items():
        for adj in adjs:
            recheck_decisions[(int(app_id), adj["claim_id"])] = adj

    # Frozen denominator keys
    frozen_keys = set(base_decisions.keys())
    require(frozen_keys, "Baseline has 0 adjudicated claims to compare against")

    def evaluate_set(dec_map, keys):
        c = sum(dec_map.get(k, {}).get("judgment") == "correct" for k in keys)
        i = sum(dec_map.get(k, {}).get("judgment") == "incorrect" for k in keys)
        u = sum(dec_map.get(k, {}).get("judgment") == "unsupported" for k in keys)
        unres = sum(dec_map.get(k, {}).get("judgment") == "unresolved" for k in keys)
        na = sum(dec_map.get(k, {}).get("judgment") == "not_applicable" for k in keys)
        pending = len(keys) - (c + i + u + unres + na)
        denom = c + i + u
        acc = c / denom if denom > 0 else None
        cov = denom / len(keys) if keys else 0.0
        return {
            "eligible": len(keys),
            "correct": c,
            "incorrect": i,
            "unsupported": u,
            "unresolved": unres,
            "not_applicable": na,
            "pending": pending,
            "denominator": denom,
            "accuracy": acc,
            "review_coverage": cov,
        }

    before_metrics = evaluate_set(base_decisions, frozen_keys)
    after_metrics = evaluate_set(recheck_decisions, frozen_keys)

    # Transitions
    transitions = []
    for k in sorted(frozen_keys):
        b_j = base_decisions.get(k, {}).get("judgment", "pending")
        a_j = recheck_decisions.get(k, {}).get("judgment", "pending")
        if b_j != a_j:
            transitions.append(
                {
                    "app_id": k[0],
                    "claim_id": k[1],
                    "before": b_j,
                    "after": a_j,
                    "reason_before": base_decisions.get(k, {}).get("reason", ""),
                    "reason_after": recheck_decisions.get(k, {}).get("reason", ""),
                }
            )

    return {
        "manifest_id": manifest.get("manifest_id"),
        "timestamp": today(),
        "baseline_reviewer": baseline_payload.get("reviewer"),
        "recheck_reviewer": recheck_payload.get("reviewer"),
        "comparable_fixed_questions": len(frozen_keys),
        "before": before_metrics,
        "after": after_metrics,
        "transitions_count": len(transitions),
        "transitions": transitions,
        "sample_reuse_disclosure": (
            "Sample reuse disclosure: this paired remeasurement evaluates a previously audited "
            "sample following targeted corrections; it is a verification of error repair rather "
            "than an unbiased held-out estimate."
        ),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Task 18 Paired Before/After Remeasurement on Fixed Questions"
    )
    parser.add_argument(
        "--baseline",
        type=Path,
        default=ROOT / "outputs/task-17/human-baseline-judgments.json",
        help="Path to Task 17 baseline judgments",
    )
    parser.add_argument(
        "--recheck",
        type=Path,
        default=ROOT / "outputs/task-18/human-recheck-judgments.json",
        help="Path to Task 18 post-correction recheck judgments",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "outputs/task-18/paired-comparison-metrics.json",
        help="Output path for comparison metrics",
    )
    args = parser.parse_args()

    manifest = read_json(ROOT / "outputs/task-06/sampling-manifest.json")

    if not args.baseline.exists():
        print(f"[ERROR] Baseline review file not found: {args.baseline}")
        print("Task 17 baseline human review must be completed and exported first.")
        sys.exit(1)

    if not args.recheck.exists():
        print(f"[ERROR] Recheck review file not found: {args.recheck}")
        print("Task 18 human recheck review must be completed before paired remeasurement.")
        sys.exit(1)

    baseline_payload = read_json(args.baseline)
    recheck_payload = read_json(args.recheck)

    comp = calculate_paired_comparison(baseline_payload, recheck_payload, manifest)
    b = comp["before"]
    a = comp["after"]

    print("\n" + "=" * 60)
    print("TASK 18: PAIRED BEFORE/AFTER REMEASUREMENT REPORT")
    print("=" * 60)
    print(f"Sampling Manifest:       {comp['manifest_id']}")
    print(f"Comparable Questions:    {comp['comparable_fixed_questions']}")
    print(f"Transitions Observed:    {comp['transitions_count']}")
    print("-" * 60)
    print(f"{'Metric':<25} | {'Before (Baseline)':<18} | {'After (Recheck)':<18}")
    print("-" * 60)
    print(
        f"{'Correct (C)':<25} | {b['correct']:<18} | {a['correct']:<18}"
    )
    print(
        f"{'Incorrect (I)':<25} | {b['incorrect']:<18} | {a['incorrect']:<18}"
    )
    print(
        f"{'Unsupported (U)':<25} | {b['unsupported']:<18} | {a['unsupported']:<18}"
    )
    print(
        f"{'Unresolved':<25} | {b['unresolved']:<18} | {a['unresolved']:<18}"
    )
    print(
        f"{'Pending':<25} | {b['pending']:<18} | {a['pending']:<18}"
    )
    print(
        f"{'Scored Denom (C+I+U)':<25} | {b['denominator']:<18} | {a['denominator']:<18}"
    )
    b_acc = f"{b['accuracy']*100:.2f}%" if b["accuracy"] is not None else "null"
    a_acc = f"{a['accuracy']*100:.2f}%" if a["accuracy"] is not None else "null"
    print(f"{'Evidence-Backed Accuracy':<25} | {b_acc:<18} | {a_acc:<18}")
    print(
        f"{'Review Coverage':<25} | {b['review_coverage']*100:.2f}%{'':<11} | {a['review_coverage']*100:.2f}%"
    )
    print("=" * 60)
    print(f"\n{comp['sample_reuse_disclosure']}\n")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(comp, indent=2), encoding="utf-8")
    print(f"Saved comparison metrics to {args.out}")


if __name__ == "__main__":
    main()
