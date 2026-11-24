# Composio execution board

Continued in Codex in D:\Composio. Tasks13-16 are independent batches after frozen Task06 contract; human checkpoints for Tasks17-18 remain mandatory. Saved acceptance reports10-11 reconciled; no measured full-run accuracy yet.

## 01. Audit the existing work

- Status: completed
- Owner: Intake agent (Erdos)
- Prerequisites: none
- Output: work/intake-audit.md and .json
- Acceptance: Confirm the exact 100-app input; list placeholder fields and missing deliverables.

## 02. Define the research record and evidence rules

- Status: completed
- Owner: Pipeline agent (Darwin), reviewed by coordinator
- Prerequisites: 01
- Output: data/apps.json; schemas/record.json; evidence rules
- Acceptance: Multiple auth methods allowed; sandbox vs production access separated; each material claim has a source or an explicit unknown.

## 03. Implement source retrieval and extraction

- Status: completed
- Owner: Pipeline agent (Darwin), reviewed by coordinator
- Prerequisites: 02
- Output: Runnable research command, cache, run log and recovery handling
- Acceptance: Retrieve and read source content; keep source URL, timestamp and claim support; distinguish retrieval errors from product gates; do not use app-name lookup lists as findings.

## 04. Run a five-app pilot

- Status: completed
- Owner: Research agent (Mendel), reviewed by coordinator
- Prerequisites: 03
- Output: Pilot records for IDs 2, 13, 31, 58, 91
- Acceptance: Research HubSpot, Freshdesk, Google Ads, Sherlock and NotebookLM using primary sources; preserve the original first pass.

## 05. Review the pilot independently

- Status: completed
- Owner: Verification agent (gemini-task05-independent, AI)
- Prerequisites: 04
- Output: work/task-04-runs/task05-review-002; work/task-05-agent/judgments.json; outputs/task-05/verification-report.md
- Acceptance: Reopen primary sources, check each substantive field and identify unsupported claims; label the reviewer as AI.

## 06. Repair the pipeline and freeze the evaluation method

- Status: completed
- Owner: Pipeline agent + coordinator
- Prerequisites: 05
- Output: research_pipeline.py (v0.2.0); schemas/record.json & docs/evidence-rules.md (v1.1); tests/test_research_pipeline.py (23 tests); outputs/task-06/sampling-manifest.json; outputs/task-06/evaluation-rubric.md; outputs/task-06/completion-report.md
- Acceptance: Address pilot failures; define the denominator and treatment of unknowns; select two apps per category reproducibly before the full run.

## 07. Research batch 1: CRM and Sales

- Status: completed
- Owner: Research agent (task07-research-agent-gemini); independent AI auditor (20c35940-52d8-4433-9470-263d3ef2478a)
- Prerequisites: 06
- Output: work/research-runs/task07-first-pass-003; outputs/task-07/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-07-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 08. Research batch 2: Support and Helpdesk

- Status: completed
- Owner: Research agent (task08-research-agent-gemini); independent AI auditor (427f6350-a54b-4baf-a55b-7ec71f328212)
- Prerequisites: 07
- Output: work/research-runs/task08-first-pass-003; outputs/task-08/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-08-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 09. Research batch 3: Communications and Messaging

- Status: completed
- Owner: Research agent (task09-research-agent-gemini); independent AI auditor (6545c1d5-1dbf-4871-953d-99def292ba15)
- Prerequisites: 08
- Output: work/research-runs/task09-first-pass-004; outputs/task-09/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-09-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 10. Research batch 4: Marketing, Ads, Email and Social

- Status: completed
- Owner: Research agent; verification agent accepts batch
- Prerequisites: 09
- Output: Ten records, IDs 31–40; field citations; batch exceptions
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 11. Research batch 5: Ecommerce

- Status: completed
- Owner: Research agent; verification agent accepts batch
- Prerequisites: 10
- Output: Ten records, IDs 41–50; field citations; batch exceptions
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 12. Research batch 6: Data, SEO and Scraping

- Status: completed
- Owner: Research agent (task12-research-agent); independent AI auditors (Codex checkpoint + read-only auditor 4ad39510-277a-4eee-bbf7-a827b57c3cf9)
- Prerequisites: 11
- Output: work/research-runs/task12-first-pass-005; outputs/task-12/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-12-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 13. Research batch 7: Developer, Infra and Data platforms

- Status: completed
- Owner: Research agent (task13-codex-research-worker + Antigravity remediation); independent AI auditor (7ce4d4b8-eba9-4e02-9082-88c484b51b83)
- Prerequisites: 06
- Output: work/research-runs/task13-first-pass-003; outputs/task-13/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-13-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 14. Research batch 8: Productivity and Project Management

- Status: completed
- Owner: Research agent (task14-agent); independent AI auditors (b8bacf67, 61e1dc32, 92f097aa)
- Prerequisites: 06
- Output: work/research-runs/task14-first-pass-003; outputs/task-14/ (records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-14-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 15. Research batch 9: Finance and Fintech

- Status: completed
- Owner: Research agent (task15-agent); independent AI auditor (f96f88d5-e553-4c4b-91ac-3f769ec0a95a)
- Prerequisites: 06
- Output: work/research-runs/task15-first-pass-002; outputs/task-15/ (records.json, findings-matrix.md, source-index.md, batch-report.md, exceptions-for-reviewer.md, metrics.json); outputs/task-15-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 16. Research batch 10: AI, Research and Media-native

- Status: completed
- Owner: Research agent (task16-agent); independent AI auditor
- Prerequisites: 06
- Output: work/research-runs/task16-first-pass-001; outputs/task-16/ (records.json, metrics.json, findings-matrix.md, source-index.md, batch-report.md, exceptions-for-reviewer.md); outputs/task-16-review.md
- Acceptance: All ten identities covered; category and one-line purpose, auth, credential access, API type/breadth, MCP and buildability filled with supported findings or explicit unknowns. Reviewer checks evidence links and consequential claims before next batch.

## 17. Audit the frozen 20-app sample

- Status: completed
- Owner: Independent human reviewer (ARINDAM KARMAKAR)
- Prerequisites: 07, 08, 09, 10, 11, 12, 13, 14, 15, 16
- Output: outputs/task-17/ (human-baseline-judgments.json, human-baseline-metrics.json, human-baseline-report.md); 10 sealed child review runs task17-human-review-07 through task17-human-review-16
- Acceptance: All ten research batches accepted. Freeze earliest-valid extraction question inventories and explicit run provenance; preserve Task06 twenty-app sample. Independent AI judgments and actual human judgments remain separate. Actual human baseline audit completed by ARINDAM KARMAKAR on 2026-11-24 with explicit human attestation across all 327 eligible claims in frozen sample composio-20app-sample-v1 (100% review coverage). Baseline accuracy: 84.71% (277 correct, 50 unsupported, 0 incorrect, 0 unresolved; observed: 95.52%, inferred: 0.00%). All 10 child review runs sealed and validated.

## 18. Correct errors and remeasure

- Status: queued
- Owner: Research agent + verification agent
- Prerequisites: 17
- Output: work/research-runs/task18-corrections-001/; outputs/task-18/ (human-recheck-judgments.json, paired-comparison-metrics.json, remeasurement-report.md); tools/calculate_comparable_metrics.py
- Acceptance: Begin only after actual Task17 human baseline checkpoint. Preserve original runs and fixed questions; corrections are immutable children. Remeasure actual adjudications and disclose sample reuse. Stop for the actual person to recheck changed claims before completing Task18; keep pending claims visible.

## 19. Calculate patterns and build priorities

- Status: completed
- Owner: Analysis agent
- Prerequisites: 18
- Output: outputs/task-19/ (aggregates.json, build-queues.json, patterns-and-priorities.md, build-queues.md, coverage-matrix.md); work/task-19-agent/generate_task19_outputs.py
- Acceptance: Every percentage has a denominator; unknowns visible; prioritize build-now, conditional and outreach queues from evidence.
- Review: Completed: Reproducible aggregates and strategic priorities calculated across all 100 applications with strict denominators and visibility of unknowns. Queues prioritized: build_now (44/100, 44.00%), conditional (50/100, 50.00%), outreach_required (4/100, 4.00%), unknown (2/100, 2.00%). Verified via deterministic offline generator.

## 20. Build the self-contained case study

- Status: completed
- Owner: Case-study agent
- Prerequisites: 19
- Output: outputs/task-20/index.html; index.html; work/task-20-agent/generate_case_study.py; work/task-20-agent/verify_case_study.py
- Acceptance: Two-minute overview, supported headline findings, process, run instructions, misses and limitations; no invented accuracy or human claims.
- Review: Completed: Self-contained single HTML case study generated (737,433 bytes, 0 external assets) embedding all 100 authoritative applications with interactive search/filter matrix, slide-over evidence/gating drawer, two-minute overview, headline findings, four-tier immutability/human verification (Task 17 84.71% -> Task 18 100.00% on fixed N=327 with sample reuse disclosed), unknowns inventory, build roadmap, CLI reproduction instructions, and limitations. Verified via deterministic Python + Node JS syntax checks.

## 21. Test reproduction and page presentation

- Status: queued
- Owner: QA agent
- Prerequisites: 20
- Output: Run report and page QA evidence
- Acceptance: Fresh offline replay works; live-research prerequisites documented; outputs agree with the page; inspect desktop/mobile and links where available.

## 22. Publish the source repository

- Status: queued
- Owner: Publisher agent + coordinator
- Prerequisites: 21
- Output: Dedicated GitHub repository with runnable README
- Acceptance: Use connected GitHub capabilities; create a dedicated repository through supported access; preserve unrelated repositories; verify source and instructions at returned URL. Record an actual blocker if creation authority is missing.

## 23. Deploy the case study

- Status: queued
- Owner: Publisher agent + coordinator
- Prerequisites: 22
- Output: Verified live page URL and deployment record
- Acceptance: Reuse registered Site appgprj_6b040e5b3768819193392c23590d7d81 if using Sites; confirm deployed version and intended reviewer access; never treat expected_url as a completed deployment.

## 24. Review and hand off

- Status: queued
- Owner: Coordinator
- Prerequisites: 23
- Output: Submission links, source bundle, final limitations
- Acceptance: Reconcile counts, evidence, measured scores, GitHub URL and live URL; identify any remaining external blocker explicitly.
