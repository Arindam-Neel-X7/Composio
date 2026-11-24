# Task 14: Batch 8 Research Report (Productivity and Project Management, IDs 71–80)

- **Date**: 2026-11-24
- **Category**: Productivity and Project Management (`data/apps.json` IDs `71–80`)
- **Final Sealed Run ID**: `task14-first-pass-003` (`work/research-runs/task14-first-pass-003`)
- **Records SHA-256**: `661013f357d38ff4e725705ff269441daabab68bc33bd9ebbac68d5544d39d17`
- **Seal SHA-256**: `416e8f822365e0cbac3f86fbc524e27f0e2b1f6249b4c17fb0177a70cbf64dc9`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy or human verification.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task14-capture-001` | `null` | Initial live capture | Sealed (`43` captures) | Public HTTP capture across IDs 71–80 (`sources-001.json`); `developers.notion.com/docs/mcp` timed out and several Zendesk/help URLs returned 403/404. |
| `task14-capture-002` | `task14-capture-001` | Expanded capture (v2) | Sealed (`52` captures) | Added 9 captures (`sources-002.json`), including retry success on `developers.notion.com/docs/mcp`, Airtable support docs, ClickUp MCP docs, Coda `?output=1` MCP doc, and Southleft Harvest MCP README. |
| `task14-first-pass-001` | `task14-capture-002` | Initial ingest attempt | Incomplete / Rejected (preserved) | Rejected during validation (`ValueError`); preserved untouched in `work/research-runs/task14-first-pass-001`. |
| `task14-first-pass-002` | `task14-capture-002` | First sealed pass (superseded) | Sealed (preserved) | Audited by independent read-only AI reviewers (`NEEDS FIXES`, 36 items in `outputs/task-14-review.md`); preserved untouched. |
| `task14-first-pass-003` | `task14-first-pass-002` | **Final Task 14 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, `328` verified evidence refs; all 36 independent AI review items remediated). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `71–80`, all 10 present with asserted non-identity research; matched verbatim against `data/apps.json`)
- **Captured Snapshots**: `52` live public snapshots (`0` synthetic fixtures; 2 Airtable 1-line SPA shells preserved in archive and excluded from citations); `7` distinct uncaptured fetch URLs preserved in `fetches` telemetry
- **Eligible Research Assertions (Frozen Inventory)**: `138` total (`117` observed documentary, `21` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `138` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 26 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 13 | 0 | 167 | 0 | 0 | 6/10 |
| `api` | 48 | 11 | 0 | 0 | 0 | 10/10 |
| `mcp` | 20 | 0 | 0 | 10 | 0 | 10/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Shared Baseline & Frozen 20-App Sample Verification

- **Task 06 Baseline Confirmed**: `outputs/task-06-review.md` (`PASS`), `research_pipeline.py` (`v0.2.0`), `schemas/record.json` (`v1.1`), and `docs/evidence-rules.md` (`v1.1`) are accepted and intact; no shared blockers observed.
- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`), and `data/apps.json` all verified byte-for-byte unchanged.
- **Frozen 20-App Sample Members**: App `76` (Monday.com) and App `77` (ClickUp) are in the frozen Task 06 sample. All 10 apps in IDs 71–80 were researched to the same documentary standard.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task14-first-pass-003
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task14-first-pass-003 --target task14-first-pass-003
```

Regenerate `outputs/task-14/` deliverables from the sealed run:

```powershell
.venv\Scripts\python.exe -B work/task-14-agent/generate_deliverables.py
```
