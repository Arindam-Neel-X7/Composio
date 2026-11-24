# Task 04: reviewed five-app pilot

The first-pass pilot is complete. Research agent Mendel used the approved pipeline for HubSpot (2), Freshdesk (13), Google Ads (31), Sherlock (58) and NotebookLM (91). The coordinator reviewed the handoff, checked evidence integrity and selected source interpretations, and reproduced the original structured intake byte-for-byte. Independent verification in Task 05 has not started.

## What was captured

- 27 selected source URLs; 26 captured: 25 vendor/project-controlled sources and one repository documenting a community NotebookLM implementation. This is retrieval coverage, not accuracy.
- Five non-synthetic records. `pilot-first-pass-001` is the frozen first-pass target.
- 71 observed claim states, including five identity claims, and 26 inferences. The scoring inventory contains **92 research assertions** after excluding identity metadata.
- 48 unknowns, four unresearched operational checks, one disputed auth question and one bounded MCP-not-found result remain visible.
- All five reviews are pending; zero adjudications and zero human checks. The scored denominator is zero and accuracy is **unmeasured**.

## First-pass findings

All buildability verdicts below are documentary feasibility inferences for the stated scope, not implemented or tested integrations.

| App | Auth and interface | Access/buildability finding | MCP finding and evidence |
| --- | --- | --- | --- |
| HubSpot | OAuth for installed accounts; static tokens for current single-account apps; legacy and app-management methods separately scoped. REST CRM resources. | Prototype candidate in a developer test account. Production still requires the relevant tenant permissions, scopes and plan. | Official remote CRM MCP documented; no connection tested. [Auth](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview), [developer testing](https://developers.hubspot.com/developer-platform-basics), [MCP](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server). |
| Freshdesk | Personal API-key credential with Basic transport; a separate FDK app OAuth route is documented, with its version uncaptured. REST ticket workflows. | Conditional on verified agent credentials, role permissions and tenant entitlement. Trial access and long-term free API eligibility are different questions. | Official hosted MCP documented for supported tenants/plans; untested. [API key](https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key), [OAuth](https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/oauth-implementation-in-apps/), [REST](https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/rest-apis/), [MCP](https://support.freshdesk.com/support/solutions/articles/50000012670). |
| Google Ads | OAuth user/service-account workflows; REST, gRPC and SDK interfaces. | Conditional on authorized account access and Cloud-project production access. Dated migration bodies describe project-level onboarding after the September 9, 2026 developer-token sunset, while older summary text conflicts. The token requirement is retained as disputed. | Official MCP documented; untested. [OAuth](https://developers.google.com/google-ads/api/docs/oauth/overview), [migration](https://developers.google.com/google-ads/api/docs/api-policy/developer-token), [access levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels), [MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server). |
| Sherlock | Local CLI username search/export. No Sherlock credential step in the documented invocation is an inference limited to that interface. | Prototype candidate as a bounded CLI wrapper using MIT-licensed software. Target-site behavior and successful detection were not tested. | No matching server established in the checked official sources; this does not establish global absence. [Repository](https://github.com/sherlock-project/sherlock), [usage](https://sherlockproject.xyz/usage), [license](https://raw.githubusercontent.com/sherlock-project/sherlock/master/LICENSE). |
| NotebookLM | Enterprise notebook/source REST API with licensed-user Bearer credentials and IAM. Current docs call the Enterprise product Gemini Notebook Enterprise. | Conditional on subscription/license assignment, IAM and project setup; API is Preview. Personal chat parity is not established. | Community personal NotebookLM MCP is separate from the Enterprise integration; neither was operationally tested. [Notebook API](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks), [licensing](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing), [community implementation](https://github.com/Morfeu333/notebooklm-mcp). |

## Review outcomes and unresolved issues

The pipeline's schema, source receipts, snapshot hashes, numbered locations, reference consistency and immutable lineage checks pass for all five records. The original extraction input was rebuilt from the saved capture and matched its SHA-256 byte-for-byte; a new replay child also validated. This establishes reproducibility and structural grounding, not factual accuracy.

1. Freshdesk's main reference at `https://developers.freshdesk.com/api/` has no captured snapshot. Approved retries logged `Capture failed: ValueError`; the saved error does not identify the guard responsible. Smaller official references supplied supported fields, while exact Basic wire encoding and main-reference rate limits remain unestablished.
2. Google's vendor API-access approval is stored under `partner_approval_required=true`, with a rationale explaining that it is not a commercial partnership. This taxonomy gap is flagged for Tasks 05/06. Do not count it as partnership-outreach demand.
3. NotebookLM's community MCP evidence mentions a tool list, but its locator ends at the header on line 165 and the first tool begins at 166. Preserve this original citation for independent assessment; correct it only through an explicit later child run.
4. MCP discovery is non-exhaustive. Documented implementations are not operationally verified; Sherlock's bounded not-found state is not a universal negative.
5. The pipeline and approved contracts, legacy artifacts and HTML retain all 11 baseline hashes. No account signup, paid service, authenticated API/MCP call, source publication or sampling was performed.

## Process and reproducibility

The research agent discovered/read primary pages, selected source URLs and authored the structured claim/paraphrase builder. The pipeline automated retrieval, readable snapshots, hashes, evidence packets, validation, lineage and metric calculation. This is agent-assisted research with controlled structured intake; it is not an embedded autonomous discovery/model service.

The archive preserves the pipeline, approved inputs/rules, research inputs/builder, original intake, all four pilot lineage runs and a separately labeled coordinator replay. Failed attempts are retained. The frozen research target is `pilot-first-pass-001`; repeated/cached runs do not add new apps or new independent evidence.

The first capture recorded 24 DNS failures. Approved access and precise additional references yielded 26 captures in later children. Fetch success is never scored as claim accuracy. The bundle README explains offline validation and exact replay; new live captures require re-reading and new line locations.

Task 04 is accepted as a completed first-pass pilot with the issues above disclosed. **Task 05 remains queued and has not started.**
