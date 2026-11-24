"""Task04 researcher-authored extraction, not automatic semantic extraction.

Claims/paraphrases below were selected by the research agent (gpt-6.1-sol)
after reading primary documentation and the captured snapshots. No model API,
fixture, account operation, independent review, or accuracy measurement occurs.
"""
import copy
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p
from make_sources import SCOPES

def build(capture_run, destination):
    directory = ROOT / 'work/task-04-runs' / capture_run
    p.verify_seal(directory)
    records = copy.deepcopy(p.read_json(directory / 'records.json'))
    captures = p.read_json(directory / 'captures.json')
    aliases = {}
    for c in captures:
        u = c['spec']['url']
        for key, end in {
            'hs_intro':'/developer-platform-basics', 'hs_auth':'/authentication/overview',
            'hs_legacy':'/private-apps/overview', 'hs_api':'/latest/overview',
            'hs_mcp':'/integrate-with-the-remote-hubspot-mcp-server',
            'fd_key':'/215517-how-to-find-your-api-key', 'fd_oauth':'/oauth-implementation-in-apps/',
            'fd_plans':'/50000011778','fd_mcp':'/50000012670','fd_rest':'/rest-apis/',
            'ads_oauth':'/oauth/overview','ads_token':'/developer-token','ads_access':'/access-levels',
            'ads_testing':'/best-practices/testing','ads_api':'/api-structure','ads_mcp':'/mcp-server',
            'ads_rest':'/rest/overview','sh_repo':'github.com/sherlock-project/sherlock',
            'sh_usage':'sherlockproject.xyz/usage','sh_license':'/master/LICENSE',
            'sh_install':'sherlockproject.xyz/installation', 'nb_api':'/api-notebooks',
            'nb_sources':'/api-notebooks-sources','nb_setup':'/set-up-notebooklm',
            'nb_licenses':'/set-up-licensing','nb_mcp':'github.com/Morfeu333/notebooklm-mcp',
        }.items():
            if u.endswith(end):
                assert key not in aliases
                aliases[key] = c

    def evidence(key, first, last, observation):
        c = aliases[key]
        lines = (directory / c['snapshot_ref']).read_text(encoding='utf-8').splitlines()
        assert 1 <= first <= last <= len(lines), (key, first, last)
        e = p.evidence_for(c, first, lines[first-1])
        e.update(locator=f'lines:{first}-{last}', observation='paraphrase: ' + observation)
        return e

    for r in records:
        app = r['identity']['id']
        scope = SCOPES[app]
        def claim(key, value, ev=(), status='observed', refs=(), rationale='Documentary observation only; independent review pending.'):
            return dict(claim_id=f'{app}.{key}', status=status, value=value, context=scope,
                evidence=list(ev), supporting_claim_refs=[f'{app}.{x}' for x in refs], rationale=rationale)
        def E(key, first, last, para):
            assert aliases[key]['spec']['app_id'] == app
            return evidence(key, first, last, para)
        def auth(key, method, details, ev, subcontext, status='observed', refs=()):
            return claim('auth.'+key,dict(method=method,context=subcontext,scopes=[],details=details),ev,status,refs,
                'Scoped mechanism; no credentials obtained or authenticated call executed.' if status=='observed' else 'Inference from documented local interface; not an operational test.')
        def items(target, entries, notes):
            target.update(coverage_status='partial',items=entries,notes=notes)
        def eligibility(env, key, val, ev, context, status='observed', refs=()):
            r['credential_eligibility'][env][key] = claim(env+'.'+key,val,ev,status,refs,context)
        def resource(key, value, ev):
            return claim('api.group.'+key,value,ev)
        def breadth(value, groups, ev, reason):
            r['api_surface']['breadth'] = claim('api.breadth',value,ev,'inferred',
                ['api.group.'+g for g in groups],reason)
        def mcp(key, origin, name, ev, source, tool_scope, server=None, repo=None):
            op = claim('mcp.'+key+'.operational',None,status='not_researched',rationale='No MCP connection or tool call was attempted.')
            r['mcp']['entries']=[claim('mcp.'+key,dict(origin=origin,name=name,source_url=aliases[source]['spec']['url'],
                repository_url=repo,server_url=server,scope=tool_scope,operational_check=op),ev)]
            r['mcp']['discovery']=claim('mcp','found',ev)
        def buildability(verdict, workflow, blockers, steps, refs, ev):
            r['buildability']=claim('buildability',dict(verdict=verdict,scope=workflow,blockers=blockers,next_steps=steps),ev,
                'inferred',['identity']+refs,'Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.')

        # Attempted but undocumented eligibility negatives stay unknown.
        for path,c in p.claims(r):
            c.update(context=scope,status='unknown',rationale='Checked selected sources; this scoped question is not established. Silence does not establish false.')
        for env in ('testing','production'):
            r['credential_eligibility'][env]['context']=scope+'; '+env+' path; narrower prerequisites are stated in each claim rationale'

        if app == 2:
            intro=E('hs_intro',251,259,'Developers can use a free account, sample-data test accounts and public APIs for development.')
            ident=E('hs_intro',244,245,'HubSpot developer tooling supports private integrations, Marketplace apps and APIs.')
            purpose=E('hs_mcp',77,80,'The CRM integration surface lets applications and agents access account CRM data.')
            r['identity']['resolution']=claim('identity','HubSpot CRM/developer platform; original HubSpot identity matched.',[ident,purpose])
            r['purpose']=claim('purpose','CRM platform whose APIs let integrations work with customer records and business workflows.',[purpose])
            oa=E('hs_auth',81,91,'Multi-account apps require OAuth; API requests send the installed account access token as Bearer.')
            static=E('hs_auth',93,98,'Single-account private distribution uses a static access token in a Bearer header.')
            legacy=E('hs_legacy',55,59,'Existing legacy private apps remain supported; new creation ended October 26, 2026, and access requires super admin.')
            items(r['auth'],[
                auth('oauth','OAuth2','OAuth access tokens for installed accounts; multi-account distribution needs hosted OAuth handling.',[oa],'Installed account API access'),
                auth('static','Bearer_token','Static access token for one authorized account; distinct from an OAuth user flow.',[static],'Current developer-platform single-account app'),
                auth('legacy','Bearer_token','Existing legacy private app token; this is not a new-app onboarding route.',[legacy,E('hs_legacy',63,69,'Legacy private app API calls use the access token as Bearer.')],'Existing legacy private apps'),
                auth('developer_key','API_key','Developer API key for selected app-management features, not general CRM data access.',[E('hs_auth',100,104,'Selected developer endpoints use a developer API key in the hapikey query parameter.')],'Selected developer app-management endpoints'),
                auth('client_credentials','OAuth2','Client-credentials tokens manage app-global webhooks journal features, not installed-user CRM actions.',[E('hs_auth',105,114,'App-global webhooks journal operations use expiring OAuth 2.0 client-credentials tokens.')],'App-global webhooks journal'),
            ],'Multiple methods/scopes retained. Legacy app creation is sunset; developer keys are not general CRM keys. Service-key details and exhaustive method coverage remain outside this pilot.')
            for key,val in [('free_access',True),('paid_required',False),('sandbox_access',True)]:
                eligibility('testing',key,val,[intro],'Free developer testing path; sandbox_access refers to developer test accounts, not a paid enterprise sandbox.')
            eligibility('testing','self_serve',True,[intro,E('hs_intro',76,87,'Free signup, guided CLI authentication and project creation form the developer onboarding path.')],
                'Inference limited to an eligible developer creating their own account; not a blanket tenant/admin exemption.','inferred',['testing.free_access','auth.static'])
            eligibility('production','admin_approval_required',True,[legacy],'Existing legacy private-app path only: requires super-admin access. New OAuth/static installations may have different permission conditions.')
            eligibility('production','free_access',True,[E('hs_legacy',130,134,'Legacy private-app rate limits explicitly include Free and Starter accounts.')],
                'Existing legacy private app in a Free account, within available scopes; does not establish a new legacy-app creation path.')
            eligibility('production','paid_required',False,[E('hs_legacy',130,134,'Legacy private-app rate limits include the Free tier.')],
                'Existing legacy private app using Free-tier features only; premium capabilities remain plan-dependent.')
            items(r['api_surface']['protocols'],[claim('api.rest','REST',[E('hs_intro',265,267,'Backend integrations can call RESTful HubSpot APIs.')])], 'REST documented; no claim about GraphQL absence.')
            r['api_surface']['public_documentation']=claim('api.public_documentation',True,[E('hs_api',118,124,'Public reference documents date-versioned API paths and a contacts GET request.')])
            gs=[resource('crm','CRM records and associations',[E('hs_api',64,81,'Reference lists CRM objects, associations, owners, pipelines and properties.')]),
                resource('marketing','Marketing resources',[E('hs_api',93,100,'Reference lists campaigns, forms and marketing-email APIs.')]),
                resource('content','Content/CMS resources',[E('hs_api',38,52,'Reference lists CMS blogs, pages, HubDB and source code.')])]
            items(r['api_surface']['resource_groups'],gs,'Documented domain families; not an endpoint inventory or confirmation of every plan entitlement.')
            breadth('broad',['crm','marketing','content'],[g['evidence'][0] for g in gs],'CRM, marketing and content are distinct business domains in the captured reference.')
            me=[E('hs_mcp',77,87,'HubSpot documents its remote CRM MCP server, https://mcp.hubspot.com, and OAuth with required PKCE.'),E('hs_mcp',119,127,'MCP actions respect user permissions; available tools vary with plan and account configuration.')]
            mcp('remote','official','HubSpot remote CRM MCP',me,'hs_mcp','Callable server for account CRM data; distinct from local developer tooling.',server='https://mcp.hubspot.com')
            buildability('build_now','Prototype CRM record reads/writes in a developer test account via scoped APIs; production evaluated per tenant.',[],
                ['Use current OAuth or static developer-platform onboarding','Check requested scopes and tenant plan before production','Test MCP separately; no operational check in this pilot'],
                ['purpose','auth.oauth','auth.static','testing.free_access','api.rest','api.group.crm','mcp.remote'],[intro,oa,static,me[1]])

        elif app == 13:
            ident=E('fd_oauth',35,39,'The documentation identifies Freshdesk resources, REST APIs, Basic/API-key access and OAuth authorization.')
            r['identity']['resolution']=claim('identity','Freshdesk helpdesk REST/API and MCP product; Freshworks support documentation matches assignment.',[ident])
            r['purpose']=claim('purpose','Customer-support helpdesk for handling tickets and conversations.',[E('fd_rest',35,42,'The support-ticket module documents ticket creation, retrieval, search and updates.'),E('fd_rest',88,92,'Conversation endpoints support ticket replies and notes.')])
            key=E('fd_key',95,101,'Verified agents retrieve a personal API key from Profile Settings; API actions follow the agent role.')
            basic=E('fd_oauth',35,39,'Freshdesk lists Basic access using API keys and OAuth token authorization as alternatives.')
            items(r['auth'],[auth('personal_key','API_key','Verified agent personal API key, with role-limited API actions.',[key],'REST agent credential'),
                auth('basic','Basic','Freshworks calls this Basic access using API keys. Exact username/dummy-password encoding remains uncaptured because the main API reference failed collection.',[basic],'REST transport for API-key credentials; same credential as personal_key'),
                auth('oauth','other','OAuth authorization/access-token flow is documented for Freshworks and private FDK custom apps. Protocol version and general external-app registration conditions are not established here.',[E('fd_oauth',38,47,'FDK Freshworks/custom apps can obtain OAuth access tokens to make authorized REST calls.')],'FDK app OAuth path; version not explicitly captured'),
                auth('mcp_key','API_key','MCP uses API-key authentication; this is distinct from the REST Basic wrapper.',[E('fd_mcp',70,72,'Freshdesk documents an official MCP bridge and API-key-only MCP authentication.')],'Official hosted MCP'),
            ],'API_key and Basic describe credential and transport aspects of the same REST path, not two independent credentials. OAuth exists in the documented FDK context; wire version/registration gates remain unknown.')
            trial=E('fd_plans',114,121,'New accounts begin with a free 14-day full-feature trial, followed by paid plans or a separate Free Program.')
            eligibility('testing','trial_access',True,[trial],'Documented product trial; API credential use remains subject to verified-agent role.', 'inferred',['auth.personal_key','api.rest'] )
            eligibility('testing','free_access',True,[trial],'Free access means the time-limited trial only, not a permanent free API plan.','inferred',['auth.personal_key','api.rest'])
            eligibility('testing','paid_required',False,[trial],'Trial subscription has no product subscription charge; not a guarantee of permanent free API access.','inferred',['auth.personal_key'])
            eligibility('testing','self_serve',True,[trial,key],'Signup trial plus verified-agent profile key is a documented developer path; role conditions still apply.','inferred',['auth.personal_key','testing.trial_access'])
            eligibility('production','self_serve',True,[key,E('fd_plans',133,145,'An Account Admin can choose a plan, pay and activate the subscription in-product.')],
                'Paid-plan Account Admin path plus verified agent key; no inference that every developer bypasses tenant administration.','inferred',['auth.personal_key'])
            eligibility('production','admin_approval_required',True,[E('fd_plans',133,145,'Purchasing and activating a paid plan is performed as Account Admin.')],
                'Tenant purchasing/setup path only; does not mean every existing verified agent needs new admin approval to read its key.')
            # API entitlement of the six-month Free Program is not established.
            r['credential_eligibility']['production']['paid_required']['rationale']='Paid plans and a temporary Free Program both exist; captured sources do not establish Free Program API entitlement. Do not assert a universal paid requirement.'
            items(r['api_surface']['protocols'],[claim('api.rest','REST',[ident])],'REST v2 resources captured through smaller official FDK guide; main reference capture rejected.')
            r['api_surface']['public_documentation']=claim('api.public_documentation',True,[E('fd_rest',34,42,'Public REST documentation lists /api/v2 ticket methods.')])
            gs=[resource('tickets','Ticket management',[E('fd_rest',36,54,'Ticket endpoints create, get, search, update, merge, delete and restore tickets.')]),
                resource('conversations','Ticket conversations',[E('fd_rest',88,92,'Conversation APIs support replies, notes, updates and deletion.')]),
                resource('time','Time entries',[E('fd_rest',102,106,'Time-entry methods create, get, update, toggle and delete tracking records.')])]
            items(r['api_surface']['resource_groups'],gs,'Partial support-ticket API scope; additional contact/company MCP tools documented separately, not silently asserted as captured REST groups.')
            breadth('moderate',['tickets','conversations','time'],[g['evidence'][0] for g in gs],'Multiple related helpdesk workflows captured; broader reference was not ingested, so no app-wide broad rating.')
            me=[E('fd_mcp',70,72,'Freshdesk describes its own MCP server and API-key authentication.'),E('fd_mcp',88,110,'Supported GA products and Growth/Pro/Enterprise action allowances are listed.'),E('fd_mcp',128,132,'The per-tenant MCP endpoint template is https://<subdomain>.freshdesk.com/mcp.')]
            mcp('official','official','Freshdesk hosted MCP',me,'fd_mcp','Callable server for supported Freshdesk Standalone 2021/Unified Omni 2026 tenants; API key; tenant URL not instantiated.')
            buildability('conditional','Read/update support tickets in an authorized trial or paid Freshdesk tenant via REST.',
                ['Verified agent key and role permissions required','Long-term free-plan API eligibility and OAuth app registration were not established'],
                ['Use verified-agent key path for initial REST prototype','Confirm entitlement/rate limits for chosen plan','Validate Basic wire convention against full reference before implementation'],
                ['auth.personal_key','auth.basic','testing.trial_access','production.self_serve','api.rest','api.group.tickets'],[key,trial,basic])

        elif app == 31:
            ident=E('ads_api',426,438,'Google Ads API models account/customer, campaign and ad-group entities.')
            # Exact ranges are checked against the saved packet before intake.
            r['identity']['resolution']=claim('identity','Google Ads API; developer-controlled campaign/account integration surface.',[ident])
            r['purpose']=claim('purpose','Programmatic advertising account, campaign and performance management.',[E('ads_api',429,435,'Google Ads services modify resources and retrieve objects and performance statistics.')])
            oauth=E('ads_oauth',421,429,'OAuth credentials must belong to the API-enabled project; Google Ads uses OAuth 2.0 to access user accounts.')
            items(r['auth'],[auth('oauth_user','OAuth2','OAuth user authorization for Ads account access.',[oauth],'Authorized Google Ads user'),
                auth('service_account','OAuth2','A service-account OAuth path is documented; principal still needs access to the target Ads accounts.',[E('ads_oauth',435,447,'The OAuth overview identifies both authorized user and service-account workflows.')],'Service-account workflow'),
                claim('auth.developer_token_requirement',None,[E('ads_oauth',417,418,'The page summary still says a developer token is required.'),E('ads_token',64,91,'The dated migration body says tokens were sunset September 9, 2026 and are optional/ignored thereafter.')],
                    'disputed',rationale='Captured official summary conflicts with dated migration text. Current onboarding body favors Cloud-project access; do not promote a mandatory developer token from stale summary text.'),
            ],'OAuth plus project access level are documented. Developer-token requirement is preserved as disputed because official page summaries contradict migration bodies; App Conversion Tracking exception is outside scope.')
            access=E('ads_access',113,122,'Enabling the Ads API automatically grants a Cloud project Test access for test accounts.')
            eligibility('testing','sandbox_access',True,[access,E('ads_testing',442,446,'Test accounts are available for development, with feature limitations.')],'Test-account environment, not live campaigns.')
            eligibility('testing','self_serve',True,[access],'Cloud project owner able to enable the API gets Test access; OAuth/account setup is still required.')
            prod=E('ads_access',123,169,'Production calls require Explorer or higher; Explorer application is submitted in Cloud Console and may be automatically approved.')
            eligibility('production','self_serve',False,[prod],'Self_serve means without vendor intervention under approved rules: new production-project access requires a Google approval decision, even where automated.','inferred',['testing.self_serve','auth.oauth_user'])
            eligibility('production','partner_approval_required',True,[prod],'Vendor API-access approval (Google), not a commercial partnership contract; Explorer-or-higher production path.')
            eligibility('production','admin_approval_required',True,[E('ads_testing',481,487,'Testing principals must be added to Ads accounts at appropriate access levels.'),E('ads_oauth',438,441,'Authorized user or service account must have target Ads-account access.')],
                'Account access assignment is required for a new principal; self-owned accounts may satisfy it themselves.','inferred',['auth.oauth_user'])
            items(r['api_surface']['protocols'],[claim('api.rest','REST',[E('ads_rest',285,300,'The API supports REST and gRPC; official libraries are recommended.')]),
                claim('api.grpc','RPC',[E('ads_rest',285,287,'Google Ads supports gRPC as well as REST.')]),
                claim('api.sdk','SDK',[E('ads_rest',288,296,'Google supplies official client libraries for calling the API.')])],'RPC specifically means gRPC; GAQL is a query language, not a separate SQL endpoint.')
            r['api_surface']['public_documentation']=claim('api.public_documentation',True,[E('ads_rest',285,300,'Public guide explains direct REST access and official client libraries.')])
            gs=[resource('campaigns','Campaign and ad-group resources',[E('ads_api',434,455,'Customer accounts contain campaigns and ad groups, with ads and criteria.')]),
                resource('performance','Performance and metadata querying',[E('ads_api',429,435,'GoogleAdsService retrieves objects/performance; metadata retrieval is also documented.')])]
            items(r['api_surface']['resource_groups'],gs,'Related advertising-management workflows captured; no exhaustive service count.')
            breadth('moderate',['campaigns','performance'],[g['evidence'][0] for g in gs],'Captured campaign management and performance querying are multiple related advertising workflows.')
            me=[E('ads_mcp',425,456,'Google documents an Ads MCP server with callable tools, stdio/HTTP transport and read plus selected mutations.'),E('ads_mcp',480,505,'MCP setup uses API-enabled Cloud-project access, OAuth/ADC, and the adwords scope.')]
            mcp('official','official','Google Ads MCP server',me,'ads_mcp','Callable server for Ads data analysis and selected mutations; configured locally or deployed remotely; no deployment URL captured.')
            buildability('conditional','Read campaign performance for authorized production Ads accounts; develop safe requests against test accounts.',
                ['Production project needs Explorer or higher approval and target-account access','Test accounts cannot establish realistic performance-report behavior'],
                ['Use current Cloud-project onboarding and OAuth','Resolve token-summary inconsistency before implementing credential checklist','Request higher access for planning/billing operations if needed'],
                ['auth.oauth_user','testing.sandbox_access','production.partner_approval_required','api.rest','api.group.performance','mcp.official'],[oauth,access,prod,E('ads_testing',445,468,'Test accounts omit features; production accounts provide real performance metrics.')])

        elif app == 58:
            ident=E('sh_repo',170,190,'The assignment repository describes Sherlock username discovery and provides CLI installation and invocation.')
            r['identity']['resolution']=claim('identity','sherlock-project/sherlock, the open-source username-search project; not similarly named CRM, detective or Apple-doc products.',[ident])
            r['purpose']=claim('purpose','Find candidate social-network profiles for a supplied username.',[E('sh_repo',188,200,'The CLI accepts one or more usernames and records discovered accounts.')])
            cli=E('sh_repo',188,200,'Documented CLI examples take usernames as arguments and write per-user results.')
            license=E('sh_license',1,10,'The MIT license permits use, modification and distribution without a license charge, subject to preserving notices.')
            items(r['auth'],[auth('cli','none','The documented local username-search invocation exposes no Sherlock credential step; this is an inference about that interface, not target sites.',[cli,E('sh_install',32,38,'Official package installation is followed directly by CLI use.')],'Local CLI only',status='inferred',refs=['api.cli'])],
                'No REST/token authentication invented. Target-site behavior and any separately hosted services are outside this local interface finding.')
            for env in ('testing','production'):
                eligibility(env,'free_access',True,[license],'Free software-license path only; network/compute costs or third-party services are not covered.')
                eligibility(env,'paid_required',False,[license],'No paid Sherlock software license required under MIT; deployment expenses not evaluated.')
                eligibility(env,'self_serve',True,[E('sh_install',32,38,'The project provides direct pipx/pip install instructions and immediate CLI use.')],
                    'Local software acquisition/install path; machine permissions and network access remain prerequisites.','inferred',['auth.cli','api.cli'])
            items(r['api_surface']['protocols'],[claim('api.cli','CLI',[cli])],'CLI established. Public REST/GraphQL and stable SDK support remain unknown rather than absent.')
            r['api_surface']['public_documentation']=claim('api.public_documentation',True,[E('sh_usage',23,38,'Public usage documentation shows single/multiple username invocations and CLI options.')])
            group=resource('username','Username search and result export',[E('sh_repo',188,212,'CLI accepts usernames and supports file/CSV/XLSX results and selected-site checks.')])
            items(r['api_surface']['resource_groups'],[group],'One focused local workflow; websites checked are not separate toolkit resource groups.')
            breadth('narrow',['username'],group['evidence'],'Username discovery and result export form one focused CLI workflow.')
            r['mcp']['discovery']=claim('mcp',None,[E('sh_repo',170,226,'Checked official README installation/usage sections describe CLI operations and do not describe an MCP server.'),E('sh_usage',23,77,'Checked official usage page documents CLI invocation/options, without a callable MCP implementation.')],
                'not_found_in_checked_sources',rationale='Bounded official README/usage/installation search only. Web search returned unrelated similarly named projects; none establishes an app-matching server. No global no-MCP claim.')
            buildability('build_now','Wrap the local Sherlock CLI as a username-search tool with structured result handling.',[],
                ['Install a supported package and bound runtime/output','Validate results on authorized examples; successful target detection was not tested','Do not advertise an existing official MCP or REST API without further evidence'],
                ['auth.cli','testing.free_access','testing.self_serve','api.cli','api.group.username'],[cli,license])

        elif app == 91:
            renamed=E('nb_licenses',140,147,'NotebookLM Enterprise is renamed Gemini Notebook Enterprise while the subscription name remains NotebookLM Enterprise.')
            r['identity']['resolution']=claim('identity','Assignment Enterprise API maps to Gemini Notebook Enterprise (renamed NotebookLM Enterprise); personal NotebookLM is a separate scope.',[renamed])
            r['purpose']=claim('purpose','Enterprise document research notebooks with programmatic notebook and source management.',[E('nb_api',148,155,'The product generates document insights and summaries, with notebook management APIs.')])
            auth_ev=E('nb_api',157,172,'Notebook APIs require a licensed user, Cloud NotebookLM User role and a user access token generated after gcloud login.')
            items(r['auth'],[auth('user_bearer','Bearer_token','Licensed user access token from gcloud auth login/print-access-token; Cloud NotebookLM User role required.',[auth_ev,E('nb_api',199,203,'REST calls send Authorization:Bearer with the user access token.')],'Enterprise notebook REST v1alpha; licensed user'),
                auth('drive_user','Bearer_token','Drive-backed source ingestion additionally requires user authorization to Google Drive.',[E('nb_sources',157,163,'Google Docs/Slides ingestion requires user credentials with Drive access via gcloud login --enable-gdrive-access.')],'Enterprise API Drive-source access')],
                'Captured API recipe establishes user Bearer tokens. Unlicensed service accounts, personal cookies and Gemini API keys are not substituted for Enterprise notebook authentication. OAuth issuance details not separately captured.')
            trial=E('nb_licenses',168,180,'Subscriptions include a full-feature 14-day free-trial tier; trial users also need the Cloud NotebookLM User role.')
            admin=E('nb_licenses',175,183,'Subscription setup requires Cloud NotebookLM Admin and Gemini Enterprise Admin roles.')
            paid=E('nb_licenses',160,173,'Paid monthly/yearly subscriptions have at least 15 licenses; a trial is a separate tier.')
            for key,val in [('trial_access',True),('free_access',True),('paid_required',False)]:
                eligibility('testing',key,val,[trial,auth_ev], 'Licensed trial-user API path; free_access covers trial subscription only. Billing/project prerequisites may create other costs.','inferred',['auth.user_bearer'])
            eligibility('testing','admin_approval_required',True,[admin],'Organization subscription setup requires administrator IAM roles, including for trial setup.')
            eligibility('production','admin_approval_required',True,[admin],'Subscription provisioning requires the stated administrator roles; licensed users then need notebook User role.')
            eligibility('production','paid_required',True,[paid],'Ongoing subscription after the 14-day trial, not a statement that trials are paid.')
            for env in ('testing','production'):
                eligibility(env,'self_serve',True,[E('nb_licenses',190,212,'An authorized administrator can add the chosen subscription tier in Google Cloud Console.')],
                    'Administrator with project/billing/IAM prerequisites; console subscription path, not an unrestricted personal developer account.','inferred',['auth.user_bearer',env+'.admin_approval_required'])
            items(r['api_surface']['protocols'],[claim('api.rest','REST',[E('nb_api',195,206,'The API guide documents notebook creation via a v1alpha REST POST.')])],
                'Enterprise Discovery Engine v1alpha notebook API; the notebook guide is Preview. Personal NotebookLM API and chat parity are unresolved.')
            r['api_surface']['public_documentation']=claim('api.public_documentation',True,[E('nb_api',137,155,'Public Preview documentation describes notebook methods.')])
            gs=[resource('notebooks','Notebook creation/retrieval/deletion/sharing',[E('nb_api',148,155,'Documented notebook management covers create, get, recent list, delete and share.')]),
                resource('sources','Notebook source ingestion/retrieval/deletion',[E('nb_sources',148,156,'Source methods support batch additions, file upload, retrieval and deletion.')])]
            items(r['api_surface']['resource_groups'],gs,'Only captured notebook/source workflows; no assumption of full personal UI or query/chat API parity.')
            breadth('moderate',['notebooks','sources'],[g['evidence'][0] for g in gs],'Notebook lifecycle and source lifecycle are multiple related research workflows, not generic Gemini generation.')
            source_url=aliases['nb_mcp']['spec']['url']
            me=[E('nb_mcp',151,165,'Repository documents an MCP server for notebooklm.google.com and lists notebook tools.'),E('nb_mcp',220,224,'The implementation uses undocumented internal APIs and browser cookies for personal/experimental use.')]
            mcp('personal_community','community','Morfeu333 NotebookLM MCP implementation',me,'nb_mcp',
                'Community callable server for personal notebooklm.google.com/internal APIs; not established as an Enterprise REST integration.',repo=source_url)
            buildability('conditional','Create/share Enterprise notebooks and ingest sources for a licensed organizational user via REST.',
                ['Enterprise subscription/license assignment, IAM roles and API-enabled billed project required','Notebook API is Preview; personal chat workflow parity is not established'],
                ['Provision trial and required roles through an authorized administrator','Use licensed-user token path and test notebook/source calls','Evaluate community personal MCP separately from the Enterprise toolkit'],
                ['auth.user_bearer','testing.trial_access','production.paid_required','production.admin_approval_required','api.rest','api.group.notebooks','api.group.sources'],
                [auth_ev,paid,E('nb_setup',259,287,'Setup requires a project, enabled billing and the Discovery Engine API.'),E('nb_api',140,147,'Notebook API is a Preview feature governed by pre-GA terms.')])

        assert r['review'] == dict(status='pending',reviewer=None,reviewed_on=None,adjudications=[])
    destination = Path(destination)
    with destination.open('x',encoding='utf-8') as f:
        json.dump({'records':records},f,ensure_ascii=False,indent=2)
    for r in records:
        print(r['identity']['app'],dict(Counter(c['status'] for _,c in p.claims(r))))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: build_extraction.py CAPTURE_RUN_ID NEW_JSON_PATH')
    build(sys.argv[1],sys.argv[2])
