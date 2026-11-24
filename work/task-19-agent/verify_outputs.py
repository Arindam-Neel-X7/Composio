import json
from pathlib import Path

out = Path("outputs/task-19")
agg = json.load(open(out / "aggregates.json", encoding="utf-8"))
bq = json.load(open(out / "build-queues.json", encoding="utf-8"))

print("=== Aggregates Check ===")
b_sum = agg["buildability_summary"]
print(f"Total Apps: {b_sum['total_applications']}")
for k in ["build_now", "conditional", "outreach_required", "unknown"]:
    v = b_sum[k]
    print(f"  {k}: {v['count']}/{v['denominator']} ({v['percentage']}%)")

print("\n=== Build Queues Check ===")
q_counts = {k: len(v) for k, v in bq.items()}
print("Queue lengths:", q_counts)
assert sum(q_counts.values()) == 100, f"Expected 100 apps, got {sum(q_counts.values())}"

print("\n=== Coverage Matrix Check ===")
lines = open(out / "coverage-matrix.md", encoding="utf-8").readlines()
matrix_rows = [l for l in lines if l.startswith("|") and not l.startswith("| ID") and not l.startswith("| ---")]
print(f"Matrix rows: {len(matrix_rows)} apps")
assert len(matrix_rows) == 100, f"Expected 100 rows, got {len(matrix_rows)}"

print("\n=== Patterns Report Check ===")
pat_lines = open(out / "patterns-and-priorities.md", encoding="utf-8").readlines()
print(f"Patterns and Priorities line count: {len(pat_lines)} lines")

print("\n=== Build Queues MD Check ===")
bq_lines = open(out / "build-queues.md", encoding="utf-8").readlines()
print(f"Build Queues MD line count: {len(bq_lines)} lines")

print("\n=== ALL VERIFICATION ASSERTIONS PASSED! ===")
