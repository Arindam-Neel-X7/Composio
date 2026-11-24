# Task 02: reviewed research format and evidence rules

Decision: accepted. Pipeline agent Darwin completed Task 02. The coordinator read the schema and evidence rules, reviewed the manifest and example, requested revisions, and ran 22 passing format/integrity checks. Task 03 has not started.

## Deliverables

- `data/apps.json`: all 100 audited identities, IDs and categories; original assignment hints and legacy URL leads retain separate provenance. Paygent Connect's identity remains unresolved and its guessed domain is not endorsed.
- `schemas/record.json`: Draft 2020-12 schema covering purpose, multiple auth methods, credential eligibility, API interfaces and breadth, MCP, buildability, conflicts, fetch outcomes, revisions and review.
- `docs/evidence-rules.md`: evidence, migration, review, sampling, accuracy, revision preservation and publication requirements, including the Task 03 runtime handoff.
- `examples/unresearched-record.json`: valid example with unknown/not-researched values; no invented research findings. Excluded from research totals.

Copies of these four deliverables and the check results are in `outputs/task-02/` with the same subdirectory structure.

## Audit findings addressed by the contract

1. Multiple auth methods are separate claims, each with its own evidence. No single auth branch suppresses alternatives.
2. Testing and production access are separate; free, trial, sandbox, paid, admin, partner, contact-sales and self-serve conditions remain independent and scoped.
3. API protocol, documentation visibility, resource groups and qualitative breadth can be known independently. No invented endpoint counts or forced breadth classification.
4. Each asserted claim requires source observations with URLs/locators/capture information. Inferences require reasoning and supporting claim references. Unknown, disputed, not-researched and not-applicable states remain explicit.
5. MCP discovery distinguishes official/community implementations and bounded not-found results; operational success requires an execution log receipt. Missing search results cannot establish global absence.
6. Fetch errors remain separate from product facts. An unresolved review can record a real failed attempt without fabricating an observation.
7. The rules require immutable run IDs, parent/correction references, preserved first-pass records and review history. Existing legacy scripts are not migrated yet.
8. Sampling rules require two apps from each of all ten categories, a seed plus algorithm/version and a frozen claim inventory. No sample was drawn in Task 02.
9. Accuracy is defined with correct/incorrect/unsupported counts and separate coverage/unresolved totals. A zero denominator means unmeasured. AI/human reviews stay distinct; corrected-sample reuse must be disclosed.
10. Publication requires repository/deployment receipts and readback; configuration alone does not establish success.

## Review and checks

All 22 structural/integrity checks passed using installed PowerShell Test-Json; no dependencies were installed. Cases cover honest unknowns, required fields, per-method auth evidence, partial API knowledge, testing/production separation, evidence-free assertion rejection, inference reference requirements, pending/completed review, unresolved adjudication, execution receipt hashes, roster integrity and the Paygent warning. Synthetic fixtures are not real app findings or operational tests.

Eight existing source/output pairs remain byte-identical to the prior deliverable copies. Legacy scripts, research records, verification ledger and HTML were not changed by this task.

JSON Schema checks record structure and local evidence requirements. Evidence truth/relevance, full reference integrity, actual reviewer activity, immutable storage and metric arithmetic still need the Task 03 runtime implementation and later research/review. Current app accuracy remains unmeasured.
