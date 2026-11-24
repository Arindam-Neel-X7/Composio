import json
from pathlib import Path
R=Path('D:/Composio'); W=R/'work/task-13-agent'
W.mkdir(exist_ok=True); (R/'outputs/task-13').mkdir(exist_ok=True)
SCOPES={
61:'GitHub.com REST API and official GitHub MCP server; personal and organization access, not Enterprise Server; testing versus production credential conditions remain separately assessed',
62:'Vercel REST API and official Vercel MCP server; hosted account/team resources, Hobby versus paid restrictions; testing and production assessed separately',
63:'Netlify hosted REST API v1 and official Netlify MCP server; personal/team sites and deployments; testing and production assessed separately',
64:'Cloudflare v4 management API and Cloudflare official remote MCP servers; account/zone resources and scoped tokens; testing and production assessed separately',
65:'Supabase hosted project Data REST API, Management API and official Supabase MCP; project API keys versus management OAuth/PAT; development and production separated',
66:'Neo4j Query API v2 and official Neo4j MCP; Community database Basic auth versus Enterprise/Aura SSO; local development versus production separated',
67:'Snowflake SQL REST API and Snowflake-managed MCP server; account SQL execution, OAuth/key-pair/PAT and role privileges; trial versus production separated',
68:'MongoDB Atlas Administration API v2 and official MongoDB MCP Atlas management tools; service accounts/API keys distinct from database connection credentials; free/testing versus production separated',
69:'Datadog hosted REST APIs v1/v2 and official Datadog MCP server; site-specific endpoints, API/application keys and OAuth; testing versus production assessed separately',
70:'Sentry hosted Web API and official Sentry MCP server; organization/user bearer tokens and remote OAuth MCP; self-hosted compatibility not presumed; testing and production assessed separately'}
URLS={
61:['https://docs.github.com/en/rest/about-the-rest-api/about-the-rest-api','https://docs.github.com/en/rest/authentication/authenticating-to-the-rest-api','https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens','https://raw.githubusercontent.com/github/github-mcp-server/main/README.md'],
62:['https://vercel.com/docs/rest-api','https://vercel.com/docs/agent-resources/vercel-mcp','https://vercel.com/docs/plans/hobby'],
63:['https://docs.netlify.com/api-and-cli-guides/api-guides/get-started-with-api/','https://raw.githubusercontent.com/netlify/netlify-mcp/main/README.md','https://www.netlify.com/pricing/'],
64:['https://developers.cloudflare.com/api/','https://developers.cloudflare.com/fundamentals/api/get-started/create-token/','https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md'],
65:['https://supabase.com/docs/guides/api','https://supabase.com/docs/guides/api/api-keys','https://supabase.com/docs/reference/api/introduction','https://supabase.com/docs/guides/getting-started/mcp','https://supabase.com/pricing'],
66:['https://neo4j.com/docs/query-api/current/','https://neo4j.com/docs/query-api/current/authentication-authorization/','https://neo4j.com/docs/mcp/current/','https://neo4j.com/docs/mcp/current/authentication/','https://neo4j.com/cloud/platform/aura-graph-database/'],
67:['https://docs.snowflake.com/en/developer-guide/sql-api/index','https://docs.snowflake.com/en/developer-guide/sql-api/authenticating','https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-mcp','https://docs.snowflake.com/en/user-guide/admin-trial-account'],
68:['https://www.mongodb.com/docs/atlas/api/','https://www.mongodb.com/docs/atlas/api/api-authentication/','https://www.mongodb.com/docs/mcp-server/overview/','https://www.mongodb.com/docs/mcp-server/prerequisites/','https://www.mongodb.com/docs/mcp-server/tools/','https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/'],
69:['https://docs.datadoghq.com/api/latest/','https://docs.datadoghq.com/account_management/api-app-keys/','https://docs.datadoghq.com/mcp_server/','https://docs.datadoghq.com/mcp_server/setup/','https://www.datadoghq.com/free-datadog-trial/'],
70:['https://docs.sentry.io/api/','https://docs.sentry.io/api/auth/','https://mcp.sentry.dev/','https://raw.githubusercontent.com/getsentry/sentry-mcp/main/README.md','https://sentry.io/pricing/']}
sources=[]
for aid,urls in URLS.items():
 for u in urls:
  kind='official_repository' if 'raw.githubusercontent.com' in u else ('official_product_page' if any(k in u for k in ['/pricing','/free-datadog-trial','/cloud/platform']) else 'primary_docs')
  sources.append(dict(app_id=aid,url=u,kind=kind,scope=SCOPES[aid],environments=['testing','production'],attribution_basis='Vendor-controlled documentation/product domain or vendor-owned GitHub repository; content inspected after capture',attribution_by='task13-codex-research-worker'))
(W/'sources-001.json').write_text(json.dumps({'sources':sources},indent=2),encoding='utf-8')
(W/'scopes.json').write_text(json.dumps(SCOPES,indent=2),encoding='utf-8')
print(len(sources),'explicit public sources')
