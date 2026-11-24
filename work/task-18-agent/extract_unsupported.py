import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

with open(ROOT / 'outputs/task-17/human-baseline-judgments.json', 'r', encoding='utf-8') as f:
    base_data = json.load(f)

unsupported_records = []
for app_id, items in base_data['records'].items():
    for it in items:
        if it.get('judgment') == 'unsupported':
            unsupported_records.append((int(app_id), it))

unsupported_records.sort(key=lambda x: (x[0], x[1]['claim_id']))
print(f"Total unsupported claims: {len(unsupported_records)}")

summary = []
for app_id, it in unsupported_records:
    summary.append({
        "app_id": app_id,
        "claim_id": it["claim_id"],
        "original_run_id": it["original_run_id"],
        "human_judgment": it["judgment"],
        "human_reason": it["reason"].strip(),
    })

with open(ROOT / 'work/task-18-agent/unsupported_claims_summary.json', 'w', encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

print("Saved summary to work/task-18-agent/unsupported_claims_summary.json")
