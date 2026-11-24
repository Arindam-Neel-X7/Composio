"""Inspect one app's claims and cited snapshot passages from pilot-first-pass-001."""
import json
import re
import sys
from pathlib import Path

RUN_DIR = Path("work/task-04-runs/pilot-first-pass-001")

def iter_claims(obj, path=()):
    if isinstance(obj, dict):
        if "claim_id" in obj and "status" in obj and "evidence" in obj:
            yield path, obj
        for k, v in obj.items():
            yield from iter_claims(v, path + (k,))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            yield from iter_claims(item, path + (i,))

def read_excerpt(snapshot_ref, locator, pad=3):
    lines = (RUN_DIR / snapshot_ref).read_text(encoding="utf-8").splitlines()
    m = re.fullmatch(r"lines:(\d+)(?:-(\d+))?", locator)
    if not m:
        return f"<invalid locator {locator}>"
    a, b = int(m[1]), int(m[2] or m[1])
    start = max(1, a - pad)
    end = min(len(lines), b + pad)
    out = []
    for ln in range(start, end + 1):
        mark = ">>>" if a <= ln <= b else "   "
        out.append(f"  {mark} {ln}: {lines[ln - 1]}")
    return "\n".join(out)

def main():
    app_id = int(sys.argv[1])
    records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
    rec = next(r for r in records if r["identity"]["id"] == app_id)
    inv = json.loads((RUN_DIR / "inventory.json").read_text(encoding="utf-8"))
    elig_map = {i["claim_id"]: i["eligible"] for i in inv if i["app_id"] == app_id}

    print(f"=== APP {app_id}: {rec['identity']['app']} ({rec['identity']['category']}) ===")
    print(f"Fetches ({len(rec['fetches'])}):")
    for idx, f in enumerate(rec["fetches"]):
        print(f"  fetches[{idx}]: {f['status']} http={f['http_status']} {f['source_url']} err={f['error']}")
    print(f"Conflicts ({len(rec['conflicts'])}):")
    for c in rec["conflicts"]:
        print(f"  {c}")
    print("\n--- CLAIMS ---")
    for path, claim in iter_claims(rec):
        cid = claim["claim_id"]
        elig = elig_map.get(cid, False)
        print(f"\n[{cid}] path={'.'.join(map(str, path))} status={claim['status']} eligible={elig}")
        print(f"  value: {json.dumps(claim['value'], ensure_ascii=False)}")
        print(f"  context: {claim['context']}")
        if claim["supporting_claim_refs"]:
            print(f"  refs: {claim['supporting_claim_refs']}")
        print(f"  rationale: {claim['rationale']}")
        for eidx, ev in enumerate(claim["evidence"]):
            print(f"  ev[{eidx}]: {ev['source_kind']} | {ev['source_url']} | {ev['locator']}")
            print(f"    obs: {ev['observation']}")
            print(read_excerpt(ev["snapshot_ref"], ev["locator"], pad=2))

if __name__ == "__main__":
    main()
