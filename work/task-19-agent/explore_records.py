import json
import os
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

def load_data():
    apps_data = json.load(open(ROOT / "data" / "apps.json", "r", encoding="utf-8"))
    roster_apps = apps_data["apps"]
    
    # 1. Load original first-pass records from outputs/task-07..16
    first_pass_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "outputs" / f"task-{t:02d}" / "records.json"
        if rec_path.exists():
            data = json.load(open(rec_path, "r", encoding="utf-8"))
            recs = data if isinstance(data, list) else data.get("records", [])
            for r in recs:
                first_pass_records[r["identity"]["id"]] = r
                
    # 2. Load Task 18 corrected records from work/research-runs/task18-corrections-*
    corr_records = {}
    for t in range(7, 17):
        corr_dir = ROOT / "work" / "research-runs" / f"task18-corrections-{t:02d}"
        rec_path = corr_dir / "records.json"
        if rec_path.exists():
            data = json.load(open(rec_path, "r", encoding="utf-8"))
            recs = data if isinstance(data, list) else data.get("records", [])
            for r in recs:
                corr_records[r["identity"]["id"]] = r

    # 3. Load sampling manifest (20 apps)
    manifest = json.load(open(ROOT / "outputs" / "task-06" / "sampling-manifest.json", "r", encoding="utf-8"))
    sample_ids = manifest.get("selected_ids", [])
    
    print(f"Roster apps: {len(roster_apps)}")
    print(f"First pass records: {len(first_pass_records)}")
    print(f"Corrected records (sample): {len(corr_records)}")
    print(f"Sample IDs: {sample_ids}")
    
    # Check buildability in first pass
    build_vals = {}
    for aid, r in sorted(first_pass_records.items()):
        b = r.get("buildability", {})
        val = b.get("value")
        status = b.get("status")
        key = f"{status}:{val}"
        build_vals[key] = build_vals.get(key, 0) + 1
    print("\nFirst-pass buildability counts (100 apps):")
    for k, v in sorted(build_vals.items()):
        print(f"  {k}: {v}")
        
    # Check buildability in corrected sample
    corr_build_vals = {}
    for aid, r in sorted(corr_records.items()):
        b = r.get("buildability", {})
        val = b.get("value")
        status = b.get("status")
        key = f"{status}:{val}"
        corr_build_vals[key] = corr_build_vals.get(key, 0) + 1
    print("\nTask 18 Corrected buildability counts (20 apps):")
    for k, v in sorted(corr_build_vals.items()):
        print(f"  {k}: {v}")

    # Check differences in buildability between first-pass and corrected for sample apps
    diffs = []
    for aid in sample_ids:
        fp_b = first_pass_records[aid].get("buildability", {})
        co_b = corr_records[aid].get("buildability", {})
        if fp_b != co_b:
            diffs.append((aid, fp_b, co_b))
    print(f"\nBuildability differences in sample apps between first-pass and Task 18: {len(diffs)}")
    for aid, fp_b, co_b in diffs:
        print(f"  App {aid}: FP={fp_b.get('value')} vs CORR={co_b.get('value')}")

if __name__ == "__main__":
    load_data()
