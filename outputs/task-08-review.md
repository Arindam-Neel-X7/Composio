# Task 08: Independent AI Review Report (Support and Helpdesk, IDs 11–20)

- **Final Verdict**: **PASS** *(initial audit of `task08-first-pass-002` returned `NEEDS FIXES` for 16 claim-level attachment/locator defects plus 2 minor hygiene items; all remediated in immutable run `task08-first-pass-003` and independently re-verified on disk → `PASS`)*
- **Reviewed on**: 2026-11-23
- **Auditor**: Independent read-only AI research subagent (`427f6350-a54b-4baf-a55b-7ec71f328212`, context-isolated; shared model family disclosed). **AI review only; not human review.**
- **Accepted Run**: `work/research-runs/task08-first-pass-003` (`records.json` SHA-256 `b8c75b62b3e4f13478cca5d079e07dc50c4f6faa437d72d3d4cc1749eb23b861`, `seal.json` SHA-256 `e3fe4e7ded6cd1ac8dcd69ff551d209833afa812a40116023862e4cbec3e44d7`)
- **Superseded Run Preserved Untouched**: `work/research-runs/task08-first-pass-002` (`records.json` SHA-256 `af301964f181076bdb624c5204ef6f6260b0e897121b7dde3803cd6f5f2d08d2`, `seal.json` SHA-256 `0b947d47a0d031c53e1f2efa565f0661464e9dbcbf1df3287d638602d5eaa151`)
- **Formal Blind Scoring**: Deferred to Task 17 (20-app stratified sample); `task08-first-pass-003` keeps `review.status == "pending"` and `accuracy: null` (`152` eligible assertions: `133` observed, `19` inferred; `295` verified evidence observations).

---

## 1. Core Verification Checks (All PASS)

| Area | Status | Verified Evidence |
| --- | --- | --- |
| Baseline & prior-run immutability | **PASS** | `pilot-first-pass-001` (`records.json` `10ff5bdb...`, `seal.json` `eaebd62d...`), `task05-review-002` (`seal.json` `9713538d...`), `outputs/task-06/sampling-manifest.json` (`7f8a6111...`), `data/apps.json` (`6e3aada1...`), `task07-first-pass-003` (`records.json` `e22d6ce7...`, `seal.json` `0fe78d44...`), and superseded `task08-first-pass-002` (`records.json` `af301964...`, `seal.json` `0b947d47...`) all verified unchanged. All 69 files in `task08-first-pass-003/seal.json` verified with 0 mismatches. |
| Schema & grounding validation | **PASS** | `research_pipeline.py validate --run-id task08-first-pass-003` passed (`Python jsonschema Draft202012Validator`, contract `v1.1`, `10/10` records matching `data/apps.json` IDs 11–20, `synthetic: false`). |
| Evidence-link & claim grounding | **PASS** | Direct line-by-line inspection of all 10 records against `task08-first-pass-003/snapshots/*.txt` confirmed all 16 material defects and 2 minor hygiene items are resolved with 0 regressions. All 9 nested MCP `operational_check` claims remain `not_researched`, and 0 claims cite the 4 compressed `developer.helpscout.com` snapshots. |
| Deliverables consistency | **PASS** | `outputs/task-08/{records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json}` match `task08-first-pass-003` hashes (`b8c75b62...`, seal `e3fe4e7d...`), counts (`58` captures, `152` eligible, `295` evidence refs), and disclose all 404/compression gaps and AI-only review. |

---

## 2. Remediations Verified on Re-Review (PASS)

1. **App 11 (Zendesk)**: Tightened `11.purpose` (`Support/Ticketing HTTP JSON APIs`) with `ticketing/introduction/` `lines:140-167` attached; expanded `zendesk.com/pricing/` on `11.production.paid_required` to `lines:167-185`; added `11.testing.sandbox_access` and `lines:182-194` to `11.buildability`.
2. **App 12 (Intercom)**: Attached `developers.intercom.com/docs` `lines:18-34` and expanded `intercom.com/pricing` to `lines:50-69` on `12.purpose`; expanded `authentication` to `lines:43-75` (`Authorization:Bearer` at `L74`) on `12.auth.access_token`; expanded `intercom.com/pricing` to `lines:52-95` (`Essential`, `Advanced $85`, `Expert $132`).
3. **App 13 (Freshdesk)**: Attached `oauth-implementation-in-apps/` `lines:35-47` to `13.purpose` to ground `FDK OAuth apps`.
4. **App 14 (Front)**: Expanded `create-and-revoke-api-tokens.md` to `lines:7-46` on `14.auth.api_token`; expanded `reference/introduction` to `lines:10-37` (`Applications` at `L36`); tightened `front.com/pricing` `lines:14-18` and expanded `lines:71-103` (`Billed Annually`, `omnichannel`) with attachment to `14.purpose`.
5. **App 15 (Pylon)**: Narrowed `pylon-mcp.md` `lines:99-100` observation to `callable write tools including create_activity and delete_account`.
6. **App 16 (LiveAgent)**: Attached `061754-Complete-API-reference` `lines:147-147` (`Quality Unit, LLC`) to `16.identity`; expanded `647358-MCP-Integration-for-Agents` to `lines:17-57`; narrowed `liveagent.com/pricing/` `lines:109-160` to `Starter, Team, Business`; removed `status updates` from `16.api.group.conversations_messages` and removed ungrounded `v3 OpenAPI` / `404` blocker text from `16.buildability`.
7. **App 17 (Plain)**: Attached `authentication.md` (`4-21`), `oauth.md` (`55-70`), and `_llms/developer.txt` (`60-116`) to `17.purpose`; expanded `plain.com/pricing` to `lines:1-45` (`Horizon $99`, `Frontier`); removed ungrounded `(e.g., customer:read)` from `17.auth.machine_user_api_key`.
8. **App 18 (Help Scout)**: Removed `Knowledge Base` from `lines:1-16`, attached `helpscout.com/pricing/` `lines:292-335` (`Knowledge base / Docs sites / Reporting`) to `18.purpose`, and removed `up to 5 users` from `lines:68-77`.
9. **App 19 (Gorgias)**: Updated `19.production.paid_required` to cite `gorgias.com/pricing` `lines:140-154` (`L144: 50 to 5,000 tickets a month, never priced per agent`); narrowed `lines:1-18`; attached `reference/introduction` `lines:16-74` and `79-179` to `19.purpose`.
10. **App 20 (Gladly)**: Attached `developer.gladly.com/rest/` `lines:13-66` and `67-134` to `20.purpose`; downgraded `20.production.contact_sales_required` to `unknown` per Contract v1.1; updated `20.buildability` to `conditional` citing `gladly.com/pricing/` `lines:166-169` (`View demo` / `Contact sales`).

---

## 3. Disposition

- **Task 08 status**: Accepted (**PASS**) as `completed` (AI review only; no human review).
- **Next task**: **Task 09 (Research batch 3: Communications and Messaging, IDs 21–30)** remains queued and has not started.
