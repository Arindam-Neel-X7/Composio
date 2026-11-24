# Task 08: Source Index (Support and Helpdesk, IDs 11–20)

- **Target Run**: `work/research-runs/task08-first-pass-003`
- **Captured Sources**: 58 snapshots (all live HTTP captures, `synthetic: false`; note 4 `developer.helpscout.com` snapshots returned compressed binary bytes and were excluded from claim citations)
- **Resolved Evidence Observations Verified**: 295 (100% snapshot existence & SHA-256 match)

## Captured Sources

| App ID | App | Kind | Envs | Lines | Captured On | URL | Snapshot SHA-256 (prefix) |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 11 | Zendesk | `primary_docs` | `testing,production` | 91 | 2026-11-23 | https://developer.zendesk.com/api-reference/introduction/security-and-auth/ | `d22aaaba3a32` |
| 11 | Zendesk | `primary_docs` | `testing,production` | 183 | 2026-11-23 | https://developer.zendesk.com/api-reference/ticketing/introduction/ | `741c17835bfa` |
| 11 | Zendesk | `primary_docs` | `testing,production` | 138 | 2026-11-23 | https://developer.zendesk.com/documentation/ticketing/getting-started/zendesk-api-quick-start/ | `94f5aa82ff30` |
| 11 | Zendesk | `community_repository` | `testing,production` | 419 | 2026-11-23 | https://github.com/reminia/zendesk-mcp-server | `4e90bc98aa89` |
| 11 | Zendesk | `primary_docs` | `testing` | 14 | 2026-11-23 | https://support.zendesk.com/hc/en-us/articles/4408828617370-Testing-changes-in-your-sandbox | `4ad5bf53c57c` |
| 11 | Zendesk | `official_product_page` | `testing,production` | 1030 | 2026-11-23 | https://www.zendesk.com/pricing/ | `229e488b83fb` |
| 12 | Intercom | `primary_docs` | `testing,production` | 93 | 2026-11-23 | https://developers.intercom.com/docs | `a22d69446a4d` |
| 12 | Intercom | `primary_docs` | `testing,production` | 89 | 2026-11-23 | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication | `5079583f2789` |
| 12 | Intercom | `primary_docs` | `testing,production` | 390 | 2026-11-23 | https://developers.intercom.com/docs/build-an-integration/learn-more/authentication/setting-up-oauth | `8216a9cadebf` |
| 12 | Intercom | `primary_docs` | `testing,production` | 418 | 2026-11-23 | https://developers.intercom.com/docs/guides/mcp | `da646bef59bb` |
| 12 | Intercom | `official_product_page` | `testing,production` | 348 | 2026-11-23 | https://www.intercom.com/pricing | `d07b8360ebd8` |
| 13 | Freshdesk | `primary_docs` | `testing,production` | 31897 | 2026-11-23 | https://developers.freshdesk.com/api/ | `97cd70178135` |
| 13 | Freshdesk | `primary_docs` | `testing,production` | 94 | 2026-11-23 | https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/oauth-implementation-in-apps/ | `07d6e7c9d1e0` |
| 13 | Freshdesk | `primary_docs` | `testing,production` | 153 | 2026-11-23 | https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/rest-apis/ | `cb68a81b9dba` |
| 13 | Freshdesk | `primary_docs` | `testing,production` | 153 | 2026-11-23 | https://support.freshdesk.com/support/solutions/articles/215517-how-to-find-your-api-key | `8992754847e4` |
| 13 | Freshdesk | `primary_docs` | `testing,production` | 261 | 2026-11-23 | https://support.freshdesk.com/support/solutions/articles/50000011778 | `2bc4b4baa653` |
| 13 | Freshdesk | `primary_docs` | `production` | 545 | 2026-11-23 | https://support.freshdesk.com/support/solutions/articles/50000012670 | `45c76d163aa7` |
| 13 | Freshdesk | `official_product_page` | `testing,production` | 228 | 2026-11-23 | https://www.freshworks.com/freshdesk/pricing/ | `1c8e96243390` |
| 14 | Front | `primary_docs` | `testing,production` | 327 | 2026-11-23 | https://dev.frontapp.com/docs/admin-mcp-server.md | `02e3b2e0e5d1` |
| 14 | Front | `primary_docs` | `testing,production` | 43 | 2026-11-23 | https://dev.frontapp.com/docs/authentication.md | `c769ce973cb9` |
| 14 | Front | `primary_docs` | `testing,production` | 67 | 2026-11-23 | https://dev.frontapp.com/docs/create-and-revoke-api-tokens.md | `9314b1aa72b1` |
| 14 | Front | `primary_docs` | `testing,production` | 261 | 2026-11-23 | https://dev.frontapp.com/docs/mcp-server.md | `3ab08a47c039` |
| 14 | Front | `primary_docs` | `testing,production` | 202 | 2026-11-23 | https://dev.frontapp.com/docs/oauth | `f3ce2aaa5a21` |
| 14 | Front | `primary_docs` | `none` | 428 | 2026-11-23 | https://dev.frontapp.com/llms.txt | `371aa8cb67c2` |
| 14 | Front | `primary_docs` | `testing,production` | 415 | 2026-11-23 | https://dev.frontapp.com/reference/introduction | `08fa0ee10636` |
| 14 | Front | `official_product_page` | `testing,production` | 436 | 2026-11-23 | https://front.com/pricing | `0ecaeba1fd53` |
| 15 | Pylon | `primary_docs` | `none` | 239 | 2026-11-23 | https://docs.usepylon.com/llms.txt | `8492851de372` |
| 15 | Pylon | `primary_docs` | `testing,production` | 145 | 2026-11-23 | https://docs.usepylon.com/pylon-docs/developer/api | `c4f7f31a82d3` |
| 15 | Pylon | `primary_docs` | `testing,production` | 85 | 2026-11-23 | https://docs.usepylon.com/pylon-docs/developer/api/api-reference.md | `03c3e741c8f4` |
| 15 | Pylon | `primary_docs` | `testing,production` | 76 | 2026-11-23 | https://docs.usepylon.com/pylon-docs/developer/api/authentication.md | `e182facdc3df` |
| 15 | Pylon | `primary_docs` | `testing,production` | 538 | 2026-11-23 | https://docs.usepylon.com/pylon-docs/integrations/pylon-mcp.md | `cffa73bec514` |
| 15 | Pylon | `official_product_page` | `testing,production` | 1313 | 2026-11-23 | https://usepylon.com/pricing | `2b1ee6d7f21a` |
| 16 | LiveAgent | `primary_docs` | `testing,production` | 148 | 2026-11-23 | https://support.liveagent.com/061754-Complete-API-reference | `20d64f43caa2` |
| 16 | LiveAgent | `primary_docs` | `testing,production` | 105 | 2026-11-23 | https://support.liveagent.com/647358-MCP-Integration-for-Agents | `59625c389263` |
| 16 | LiveAgent | `official_product_page` | `testing,production` | 861 | 2026-11-23 | https://www.liveagent.com/pricing/ | `ec9f58ba562b` |
| 17 | Plain | `primary_docs` | `none` | 212 | 2026-11-23 | https://www.plain.com/docs/_llms/developer.txt | `2f771b33ed9c` |
| 17 | Plain | `primary_docs` | `testing,production` | 22 | 2026-11-23 | https://www.plain.com/docs/graphql/authentication.md | `eadfbcd5eab9` |
| 17 | Plain | `primary_docs` | `testing,production` | 39 | 2026-11-23 | https://www.plain.com/docs/graphql/introduction.md | `9f873af307d3` |
| 17 | Plain | `primary_docs` | `testing,production` | 114 | 2026-11-23 | https://www.plain.com/docs/graphql/oauth.md | `1f2d76be356a` |
| 17 | Plain | `primary_docs` | `testing,production` | 142 | 2026-11-23 | https://www.plain.com/docs/integrations/mcp-server.md | `87b04fae1ec4` |
| 17 | Plain | `primary_docs` | `none` | 15 | 2026-11-23 | https://www.plain.com/docs/llms.txt | `c3824ee1a461` |
| 17 | Plain | `official_product_page` | `testing,production` | 537 | 2026-11-23 | https://www.plain.com/pricing | `4f0b73d3d8ac` |
| 18 | Help Scout | `primary_docs` | `testing,production` | 53 | 2026-11-23 | https://developer.helpscout.com/ | `4b2e229623f5` |
| 18 | Help Scout | `primary_docs` | `testing,production` | 100 | 2026-11-23 | https://developer.helpscout.com/docs-api/ | `ee71a6d0a109` |
| 18 | Help Scout | `primary_docs` | `testing,production` | 125 | 2026-11-23 | https://developer.helpscout.com/mailbox-api/ | `ae61d8a3eece` |
| 18 | Help Scout | `primary_docs` | `testing,production` | 203 | 2026-11-23 | https://developer.helpscout.com/mailbox-api/overview/authentication/ | `5c590aacef71` |
| 18 | Help Scout | `official_product_page` | `testing,production` | 424 | 2026-11-23 | https://www.helpscout.com/pricing/ | `17e5f2e17326` |
| 19 | Gorgias | `primary_docs` | `testing,production` | 13 | 2026-11-23 | https://developers.gorgias.com/docs/5-submit-app-for-review.md | `9bac8868ece1` |
| 19 | Gorgias | `primary_docs` | `testing,production` | 92 | 2026-11-23 | https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md | `c13da8222ac0` |
| 19 | Gorgias | `primary_docs` | `testing,production` | 20 | 2026-11-23 | https://developers.gorgias.com/docs/overview.md | `a522625ac5a1` |
| 19 | Gorgias | `primary_docs` | `none` | 199 | 2026-11-23 | https://developers.gorgias.com/llms.txt | `862bb13627c7` |
| 19 | Gorgias | `primary_docs` | `testing,production` | 203 | 2026-11-23 | https://developers.gorgias.com/reference/authentication | `1afd08613705` |
| 19 | Gorgias | `primary_docs` | `testing,production` | 206 | 2026-11-23 | https://developers.gorgias.com/reference/introduction | `622db2b197c2` |
| 19 | Gorgias | `community_repository` | `testing,production` | 214 | 2026-11-23 | https://github.com/mattcoatsworth/Gorgias-MCP-Server | `d3c6d14ed250` |
| 19 | Gorgias | `official_product_page` | `testing,production` | 161 | 2026-11-23 | https://www.gorgias.com/pricing | `c7ed49f7def6` |
| 20 | Gladly | `primary_docs` | `testing,production` | 51 | 2026-11-23 | https://developer.gladly.com/ | `4b5177a5b172` |
| 20 | Gladly | `primary_docs` | `testing,production` | 5595 | 2026-11-23 | https://developer.gladly.com/rest/ | `1c8ebb81f8a5` |
| 20 | Gladly | `official_product_page` | `testing,production` | 170 | 2026-11-23 | https://www.gladly.com/pricing/ | `6deba79d3746` |

## Uncaptured / Failed Fetch Attempts (Network Runs)

Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence.

| App ID | App | Status | HTTP | URL | Error |
| ---: | --- | --- | --- | --- | --- |
| 11 | Zendesk | `http_error` | `404` | https://support.zendesk.com/hc/en-us/articles/8244243105178-Using-the-Zendesk-MCP-client-to-access-MCP-tools-in-action-flows-and-advanced-action-flows | HTTP 404 |
| 12 | Intercom | `http_error` | `404` | https://developers.intercom.com/docs/build-an-integration/getting-started/build-an-app-for-your-workspace | HTTP 404 |
| 14 | Front | `http_error` | `404` | https://dev.frontapp.com/docs/core-api-authentication | HTTP 404 |
| 16 | LiveAgent | `http_error` | `404` | https://www.liveagent.com/api/ | HTTP 404 |
| 17 | Plain | `http_error` | `404` | https://www.plain.com/docs/api-reference/overview | HTTP 404 |
| 17 | Plain | `http_error` | `404` | https://www.plain.com/docs/api-reference/authentication | HTTP 404 |
| 18 | Help Scout | `http_error` | `404` | https://www.helpscout.com/blog/mcp-server/ | HTTP 404 |
| 20 | Gladly | `http_error` | `404` | https://developer.gladly.com/lookup/ | HTTP 404 |
| 20 | Gladly | `http_error` | `404` | https://help.gladly.com/docs/create-api-tokens | HTTP 404 |
| 20 | Gladly | `http_error` | `404` | https://help.gladly.com/docs/what-is-the-sandbox-environment | HTTP 404 |
