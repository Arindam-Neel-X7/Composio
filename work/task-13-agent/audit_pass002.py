import hashlib
import json
from pathlib import Path

ROOT = Path("D:/Composio")
RUN_DIR = ROOT / "work/research-runs/task13-first-pass-002"
recs = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
caps = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))

# Check baseline hashes
baselines = {
    "pilot-first-pass-001/records.json": ("work/task-04-runs/pilot-first-pass-001/records.json", "10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90"),
    "pilot-first-pass-001/seal.json": ("work/task-04-runs/pilot-first-pass-001/seal.json", "eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2"),
    "task05-review-002/seal.json": ("work/task-04-runs/task05-review-002/seal.json", "9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f"),
    "outputs/task-06/sampling-manifest.json": ("outputs/task-06/sampling-manifest.json", "7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327"),
    "data/apps.json": ("data/apps.json", "6e3aada149102c2e5539c126aa556c1ceaca3d9d25ca6e0a8f56b3a569f81c19"),
}
for name, (rel, exp) in baselines.items():
    got = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
    print(f"BASELINE {name}: {'OK' if got == exp else 'MISMATCH'}")

# Check task13 runs lineage
for rdir in sorted((ROOT / "work/research-runs").glob("task13-*")):
    mpath = rdir / "manifest.json"
    vpath = rdir / "validation.json"
    spath = rdir / "seal.json"
    m = json.loads(mpath.read_text(encoding="utf-8")) if mpath.exists() else {}
    v = json.loads(vpath.read_text(encoding="utf-8")) if vpath.exists() else {}
    cpath = rdir / "captures.json"
    ncaps = len(json.loads(cpath.read_text(encoding="utf-8"))) if cpath.exists() else 0
    print(f"RUN {rdir.name}: parent={m.get('parent_run_id')} status={m.get('status')} sealed={spath.exists()} captures={ncaps} val={v.get('structure_and_grounding')}")

# Check cited URLs and evidence integrity in task13-first-pass-002
bad_urls = {
    "https://docs.datadoghq.com/account_management/api-app-keys/",
    "https://docs.datadoghq.com/mcp_server/",
    "https://docs.datadoghq.com/account_management/api-app-keys/?_task13=identity",
}
ev_count = 0
bad_cited = []
for r in recs:
    def walk(o):
        global ev_count
        if isinstance(o, dict):
            if "evidence" in o and isinstance(o["evidence"], list):
                for ev in o["evidence"]:
                    ev_count += 1
                    if ev["source_url"] in bad_urls:
                        bad_cited.append((r["identity"]["id"], ev["source_url"]))
                    snap = RUN_DIR / ev["snapshot_ref"]
                    assert snap.exists(), f"Missing {snap}"
                    h = hashlib.sha256(snap.read_bytes()).hexdigest()
                    assert h == ev["content_sha256"], f"Hash mismatch {snap}"
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for x in o:
                walk(x)
    walk(r)

print(f"Evidence refs verified: {ev_count}, bad Datadog HTML cited: {bad_cited}")
print(f"Records SHA-256: {hashlib.sha256((RUN_DIR/'records.json').read_bytes()).hexdigest()}")
print(f"Seal SHA-256:    {hashlib.sha256((RUN_DIR/'seal.json').read_bytes()).hexdigest()}")
