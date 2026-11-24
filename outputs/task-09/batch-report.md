# Task 09: Batch 3 Research Report (Communications and Messaging, IDs 21–30)

- **Date**: 2026-11-23
- **Category**: Communications and Messaging (`data/apps.json` IDs `21–30`)
- **Final Sealed Run ID**: `task09-first-pass-004` (`work/research-runs/task09-first-pass-004`)
- **Records SHA-256**: `862f7f1089929460f11ed2310b945ae6698564a763ba59bd82beb7dd63fd9b5e`
- **Seal SHA-256**: `4f9b332cdaacd26cf9a47a1ba471a44857b8cf08ac0d0e0637d2db09a73b0a5b`
- **Pipeline / Contract**: `research_pipeline.py` `v0.2.0` / Contract `v1.1`
- **Independent Review Status**: **Pending** (`accuracy: null`, `review_coverage: 0.0%`). Schema and grounding validation passed, which does **not** establish factual accuracy.

## 1. Run Lineage & Validation Results

| Run ID | Parent | Role | Status | Notes |
| --- | --- | --- | --- | --- |
| `task09-capture-001` | `null` | Initial capture (sandboxed) | Sealed (`0` captures) | Preserves initial sandbox DNS failures per immutable-run rules. |
| `task09-capture-002` | `task09-capture-001` | Network capture recovery (v1) | Sealed (`41` captures) | Approved-network HTTP capture across IDs 21–30 (including 14,067-line Telegram Bot API, 13,223-line Aircall API ref, 10,572-line Zoho Cliq API v2). |
| `task09-capture-003` | `task09-capture-002` | Expanded capture (v2) | Sealed (`51` captures) | Added official Lark Python/Node SDK repos, Pumble Node SDK/landing/help, WhatsApp `llms.txt` + `access-tokens`, Aircall `llms.txt` + retried `tutorials/oauth/`, and Vonage Kiro Power repo. |
| `task09-capture-004` | `task09-capture-003` | Final capture (v3) | Sealed (`54` captures) | Added WhatsApp `app-review.md`, community WhatsApp Business Cloud API MCP (`tkhattar14/whatsapp-business-mcp`), and Aircall AI `llms.txt`. |
| `task09-first-pass-001` | `task09-capture-004` | Initial ingest attempt | Rejected (preserved) | Rejected by primary-evidence guard (community MCP repos cited on non-MCP claims); preserved untouched. |
| `task09-first-pass-002` | `task09-capture-004` | First sealed pass (superseded) | Sealed (preserved) | Validated cleanly, but left unestablished credential booleans as `not_researched` instead of explicit `unknown`; preserved untouched. |
| `task09-first-pass-003` | `task09-capture-004` | Second sealed pass (superseded) | Sealed (preserved) | Audited by independent AI reviewer (`NEEDS FIXES` for 25 claim-grounding/locator defects); preserved untouched. |
| `task09-first-pass-004` | `task09-capture-004` | **Final Task 09 first-pass run** | **Sealed & Validated** | `structure_and_grounding: passed` (`Python jsonschema Draft202012Validator`, `10` records, `synthetic: false`, all 25 audit defects remediated). |

## 2. Source-Capture and Claim-Coverage Counts

- **Selected Apps**: `10 / 100` (IDs `21–30`, all 10 present with asserted non-identity research)
- **Captured Snapshots**: `54` live public snapshots (`0` synthetic fixtures; 3 Lark JS-shell pages excluded from citations); `3` distinct URLs failed in network runs (preserved in `fetches`, never promoted into claims)
- **Eligible Research Assertions (Frozen Inventory)**: `192` total (`172` observed documentary, `20` inferred; excludes 10 identity claims)
- **Review Status**: `0` correct, `0` incorrect, `0` unsupported, `0` unresolved, `192` pending, `accuracy: null`

| Research Area | Observed | Inferred | Unknown | Not Researched | Not Found (Bounded) | Apps w/ Assertions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `identity` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `purpose` | 10 | 0 | 0 | 0 | 0 | 10/10 |
| `auth` | 22 | 0 | 0 | 0 | 0 | 10/10 |
| `credentials` | 52 | 0 | 128 | 0 | 0 | 10/10 |
| `api` | 67 | 10 | 0 | 0 | 0 | 10/10 |
| `mcp` | 21 | 0 | 0 | 12 | 1 | 9/10 |
| `buildability` | 0 | 10 | 0 | 0 | 0 | 10/10 |

## 3. Pilot Overlap & Integrity Verification

- **Pilot Overlap**: None of IDs `21–30` were part of the 5-app Task 04/05 pilot (IDs 2, 13, 31, 58, 91).
- **Frozen 20-App Sample Integrity**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`, SHA-256 `7f8a61110dfebc48e38d6130d3c3ab6a3acf1fbb9b39da5c7a47fae54a731327`) is untouched. All 10 apps in Communications and Messaging were researched to the same documentary standard without preferential treatment for sample apps (`21` Slack, `27` Telegram).
- **Baseline Hash Verification**: `pilot-first-pass-001`, `task05-review-002`, `outputs/task-06/sampling-manifest.json`, `data/apps.json`, `task07-first-pass-003`, and `task08-first-pass-003` all verified byte-for-byte unchanged.

## 4. Reproduction Instructions

Offline validation and metrics replay (no network or API keys required):

```powershell
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs validate --run-id task09-first-pass-004
.venv\Scripts\python.exe -B research_pipeline.py --store work/research-runs metrics --run-id task09-first-pass-004 --target task09-first-pass-004
```

Rebuild extraction JSON from sealed capture `task09-capture-004`:

```powershell
.venv\Scripts\python.exe -B work/task-09-agent/build_extraction.py
```
