"""Helper to summarize captures, failures, and search snapshot lines."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def summarize(run_id: str):
    d = ROOT / "work/research-runs" / run_id
    caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))
    recs = json.loads((d / "records.json").read_text(encoding="utf-8"))
    print(f"=== CAPTURED ({len(caps)}) ===")
    cap_urls = set()
    for c in sorted(caps, key=lambda x: (x["spec"]["app_id"], x["spec"]["url"])):
        aid = c["spec"]["app_id"]
        u = c["spec"]["url"]
        cap_urls.add((aid, u))
        print(f"  [{aid:2d}] lines={c['line_count']:5d}  {c['snapshot_ref']}  {u}")
    print("=== FAILED ===")
    for r in recs:
        aid = r["identity"]["id"]
        seen = set()
        for f in r["fetches"]:
            u = f["source_url"]
            if (aid, u) not in cap_urls and u not in seen:
                latest = [x for x in r["fetches"] if x["source_url"] == u][-1]
                seen.add(u)
                print(f"  [{aid:2d}] {latest['status']} http={latest['http_status']} {u} -> {latest['error']}")


def dump_app(run_id: str, app_id: int, max_lines: int = 120):
    d = ROOT / "work/research-runs" / run_id
    caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))
    for c in sorted(caps, key=lambda x: x["spec"]["url"]):
        if c["spec"]["app_id"] != app_id:
            continue
        lines = (d / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
        print(f"\n--- [{app_id}] {c['spec']['url']} ({len(lines)} lines, {c['snapshot_ref']}) ---")
        for i, line in enumerate(lines[:max_lines], 1):
            print(f"{i:4d}: {line[:220]}")
        if len(lines) > max_lines:
            print(f"... ({len(lines) - max_lines} more lines)")


def grep_app(run_id: str, app_id: int, terms: list[str], context: int = 2):
    d = ROOT / "work/research-runs" / run_id
    caps = json.loads((d / "captures.json").read_text(encoding="utf-8"))
    terms_l = [t.lower() for t in terms]
    for c in sorted(caps, key=lambda x: x["spec"]["url"]):
        if c["spec"]["app_id"] != app_id:
            continue
        lines = (d / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
        hits = [i for i, l in enumerate(lines) if any(t in l.lower() for t in terms_l)]
        if not hits:
            continue
        print(f"\n--- [{app_id}] {c['spec']['url']} ({len(lines)} lines, {len(hits)} hits) ---")
        shown = set()
        for h in hits[:40]:
            for idx in range(max(0, h - context), min(len(lines), h + context + 1)):
                if idx not in shown:
                    shown.add(idx)
                    print(f"{idx+1:4d}: {lines[idx][:220]}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "summary":
        summarize(sys.argv[2])
    elif cmd == "dump":
        dump_app(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 120)
    elif cmd == "grep":
        grep_app(sys.argv[2], int(sys.argv[3]), sys.argv[4:])
