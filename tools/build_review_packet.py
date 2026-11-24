"""Build blank human worksheets from an explicit run registry; never score or attest."""
import argparse
import csv
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def claims(value):
    if isinstance(value, dict):
        if 'claim_id' in value and 'status' in value:
            yield value
        for key, item in value.items():
            if key not in {'evidence', 'review', 'fetches', 'run'}:
                yield from claims(item)
    elif isinstance(value, list):
        for item in value:
            yield from claims(item)


def build(root, registry, output):
    selection = root / 'outputs/task-06/sampling-manifest.json'
    sample = json.loads(selection.read_text(encoding='utf-8-sig'))
    registry_data = json.loads(registry.read_text(encoding='utf-8-sig'))
    if registry_data.get('status') != 'frozen':
        raise ValueError('Evaluation targets must be explicitly frozen before building a human packet')
    targets = registry_data['targets']
    roster_path = root / 'data/apps.json'
    if sha(roster_path) != sample['roster_sha256']:
        raise ValueError('Roster differs from frozen sample')
    selected = set(sample['selected_ids'])
    if len(selected) != 20:
        raise ValueError('Expected frozen twenty-app sample')
    if output.exists():
        raise ValueError('Choose a new output directory; existing packets are immutable')
    records = {}
    for target in targets:
        run = target['baseline_run_id']
        directory = root / 'work/research-runs' / run
        seal = json.loads((directory / 'seal.json').read_text(encoding='utf8'))
        actual = {str(p.relative_to(directory)).replace('\\', '/'): sha(p) for p in directory.rglob('*') if p.is_file() and p.name != 'seal.json'}
        if actual != seal['files']:
            raise ValueError(f'Integrity mismatch: {run}')
        if sha(directory / 'records.json') != target['baseline_records_sha256']:
            raise ValueError(f'Registry hash mismatch: {run}')
        data = json.loads((directory / 'records.json').read_text(encoding='utf8'))
        inventory = json.loads((directory / 'inventory.json').read_text(encoding='utf8'))
        for record in data:
            app = record['identity']['id']
            if app not in selected:
                continue
            if app in records:
                raise ValueError(f'Duplicate sampled app: {app}')
            eligible = {x['claim_id'] for x in inventory if x['app_id'] == app and x['eligible']}
            records[app] = (run, directory, record, eligible)
    if set(records) != selected:
        raise ValueError(f'Missing frozen apps: {sorted(selected-set(records))}')
    output.mkdir(parents=True)
    rows = []
    app_counts = {}
    for app in sample['selected_ids']:
        run, directory, record, eligible = records[app]
        page = [f"# {app}. {record['identity']['app']}", '', f'Baseline: `{run}`. Judgments are intentionally blank.', '', 'Open the primary documents and read the relevant sections yourself. Captured excerpts are a dated backup, not a verified answer. Check every material detail and edition/access scope; do not infer truth from a working URL or a hash.', '']
        for claim in claims(record):
            if claim['claim_id'] not in eligible:
                continue
            evidence = claim['evidence']
            rows.append({'app_id':app, 'app':record['identity']['app'], 'baseline_run_id':run, 'claim_id':claim['claim_id'], 'basis':claim['status'], 'claimed_value':json.dumps(claim['value'], ensure_ascii=False), 'context':claim['context'], 'source_urls':' | '.join(e['source_url'] or '' for e in evidence), 'locators':' | '.join(e['locator'] for e in evidence), 'judgment':'', 'reviewer_name':'', 'reviewed_on':'', 'docs_read_url':'', 'reason':''})
            page += [f"## {claim['claim_id']} ({claim['status']})", '', json.dumps(claim['value'], ensure_ascii=False, indent=2), '', f"Scope: {claim['context']}", '', f"Researcher's rationale: {claim['rationale']}", '']
            for e in evidence:
                snapshot = (directory / e['snapshot_ref']).resolve()
                if not snapshot.is_relative_to(directory.resolve()):
                    raise ValueError('Snapshot escapes run')
                a, _, b = e['locator'].removeprefix('lines:').partition('-')
                start, end = int(a), int(b or a)
                excerpt = snapshot.read_text(encoding='utf8').splitlines()[start-1:end]
                page += [f"Source: {e['source_url']} ({e['source_kind']}; captured {e['captured_on']}; {e['locator']})", '', 'Captured passage:', '', '```text', *[f'{i}: {line}' for i, line in enumerate(excerpt, start)], '```', '']
            page += ['Human judgment: ______  Docs actually read: ______  Reason: ______', '']
        app_counts[str(app)] = len(eligible)
        (output / f'app-{app:03d}.md').write_text('\n'.join(page), encoding='utf8')
    with (output / 'human-judgments.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    manifest = {'status':'awaiting_actual_human_review', 'selection_manifest_sha256':sha(selection), 'target_registry_sha256':sha(registry), 'selected_ids':sample['selected_ids'], 'eligible_claims':len(rows), 'claims_per_app':app_counts, 'human_judgments_recorded':0, 'accuracy':None, 'ai_judgments_included':False, 'baseline_definition':registry_data['baseline_definition'], 'limitations':['Sample known to researchers since Task06, so do not describe it as a concealed held-out set.', 'Earlier AI batch review may have occurred; baseline run provenance must be disclosed.', 'A completed worksheet is not imported as human review until actual person identity and judgments are checked.']}
    (output / 'packet-manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf8')
    (output / 'START-HERE.md').write_text('''# Human verification checkpoint

No human judgments or accuracy scores have been supplied by this tool.

Open each app's worksheet. Read its original primary docs yourself, using the cited section and captured excerpt to locate the question. For each row in human-judgments.csv enter your name, actual review date, docs_read_url, reason, and one judgment: correct, incorrect, unsupported, unresolved, or not_applicable. A compound claim is correct only if every material detail is supported for that scope. Use unsupported when evidence is insufficient; a failed fetch is not proof of a false claim. Leave unchecked rows blank.

Do not consult AI verdicts before recording your own judgments. Return the worksheet to the coordinator for validation and capture of any new evidence. Partial work is welcome but will be reported with its actual coverage. The agent must stop before corrections until you finish or explicitly submit your intended review scope. After corrections, a second human checkpoint will compare the same frozen questions. No automatic human attestation occurs.
''', encoding='utf8')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--registry', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    build(args.root.resolve(), args.registry.resolve(), args.out.resolve())
