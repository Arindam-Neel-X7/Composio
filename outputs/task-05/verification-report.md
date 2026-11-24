# Task 05: Independent AI Verification Report (Five-App Pilot)

- **Reviewer**: `gemini-task05-independent` (`reviewer_type: ai`, Gemini in a fresh conversation; **not human review**)
- **Frozen target run**: `work/task-04-runs/pilot-first-pass-001` (untouched; `records.json` SHA-256 `10ff5bdb556920e5fd0c692e6a3694c219ee98011c6244d9cf796203505d8f90`, `seal.json` SHA-256 `eaebd62d4f63c52465b15d5d94aa708db3a2140f25b120ca28b704ac38e03ca2`)
- **Completed review child run**: `work/task-04-runs/task05-review-002` (`seal.json` SHA-256 `9713538d659d4d56d5a980d96eb58cf78669715fb8dcd5343203f02776d5a94f`)
- **Rejected attempt preserved**: `work/task-04-runs/task05-review-001` (rejected by pipeline validator because one verbatim review quote crossed a line break; preserved untouched per immutable-run rules)
- **Validation backend**: Python `jsonschema` `Draft202012Validator` (installed in `.venv`; all 19 offline pipeline tests pass)

---

## 1. Measured Accuracy and Coverage (Frozen 92-Claim Pilot Inventory)

| Slice | Eligible | Correct (C) | Incorrect (I) | Unsupported (U) | Unresolved | Not Applicable | Pending | Denominator (C+I+U) | Accuracy C/(C+I+U) | Review Coverage |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Overall** | 92 | 87 | 0 | 5 | 0 | 0 | 0 | 92 | **94.57%** (87/92) | **100.0%** (92/92) |
| **Observed (documentary)** | 66 | 62 | 0 | 4 | 0 | 0 | 0 | 66 | **93.94%** (62/66) | **100.0%** (66/66) |
| **Inferred** | 26 | 25 | 0 | 1 | 0 | 0 | 0 | 26 | **96.15%** (25/26) | **100.0%** (26/26) |

### Per-App Breakdown

| App ID | App | Eligible | Correct | Incorrect | Unsupported | Accuracy | Key Issues / Notes |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 2 | HubSpot | 22 | 22 | 0 | 0 | 100.0% (22/22) | Caveat: `2.production.*` rely on sunset legacy private apps (new creation ended 2026-10-26) under a broad app-wide `context`. |
| 13 | Freshdesk | 20 | 20 | 0 | 0 | 100.0% (20/20) | Capture gap: main API reference `developers.freshdesk.com/api/` failed (`Capture failed: ValueError`). |
| 31 | Google Ads | 18 | 16 | 0 | 2 | 88.89% (16/18) | `31.production.partner_approval_required` (taxonomy mismatch) and `31.production.admin_approval_required` (unsupported inference) judged `unsupported`. |
| 58 | Sherlock | 13 | 13 | 0 | 0 | 100.0% (13/13) | Bounded `58.mcp` (`not_found_in_checked_sources`) is accurate for official sources; community wrappers exist outside checked sources. |
| 91 | NotebookLM | 19 | 16 | 0 | 3 | 84.21% (16/19) | `91.purpose` (missing second citation), `91.mcp` (Enterprise/personal conflation + truncated locator), and `91.mcp.personal_community` (truncated locator) judged `unsupported`. |

---

## 2. Unsupported Claims Found (5 of 92)

1. **`31.production.partner_approval_required`** (`observed`, value `true`) — **Unsupported (Taxonomy Mismatch)**
   - **Finding**: `developers.google.com/google-ads/api/docs/api-policy/access-levels` (`lines:123-169`) documents **Google vendor API-access approval** (Explorer/Basic/Standard application in Cloud Console; line 168: *"Google may automatically upgrade your project's API access level to Explorer"*), not a partner program or commercial partnership. Even the claim's own rationale disclaims commercial partnership. Storing vendor API-access review under `partner_approval_required=true` is unsubstantiated by the cited text and reflects a schema gap.
2. **`31.production.admin_approval_required`** (`inferred`, value `true`) — **Unsupported Inference**
   - **Finding**: Not flagged in Task 04 handoff. The claim cites `best-practices/testing` (`lines:481-487`), which describes adding a test principal to test accounts and explicitly warns *"Don't give this user or service account access to any production accounts"*, plus `oauth/overview` (`lines:438-441`), which only says *"Make sure your authorized user or your service account has access to the Google Ads accounts you are making API calls to."* Neither passage establishes that admin approval is required for production credentials.
3. **`91.purpose`** (`observed`, value `"Enterprise document research notebooks with programmatic notebook and source management."`) — **Unsupported Material Detail in Attached Evidence**
   - **Finding**: Not flagged in Task 04 handoff. Factually accurate across the two captured Enterprise API docs, but `91.purpose` attaches only `api-notebooks` (`lines:148-155`), which covers notebook management (create/retrieve/list/delete/share) and never mentions source management. Source management is documented in `api-notebooks-sources` (`lines:148-156`, captured in this run) but was omitted from `91.purpose`'s own evidence array.
4. **`91.mcp`** (`observed`, value `"found"`) — **Unsupported (Edition/Scope Conflation + Truncated Locator)**
   - **Finding**: Asserts app-level `mcp.discovery = "found"` on a NotebookLM Enterprise API record based solely on a community repository (`github.com/Morfeu333/notebooklm-mcp`) targeting personal `notebooklm.google.com` via undocumented internal APIs and browser cookies that explicitly states *"May work with NotebookLM Enterprise accounts but has not been tested."* (line 157) and *"Use at your own risk for personal/experimental purposes."* (line 224). Additionally, `ev[0]` cites `lines:151-165`, which ends at the table header (`Tool / Description`) and cuts off the actual tool rows beginning at line 166.
5. **`91.mcp.personal_community`** (`observed`) — **Unsupported (Truncated Locator)**
   - **Finding**: Although `value.scope` accurately distinguishes personal `notebooklm.google.com` internal APIs from Enterprise REST, `ev[0]` cites `lines:151-165` with the paraphrase *"and lists notebook tools"*, whereas lines 151–165 stop at the header (`164: Tool`, `165: Description`) and exclude the actual callable tool rows starting at line 166 (`notebook_list`, `notebook_create`, etc.).

---

## 3. Explicit Assessment of Required Focus Areas & Comparison with Task 04 Notes

Comparison against `work/task-04-agent/handoff.json` and `outputs/task-04-review.md` (performed **after** completing the independent pass):

1. **Google Ads access-approval taxonomy (`31.production.partner_approval_required`)**: Independently confirmed as `unsupported` due to schema conflation of vendor API-access approval vs. commercial partner approval. Agrees with `task04-google-approval-taxonomy`. Additionally, independent review flagged `31.production.admin_approval_required` as an unsupported inference and noted that `31.buildability` (judged `correct` on its own blocker text and evidence) still lists `31.production.partner_approval_required` in `supporting_claim_refs`.
2. **Google Ads developer-token documentation conflict (`31.auth.developer_token_requirement`, status `disputed`, excluded from eligible denominator)**: Confirmed as properly handled coverage state. `oauth/overview` lines 417–418 still claim a developer token is required, while `api-policy/developer-token` lines 64–91 (and `mcp-server` lines 486–489) state developer tokens were sunset on September 9, 2026 and are optional/ignored thereafter. Retaining both citations as `disputed` avoids silently promoting stale summary text.
3. **Freshdesk reference-capture gap (`developers.freshdesk.com/api/`)**: Confirmed. Three approved-network attempts (`fetches[5,6,11]`) failed with `Capture failed: ValueError` (no snapshot captured; exact guard not surfaced in the sanitized error, likely the 2 MB HTTP body limit). Smaller official docs (`developers.freshworks.com/.../rest-apis/`, `oauth-implementation-in-apps/`, and Freshdesk support articles) adequately support all 20 asserted claims, while exact Basic wire encoding and main-reference rate limits remain honestly unpromoted.
4. **NotebookLM MCP locator range and personal-vs-Enterprise distinction**: Independently confirmed both defects. `lines:151-165` cuts off immediately before line 166 (`notebook_list`), rendering `91.mcp.personal_community` and `91.mcp` unsupported as cited; moreover, `91.mcp` (`discovery = "found"`) conflates an untested personal cookie-scraping community repo with the Enterprise API scope.
5. **Bounded Sherlock MCP result (`58.mcp`, status `not_found_in_checked_sources`, excluded from eligible denominator)**: Confirmed as appropriate for the bounded official sources (`github.com/sherlock-project/sherlock` and `sherlockproject.xyz/usage`). Independent web search confirmed no official Sherlock MCP exists, while third-party community FastMCP wrappers (e.g., `Burnsedia/sherlock-mcp`, `qKitNp/sherlock_mcp`) do exist in the broader ecosystem — reinforcing why `not_found_in_checked_sources` must never be translated into "no MCP exists."
6. **Non-eligible coverage states audited separately**: 48 `unknown`, 4 `not_researched` operational checks, 1 `disputed`, and 1 `not_found_in_checked_sources` were inspected separately and excluded from the accuracy denominator (never counted as correct).

---

## 4. Limitations

- **AI review only**: Performed by an AI verification agent (`gemini-task05-independent`). No human verification has been performed.
- **Pilot only (not a held-out estimate)**: Covers the 5 pilot apps (92 claims), not the 20-app stratified evaluation sample (Tasks 06/17). No accuracy improvement is claimed.
- **Documentary verification only**: No authenticated API/MCP calls, account signups, paid subscriptions, or live operational checks were performed. All 4 MCP `operational_check` fields remain `not_researched`.
- **Snapshot currency**: Verification checked captured snapshots dated `2026-11-23` (plus an independent web check for Sherlock MCP).

---

## 5. Proposed Fixes for Task 06

1. **Schema taxonomy (`schemas/record.json` & `docs/evidence-rules.md`)**: Add a distinct `vendor_approval_required` boolean (for vendor API-access review like Google Ads Explorer/Basic/Standard) separate from `partner_approval_required` (commercial/agency/technology partnership gates).
2. **Collector error diagnostics & large-page handling (`research_pipeline.py`)**: Distinguish `max_bytes_exceeded` (2 MB cap) from generic `Capture failed: ValueError` in sanitized fetch telemetry, and evaluate raising or configuring the response byte limit (or supporting section-targeted official reference URLs) for large single-page API references like `developers.freshdesk.com/api/`.
3. **HTML-to-text normalization (`research_pipeline.py`)**: Strip Mintlify/Next.js/MDX hydration JSON script/payload blobs (observed leaking into `sherlockproject.xyz/usage` lines 76–77) so normalized snapshots stay clean and compact.
4. **Scope-specific context granularity**: Allow credential claims to carry a narrower path/edition `context` than the full app-level source `scope` (or define separate source specs per path), preventing sunset legacy paths (like HubSpot `2.production.*`) or personal-tier MCP repos (like NotebookLM `91.mcp`) from sharing a broad Enterprise/current `context` string.
5. **MCP discovery vs. edition alignment**: Clarify in `docs/evidence-rules.md` that a community MCP targeting a different product edition (e.g., personal cookie-scraping `notebooklm.google.com` vs. Gemini Notebook Enterprise REST API) should not set Enterprise-scoped `mcp.discovery = "found"` without explicit edition tagging.
6. **Child correction run (Task 06)**: Repair the 5 unsupported pilot claims in a new child run (preserving `pilot-first-pass-001` and `task05-review-002`) and freeze the 20-app stratified sampling manifest and rubric before beginning Batch 1 (Task 07).
