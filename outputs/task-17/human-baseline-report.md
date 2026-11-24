# Task 17: Human Baseline Review Report

- **Reviewer Identity**: `ARINDAM KARMAKAR` (type: `human`)
- **Actual Human Attestation**: `True`
- **Reviewed On**: `2026-11-24`
- **Sampling Manifest**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`)
- **Eligible Questions Evaluated**: `327` claims across 20 stratified apps

---

## 1. Measured Baseline Results

| Metric | Total | Observed (Documentary) | Inferred (Synthesized) |
| --- | --- | --- | --- |
| **Eligible Assertions** | 327 | 290 | 37 |
| **Completed Judgments** | 327 | 290 | 37 |
| **Pending** | 0 | 0 | 0 |
| **Correct (C)** | 277 | 277 | 0 |
| **Incorrect (I)** | 0 | 0 | 0 |
| **Unsupported (U)** | 50 | 13 | 37 |
| **Unresolved** | 0 | 0 | 0 |
| **Not Applicable** | 0 | 0 | 0 |
| **Scored Denominator (C+I+U)** | 327 | 290 | 37 |
| **Evidence-Backed Accuracy** | **84.71%** | **95.52%** | **0.00%** |
| **Review Coverage** | 100.00% | 100.00% | 100.00% |

---

## 2. Separate Verification Channels

1. **Channel 1 — AI Consistency Review**: Prior model reviews in Tasks 07–16 established pipeline schema compliance and snapshot locator bounds. They were strictly labeled `reviewer_type: 'ai'` and withheld from the human reviewer during baseline adjudication.
2. **Channel 2 — Automated Browser & Telemetry Checks**: 622 primary snapshots and fetch telemetry were verified byte-for-byte against local SHA-256 digests. Automated checks do not establish factual correctness.
3. **Channel 3 — Actual Human Audit**: Direct verification conducted by `ARINDAM KARMAKAR` against primary vendor documentation URLs and snapshot locators under explicit human attestation.

---

## 3. Immutability and Handoff to Task 18

- Original first-pass answers in `task07-first-pass-003` through `task16-first-pass-001` remain sealed and unaltered.
- Human baseline decisions are permanently preserved in `outputs/task-17/human-baseline-judgments.json` and 10 child review runs (`task17-human-review-07` through `task17-human-review-16`).
- Task 18 error corrections will be authored as immutable child runs without mutating baseline records.
- Final remeasurement in Task 18 will re-evaluate these exact same 327 questions with sample reuse disclosure.
