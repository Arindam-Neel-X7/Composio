# Task 15: Batch 9 Research Report (Finance and Fintech, IDs 81–90)

- **Date**: 2026-11-24
- **Category**: Finance and Fintech (`data/apps.json` IDs `81–90`)
- **Final Sealed Run ID**: `task15-first-pass-002` (`work/research-runs/task15-first-pass-002`)
- **Records SHA-256**: `3a82fb00f79ed6bde41e66ad29d34a01e8a1dbd2d92ffa8d52a302bffcdd3f8f`
- **Seal SHA-256**: `ca7e91ab10379502c65d5102b9d97b930234b61cecfd2a3b481f61a61544c65b`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy or human verification.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task15-capture-001` | `null` | Initial live capture | Sealed (preserved) | Initial primary docs and product pages across IDs 81–90. |
| `task15-capture-002` | `task15-capture-001` | Follow-up capture | Sealed (preserved) | Added Plaid Trial/MCP, Binance/iPayX MCP READMEs, Xero FAQs/SDK, Brex `mcp.md`, Ramp `llms-guides/*.txt`. |
| `task15-capture-003` | `task15-capture-002` | Alternate host capture | Sealed (`55` captures, preserved) | Added Ramp `sandbox-access.txt`; retried QBO `all-entities` (403) and PitchBook `www.pitchbook.com` (403). |
| `task15-capture-004` | `task15-capture-003` | Sandboxed capture attempt | Sealed (`55` captures, unused branch) | Ran in network-isolated sandbox; 7 new URLs did not fetch; preserved untouched. |
| `task15-capture-005` | `task15-capture-003` | Final live capture | Sealed (`62` captures) | Added Stripe Connect OAuth, Binance README, official QBO MCP README, official Xero MCP & OpenAPI READMEs, Ramp `llms.txt` & `llms-api.txt` (35,019L). |
| `task15-first-pass-001` | `task15-capture-005` | Initial ingest attempt | Rejected (preserved) | Rejected by community-source guard on `83.buildability` and `85.buildability`; preserved untouched. |
| `task15-first-pass-002` | `task15-capture-005` | **Final Task 15 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, `284` verified evidence refs). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `81–90`; `8` apps with asserted non-identity research; `2` apps honestly preserved as `unknown`: ID `84` Paygent Connect unresolved identity, ID `90` PitchBook blocked HTTP 403)
- **Captured Snapshots**: `62` live public snapshots (`0` synthetic fixtures); `15` failed fetch attempts preserved in `records.json` `fetches`
- **Eligible Research Assertions (Frozen Inventory)**: `168` total (`153` observed documentary, `15` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `168` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 8 | 0 | 2 | 0 | 0 | 8/10 |
| `purpose` | 8 | 0 | 2 | 0 | 0 | 8/10 |
| `auth` | 18 | 0 | 0 | 0 | 0 | 7/10 |
| `credentials` | 60 | 0 | 120 | 0 | 0 | 7/10 |
| `api` | 49 | 7 | 6 | 0 | 0 | 7/10 |
| `mcp` | 18 | 0 | 2 | 10 | 0 | 8/10 |
| `buildability` | 0 | 8 | 2 | 0 | 0 | 8/10 |

## 3. Shared Baseline & Sample Integrity Verification

- **Task 06 Shared Baseline**: Accepted (`research_pipeline.py` `v0.2.0`, Contract `v1.1`, `outputs/task-06/sampling-manifest.json` frozen). No shared pipeline/contract blockers encountered.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`) verified byte-for-byte unchanged. Sample apps in this batch (`83` Binance, `84` Paygent Connect) were researched under the same evidence standard as all other apps.
- **Baseline Hashes Verified Unchanged**: `data/apps.json`, `outputs/task-06/sampling-manifest.json`, `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, and `task05-review-002/seal.json`.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task15-first-pass-002
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task15-first-pass-002 --target task15-first-pass-002
```

Rebuild extraction JSON and Task 15 deliverables from sealed capture `task15-capture-005`:

```powershell
.venv\Scripts\python.exe -B work/task-15-agent/build_extraction.py
.venv\Scripts\python.exe -B work/task-15-agent/generate_deliverables.py
```
