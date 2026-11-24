# Task 16: Batch 10 Research Report (AI, Research and Media-native, IDs 91–100)

- **Date**: 2026-11-23
- **Category**: AI, Research and Media-native (`data/apps.json` IDs `91–100`)
- **Final Sealed Run ID**: `task16-first-pass-001` (`work/research-runs/task16-first-pass-001`)
- **Records SHA-256**: `56aba7c2e67ec24fcd831307c856fb5c2a7d6ebddecd66fc8dbd7623d266429a`
- **Seal SHA-256**: `fc2dbb794eb2f3c80ae95202e02bdbe0f85b419b0c520feffd99e6ee7b66dbdb`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task16-capture-001` .. `task16-capture-007` | chained | Live public HTTP capture sequence | Sealed (`55` captures in `task16-capture-007`) | Iterative primary-source HTTP capture across IDs 91–100 (`synthetic: false`), culminating in `task16-capture-007`. |
| `task16-first-pass-001` | `task16-capture-007` | **Task 16 first-pass extraction** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, `424` verified evidence refs, review pending). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `91–100`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `55` live public snapshots (`0` synthetic fixtures); `12` uncaptured fetch URLs preserved in telemetry
- **Eligible Research Assertions (Frozen Inventory)**: `186` total (`166` observed documentary, `20` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `186` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Applicable | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 22 | 0 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 58 | 0 | 118 | 0 | 4 | 0 | 10/10 |
| `api` | 60 | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `mcp` | 16 | 0 | 0 | 8 | 0 | 2 | 8/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 0 | 10/10 |

## 3. Pilot Overlap (NotebookLM ID 91), Sample Integrity & Baseline Verification

- **Pilot Overlap (App 91 — NotebookLM)**:
  - In Task 05, NotebookLM Enterprise had edition-conflation and citation-attachment findings that motivated Contract v1.1's edition-matching rule for `mcp.discovery` and per-claim locator reinforcement.
  - In `task16-capture-007` and `task16-first-pass-001`, NotebookLM Enterprise (now renamed **Gemini Notebook Enterprise** on Google Cloud) is freshly captured under pipeline v0.2.0 and contract v1.1 with strict edition separation: the personal `developers.google.com/notebook/docs/authentication` Public Preview is explicitly excluded from Enterprise scope, and `91.mcp.discovery` is `not_found_in_checked_sources` rather than conflating personal/community MCPs.
  - Original sealed Task 04/05 pilot runs (`pilot-first-pass-001` and `task05-review-002`) remain byte-for-byte untouched.
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in AI, Research and Media-native were researched to the same documentary standard without preferential treatment for sample apps (`97` higgsfield, `98` Mermaid CLI).
- **Baseline Hash Verification**: `pilot-first-pass-001/records.json`, `pilot-first-pass-001/seal.json`, `task05-review-002/seal.json`, `outputs/task-06/sampling-manifest.json`, and `data/apps.json` all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task16-first-pass-001
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task16-first-pass-001 --target task16-first-pass-001
```

Rebuild extraction JSON and Task 16 deliverables from sealed capture `task16-capture-007`:

```powershell
.venv\Scripts\python.exe -B work/task-16-agent/build_extraction.py
.venv\Scripts\python.exe -B work/task-16-agent/generate_deliverables.py
```
