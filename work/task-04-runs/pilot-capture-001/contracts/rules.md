# Task 02: research format and evidence rules

Contract version 1.0, 2026-11-23. This task defines inputs and records only. It implements no retrieval, research, accuracy measurement or publication. Task 03 must implement the runtime checks below before promoting findings.

## Files and migration

- `data/apps.json` is the 100-app identity roster, in assignment order. Its provenance identifies the original conversation and user turn. Original app/hint Markdown is retained verbatim, including link targets and parenthetical hints. Categories and normalized names match the audited roster.
- `legacy_candidate_doc_urls` preserves the scaffold's URL leads with their separate provenance. Neither these URLs nor assignment hints establish auth, access, API or MCP findings. Do not inherit the old OAUTH/APIKEY/GATED/MCP lists, generic descriptions, breadth placeholders or buildability labels.
- `schemas/record.json` is a Draft 2020-12 schema for one app in one immutable run. `examples/unresearched-record.json` is a format example, excluded from research and accuracy totals.
- Initialize substantive claims as `not_researched`, with null values and empty evidence. Keep prior artifacts intact as legacy material; a migration must not relabel their guesses as documentary observations. Existing scripts do not yet consume or enforce this contract.
- Paygent Connect (84) is unresolved. Preserve the original `paygent (NMI-powered)` hint. The legacy paygentglobal.com lead has no established identity match. Resolve vendor/product/edition with primary evidence before attaching that domain's facts; do not substitute a similarly named payment company. The example intentionally leaves this unresolved.

## Claim states and evidence

Each scalar claim has a stable `claim_id`, `status`, `value`, `context`, `evidence`, `supporting_claim_refs` and `rationale`. Context names the edition, API version, account type, region and environment where relevant; say which details remain unknown. IDs remain stable across revisions for the same question. Split materially different scopes into distinct method/entry claims rather than merging them.

| Status | Meaning and counting |
| --- | --- |
| `observed` | Explicitly supported by captured source content; non-null value and evidence required. This means documentary observation, not verified truth or a successful API call. |
| `inferred` | Reasoned conclusion; non-null value, evidence, rationale and supporting claim references required. Report separately from documentary observations. |
| `unknown` | Attempted investigation did not resolve the question. Null value; explain the gap. |
| `disputed` | Conflicting content has not been reconciled. Null value; at least two evidence observations and an explanation required. |
| `not_researched` | No investigation yet. Null value; never count as a finding. |
| `not_applicable` | Evidence explains why the question does not apply to the stated scope. Null value; not a negative result or a correct auth/access claim. |
| `not_found_in_checked_sources` | A bounded search found no supported result. Null value and evidence identifying checked content/search scope required. Use for MCP discovery; never translate to 'no MCP exists'. |

`coverage_status` on auth/protocol/resource collections is workflow metadata: `not_researched`, `partial`, or `checked_sources`. `checked_sources` means only the listed sources were examined, never exhaustive coverage of the vendor. Empty arrays do not prove absence. Record unresolved questions in `notes`; a researched collection can still be incomplete.

For each evidence observation record:

- The actual source URL, source kind, exact heading/anchor, page/line range, or repository path plus commit and line range in `locator`.
- A short captured observation or faithful paraphrase supporting this specific claim. A homepage URL, search-result snippet, or a whole-page citation without a locator is a lead, not substantive evidence.
- `captured_on` (ISO date), capture method, and document date/version when known. Null document metadata means unknown, not current. Capture dates must reflect actual reading, not run creation.
- SHA-256 of the captured content and a relative `snapshot_ref` where feasible. Hash normalized/extracted content only if the snapshot is exactly that content and the extraction method is recorded. If no content snapshot/hash is available, use null and a specific `hash_unavailable_reason`; do not fabricate a digest. A hash proves content identity, not correctness. Never store credentials in snapshots.

For actual operational tests, use `source_kind: execution_receipt` and `capture_method: execution_log`. These require a real local receipt/log in `snapshot_ref` and its SHA-256; `source_url` may be null for a local log. Its locator identifies the run/tool call and relevant log lines; observation states the actual result. This is the only source kind that allows a null source URL. This format permits future receipts; it implements no execution functionality and the Task 02 example has no operational findings.

Prefer vendor developer/auth/pricing/access docs and official repositories. Community repositories support their own implementation claims, not vendor endorsement. Assignment text supports identity/category/hints only. Cite approval and pricing sources for eligibility claims; an API reference alone need not establish a free credential path. If official sources conflict, preserve both observations and their time, version and scope; do not silently pick one. `conflicts` links the affected claim IDs and explains the discrepancy; `disputed` claims may also hold both observations directly.

Evidence is attached per claim. Each auth method, API protocol, resource group and MCP entry has its own claim and evidence. A shared page may be cited repeatedly with the appropriate locator. One citation must not silently support other array members or scopes. When one claim necessarily includes several details (e.g. an auth method plus documented scopes), its evidence must support every detail; otherwise split the claim or omit unestablished optional details. For review, any unsupported material detail makes that whole claim unsupported; do not inflate the denominator by splitting punctuation into claims.

## Field rules

**Identity and purpose.** `identity.id`, `app` and `category` come from the roster; resolve product identity in `identity.resolution` using a cited product/edition description. Category is assignment metadata, not a researched auth claim. `purpose` is a short, single-line, cited description. Do not put placeholder prose in an observed value.

**Auth.** `auth.items` contains a separate claim per method and scope. Preserve OAuth2, API key, Basic and tokens separately; don't choose a single winner. `context` and `details` explain API/edition/actor, OAuth grant or signing scheme; `scopes` lists only documented scopes relevant to the described use. An empty scopes list means no scopes captured, not unrestricted permissions. For CLI/local software, only assert `none` or `not_applicable` when supported for that interface; lack of a REST API does not settle CLI buildability.

**Credentials.** `credential_eligibility.testing` and `.production` each contain independent boolean claims:

- `free_access`, `trial_access`, `sandbox_access`: true means a documented credential/use path is available for this environment; false requires evidence of its absence or inapplicability. Unknown stays null.
- `paid_required`, `admin_approval_required`, `partner_approval_required`, `contact_sales_required`: true means this condition is required for the stated path/scope. False needs explicit support for proceeding without it; silence is unknown.
- `self_serve`: a documented path allows the intended developer to obtain the relevant credentials without vendor/partner intervention. A paid path may be self-serve; an existing tenant's admin can still be required. State actor/plan/prerequisites in each claim's context. Never derive this by default or from 'Sign up'.

These conditions can coexist. A free sandbox can require admin approval; production may require a paid account and partner approval. For alternative credential paths, the context of each claim must identify exactly which path it describes. Do not collapse conflicting paths to one app-wide boolean: use unknown/disputed with explanatory evidence until a scoped answer is possible. A paid product does not automatically mean API access is gated, and a free trial does not establish production access.

**API surface.** Protocols, public documentation, resource groups and breadth are independent claims. A known REST protocol must survive even when breadth and resource groups are unknown. Record each documented protocol and resource group separately with supporting sections; a source can establish 'contacts' while leaving 'billing' unresearched. `public_documentation` refers to documentation visibility for this API scope, not credential eligibility or public data access. Public documentation does not mean anonymous API access.

`breadth` is an inference supported by resource-group claim IDs: `narrow` = one focused workflow/group; `moderate` = multiple related groups; `broad` = multiple distinct business domains. Explain the classification and captured examples in context/rationale. This is qualitative scope, not a fabricated endpoint inventory or a guarantee of completeness. Leave unknown if not enough resource documentation was read. REST/GraphQL/SDK/CLI can coexist; include other interfaces when relevant to agent-callable tools.

**MCP.** `mcp.discovery` is `observed` with value `found` only when at least one supported entry is recorded. Otherwise use the appropriate null state. Each `mcp.entries` item is its own claim with `official`/`community`, source URL, scope, and repository/server URL where established (null otherwise). A server URL may be a hosted endpoint, while a local stdio server may have only a repository URL. No guessed URL. Vendor endorsement must be supported to call it official. Entries for outgoing MCP clients do not establish an app's callable server; record tool direction/scope. `operational_check` remains `not_researched` unless actual execution logs support the result. Docs, a server listing, or a GitHub README cannot establish successful connection, tool calls, or production readiness. This task runs no operational checks.

**Buildability.** This is an explicit inference for a stated agent workflow: `build_now`, `conditional`, `outreach_required` or `not_buildable_for_stated_scope`. Cite supported identity/auth/access/API/MCP or CLI claims through `supporting_claim_refs`, include relevant source evidence, explain the conclusion, list blockers and next steps. A public API can still require outreach; no MCP alone is not a blocker to building an API wrapper. Unknown identity/access/API details can leave buildability unknown. `build_now` is feasibility from evidence, not an implemented or tested integration. Blocker statements also require support; do not label an app unbuildable because a fetch failed.

## Fetch telemetry is separate

`fetches` records URL, attempt date, status, HTTP status, resolved URL, error and optional content digest. It never supplies claim truth. DNS/HTTP errors, login walls, robots blocks and timeouts do not establish no API, paid access, partner gating or nonexistent MCP. A 200 response does not establish a cited claim. Fetch outcomes can prompt follow-up but cannot promote research states automatically.

## Review, runs and accuracy

1. Every saved run gets a unique `run_id`, creation date and producer identity/type. Persist the run input roster hash, schema/rules versions, tool/model versions and configuration alongside that run in a run manifest. Never reuse a run ID or overwrite original records, evidence snapshots, logs or adjudications. The example's run ID is illustrative only.
2. Corrections create a new run with `parent_run_id` and `correction_refs` naming original run/claim IDs plus reasons. Keep the original value/evidence unchanged in the parent; revised claims reuse the same question ID where scope is unchanged. Record added/removed/split claims explicitly in the correction log. New evidence does not retroactively become first-pass evidence.
3. `review` is pending until actual claim adjudications exist. Completed means the listed adjudications are completed, not that every field/app was reviewed. Capture reviewer ID, `ai` or `human`, date, original run ID, each claim ID, judgment, rationale and review evidence. A tool/browser action or another AI is still AI review; only an actual identified person can sign human review. Producer and reviewer identities must be distinct for independent review; disclose shared model/context. Do not copy pending entries over completed reviews.

   An `unresolved` judgment may have an empty evidence array when no source content could be captured. Its required reason must name the actual fetch attempt (for example `fetches[0]` and its date/URL) or an existing failure-log path and describe why adjudication could not finish. Runtime review must resolve that reference. Do not fabricate a source observation for a DNS/access failure. `correct`, `incorrect`, `unsupported` and `not_applicable` judgments still require captured evidence; a failure-only review cannot establish any of them. A completed review containing unresolved judgments does not mean those claims have been verified and contributes no accuracy denominator for those judgments.
4. Before full-run verification, freeze a sampling manifest: manifest ID/path, target run, roster SHA-256, selection date, method/algorithm/version, seed, selected IDs, category counts, reviewer assignments and claim rubric. Use a deterministic seeded selection of two apps per category (20 total), without replacement; report all ten categories including Support and Helpdesk. Preserve pilot/targeted reviews separately from this sample. A seed alone does not reproduce an unspecified algorithm. Do not select actual sample IDs in Task 02.
5. Freeze the claim inventory and scoring rubric before review. Unit = each non-null `observed` or `inferred` claim object, identified by `(run_id, app_id, claim_id)`. Count auth methods, protocols, groups and MCP entries separately; nested operational checks are separate claims only if asserted. Score a compound claim correct only if all material details hold for its scope. Report documentary and inference results separately. Category/roster metadata, example fixtures, collection metadata, null states and bare URLs are not scored findings.
6. Each adjudication is `correct`, `incorrect`, `unsupported`, `unresolved`, or `not_applicable`. Unsupported is a failure to substantiate, not proof of factual falsity. Let C/I/U be completed correct/incorrect/unsupported judgments for asserted claims. Evidence-backed accuracy = C / (C + I + U); print those counts, with unresolved/pending/excluded totals alongside. If the denominator is zero, accuracy is null ('unmeasured'), not 0% or 100%. Exclude null-state claims and not-applicable judgments from this accuracy denominator; report any invalid applicability claims as audit issues. Do not drop incorrect or unsupported results after correction.
7. Report review coverage = completed C/I/U judgments / eligible asserted claims in the frozen sample, with unresolved and pending counts. Separately report research coverage across all 100: counts of observed, inferred and each null state for the six required research areas (purpose, auth, credentials, API, MCP, buildability), plus identity resolution. A collection is not covered just because it exists; distinguish partial protocol knowledge from missing breadth. Report area completion criteria and every denominator. Unknowns do not count as correct findings. No one overall 'accuracy' number should conceal missing research or missing review.
8. First-pass and corrected scores refer to immutable runs, the same sample and the frozen claim questions. Link changed/removed/split/new questions; publish paired results on comparable questions and the changed inventory separately. Do not claim improvement by deleting hard claims, changing denominators or relabeling a failure unknown. A corrected/previously reviewed sample is not an unbiased held-out estimate; disclose reuse. Report no accuracy or improvement until actual adjudication exists. Prepare a human checklist if no person has reviewed yet; do not claim human checks were performed.

## Publication contract (later tasks only)

A hosting config, Site registration, expected URL, local Git directory or ZIP is not proof of publication. Save a repository creation/write receipt, actual repository URL, commit SHA, source/README existence and readback evidence. Save the deployment ID/status, actual live URL, deployed commit or artifact SHA-256, date, and an independent fetch/browser result demonstrating the page is accessible to the intended reviewer. Record real errors/blockers when unsuccessful. No publication is attempted in Task 02.

## Validation and Task 03 handoff

No dependencies were installed. From the workspace root, the available PowerShell validates the example:

```powershell
Test-Json -Path examples/unresearched-record.json -SchemaFile schemas/record.json
$roster = Get-Content -Raw data/apps.json | ConvertFrom-Json
if ($roster.apps.Count -ne 100) { throw 'Expected 100 apps' }
if (($roster.apps.id -join ',') -ne ((1..100) -join ',')) { throw 'IDs/order changed' }
if (@($roster.apps | Group-Object category).Count -ne 10) { throw 'Expected 10 categories' }
if (@($roster.apps | Group-Object category | Where-Object Count -ne 10).Count) { throw 'Expected 10 apps per category' }
```

If `jsonschema` is already installed in another environment, this optional check verifies both the schema and example (do not install it for this task):

```console
python -c "import json,jsonschema; s=json.load(open('schemas/record.json')); jsonschema.Draft202012Validator.check_schema(s); jsonschema.Draft202012Validator(s, format_checker=jsonschema.FormatChecker()).validate(json.load(open('examples/unresearched-record.json'))); print('valid')"
```

Schema validation enforces required fields, value types, explicit states, local evidence minimums for assertions, reference presence for inferences, and pending/completed review shape. It cannot establish source truth, identity, evidence relevance, all reference integrity, actual human activity, or immutable run history. Validators may treat `format` as annotation: Task 03 must explicitly validate URLs/date values.

Runtime/reviewer checks to implement in Task 03 (not implemented here):

- Match IDs/names/categories to the roster; unresolved identity blocks promotion of product-specific claims.
- Ensure unique claim IDs (including nested checks), resolve all support/conflict/adjudication/correction references, reject self/circular support, and ensure buildability/breadth dependencies are supported and scoped consistently. Referenced IDs are claim IDs within this app/run unless explicitly paired with an original run ID.
- Require each asserted method/group/server and every material detail to be supported by its own evidence; inspect the actual cited content. Do not accept assignment hints or legacy leads as product evidence. `breadth` must use `inferred` and reference resource claims; `not_found_in_checked_sources` is restricted to MCP discovery.
- Require no asserted items under `not_researched` collection status; track partial knowledge and source scope. MCP `found` needs at least one supported entry and source-backed origin; operational success needs execution receipts. No nonempty MCP entries under an unknown/negative discovery state.
- Verify valid dates/URLs, content hashes/snapshot paths, document versions, primary/community attribution and conflicts. Keep fetch failures separate and ensure captures correspond to real reads.
- Enforce append-only runs/reviews and snapshot storage, parent/correction linkage, review identity/type, sample reproducibility/category coverage, frozen claim denominators and metric arithmetic. Retain unsupported results.
- Require publication receipts/readback before reporting repo/live-page success.

Coordinator acceptance should cover: honest unknown example passes; multi-auth and REST-only partial knowledge pass; evidence-free observed auth/purpose and unsupported inferred buildability fail; malformed dates/refs are flagged by runtime if the validator does not reject them; completed review with no reviewer/judgments fails. Passing a schema is not evidence that Task 03 or the assignment research is complete.
