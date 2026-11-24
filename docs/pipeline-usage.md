# Research pipeline usage and boundaries

Task 06, pipeline version 0.2.0 (contract v1.1; sealed v1.0 runs retain their frozen contracts and validate unchanged). Read `docs/evidence-rules.md` for claim meanings and accuracy policy. This implementation uses Python's standard library plus an already installed full JSON Schema validator. It installs no dependencies. It does not include discovery services, an embedded model, operational tool testing, deployment or GitHub writes. Task 06 added explicit collector guard error codes, configurable `--max-bytes` (up to 10 MB), HTML hydration-blob stripping, `vendor_approval_required` schema support, and deterministic stratified sampling via `sample`.

## What the pipeline does

`collect → packet.json → explicit extraction or researcher intake → validated child run → independent review → metrics`

Collection retrieves actual HTTP response content, strips HTML scripts/styles, normalizes visible text into numbered lines, saves UTF-8 text snapshots, and hashes those exact bytes. It does not infer facts from HTTP status. Public URLs are supplied explicitly: the roster's hints and legacy candidates are never silently promoted into sources. A source-kind declaration is a researcher's attribution assertion, not proof of ownership.

The packet includes the record template/current record, the complete schema/rules, roster provenance, source receipts, numbered text and keyword-selected candidate excerpts with evidence objects. Keywords only help locate text: they never set auth, access, MCP or buildability values. Sources are untrusted text; extractors must not execute instructions found in them. No model is invoked unless the user supplies `--extractor-command-json`.

The pipeline validates the full record using installed Python `jsonschema`, falling back to PowerShell 7 `Test-Json` (Draft 2020-12). If neither is available, it fails with an actionable message. There is no handwritten substitute for JSON Schema. Runtime checks then verify roster identity consistency, claim IDs/references, dependencies/cycles, captured evidence/locators/hashes, dates, scope declarations, source-kind rules, MCP consistency, review targets, corrections and run history.

## Select and collect

All commands use the repository root as working directory. `--store` precedes the subcommand; every child needs a fresh `--run-id`. The default store is `work/research-runs`. For this task's demonstrations/tests use `work/task-03-agent/` only.

```powershell
python -B research_pipeline.py leads --ids 2,13,31,58,91
python -B research_pipeline.py --store work/my-runs collect --run-id capture-001 --ids 2,13 --sources my-public-sources.json --timeout 10 --retries 1 --max-bytes 5000000
python -B research_pipeline.py sample --seed composio-eval-2026-11-23-v1 --per-category 2 --manifest-id composio-20app-sample-v1 --rubric-ref outputs/task-06/evaluation-rubric.md --out outputs/task-06/sampling-manifest.json
```

The first command only displays assignment hints and legacy leads. The second is a future live-research command, not something Task 03 performed. To select all 100, pass `(1..100) -join ','` as the `--ids` argument in PowerShell. A child inherits its parent's selection and contract snapshots.

A source file is an object with a `sources` array. The following is a **synthetic format example**, not a real source endorsement:

```json
{
  "sources": [{
    "app_id": 2,
    "url": "https://synthetic.example/docs",
    "kind": "primary_docs",
    "scope": "SYNTHETIC testing edition v1; no real app facts",
    "environments": ["testing"],
    "attribution_basis": "Synthetic fixture; not vendor documentation",
    "attribution_by": "synthetic-test-author",
    "fixture": "tests/fixtures/vendor.html"
  }]
}
```

For live HTTP capture, omit `fixture`; replace the URL, scope, attribution basis/by and environment metadata using actual research, and omit `--synthetic`. Supported kinds are `primary_docs`, `official_repository`, `official_product_page`, `community_repository`, `community_docs`. Optional `document_version`/`document_date` must be actual source metadata, not guesses. Use `testing`, `production`, both, or neither for environments according to the source scope. These declarations are checked for internal consistency but still need independent factual review.

Local fixture input requires `--synthetic`. Synthetic runs cannot fetch network URLs; descendants stay synthetic. Production intake cannot supply fixture files. The same app/URL can have separate explicit scopes; receipt matching uses the referring claim's context. Within an app/URL/scope, use one consistent attribution declaration. Don't split scopes merely to bypass evidence conflicts. Scope consistency is textual, not semantic.

HTTP has a configurable response size limit (`--max-bytes`, default 2 MB, allowed 100 KB–10 MB, recorded in `manifest.config.max_bytes`), a finite socket/body time budget, at most three retries, and sanitized failure logs using explicit `CaptureError` diagnostic codes (`size_limit_exceeded`, `unsupported_content_type`, `empty_readable_content`, `time_budget_exceeded`, `non_success_status`). The default is 10 seconds and one retry. Retry outcomes are separate fetch attempts; a failed URL creates no supported app claim. A successful capture can still be a login/challenge page and requires researcher inspection. There is no claim of connectivity being globally unavailable: the coordinator demonstrated a public-page fetch under approved execution. Environments can require network approval.

Only public, credential-free documentation URLs are accepted. Userinfo and credential-like query parameter names are rejected. No authorization headers/cookies/API keys are accepted or logged. Do not include secrets in URLs, source declarations, extractor labels, claim text or public page contents: arbitrary text cannot be reliably secret-scanned. Adapter argv/env/stdout errors are not logged; use environment variables or your own credential store inside your explicitly selected adapter. Don't put credentials in argv.

## Read packets and provide extraction

Each collected run contains `packet.json`. `packet --run-id <id>` prints that same JSON to stdout without network or mutation. An extractor receives this object on stdin and must output exactly one JSON object containing a `records` array, with all selected records in their original order. The array must follow the supplied Task 02 schema. An empty object, null, wrong type or missing records is an error, not a successful no-op extraction.

```powershell
python -B research_pipeline.py --store work/my-runs ingest --run-id extracted-001 --parent capture-001 --claims researched-records.json --reason 'Initial extraction; researcher/tool and version recorded here'
```

`ingest` reads a researcher-produced `{"records": [...]}` file. It accepts no invented snapshots or fetch attempts. Use stable app-prefixed claim IDs, exact source scope strings as claim contexts, and evidence copied from actual capture receipts. Keep the review pending. The pipeline assigns child run metadata and correction references; extractor-supplied run metadata is not trusted for lineage.

For your own model backend, supply a JSON argv array, not a shell command:

```powershell
$adapter = ConvertTo-Json -Compress -InputObject @('python', '-B', 'your_extractor.py')
python -B research_pipeline.py --store work/my-runs extract --run-id extracted-001 --parent capture-001 --reason 'Initial extraction' --extractor-label 'your-model-and-adapter-version' --extractor-command-json $adapter --extractor-timeout 60
```

The adapter runs only when explicitly requested, with `shell=False` and a bounded process timeout (1–300 seconds). It is trusted executable code selected by the user, not code discovered in a document. The pipeline supplies no model credentials. The adapter handles its own backend and should produce no credentials in records. Its non-secret model/tool/version label is recorded in the manifest. Nonzero exit, timeout, invalid JSON, schema failure or grounding failure rejects intake. Output/stderr are not persisted on failure. `tests/fixtures/synthetic_extractor.py` documents a runnable adapter example and refuses real packets; it is a fixture, not a general research model.

## Evidence intake requirements

This pipeline intentionally accepts only evidence with captured local snapshots and receipts, even though the schema permits a documented missing hash for other workflows. This is a stricter supported intake subset, not a change to Task 02. Browser captures, PDF parsing, JavaScript-only pages and external execution receipts need a future explicit receipt-import path; do not fabricate a local file to bypass it.

- A claim's evidence must match its selected app, source URL/kind, capture date/method, content digest, local path, document metadata and declared scope. Locators are `lines:N` or `lines:N-M` in the normalized text. Evidence from an uncaptured URL or path outside the run is rejected.
- Prefix captured literal observations `quote: `: their exact text must occur inside the cited lines. Prefix researcher paraphrases `paraphrase: `: the code cannot establish their entailment; reviewers must read the cited source. These prefixes distinguish quotation from interpretation without modifying the schema.
- Auth methods, protocols, resource groups and MCP entries are independently cited claims. Unknown API breadth does not discard a supported protocol. Product claims need primary content; community evidence can support MCP implementations, not unrelated product facts. Assignment hints are never substantive evidence.
- Product-specific assertions require an observed, source-supported identity resolution. For an identity flagged unresolved in the roster, the resolution rationale must explicitly reconcile the preserved original hint. This is a consistency gate plus researcher attribution, **not factual identity proof**. No Paygent domain is automatically endorsed. An investigator still has to establish the actual product match.
- Claim references must resolve within the app; unsupported dependencies, duplicates, self-support and cycles fail. Buildability requires identity plus API/MCP support; `build_now` additionally needs auth and credential support. Breadth must be inferred from resource-group claims. The code cannot decide whether all blockers, permissions or business prerequisites have been discovered.
- Credential evidence must declare the matching testing/production environment. Equivalent scopes and account conditions are not inferred automatically. A context string must equal the source scope, so give differently scoped sources/claims separate IDs.
- MCP discovery needs supported observed entries; each entry must explicitly say callable server direction and have source-backed origin/URLs. Matching words and URL presence are consistency checks, not proof the server works or that vendor endorsement is authentic. Operational checks must remain `not_researched`: this version cannot import authenticated execution receipts or perform operational tests, although the schema permits future receipt intake.

Malformed dates/URLs, invented snapshots/hashes, inappropriate source kinds, asserted items under unresearched collections, or undocumented official MCP origin fail validation. Structurally well-formed but false paraphrases and wrong source attribution can still pass: they need independent AI/person review. Validation never automatically signs factual verification or human review.

## Immutable runs, replay and recovery

A run stores `manifest.json`, `records.json`, `captures.json`, `snapshots/`, `packet.json`, `inventory.json`, `changes.json`, `events.jsonl`, `validation.json`, approved contract snapshots and `seal.json`. The manifest records roster/schema/rules digests, pipeline code digest/version, Python version, selection, source declarations, extractor label and timeout/retry configuration. Capture receipts document normalized text extraction rather than claiming raw HTML byte preservation.

Directories and files are created exclusively. There is no overwrite/update command. Successful manifests receive `complete` only after schema/runtime validation passes. This status means completed pipeline processing with review still required, not completed app research. Failed intake retains an incomplete manifest/failure receipt and sanitized log; it cannot be used as a valid parent. A process killed before sealing remains unusable, and recovery starts a new run from the last valid parent. Existing partial files are never silently repaired or replaced.

```powershell
python -B research_pipeline.py --store work/my-runs collect --run-id replay-002 --parent extracted-001 --replay
python -B research_pipeline.py --store work/my-runs collect --run-id recovered-003 --parent capture-001 --sources corrected-public-sources.json
python -B research_pipeline.py --store work/my-runs validate --run-id extracted-001
```

Replay copies sealed captures, records and contract snapshots and makes no HTTP requests. Resuming reuses successful captured sources; uncaptured/failed sources are tried again in a new child. Fetch histories remain in the parent and child. `--refresh` rechecks a cached source, but changed content at the same source key is rejected to avoid invalidating prior citations: use a distinct versioned URL and a new capture branch. This is a known limitation for unversioned changing docs; later work can support receipt IDs per capture version. Never alter old evidence to fit new claims.

Extraction/correction children preserve original runs, keep stable question IDs where scope is unchanged, automatically link changed/removed parent claim IDs, and log added/removed/changed questions. An asserted claim with a changed scope needs a new ID. Corrections require a reason. Old review and claim versions remain inspectable in the parent even if corrected records need fresh review.

Seals hash all run files; parent seals are checked before use. They detect accidental content changes, added files and missing files. They are unsigned integrity checksums, not an adversarial tamper-proof ledger: a person who can rewrite both data and seals can defeat them. Network source ownership, account identity, human identity and factual truth cannot be guaranteed by local hashes.

## Review and accuracy

Review is explicit and never generated by collection/extraction. The reviewer file has `{"records": {"2": [adjudication objects], "13": [...]}}`; omitted app IDs remain pending. Each adjudication uses the Task 02 fields `claim_id`, `original_run_id`, `judgment`, `reason`, `evidence`. Target IDs must resolve in a sealed ancestor. The target producer and reviewer IDs must differ. Review evidence must also refer to captured content available in that branch; collect additional review documentation in a child before submitting judgments if necessary.

```powershell
python -B research_pipeline.py --store work/my-runs review --run-id reviewed-004 --parent extracted-001 --reviewer-id actual-independent-reviewer-id --reviewer-type ai --judgments actual-review.json
python -B research_pipeline.py --store work/my-runs metrics --run-id reviewed-004 --target extracted-001
```

Use `--reviewer-type human --actual-human-attestation` only when the identified actual person performed the checks. The flag records an explicit assertion; it does not authenticate the person. AI/browser work remains AI review. Completed reviews are not overwritten; start a separate review branch from the target for another reviewer. Review input identifies the target's original run, so a later review child does not silently re-score different claims.

`unresolved` may have empty evidence only if its reason names an existing failed `fetches[N]` attempt in the current record. This implementation uses indexed fetch references rather than arbitrary external failure-log paths. Other judgments require captured evidence. Neither a failed fetch nor a review marked completed establishes that an unresolved claim is correct.

The frozen `inventory.json` defines eligible non-null observed/inferred research claims (identity metadata excluded). `metrics --target` uses that target inventory, not the latest record's rewritten inventory. Nested operational claims would be separate questions but are unresearched in this version. It reports correct C, incorrect I, unsupported U, unresolved, not applicable, pending, eligible and scored denominators; accuracy is C/(C+I+U), null when the denominator is zero. Review coverage is (C+I+U)/eligible. Documentary observations and inferences have separate scores. Null states do not count as correct findings.

Research coverage separately reports per-area status counts, collection statuses and apps with at least one assertion over the selected-app denominator, alongside the full assignment denominator 100. These counts do not declare an area complete. `app_findings_total` counts only apps with non-identity asserted research; it is zero for every synthetic run and for real capture-only runs. `selected_apps` is a separate count. Synthetic claim/review fixtures can exercise arithmetic but never contribute to actual app findings or accuracy.

Deterministic stratified sampling is implemented via `research_pipeline.py sample` (`--seed`, `--per-category`, `--manifest-id`, `--target-run-id`, `--rubric-ref`, `--out`), using language-independent `stratified-sha256-v1` ranking and exclusive file creation (`write_new`). The frozen Task 06 20-app sample manifest and scoring rubric live at `outputs/task-06/sampling-manifest.json` and `outputs/task-06/evaluation-rubric.md`. No first-pass/final improvement is manufactured. For eventual paired scoring, retain the same target sample/question inventory and rubric, publish added/removed/split questions from `changes.json`, and disclose corrected-sample reuse. The CLI provides frozen-target scoring, not an unbiased held-out evaluation service.

## Tests and handoff

Run the offline suite in the README. Tests exercise real schema validation and synthetic collect/extract/ingest/review paths, multi-auth/partial knowledge, source anchoring, unresolved identity, dependency cycles, MCP direction, operational-test rejection, retry/recovery, immutable children, tamper detection and accuracy denominators. Subprocess adapter testing uses explicit argv; no model keys or real app accounts are needed.

Publication receipts, actual source truth/ownership, real human verification, operational tests, and live full-batch assignment research remain later responsibilities. Neither local configuration nor a successful synthetic run is a repository/deployment receipt.
