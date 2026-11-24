# Task 04 five-app pilot — research agent handoff

Scope is exactly IDs 2 HubSpot, 13 Freshdesk, 31 Google Ads, 58 Sherlock,
and 91 NotebookLM. Task 05 independent verification has not started here.
All records have `review.pending`; no account signup, paid service, API-key
creation, authenticated API/MCP request, publication, or sampling was performed.

## Method and producer

The Task04 research agent (OpenAI gpt-6.1-sol) discovered primary pages using the
web tool, opened vendor documentation and the original Sherlock repository,
selected explicit source URLs, then read the actual HTTP snapshots. Search snippets
were used as leads only. The Enterprise hint determines NotebookLM's main scope;
the community personal MCP implementation is separately labeled and does not
establish Enterprise functionality. Outgoing MCP clients were not counted as
callable app servers. Similar-name Sherlock detective/Apple-documentation projects
were rejected as identity mismatches.

The existing pipeline performs HTTP collection, text normalization, SHA-256
provenance, contract validation, immutable lineage and metric calculation.
`build_extraction.py` is researcher-authored structured intake: its claims and
paraphrases encode this agent's reading, with explicit numbered locators. It is
not a fully automatic discovery/semantic extraction engine and invokes no paid
model. The manifest's producer ID is the pipeline's fixed `pipeline-extractor`;
the ingest reason identifies the actual research agent and model.

## Preserved runs

All paths below are relative to the workspace root and under `work/task-04-runs/`:

1. `pilot-capture-001`: original default-permission collection. All 24 attempts
   failed DNS. This is telemetry only and is preserved unchanged.
2. `pilot-capture-002`: approved-network child, 23 captured sources. Freshdesk's
   main reference failed with `Capture failed: ValueError` twice; one Ads testing
   timeout succeeded on retry. The ValueError is not precise enough to establish
   whether size, body-time budget, or another collector guard caused rejection.
3. `pilot-capture-003`: approved-network child adding three smaller/precise
   official references: Ads REST transport, Sherlock installation and Freshdesk
   FDK REST resources. Failed Freshdesk reference attempted once again, preserved.
4. `pilot-first-pass-001`: original researcher extraction, sealed and validated.
   This is the frozen first-pass research target, not an independently verified run.

`sources.json` records the initial 24 selections. `sources-expanded.json` records
all 27 selected sources with kinds, attribution basis and environment metadata.
Each source has an explicit common per-app research context so dependencies align;
claim rationales and auth subcontexts narrow the applicable edition/account path.
An environment declaration only permits evidence use for that environment; it
does not prove credentials are obtainable in that environment.

## Reproduce using the saved evidence (no network)

From the workspace root, choose a **new** destination JSON and run ID:

```powershell
python -B work/task-04-agent/build_extraction.py pilot-capture-003 work/task-04-agent/rebuilt-claims-001.json
python -B research_pipeline.py --store work/task-04-runs ingest --run-id pilot-rebuilt-001 --parent pilot-capture-003 --claims work/task-04-agent/rebuilt-claims-001.json --reason 'Replay of Task04 researcher-authored gpt-6.1-sol extraction from unchanged captured evidence; no new research or independent review'
python -B research_pipeline.py --store work/task-04-runs validate --run-id pilot-rebuilt-001
python -B research_pipeline.py --store work/task-04-runs metrics --run-id pilot-rebuilt-001 --target pilot-rebuilt-001
```

`build_extraction.py` uses numbered locators for the saved `pilot-capture-003`
snapshots. Do not apply those numbers blindly to new live captures. Re-read new
snapshots and update a separate builder before research intake.

## Recollect current public sources

```powershell
python -B research_pipeline.py --store work/task-04-runs collect --run-id pilot-fresh-capture-001 --ids 2,13,31,58,91 --sources work/task-04-agent/sources-expanded.json --timeout 15 --retries 1
```

Use a fresh run ID on every execution. If this execution environment denies DNS,
retry the command through approved network execution in a new child of the failed
capture, as done in this pilot. A previous failed request never proves a vendor
has no API, no MCP or a payment/partnership gate. Do not overwrite sealed runs.

## Inspect the actual first pass

```powershell
python -B research_pipeline.py --store work/task-04-runs validate --run-id pilot-first-pass-001
python -B research_pipeline.py --store work/task-04-runs metrics --run-id pilot-first-pass-001 --target pilot-first-pass-001
```

`first-pass-extraction.json` preserves the original researcher intake. The sealed
run contains `records.json`, `captures.json`, numbered `packet.json`, normalized
snapshots, `inventory.json`, `changes.json`, fetch event logs, contract/manifest
hashes and a seal. Snapshot hashes prove content identity, not factual accuracy.
`metrics.json` contains actual pipeline output. `handoff.json` includes exact
counts, capture exceptions, per-app unknowns and the unmodified pending reviews.

## Remaining issues before trusting findings

* **Taxonomy exception for Task 05/06:** frozen claim
  `31.production.partner_approval_required` stores `true`, but its rationale means
  Google's vendor API-access approval, not a commercial partnership. Keep that
  original value and all 92 eligible research claims intact. Do not count this
  flag as evidence of a partnership gate in category totals or outreach estimates.
  Task 05 should examine the claim against its stated scope; Task 06 should define
  separate vendor API approval and commercial partnership categories before
  aggregation. Any later change needs a child run and a visible migration/correction
  entry. This handoff annotation is not an adjudication or a schema change.
* Google Ads official summaries still describe mandatory developer tokens, while
  the dated migration bodies say sunset on September 9, 2026 and describe
  Cloud-project Test/Explorer/Basic/Standard access. The token requirement is
  explicitly disputed; project-level testing and production approval are scoped.
  Ads API usage charges/free-use conditions are unknown in this pilot.
* HubSpot's legacy private-app creation ended October 26, 2026. Existing private
  tokens, current static tokens and OAuth distribution are separate entries.
  Free production/private-app observations apply to existing legacy apps only.
  Do not generalize them to every new integration or premium CRM capability.
* Freshdesk Basic/API-key and FDK OAuth alternatives are captured. Exact Basic
  username/dummy-password encoding from the main reference was read with the web
  tool but cannot enter supported claims until the collector captures it.
  The OAuth version remains unspecified in the captured FDK guide, so the record
  uses `other` with an explicit OAuth label. The temporary Free Program's API
  entitlement and a universal paid requirement remain unknown.
  The main reference URL is `https://developers.freshdesk.com/api/`. Its original
  default-network attempt is Freshdesk `fetches[0]` (`dns_error`,
  `Request failed: gaierror`). Approved-network attempts at `fetches[5]`, `[6]`
  and `[11]` recorded `other_error`, `http_status: null`, and the exact error
  `Capture failed: ValueError`. No snapshot was captured for that URL. The saved
  error does not establish which collector guard rejected it and does not establish
  any restriction on the Freshdesk product itself.
* Sherlock's no-credential finding is an inference about documented local CLI
  usage only. MIT license access is free; target-site availability/reliability was
  not tested. Official usage text shows an older help version than the repository.
  MCP is bounded `not_found_in_checked_sources`, not a claim of global absence.
* NotebookLM uses licensed-user Enterprise REST, IAM, billed project and Discovery
  Engine setup, with a documented subscription trial. Personal community MCP
  uses internal APIs/cookies and does not establish Enterprise support. Chat/query
  parity is not established. One community MCP observation says 'lists notebook
  tools' while its locator ends at the table header (165); the first tool starts
  at 166. Server identity is supported at 155–157, but tool-list wording needs
  locator correction in a child before reliance. Original first pass is preserved.
* Eligibility flags not established by specific documentation remain null, not
  false. Buildability and breadth are expressly inferences. No independent AI or
  human review has been claimed and all operational checks are not researched.
* **MCP discovery is non-exhaustive for every app.** Found entries establish only
  the implementations described by captured sources, not a complete ecosystem
  inventory. Sherlock's bounded result covers official repository README,
  installation and usage sources; unrelated same-name search hits were rejected.
  It cannot establish that no community or official MCP exists elsewhere. All four
  recorded MCP operational checks remain `not_researched`.

## Coordinator handoff boundary

Technical handoff checks confirmed five non-synthetic records, 26 captured sources,
71 observed states (including five identities), 26 inferred states, 48 unknown
states, four unresearched operational checks, one disputed auth question and one
bounded MCP-not-found state. The research scoring inventory remains 92 claims,
all pending; the scored denominator is zero and accuracy is null. These are
structure/telemetry checks, not independent factual verification.

The taxonomy exception above and the previously noted NotebookLM locator issue
are explicit unresolved handoff issues. Neither changes the frozen extraction,
snapshots, inventory, metrics, or pending reviews. `handoff.json` includes these
machine-readable exceptions; `summarize.py` produced the original telemetry
portion before these coordinator-requested annotations were added. Do not rerun
it over existing files: its exclusive writes intentionally reject overwriting.

The coordinator owns final review, packaging and task-board updates. This agent
does not modify those outputs or start Task 05.
