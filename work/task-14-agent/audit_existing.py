import hashlib
import json
import pathlib

def sha256(p: str) -> str:
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

expected = {
    "data/apps.json": "6e3aada149102c2e5539c126aa556c1ceaca3d9d25ca6e0a8f56b3a569f81c19",
    "outputs/task-06/sampling-manifest.json": "7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327",
    "work/task-04-runs/pilot-first-pass-001/records.json": "10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90",
    "work/task-04-runs/pilot-first-pass-001/seal.json": "eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2",
    "work/task-04-runs/task05-review-002/seal.json": "9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f",
}
print("=== BASELINE HASH CHECK ===")
for path, exp in expected.items():
    got = sha256(path)
    print("OK  " if got == exp else "DIFF", path, got[:16])

run_dir = pathlib.Path("work/research-runs/task14-first-pass-002")
caps = json.loads((run_dir / "captures.json").read_text(encoding="utf-8"))
print(f"\n=== SNAPSHOT QUALITY CHECK ({len(caps)} captures) ===")
for c in caps:
    sp = run_dir / c["snapshot_ref"]
    txt = sp.read_text(encoding="utf-8", errors="replace")
    head = " | ".join(l.strip() for l in txt.splitlines()[:3] if l.strip())[:110]
    warn = ""
    low = txt.lower()
    if any(w in low[:1500] for w in ["just a moment", "enable javascript", "access denied", "captcha", "403 forbidden", "page not found"]):
        warn = " [CHECK!]"
    print(f"{c['spec']['app_id']} {c['spec']['kind']:21s} L={c['line_count']:4d} {c['spec']['url']}{warn}")
    if warn or c["line_count"] < 20:
        print("   HEAD:", head)

recs = json.loads((run_dir / "records.json").read_text(encoding="utf-8"))
print("\n=== PER-APP CLAIM SUMMARY ===")
for r in recs:
    aid = r["identity"]["id"]
    app = r["identity"]["app"]
    print(f"\n--- {aid}: {app} ---")
    print("  purpose:", r["purpose"]["status"], "|", r["purpose"]["value"])
    for a in r["auth"]["items"]:
        v = a["value"]
        print(f"  auth {a['claim_id']}: {v['method']} | ctx={v['context'][:60]} | scopes={len(v['scopes'])} | {v['details'][:100]}")
    for env in ("testing", "production"):
        obs = {k: v["value"] for k, v in r["credential_eligibility"][env].items() if k != "context" and v["status"] == "observed"}
        unk = [k for k, v in r["credential_eligibility"][env].items() if k != "context" and v["status"] == "unknown"]
        print(f"  cred.{env}: obs={obs} | unk_n={len(unk)}")
    print("  api.protocols:", [(x["claim_id"], x["value"]) for x in r["api_surface"]["protocols"]["items"]])
    print("  api.public_doc:", r["api_surface"]["public_documentation"]["status"], r["api_surface"]["public_documentation"]["value"])
    print("  api.rgs:", [(x["claim_id"], x["value"][:70]) for x in r["api_surface"]["resource_groups"]["items"]])
    print("  api.breadth:", r["api_surface"]["breadth"]["status"], r["api_surface"]["breadth"]["value"])
    print("  mcp.discovery:", r["mcp"]["discovery"]["status"], r["mcp"]["discovery"]["value"])
    for m in r["mcp"]["entries"]:
        mv = m["value"]
        print(f"  mcp.entry {m['claim_id']}: origin={mv['origin']} name={mv['name']} server={mv['server_url']} repo={mv['repository_url']} op={mv['operational_check']['status']}")
    bv = r["buildability"]["value"]
    print(f"  buildability: {bv['verdict']} | scope={bv['scope'][:80]} | blockers={len(bv['blockers'])}")
    if r["conflicts"]:
        print("  conflicts:", len(r["conflicts"]))
