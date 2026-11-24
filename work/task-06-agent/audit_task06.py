"""Independent programmatic audit for Task 06 artifacts."""
import hashlib
import json
from pathlib import Path
import jsonschema


def sha256(path: str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    # 1. Sealed Task 04/05 hashes untouched
    assert sha256("work/task-04-runs/pilot-first-pass-001/records.json") == "10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90"
    assert sha256("work/task-04-runs/pilot-first-pass-001/seal.json") == "eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2"
    assert sha256("work/task-04-runs/task05-review-002/seal.json") == "9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f"
    print("CHECK 1 PASS: Sealed Task 04/05 hashes unchanged.")

    # 2. Schema v1.1 & example check
    schema = json.loads(Path("schemas/record.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    example = json.loads(Path("examples/unresearched-record.json").read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()).validate(example)
    assert schema["properties"]["schema_version"]["const"] == "1.1"
    assert "vendor_approval_required" in schema["$defs"]["eligibility"]["required"]
    print("CHECK 2 PASS: Schema v1.1 valid and validates v1.1 example.")

    # 3. Independent re-derivation of 20-app stratified sample
    manifest = json.loads(Path("outputs/task-06/sampling-manifest.json").read_text(encoding="utf-8"))
    roster_bytes = Path("data/apps.json").read_bytes()
    assert hashlib.sha256(roster_bytes).hexdigest() == manifest["roster_sha256"]
    apps = json.loads(roster_bytes.decode("utf-8-sig"))["apps"]
    by_cat = {}
    for app in apps:
        by_cat.setdefault(app["category"], []).append(app)
    assert len(by_cat) == 10 and all(len(v) == 10 for v in by_cat.values())
    seed = manifest["seed"]
    recomputed = []
    for cat in sorted(by_cat):
        ranked = sorted(
            by_cat[cat],
            key=lambda a: (hashlib.sha256(f"{seed}:{cat}:{a['id']}".encode("utf-8")).hexdigest(), a["id"]),
        )
        recomputed.extend([a["id"] for a in ranked[:2]])
    assert recomputed == manifest["selected_ids"], f"Mismatch: {recomputed} vs {manifest['selected_ids']}"
    assert len(set(recomputed)) == 20
    assert manifest["category_counts"].get("Support and Helpdesk") == 2
    assert manifest["pilot_overlap_disclosure"]["overlapping_ids"] == [31]
    print("CHECK 3 PASS: Independent re-derivation of 20-app sample matches manifest exactly.")


if __name__ == "__main__":
    main()
