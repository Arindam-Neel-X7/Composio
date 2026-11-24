"""Save actual pipeline metrics and capture telemetry; no adjudication."""
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p

run_id = 'pilot-first-pass-001'
d = ROOT / 'work/task-04-runs' / run_id
p.verify_seal(d)
result = subprocess.run([sys.executable,'-B',str(ROOT/'research_pipeline.py'),
    '--store',str(ROOT/'work/task-04-runs'),'metrics','--run-id',run_id,'--target',run_id],
    cwd=ROOT,capture_output=True,text=True,check=True)
metrics = json.loads(result.stdout)
records = p.read_json(d/'records.json')
captures = p.read_json(d/'captures.json')
apps = []
for r in records:
    app = r['identity']['id']
    attempts = r['fetches']
    apps.append(dict(id=app,app=r['identity']['app'],category=r['identity']['category'],
        claim_status_counts=dict(Counter(c['status'] for _,c in p.claims(r))),
        captured_sources=[c['spec']['url'] for c in captures if c['spec']['app_id']==app],
        fetch_attempt_status_counts=dict(Counter(f['status'] for f in attempts)),
        failed_attempts=[dict(index=i,**f) for i,f in enumerate(attempts) if f['status']!='fetched'],
        review_status=r['review']['status'],buildability=r['buildability']['value']))
summary = dict(run_id=run_id,synthetic=False,extraction_producer='Task04 research agent, gpt-6.1-sol; researcher-authored structured builder',
    capture_lineage=['pilot-capture-001','pilot-capture-002','pilot-capture-003',run_id],
    selected_source_urls=len(p.read_json(d/'manifest.json')['source_specs']),captured_source_receipts=len(captures),
    source_urls_without_capture=sorted({s['url'] for s in p.read_json(d/'manifest.json')['source_specs']}-{c['spec']['url'] for c in captures}),
    total_claim_status_counts=dict(Counter(c['status'] for r in records for _,c in p.claims(r))),apps=apps,
    validation=p.read_json(d/'validation.json'),
    limitations=['Claims pending independent review; metrics accuracy is null',
        'No authenticated API/MCP execution or paid accounts',
        'Freshdesk main API reference failed capture; exact Basic wire encoding and rate limits not promoted',
        'Google Ads dated migration conflicts with official summaries; developer token requirement disputed',
        'NotebookLM personal community MCP is not Enterprise API proof',
        'Sources are timestamped snapshots, not necessarily pinned repository commits',
        'NotebookLM MCP evidence locator 151-165 establishes server identity and untested Enterprise scope; first tool row starts at 166, so wording lists notebook tools needs a wider locator before relying on it',
        'Independent coordinator review/package remains outside the research agent write scope'])
for name,data in [('metrics.json',metrics),('handoff.json',summary)]:
    p.write_new(Path(__file__).parent/name,p.encoded(data))
assert metrics['overall']['accuracy'] is None
assert metrics['overall']['denominator']==0
assert len(records)==5 and all(r['review']['status']=='pending' for r in records)
assert all(c['spec'].get('fixture') is None for c in captures)
print(json.dumps({k:v for k,v in summary.items() if k not in {'apps','limitations'}},indent=2))
