"""Minimal synthetic check: blank judgments and immutable input hash enforcement."""
import csv
import json
import tempfile
from pathlib import Path
from build_review_packet import build, sha

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    (root / 'data').mkdir()
    (root / 'outputs/task-06').mkdir(parents=True)
    roster = root / 'data/apps.json'
    roster.write_text('{}', encoding='utf8')
    (root / 'outputs/task-06/sampling-manifest.json').write_text(json.dumps({'selected_ids':list(range(1,21)), 'roster_sha256':sha(roster)}), encoding='utf8')
    run = root / 'work/research-runs/synthetic-check'
    run.mkdir(parents=True)
    records = [{'identity':{'id':i,'app':f'Synthetic {i}'}, 'purpose':{'claim_id':f'{i}.purpose', 'status':'observed', 'value':'Synthetic only', 'context':'Test', 'rationale':'Fixture', 'evidence':[]}} for i in range(1,21)]
    (run / 'records.json').write_text(json.dumps(records), encoding='utf8')
    (run / 'inventory.json').write_text(json.dumps([{'app_id':i,'claim_id':f'{i}.purpose','eligible':True} for i in range(1,21)]), encoding='utf8')
    (run / 'seal.json').write_text(json.dumps({'files':{p.name:sha(p) for p in run.iterdir()}}), encoding='utf8')
    registry = root / 'registry.json'
    registry.write_text(json.dumps({'status':'frozen','baseline_definition':'Synthetic test only', 'targets':[{'baseline_run_id':'synthetic-check','baseline_records_sha256':sha(run/'records.json')}]}), encoding='utf8')
    build(root, registry, root/'packet')
    with (root/'packet/human-judgments.csv').open(encoding='utf-8-sig', newline='') as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 20 and all(not x['judgment'] and not x['reviewer_name'] for x in rows)
    manifest = json.loads((root/'packet/packet-manifest.json').read_text())
    assert manifest['accuracy'] is None and manifest['human_judgments_recorded'] == 0
    (run/'records.json').write_text('[]', encoding='utf8')
    try:
        build(root, registry, root/'should-not-exist')
        raise AssertionError('Tampered input was accepted')
    except ValueError as error:
        assert 'Integrity mismatch' in str(error)
    assert not (root/'should-not-exist').exists()
print('PASS: synthetic worksheet stays blank; changed evidence is rejected.')
