import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
STORE = ROOT / "work/research-runs"

total_changes = 0
changes_by_type = {}
changes_list = []

for b in range(7, 17):
    run_id = f"task18-corrections-{b:02d}"
    run_dir = STORE / run_id
    val = json.loads((run_dir / "validation.json").read_text(encoding="utf-8"))
    assert val.get("structure_and_grounding") == "passed", f"Run {run_id} validation failed!"
    
    changes = json.loads((run_dir / "changes.json").read_text(encoding="utf-8"))
    total_changes += len(changes)
    for c in changes:
        ch_type = c.get("change")
        changes_by_type[ch_type] = changes_by_type.get(ch_type, 0) + 1
        changes_list.append((b, c))

print(f"Total changes across all 10 child runs: {total_changes}")
print(f"Changes by type: {changes_by_type}")
print("All 10 child runs validated successfully with 0 errors!")

with open(ROOT / "work/task-18-agent/corrections_log.json", "w", encoding="utf-8") as f:
    json.dump({
        "total_corrections": total_changes,
        "by_type": changes_by_type,
        "runs": [f"task18-corrections-{b:02d}" for b in range(7, 17)],
        "changes": [c for _, c in changes_list]
    }, f, indent=2)

print("Saved corrections log to work/task-18-agent/corrections_log.json")
