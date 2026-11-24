# Task 07: Source Index (CRM and Sales, IDs 1–10)

- **Target Run**: `work/research-runs/task07-first-pass-003`
- **Captured Sources**: 58 snapshots (all live HTTP captures, `synthetic: false`)
- **Resolved Evidence Observations Verified**: 296 (100% snapshot existence & SHA-256 match)

## Captured Sources

| App ID | App | Kind | Envs | Lines | Captured On | URL | Snapshot SHA-256 (prefix) |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 1 | Salesforce | `official_repository` | `testing,production` | 226 | 2026-11-23 | https://github.com/forcedotcom/postman-salesforce-apis | `8ae66aa9d358` |
| 1 | Salesforce | `official_repository` | `testing,production` | 546 | 2026-11-23 | https://github.com/salesforcecli/mcp | `630abf00744f` |
| 1 | Salesforce | `primary_docs` | `testing,production` | 5 | 2026-11-23 | https://help.salesforce.com/s/articleView?id=platform.integrate_what_is_api.htm&type=5 | `4efd14b1a5ba` |
| 1 | Salesforce | `primary_docs` | `testing,production` | 301 | 2026-11-23 | https://trailhead.salesforce.com/content/learn/modules/api_basics/api_basics_rest | `cc662decc49f` |
| 1 | Salesforce | `official_product_page` | `testing,production` | 166 | 2026-11-23 | https://www.salesforce.com/crm/pricing/ | `266a9ef20934` |
| 2 | HubSpot | `official_product_page` | `testing,production` | 328 | 2026-11-23 | https://developers.hubspot.com/developer-platform-basics | `b18b10c56e94` |
| 2 | HubSpot | `primary_docs` | `none` | 132 | 2026-11-23 | https://developers.hubspot.com/docs/api-reference/latest/overview | `197e437888bc` |
| 2 | HubSpot | `primary_docs` | `testing,production` | 176 | 2026-11-23 | https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/oauth/working-with-oauth | `79b9a6a8a9fc` |
| 2 | HubSpot | `primary_docs` | `testing,production` | 131 | 2026-11-23 | https://developers.hubspot.com/docs/apps/developer-platform/build-apps/authentication/overview | `60ec5450f10f` |
| 2 | HubSpot | `primary_docs` | `testing,production` | 186 | 2026-11-23 | https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server | `0ca10eeea7be` |
| 2 | HubSpot | `primary_docs` | `production` | 154 | 2026-11-23 | https://developers.hubspot.com/docs/apps/legacy-apps/private-apps/overview | `745a04424632` |
| 2 | HubSpot | `official_product_page` | `production` | 1 | 2026-11-23 | https://www.hubspot.com/pricing/crm | `2f1fbe52304d` |
| 3 | Pipedrive | `community_repository` | `testing,production` | 449 | 2026-11-23 | https://github.com/Wirasm/pipedrive-mcp | `62da1721cd82` |
| 3 | Pipedrive | `primary_docs` | `testing,production` | 134 | 2026-11-23 | https://pipedrive.readme.io/docs/core-api-concepts-authentication | `937d467b5dd7` |
| 3 | Pipedrive | `primary_docs` | `testing` | 26 | 2026-11-23 | https://pipedrive.readme.io/docs/developer-sandbox-account.md | `959e87955584` |
| 3 | Pipedrive | `primary_docs` | `production` | 24 | 2026-11-23 | https://pipedrive.readme.io/docs/enabling-api-for-company-users.md | `c9ad5678a96d` |
| 3 | Pipedrive | `primary_docs` | `production` | 210 | 2026-11-23 | https://pipedrive.readme.io/docs/marketplace-app-approval-process.md | `1a68120b8b9b` |
| 3 | Pipedrive | `primary_docs` | `testing,production` | 189 | 2026-11-23 | https://pipedrive.readme.io/docs/marketplace-creating-a-proper-app | `bbba42500773` |
| 3 | Pipedrive | `primary_docs` | `testing,production` | 34 | 2026-11-23 | https://pipedrive.readme.io/docs/marketplace-oauth-api.md | `ec2566c00fae` |
| 3 | Pipedrive | `primary_docs` | `none` | 34 | 2026-11-23 | https://pipedrive.readme.io/docs/pipedrive-api-v2.md | `893805bc9db9` |
| 3 | Pipedrive | `primary_docs` | `none` | 77 | 2026-11-23 | https://pipedrive.readme.io/llms.txt | `90a937e4b150` |
| 4 | Attio | `official_product_page` | `testing,production` | 739 | 2026-11-23 | https://attio.com/pricing | `f3cf91daf84e` |
| 4 | Attio | `primary_docs` | `none` | 417 | 2026-11-23 | https://docs.attio.com/llms.txt | `9254da109af6` |
| 4 | Attio | `primary_docs` | `testing,production` | 240 | 2026-11-23 | https://docs.attio.com/mcp/overview.md | `5096a080a9d9` |
| 4 | Attio | `primary_docs` | `testing,production` | 205 | 2026-11-23 | https://docs.attio.com/rest-api/guides/authentication | `db6dea14d9a9` |
| 4 | Attio | `primary_docs` | `testing,production` | 96 | 2026-11-23 | https://docs.attio.com/rest-api/overview | `c6e980184741` |
| 4 | Attio | `primary_docs` | `testing,production` | 351 | 2026-11-23 | https://docs.attio.com/rest-api/tutorials/connect-an-app-through-oauth.md | `faea4cc9d02c` |
| 5 | Twenty | `primary_docs` | `testing,production` | 105 | 2026-11-23 | https://docs.twenty.com/developers/extend/api | `d7acf795ef6c` |
| 5 | Twenty | `primary_docs` | `none` | 50 | 2026-11-23 | https://docs.twenty.com/llms.txt | `417b7fd262ea` |
| 5 | Twenty | `community_repository` | `testing,production` | 943 | 2026-11-23 | https://github.com/jezweb/twenty-mcp | `d962dcb649dc` |
| 5 | Twenty | `official_repository` | `testing,production` | 286 | 2026-11-23 | https://github.com/twentyhq/twenty | `64a7541e1464` |
| 5 | Twenty | `official_product_page` | `testing,production` | 371 | 2026-11-23 | https://twenty.com/pricing | `d9ca2d2c9794` |
| 6 | Podio | `primary_docs` | `testing,production` | 69 | 2026-11-23 | https://developers.podio.com/ | `2f5f0a0f44c0` |
| 6 | Podio | `primary_docs` | `testing,production` | 108 | 2026-11-23 | https://developers.podio.com/authentication | `0520f5cd31c0` |
| 6 | Podio | `primary_docs` | `none` | 136 | 2026-11-23 | https://developers.podio.com/doc | `4b270ae213af` |
| 6 | Podio | `official_product_page` | `testing,production` | 300 | 2026-11-23 | https://www.podio.com/site/pricing | `dbc535dee69b` |
| 7 | Zoho CRM | `primary_docs` | `testing,production` | 14 | 2026-11-23 | https://www.zoho.com/crm/developer/docs/api/v8/ | `c5dd26e5f489` |
| 7 | Zoho CRM | `primary_docs` | `testing,production` | 128 | 2026-11-23 | https://www.zoho.com/crm/developer/docs/api/v8/api-limits.html | `cdcbbe60556f` |
| 7 | Zoho CRM | `primary_docs` | `testing,production` | 38 | 2026-11-23 | https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html | `8a2b1164eed9` |
| 7 | Zoho CRM | `primary_docs` | `testing,production` | 43 | 2026-11-23 | https://www.zoho.com/crm/developer/docs/api/v8/register-client.html | `71b7c684f9fb` |
| 7 | Zoho CRM | `primary_docs` | `testing,production` | 45 | 2026-11-23 | https://www.zoho.com/crm/developer/docs/api/v8/scopes.html | `35cf12552f73` |
| 7 | Zoho CRM | `official_product_page` | `testing,production` | 268 | 2026-11-23 | https://www.zoho.com/crm/pricing.html | `c4c62f5bb339` |
| 7 | Zoho CRM | `official_product_page` | `testing,production` | 240 | 2026-11-23 | https://www.zoho.com/mcp/ | `633657206cbb` |
| 8 | Close | `primary_docs` | `testing,production` | 73 | 2026-11-23 | https://developer.close.com/ | `cdd59074e164` |
| 8 | Close | `primary_docs` | `testing,production` | 96 | 2026-11-23 | https://developer.close.com/api/overview/oauth-authentication.md | `e1f257204e96` |
| 8 | Close | `primary_docs` | `testing,production` | 21 | 2026-11-23 | https://developer.close.com/integrations/create-an-oauth-app.md | `2e04653bf8d5` |
| 8 | Close | `primary_docs` | `none` | 398 | 2026-11-23 | https://developer.close.com/llms.txt | `ae38b285e894` |
| 8 | Close | `primary_docs` | `testing,production` | 155 | 2026-11-23 | https://developer.close.com/mcp/ | `30f907797fcc` |
| 8 | Close | `primary_docs` | `testing,production` | 978 | 2026-11-23 | https://developer.close.com/mcp/tools.md | `24d0559296d6` |
| 8 | Close | `primary_docs` | `testing,production` | 523 | 2026-11-23 | https://developer.close.com/topics/authentication/ | `12f9bf2dc90f` |
| 8 | Close | `official_product_page` | `testing,production` | 346 | 2026-11-23 | https://www.close.com/pricing | `4afba348e5f7` |
| 9 | Copper | `primary_docs` | `testing,production` | 215 | 2026-11-23 | https://developer.copper.com/ | `bd2e3a000f73` |
| 9 | Copper | `primary_docs` | `testing,production` | 193 | 2026-11-23 | https://developer.copper.com/introduction/authentication.html | `5553f609dd7f` |
| 9 | Copper | `official_product_page` | `testing,production` | 366 | 2026-11-23 | https://www.copper.com/pricing | `c537c9799255` |
| 10 | DealCloud | `primary_docs` | `testing,production` | 235 | 2026-11-23 | https://api.docs.dealcloud.com/ | `51ab9c156a17` |
| 10 | DealCloud | `primary_docs` | `testing,production` | 464 | 2026-11-23 | https://api.docs.dealcloud.com/mcp/authentication | `1f70e0a549ef` |
| 10 | DealCloud | `primary_docs` | `testing,production` | 475 | 2026-11-23 | https://api.docs.dealcloud.com/mcp/getting-started | `84c0577b1646` |
| 10 | DealCloud | `official_product_page` | `production` | 588 | 2026-11-23 | https://www.intapp.com/dealcloud/ | `16a09c9a7fb8` |

## Uncaptured / Failed Fetch Attempts (Network Runs)

Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence.

| App ID | App | Status | HTTP | URL | Error |
| ---: | --- | --- | --- | --- | --- |
| 1 | Salesforce | `blocked` | `403` | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.htm | HTTP 403 |
| 1 | Salesforce | `blocked` | `403` | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_supported_editions.htm | HTTP 403 |
| 1 | Salesforce | `blocked` | `403` | https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_oauth.htm | HTTP 403 |
| 1 | Salesforce | `blocked` | `403` | https://developer.salesforce.com/signup | HTTP 403 |
| 1 | Salesforce | `blocked` | `403` | https://www.salesforce.com/form/developer-signup/ | HTTP 403 |
| 3 | Pipedrive | `http_error` | `404` | https://pipedrive.readme.io/docs/oauth-authorization | HTTP 404 |
| 3 | Pipedrive | `blocked` | `403` | https://www.pipedrive.com/en/pricing | HTTP 403 |
| 4 | Attio | `http_error` | `404` | https://docs.attio.com/rest-api/guides/oauth | HTTP 404 |
| 4 | Attio | `http_error` | `404` | https://attio.com/help/reference/integrations-automations/attio-mcp | HTTP 404 |
| 7 | Zoho CRM | `other_error` | `None` | https://help.zoho.com/portal/en/kb/crm/developer-space/sandbox/articles/sandbox-overview | Capture failed: empty_readable_content |
| 8 | Close | `http_error` | `404` | https://developer.close.com/topics/oauth/ | HTTP 404 |
| 8 | Close | `http_error` | `404` | https://developer.close.com/build-an-integration/create-an-oauth-app/ | HTTP 404 |
| 9 | Copper | `http_error` | `404` | https://developer.copper.com/oauth/overview.html | HTTP 404 |
| 9 | Copper | `http_error` | `404` | https://www.copper.com/blog/copper-mcp-server | HTTP 404 |
| 10 | DealCloud | `http_error` | `404` | https://api.docs.dealcloud.com/api-reference/getting-started/api-keys | HTTP 404 |
| 10 | DealCloud | `http_error` | `404` | https://api.docs.dealcloud.com/api-reference/getting-started/authorization-token | HTTP 404 |
| 10 | DealCloud | `http_error` | `404` | https://api.docs.dealcloud.com/mcp/available-tools | HTTP 404 |
| 10 | DealCloud | `http_error` | `404` | https://api.docs.dealcloud.com/getting-started/api-keys | HTTP 404 |
| 10 | DealCloud | `http_error` | `404` | https://api.docs.dealcloud.com/getting-started/authorization-token | HTTP 404 |
