# Task 03: reviewed research pipeline

Decision: accepted. Pipeline agent Darwin implemented Task 03. The coordinator reviewed the implementation and usage guide, requested corrections, tested a fresh source copy, and performed independent synthetic integration and public-page retrieval checks. Task 04 has not started.

## Working workflow

1. Select identities from the approved 100-app roster and explicitly supply public source URLs with attribution and scope.
2. Collect actual page content with finite timeouts/retries, extract readable text, save exact text snapshots and SHA-256 hashes, and log outcomes separately from app claims.
3. Produce numbered evidence packets, unresearched record templates and candidate excerpts. Keywords locate passages but do not classify apps.
4. Supply an explicitly configured model adapter or researcher-produced records. Intake validates the approved schema plus capture receipts, quote locations, hashes, paths, identities, scopes, dependencies and correction history.
5. Save a new immutable child run; replay cached sources or recover failed collection in another child. Existing runs cannot be overwritten.
6. Import actual independent review judgments and calculate frozen-target accuracy and coverage. Pending/unknown claims do not become correct answers, and zero denominators remain unmeasured.

## Review findings addressed

- App-count metrics now distinguish selected records from apps with substantive assertions; every synthetic run contributes zero real app findings.
- A run is marked complete only after schema/runtime checks pass. Rejected intake has an incomplete manifest and a failure receipt.
- The same page can support distinct declared scopes; receipt matching uses the referring claim's context.
- Empty/null/malformed extractor output is rejected rather than becoming a collector-style no-op.
- Operational MCP claims remain unresearched because this release does not import actual execution receipts. Documentation is never accepted as proof of a successful tool call.

## Measured checks

- **19/19 regression tests passed** from a fresh copy of the 11-file source package, using the installed full JSON Schema validator; no packages were installed.
- **10/10 independent coordinator integration checks passed**, including 100-app blank initialization, explicit extraction adapter operation, quotation/hash/reference rejection, human-review forgery rejection, replay, overwrite prevention, parent preservation and synthetic metric arithmetic.
- **Live HTTP smoke passed:** the pipeline retrieved example.com with approved access, received HTTP 200, extracted 172 characters over two normalized lines, and matched the text digest. No assignment app record or research run was created by this probe. The default-permission attempt recorded a DNS error; approved execution succeeded.
- **11/11 protected files retained their baseline hashes:** approved Task 02 inputs/format/rules/example and legacy scripts/research artifacts/HTML. README was intentionally updated to explain the new pipeline.

All extraction and review fixtures are synthetic. These results measure pipeline behavior, not app-finding accuracy. No real app research, human verification or measured real-app accuracy is claimed.

## Deliverables and next boundary

The source package includes `research_pipeline.py`, the runnable README, approved roster/schema/evidence rules/example, the usage guide, and the regression suite with synthetic fixtures. Check details are in `task-03/check-results.json`; source files are under `task-03/source/`, with a ZIP alongside them.

The pipeline needs explicitly selected source URLs and either a supplied model adapter or researcher-produced structured records. It has no embedded model credentials, discovery service or Composio SDK integration. Source truth, paraphrase entailment, product identity and actual reviewer identity still need independent review. HTTP-readable content is supported; browser/PDF capture imports, operational execution receipts, sampling, full paired evaluation and publication remain outside this implementation. Changed unversioned source content needs a new versioned URL/branch to preserve citations. Seals are unsigned integrity checksums.

Task 03 is complete. Task 04, the five-app pilot, remains queued.
