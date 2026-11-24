import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent

def analyze_buildability():
    # Load 100 apps
    first_pass_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "outputs" / f"task-{t:02d}" / "records.json"
        data = json.load(open(rec_path, "r", encoding="utf-8"))
        recs = data if isinstance(data, list) else data.get("records", [])
        for r in recs:
            first_pass_records[r["identity"]["id"]] = r

    # Load 20 sample corrected apps from Task 18
    corr_records = {}
    for t in range(7, 17):
        rec_path = ROOT / "work" / "research-runs" / f"task18-corrections-{t:02d}" / "records.json"
        if rec_path.exists():
            data = json.load(open(rec_path, "r", encoding="utf-8"))
            recs = data if isinstance(data, list) else data.get("records", [])
            for r in recs:
                corr_records[r["identity"]["id"]] = r

    manifest = json.load(open(ROOT / "outputs" / "task-06" / "sampling-manifest.json", "r", encoding="utf-8"))
    sample_ids = set(manifest.get("selected_ids", []))

    # Helper to get verdict
    def get_verdict(r):
        b = r.get("buildability", {})
        status = b.get("status")
        val = b.get("value")
        if status == "unknown" or val is None:
            return "unknown"
        if isinstance(val, dict):
            return val.get("verdict", "unknown")
        return str(val)

    # 1. 100 apps first-pass
    fp_counts = {}
    for aid, r in sorted(first_pass_records.items()):
        v = get_verdict(r)
        fp_counts[v] = fp_counts.get(v, 0) + 1

    print("--- 100-App First-Pass Buildability Breakdown ---")
    for k, v in sorted(fp_counts.items()):
        print(f"  {k}: {v}/100 ({v/100*100:.1f}%)")

    # 2. Check if any buildability verdict changed in Task 18 corrections
    changed_verdicts = []
    for aid in sample_ids:
        fp_v = get_verdict(first_pass_records[aid])
        co_v = get_verdict(corr_records[aid])
        if fp_v != co_v:
            changed_verdicts.append((aid, fp_v, co_v))
    print(f"\nSample apps with changed buildability verdict in Task 18: {len(changed_verdicts)}")
    for aid, fp_v, co_v in changed_verdicts:
        print(f"  App {aid} ({first_pass_records[aid]['identity']['app']}): {fp_v} -> {co_v}")

    # 3. Authoritative merged dataset (using Task 18 corrections for the 20 sampled apps, first-pass for remaining 80)
    auth_records = {}
    for aid in range(1, 101):
        if aid in corr_records:
            auth_records[aid] = corr_records[aid]
        else:
            auth_records[aid] = first_pass_records[aid]

    auth_counts = {}
    for aid, r in sorted(auth_records.items()):
        v = get_verdict(r)
        auth_counts[v] = auth_counts.get(v, 0) + 1

    print("\n--- 100-App Authoritative (Post-Task 18 Corrections) Buildability Breakdown ---")
    for k, v in sorted(auth_counts.items()):
        print(f"  {k}: {v}/100 ({v/100*100:.1f}%)")

    # List apps by queue in authoritative dataset
    queues = {}
    for aid, r in sorted(auth_records.items()):
        v = get_verdict(r)
        queues.setdefault(v, []).append((aid, r["identity"]["app"], r["identity"]["category"]))
        
    print("\nQueue membership counts:")
    for q, apps in queues.items():
        print(f"  Queue '{q}': {len(apps)} apps")

if __name__ == "__main__":
    analyze_buildability()
