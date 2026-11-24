# Frozen Evaluation Method & Scoring Rubric (Task 06)

- **Version**: 1.1 (2026-11-23)
- **Applies to**: Full 100-app evaluation (Task 17 first-pass blind audit of the frozen 20-app stratified sample, and Task 18 paired before/after remeasurement)
- **Frozen sampling manifest**: `outputs/task-06/sampling-manifest.json` (`manifest_id: composio-20app-sample-v1`)
- **Contract references**: `schemas/record.json` (v1.1), `docs/evidence-rules.md` (v1.1), `research_pipeline.py` (v0.2.0)

---

## 1. Reproducible 20-App Sampling Method

- **Algorithm**: `stratified-sha256-v1` (implemented in `research_pipeline.py sample`, language- and platform-independent).
- **Input**: `data/apps.json` (100 apps, 10 categories × 10 apps each; verified by `roster_sha256` in the manifest).
- **Selection rule**:
  1. Group all 100 roster apps by `category` in deterministic alphabetical order (covering all 10 categories, including **Support and Helpdesk**).
  2. For each app, compute `rank_hash = sha256(f"{seed}:{category}:{app_id}".encode("utf-8")).hexdigest()`.
  3. Sort ascending by `(rank_hash, app_id)` and select the first `2` apps per category without replacement (`20` apps total).
- **Seed**: `composio-eval-2026-11-23-v1` (fixed before full-run research begins; never re-rolled).
- **Pilot separation**: Task 04/05 pilot results (`pilot-first-pass-001`, `task05-review-002`) remain preserved separately. Any overlap between the deterministic 20-app sample and the 5 pilot apps is explicitly disclosed in `pilot_overlap_disclosure` in `sampling-manifest.json`.

---

## 2. Scoring Unit and Frozen Denominator

- **Scoring unit**: Each eligible asserted claim `(run_id, app_id, claim_id)` recorded in the target run's frozen `inventory.json`, where:
  - `status` is `observed` or `inferred` (non-null value), AND
  - `path[0] != "identity"` (identity metadata/resolution is audited as a prerequisite gate, excluded from the scored research assertion denominator).
- **Granularity**: Each auth method, API protocol, resource group, credential eligibility boolean (`free_access`, `trial_access`, `sandbox_access`, `paid_required`, `admin_approval_required`, `vendor_approval_required`, `partner_approval_required`, `contact_sales_required`, `self_serve`), and MCP entry is a separate claim. Nested `operational_check` claims are scored only if asserted (currently `not_researched`).
- **Compound claims**: A compound claim is judged `correct` **only if every material detail** holds for the declared scope and is anchored in that claim's own attached evidence and locator range. Any unsupported material detail makes the whole claim `unsupported`.

---

## 3. Adjudication Labels and Accuracy Formulas

| Label | Meaning | In Accuracy Denominator? |
| --- | --- | --- |
| `correct` (C) | All material details hold for the declared scope and are anchored in captured primary (or permitted community MCP) evidence. | Yes (numerator & denominator) |
| `incorrect` (I) | Contradicted by primary documentation or factually false for the stated scope/edition. | Yes (denominator only) |
| `unsupported` (U) | Fails to substantiate one or more material details (missing citation, truncated locator, unsupported inference leap, schema taxonomy mismatch, or edition conflation). | Yes (denominator only) |
| `unresolved` | Could not be adjudicated because primary source capture failed (requires `fetches[N]` failure reference if evidence is empty). | No (reported separately) |
| `not_applicable` | Claim does not apply to the stated scope, backed by captured evidence. | No (reported separately; invalid applicability flagged as audit issue) |

### Required Metrics (Always Reported Together)
1. **Evidence-backed accuracy**: `C / (C + I + U)` (`null` / unmeasured if `C + I + U == 0`).
2. **Scored denominator**: `C + I + U`.
3. **Review coverage**: `(C + I + U) / eligible_claims_in_frozen_inventory`, with `pending`, `unresolved`, and `not_applicable` counts reported alongside.
4. **Basis split**: Report `observed` (documentary) and `inferred` accuracy, denominators, and coverage separately.
5. **Treatment of unknowns & null states**: `unknown`, `not_researched`, `disputed`, and `not_found_in_checked_sources` are **never** counted as correct findings and are excluded from `C / (C + I + U)`. They are reported separately under research coverage across all 6 research areas (`purpose`, `auth`, `credentials`, `api`, `mcp`, `buildability`) plus `identity`.

---

## 4. Reviewer Independence & Before/After Policy

- **AI vs. Human**: All model/agent verification is labeled `reviewer_type: "ai"` with a `reviewer_id` distinct from the extraction producer. `--actual-human-attestation` is strictly reserved for an identified human reviewer.
- **Paired remeasurement (Task 18)**: First-pass and corrected scores must reference immutable parent/child runs against the **same frozen question inventory** (`metrics --target <original_run_id>`). Added, removed, split, or scope-changed claims are logged in `changes.json` and reported separately. Do not claim improvement by deleting hard claims, shrinking denominators, or relabeling failures as `unknown`. Disclose that a corrected/previously reviewed sample is no longer an unbiased held-out estimate.
