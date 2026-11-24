"""Explicit Task16 researcher intake, authored after reading pipeline captures.
No keyword classifier, synthetic facts, operational calls, or independent review.
Helpers follow work/task-12-agent/build_extraction.py's claim/evidence pattern.
"""
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
import research_pipeline as p
from make_sources import SCOPES
RUN='task16-capture-007'
D=ROOT/'work/research-runs'/RUN
p.verify_seal(D)
records=copy.deepcopy(p.read_json(D/'records.json'))
captures=p.read_json(D/'captures.json')
for r in records:
 a=r['identity']['id']; scope=SCOPES[a]
 def E(url,first,last,text):
  cs=[c for c in captures if c['spec']['app_id']==a and c['spec']['url']==url]
  assert len(cs)==1,(a,url,len(cs))
  c=cs[0]; lines=(D/c['snapshot_ref']).read_text(encoding='utf-8').splitlines()
  assert 1<=first<=last<=len(lines),(a,url,first,last,len(lines))
  e=p.evidence_for(c,first,lines[first-1]);e.update(locator=f'lines:{first}-{last}',observation='paraphrase: '+text); return e
 def C(k,v,ev=(),status='observed',refs=(),why='Documentary observation; independent AI and actual human reviews pending.'):
  return dict(claim_id=f'{a}.{k}',status=status,value=v,context=scope,evidence=list(ev),supporting_claim_refs=[f'{a}.{x}' for x in refs],rationale=why)
 def A(k,method,detail,ev,sub,scopes=(),status='observed',refs=()):
  r['auth']['items'].append(C('auth.'+k,dict(method=method,context=sub,scopes=list(scopes),details=detail),ev,status,refs))
 def P(k,value,ev):r['api_surface']['protocols']['items'].append(C('api.protocol.'+k,value,ev))
 def G(k,value,ev):r['api_surface']['resource_groups']['items'].append(C('api.group.'+k,value,ev))
 def Q(env,key,val,ev,why):r['credential_eligibility'][env][key]=C(env+'.'+key,val,ev,why=why)
 def B(value,groups,ev,why):r['api_surface']['breadth']=C('api.breadth',value,ev,'inferred',['api.group.'+g for g in groups],why)
 def M(k,name,ev,url,server,sub,repo=None):
  op=C('mcp.'+k+'.operational',None,status='not_researched',why='No MCP connection or authenticated tool call was attempted.')
  r['mcp']['entries'].append(C('mcp.'+k,dict(origin='official',name=name,source_url=url,repository_url=repo,server_url=server,scope=sub,operational_check=op),ev))
  r['mcp']['discovery']=C('mcp.discovery','found',ev,why='Captured vendor documentation establishes a callable server in the declared product scope; no execution implied.')
 def BUILD(verdict,workflow,blockers,steps,ev,refs,why):r['buildability']=C('buildability',dict(verdict=verdict,scope=workflow,blockers=blockers,next_steps=steps),ev,'inferred',refs,why)
 def ID(text,ev,purpose=None):
  r['identity']['resolution']=C('identity',text,ev)
  r['purpose']=C('purpose',purpose or text,ev)
 def DOC(ev):r['api_surface']['public_documentation']=C('api.public_docs',True,ev)
 for env in ('testing','production'):
  r['credential_eligibility'][env]['context']=scope
  for k,v in r['credential_eligibility'][env].items():
   if k!='context':r['credential_eligibility'][env][k]=C(env+'.'+k,None,status='unknown',why=f'Checked captured sources do not explicitly resolve {env}.{k} for the declared interface/path. Unknown is not a negative result.')
 r['auth'].update(coverage_status='partial',items=[],notes='Only captured methods and interface scopes are asserted; no operational authentication was attempted.')
 for k in ('protocols','resource_groups'):
  r['api_surface'][k].update(coverage_status='partial',items=[],notes='Bounded primary-source reading; captured examples only, not an exhaustive endpoint inventory.')
 if a==91:
  n='https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks'
  l='https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing'
  s='https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources'
  ident=E(n,137,172,'Gemini Notebook Enterprise generates document insights and summaries; notebook management REST methods require an authenticated user with an active Enterprise license and Cloud NotebookLM User IAM role.')
  rename=E(l,140,144,'NotebookLM Enterprise has been renamed Gemini Notebook Enterprise; subscription name remains NotebookLM Enterprise.')
  auth=E(n,156,172,'Sign in using gcloud auth login as a licensed user with roles/discoveryengine.notebookLmUser; gcloud auth print-access-token returns the user access token.')
  rest=E(n,195,206,'REST POST notebook create uses Authorization:Bearer with gcloud auth print-access-token at the discoveryengine.googleapis.com v1alpha projects/locations/notebooks resource.')
  lic=E(l,160,183,'Subscriptions have at least 15 licenses; free-trial tier is full-featured for 14 days with 5,000 licenses; paid tier is monthly/yearly. Setup requires NotebookLM User role and administrators holding NotebookLM Admin and Gemini Enterprise Admin roles.')
  signup=E(l,184,212,'An authorized administrator adds a subscription in Google Cloud console, selecting region, license count, term and tier. Paid subscriptions bill the project Cloud Billing account.')
  sources=E(s,148,163,'Notebook sources include Google Docs, Slides, raw text, web content and YouTube videos; sources can be batch-added, uploaded, retrieved and deleted. Docs/Slides imports require Google Drive authorization with user credentials.')
  ID('NotebookLM Enterprise, now Gemini Notebook Enterprise on Google Cloud; Enterprise REST API scope, distinct from personal Gemini Notebook API.',[ident,rename], 'Generate document-grounded insights and summaries with programmatic notebook and source management in Gemini Notebook Enterprise.')
  A('licensed_user','Bearer_token','User access token obtained through Google Cloud CLI user login; Authorization:Bearer header. Requires active Enterprise license and Cloud NotebookLM User IAM role.',[auth,rest],'Enterprise v1alpha projects.locations.notebooks; licensed user identity, not personal notebook.googleapis.com API')
  for env in ('testing','production'):
   Q(env,'admin_approval_required',True,[auth,lic],'Enterprise setup/licensing path requires administrator roles and granting the user IAM role; this is customer tenant administration, not vendor approval.')
   Q(env,'self_serve',True,[signup,lic],'Authorized customer administrator can add trial/paid subscriptions in Google Cloud console; self-serve is for that administrator and does not remove IAM/license prerequisites.')
  Q('testing','trial_access',True,[lic,auth],'Full-featured 14-day Enterprise trial supplies licenses; the notebook API requires an active licensed user. No API request was tested.')
  Q('testing','free_access',True,[lic,auth],'Time-limited free-trial tier for Enterprise licenses; not an ongoing free production tier.')
  Q('testing','paid_required',False,[lic],'The documented free-trial subscription is an alternative to a paid subscription for evaluation.')
  Q('production','paid_required',True,[lic,signup],'Continued Enterprise use after the 14-day trial requires the paid subscription tier; API remains Preview/Pre-GA, not a production-readiness certification.')
  P('rest','REST',[rest]);DOC([ident,rest])
  G('notebooks','Notebook create, retrieve, recently viewed list, delete and share',[E(n,148,155,'The API lists create, retrieve, list recently viewed, delete and share notebook management operations.')])
  G('sources','Notebook source batch addition, file upload, retrieval and deletion',[sources])
  B('moderate',['notebooks','sources'],[ident,sources],'Two closely related resource groups: notebook lifecycle/sharing and content-source management. No exhaustive endpoint count or general consumer API claim.')
  r['mcp']['discovery']=C('mcp.discovery',None,[ident,sources],'not_found_in_checked_sources',why='Bounded check of captured Enterprise notebook/source API and licensing docs did not establish an Enterprise callable MCP server. Personal API MCP references are edition-separated and do not establish Enterprise MCP.')
  r['auth']['notes']='Enterprise scope preserved separately from earlier five-app pilot app91. Captured developers.google.com/notebook/docs/authentication lines 51-54 explicitly restrict its distinct Public Preview to personal Google Accounts; its scopes/endpoints/MCP are excluded here.'
  BUILD('conditional','Create/manage Enterprise notebooks and sources with licensed user REST credentials',['Active Enterprise license and Cloud NotebookLM User IAM role are required.','API is Preview/Pre-GA with limited-support caveats.','Google Docs/Slides source imports need extra Google Drive authorization.'],['Have the customer administrator set up trial or paid licensing and IAM.','Confirm region, preview terms and intended deployment suitability before implementing the REST wrapper.'],[ident,lic,rest,sources,E(n,140,147,'The feature is Preview, subject to Pre-GA terms and available as-is with potentially limited support.')],['identity','auth.licensed_user','testing.trial_access','production.paid_required','api.protocol.rest','api.breadth'],'Documented REST makes a wrapper feasible, conditioned on licensed-user IAM, regional setup and Pre-GA acceptance. No consumer API or service-account capability is imported.')
 elif a==92:
  m='https://help.otter.ai/hc/en-us/articles/35287607569687-Otter-MCP-Server'
  j='https://help.otter.ai/api/v2/help_center/en-us/articles/36130822688279.json'
  gate='https://help.otter.ai/hc/en-us/articles/4412365535895-Does-Otter-offer-an-open-API'
  base=E(m,26,39,'Otter MCP lets AI assistants search meeting transcripts and analyze meeting data; access uses OAuth and authorized meetings only.')
  oauth=E(m,79,93,'Cursor custom MCP configuration points to https://mcp.otter.ai/mcp and prompts the user to sign in to Otter and authorize access.')
  tools=E(m,130,146,'Tools overview documents Get user info for name/email, Search for meetings, and Fetch for a full meeting/conversation speech transcript; conversations must be shared with the user.')
  # Vendor JSON response is one immutable normalized line. The observation identifies the exact JSON field and HTML section; no fabricated line splitting.
  api=E(j,1,1,'article.body introductory paragraph and #authentication section: Otter Public API retrieves channels, conversations, transcripts, audio, action items, insights, outlines and workspace details; Enterprise users create an API key at Integrations -> Developer and send Authorization: Bearer YOUR_API_KEY.')
  apigate=E(gate,20,21,'Public API is for Enterprise customers; contact the Otter account manager to enable access.')
  ID('Otter AI meeting knowledge platform with OAuth callable MCP and a separately Enterprise-scoped public API.',[base,api],'Search, retrieve and analyze Otter meeting conversations and transcripts from external applications or AI assistants.')
  A('mcp_oauth','OAuth2','OAuth-authenticated user authorization for Otter callable MCP; accessible meetings are those authorized/shared with the user.',[base,oauth],'Otter callable MCP server')
  A('enterprise_api_key','API_key','User-created API key in Integrations -> Developer, sent as Authorization: Bearer YOUR_API_KEY; Enterprise Public API.',[api],'Enterprise Public API; distinct from MCP OAuth')
  for env in ('testing','production'):
   Q(env,'self_serve',True,[oauth],'MCP path only: existing Otter user connects the documented server and authorizes in browser. Enterprise API activation is a separate account-manager path, not covered by this self-serve finding.')
  P('rest','REST',[E(j,1,1,'article.body #endpoints / #channels: curl GET https://api.otter.ai/v1/channels with Bearer API key; resource-oriented HTTP endpoints are published.')]); P('mcp','other',[oauth]);DOC([api,tools])
  G('meeting_content','Enterprise API meeting conversations, transcripts, audio, action items, insights and outlines',[api])
  G('channels_workspace','Enterprise API channels and workspace details',[api])
  G('mcp_profile','MCP Get user info, meeting Search and transcript Fetch tools',[tools])
  B('moderate',['meeting_content','channels_workspace','mcp_profile'],[api,tools],'Multiple related meeting-content, organization and profile resource groups; not broad unrelated business domains.')
  M('otter','Otter MCP Server',[base,oauth,tools],m,'https://mcp.otter.ai/mcp','Official callable server exposing authorized Otter meeting search/transcript fetch and profile tools; OAuth required.')
  r['auth']['notes']='MCP FAQ lines182-183 says no public API key for MCP setup; separate Enterprise API article documents keys. These scopes must not be conflated. MCP plan eligibility and Enterprise commercial costs remain unknown from captured passages.'
  BUILD('conditional','Connect an existing authorized Otter user to meeting-search/transcript-fetch MCP; Enterprise API is a separate optional route',['MCP requires Otter account OAuth authorization and meetings shared with that user.','Captured MCP setup docs do not settle plan eligibility.','Enterprise API requires account-manager enablement; this is not an API-key alternative for MCP authentication.'],['Confirm MCP account/plan entitlement and authorize the user.','If using Enterprise REST instead, ask the account manager to enable access and create an API key.'],[base,oauth,apigate,api],['identity','auth.mcp_oauth','api.protocol.mcp','mcp.discovery'],'A callable MCP path is documented, while plan entitlement remains unresolved; public Enterprise REST activation is separately gated. No paid plan is inferred from the Enterprise name alone.')
 elif a==93:
  q='https://developers.fathom.ai/quickstart.md'; h='https://help.fathom.video/en/articles/8368641'; o='https://developers.fathom.ai/sdks/oauth.md'; reg='https://developers.fathom.ai/oauth.md'; idx='https://developers.fathom.ai/llms.txt'; m='https://developers.fathom.ai/mcp-docs/index.md'
  ident=E(h,19,31,'Fathom public API provides meeting summaries, transcripts and action items; API keys are user-level and cannot access others unshared meetings.')
  key=E(q,6,19,'Create an API key in User Settings API Access; it is user-scoped and passed as X-Api-Key to https://api.fathom.ai/external/v1/meetings. Even admin keys do not grant private meeting access.')
  oa=E(o,6,37,'Fathom supports OAuth2 for multi-account integrations; register an app first, request public_api scope, redirect user to authorize, then exchange authorization code for tokens.')
  mc=E(m,6,19,'Fathom offers its official callable MCP server connecting meeting data to AI assistants; server URL https://api.fathom.ai/mcp requires authentication.')
  ID('Fathom video meeting assistant (fathom.video linked developer API at developers.fathom.ai), not similarly named Fathom products.',[ident,key],'Access Fathom meeting summaries, transcripts and action items for custom integrations and AI assistants.')
  A('api_key','API_key','User-generated X-Api-Key header for meetings recorded by or shared with the user/Team; admin keys never unlock private meetings.',[key],'Fathom external/v1 API, internal user integrations')
  A('oauth','OAuth2','Registered app uses authorization-code OAuth2 and public_api scope for multi-user integrations.',[oa],'Fathom public apps installed by multiple accounts',['public_api'])
  for env in ('testing','production'):Q(env,'self_serve',True,[key],'Internal user API-key path: generate a key in API Access under User Settings; this does not assert unrestricted public OAuth app launch, free usage or plan eligibility.')
  # Public OAuth review is deliberately not projected onto the internal API-key path.
  P('rest','REST',[key]);P('sdk','SDK',[E('https://developers.fathom.ai/',39,45,'Developer introduction offers TypeScript and Python SDKs and installable OAuth integrations.')]);DOC([ident,key])
  meetings=E(idx,8,13,'Official API index lists meeting listing/types, summary/transcript retrieval and asynchronous recording-download requests/status.')
  org=E(idx,14,19,'Official API index lists teams, team members, users/permissions, and create/delete webhooks/new meeting content payloads.')
  G('meeting_recordings','Meetings and meeting types, recording summaries/transcripts and downloadable recording exports',[meetings])
  G('teams_webhooks','Teams, team members, users/permissions and meeting webhooks',[org])
  B('moderate',['meeting_recordings','teams_webhooks'],[meetings,org],'Multiple related meeting-data, organization and delivery-webhook resource groups; bounded to published index descriptions.')
  M('fathom','Fathom MCP Server',[mc],m,'https://api.fathom.ai/mcp','Official callable server giving authenticated AI clients access to Fathom meeting data.')
  r['auth']['notes']='Official fathom.video help page links to developers.fathom.ai; fathom.one is excluded. Public OAuth apps are subject to vendor review (oauth.md lines7-8), whereas the selected eligibility path is internal user-generated API keys. OAuth approval timing and plan costs remain unresolved.'
  review=E(reg,7,8,'Public OAuth apps should use OAuth and are subject to review for user experience; marketplace promotion is a separate possibility.')
  BUILD('conditional','Read authorized Fathom meeting data using a user API key or callable MCP; multi-user OAuth is a separate launch scope',['API keys inherit user/team sharing and never grant private-meeting access.','Plan/free-use eligibility was not established in captured sources.','Public OAuth apps are subject to review; this does not automatically gate an internal API-key workflow.'],['Confirm plan entitlements, then generate a user API key or authorize MCP.','For a distributable OAuth app, register it and confirm the vendor review requirements.'],[ident,key,mc,review],['identity','auth.api_key','testing.self_serve','api.protocol.rest','mcp.discovery'],'Interfaces and self-service user keys are documented, but usage entitlement and public-app review remain conditions; do not overstate build_now from public docs alone.')
 elif a==94:
  q='https://docs.consensus.app/api-get-started.md';l='https://docs.consensus.app/api-plans-and-access.md';m='https://docs.consensus.app/consensus-mcp.md';conn='https://docs.consensus.app/enterprise/connection-reference.md'
  ident=E(q,4,14,'Consensus REST API searches scholarly research papers; every plan includes API access with 30 monthly calls on Free; user creates a key in the API & MCP Dashboard.')
  key=E(q,171,179,'REST base URL is https://api.consensus.app and every request includes the API key in x-api-key.')
  plans=E(l,6,29,'API is self-serve on every Consensus plan; Free has 30 calls/month, max 20 papers/request and no pagination, full text or citation/reference beta access; paid plans add these features.')
  oauth=E(conn,32,46,'MCP supports OAuth2 authorization-code flow, per-user consent, default search scope, mandatory PKCE S256 and dynamic registration of public clients. Confidential enterprise client credentials require manual provisioning/contact sales.')
  mc=E(conn,7,14,'Consensus callable MCP endpoint https://mcp.consensus.app/mcp uses Streamable HTTP and provides search, signed-in Thread tools and paid full-text retrieval.')
  mk=E(conn,19,29,'MCP gateway API keys are sent as Authorization: Bearer; the account dashboard generates the opaque key.')
  ID('Consensus (consensus.app), scholarly research engine with REST API and official callable MCP.',[ident,E(m,4,12,'Consensus hosts a scholarly research MCP server at https://mcp.consensus.app/mcp.')],'Search scholarly papers and retrieve research content through the Consensus API or MCP.')
  A('rest_key','API_key','REST requests use x-api-key from the self-serve API & MCP Dashboard.',[ident,key],'Consensus REST /v1 API')
  A('mcp_oauth','OAuth2','MCP authorization-code user consent with PKCE S256; dynamic registration for public clients; confidential enterprise clients are provisioned manually.',[oauth],'Consensus MCP per-user authorization',['search'])
  A('mcp_key','API_key','MCP gateway sends an API key as Authorization: Bearer; enterprise-gateway instructions describe account dashboard creation.',[mk],'Consensus MCP API-key gateway route; distinct from REST x-api-key')
  for env in ('testing','production'):
   Q(env,'free_access',True,[plans],'Basic REST search on the recurring Free plan: 30 calls/month and max 20 results/request, without paid features.')
   Q(env,'paid_required',False,[plans],'Basic first-page REST search has a Free allowance; paid-only full-text, pagination and beta citation/reference endpoints are excluded from this finding.')
   Q(env,'self_serve',True,[plans,ident],'Ordinary REST API key path is explicitly self-serve on every plan. Manual confidential enterprise OAuth provisioning is a separate path.')
  P('rest','REST',[ident,key]);P('mcp','other',[mc]);DOC([ident,plans])
  G('search','Ranked scholarly paper search via REST search endpoint',[E(q,4,6,'Consensus REST search returns ranked papers with titles, authors, journals, publication years, citation counts and links.')])
  G('full_text','Paid open-access paper full text',[E(q,166,170,'Paid searches provide full-text excerpts, and GET /v1/papers/full_text returns complete open-access paper text as Markdown.')])
  G('threads','Asynchronous research-agent Threads',[E(l,30,35,'Threads are charged by research work; API/MCP calls share a monthly allowance.') ,mc])
  G('citations','Paid beta citation and reference traversal',[E(l,24,28,'GET /v1beta/papers/citations and /v1beta/papers/references are paid beta endpoints billed per 100 returned papers; schemas may change.')])
  B('moderate',['search','full_text','threads','citations'],[plans,mc],'Related scholarly research workflows: paper retrieval, full-text reading, citation graph traversal and research conversations.')
  M('consensus','Consensus MCP',[mc,E(m,4,12,'Consensus publishes its hosted scholarly research MCP server endpoint.')],conn,'https://mcp.consensus.app/mcp','Official callable scholarly-search and research-thread server; OAuth or API-key authentication.')
  r['auth']['notes']='Original OAuth-requested hint is not an observed credential gate. REST uses self-serve API keys; per-user MCP OAuth uses DCR/PKCE; manual confidential enterprise clients alone require sales. Rate limits differ between api-plans-and-access.md and enterprise/connection-reference.md; no global rate-limit claim asserted.'
  BUILD('build_now','Basic first-page scholarly paper search using a self-serve Free REST key',['Free allowance is 30 calls/month and 20 papers/request; pagination/full-text/citation beta features require paid plans.'],['Generate an API key in API & MCP Dashboard.','Implement bounded REST search; confirm paid or enterprise conditions before expanding scope.'],[ident,key,plans],['identity','auth.rest_key','testing.free_access','testing.self_serve','api.protocol.rest','api.group.search'],'Published REST authentication and explicit recurring Free/self-serve access make the narrow search wrapper feasible now. This is a documentary feasibility inference, not a tested integration.')
 elif a==95:
  q='https://docs.reducto.ai/quickstart/index.md'; st='https://docs.reducto.ai/studio-account/index.md'; cr='https://docs.reducto.ai/reference/credit-usage/index.md'; ag='https://docs.reducto.ai/agent-guide/index.md'; mc='https://docs.reducto.ai/mcp-server/index.md'; ref='https://docs.reducto.ai/reference/llms.txt'
  ident=E(q,1,17,'Reducto parses documents via API; users sign up for a free account at studio.reducto.ai and create REDUCTO_API_KEY under API Keys.')
  bearer=E(q,201,202,'REST POST https://platform.reducto.ai/parse authenticates with Authorization: Bearer $REDUCTO_API_KEY.')
  roles=E(st,13,21,'All roles in Reducto Studio can create API keys; only Owners and Admins can edit or delete keys.')
  billing=E(cr,11,43,'Standard list pricing bills per 1,000 pages across Parse (r-1 $10, r-1 mini $1), Extract ($20), Deep Extract ($40), Split ($20), Deep Split ($40), Classify ($7.50), Deep Classify ($15), and Edit ($60).')
  sub=E(st,48,56,'Studio Billing page manages payment methods and monthly/yearly Stripe subscriptions.')
  sdks=E(q,31,43,'Official Reducto SDKs are available for Python (reductoai), Node.js (reductoai), and Go (github.com/reductoai/reducto-go-sdk).')
  routes=E(ag,11,35,'Reducto exposes CLI (reducto parse), MCP server, Python/Node.js SDKs, and REST endpoints (/parse, /extract, /split, /classify, /edit, /upload, async variants, and GET /job/{job_id}) across 30+ document formats.')
  usage=E(cr,53,57,'Usage is monitored in Reducto Studio and exported programmatically via the Usage Export API.')
  mhost=E(mc,53,69,'Official hosted Reducto MCP server runs at https://mcp.reducto.ai/mcp using Streamable HTTP and Authorization: Bearer API key; hosted server accepts public URLs only.')
  mloc=E(mc,70,93,'Official local Reducto MCP server runs via uvx mcp-server-reducto with local filesystem upload support and OAuth device-code browser login (uvx mcp-server-reducto --login) saving the API key to ~/.reducto/config.yaml.')
  mcap=E(mc,8,10,'Reducto MCP server connects AI agents to classify, parse, extract, split, and edit documents.')
  ID('Reducto (reducto.ai), document processing API and platform for parsing, extracting, splitting, classifying, and editing complex documents.',[ident,routes],'Parse, extract, split, classify, and edit PDFs, spreadsheets, images, and office documents via REST, SDKs, CLI, or MCP.')
  A('api_key','API_key','Studio API key (REDUCTO_API_KEY) sent as Authorization: Bearer to https://platform.reducto.ai and hosted MCP https://mcp.reducto.ai/mcp; all org roles can create keys while only Owners/Admins can edit or delete keys.',[ident,bearer,roles,mhost],'Reducto REST API, SDKs, and hosted MCP server')
  A('local_mcp_oauth_device','OAuth2','OAuth device-code browser login via uvx mcp-server-reducto --login, storing the resulting API key in ~/.reducto/config.yaml shared with the Reducto CLI.',[mloc],'Local Reducto MCP server and CLI login flow')
  for env in ('testing','production'):
   Q(env,'self_serve',True,[ident,roles],'Self-serve account signup and API key creation in Reducto Studio (studio.reducto.ai).')
   Q(env,'admin_approval_required',False,[roles],'Studio Account docs explicitly state all roles can create API keys (only editing/deleting keys is restricted to Owners and Admins).')
  Q('production','paid_required',True,[billing,sub],'Per-page list pricing applies across all Reducto endpoints with Stripe subscription/payment management in Studio Billing.')
  P('rest','REST',[bearer,routes]);P('sdk','SDK',[sdks]);P('cli','CLI',[routes]);P('mcp','other',[mhost,mloc]);DOC([ident,routes])
  G('parse_upload','Document upload (/upload, up to 100MB direct or 5GB presigned) and layout-aware parsing (/parse, /parse_async)',[routes])
  G('extract_split_classify_edit','Structured extraction (/extract), document splitting (/split), classification (/classify), form editing (/edit), and async job polling (/job/{job_id})',[routes])
  G('usage_export','Programmatic usage export (Usage Export API) and per-product billing metrics',[usage,E(ref,16,16,'Reference index lists Usage Export API to programmatically export usage data.')])
  B('moderate',['parse_upload','extract_split_classify_edit','usage_export'],[routes,usage],'Multiple related document-processing and usage-reporting resource groups within one document-AI domain.')
  M('reducto_hosted','Reducto MCP Server (Hosted & Local)',[mcap,mhost,mloc],mc,'https://mcp.reducto.ai/mcp','Official callable hosted Streamable HTTP server (public URLs, Bearer API key) and companion local uvx mcp-server-reducto server (local files, OAuth device-code login) for classify, parse, extract, split, and edit.')
  r['auth']['notes']='Free account signup is documented in quickstart/index.md line 12, but captured pricing docs (credit-usage/index.md) do not specify a free page/credit allowance, so testing.free_access and testing.paid_required remain unknown.'
  BUILD('build_now','Parse and extract documents via self-serve Reducto REST/SDK API or official MCP server',['Per-page list pricing applies ($1-$60 per 1,000 pages depending on product/model); free starter quota is not established in captured sources.','Hosted MCP only accepts public URLs; local files require local uvx mcp-server-reducto or REST /upload.'],['Sign up at studio.reducto.ai and generate REDUCTO_API_KEY.','Confirm billing/credit allowance and call POST https://platform.reducto.ai/parse or connect https://mcp.reducto.ai/mcp.'],[ident,bearer,routes,billing,mhost],['identity','auth.api_key','testing.self_serve','api.protocol.rest','api.breadth','mcp.discovery'],'Self-serve API key creation, REST/SDK/CLI interfaces, and official callable MCP server are documented; documentary feasibility only, not an operational test.')
 elif a==96:
  au='https://docs.devin.ai/api-reference/authentication.md'; v3='https://docs.devin.ai/api-reference/v3/overview.md'; tm='https://docs.devin.ai/api-reference/getting-started/teams-quickstart.md'; mc='https://docs.devin.ai/work-with-devin/devin-mcp.md'; api='https://docs.devin.ai/_llms/en/api.txt'
  ident=E(au,4,16,'Devin API uses a principal + token model with cog_-prefixed credentials sent as Authorization: Bearer to https://api.devin.ai/v3/organizations/{org_id}/sessions.')
  svc=E(au,31,60,'Service users are non-human accounts provisioned in Settings > Devin API (org) or Enterprise settings > Devin API (enterprise), assigned RBAC roles and expiration, using cog_ API keys.')
  pat=E(au,63,68,'Personal Access Tokens (PATs, cog_ prefix) authenticate as the human user across all accessible orgs; on Enterprise accounts, PATs are disabled by default and governed by an enterprise admin policy with approval workflow and mandatory expiration.')
  leg=E(au,70,78,'Legacy v1/v2 API keys (apk_ and apk_user_) are deprecated and lack v3 RBAC/pagination.')
  tm_setup=E(tm,10,36,'Teams quick start provisions a service user in Settings > Devin API with Admin or Member role and copies the cog_ API key for Authorization: Bearer.')
  tm_roles=E(tm,68,73,'Teams permission model restricts managing organization settings to Admin; Member can create sessions and manage knowledge/playbooks/secrets.')
  v3_urls=E(v3,6,20,'Devin v3 REST base URLs are https://api.devin.ai/v3/organizations/* and https://api.devin.ai/v3/enterprise/* (or dedicated Enterprise custom domain); every endpoint except GET /v3/self is permission-gated.')
  v3_ent=E(v3,21,46,'Enterprise permissions cover organizations, roles, users, IdP groups, service users, knowledge, playbooks, Git integrations/permissions, billing ACU limits, audit logs, consumption, usage metrics, hypervisors, security profiles, sessions, and code scans.')
  v3_org=E(v3,47,66,'Organization permissions cover secrets, org settings, security profiles, knowledge, playbooks, service users, schedules, automations, consumption, sessions, impersonation, and code scans.')
  api_idx=E(api,15,34,'Official English API index lists organization and enterprise session lifecycle endpoints (list, create, get, messages, attachments, terminate, archive, tags, insights).')
  api_snap=E(api,88,119,'Official English API index lists repository indexing and organization/enterprise snapshot setup blueprints and builds.')
  mcp_ov=E(mc,4,19,'Official Devin MCP server (https://mcp.devin.ai/) exposes public/private repo DeepWiki docs plus session management, playbooks, knowledge, and scheduling; requires a Devin account and API key.')
  mcp_auth=E(mc,20,47,'Devin MCP supports org-scoped cog_ service keys (auto org resolution), enterprise cog_ keys and PATs (requiring X-Org-Id header); legacy apk_/apk_user_ keys only work on repo wiki tools and are rejected by session/platform tools.')
  mcp_wire=E(mc,85,118,'Devin MCP exposes integration/MCP management tools (devin_mcp_server_manage), automations, Devin Review, code scans, and user utilities over Streamable HTTP at https://mcp.devin.ai/mcp (legacy /sse deprecated); distinct from free public-repo-only DeepWiki MCP (https://mcp.deepwiki.com/).')
  ID('Devin (devin.ai / docs.devin.ai), autonomous AI software engineering platform with v3 REST API and official callable Devin MCP server.',[ident,mcp_ov],'Programmatically create and manage Devin engineering sessions, knowledge, playbooks, schedules, automations, code scans, and repository wikis.')
  A('service_user_key','API_key','Non-human Service User API key (cog_ prefix) sent as Authorization: Bearer; org-scoped or enterprise-scoped with RBAC roles; enterprise keys need X-Org-Id on MCP.',[svc,tm_setup,mcp_auth],'Devin v3 REST API and Devin MCP server (recommended for automation)')
  A('personal_access_token','Bearer_token','Human Personal Access Token (cog_ prefix) sent as Authorization: Bearer; inherits user permissions across orgs; disabled by default on Enterprise pending enterprise admin policy; needs X-Org-Id on MCP.',[pat,mcp_auth],'Devin v3 REST API and Devin MCP server (human identity)')
  A('legacy_api_key','API_key','Deprecated v1/v2 API keys (apk_ / apk_user_); on Devin MCP, restricted to repository wiki tools only and rejected by session/platform tools.',[leg,mcp_auth],'Legacy Devin v1/v2 REST API and limited Devin MCP wiki tools')
  for env in ('testing','production'):
   Q(env,'admin_approval_required',True,[tm_roles,pat,v3_org],'Provisioning service users requires ManageOrgServiceUsers / Admin settings access in Teams or Enterprise, and Enterprise PATs are disabled by default under an enterprise admin approval policy.')
   Q(env,'self_serve',True,[tm_setup,mcp_ov],'An authorized Teams/Enterprise organization admin can self-provision service user keys in Settings > Devin API without vendor intervention; plan/account purchase prerequisites remain unverified.')
  P('rest','REST',[v3_urls,api_idx]);P('mcp','other',[mcp_wire]);DOC([v3_urls,api_idx])
  G('sessions','Organization and Enterprise Devin sessions (create, list, messages, attachments, terminate, archive, tags, insights)',[api_idx,v3_org])
  G('knowledge_playbooks_secrets','Knowledge notes/folders, playbooks (moving to Skills), and organization secrets',[v3_ent,v3_org])
  G('automations_schedules_scans','Scheduled sessions, automations, Devin Review, code scans, repository indexing, and snapshot blueprints/builds',[api_snap,v3_org,mcp_wire])
  G('enterprise_governance','Enterprise orgs, membership/IdP groups, Git integrations/permissions, ACU billing limits, consumption, usage metrics, audit logs, and security profiles',[v3_ent])
  B('broad',['sessions','knowledge_playbooks_secrets','automations_schedules_scans','enterprise_governance'],[v3_ent,v3_org,api_idx,api_snap],'Spans multiple distinct domains: autonomous engineering sessions, knowledge/playbooks, code scanning/CI snapshots, and enterprise IAM/audit/billing governance.')
  M('devin','Devin MCP Server',[mcp_ov,mcp_auth,mcp_wire],mc,'https://mcp.devin.ai/mcp','Official callable Streamable HTTP MCP server exposing DeepWiki repo docs, sessions, playbooks, knowledge, schedules, automations, reviews, and code scans; distinct from Devin outgoing MCP client/marketplace management (devin_mcp_server_manage) and free public-only DeepWiki MCP (https://mcp.deepwiki.com/).')
  r['auth']['notes']='Pricing/free-tier eligibility for Devin accounts was not captured (devin-mcp.md line 118 states Requires Devin account vs Free DeepWiki MCP), so free_access, trial_access, and paid_required remain unknown.'
  BUILD('conditional','Manage Devin sessions, knowledge, automations, and repo wikis via v3 REST API or callable Devin MCP server',['Requires an active Devin Teams or Enterprise account (pricing/free-tier terms not established in captured sources).','Service user provisioning requires org/enterprise Admin permissions, and Enterprise PATs are disabled by default pending admin policy.','Enterprise keys and PATs must supply X-Org-Id when calling Devin MCP; legacy apk_ keys cannot run session/platform tools.'],['Provision a Member- or Admin-role cog_ service user key in Settings > Devin API.','Call https://api.devin.ai/v3/organizations/{org_id}/* or connect https://mcp.devin.ai/mcp with Authorization: Bearer.'],[ident,svc,tm_roles,pat,v3_urls,mcp_wire],['identity','auth.service_user_key','testing.admin_approval_required','api.protocol.rest','api.breadth','mcp.discovery'],'Comprehensive v3 REST and callable MCP docs make integration feasible, conditioned on account entitlement and org-admin credential provisioning. Documentary inference only.')
 elif a==97:
  cli='https://higgsfield.ai/blog/higgsfield-cli'; api='https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api'; ent='https://higgsfield.ai/enterprise-help-center/platform/integrations'
  ident=E(cli,32,38,'Higgsfield is an AI-native creative suite for video and image generation with an open-source CLI (higgsfield/higgs) that signs in via browser and charges plan credits.')
  cmp=E(cli,78,109,'Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.')
  cli_req=E(cli,110,124,'Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.')
  cli_auth=E(cli,127,135,'higgsfield auth login opens a browser consent page (email, profile, org membership) and stores a short-lived local access token; higgsfield auth token prints it and no API key is used.')
  cli_cov=E(cli,40,58,'CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.')
  api_ov=E(api,32,59,'Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.')
  api_bill=E(api,60,66,'API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.')
  api_org=E(api,97,100,'API accounts start as personal organizations and can create team organizations; API keys appear only once at creation and unlock 20 concurrent requests.')
  mcp_ent=E(ent,44,55,'Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.')
  ID('Higgsfield (higgsfield.ai), AI-native video/image creative suite with separately billed REST/SDK API (open.higgsfield.ai / api.higgsfield.ai) and subscription-credit CLI + MCP.',[ident,cmp,api_ov],'Generate AI video, images, Soul characters, and creative workflows via Higgsfield REST/SDK API, open-source CLI, or hosted MCP.')
  A('api_key','API_key','API key generated in Open Higgsfield console (open.higgsfield.ai) for calling api.higgsfield.ai via REST or Python/TypeScript SDK; billed from prepaid USD balance ($5 min top-up), independent of web subscription.',[api_ov,api_bill,api_org],'Higgsfield API (api.higgsfield.ai), separate from CLI/MCP')
  A('cli_browser_oauth','OAuth2','Browser device-authorization consent (higgsfield auth login) storing a short-lived local access token; no API key; consumes paid higgsfield.ai plan credits.',[cli_auth,cli_req],'Higgsfield CLI (@higgsfield/cli)')
  A('mcp_browser_signin','OAuth2','Browser account sign-in when connecting https://mcp.higgsfield.ai/mcp from Claude or ChatGPT; no API key; consumes paid plan/workspace credits.',[cmp,mcp_ent],'Higgsfield hosted MCP server (https://mcp.higgsfield.ai/mcp)')
  for env in ('testing','production'):
   Q(env,'free_access',False,[cli_req,api_bill],'Web free/Unlimited generations explicitly do not apply to CLI or MCP (paid subscription required), and the separate Higgsfield API requires funding a prepaid USD balance ($5 minimum top-up).')
   Q(env,'paid_required',True,[cli_req,api_bill],'CLI/MCP require a paid Higgsfield subscription with plan credits; Higgsfield API requires a funded prepaid USD balance ($5 minimum top-up).')
   Q(env,'self_serve',True,[api_ov,cli_auth,mcp_ent],'Individuals or companies can self-serve API signup/funding/key creation at open.higgsfield.ai, or install CLI and authenticate via browser / connect MCP.')
  P('rest','REST',[api_ov,api_bill]);P('sdk','SDK',[api_ov]);P('cli','CLI',[ident,cli_req,cli_cov]);P('mcp','other',[mcp_ent]);DOC([api_ov,cli_cov])
  G('media_generation','Asynchronous video, image, 3D, and audio/voiceover generation across 50+ API catalog / 35+ CLI models plus cost estimation',[api_ov,api_bill,cli_cov])
  G('soul_characters_workflows','Soul ID character training/reuse and media workflows (reframe, dubbing, voice change, draw-to-video, upscaling, background removal, Ad Multiplier)',[cli_cov,mcp_ent])
  G('account_workspace_assets','Account balance, transactions, personal/team billing workspaces, and generated Assets (7+ day retention on API)',[cli_cov,api_bill,api_org])
  B('moderate',['media_generation','soul_characters_workflows','account_workspace_assets'],[api_ov,cli_cov,mcp_ent],'Multiple related media-generation, character/workflow, and workspace-billing resource groups.')
  M('higgsfield','Higgsfield MCP Server',[cmp,mcp_ent],ent,'https://mcp.higgsfield.ai/mcp','Official hosted callable MCP server exposing image/video generation, upscaling, background removal, Soul characters, voiceover/dubbing, Ad Multiplier, and credit balance checks via browser account sign-in using plan/workspace credits.')
  r['auth']['notes']='Billing paths are strictly separated: API (open.higgsfield.ai, USD prepaid $5+ balance, API key) vs CLI/MCP (higgsfield.ai paid subscription credits, browser login, no API key). Enterprise voice-clone limit increases require contacting an account manager (platform/integrations line 54).'
  BUILD('conditional','Generate AI images/video via Higgsfield REST/SDK API ($5+ prepaid balance) or CLI/MCP (paid subscription credits)',['No free programmatic tier: API requires $5 minimum prepaid USD top-up (expiring in 1 year), while CLI and MCP require a paid subscription and exclude web Unlimited/free generations.','API outputs are stored for at least 7 days and must be downloaded for long-term retention.','CLI browser tokens are short-lived and require re-running higgsfield auth login when expired.'],['For app/backend integrations, fund an open.higgsfield.ai USD balance and generate an API key for api.higgsfield.ai.','For agent/terminal workflows on an existing paid plan, install @higgsfield/cli or connect https://mcp.higgsfield.ai/mcp.'],[cmp,cli_req,api_ov,api_bill,mcp_ent],['identity','auth.api_key','testing.paid_required','testing.self_serve','api.protocol.rest','api.protocol.cli','mcp.discovery'],'All three programmatic interfaces are publicly documented and self-serve, conditioned on prepaid USD funding (API) or a paid subscription (CLI/MCP). Documentary inference only.')
 elif a==98:
  rm='https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md'; lic='https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE'; gh='https://github.com/mermaid-js/mermaid-cli'
  ident=E(rm,1,17,'mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.')
  mit=E(lic,1,17,'Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.')
  inst=E(rm,9,23,'Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.')
  opts=E(rm,25,63,'Supports PNG/SVG/PDF output, themes, transparent backgrounds, custom icon packs (npm or URI), custom CSS animation, sizing, and transforming Markdown files with embedded Mermaid code blocks.')
  dock=E(rm,111,135,'Official container images are published on GHCR (ghcr.io/mermaid-js/mermaid-cli/mermaid-cli) and Docker Hub (minlag/mermaid-cli) for local Docker or Podman execution.')
  node=E(rm,136,158,'Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.')
  iss=E(rm,169,172,'Known operational issues include Linux sandbox configuration, Docker permission denied, and configuring an already-installed Chromium browser.')
  ID('Mermaid CLI (@mermaid-js/mermaid-cli at github.com/mermaid-js/mermaid-cli), official open-source MIT local diagram rendering CLI and Node.js library.',[ident,mit],'Render Mermaid diagram definitions and Markdown code blocks locally to SVG, PNG, or PDF via the mmdc CLI or Node.js API.')
  r['auth']['coverage_status']='checked_sources'
  A('local_none','none','Local open-source CLI (mmdc) and Node.js library executed locally or in a local container; no vendor account, API key, or OAuth credentials required.',[ident,inst,dock,mit],'Local CLI, Docker/Podman container, and Node.js API execution')
  for env in ('testing','production'):
   Q(env,'free_access',True,[mit,inst],'MIT-licensed open-source package freely installable via npm, npx, or container registries.')
   Q(env,'paid_required',False,[mit],'MIT License explicitly grants permission free of charge.')
   Q(env,'admin_approval_required',False,[inst,node],'Local CLI/package installation requires no vendor tenant or workspace administrator approval.')
   Q(env,'vendor_approval_required',False,[mit,inst],'Open-source MIT distribution on npm/GitHub/GHCR requires no vendor API approval.')
   Q(env,'partner_approval_required',False,[mit],'No partner program gate applies to MIT-licensed local software.')
   Q(env,'contact_sales_required',False,[mit],'No sales contact is required to install or run MIT-licensed software.')
   Q(env,'self_serve',True,[inst,dock,node],'Self-serve installation via npm, npx, Docker, or Podman.')
   r['credential_eligibility'][env]['trial_access']=C(env+'.trial_access',None,[ident,mit],'not_applicable',why='Local MIT-licensed CLI software has no hosted vendor trial tier.')
   r['credential_eligibility'][env]['sandbox_access']=C(env+'.sandbox_access',None,[ident,mit],'not_applicable',why='Local MIT-licensed CLI software runs directly on the user machine/container rather than a hosted vendor sandbox.')
  P('cli','CLI',[ident,inst,dock]);P('sdk','SDK',[node]);DOC([ident,opts,node])
  G('diagram_rendering','Convert .mmd Mermaid diagram files to SVG, PNG, or PDF with theme, background, size, CSS, and icon pack options',[ident,opts])
  G('markdown_transformation','Transform Markdown files containing embedded Mermaid code blocks into rendered diagram images and updated Markdown',[ident,opts])
  B('narrow',['diagram_rendering','markdown_transformation'],[ident,opts],'Focused single-domain local diagram-rendering surface; no hosted REST API.')
  r['mcp']['discovery']=C('mcp.discovery',None,[ident,E(gh,1,40,'Official github.com/mermaid-js/mermaid-cli repository overview and README checked; no official MCP server documented.')],'not_found_in_checked_sources',why='Bounded check of the official mermaid-js/mermaid-cli repository and README found no official MCP server. Absence from checked docs does not prove no community MCP exists.')
  r['auth']['notes']='Local MIT-licensed CLI/Node.js tool with no vendor authentication; lack of a hosted REST API does not block local agent tool wrapping.'
  BUILD('build_now','Wrap local mmdc CLI or Node.js run() API to render Mermaid diagrams to SVG/PNG/PDF',['Requires local Node.js/Chromium or Docker/Podman runtime; Linux sandbox and Docker permission caveats apply.','Node.js programmatic API is explicitly not covered by semver.','No official MCP server found in checked official repo docs (local CLI wrapper needed).'],['Install @mermaid-js/mermaid-cli locally or pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli.','Invoke mmdc -i input.mmd -o output.svg (or PNG/PDF) in a sandboxed local tool wrapper.'],[ident,mit,inst,node,iss],['identity','auth.local_none','testing.free_access','testing.self_serve','api.protocol.cli','api.breadth'],'Open-source MIT local CLI with zero auth or billing gates is feasible to wrap immediately; documentary feasibility only, not an operational execution test.')
 elif a==99:
  gs='https://transcriptapi.com/docs/getting-started/'; mc='https://transcriptapi.com/docs/mcp/'
  ident=E(gs,45,66,'TranscriptAPI.com provides YouTube video transcripts via a REST API (GET https://transcriptapi.com/api/v2/youtube/transcript with Authorization: Bearer YOUR_API_KEY) and MCP integration.')
  caps=E(gs,80,90,'Supports extracting YouTube video transcripts, paginated video/channel search, channel uploads, free RSS latest videos, playlist browsing, free channel handle resolution, JSON/plain-text output, metadata, and timestamps.')
  mcp_ov=E(mc,129,133,'TranscriptAPI runs a hosted remote MCP server at https://transcriptapi.com/mcp sharing the same account, API keys, and credits as the REST API; 12 tools, 2 free, others 1 credit/call or page, 100 free starter credits.')
  mcp_oa=E(mc,216,254,'MCP supports OAuth 2.1 (scope mcp:access, oat_ tokens, auto-refresh) with Dynamic Client Registration (RFC 7591, optional credentials for Claude) and Static Client Registration (Client ID/Secret from MCP Integration dashboard, required for ChatGPT).')
  mcp_key=E(mc,255,280,'API Key authentication uses Authorization: Bearer sk_... from the API Keys dashboard; keys never expire unless revoked and work identically for REST API and MCP.')
  tools=E(mc,288,330,'Lists 12 MCP tools covering transcripts (get_youtube_transcript), free video info (get_youtube_video_info), rich metadata, YouTube search, channel profile/RSS/search/videos/playlists/posts/sections, and playlist videos.')
  cred=E(mc,881,943,'New accounts get 100 free credits with no card required (verified email needed); 2 tools cost 0 credits; exhausted accounts receive 402 Payment required; paid plans start at $5/month for 1,000 credits.')
  ID('YouTube Transcript via TranscriptAPI.com (matching roster hint transcriptapi.com), hosted REST API and official callable MCP server for YouTube transcripts and channel/video metadata.',[ident,mcp_ov],'Fetch YouTube video transcripts, video metadata, search results, channel feeds, and playlists via TranscriptAPI REST v2 or hosted MCP.')
  A('api_key','API_key','API key (sk_ prefix) from the TranscriptAPI dashboard sent as Authorization: Bearer sk_...; never expires unless revoked; works for both REST API v2 and hosted MCP.',[ident,mcp_key],'TranscriptAPI REST v2 API and hosted MCP server')
  A('mcp_oauth21','OAuth2','OAuth 2.1 (scope mcp:access, oat_ tokens with refresh) supporting RFC 7591 Dynamic Client Registration (Claude) and Static Client Registration (Client ID/Secret for ChatGPT).',[mcp_oa],'TranscriptAPI hosted MCP server (https://transcriptapi.com/mcp)',['mcp:access'])
  Q('testing','free_access',True,[mcp_ov,cred],'New accounts receive 100 free credits with no credit card required (verified email needed), plus 2 zero-credit tools.')
  Q('testing','paid_required',False,[cred],'100 free starter credits with no card required and 2 free zero-credit tools allow testing without payment.')
  Q('testing','self_serve',True,[ident,mcp_oa,mcp_key,cred],'Self-serve free signup, API Keys dashboard, and MCP OAuth DCR/static client creation.')
  Q('production','paid_required',True,[cred],'Ongoing production transcript/search/channel usage beyond the 100 starter credits requires paid plans starting at $5/month for 1,000 credits (402 Payment required when credits are exhausted).')
  Q('production','self_serve',True,[mcp_key,cred],'Self-serve API key, OAuth setup, and dashboard billing at /dashboard/billing.')
  P('rest','REST',[ident,caps]);P('mcp','other',[mcp_ov,mcp_key]);DOC([ident,mcp_ov])
  G('transcripts_metadata','YouTube transcript extraction (JSON/markdown/plain text, language selection, timestamps) and video info/rich metadata',[caps,tools])
  G('search_channels_playlists','Paginated YouTube search, channel profiles/uploads/RSS/posts/sections/handle resolution, and playlist video listing',[caps,tools])
  B('narrow',['transcripts_metadata','search_channels_playlists'],[caps,tools],'Focused single-domain YouTube transcript and channel/playlist discovery surface.')
  M('transcriptapi','TranscriptAPI YouTube Transcript MCP Server',[mcp_ov,mcp_oa,mcp_key,tools],mc,'https://transcriptapi.com/mcp','Official hosted callable remote MCP server exposing 12 YouTube transcript, metadata, search, channel, and playlist tools via OAuth 2.1 (DCR or Static) or Bearer API key.')
  r['auth']['notes']='Free starter allowance is 100 one-time credits (no card) plus 2 zero-credit tools (get_youtube_video_info, get_channel_latest_videos); production.free_access remains unknown because zero-credit tools are free while core transcript calls require credits beyond the starter pool.'
  BUILD('build_now','Fetch YouTube transcripts and channel/video metadata via TranscriptAPI REST v2 or hosted MCP',['Requires verified email; core transcript calls consume 1 credit/call beyond the 100 free starter credits ($5/month for 1,000 credits).','Third-party YouTube transcript service rather than an official Google/YouTube API.'],['Sign up free at transcriptapi.com and generate an sk_ API key (or authorize OAuth 2.1 MCP).','Call GET https://transcriptapi.com/api/v2/youtube/transcript or connect https://transcriptapi.com/mcp.'],[ident,mcp_ov,mcp_key,cred],['identity','auth.api_key','testing.free_access','testing.self_serve','api.protocol.rest','mcp.discovery'],'Public REST v2 and hosted MCP server with self-serve free signup and 100 no-card starter credits make integration immediately feasible. Documentary inference only.')
 elif a==100:
  ov='https://developers.grain.com/'; au='https://developers.grain.com/authentication.html'; faq='https://developers.grain.com/mcp/faq.html'; cl='https://developers.grain.com/mcp/claude-setup.html'; ex='https://support.grain.com/en/articles/15297887-export-meetings'
  ident=E(ov,15,39,'Grain API (https://api.grain.com/_/public-api/v2) reads and manages recordings, highlights, uploads, and more using Authorization: Bearer and Public-Api-Version headers.')
  toks=E(au,16,46,'Three token types: Personal Access Token (personal scope, non-expiring, user-level access, works on REST and MCP https://api.grain.com/_/mcp), Workspace Access Token (workspace scope, admin-only, full workspace access, not on all plans, rejected by MCP), and OAuth Token (personal or workspace scope, expiring with refresh).')
  oa=E(au,47,137,'OAuth2 Authorization Code flow with PKCE S256 (https://grain.com/_/public-api/oauth2/authorize); server-side apps request Client ID/Secret manually; public/MCP clients can use an HTTPS Client ID Metadata Document; workspace scope is only available to clients verified by Grain.')
  exp=E(ex,68,94,'Any user on every plan including Free can generate a Personal API token; Workspace API tokens are for workspace admins on Business and Enterprise plans; for Grain MCP, a workspace admin enables the connector and each user connects via OAuth.')
  mfaq=E(faq,17,28,'Most Grain MCP tools (meeting search, transcripts, notes, contacts) work on all Grain plans (Free, Starter, Business, Enterprise); Deals and Sales Coaching/Scorecards tools are restricted to Business and Enterprise; MCP uses OAuth and enforces existing user permissions.')
  mcl=E(cl,16,33,'Official Grain MCP server endpoint is https://api.grain.com/_/mcp; Claude setup connects via OAuth approval.')
  mpat=E(cl,72,84,'Headless MCP clients, scripts, and CI can connect to https://api.grain.com/_/mcp using Authorization: Bearer grain_pat_...; Workspace Access Tokens are not accepted by the MCP server.')
  ID('Grain (grain.com / developers.grain.com), meeting recording and notes platform with Personal/Workspace REST APIs and official callable MCP server.',[ident,exp],'Programmatically access Grain meeting recordings, transcripts, highlights, notes, contacts, and (on paid tiers) workspace/deal/coaching data via REST or MCP.')
  A('personal_access_token','Bearer_token','Personal Access Token (grain_pat_..., personal scope) generated manually by any user on any plan including Free; non-expiring; accesses user-permitted meetings only; accepted by REST API and MCP server.',[ident,toks,exp,mpat],'Grain REST API v2 and headless Grain MCP (personal scope)')
  A('workspace_access_token','Bearer_token','Workspace Access Token (workspace scope) generated manually by workspace admins only on Business and Enterprise plans; full workspace data access; rejected by Grain MCP server.',[toks,exp,mpat],'Grain Workspace REST API (admin-only, Business/Enterprise; not MCP)')
  A('oauth2','OAuth2','OAuth2 Authorization Code flow with PKCE S256 (personal or workspace scope, expiring with refresh); supports Client ID Metadata Documents for public/MCP clients; workspace scope restricted to Grain-verified clients; server-side Client ID/Secret requested manually.',[toks,oa],'Grain multi-user REST API and interactive MCP integrations',['personal','workspace'])
  for env in ('testing','production'):
   Q(env,'free_access',True,[exp,mfaq],'Personal API tokens and core Grain MCP tools (meeting search, transcripts, notes, contacts) are available on every Grain plan including Free. Workspace API and Deals/Coaching MCP tools require Business/Enterprise.')
   Q(env,'paid_required',False,[exp,mfaq],'Personal API and core MCP meeting/transcript tools do not require a paid Grain plan; Workspace API and Deals/Coaching MCP tools are separately gated to Business and Enterprise.')
   Q(env,'self_serve',True,[ident,exp,mpat,oa],'Personal Access Tokens are self-generated in Account settings -> Integrations -> Personal API, and public/MCP clients can use Client ID Metadata Documents without manual client registration.')
  P('rest','REST',[ident,toks]);P('mcp','other',[mcl,mpat]);DOC([ident,toks,mfaq])
  G('recordings_transcripts_highlights','Recordings (including MP4), transcripts, highlights, uploads, and webhooks/hooks via REST v2',[ident,E(ov,10,13,'API Docs sidebar lists Endpoints, Uploads, Hooks, and 2025-10-31 Endpoints.'),E(ex,78,81,'API extracts transcripts and MP4 recordings (~300 calls/min).')])
  G('mcp_meetings_contacts_deals_coaching','MCP tools for meeting search, transcripts, notes, action items, clips, companies/contacts, plus Business/Enterprise-only Deals and Sales Coaching/Scorecards',[mfaq,E(ex,85,91,'Grain MCP accesses meetings, transcripts, notes, action items, coaching feedback, deal data, and clips.')])
  B('moderate',['recordings_transcripts_highlights','mcp_meetings_contacts_deals_coaching'],[ident,mfaq],'Multiple related meeting-recording, transcript/highlight, contact, deal, and coaching resource groups.')
  M('grain','Official Grain MCP Server',[mfaq,mcl,mpat],cl,'https://api.grain.com/_/mcp','Official hosted callable MCP server exposing authorized meeting search, transcripts, notes, contacts, clips, and (on Business/Enterprise) deals and coaching feedback via OAuth or Personal Access Token (grain_pat_...); rejects Workspace Access Tokens.')
  r['auth']['notes']='Paths are explicitly separated: Personal PAT works self-serve on Free+ plans for REST and headless MCP; Workspace API tokens require workspace admin + Business/Enterprise (rejected by MCP); OAuth workspace scope requires Grain client verification; support article (export-meetings line 93) notes workspace admin enables the Grain MCP connector for the workspace, so admin_approval_required and vendor_approval_required remain unknown across mixed paths.'
  BUILD('build_now','Read user-authorized Grain meetings, transcripts, and notes via Personal API token (REST v2) or headless PAT MCP',['Workspace-wide API access requires Business/Enterprise plan and workspace admin role (and is rejected by MCP).','OAuth workspace scope is restricted to Grain-verified clients; interactive workspace MCP setup notes workspace admin enablement.','Deals and Sales Coaching MCP tools require Business or Enterprise plans.'],['Generate a Personal Access Token (grain_pat_...) at grain.com/app/settings/integrations?tab=api.','Call https://api.grain.com/_/public-api/v2 with Public-Api-Version header or connect https://api.grain.com/_/mcp.'],[ident,toks,exp,mfaq,mpat,oa],['identity','auth.personal_access_token','testing.free_access','testing.self_serve','api.protocol.rest','mcp.discovery'],'Personal API tokens and core MCP tools are self-serve on every Grain plan including Free, making a personal-scope wrapper immediately feasible. Documentary inference only.')

OUT=ROOT/'work/task-16-agent/extracted-records.json'
OUT.write_text(json.dumps({'records':records},indent=2)+'\n',encoding='utf-8')
print(f'Wrote {len(records)} records to {OUT}')

