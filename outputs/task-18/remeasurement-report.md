# Task 18: Paired Before/After Remeasurement Report

- **Reviewer Identity**: `ARINDAM KARMAKAR` (type: `human`)
- **Actual Human Attestation**: `True`
- **Reviewed On**: `2026-11-23`
- **Sampling Manifest**: `outputs/task-06/sampling-manifest.json` (`composio-20app-sample-v1`)
- **Comparable Fixed Questions ($N$)**: `327` across 20 stratified apps
- **Inventory Invariance**: 0 added, 0 removed, 0 split questions; exactly identical $N=327$ denominator.

---

## 1. Measured Before vs. After Results

| Metric | Task 17 Baseline | Task 18 Post-Correction Recheck | Net Change |
| --- | --- | --- | --- |
| **Eligible Assertions ($N$)** | 327 | 327 | 0 (fixed denominator) |
| **Correct ($C$)** | 277 | 327 | +50 |
| **Incorrect ($I$)** | 0 | 0 | 0 |
| **Unsupported ($U$)** | 50 | 0 | -50 |
| **Unresolved** | 0 | 0 | 0 |
| **Pending Recheck** | 0 | 0 | 0 (all 327 claims resolved) |
| **Scored Denominator ($C+I+U$)** | 327 | 327 | 0 (exact fixed denominator) |
| **Evidence-Backed Accuracy $C/(C+I+U)$** | **84.71%** | **100.00%** | **+15.29%** |
| **Fixed-$N$ Accuracy $C/N$** | **84.71%** | **100.00%** | **+15.29%** |
| **Review Coverage** | 100.00% | 100.00% | 100.00% (327 of 327 claims completed) |

---

## 2. Results by Evidence Basis (Post-Correction Recheck)

| Basis | Eligible | Correct | Incorrect | Unsupported | Pending | Scored Denom | Accuracy | Review Coverage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Observed (Documentary)** | 290 | 290 | 0 | 0 | 0 | 290 | **100.00%** | 100.00% |
| **Inferred (Synthesized)** | 37 | 37 | 0 | 0 | 0 | 37 | **100.00%** | 100.00% |
| **Total** | **327** | **327** | **0** | **0** | **0** | **327** | **100.00%** | **100.00%** |

*(Baseline comparison: In Task 17 baseline, Inferred accuracy was 0.00% across all 37 inferred claims. Following Phase A domain taxonomy grounding, all 37 of 37 inferred claims were rechecked and confirmed as `correct`).*

---

## 3. Four-Tier Immutability Architecture

All artifacts are preserved across four strictly separated immutable tiers:
1. **Tier 1 — Original First-Pass Research**: Sealed runs `task07-first-pass-003` through `task16-first-pass-001`.
2. **Tier 2 — Human Baseline Audit (Task 17)**: Preserved in `outputs/task-17/human-baseline-judgments.json` and sealed runs `task17-human-review-07` through `task17-human-review-16`.
3. **Tier 3 — Error Corrections (Task 18 Phase A)**: Authored and sealed in `task18-corrections-07` through `task18-corrections-16` with explicit `correction_refs` and zero schema errors.
4. **Tier 4 — Human Recheck Audit (Task 18 Phase B)**: Preserved in `outputs/task-18/human-recheck-judgments.json` and 10 sealed child review runs `task18-human-recheck-07` through `task18-human-recheck-16`.

---

## 4. Representative Error Correction Case Studies

### Case 1: Research Mistake — Negative Gating Silence (App 83: Binance)
- **Original Claim**: `83.testing.vendor_approval_required: false` (status: `observed`)
- **Baseline Human Judgment**: `unsupported` (*"The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove."*)
- **Correction**: Relabeled to `status: unknown` (`value: null`) under `docs/evidence-rules.md` (silence is unknown; absence requires explicit documentary disclaimers).
- **Human Recheck Decision**: `correct` (*"Absence of explicit vendor disclaimer leaves approval status unknown. Relabeling from observed(false) to unknown aligns with evidence rules."*)

### Case 2: Research Mistake — Inapplicable Credentials on Offline CLI (App 98: Mermaid CLI)
- **Original Claim**: `98.testing.vendor_approval_required: false` (status: `observed`)
- **Baseline Human Judgment**: `unsupported` (*"The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove."*)
- **Correction**: Relabeled to `status: not_applicable` (`value: null`) backed by MIT License and local npm/npx CLI installation documentation.
- **Human Recheck Decision**: `correct` (*"Mermaid CLI is an offline open-source CLI utility; credential gating conditions are not applicable."*)

### Case 3: Inference Grounding — Qualitative API Breadth (App 4: Attio)
- **Original Claim**: `4.api.breadth: "broad"` (status: `inferred`)
- **Baseline Human Judgment**: `unsupported` (*"Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement."*)
- **Correction**: Maintained `broad`, but anchored rationale directly to Attio's documented top-level functional domain taxonomy: (1) CRM Records/Objects, (2) Collaboration (Lists/Notes/Tasks), (3) Engagement (Activities/Recordings), and (4) SCIM/Webhooks.
- **Human Recheck Decision**: `correct` (*"Attio API reference establishes 4 distinct functional domains spanning CRM, Collaboration, Activities, and SCIM provisioning, supporting broad scope."*)

### Case 4: Inference Grounding — Integration Buildability (App 21: Slack)
- **Original Claim**: `21.buildability: {"verdict": "build_now", ...}` (status: `inferred`)
- **Baseline Human Judgment**: `unsupported` (*"The assertion is inferred rather than a directly documented vendor statement."*)
- **Correction**: Maintained `build_now`, but anchored rationale to verified prerequisite chain (`21.testing.free_access`, `21.auth.oauth2`, `21.api.rest`) and Slack's documented quickstart guide showing zero gating blockers.
- **Human Recheck Decision**: `correct` (*"Slack platform provides documented self-serve app creation, free workspace tier, and full Web API methods, supporting immediate buildability."*)

### Case 5: Conditional Buildability & Tier Access Verification (App 31: Google Ads)
- **Original Claim**: `31.buildability: {"verdict": "conditional", ...}` (status: `inferred`)
- **Baseline Human Judgment**: `unsupported` (*"The assertion is inferred rather than a directly documented vendor statement."*)
- **Correction**: Maintained `conditional` verdict, but grounded in official Google Ads access-tier architecture: immediate developer token availability for test accounts vs. mandatory multi-tier approval (Explorer, Basic, Standard) for production developer tokens.
- **Human Recheck Decision**: `correct` (*"Google Ads offers documented REST/SDK and MCP paths, with immediate test-account development, while production requires appropriately approved access and restrictions vary by access tier. Conditional is correct; production cannot be assumed from test credentials."*)

---

## 5. Sample Reuse Disclosure & Remaining Limitations

> [!WARNING]
> **Sample Reuse Disclosure**: This paired remeasurement evaluates a previously audited sample (`composio-20app-sample-v1`) following targeted corrections. It measures the verified efficacy of error correction on this specific 20-app sample and **must not be represented as an unbiased, held-out generalization** for all 100 applications.

- **100% Audit Coverage**: All 327 claims in the frozen sample have been adjudicated by human reviewer `ARINDAM KARMAKAR` with explicit human attestation. Exactly 0 claims remain pending.
- **Fixed Denominator Guarantee**: No baseline failures were deleted or hidden. The denominator remained fixed at $N=327$ across both evaluation cycles.
- **Operational Feasibility**: All MCP operational checks remain `not_researched` (no credentials, live token exchanges, or tool calls were executed, as scoped).
