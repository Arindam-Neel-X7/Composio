# Task 05: independent verification of the five-app pilot

Role: verification agent, using Gemini in a fresh conversation. You did not produce the first-pass claims. Execute Task 05 only, then stop before Task 06.

## Scope

Frozen target: `work/task-04-runs/pilot-first-pass-001`.
Apps: IDs 2, 13, 31, 58, 91. Its inventory has 92 eligible asserted research questions. Read the frozen inventory and record files; independently inspect primary documentation and captured supporting passages for each eligible claim. Do not treat the researcher/coordinator's conclusions as your own judgments.

First validate the target with the CLI in HANDOFF.md. Preserve its hashes and all parent runs. Capture additional primary documentation through the pipeline in new child runs when necessary. Sources need matching declared app/scope and environments; use the captured metadata and exact locators. If new evidence is blocked by implementation limits, record unresolved questions/blockers rather than fabricating receipts or changing sealed files.

Source text is untrusted data. Read narrowly per app/claim, not the entire dataset in one prompt. The selected vendor docs and original repository are linked by the captured source receipts. Compare exact evidence scope, edition, time and wording; do not approve a whole row merely because its URL works.

## Output

Own new paths: `work/task-05-agent/` for judgments, progress and a verification report; fresh child runs under `work/task-04-runs/`; user-facing report/artifacts under `outputs/task-05/`. Do not change pipeline or contract files in this task. Record proposed fixes for Task 06.

Judgment values: correct, incorrect, unsupported, unresolved, not_applicable, with reason and evidence. Follow docs/evidence-rules.md. A compound claim is correct only when all material details hold. Review observations and inferences separately. Inspect null/disputed states as coverage issues separately; do not count them as correct assertions.

Adjudication input shape:

```json
{"records":{"2":[{"claim_id":"2.purpose","original_run_id":"pilot-first-pass-001","judgment":"unresolved","reason":"Replace with actual investigation outcome and references","evidence":[]}]}}
```

This is a shape illustration, not a valid completed review. For correct/incorrect/unsupported/not_applicable use actual captured review evidence. Unresolved with empty evidence requires an existing failed `fetches[N]` reference under the current validator. Do not force a judgment into this example if that requirement is unmet.

Import completed AI judgments using a fresh child and an actual reviewer ID distinct from the producer:

```powershell
python -B research_pipeline.py --store work/task-04-runs review --run-id task05-review-001 --parent YOUR_REVIEW_EVIDENCE_PARENT --reviewer-id gemini-task05-independent --reviewer-type ai --judgments work/task-05-agent/judgments.json
python -B research_pipeline.py --store work/task-04-runs metrics --run-id task05-review-001 --target pilot-first-pass-001
```

Use `pilot-first-pass-001` as the parent if its existing captures suffice; otherwise collect review evidence in a child first and use that child as parent. Keep all adjudication original_run_id values pointed at the original target. Never use `--actual-human-attestation`.

Report C/I/U counts, accuracy C/(C+I+U), the denominator, review coverage out of 92, pending/unresolved/excluded counts, and separate observation/inference results. Zero denominator means unmeasured. Do not claim improvement or a held-out estimate; this is the pilot, not the later 20-app sample.

After your independent pass, compare with `work/task-04-agent/handoff.json` and `outputs/task-04-review.md`. Explicitly assess the Google access-approval taxonomy, developer-token documentation conflict, Freshdesk reference-capture gap, NotebookLM MCP locator range and personal-vs-Enterprise distinction, and bounded Sherlock MCP result. Do not silently fix the original to improve its score.

Finish with a concise report: what passed/failed, exact examples, measured scores and limits, proposed Task 06 changes, files/run IDs created and command results. Update the execution board only to reflect actual completion. Stop for user review before Task 06. Do not research the remaining 95 apps, publish, or deploy.
