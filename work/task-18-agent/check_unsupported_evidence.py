import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

with open(ROOT / 'outputs/task-17/human-baseline-judgments.json', 'r', encoding='utf-8') as f:
    base_data = json.load(f)

for app_id, items in base_data['records'].items():
    for it in items:
        if it.get('judgment') == 'unsupported':
            cid = it['claim_id']
            ev_list = it.get('evidence', [])
            print(f"App {app_id:2s} | Claim {cid:30s} | Evidence count: {len(ev_list)}")
            for e in ev_list:
                snap = e.get('snapshot_ref')
                loc = e.get('locator')
                url = e.get('source_url')
                print(f"    loc: {loc} | snap: {snap} | url: {url}")
