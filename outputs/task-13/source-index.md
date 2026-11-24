# Task 13: Source Index (Developer, Infra and Data platforms, IDs 61–70)

- **Target Run**: `work/research-runs/task13-first-pass-003`
- **Captured Sources**: 52 snapshots (all live HTTP captures, `synthetic: false`; 3 Datadog HTML captures with gzip-corrupt output are preserved in the run archive and excluded from claim citations in favor of readable `.md` captures)
- **Resolved Evidence Observations Verified**: 245 (100% snapshot existence & SHA-256 match)

## Captured Sources

| App ID | App | Kind | Envs | Lines | Captured On | URL | Snapshot SHA-256 (prefix) |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 61 | GitHub | `primary_docs` | `testing,production` | 333 | 2026-11-23 | https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens | `f821e2d97756` |
| 61 | GitHub | `primary_docs` | `testing,production` | 313 | 2026-11-23 | https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api | `10f0d347dad4` |
| 61 | GitHub | `primary_docs` | `testing,production` | 395 | 2026-11-23 | https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api | `f84ec67e24cb` |
| 61 | GitHub | `official_repository` | `testing,production` | 1505 | 2026-11-23 | https://raw.githubusercontent.com/github/github-mcp-server/main/README.md | `667665fe7aa8` |
| 62 | Vercel | `primary_docs` | `testing,production` | 268 | 2026-11-23 | https://vercel.com/docs/accounts/create-an-account | `21cc84b3f9a1` |
| 62 | Vercel | `primary_docs` | `testing,production` | 316 | 2026-11-23 | https://vercel.com/docs/agent-resources/vercel-mcp | `db82c7ed7197` |
| 62 | Vercel | `primary_docs` | `testing,production` | 86 | 2026-11-23 | https://vercel.com/docs/limits/fair-use-guidelines | `fe2e0326e22c` |
| 62 | Vercel | `primary_docs` | `testing,production` | 110 | 2026-11-23 | https://vercel.com/docs/plans/hobby | `b2b1e59f9d78` |
| 62 | Vercel | `primary_docs` | `testing,production` | 641 | 2026-11-23 | https://vercel.com/docs/rest-api | `6199be4bc8d4` |
| 62 | Vercel | `primary_docs` | `testing,production` | 2188 | 2026-11-23 | https://vercel.com/docs/rest-api/deployments/get-a-deployment-by-id-or-url | `7989d4ec638d` |
| 62 | Vercel | `primary_docs` | `testing,production` | 641 | 2026-11-23 | https://vercel.com/docs/rest-api/reference | `6199be4bc8d4` |
| 62 | Vercel | `primary_docs` | `testing,production` | 43 | 2026-11-23 | https://vercel.com/docs/rest-api/reference/authentication | `4c3c1881e8e3` |
| 62 | Vercel | `primary_docs` | `testing,production` | 641 | 2026-11-23 | https://vercel.com/docs/rest-api/reference/welcome | `6199be4bc8d4` |
| 63 | Netlify | `primary_docs` | `testing,production` | 691 | 2026-11-23 | https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/ | `c703074e7b51` |
| 63 | Netlify | `official_repository` | `testing,production` | 114 | 2026-11-23 | https://raw.githubusercontent.com/netlify/netlify-mcp/main/README.md | `7bf3eadc1b69` |
| 63 | Netlify | `official_product_page` | `testing,production` | 637 | 2026-11-23 | https://www.netlify.com/pricing/ | `ab74a6102740` |
| 64 | Cloudflare | `primary_docs` | `testing,production` | 11704 | 2026-11-23 | https://developers.cloudflare.com/api/ | `13f4a4e73aec` |
| 64 | Cloudflare | `primary_docs` | `testing,production` | 236 | 2026-11-23 | https://developers.cloudflare.com/fundamentals/api/get-started/create-token/ | `6f48483a7e8c` |
| 64 | Cloudflare | `official_repository` | `testing,production` | 65 | 2026-11-23 | https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md | `32f2dbb414f6` |
| 65 | Supabase | `primary_docs` | `testing,production` | 101 | 2026-11-23 | https://supabase.com/docs/guides/api | `dc871d04ef08` |
| 65 | Supabase | `primary_docs` | `testing,production` | 337 | 2026-11-23 | https://supabase.com/docs/guides/api/api-keys | `6dff57862de9` |
| 65 | Supabase | `primary_docs` | `testing,production` | 272 | 2026-11-23 | https://supabase.com/docs/guides/getting-started/mcp | `7ab1e1009881` |
| 65 | Supabase | `primary_docs` | `testing,production` | 360 | 2026-11-23 | https://supabase.com/docs/reference/api/introduction | `b2653af603a0` |
| 65 | Supabase | `official_product_page` | `testing,production` | 781 | 2026-11-23 | https://supabase.com/pricing | `2777cee29301` |
| 66 | Neo4j | `official_product_page` | `testing,production` | 652 | 2026-11-23 | https://neo4j.com/cloud/platform/aura-graph-database/ | `141f0a617ab9` |
| 66 | Neo4j | `primary_docs` | `testing,production` | 210 | 2026-11-23 | https://neo4j.com/docs/mcp/current/ | `726d464205d4` |
| 66 | Neo4j | `primary_docs` | `testing,production` | 314 | 2026-11-23 | https://neo4j.com/docs/mcp/current/authentication/ | `f8a58e1eb8a3` |
| 66 | Neo4j | `primary_docs` | `testing,production` | 201 | 2026-11-23 | https://neo4j.com/docs/query-api/current/ | `751acc4909fd` |
| 66 | Neo4j | `primary_docs` | `testing,production` | 247 | 2026-11-23 | https://neo4j.com/docs/query-api/current/authentication-authorization/ | `257c76861e57` |
| 67 | Snowflake | `primary_docs` | `testing,production` | 364 | 2026-11-23 | https://docs.snowflake.com/en/developer-guide/sql-api/authenticating | `eb853d95c4be` |
| 67 | Snowflake | `primary_docs` | `testing,production` | 99 | 2026-11-23 | https://docs.snowflake.com/en/developer-guide/sql-api/index | `6d223e5fcfed` |
| 67 | Snowflake | `primary_docs` | `testing,production` | 171 | 2026-11-23 | https://docs.snowflake.com/en/user-guide/admin-trial-account | `c164836df3db` |
| 67 | Snowflake | `primary_docs` | `testing,production` | 1083 | 2026-11-23 | https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp | `585ad1c5bab3` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 347 | 2026-11-23 | https://www.mongodb.com/docs/atlas/api/ | `f8f1d0408bc1` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 361 | 2026-11-23 | https://www.mongodb.com/docs/atlas/api/api-authentication/ | `6a5199487545` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 237 | 2026-11-23 | https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/ | `039d640a5a52` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 321 | 2026-11-23 | https://www.mongodb.com/docs/mcp-server/overview/ | `401c416cfb75` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 321 | 2026-11-23 | https://www.mongodb.com/docs/mcp-server/prerequisites/ | `a18108829a63` |
| 68 | MongoDB Atlas | `primary_docs` | `testing,production` | 521 | 2026-11-23 | https://www.mongodb.com/docs/mcp-server/tools/ | `ad48b01b5c4a` |
| 69 | Datadog | `primary_docs` | `testing,production` | 136 | 2026-11-23 | https://docs.datadoghq.com/account_management/api-app-keys.md | `1f7638b0c3a4` |
| 69 | Datadog | `primary_docs` | `testing,production` | 2072 | 2026-11-23 | https://docs.datadoghq.com/account_management/api-app-keys/ *(excluded: gzip-corrupt HTML)* | `a56f9932d76d` |
| 69 | Datadog | `primary_docs` | `testing,production` | 2072 | 2026-11-23 | https://docs.datadoghq.com/account_management/api-app-keys/?_task13=identity *(excluded: gzip-corrupt HTML)* | `a56f9932d76d` |
| 69 | Datadog | `primary_docs` | `testing,production` | 909 | 2026-11-23 | https://docs.datadoghq.com/api/latest/ | `c07b8f0271c1` |
| 69 | Datadog | `primary_docs` | `testing,production` | 95 | 2026-11-23 | https://docs.datadoghq.com/mcp_server.md | `921ecdeb82d1` |
| 69 | Datadog | `primary_docs` | `testing,production` | 2286 | 2026-11-23 | https://docs.datadoghq.com/mcp_server/ *(excluded: gzip-corrupt HTML)* | `6b996905ab9e` |
| 69 | Datadog | `primary_docs` | `testing,production` | 803 | 2026-11-23 | https://docs.datadoghq.com/mcp_server/setup.md | `db2fee977e17` |
| 69 | Datadog | `official_product_page` | `testing,production` | 305 | 2026-11-23 | https://www.datadoghq.com/free-datadog-trial/ | `fc33471de2de` |
| 70 | Sentry | `primary_docs` | `testing,production` | 77 | 2026-11-23 | https://docs.sentry.io/api/ | `bf807ef6d639` |
| 70 | Sentry | `primary_docs` | `testing,production` | 551 | 2026-11-23 | https://docs.sentry.io/api/auth/ | `efbbd3248386` |
| 70 | Sentry | `primary_docs` | `testing,production` | 51 | 2026-11-23 | https://mcp.sentry.dev/ | `e7da19afd6a6` |
| 70 | Sentry | `official_repository` | `testing,production` | 258 | 2026-11-23 | https://raw.githubusercontent.com/getsentry/sentry-mcp/main/README.md | `446f21cd7698` |
| 70 | Sentry | `official_product_page` | `testing,production` | 521 | 2026-11-23 | https://sentry.io/pricing/ | `c06c7bd05770` |

## Uncaptured / Failed Fetch Attempts (Network Runs)

Failed fetches are preserved in `fetches` telemetry and never used to assert gating or absence (`7` uncaptured source URLs across IDs 68 and 69).

| App ID | App | Status | HTTP | URL | Error |
| ---: | --- | --- | --- | --- | --- |
| 68 | MongoDB Atlas | `http_error` | `404` | https://www.mongodb.com/docs/atlas/api/api-resources/ | HTTP 404 |
| 69 | Datadog | `timeout` | `None` | https://docs.datadoghq.com/mcp_server/setup/ | Request timed out |
| 69 | Datadog | `http_error` | `404` | https://docs.datadoghq.com/mcp_server/index.md | HTTP 404 |
| 69 | Datadog | `http_error` | `404` | https://docs.datadoghq.com/mcp_server/setup/index.md | HTTP 404 |
| 69 | Datadog | `http_error` | `404` | https://raw.githubusercontent.com/DataDog/documentation/master/content/en/account_management/api-app-keys.md | HTTP 404 |
| 69 | Datadog | `http_error` | `404` | https://raw.githubusercontent.com/DataDog/documentation/master/content/en/mcp_server/_index.md | HTTP 404 |
| 69 | Datadog | `http_error` | `404` | https://raw.githubusercontent.com/DataDog/documentation/master/content/en/mcp_server/setup.md | HTTP 404 |
