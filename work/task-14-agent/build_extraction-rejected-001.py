"""Researcher-authored Task 14 extraction. Explicit captured-line facts, no app-name inference."""
import copy,json,sys
from pathlib import Path
ROOT=Path('D:/Composio')
sys.path.insert(0,str(ROOT))
import research_pipeline as p
sys.path.insert(0,str(ROOT/'work/task-14-agent'))
from make_sources import SCOPES
CAP=sys.argv[1]
D=ROOT/'work/research-runs'/CAP
p.verify_seal(D)
records=copy.deepcopy(p.read_json(D/'records.json'))
caps=p.read_json(D/'captures.json')

def build(r):
 a=r['identity']['id']; scope=SCOPES[a]
 def c(k,v=None,ev=(),status='observed',refs=(),why='Documentary observation from captured source; independent adjudication pending.'):
  return dict(claim_id=f'{a}.{k}',status=status,value=v,context=scope,evidence=list(ev),supporting_claim_refs=[f'{a}.{x}' for x in refs],rationale=why)
 def e(url,lo,hi,para):
  matches=[x for x in caps if x['spec']['app_id']==a and x['spec']['url']==url]
  assert len(matches)==1,(a,url)
  cap=matches[0]; lines=(D/cap['snapshot_ref']).read_text(encoding='utf-8').splitlines()
  assert 1<=lo<=hi<=len(lines),(url,lo,hi,len(lines))
  ev=p.evidence_for(cap,lo,lines[lo-1]); ev.update(locator=f'lines:{lo}-{hi}',observation='paraphrase: '+para)
  return ev
 def init(identity,purpose,ev):
  r['identity']['resolution']=c('identity',identity,ev)
  r['purpose']=c('purpose',purpose,ev)
 def auth(k,method,details,ev,sub='',scopes=()):
  r['auth']['items'].append(c('auth.'+k,dict(method=method,context=sub or scope,scopes=list(scopes),details=details),ev))
 def protocol(v,ev):r['api_surface']['protocols']['items'].append(c('api.protocol.'+v.lower(),v,ev))
 def group(k,v,ev):r['api_surface']['resource_groups']['items'].append(c('api.group.'+k,v,ev))
 def elig(env,k,v,ev,why):r['credential_eligibility'][env][k]=c(env+'.'+k,v,ev,why=why)
 def both(k,v,ev,why):
  for env in ['testing','production']:elig(env,k,v,ev,why)
 def mcp(origin,name,ev,source,server,repo,toolscope):
  r['mcp']['entries']=[c('mcp.server',dict(origin=origin,name=name,source_url=source,repository_url=repo,server_url=server,scope=toolscope,operational_check=c('mcp.operational',None,status='not_researched',why='No MCP connection or tool call performed.')),ev)]
  r['mcp']['discovery']=c('mcp.discovery','found',ev)
 def finish(bscope,blockers,nexts,ev,extra=()):
  groups=r['api_surface']['resource_groups']['items']
  if groups:
   r['api_surface']['breadth']=c('api.breadth','moderate',sum([x['evidence'] for x in groups],[]),'inferred',[x['claim_id'].split('.',1)[1] for x in groups],why='Captured resource groups cover multiple related work-management workflows. Qualitative scope, not an endpoint count or exhaustive inventory.')
  r['buildability']=c('buildability',dict(verdict='conditional',scope=bscope,blockers=blockers,next_steps=nexts),ev,'inferred',['identity']+[x['claim_id'].split('.',1)[1] for x in r['api_surface']['protocols']['items']]+[x['claim_id'].split('.',1)[1] for x in r['auth']['items']]+list(extra),why='A documented API supports a possible agent wrapper; feasibility remains conditional on account permissions and the stated access gaps. No implementation, credential acquisition, or operational test occurred.')
 for env in ['testing','production']:
  r['credential_eligibility'][env]['context']=scope
  for k,v in list(r['credential_eligibility'][env].items()):
   if k!='context':r['credential_eligibility'][env][k]=c(env+'.'+k,None,status='unknown',why=f'Checked selected public documentation; {k} for this {env} path was not established. Silence does not establish absence. Testing is not assumed to be an isolated sandbox; production does not inherit trial entitlements.')
 for target in [r['auth'],r['api_surface']['protocols'],r['api_surface']['resource_groups']]:
  target.update(coverage_status='partial',items=[],notes='Only the captured and cited interfaces are covered; no claim of exhaustive vendor coverage. Edition, resource permissions and plan limits must be retained.')
 r['mcp']['discovery']=c('mcp.discovery',None,status='unknown',why='Selected documentation checked; matching callable server origin/direction not yet established. This is not proof that no MCP exists.')
 if a==71:
  u='https://developers.notion.com/docs/create-a-notion-integration'; au='https://developers.notion.com/docs/authorization'; mu='https://developers.notion.com/docs/get-started-with-mcp'
  ep=e(u,69,73,'Notion API builds tools and automations to create pages, organize data and share feedback in a Notion workspace.')
  init('Notion hosted workspace developer API and Notion MCP.','Workspace content platform exposing pages, structured data and feedback automation through its API.',[ep])
  ea=e(au,85,98,'Internal connections use static API tokens for REST requests; creation requires a workspace owner and pages must be shared with the connection.')
  auth('internal','Bearer_token','Static internal connection API token in Authorization: Bearer; team automation requires workspace-owner creation and explicit page sharing.',[ea])
  pat=e(au,119,127,'Personal access tokens are user-scoped credentials created in the Developer portal and sent with Authorization: Bearer; they act using the user permissions.')
  auth('pat','Bearer_token','User-scoped personal access token sent in Authorization: Bearer.',[pat])
  eo=e(au,128,148,'OAuth integrations use OAuth 2.0; configure client credentials and redirect URI then obtain user authorization and exchange the temporary code. Marketplace submission or review is not required to start authorization.')
  auth('oauth','OAuth2','OAuth 2.0 authorization-code flow for scoped or public integrations; users select pages.',[eo])
  protocol('REST',[ea]); protocol('SDK',[e(u,225,228,'The quickstart links an official JavaScript client library for Node.js.')])
  for k,v,l,h in [('pages','Pages and page content',208,209),('data','Databases and data sources',210,215),('comments','Page and inline comments',218,219)]:group(k,v,[e(u,l,h,v+' are documented API resources.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e('https://developers.notion.com/reference/intro',78,93,'Public introduction gives HTTPS base URL, Bearer and version headers, JSON conventions, and pagination documentation.')])
  both('admin_approval_required',True,[ea],'Internal-connection route only: workspace owner must create the connection. PAT and public OAuth paths have different controls; this is not an app-wide restriction.')
  both('vendor_approval_required',False,[eo],'Configured OAuth integration authorization can begin without Marketplace submission or review; this says nothing about a Marketplace listing or MCP client approval.')
  both('self_serve',True,[e(u,72,82,'User creates a PAT in the Developer portal; Business/Enterprise PAT creation is restricted by default and workspace owner must enable it.')],'PAT route for an eligible member with PAT creation enabled; admin policy is a prerequisite, not vendor or partner approval.')
  em=e(mu,83,99,'Notion documents its remote MCP server at https://mcp.notion.com/mcp; after authorization AI assistants can read and update workspace content the user can access.')
  em2=e(mu,300,315,'Hosted Notion MCP supports OAuth and plan-gated MCP tokens; workspace members only, not guests. The hosted server is actively maintained; older local server is not.')
  mcp('official','Notion hosted MCP',[em,em2],mu,'https://mcp.notion.com/mcp',None,'Callable hosted server exposing accessible Notion workspace content to external MCP clients; members only. OAuth on every plan; MCP tokens require Business/Enterprise owner. Not the deprecated local server.')
  finish('Create and update permitted Notion pages through an API wrapper or hosted MCP.',['Internal connections require owner creation and shared pages; PAT policy can restrict creation.','Hosted MCP excludes guests; unattended MCP token path requires Business/Enterprise owner.'],['Select PAT, internal connection, or OAuth actor model; check workspace controls.','Validate permissions and rate limits in an authorized workspace before deployment.'],[ea,pat,em2])
 if a==72:
  u='https://support.airtable.com/docs/getting-started-with-airtables-web-api'; au='https://support.airtable.com/docs/creating-personal-access-tokens'; mu='https://support.airtable.com/docs/using-the-airtable-mcp-server'
  ep=e(au,17,19,'Airtable personal access tokens permit scoped access to data in Airtable bases and workspaces.')
  init('Airtable hosted bases/workspaces Web API and Airtable MCP.','Platform for structured bases and workspaces with programmatic data access.',[ep])
  ea=e(au,17,30,'Users create personal access tokens in the developer hub, selecting scopes and base/workspace resources.')
  auth('pat','other','Personal access token with selected scopes and base/workspace resource access in the Authorization header; captured support docs do not establish the exact header prefix. Not the deprecated API key.',[ea,e(au,90,95,'Airtable accepts complete personal tokens through the Authorization header; rejected tokens return 401.')])
  eo=e(u,41,44,'Create base via POST /v0/meta/bases supports PAT or OAuth tokens on all plans; deprecated API-key authentication has different historical restrictions.')
  auth('oauth','OAuth2','OAuth authorization for third-party integrations; token accepted by Web API. Full grant configuration not captured.',[eo,e(au,58,64,'Legacy API keys no longer access the API; users should migrate to PATs for individual use or OAuth for third-party integrations.')])
  protocol('REST',[eo,e(u,14,23,'Web API lists table records through resource URLs with pagination and documents POST base creation.')])
  r['api_surface']['protocols']['items'][-1].update(status='inferred',supporting_claim_refs=[f'{a}.api.group.records',f'{a}.api.group.bases'],rationale='REST-style interface inferred from resource-oriented HTTP URLs, POST create-base and GET metadata descriptions; exact protocol label was not readable in the developer-reference shell.')
  group('records','Table records with pagination',[e(u,14,16,'List-record API returns pages of up to 100 records from a table.')])
  group('bases','Base creation and metadata',[eo])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,14,16,'Public support documentation explains list-record API pagination; developer-reference pages captured only a title.')])
  ef=e(u,32,36,'The Free plan allows 1000 API calls per workspace per month; other plans have different call limits.')
  both('free_access',True,[ef],'Ordinary Web API use on Free plan within 1000 calls/workspace/month; not Enterprise-only scopes or an isolated sandbox.')
  both('paid_required',False,[ef],'Limited ordinary Web API use has a documented Free-plan quota; additional or enterprise capabilities are not covered by this negative.')
  both('self_serve',True,[ea],'Eligible user creates a PAT in developer hub with scopes and resources; existing permissions and organization allowlist policy remain prerequisites.')
  em=e(mu,73,87,'External remote MCP HTTP clients connect to https://mcp.airtable.com/mcp using OAuth; some clients can instead use a PAT. Restricted organizations require integration allowlisting.')
  em2=e(mu,51,64,'MCP exposes selected bases/apps under user permissions and API rate limits; restricted enterprise integrations need admin allowlisting.')
  mcp('official','Airtable hosted MCP',[em,em2],mu,'https://mcp.airtable.com/mcp',None,'Callable hosted server lets external MCP clients access permitted Airtable bases and apps. OAuth or documented PAT alternative; tenant policy and base permissions apply.')
  both('admin_approval_required',True,[e(mu,104,117,'Organization admin must allowlist an MCP integration when third-party integrations are restricted.')],'Conditional restricted-organization MCP path only; not a universal requirement for every Airtable user or PAT.')
  finish('Read permitted Airtable table records and create bases via Web API or connect external clients to Airtable MCP.',['PAT scopes and base permissions constrain operations; organization policy may require allowlisting.','Developer Web API reference captures are JavaScript shells, so detailed OAuth setup remains unresolved.'],['Confirm intended base-level access and call quota.','Inspect full endpoint/grant reference before an authorized test.'],[ea,ef,em2])
 if a==73:
  u='https://linear.app/developers/graphql'; au='https://linear.app/developers/oauth-2-0-authentication'; wu='https://linear.app/docs/api-and-webhooks'; mu='https://linear.app/docs/mcp'
  ep=e(u,43,60,'Linear offers a public GraphQL API with personal API keys and OAuth2 authentication.')
  init('Linear hosted public GraphQL API and Linear hosted MCP.','Issue and team workflow platform exposing query and mutation APIs.',[ep,e(u,87,101,'Linear API examples retrieve teams and their issues; issue creation and editing are documented.')])
  ea=e(u,58,66,'Personal scripts authenticate using API keys created in Security & access settings, passed as Authorization: <API_KEY>.')
  auth('key','API_key','Personal API key in Authorization header, without a Bearer prefix for GraphQL requests.',[ea])
  eo=e(u,49,57,'OAuth2 access tokens are passed as Authorization: Bearer for the GraphQL API.')
  auth('oauth','OAuth2','OAuth2 user authorization with bearer access token for GraphQL.',[eo,e(au,108,122,'User authorization returns an authorization code which is exchanged for an API access token.')])
  auth('client_credentials','OAuth2','Optional OAuth2 client_credentials grant for server-to-server use; app actor, enabled on the OAuth app.',[e(au,227,231,'Linear supports client_credentials grant for OAuth2 apps; tokens use the app actor, expire in 30 days, and require enabling client credentials tokens.')])
  protocol('GraphQL',[e(u,43,47,'Public API uses GraphQL endpoint https://api.linear.app/graphql and supports schema introspection.')]);protocol('SDK',[e(u,72,73,'Linear TypeScript SDK exposes the GraphQL schema, models and mutations.')])
  group('issues','Issues and issue creation/editing',[e(u,124,126,'Linear documents creating and editing issues through mutations.')]);group('teams','Teams and team issue queries',[e(u,87,101,'The GraphQL API retrieves team IDs and queries issues for a selected team.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,72,77,'The GraphQL API is publicly explorable in Apollo Studio without login for schema browsing; API data requests still require auth.')])
  both('self_serve',True,[e(wu,74,77,'Admins and permitted members create personal API keys in account settings, with permission and team restrictions.')],'Personal-key route for an admin or member allowed by workspace policy; no claim of automatic entitlement for all members.')
  both('admin_approval_required',True,[e(wu,78,83,'Creating/managing webhooks and viewing the OAuth application administration page requires admin permissions.')],'OAuth-app creation/management and webhook route only; personal key route can be available to permitted members.')
  em=e(mu,65,75,'Linear centrally hosts its MCP server for external clients; tools find/create/update issues, projects and comments. Primary Streamable HTTP endpoint is https://mcp.linear.app/mcp; interactive setup uses OAuth2.1.')
  mcp('official','Linear hosted MCP',[em],mu,'https://mcp.linear.app/mcp',None,'Callable hosted server for external clients to find, create and update Linear issues, projects and comments through authenticated Streamable HTTP.')
  finish('Query teams and read/create/edit issues through a GraphQL agent wrapper or Linear hosted MCP.',['Member API key creation depends on workspace policy; OAuth application administration requires admin permissions.','Plan-specific credential costs and isolated sandbox entitlement are unresolved.'],['Choose personal-key or user/app OAuth actor route.','Check workspace policy, permissions and limits before authorized testing.'],[ea,e(wu,74,83,'Admin policy controls member keys; OAuth/webhook management requires workspace admin permissions.'),em])
 if a==74:
  u='https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/'; au='https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/'; mu='https://atlassian.github.io/atlassian-mcp-server/'
  ep=e(u,151,158,'This is the Jira Cloud platform REST API v3 reference.')
  init('Jira Cloud platform REST API v3; excludes Data Center/Server.','Cloud issue and project management with REST resources and remote MCP access.',[ep,e(u,88,99,'The reference lists issue search and issues.'),e(u,113,127,'The reference lists project resources.')])
  ea=e(au,69,80,'Personal REST scripts can use Basic auth with Atlassian account email and API token; passwords are deprecated; OAuth2 authorization-code grants are an alternative.')
  auth('basic','Basic','Atlassian account email and API token for personal REST scripts; not account password.',[ea])
  eo=e(u,186,198,'Non-Forge/Connect integrations use OAuth 2.0 authorization-code grants (3LO); API requests use the api.atlassian.com/ex/jira/<cloudId>/rest/api/3 route; personal bots can use Basic auth.')
  auth('oauth','OAuth2','OAuth 2.0 authorization-code grant (3LO) for distributable external integrations.',[eo])
  protocol('REST',[ep,eo]);group('issues','Issues and issue search',[e(u,88,99,'REST reference lists issue search, types, votes, watchers, worklogs and issues.')]);group('projects','Projects and project configuration',[e(u,113,127,'REST reference lists projects, components, versions, roles and permission schemes.')]);group('users','Users and user search',[e(u,139,142,'REST reference lists user properties, user search and users.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[ep])
  both('self_serve',True,[e(au,94,102,'A user generates an API token for their Atlassian account for Basic auth.')],'Personal script token route for an existing Jira Cloud user; does not establish tenant access or commercial integration approval.')
  em=e(mu,1,18,'Official cloud-hosted Atlassian MCP bridges external AI tools to Jira and other Atlassian Cloud products using OAuth2.1 or API tokens. Recommended endpoint is https://mcp.atlassian.com/v2/mcp.')
  mcp('official','Atlassian remote MCP for Jira Cloud',[em],mu,'https://mcp.atlassian.com/v2/mcp',None,'Callable hosted server exposes Jira Cloud data/actions to external MCP clients; supports other Atlassian products but this record concerns Jira Cloud.')
  both('admin_approval_required',True,[e(mu,238,248,'Headless MCP token authentication requires an organization admin to enable API-token authentication; tokens must have required scopes.')],'Headless Atlassian MCP API-token authentication route only; do not project onto every REST or interactive OAuth use.')
  finish('Read and update permitted Jira Cloud issues/projects via REST v3 or hosted MCP.',['Operations require the calling user permissions.','Commercial integrations must use a distributable 3LO app rather than collect customer API tokens.','Headless MCP token authentication requires organization-admin enablement.'],['Choose personal script or distributable OAuth integration model.','Confirm site, project permissions and admin MCP policy before authorized tests.'],[e(u,199,215,'Most operations require user/project/site permissions.'),e(au,82,91,'Apps collecting API tokens or instructing customers to create individual 3LO apps do not comply with cloud app security requirements; use one distributable 3LO app.'),e(mu,238,248,'Headless MCP API-token authentication requires admin enablement.')])
 if a==75:
  u='https://developers.asana.com/docs/overview'; au='https://developers.asana.com/docs/personal-access-token'; ou='https://developers.asana.com/docs/oauth'; su='https://developers.asana.com/docs/developer-sandbox'; mu='https://developers.asana.com/docs/integrating-with-asanas-mcp-server'
  ep=e(u,91,98,'Asana apps integrate other tools, add/extract Work Graph data and automate workflows with REST API, components and webhooks.')
  init('Asana hosted REST API and standard Asana V2 MCP; Command MCP excluded.','Work Graph and workflow platform with APIs for tool integrations and workflow automation.',[ep])
  ea=e(au,91,106,'Generate a PAT in Asana developer console and send it in Authorization: Bearer to the REST API.')
  auth('pat','Bearer_token','Personal access token created in developer console and sent as Authorization: Bearer.',[ea])
  eo=e(ou,89,103,'Asana supports OAuth authorization-code grant; API requests carry bearer access tokens.')
  auth('oauth','OAuth2','OAuth 2.0 authorization-code grant for acting on behalf of a user; app registration required.',[eo,e(ou,128,145,'Register app in developer console and configure OAuth permission scopes; examples include projects:read and tasks:read/write/delete.')],scopes=['projects:read','tasks:read','tasks:write','tasks:delete'])
  protocol('REST',[e(u,105,111,'Asana REST API can be explored from the API reference; choose existing workspace, free account or requested developer sandbox.')])
  group('tasks','Tasks',[e(ou,140,146,'Documented OAuth scopes include tasks:read, tasks:write and tasks:delete.')]);group('projects','Projects',[e(ou,140,145,'OAuth scope example includes projects:read.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,105,111,'Public developer overview links an API reference and embedded API explorer.')])
  elig('testing','free_access',True,[e(u,108,110,'Testing may use an existing workspace, free account or requested developer sandbox; developer sandbox permits premium-feature tests.')],'Free-account ordinary API testing path; this does not imply free premium production access.')
  elig('testing','self_serve',True,[e(u,108,110,'Free-account API testing can start with a PAT created in developer console.')],'PAT testing in a free or existing workspace; distinct from request/provisioning process for an isolated developer sandbox.')
  es=e(su,91,100,'Temporary developer sandboxes are requested by form for integration developers or existing Starter+ customers; premium features on request, maximum one year; provisioning may take a week and extensions undergo Legal review.')
  elig('testing','sandbox_access',True,[es],'A request-based developer sandbox path is documented; approval/provisioning is not assumed granted.')
  elig('testing','vendor_approval_required',True,[es],'Requested developer sandbox must be provisioned by Asana; not a commercial partnership and not required for free-account ordinary API testing.')
  em=e(mu,89,105,'The official Asana V2 MCP server uses OAuth and requires pre-registering an MCP app; Command is separate and V1 SSE is deprecated.')
  em2=e(mu,139,158,'Asana MCP endpoint is https://mcp.asana.com/v2/mcp with bearer token; dynamic client registration is unsupported.')
  em3=e(mu,175,177,'MCP actions run as the authorizing user and are limited to accessible workspaces, projects and tasks.')
  mcp('official','Asana V2 MCP',[em,em2,em3],mu,'https://mcp.asana.com/v2/mcp',None,'Callable official hosted Asana V2 server for external MCP clients; OAuth MCP app pre-registration required and user workspace/project/task permissions apply; Command server excluded.')
  finish('Read projects and manage permitted tasks through REST or standard Asana V2 MCP.',['Free-account tests do not establish premium-feature entitlements.','Requested isolated sandbox has provisioning/term limits; MCP requires pre-registration and separate MCP tokens.'],['Choose ordinary workspace testing or request a scoped sandbox.','Register OAuth API/MCP app with correct distribution and permissions before authorized tests.'],[es,em,e(mu,95,97,'V1 MCP is deprecated; MCP-app tokens do not work with the standard REST API.')])
 if a==76:
  u='https://developer.monday.com/api-reference/docs/introduction-to-graphql'; au='https://developer.monday.com/api-reference/docs/authentication'; su='https://developer.monday.com/api-reference/docs/developer-sandbox'; mu='https://developer.monday.com/api-reference/docs/mcp-api-token'; hu='https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP'
  ep=e(u,151,161,'monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns.')
  init('monday.com hosted GraphQL platform API v2 and monday MCP.','Workspace and board platform exposing data queries and mutations for workflow integrations.',[ep,e(u,199,204,'GraphQL mutation example creates an item on a board.')])
  ea=e(au,151,174,'Platform API personal V2 tokens mirror user UI permissions and are accessed through Developer Center; send token in Authorization header.')
  auth('personal','API_key','Personal V2 API token in Authorization header; permissions mirror UI permissions.',[ea])
  auth('mcp_oauth','OAuth2','Compatible hosted-MCP clients authorize via OAuth; per-user data permissions apply.',[e(mu,151,154,'Hosted MCP supports OAuth for compatible clients or a personal token for testing/custom clients.'),e(hu,144,148,'Each user authorizes MCP via OAuth, with permissions limited to user access and granted OAuth scopes.')],sub='Hosted monday MCP; this observation does not specify platform API OAuth grant details.')
  protocol('GraphQL',[ep]);group('boards','Boards and columns',[e(u,160,171,'GraphQL example queries columns on boards.')]);group('items','Board items',[e(u,199,207,'GraphQL create_item mutation creates a board item and returns its ID/name.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[ep])
  es=e(su,151,158,'Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center.')
  for k in ['free_access','sandbox_access','self_serve']:elig('testing',k,True,[es],'Free developer-account testing path; separate from production and advanced-capacity requests.')
  elig('testing','paid_required',False,[es],'Documented developer sandbox is free for development/testing.')
  elig('testing','trial_access',True,[e(su,159,163,'An alternate trial account is offered to evaluate monday beyond development; extension requests contact support.')],'Alternate evaluation-trial path; not the free developer sandbox and not a production entitlement.')
  both('self_serve',True,[ea],'Existing-user platform API token through Developer Center, subject to API/user permissions; testing may also use free developer account.')
  em=e(mu,151,175,'monday hosted MCP supports OAuth or personal API token, with token clients sending Bearer token to https://mcp.monday.com/mcp; personal tokens are for individual development, not integrations used by others.')
  em2=e(hu,110,125,'monday MCP is a hosted server connecting external AI tools to workspace data; active account, user permissions and possible admin AI Connector settings apply.')
  mcp('official','monday hosted MCP',[em,em2],mu,'https://mcp.monday.com/mcp',None,'Callable hosted server lets external AI clients query or modify permitted monday workspace data; OAuth route for clients, personal-token route for personal development/testing.')
  finish('Query boards/columns and create board items via GraphQL, or use hosted MCP under permitted actor.',['Free developer sandbox is explicitly not for production business workflows or end customers.','MCP user permissions and AI Connector admin policy apply.'],['Keep developer account and production data separate.','Choose personal API token or appropriate OAuth integration route; check limits before authorized tests.'],[e(su,183,191,'Developer accounts are testing-only, not production business workflows; extra capacity requests are reviewed.'),em2])
 if a==77:
  au='https://developer.clickup.com/docs/authentication'; u='https://developer.clickup.com/reference/gettasks'; mu='https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1'; hu='https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP'
  ep=e(hu,17,24,'ClickUp MCP supports task workflows, work reporting, time tracking, search of tasks/docs/comments and collaboration with comments/chat.')
  init('ClickUp hosted public API v2 and ClickUp hosted MCP server, not the feature for consuming other MCP servers.','Workspace/task platform exposing task management, work reporting, time tracking and collaboration.',[ep])
  ea=e(au,55,77,'Personal/testing API requests use personal tokens generated from account Apps settings and sent in the Authorization header.')
  auth('personal','API_key','Personal API token sent as Authorization: {personal_token}, for individual or testing use.',[ea])
  eo=e(au,78,97,'Multi-user apps use OAuth2 authorization-code flow; only workspace owners/admins create OAuth apps and configure the redirect URL.')
  auth('oauth','OAuth2','Public API OAuth 2.0 authorization-code flow; app creation requires workspace owner/admin and each user authorizes workspaces.',[eo,e(au,106,110,'Users authorize workspaces and exchange the authorization code; token is sent in Authorization: Bearer.')])
  em=e(hu,67,78,'Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup.')
  auth('mcp_oauth','OAuth2','Hosted MCP uses OAuth 2.1 with PKCE; personal public-API keys cannot authenticate this MCP endpoint.',[em],sub='Hosted ClickUp MCP endpoint, distinct from public API token authentication.')
  # HTTP resource methods/endpoints in v2 reference are architectural evidence for REST style.
  protocol('REST',[e(u,9,23,'ClickUp API v2 reference lists resource-oriented comment endpoints with GET/POST/PUT/DELETE methods.')])
  group('comments','Task/List comments',[e(u,15,25,'API v2 lists read/create/update/delete and threaded comment operations.')]);group('lists','Lists and list metadata',[e(u,63,70,'API v2 lists get/create/update/delete List operations.')]);group('time','Time entries and timers',[e(u,131,144,'API v2 lists time-entry read/create/update/delete and timer start/stop operations.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,8,25,'Public ClickUp API v2 reference exposes endpoint names and resource methods.')])
  both('self_serve',True,[ea],'Personal API token generated by existing signed-in user; production multi-user OAuth app requires owner/admin setup instead.')
  both('admin_approval_required',True,[eo],'Creating a public API OAuth app requires workspace owner/admin role; not a blanket requirement for personal API tokens or external hosted MCP connection.')
  ef=e(hu,48,55,'Without Everything AI add-on, Free Forever MCP allows 100 calls per rolling 24 hours per person shared across clients; paid plans have higher quotas.')
  both('free_access',True,[ef],'Hosted MCP Free Forever route without Everything AI add-on, within documented rolling daily limits; not an isolated API sandbox.')
  both('paid_required',False,[ef],'Free Forever MCP quota is available without the Everything AI add-on; additional capacity/features may require payment.')
  em2=e(mu,55,67,'ClickUp documents external AI assistants connecting to its hosted MCP endpoint https://mcp.clickup.com/mcp.')
  mcp('official','ClickUp hosted MCP',[em,em2,ep],mu,'https://mcp.clickup.com/mcp',None,'Callable hosted server lets external AI clients work with ClickUp tasks, time entries and collaboration data; OAuth2.1/PKCE only; public API personal tokens are a different route.')
  finish('Manage permitted ClickUp lists/comments/time entries via public API or task workflows through hosted MCP.',['Public API OAuth app creation requires workspace owner/admin.','Hosted MCP uses OAuth only and has plan/add-on-dependent daily or per-minute limits.'],['Select personal API script, multi-user API OAuth app or hosted MCP route.','Check workspace plan and actor permissions before authorized tests.'],[eo,em,ef])
 if a==78:
  u='https://coda.io/developers/apis/v1'; mu='https://help.coda.io/hc/en-us/articles/44722661982989-Connect-to-the-Coda-MCP?output=1'
  ep=e(u,92,103,'Vendor reference names Superhuman Docs (formerly Coda), a RESTful API for docs, pages/tables/formulas/controls and row mutations; it also points to a Docs MCP server.')
  init('Coda identity matched by vendor API reference: Superhuman Docs (formerly Coda), REST API base remains https://coda.io/apis/v1.','Document platform exposing document discovery, structured tables and row updates through a REST API.',[ep,e(u,120,121,'API base path remains https://coda.io/apis/v1.')])
  ea=e(u,300,316,'API request example uses an Authorization Bearer API token.')
  ea=e(u,289,294,'API request example uses an Authorization Bearer API token to GET Coda folders.')
  auth('api_token','Bearer_token','REST API access token in Authorization: Bearer; user/token permissions apply.',[ea,e(u,176,184,'API use is subject to token-owner workspace role; creating docs requires Doc Maker/Admin or documented promotion settings.')])
  em=e(mu,13,16,'Coda MCP beta enables external AI clients to read/write Coda docs using prompts; behavior and tools may change.')
  em2=e(mu,164,169,'Codex clients generate MCP-restricted personal tokens from Coda account API settings and send Bearer token to https://coda.io/apis/mcp.')
  auth('mcp_pat','Bearer_token','MCP-restricted personal token in Authorization: Bearer; select MCP restriction type when generating.',[em2],sub='Coda hosted MCP token, distinct from general REST API token restrictions.')
  auth('mcp_oauth','OAuth2','Hosted Coda MCP supports OAuth2 for ChatGPT, Claude and Cursor.',[e(mu,27,42,'Supported-client table lists OAuth2 for ChatGPT/Claude/Cursor, personal access tokens for Codex/Antigravity/Copilot.')],sub='Coda hosted MCP; standard REST API OAuth is not established by this evidence.')
  protocol('REST',[e(u,94,103,'Vendor describes a RESTful API for document and data resources.')]);group('docs','Docs and document discovery',[e(u,94,98,'RESTful API lists/searches, creates/copies, shares and publishes docs.')]);group('tables','Tables, rows, formulas and controls',[e(u,99,100,'API discovers pages/tables/formulas/controls and reads/inserts/upserts/updates/deletes rows.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,94,103,'Public API reference describes RESTful doc/data API functionality.')])
  ef=e(u,176,184,'API is available free of charge in both free and paid workspaces, subject to token owner role; doc creation requires Doc Maker/Admin or documented promotion settings.')
  both('free_access',True,[ef],'REST API in free or paid workspace with suitable token-owner role; MCP quotas are separate.')
  both('paid_required',False,[ef],'REST API is free of charge for all users in free and paid workspaces; not an entitlement to unlimited paid-plan MCP.')
  both('self_serve',True,[em2],'Hosted MCP personal-token creation path for existing Coda account; role/quota limits still apply.')
  em3=e(mu,194,198,'MCP role limits differ: paid Doc Makers have full experience; free Doc Makers have 30/week max60/month all tools; Editors have same free-taste quota but read-only tools.')
  mcp('official','Coda hosted MCP beta',[em,em2,em3],mu,'https://coda.io/apis/mcp',None,'Callable hosted beta server lets external AI clients read/write Coda docs; OAuth2 or MCP-restricted personal tokens; role and plan quotas constrain actions, Editors read-only.')
  finish('Discover Coda/Superhuman Docs and modify authorized table rows through REST, or use role-permitted Coda MCP tools.',['API doc creation requires appropriate workspace role; MCP Editor access is read-only.','MCP beta behavior/tools can change and free-taste quotas are limited.'],['Retain Coda/Superhuman Docs identity mapping and select REST or MCP token restriction.','Check Doc Maker/Editor role and MCP quota before authorized tests.'],[ef,em,em3])
 if a==79:
  u='https://developers.smartsheet.com/api/smartsheet/introduction'; au='https://developers.smartsheet.com/api/smartsheet/guides/basics/authentication'; ou='https://developers.smartsheet.com/api/smartsheet/guides/advanced-topics/oauth'; su='https://www.smartsheet.com/content-center/best-practices/tips-tricks/api-getting-started'; mu='https://developers.smartsheet.com/ai-mcp/smartsheet/mcp-server-tools'; hu='https://help.smartsheet.com/articles/2483656-install-smartsheet-connector-claude'
  ep=e(u,65,71,'Smartsheet API manages organization resources including sheets, folders, users, reports and asset paths; requires Business, Enterprise or Advanced Work Management.')
  init('Smartsheet hosted API 2.0 and hosted MCP; regional endpoints/tokens are separate.','Work-management resource platform with APIs for organization sheets, folders, users and reports.',[ep])
  ea=e(au,99,110,'Generate access tokens in Smartsheet UI and pass them in Authorization: Bearer; tokens inherit user access, Gov/Europe tokens separate; OAuth2 is a separate user-consent route.')
  auth('token','Bearer_token','UI-generated access token/API key as Authorization: Bearer; region and user permissions apply.',[ea])
  eo=e(ou,89,100,'OAuth2 enables user-consented resource access; Developer Tools registration requires Smartsheet acceptance and may be denied.')
  auth('oauth','OAuth2','Three-legged OAuth2 for user-consented access; register Developer Tools and app before retrieving user token.',[eo,e(au,104,108,'User-interaction scenarios use three-legged OAuth2, distinct from machine-to-machine raw token access.')])
  protocol('REST',[e(u,76,88,'REST API base is https://api.smartsheet.com/2.0; Gov/EU/Australia use distinct regional base URLs; SDKs provide REST snippets.')]);protocol('SDK',[e(u,82,88,'Smartsheet provides client libraries for JavaScript/Node, Python, Java and C#.')])
  group('sheets','Sheets and cells',[e(u,89,94,'OpenAPI reference documents Sheets, Cells and Folders resource endpoints and objects.')]);group('folders','Folders and organization users',[ep]);group('reports','Reports lifecycle',[e(u,70,71,'Report CRUD endpoints manage the report lifecycle; asset paths locate sheets/reports/dashboards/folders.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,65,75,'Public reference offers object schemas, operation specs, code snippets and a Try-it request editor.')])
  both('paid_required',True,[e(u,65,67,'API requires Business, Enterprise or Advanced Work Management plan.')],'Ordinary tenant API route requires the listed commercial plan; this does not settle cost of a separately requested developer sandbox.')
  both('self_serve',True,[e(au,99,103,'Existing eligible users generate access tokens in the Smartsheet UI.')],'Direct token route for existing eligible account; OAuth Developer Tools activation is separately accepted by vendor.')
  both('vendor_approval_required',True,[eo],'OAuth Developer Tools registration route requires Smartsheet acceptance and can be denied; not a partnership approval and not necessarily direct-token access.')
  elig('testing','sandbox_access',True,[e(su,147,153,'A developer registration path is required for a separate sandbox account and third-party applications; direct access tokens are generated in UI.')],'Requested registered developer sandbox path; no claim of successful provisioning, free cost or automatic entitlement.')
  em=e(mu,31,38,'Official Smartsheet MCP exposes public API through AI clients; Business/Enterprise/Advanced Work Management plan and tool-specific OAuth scopes required; API rate limits apply.')
  em2=e(hu,110,125,'Client setup signs into Smartsheet and selects regional MCP URL: US https://mcp.smartsheet.com, EU and Australia separate.')
  mcp('official','Smartsheet hosted MCP',[em,em2],hu,'https://mcp.smartsheet.com',None,'Callable official hosted server exposes Smartsheet public API tools to external AI clients; US endpoint shown, EU/Australia separate; eligible plan and tool-specific OAuth scopes required.')
  finish('Manage permitted Smartsheet sheets/cells/folders/reports through REST2.0 or hosted MCP.',['Ordinary API and MCP require Business/Enterprise/Advanced Work Management.','OAuth Developer Tools activation requires vendor acceptance.','Regional API endpoints/tokens differ and user sharing permissions still apply.'],['Confirm plan, region and direct-token versus OAuth developer route.','Request sandbox/Developer Tools if needed and conduct authorized tests only after access.'],[ep,ea,eo,em])
 if a==80:
  u='https://help.getharvest.com/api-v2/introduction/overview/general/'; au='https://help.getharvest.com/api-v2/authentication-api/authentication/authentication/'; ix='https://help.getharvest.com/api-v2/'; mu='https://github.com/southleft/harvest-mcp'; pu='https://www.getharvest.com/pricing'
  ep=e(u,11,14,'Harvest time-tracking API v2 is a REST API for tracking time, logging expenses, creating projects and other account operations; requests require OAuth2 or PAT.')
  init('Harvest time-tracking API v2 (help.getharvest.com and api.harvestapp.com), not Greenhouse recruiting Harvest API.','Time-tracking platform with APIs for time, expenses, projects and account workflows.',[ep])
  ea=e(au,14,29,'Harvest ID Developers creates PATs; API v2 bearer requests require account ID and example User-Agent. PAT replaces API-v1 Basic auth.')
  auth('pat','Bearer_token','Harvest ID personal access token in Authorization: Bearer with Harvest-Account-Id; not legacy Basic auth.',[ea])
  eo=e(au,33,66,'Register OAuth2 app in Harvest ID Developers; server-side authorization-code flow yields access/refresh tokens; app selects Harvest/Forecast products.')
  auth('oauth_code','OAuth2','Server-side OAuth2 authorization-code grant for multi-user Harvest integrations.',[eo])
  auth('oauth_implicit','OAuth2','Documented legacy client-side implicit grant; vendor recommends authorization code if a backend exists.',[e(au,90,108,'Harvest documents implicit grant for browser applications, with authorization code recommended when a backend is available.')])
  protocol('REST',[ep]);group('time','Time entries',[e(ix,43,45,'Timesheets API includes Time Entries.')]);group('projects','Projects and task/user assignments',[e(ix,46,51,'Projects API includes Projects, Project User Assignments and Project Task Assignments.')]);group('expenses','Expenses',[e(ix,36,39,'Expenses API includes expenses and expense categories.')]);group('invoices','Invoices and payments',[e(ix,25,30,'Invoices API lists invoices, messages, payments and item categories.')])
  r['api_surface']['public_documentation']=c('api.public_docs',True,[e(u,11,24,'Public API overview describes REST requests, methods and request formatting.')])
  both('self_serve',True,[e(au,17,24,'An existing Harvest ID user creates a personal access token in Developers and receives account IDs.')],'Existing Harvest-user PAT creation route; account product/plan entitlements remain separately unresolved.')
  # Pricing alone does not prove that a free or trial account is API-enabled.
  for env in ['testing','production']:
   for k in ['free_access','trial_access','paid_required']:
    r['credential_eligibility'][env][k]=c(env+'.'+k,None,[e(pu,97,117,'Harvest pricing advertises a free trial and Free plan with one seat/two projects but does not establish API entitlement in this excerpt.')],status='unknown',why='Product pricing documents Free/trial plans, but captured sources do not explicitly match API credential entitlement to those plans. Do not promote product pricing into API-access proof.')
  em=e(mu,155,166,'Southleft community Harvest MCP connects AI assistants to Harvest time tracking and advertises https://harvest-mcp.southleft.com/mcp with Harvest OAuth connection.')
  em2=e(mu,211,224,'Community README lists time-entry read/create/delete and timer-stop MCP tools.')
  mcp('community','Southleft Harvest MCP',[em,em2],mu,'https://harvest-mcp.southleft.com/mcp',mu,'Callable community-maintained server exposes Harvest time-tracking operations to external MCP clients, authenticating with Harvest OAuth; not vendor endorsement or operational verification.')
  finish('Track time and inspect permitted Harvest projects/expenses/invoices through REST v2; community MCP is an optional untested route.',['Account ID and correctly identified application User-Agent are required.','Free/trial API entitlement remains unconfirmed; community MCP maintenance/security/operation not independently assessed.'],['Confirm API credential eligibility for intended Harvest account plan.','Prefer official REST documentation; separately review community implementation before any connection.'],[ea,e(u,25,33,'Each request requires User-Agent with application name and URL/email; absent User-Agent returns400.'),em])
 if a==80:
  r['api_surface']['breadth'].update(value='broad',rationale='Captured groups cross time tracking, projects, expense accounting and invoicing/payment workflows: multiple business domains. Qualitative inference only, not endpoint completeness.')
 return r

out={'records':[build(r) for r in records]}
(ROOT/'work/task-14-agent/extracted-records-001.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
