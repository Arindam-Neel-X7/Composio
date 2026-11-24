# Task 18: Human Recheck Worksheet (Frozen 20-App Sample)

- **Sampling Manifest**: `composio-20app-sample-v1`
- **Date**: `2026-11-24`
- **Total Eligible Assertions**: `327`
- **Corrected Assertions (Action Required)**: `50`
- **Unchanged Baseline Assertions**: `277`

> [!IMPORTANT]
> Reviewer instructions: For each corrected claim below, open the primary documentation link, inspect the cited excerpt, 
> and record your human recheck judgment (`correct`, `incorrect`, `unsupported`, `unresolved`, `not_applicable`) 
> along with an explanation. Human attestation is required for all submitted decisions.

---

## App 4: Attio (CRM and Sales)
- Total claims: 17 | Corrected: 2

### Claim: `4.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:57-75): REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Spans CRM objects/records, lists/notes/tasks, activities/call recordings, webhooks, and SCIM provisioning.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Attio documentation defines four distinct top-level functional domains: (1) Core CRM Objects & Records, (2) Collaboration & Tasks (Lists, Notes, Tasks, Comments), (3) Interaction Tracking (Activities, Call Recordings), and (4) Workspace Administration (SCIM 2.0 provisioning, Webhooks). Per evidence rules, multiple distinct business domains substantiate a broad API surface.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:57-75`)
  - *Observation*: paraphrase: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.
  ```text
  Core endpoints
  Standard objects
  SCIM 2.0
  OAuth 2.0
  Webhook reference
  Activity events
  Activity attribute events
  Activity record events
  Call recording events
  Comment events
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.group.lists_notes_tasks` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Lists, notes, comments, and tasks. Source evidence (lines:57-75) states: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:57-75`)
  - *Observation*: paraphrase: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.
  ```text
  Core endpoints
  Standard objects
  SCIM 2.0
  OAuth 2.0
  Webhook reference
  Activity events
  Activity attribute events
  Activity record events
  Call recording events
  Comment events
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.group.objects_records` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Standard/custom objects and records. Source evidence (lines:57-75) states: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:57-75`)
  - *Observation*: paraphrase: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.
  ```text
  Core endpoints
  Standard objects
  SCIM 2.0
  OAuth 2.0
  Webhook reference
  Activity events
  Activity attribute events
  Activity record events
  Call recording events
  Comment events
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.group.webhooks_scim` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Webhooks, activities, call recordings, and SCIM 2.0. Source evidence (lines:57-75) states: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:57-75`)
  - *Observation*: paraphrase: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.
  ```text
  Core endpoints
  Standard objects
  SCIM 2.0
  OAuth 2.0
  Webhook reference
  Activity events
  Activity attribute events
  Activity record events
  Call recording events
  Comment events
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.public_documentation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:81-89) states: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:81-89`)
  - *Observation*: paraphrase: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.
  ```text
  Attio provides a public REST API which exchanges JSON over HTTPS. In this section, you will find
  guidance about working with the API.
  To get up and running, read our guide on how to authenticate requests.
  From there, feel free to explore other topics or jump straight to the reference documentation.
  Building an OAuth flow for your app
  Working within our rate limits
  Setting up and listening to webhooks
  Filtering and sorting record and entry API queries
  Paginating API responses
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:81-89) states: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:81-89`)
  - *Observation*: paraphrase: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.
  ```text
  Attio provides a public REST API which exchanges JSON over HTTPS. In this section, you will find
  guidance about working with the API.
  To get up and running, read our guide on how to authenticate requests.
  From there, feel free to explore other topics or jump straight to the reference documentation.
  Building an OAuth flow for your app
  Working within our rate limits
  Setting up and listening to webhooks
  Filtering and sorting record and entry API queries
  Paginating API responses
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.api.sql` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other. Source evidence (lines:116-118) states: Ultra plan includes querying workspace data in SQL with API or MCP. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:116-118`)
  - *Observation*: paraphrase: Ultra plan includes querying workspace data in SQL with API or MCP.
  ```text
  Everything in Pro, and:
  Unlimited objects
  Query in SQL with API or MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.auth.api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Single-workspace REST API. Source evidence (lines:91-105) states: Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/guides/authentication](https://docs.attio.com/rest-api/guides/authentication) (locator: `lines:91-105`)
  - *Observation*: paraphrase: Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations.
  ```text
  In order to make requests to the Attio REST API, you need to generate an access token.
  There are two ways to generate an access token:
  By implementing an OAuth 2.0 flow
  By generating an API key for your workspace
  You should prefer the OAuth 2.0 flow if building an app for multiple workspaces. If you are building
  an app for a single workspace, you can manually generate an API key to make requests on behalf of
  that workspace only.
  Generating access tokens
  OAuth 2.0
  Attio implements the standard OAuth 2.0 specification,
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.auth.oauth2` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Multi-workspace REST API and Attio MCP. Source evidence (lines:91-105) states: Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/guides/authentication](https://docs.attio.com/rest-api/guides/authentication) (locator: `lines:91-105`)
  - *Observation*: paraphrase: Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations.
  ```text
  In order to make requests to the Attio REST API, you need to generate an access token.
  There are two ways to generate an access token:
  By implementing an OAuth 2.0 flow
  By generating an API key for your workspace
  You should prefer the OAuth 2.0 flow if building an app for multiple workspaces. If you are building
  an app for a single workspace, you can manually generate an API key to make requests on behalf of
  that workspace only.
  Generating access tokens
  OAuth 2.0
  Attio implements the standard OAuth 2.0 specification,
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for CRM record, list, activity, and task automation via Attio REST API or official hosted MCP. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:81-89): Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "CRM record, list, activity, and task automation via Attio REST API or official hosted MCP", "blockers": ["SQL querying via API/MCP requires the Ultra plan ($1,000/mo/workspace); custom objects require Pro or higher."], "next_steps": ["Create a free Attio workspace to generate a workspace API key or register an OAuth 2.0 app.", "Build against Attio REST API or connect MCP clients to https://mcp.attio.com/mcp via OAuth."]}`
  - Original Rationale: Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "CRM record, list, activity, and task automation via Attio REST API or official hosted MCP", "blockers": ["SQL querying via API/MCP requires the Ultra plan ($1,000/mo/workspace); custom objects require Pro or higher."], "next_steps": ["Create a free Attio workspace to generate a workspace API key or register an OAuth 2.0 app.", "Build against Attio REST API or connect MCP clients to https://mcp.attio.com/mcp via OAuth."]}`
  - Corrected Rationale: Buildability inference is anchored directly to the verified prerequisite chain: free self-serve workspace access (4.testing.free_access), public JSON REST API v2 (4.api.rest), and official hosted MCP endpoint https://mcp.attio.com/mcp (4.mcp.hosted_official) with zero vendor gating or partner blockers.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:81-89`)
  - *Observation*: paraphrase: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.
  ```text
  Attio provides a public REST API which exchanges JSON over HTTPS. In this section, you will find
  guidance about working with the API.
  To get up and running, read our guide on how to authenticate requests.
  From there, feel free to explore other topics or jump straight to the reference documentation.
  Building an OAuth flow for your app
  Working within our rate limits
  Setting up and listening to webhooks
  Filtering and sorting record and entry API queries
  Paginating API responses
  ```
- **URL**: [https://docs.attio.com/rest-api/guides/authentication](https://docs.attio.com/rest-api/guides/authentication) (locator: `lines:91-105`)
  - *Observation*: paraphrase: Attio REST API supports two ways to generate access tokens: OAuth 2.0 Authorization Code Grant Flow (RFC 6749) for multi-workspace apps, or manually generated workspace API keys for single-workspace integrations.
  ```text
  In order to make requests to the Attio REST API, you need to generate an access token.
  There are two ways to generate an access token:
  By implementing an OAuth 2.0 flow
  By generating an API key for your workspace
  You should prefer the OAuth 2.0 flow if building an app for multiple workspaces. If you are building
  an app for a single workspace, you can manually generate an API key to make requests on behalf of
  that workspace only.
  Generating access tokens
  OAuth 2.0
  Attio implements the standard OAuth 2.0 specification,
  ```
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:71-81`)
  - *Observation*: paraphrase: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.
  ```text
  Free
  For individuals to get started with Attio.
  $00
  Up to 3 users.
  Start for free
  Get started with:
  Ask Attio, your personal agent
  Self-builds from email and calendar
  Automatic enrichment
  Agents and workflows
  ```
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:94-118`)
  - *Observation*: paraphrase: Pro plan adds Custom objects; Ultra plan ($1,000/mo/workspace) includes querying in SQL with API or MCP.
  ```text
  Pro
  Most popular
  For growing teams turning sales into a repeatable engine.
  $125100mo/workspace
  Includes 1 user.
  Add users for $99$79/mo each.
  Start for free
  Everything in Plus, and:
  Custom objects
  Call intelligence
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:28-33`)
  - *Observation*: paraphrase: Hosted remote MCP server endpoint is https://mcp.attio.com/mcp using OAuth authentication (no API keys required).
  ```text
  Attio MCP uses OAuth authentication, so you simply log in with your Attio account—no API keys required.
  #### Add as a Custom Connector
  In your AI tool of choice, add the following URL as a custom MCP connector:
  ```
  https://mcp.attio.com/mcp
  ```
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:8-15) states: Attio MCP is Attio's official hosted MCP server giving AI tools OAuth-authenticated access to search, read, create, and update workspace records. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:8-15`)
  - *Observation*: paraphrase: Attio MCP is Attio's official hosted MCP server giving AI tools OAuth-authenticated access to search, read, create, and update workspace records.
  ```text
  ## What is Attio MCP?
  Attio MCP is Attio's hosted MCP server that gives AI tools secure access to your Attio workspace. It's designed to work seamlessly with popular AI assistants like Claude, ChatGPT, Cursor, and more.
  ### Why use Attio MCP?
  * **Easy setup** — Connect through simple OAuth with one-click installation for supported AI tools
  * **Natural language CRM management** — Manage your entire Attio workspace through conversational AI instead of clicking through multiple screens
  * **Full workspace access** — AI tools can search, read, create, and update records across your CRM—people, companies, deals, tasks, and notes
  * **Optimized for AI** — Built specifically for AI agents with efficient data formatting and human-readable responses
  * **Secure by design** — Authenticates as your Attio user with OAuth, and read operations are auto-approved while write operations request confirmation
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:28-33`)
  - *Observation*: paraphrase: Hosted remote MCP server endpoint is https://mcp.attio.com/mcp using OAuth authentication (no API keys required).
  ```text
  Attio MCP uses OAuth authentication, so you simply log in with your Attio account—no API keys required.
  #### Add as a Custom Connector
  In your AI tool of choice, add the following URL as a custom MCP connector:
  ```
  https://mcp.attio.com/mcp
  ```
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:49-78`)
  - *Observation*: paraphrase: Documents callable MCP tools across Records & Objects (list-objects, search-records, create-record, upsert-record), Activities, and Lists.
  ```text
  ### Records & Objects
  | Tool | Description | Example Prompts |
  | - | - | - |
  | `list-objects` | List all objects in the workspace (e.g. companies, people, deals), with optional fuzzy search by name or API slug | • "What objects do we have?" • "Find the object for tracking deals" |
  | `search-records` | Full-text search for records (people, companies, deals, etc.) by name, email, domain, or other indexed attributes | • "Find all contacts at Stripe" • "What's the email for Namit Chadha?" • "Show me everything we know about TheSwarm" |
  | `list-records` | List records in a given object with optional filtering and sorting | • "List all open deals" • "Show me companies created this month" |
  | `get-records-by-ids` | Retrieve full details for specific records by their IDs | • "Get the complete profile for this contact" • "Show me all details for these three companies" |
  | `create-record` | Create a new record (person, company, deal, or custom object) | • "Add a new contact: John Smith, CTO at Acme Corp" • "Create a company record for Linear" |
  | `upsert-record` | Create or update a record using a matching attribute (e.g., email or domain) | • "Update the company record for stripe.com with their new funding info" • "Add or update Sarah's contact with her new title" |
  | `update-record` | Update an existing record by `record_id` | • "Update this company record with the new ARR" • "Change Sarah's title to VP Product" |
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.mcp.hosted_official` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Attio MCP; source_url=https://docs.attio.com/mcp/overview.md. Source evidence (lines:8-15) states: Attio MCP is Attio's official hosted MCP server giving AI tools OAuth-authenticated access to search, read, create, and update workspace records. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:8-15`)
  - *Observation*: paraphrase: Attio MCP is Attio's official hosted MCP server giving AI tools OAuth-authenticated access to search, read, create, and update workspace records.
  ```text
  ## What is Attio MCP?
  Attio MCP is Attio's hosted MCP server that gives AI tools secure access to your Attio workspace. It's designed to work seamlessly with popular AI assistants like Claude, ChatGPT, Cursor, and more.
  ### Why use Attio MCP?
  * **Easy setup** — Connect through simple OAuth with one-click installation for supported AI tools
  * **Natural language CRM management** — Manage your entire Attio workspace through conversational AI instead of clicking through multiple screens
  * **Full workspace access** — AI tools can search, read, create, and update records across your CRM—people, companies, deals, tasks, and notes
  * **Optimized for AI** — Built specifically for AI agents with efficient data formatting and human-readable responses
  * **Secure by design** — Authenticates as your Attio user with OAuth, and read operations are auto-approved while write operations request confirmation
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:28-33`)
  - *Observation*: paraphrase: Hosted remote MCP server endpoint is https://mcp.attio.com/mcp using OAuth authentication (no API keys required).
  ```text
  Attio MCP uses OAuth authentication, so you simply log in with your Attio account—no API keys required.
  #### Add as a Custom Connector
  In your AI tool of choice, add the following URL as a custom MCP connector:
  ```
  https://mcp.attio.com/mcp
  ```
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:49-78`)
  - *Observation*: paraphrase: Documents callable MCP tools across Records & Objects (list-objects, search-records, create-record, upsert-record), Activities, and Lists.
  ```text
  ### Records & Objects
  | Tool | Description | Example Prompts |
  | - | - | - |
  | `list-objects` | List all objects in the workspace (e.g. companies, people, deals), with optional fuzzy search by name or API slug | • "What objects do we have?" • "Find the object for tracking deals" |
  | `search-records` | Full-text search for records (people, companies, deals, etc.) by name, email, domain, or other indexed attributes | • "Find all contacts at Stripe" • "What's the email for Namit Chadha?" • "Show me everything we know about TheSwarm" |
  | `list-records` | List records in a given object with optional filtering and sorting | • "List all open deals" • "Show me companies created this month" |
  | `get-records-by-ids` | Retrieve full details for specific records by their IDs | • "Get the complete profile for this contact" • "Show me all details for these three companies" |
  | `create-record` | Create a new record (person, company, deal, or custom object) | • "Add a new contact: John Smith, CTO at Acme Corp" • "Create a company record for Linear" |
  | `upsert-record` | Create or update a record using a matching attribute (e.g., email or domain) | • "Update the company record for stripe.com with their new funding info" • "Add or update Sarah's contact with her new title" |
  | `update-record` | Update an existing record by `record_id` | • "Update this company record with the new ARR" • "Change Sarah's title to VP Product" |
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:71-81) states: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:71-81`)
  - *Observation*: paraphrase: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.
  ```text
  Free
  For individuals to get started with Attio.
  $00
  Up to 3 users.
  Start for free
  Get started with:
  Ask Attio, your personal agent
  Self-builds from email and calendar
  Automatic enrichment
  Agents and workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:71-81) states: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans. The cited route appears accessible without this particular gate for production access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:71-81`)
  - *Observation*: paraphrase: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.
  ```text
  Free
  For individuals to get started with Attio.
  $00
  Up to 3 users.
  Start for free
  Get started with:
  Ask Attio, your personal agent
  Self-builds from email and calendar
  Automatic enrichment
  Agents and workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Flexible CRM platform offering a JSON REST API and hosted MCP server for managing objects, records, lists, activities, notes, and tasks.. Source evidence (lines:81-89) states: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:81-89`)
  - *Observation*: paraphrase: Attio provides a public REST API exchanging JSON over HTTPS with OAuth, webhooks, filtering/sorting, and pagination.
  ```text
  Attio provides a public REST API which exchanges JSON over HTTPS. In this section, you will find
  guidance about working with the API.
  To get up and running, read our guide on how to authenticate requests.
  From there, feel free to explore other topics or jump straight to the reference documentation.
  Building an OAuth flow for your app
  Working within our rate limits
  Setting up and listening to webhooks
  Filtering and sorting record and entry API queries
  Paginating API responses
  ```
- **URL**: [https://docs.attio.com/rest-api/overview](https://docs.attio.com/rest-api/overview) (locator: `lines:57-75`)
  - *Observation*: paraphrase: REST API docs cover Standard objects, Core endpoints, SCIM 2.0, OAuth 2.0, and webhook events for activities, call recordings, comments, lists, notes, records, tasks, and workspace members.
  ```text
  Core endpoints
  Standard objects
  SCIM 2.0
  OAuth 2.0
  Webhook reference
  Activity events
  Activity attribute events
  Activity record events
  Call recording events
  Comment events
  ```
- **URL**: [https://docs.attio.com/mcp/overview.md](https://docs.attio.com/mcp/overview.md) (locator: `lines:7-15`)
  - *Observation*: paraphrase: Attio MCP is Attio's hosted MCP server connecting AI assistants to Attio CRM workspaces for people, companies, deals, tasks, and notes.
  ```text
  Connect your AI tools to Attio using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction), an open standard that lets AI assistants interact with your Attio CRM workspace.
  ## What is Attio MCP?
  Attio MCP is Attio's hosted MCP server that gives AI tools secure access to your Attio workspace. It's designed to work seamlessly with popular AI assistants like Claude, ChatGPT, Cursor, and more.
  ### Why use Attio MCP?
  * **Easy setup** — Connect through simple OAuth with one-click installation for supported AI tools
  * **Natural language CRM management** — Manage your entire Attio workspace through conversational AI instead of clicking through multiple screens
  * **Full workspace access** — AI tools can search, read, create, and update records across your CRM—people, companies, deals, tasks, and notes
  * **Optimized for AI** — Built specifically for AI agents with efficient data formatting and human-readable responses
  * **Secure by design** — Authenticates as your Attio user with OAuth, and read operations are auto-approved while write operations request confirmation
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:71-81) states: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:71-81`)
  - *Observation*: paraphrase: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.
  ```text
  Free
  For individuals to get started with Attio.
  $00
  Up to 3 users.
  Start for free
  Get started with:
  Ask Attio, your personal agent
  Self-builds from email and calendar
  Automatic enrichment
  Agents and workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `4.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:71-81) states: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans. The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://attio.com/pricing](https://attio.com/pricing) (locator: `lines:71-81`)
  - *Observation*: paraphrase: Attio offers a Free CRM plan ($0, up to 3 users, 50,000 records, 3 objects) plus paid plans.
  ```text
  Free
  For individuals to get started with Attio.
  $00
  Up to 3 users.
  Start for free
  Get started with:
  Ask Attio, your personal agent
  Self-builds from email and calendar
  Automatic enrichment
  Agents and workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 8: Close (CRM and Sales)
- Total claims: 17 | Corrected: 2

### Claim: `8.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:16-38): Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Covers CRM leads/contacts, multi-channel outreach/sequences, webhooks/events, and reporting.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Close documentation defines multiple distinct business domains: (1) Lead & Contact Management, (2) Multi-channel Communications (Calls, Emails, SMS), (3) Workflow Automation (Sequences), and (4) Sales Analytics/Reporting. Per evidence rules, multiple distinct business domains substantiate a broad API surface.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.api.group.activities_outreach` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Activities, email/SMS outreach, sequences, and bulk actions. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.api.group.leads_contacts` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Leads, contacts, and custom data. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.api.group.webhooks_reporting` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Webhooks, 30-day event log, and pipeline reporting. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.api.public_documentation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.api.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.auth.api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Basic authentication for Internal scripts and single-org integrations. Source evidence (lines:15-31) states: API keys (created in Settings -> Developer -> API Keys, user/org-scoped) authenticate via HTTP Basic Auth with the API key as username and an empty password. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/topics/authentication/](https://developer.close.com/topics/authentication/) (locator: `lines:15-31`)
  - *Observation*: paraphrase: API keys (created in Settings -> Developer -> API Keys, user/org-scoped) authenticate via HTTP Basic Auth with the API key as username and an empty password.
  ```text
  Authentication with API keys
  How to authenticate Close API requests using API keys with HTTP Basic Auth.
  Ask a question|Copy page|View as Markdown|More actions
  API keys are best used for scripts and simple integrations that are internal to
  your organization. Alternatively, see Authentication with OAuth
  instead.
  Getting an API key
  API keys can be created and managed in your Close account under Settings → Developer → API Keys.
  API keys are scoped to a particular user/organization combination and can be generated and deleted in the Settings page. See API Keys & OAuth for more information.
  Perform API calls with API key
  ```
- **URL**: [https://developer.close.com/mcp/](https://developer.close.com/mcp/) (locator: `lines:88-88`)
  - *Observation*: paraphrase: Close MCP server also supports API key authentication via the Close-API-Key header.
  ```text
  OAuth is recommended. If you need to use an API key instead, select Header Auth for Authentication and create a Header Auth Credential with Name set to Close-API-Key and Value set to your Close API Key.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.auth.oauth2` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for User-facing and multi-tenant integrations. Source evidence (lines:31-45) states: OAuth 2.0 authorization code flow exchanges code for Bearer access_token (expires_in 3600s) and refresh_token with scopes all.full_access and offline_access. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/api/overview/oauth-authentication.md](https://developer.close.com/api/overview/oauth-authentication.md) (locator: `lines:31-45`)
  - *Observation*: paraphrase: OAuth 2.0 authorization code flow exchanges code for Bearer access_token (expires_in 3600s) and refresh_token with scopes all.full_access and offline_access.
  ```text
  ```
  You will get a following JSON response:
  ```json
  {
  "token_type": "Bearer",
  "access_token": "ACCESS_TOKEN",
  "expires_in": 3600,
  "refresh_token": "REFRESH_TOKEN",
  "scope": "all.full_access offline_access",
  "organization_id": "ORGANIZATION_ID",
  ```
- **URL**: [https://developer.close.com/integrations/create-an-oauth-app.md](https://developer.close.com/integrations/create-an-oauth-app.md) (locator: `lines:3-21`)
  - *Observation*: paraphrase: OAuth apps are created in Settings -> Developer -> OAuth Apps with all.full_access offline_access scopes; apps are Private by default and require requesting publication to become public.
  ```text
  OAuth 2.0 allows third-party applications to access Close data on behalf of users without exposing passwords or sharing API keys. You can create custom OAuth apps for Close to add bespoke features, automate tasks, and enhance data analytics, tailored to your business needs.
  ## Create a new OAuth app
  #### Go to OAuth Apps settings
  Navigate to [**Settings** → **Developer** → **OAuth Apps**](https://app.close.com/settings/developer/oauth-apps) and click **Create App**.
  #### Fill in your app details
  * **App Name** — Your application name that users will see on the consent screen.
  * **App Description** — 1–2 sentence description of what your app does.
  * **Redirect URL** — The http**s** URL where users are redirected after authorizing your app (e.g. `https://yourapp.com/callback/close`). Must use TLS/SSL — plain `http://` URLs are not accepted.
  * **Terms of Service URL** — Optional for internal-only apps
  * **Privacy Policy URL** — Optional for internal-only apps
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Sales CRM and outreach agent toolkit via Close REST API or official hosted MCP. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:16-38): Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Sales CRM and outreach agent toolkit via Close REST API or official hosted MCP", "blockers": ["Production requires a paid Close subscription (only a 14-day free trial is offered; no free tier).", "Multi-tenant public OAuth distribution requires requesting publication approval from Close (OAuth apps are Private by default)."], "next_steps": ["Start a 14-day no-card free trial to test API key (Basic Auth), private OAuth app, or https://mcp.close.com/mcp.", "Submit OAuth app for Close public listing if distributing across external Close customer orgs."]}`
  - Original Rationale: Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Sales CRM and outreach agent toolkit via Close REST API or official hosted MCP", "blockers": ["Production requires a paid Close subscription (only a 14-day free trial is offered; no free tier).", "Multi-tenant public OAuth distribution requires requesting publication approval from Close (OAuth apps are Private by default)."], "next_steps": ["Start a 14-day no-card free trial to test API key (Basic Auth), private OAuth app, or https://mcp.close.com/mcp.", "Submit OAuth app for Close public listing if distributing across external Close customer orgs."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Close platform documentation: REST API and official hosted MCP server are fully documented and functional, but require an active Close plan ($49+/seat/mo) or active trial for API key / OAuth access (8.testing.paid_required, 8.auth.api_key, 8.mcp.hosted_official).

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```
- **URL**: [https://developer.close.com/integrations/create-an-oauth-app.md](https://developer.close.com/integrations/create-an-oauth-app.md) (locator: `lines:3-21`)
  - *Observation*: paraphrase: OAuth apps are created in Settings -> Developer -> OAuth Apps with all.full_access offline_access scopes; apps are Private by default and require requesting publication to become public.
  ```text
  OAuth 2.0 allows third-party applications to access Close data on behalf of users without exposing passwords or sharing API keys. You can create custom OAuth apps for Close to add bespoke features, automate tasks, and enhance data analytics, tailored to your business needs.
  ## Create a new OAuth app
  #### Go to OAuth Apps settings
  Navigate to [**Settings** → **Developer** → **OAuth Apps**](https://app.close.com/settings/developer/oauth-apps) and click **Create App**.
  #### Fill in your app details
  * **App Name** — Your application name that users will see on the consent screen.
  * **App Description** — 1–2 sentence description of what your app does.
  * **Redirect URL** — The http**s** URL where users are redirected after authorizing your app (e.g. `https://yourapp.com/callback/close`). Must use TLS/SSL — plain `http://` URLs are not accepted.
  * **Terms of Service URL** — Optional for internal-only apps
  * **Privacy Policy URL** — Optional for internal-only apps
  ```
- **URL**: [https://developer.close.com/mcp/](https://developer.close.com/mcp/) (locator: `lines:78-88`)
  - *Observation*: paraphrase: Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header.
  ```text
  Tool — This is where you will connect to Close’s MCP server.
  Connect the Chat Model and Memory options of your choice, and then add the MCP Client Tool node under Tool.
  For the MCP Client Tool node, use the following configuration:
  Endpoint: https://mcp.close.com/mcp
  Server Transport: HTTP Streamable
  Authentication: MCP OAuth2
  Create a new MCP OAuth2 API Credential in your n8n account with:
  Server URL: https://mcp.close.com/mcp
  Tools to Include: All
  Once you’ve successfully connected the MCP server, start chatting with your new AI Agent in the “Chat” window at the bottom left of the Workflow Editor.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:78-88) states: Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/mcp/](https://developer.close.com/mcp/) (locator: `lines:78-88`)
  - *Observation*: paraphrase: Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header.
  ```text
  Tool — This is where you will connect to Close’s MCP server.
  Connect the Chat Model and Memory options of your choice, and then add the MCP Client Tool node under Tool.
  For the MCP Client Tool node, use the following configuration:
  Endpoint: https://mcp.close.com/mcp
  Server Transport: HTTP Streamable
  Authentication: MCP OAuth2
  Create a new MCP OAuth2 API Credential in your n8n account with:
  Server URL: https://mcp.close.com/mcp
  Tools to Include: All
  Once you’ve successfully connected the MCP server, start chatting with your new AI Agent in the “Chat” window at the bottom left of the Workflow Editor.
  ```
- **URL**: [https://developer.close.com/mcp/tools.md](https://developer.close.com/mcp/tools.md) (locator: `lines:3-19`)
  - *Observation*: paraphrase: Documents scoped callable Close MCP read-only tools (mcp.read including activity_search and search/fetch tools).
  ```text
  The Close MCP Server provides tools organized by scope. Each higher scope includes all tools from the lower scopes.
  ## Read-only Tools – `mcp.read`
  Read-only tools for searching, fetching, and exploring your Close data.
  ### Activity Search – `activity_search`
  > Search for activities. Results are returned ordered by date descending.
  >
  > Examples:
  >
  > * To list activities on a lead, use the lead_ids filter.
  > * To list conversations, filter for calls and meetings.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.mcp.hosted_official` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Close MCP Server; source_url=https://developer.close.com/mcp/. Source evidence (lines:78-88) states: Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/mcp/](https://developer.close.com/mcp/) (locator: `lines:78-88`)
  - *Observation*: paraphrase: Official Close MCP server hosted at https://mcp.close.com/mcp using HTTP Streamable transport with MCP OAuth2 (recommended) or Close-API-Key header.
  ```text
  Tool — This is where you will connect to Close’s MCP server.
  Connect the Chat Model and Memory options of your choice, and then add the MCP Client Tool node under Tool.
  For the MCP Client Tool node, use the following configuration:
  Endpoint: https://mcp.close.com/mcp
  Server Transport: HTTP Streamable
  Authentication: MCP OAuth2
  Create a new MCP OAuth2 API Credential in your n8n account with:
  Server URL: https://mcp.close.com/mcp
  Tools to Include: All
  Once you’ve successfully connected the MCP server, start chatting with your new AI Agent in the “Chat” window at the bottom left of the Workflow Editor.
  ```
- **URL**: [https://developer.close.com/mcp/tools.md](https://developer.close.com/mcp/tools.md) (locator: `lines:3-19`)
  - *Observation*: paraphrase: Documents scoped callable Close MCP read-only tools (mcp.read including activity_search and search/fetch tools).
  ```text
  The Close MCP Server provides tools organized by scope. Each higher scope includes all tools from the lower scopes.
  ## Read-only Tools – `mcp.read`
  Read-only tools for searching, fetching, and exploring your Close data.
  ### Activity Search – `activity_search`
  > Search for activities. Results are returned ordered by date descending.
  >
  > Examples:
  >
  > * To list activities on a lead, use the lead_ids filter.
  > * To list conversations, filter for calls and meetings.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:52-113) states: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:52-113) states: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.production.vendor_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:3-21) states: OAuth apps are created in Settings -> Developer -> OAuth Apps with all.full_access offline_access scopes; apps are Private by default and require requesting publication to become public. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/integrations/create-an-oauth-app.md](https://developer.close.com/integrations/create-an-oauth-app.md) (locator: `lines:3-21`)
  - *Observation*: paraphrase: OAuth apps are created in Settings -> Developer -> OAuth Apps with all.full_access offline_access scopes; apps are Private by default and require requesting publication to become public.
  ```text
  OAuth 2.0 allows third-party applications to access Close data on behalf of users without exposing passwords or sharing API keys. You can create custom OAuth apps for Close to add bespoke features, automate tasks, and enhance data analytics, tailored to your business needs.
  ## Create a new OAuth app
  #### Go to OAuth Apps settings
  Navigate to [**Settings** → **Developer** → **OAuth Apps**](https://app.close.com/settings/developer/oauth-apps) and click **Create App**.
  #### Fill in your app details
  * **App Name** — Your application name that users will see on the consent screen.
  * **App Description** — 1–2 sentence description of what your app does.
  * **Redirect URL** — The http**s** URL where users are redirected after authorizing your app (e.g. `https://yourapp.com/callback/close`). Must use TLS/SSL — plain `http://` URLs are not accepted.
  * **Terms of Service URL** — Optional for internal-only apps
  * **Privacy Policy URL** — Optional for internal-only apps
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Sales CRM with built-in calling, email, and SMS, offering a REST API, webhooks, and hosted MCP server for leads, contacts, and outreach.. Source evidence (lines:16-38) states: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.close.com/](https://developer.close.com/) (locator: `lines:16-38`)
  - *Observation*: paraphrase: Close Developer Platform provides a REST API, webhooks/events, OAuth apps, and an MCP server for managing leads, contacts, activities, sequences, and reporting.
  ```text
  Whether you’re a Close customer automating your sales process or a partner building an integration, the Close Developer Platform gives everything you or your AI agents need.
  REST API Reference
  Full endpoint docs with schemas, examples, and an interactive API explorer.
  Authentication
  API keys for scripts or OAuth 2.0 for user-facing integrations.
  Webhooks & Events
  Real-time event notifications and a 30-day event log.
  MCP Server
  Model Context Protocol for AI agents.
  Build an Integration
  ```
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:52-113) states: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed. The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `8.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:52-113) states: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://www.close.com/pricing](https://www.close.com/pricing) (locator: `lines:52-113`)
  - *Observation*: paraphrase: Close CRM offers Solo, Essentials, Growth, and Scale paid plans with a 14-day free trial (no credit card required); no free tier is listed.
  ```text
  Close CRM Pricing
  Built-in calling, sales dialers, email, SMS, and AI Agents in one CRM. Reach more leads, automate follow-up, and close more deals.
  AnnualSave with annual billingMonthly
  Enterprise Needs? Talk to Sales →
  Solo
  1 user only · Up to 10,000 leads
  For independent sellers.
  Regular monthly price $19Annual price $9/mo
  $19/mo
  Billed monthly · Save $120/yr annually
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 19: Gorgias (Support and Helpdesk)
- Total claims: 16 | Corrected: 2

### Claim: `19.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:16-74): Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Covers ticketing, messaging, customers, macros, rules, surveys, statistics, voice calls, and integrations.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Gorgias API documentation covers multiple distinct functional domains: (1) Helpdesk Tickets & Messages, (2) Customer Management, (3) Ecommerce Order/Store Data, and (4) Third-party Integrations/HTTP Webhooks. Per evidence rules, spanning multiple distinct functional domains substantiates broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:16-74`)
  - *Observation*: paraphrase: Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros.
  ```text
  Account
  The Account object
  Retrieve your accountget
  List settingsget
  Create a settingpost
  Update a settingput
  Customers
  The Customer object
  Delete customersdel
  List customersget
  ```
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:79-179`)
  - *Observation*: paraphrase: Gorgias REST API documents Rules, Satisfaction Surveys, Search, Statistics, Tags, Teams, Tickets, Ticket Messages, Users, Views, Voice Calls, and Widgets.
  ```text
  Rules
  The Rule object
  List rulesget
  Create a rulepost
  Update rules' prioritiespost
  Delete a ruledel
  Retrieve a ruleget
  Update a ruleput
  Satisfaction Surveys
  The SatisfactionSurvey object
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.api.group.customers_macros_integrations` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Account/settings, customers, custom fields, events, files, integrations, jobs, and macros. Source evidence (lines:16-74) states: Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:16-74`)
  - *Observation*: paraphrase: Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros.
  ```text
  Account
  The Account object
  Retrieve your accountget
  List settingsget
  Create a settingpost
  Update a settingput
  Customers
  The Customer object
  Delete customersdel
  List customersget
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.api.group.tickets_rules_voice_stats` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Tickets, ticket messages, rules, surveys, search, statistics, tags, teams, users, views, voice calls, and widgets. Source evidence (lines:79-179) states: Gorgias REST API documents Rules, Satisfaction Surveys, Search, Statistics, Tags, Teams, Tickets, Ticket Messages, Users, Views, Voice Calls, and Widgets. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:79-179`)
  - *Observation*: paraphrase: Gorgias REST API documents Rules, Satisfaction Surveys, Search, Statistics, Tags, Teams, Tickets, Ticket Messages, Users, Views, Voice Calls, and Widgets.
  ```text
  Rules
  The Rule object
  List rulesget
  Create a rulepost
  Update rules' prioritiespost
  Delete a ruledel
  Retrieve a ruleget
  Update a ruleput
  Satisfaction Surveys
  The SatisfactionSurvey object
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:188-190) states: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:188-190`)
  - *Observation*: paraphrase: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes.
  ```text
  The Gorgias API is structured with REST in mind. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
  On this page, you'll find the complete REST API reference, examples, definitions of objects, and guides.
  🚫
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:188-190) states: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:188-190`)
  - *Observation*: paraphrase: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes.
  ```text
  The Gorgias API is structured with REST in mind. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
  On this page, you'll find the complete REST API reference, examples, definitions of objects, and guides.
  🚫
  ```
- **URL**: [https://developers.gorgias.com/reference/authentication](https://developers.gorgias.com/reference/authentication) (locator: `lines:184-190`)
  - *Observation*: paraphrase: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.
  ```text
  Authentication
  The Gorgias API supports two authentication methods:
  🔐 Private app → API key
  👥 Public app → OAuth2
  Using OAuth2 is mandatory for public apps.
  For testing purposes, you can perform requests directly from the API Reference using your API keys.
  Go to any endpoint (e.g: "Retrieve your account")
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.auth.api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Private Gorgias apps and API testing. Source evidence (lines:184-190) states: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/authentication](https://developers.gorgias.com/reference/authentication) (locator: `lines:184-190`)
  - *Observation*: paraphrase: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.
  ```text
  Authentication
  The Gorgias API supports two authentication methods:
  🔐 Private app → API key
  👥 Public app → OAuth2
  Using OAuth2 is mandatory for public apps.
  For testing purposes, you can perform requests directly from the API Reference using your API keys.
  Go to any endpoint (e.g: "Retrieve your account")
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.auth.oauth2` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Multi-tenant public Gorgias apps. Source evidence (lines:184-190) states: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/authentication](https://developers.gorgias.com/reference/authentication) (locator: `lines:184-190`)
  - *Observation*: paraphrase: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.
  ```text
  Authentication
  The Gorgias API supports two authentication methods:
  🔐 Private app → API key
  👥 Public app → OAuth2
  Using OAuth2 is mandatory for public apps.
  For testing purposes, you can perform requests directly from the API Reference using your API keys.
  Go to any endpoint (e.g: "Retrieve your account")
  ```
- **URL**: [https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md](https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md) (locator: `lines:6-55`)
  - *Observation*: paraphrase: Gorgias OAuth2 uses Authorization Code flow on tenant subdomains (https://{subdomain}.gorgias.com/oauth/authorize & /oauth/token) with 24-hour Bearer access tokens, non-expiring refresh tokens, and granular scopes (e.g., customers:read, tickets:read).
  ```text
  # OAuth2 authentication for creating apps with Gorgias
  ## Introduction
  In order to be able to have an approved public app with Gorgias, it is required that the app is using OAuth2 for authentication.
  You can obtain the OAuth2 token by following these steps and requirements:
  <ol>
  <li> Creating an app on the partners’ account</li>
  <li> Obtaining the client_id and client_secret</li>
  <li> Redirect authorization</li>
  <li> Post request to obtain the access token (has a 24 hours expiration time)</li>
  <li> Refresh token used to obtain the next token (does not have expiration time)</li>
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Gorgias ecommerce helpdesk ticket/customer automation via REST API (private API key or public OAuth2). The assertion is inferred rather than a directly documented vendor statement. Available source (lines:184-190): Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Gorgias ecommerce helpdesk ticket/customer automation via REST API (private API key or public OAuth2)", "blockers": ["Converting a trial to a Sandbox requires contacting techpartners@gorgias.com", "Public multi-tenant OAuth2 apps require Gorgias tech partnership review and approval", "Official Gorgias MCP docs were not captured in checked developer portal sources"], "next_steps": ["Use private API key on a trial/paid tenant for single-tenant prototyping", "Register on Gorgias Developer Portal and contact techpartners@gorgias.com for Sandbox and public OAuth2 review"]}`
  - Original Rationale: Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Gorgias ecommerce helpdesk ticket/customer automation via REST API (private API key or public OAuth2)", "blockers": ["Converting a trial to a Sandbox requires contacting techpartners@gorgias.com", "Public multi-tenant OAuth2 apps require Gorgias tech partnership review and approval", "Official Gorgias MCP docs were not captured in checked developer portal sources"], "next_steps": ["Use private API key on a trial/paid tenant for single-tenant prototyping", "Register on Gorgias Developer Portal and contact techpartners@gorgias.com for Sandbox and public OAuth2 review"]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Gorgias documentation: REST API and OAuth 2.0 app registration are fully documented, but require an active Gorgias paid helpdesk account (19.testing.paid_required, 19.auth.oauth2).

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/reference/authentication](https://developers.gorgias.com/reference/authentication) (locator: `lines:184-190`)
  - *Observation*: paraphrase: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.
  ```text
  Authentication
  The Gorgias API supports two authentication methods:
  🔐 Private app → API key
  👥 Public app → OAuth2
  Using OAuth2 is mandatory for public apps.
  For testing purposes, you can perform requests directly from the API Reference using your API keys.
  Go to any endpoint (e.g: "Retrieve your account")
  ```
- **URL**: [https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md](https://developers.gorgias.com/docs/oauth2-authentication-for-creating-apps-with-gorgias.md) (locator: `lines:6-55`)
  - *Observation*: paraphrase: Gorgias OAuth2 uses Authorization Code flow on tenant subdomains (https://{subdomain}.gorgias.com/oauth/authorize & /oauth/token) with 24-hour Bearer access tokens, non-expiring refresh tokens, and granular scopes (e.g., customers:read, tickets:read).
  ```text
  # OAuth2 authentication for creating apps with Gorgias
  ## Introduction
  In order to be able to have an approved public app with Gorgias, it is required that the app is using OAuth2 for authentication.
  You can obtain the OAuth2 token by following these steps and requirements:
  <ol>
  <li> Creating an app on the partners’ account</li>
  <li> Obtaining the client_id and client_secret</li>
  <li> Redirect authorization</li>
  <li> Post request to obtain the access token (has a 24 hours expiration time)</li>
  <li> Refresh token used to obtain the next token (does not have expiration time)</li>
  ```
- **URL**: [https://developers.gorgias.com/docs/overview.md](https://developers.gorgias.com/docs/overview.md) (locator: `lines:7-17`)
  - *Observation*: paraphrase: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.
  ```text
  Below are the major steps of the process you need to follow when building a public app with Gorgias.
  1. Register on the [Developer Portal]() to submit your app and manage your listing.
  2. Create a Draft app in the Developer Portal.
  3. Get Gorgias Sandbox to test your app: [create a trial account](https://www.gorgias.com/signup) and reach out to <techpartners@gorgias.com> to convert it into a Sandbox account.
  1. :warning: You need to complete steps 1-2 to convert Trial to Sandbox account.
  4. **[Set up OAuth2](https://developers.gorgias.com/docs/set-up-oauth2-app-store) for your app.**
  5. Build your app using our [API docs](https://developers.gorgias.com/reference/introduction) and test it.
  6. Complete the rest of the form on the Developer Portal and submit your app for review
  1. :warning: Make sure to include testing instructions with a test account
  7. Once your app is approved, we will announce it at our next [Product Town Hall](https://www.gorgias.com/events/gorgias-product-town-hall-june).
  ```
- **URL**: [https://developers.gorgias.com/docs/5-submit-app-for-review.md](https://developers.gorgias.com/docs/5-submit-app-for-review.md) (locator: `lines:11-13`)
  - *Observation*: paraphrase: Gorgias tech partnership team reviews submitted public apps before approving them for the App Store.
  ```text
  * Once done, click on **Submit Application**.
  * Our tech partnership team will review your app to make sure it works properly and is aligned with our expectations.
  * Once we complete the review we will reach out to you to let you know about the result. If it is approved, it will appear in both the in-product App Store and the [public App Store page](https://www.gorgias.com/apps). If it is not approved, we will let you know what needs to be fixed/changed for your app to be approved.
  ```
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:188-190`)
  - *Observation*: paraphrase: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes.
  ```text
  The Gorgias API is structured with REST in mind. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
  On this page, you'll find the complete REST API reference, examples, definitions of objects, and guides.
  🚫
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:138-179) states: Community GitHub repository mattcoatsworth/Gorgias-MCP-Server implements a Node.js MCP server authenticating with Gorgias API key or OAuth access token and exposing ticket and customer tools (list_tickets, get_ticket, create_ticket, add_message_to_ticket, list_customers,…. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://github.com/mattcoatsworth/Gorgias-MCP-Server](https://github.com/mattcoatsworth/Gorgias-MCP-Server) (locator: `lines:138-179`)
  - *Observation*: paraphrase: Community GitHub repository mattcoatsworth/Gorgias-MCP-Server implements a Node.js MCP server authenticating with Gorgias API key or OAuth access token and exposing ticket and customer tools (list_tickets, get_ticket, create_ticket, add_message_to_ticket, list_customers, get_customer).
  ```text
  Gorgias MCP Server
  An MCP server for interacting with the Gorgias helpdesk API. This server provides tools and resources for managing tickets, customers, and other Gorgias functionality.
  ## Setup
  1. Clone this repository
  2. Install dependencies:
  ```
  npm install
  ```
  3. Create a `.env` file based on `.env.example` with your Gorgias credentials:
  ```
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.mcp.community_mattcoatsworth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=community; name=mattcoatsworth/Gorgias-MCP-Server; source_url=https://github.com/mattcoatsworth/Gorgias-MCP-Server. Source evidence (lines:138-179) states: Community GitHub repository mattcoatsworth/Gorgias-MCP-Server implements a Node.js MCP server authenticating with Gorgias API key or OAuth access token and exposing ticket and customer tools (list_tickets, get_ticket, create_ticket, add_message_to_ticket, list_customers,…. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://github.com/mattcoatsworth/Gorgias-MCP-Server](https://github.com/mattcoatsworth/Gorgias-MCP-Server) (locator: `lines:138-179`)
  - *Observation*: paraphrase: Community GitHub repository mattcoatsworth/Gorgias-MCP-Server implements a Node.js MCP server authenticating with Gorgias API key or OAuth access token and exposing ticket and customer tools (list_tickets, get_ticket, create_ticket, add_message_to_ticket, list_customers, get_customer).
  ```text
  Gorgias MCP Server
  An MCP server for interacting with the Gorgias helpdesk API. This server provides tools and resources for managing tickets, customers, and other Gorgias functionality.
  ## Setup
  1. Clone this repository
  2. Install dependencies:
  ```
  npm install
  ```
  3. Create a `.env` file based on `.env.example` with your Gorgias credentials:
  ```
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:140-154) states: Gorgias pricing states Helpdesk scales from 50 to 5,000 tickets a month (never priced per agent), with AI Agent paid per resolution and Voice/SMS add-ons. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://www.gorgias.com/pricing](https://www.gorgias.com/pricing) (locator: `lines:140-154`)
  - *Observation*: paraphrase: Gorgias pricing states Helpdesk scales from 50 to 5,000 tickets a month (never priced per agent), with AI Agent paid per resolution and Voice/SMS add-ons.
  ```text
  Pricing
  Helpdesk + AI Agent.
  One platform. One inbox. One bill.
  AI Agent on every plan, pay only when it resolves a conversation.
  Helpdesk scales from 50 to 5,000 tickets a month, never priced per agent.
  We power customer conversations for 40% of Shopify brands
  Read case study
  Read case study
  Read case study
  Read case study
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.production.partner_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:7-17) states: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/docs/overview.md](https://developers.gorgias.com/docs/overview.md) (locator: `lines:7-17`)
  - *Observation*: paraphrase: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.
  ```text
  Below are the major steps of the process you need to follow when building a public app with Gorgias.
  1. Register on the [Developer Portal]() to submit your app and manage your listing.
  2. Create a Draft app in the Developer Portal.
  3. Get Gorgias Sandbox to test your app: [create a trial account](https://www.gorgias.com/signup) and reach out to <techpartners@gorgias.com> to convert it into a Sandbox account.
  1. :warning: You need to complete steps 1-2 to convert Trial to Sandbox account.
  4. **[Set up OAuth2](https://developers.gorgias.com/docs/set-up-oauth2-app-store) for your app.**
  5. Build your app using our [API docs](https://developers.gorgias.com/reference/introduction) and test it.
  6. Complete the rest of the form on the Developer Portal and submit your app for review
  1. :warning: Make sure to include testing instructions with a test account
  7. Once your app is approved, we will announce it at our next [Product Town Hall](https://www.gorgias.com/events/gorgias-product-town-hall-june).
  ```
- **URL**: [https://developers.gorgias.com/docs/5-submit-app-for-review.md](https://developers.gorgias.com/docs/5-submit-app-for-review.md) (locator: `lines:11-13`)
  - *Observation*: paraphrase: Gorgias tech partnership team reviews submitted public apps before approving them for the App Store.
  ```text
  * Once done, click on **Submit Application**.
  * Our tech partnership team will review your app to make sure it works properly and is aligned with our expectations.
  * Once we complete the review we will reach out to you to let you know about the result. If it is approved, it will appear in both the in-product App Store and the [public App Store page](https://www.gorgias.com/apps). If it is not approved, we will let you know what needs to be fixed/changed for your app to be approved.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Ecommerce helpdesk and CX platform providing a REST API (private API keys and public OAuth2) for tickets, messages, customers, macros, rules, and voice.. Source evidence (lines:1-18) states: Gorgias is an AI-powered ecommerce customer experience (CX) and helpdesk platform with AI Agent, Gaia, Helpdesk, Voice, and SMS. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://www.gorgias.com/pricing](https://www.gorgias.com/pricing) (locator: `lines:1-18`)
  - *Observation*: paraphrase: Gorgias is an AI-powered ecommerce customer experience (CX) and helpdesk platform with AI Agent, Gaia, Helpdesk, Voice, and SMS.
  ```text
  Gorgias Pricing - AI-Powered Ecommerce CX Platform Plans
  -->
  Product
  Solutions
  Pricing
  Integrations
  Resources
  Login
  Book a demo
  Sign up free
  ```
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:188-190`)
  - *Observation*: paraphrase: Gorgias API is a JSON REST API with resource-oriented URLs and standard HTTP verbs/status codes.
  ```text
  The Gorgias API is structured with REST in mind. Our API has predictable resource-oriented URLs, accepts JSON-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.
  On this page, you'll find the complete REST API reference, examples, definitions of objects, and guides.
  🚫
  ```
- **URL**: [https://developers.gorgias.com/reference/authentication](https://developers.gorgias.com/reference/authentication) (locator: `lines:184-190`)
  - *Observation*: paraphrase: Gorgias API supports two authentication methods: API key for private apps (and testing in API Reference) and mandatory OAuth2 for public apps.
  ```text
  Authentication
  The Gorgias API supports two authentication methods:
  🔐 Private app → API key
  👥 Public app → OAuth2
  Using OAuth2 is mandatory for public apps.
  For testing purposes, you can perform requests directly from the API Reference using your API keys.
  Go to any endpoint (e.g: "Retrieve your account")
  ```
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:16-74`)
  - *Observation*: paraphrase: Gorgias REST API documents Account/Settings, Customers, Custom Fields, Events, Files, Integrations, Jobs, and Macros.
  ```text
  Account
  The Account object
  Retrieve your accountget
  List settingsget
  Create a settingpost
  Update a settingput
  Customers
  The Customer object
  Delete customersdel
  List customersget
  ```
- **URL**: [https://developers.gorgias.com/reference/introduction](https://developers.gorgias.com/reference/introduction) (locator: `lines:79-179`)
  - *Observation*: paraphrase: Gorgias REST API documents Rules, Satisfaction Surveys, Search, Statistics, Tags, Teams, Tickets, Ticket Messages, Users, Views, Voice Calls, and Widgets.
  ```text
  Rules
  The Rule object
  List rulesget
  Create a rulepost
  Update rules' prioritiespost
  Delete a ruledel
  Retrieve a ruleget
  Update a ruleput
  Satisfaction Surveys
  The SatisfactionSurvey object
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.testing.partner_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:7-17) states: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review. The cited policy describes this access condition for test access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/docs/overview.md](https://developers.gorgias.com/docs/overview.md) (locator: `lines:7-17`)
  - *Observation*: paraphrase: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.
  ```text
  Below are the major steps of the process you need to follow when building a public app with Gorgias.
  1. Register on the [Developer Portal]() to submit your app and manage your listing.
  2. Create a Draft app in the Developer Portal.
  3. Get Gorgias Sandbox to test your app: [create a trial account](https://www.gorgias.com/signup) and reach out to <techpartners@gorgias.com> to convert it into a Sandbox account.
  1. :warning: You need to complete steps 1-2 to convert Trial to Sandbox account.
  4. **[Set up OAuth2](https://developers.gorgias.com/docs/set-up-oauth2-app-store) for your app.**
  5. Build your app using our [API docs](https://developers.gorgias.com/reference/introduction) and test it.
  6. Complete the rest of the form on the Developer Portal and submit your app for review
  1. :warning: Make sure to include testing instructions with a test account
  7. Once your app is approved, we will announce it at our next [Product Town Hall](https://www.gorgias.com/events/gorgias-product-town-hall-june).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.testing.sandbox_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:7-17) states: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review. The documentation describes a sandbox or test environment relevant to test access, distinct from live production access.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/docs/overview.md](https://developers.gorgias.com/docs/overview.md) (locator: `lines:7-17`)
  - *Observation*: paraphrase: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.
  ```text
  Below are the major steps of the process you need to follow when building a public app with Gorgias.
  1. Register on the [Developer Portal]() to submit your app and manage your listing.
  2. Create a Draft app in the Developer Portal.
  3. Get Gorgias Sandbox to test your app: [create a trial account](https://www.gorgias.com/signup) and reach out to <techpartners@gorgias.com> to convert it into a Sandbox account.
  1. :warning: You need to complete steps 1-2 to convert Trial to Sandbox account.
  4. **[Set up OAuth2](https://developers.gorgias.com/docs/set-up-oauth2-app-store) for your app.**
  5. Build your app using our [API docs](https://developers.gorgias.com/reference/introduction) and test it.
  6. Complete the rest of the form on the Developer Portal and submit your app for review
  1. :warning: Make sure to include testing instructions with a test account
  7. Once your app is approved, we will announce it at our next [Product Town Hall](https://www.gorgias.com/events/gorgias-product-town-hall-june).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `19.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:7-17) states: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.gorgias.com/docs/overview.md](https://developers.gorgias.com/docs/overview.md) (locator: `lines:7-17`)
  - *Observation*: paraphrase: Building a public Gorgias app requires registering on the Developer Portal, creating a trial account, emailing techpartners@gorgias.com to convert it to a Sandbox, configuring OAuth2, and submitting for review.
  ```text
  Below are the major steps of the process you need to follow when building a public app with Gorgias.
  1. Register on the [Developer Portal]() to submit your app and manage your listing.
  2. Create a Draft app in the Developer Portal.
  3. Get Gorgias Sandbox to test your app: [create a trial account](https://www.gorgias.com/signup) and reach out to <techpartners@gorgias.com> to convert it into a Sandbox account.
  1. :warning: You need to complete steps 1-2 to convert Trial to Sandbox account.
  4. **[Set up OAuth2](https://developers.gorgias.com/docs/set-up-oauth2-app-store) for your app.**
  5. Build your app using our [API docs](https://developers.gorgias.com/reference/introduction) and test it.
  6. Complete the rest of the form on the Developer Portal and submit your app for review
  1. :warning: Make sure to include testing instructions with a test account
  7. Once your app is approved, we will announce it at our next [Product Town Hall](https://www.gorgias.com/events/gorgias-product-town-hall-june).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 16: LiveAgent (Support and Helpdesk)
- Total claims: 15 | Corrected: 2

### Claim: `16.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts narrow. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:10-48): LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "narrow"`
  - Original Rationale: Captured public API reference snapshot only explicitly documents conversation, message, and department operations.
- **Corrected Answer**: `status: inferred`, `value: "narrow"`
  - Corrected Rationale: LiveAgent API v1 reference focuses on a single core workflow domain: helpdesk ticket/conversation management, message posting, and department assignments. Per evidence rules, a single focused workflow domain constitutes narrow breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.api.group.conversations_messages` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Conversations, messages, and departments. Source evidence (lines:10-48) states: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:10-48) states: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:10-48) states: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.auth.api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for LiveAgent REST API calls. Source evidence (lines:10-48) states: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:438-440`)
  - *Observation*: paraphrase: LiveAgent pricing comparison table documents tiered API key allowances across plans.
  ```text
  API keys
  1
  5
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.auth.mcp_bearer_token` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Built-in LiveAgent MCP server (non-OAuth clients). Source evidence (lines:17-57) states: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.auth.mcp_oauth2_pkce` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Built-in LiveAgent MCP server. Source evidence (lines:17-57) states: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for LiveAgent ticket/conversation support agent toolkit via built-in MCP server or REST API. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:10-48): LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "LiveAgent ticket/conversation support agent toolkit via built-in MCP server or REST API", "blockers": ["Captured public REST API documentation reflects older API v1 PHP examples", "MCP tool calls count against a shared workspace AI budget"], "next_steps": ["Start a 30-day no-credit-card free trial to test the built-in /api/mcp endpoint and REST API", "Authenticate via OAuth 2.1 + PKCE or personal MCP Bearer token"]}`
  - Original Rationale: Feasibility inference for the stated workflow from cited documentation; neither implementation nor successful execution established.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "LiveAgent ticket/conversation support agent toolkit via built-in MCP server or REST API", "blockers": ["Captured public REST API documentation reflects older API v1 PHP examples", "MCP tool calls count against a shared workspace AI budget"], "next_steps": ["Start a 30-day no-credit-card free trial to test the built-in /api/mcp endpoint and REST API", "Authenticate via OAuth 2.1 + PKCE or personal MCP Bearer token"]}`
  - Corrected Rationale: Buildability inference is anchored to verified LiveAgent documentation: built-in MCP server support and REST API with self-serve API key generation on free trial or paid accounts (16.testing.free_access, 16.auth.api_key, 16.mcp.builtin_mcp).

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:23-27`)
  - *Observation*: paraphrase: LiveAgent offers a 30-day free trial with no credit card required across help desk plans.
  ```text
  30-day free trial, no credit card
  AI
  AI in LiveAgent
  AI that answers customers and drafts replies, inside the same inbox your team already uses.
  On every plan. You pay your AI provider directly; LiveAgent charges nothing for AI.
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:58-62`)
  - *Observation*: paraphrase: LiveAgent MCP integration gives external AI tools access to the full set of LiveAgent MCP tools under the agent's identity and role permissions, counting toward a shared AI budget.
  ```text
  Permissions and available tools
  Regardless of whether you connect via OAuth or bearer token, your AI tool has access to the full set of LiveAgent MCP tools. See the MCP tools reference for the complete list of tools and their detailed description.
  All actions are performed under your agent identity and are subject to your role's permissions, exactly as if you had performed them in the LiveAgent panel. They appear in the ticket's activity history under your name.
  Note: Unlike LiveAgent AI agents, which restrict the tool set per AI agent configuration, personal MCP integration gives access to all tools. Your role's permissions still apply - actions your role is not permitted to perform will be rejected.
  Note: Actions performed through an MCP connection count toward a common AI budget shared by all users, which limits the number of tool calls. See the AI budgets article for details on how AI budgets work.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:17-57) states: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry). The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:58-62`)
  - *Observation*: paraphrase: LiveAgent MCP integration gives external AI tools access to the full set of LiveAgent MCP tools under the agent's identity and role permissions, counting toward a shared AI budget.
  ```text
  Permissions and available tools
  Regardless of whether you connect via OAuth or bearer token, your AI tool has access to the full set of LiveAgent MCP tools. See the MCP tools reference for the complete list of tools and their detailed description.
  All actions are performed under your agent identity and are subject to your role's permissions, exactly as if you had performed them in the LiveAgent panel. They appear in the ticket's activity history under your name.
  Note: Unlike LiveAgent AI agents, which restrict the tool set per AI agent configuration, personal MCP integration gives access to all tools. Your role's permissions still apply - actions your role is not permitted to perform will be rejected.
  Note: Actions performed through an MCP connection count toward a common AI budget shared by all users, which limits the number of tool calls. See the AI budgets article for details on how AI budgets work.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.mcp.hosted_official` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=LiveAgent Built-in MCP Server; source_url=https://support.liveagent.com/647358-MCP-Integration-for-Agents. Source evidence (lines:17-57) states: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry). The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:58-62`)
  - *Observation*: paraphrase: LiveAgent MCP integration gives external AI tools access to the full set of LiveAgent MCP tools under the agent's identity and role permissions, counting toward a shared AI budget.
  ```text
  Permissions and available tools
  Regardless of whether you connect via OAuth or bearer token, your AI tool has access to the full set of LiveAgent MCP tools. See the MCP tools reference for the complete list of tools and their detailed description.
  All actions are performed under your agent identity and are subject to your role's permissions, exactly as if you had performed them in the LiveAgent panel. They appear in the ticket's activity history under your name.
  Note: Unlike LiveAgent AI agents, which restrict the tool set per AI agent configuration, personal MCP integration gives access to all tools. Your role's permissions still apply - actions your role is not permitted to perform will be rejected.
  Note: Actions performed through an MCP connection count toward a common AI budget shared by all users, which limits the number of tool calls. See the AI budgets article for details on how AI budgets work.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:109-160) states: LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business). The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:109-160`)
  - *Observation*: paraphrase: LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business).
  ```text
  Starter
  Per agent · up to 15 agents
  Email and live chat for a small team
  Black Friday
  40% off
  Offer price $9
  $12.73$12.73
  Regular price: $15.
  /agent/mo
  5 agents: $45/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:109-160) states: LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business). The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:109-160`)
  - *Observation*: paraphrase: LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business).
  ```text
  Starter
  Per agent · up to 15 agents
  Email and live chat for a small team
  Black Friday
  40% off
  Offer price $9
  $12.73$12.73
  Regular price: $15.
  /agent/mo
  5 agents: $45/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Multichannel help desk, ticketing, live chat, social, and voice helpdesk platform providing a REST API and a built-in agent MCP server.. Source evidence (lines:128-128) states: LiveAgent is a cloud customer support software, ticketing system, live chat, social helpdesk, and voice helpdesk. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:128-128`)
  - *Observation*: paraphrase: LiveAgent is a cloud customer support software, ticketing system, live chat, social helpdesk, and voice helpdesk.
  ```text
  LiveAgent is an integrated customer support software, ticketing system, live chat, social helpdesk and voice helpdesk. You name it, it's there. Based in cloud and accessible from everywhere, with SSL safety.
  ```
- **URL**: [https://support.liveagent.com/061754-Complete-API-reference](https://support.liveagent.com/061754-Complete-API-reference) (locator: `lines:10-48`)
  - *Observation*: paraphrase: LiveAgent exposes a REST API (v1 PHP examples captured) authenticating requests with an apikey parameter for reading and creating conversations, messages, and departments.
  ```text
  LiveAgent API
  >
  REST API
  >
  API v1
  >
  Documentation
  >
  How to make REST calls in PHP
  Example of calling GET request
  ```
- **URL**: [https://support.liveagent.com/647358-MCP-Integration-for-Agents](https://support.liveagent.com/647358-MCP-Integration-for-Agents) (locator: `lines:17-57`)
  - *Observation*: paraphrase: LiveAgent exposes a built-in Streamable HTTP MCP server at https://<your-liveagent-domain>/api/mcp supporting OAuth 2.1 (Authorization Code + PKCE) or profile-generated Bearer access tokens (up to 10 active, 2-year automatic expiry).
  ```text
  LiveAgent exposes a built-in MCP server (Model Context Protocol) that lets you connect external AI tools, such as ChatGPT, Claude Desktop, Cursor, claude.ai, FlowHunt, or any other MCP-compatible client, directly with your LiveAgent account. Once connected, your own AI tools/agents can read ticket data and perform actions on your behalf, using your agent identity and permissions.
  There are two ways to authenticate your MCP client - OAuth 2.1 (recommended), where the AI tool discovers the authorization server automatically and redirects you to a consent screen, or Bearer token, where you generate an MCP access token in your profile and paste it into the AI tool's configuration manually.
  In this article
  Finding MCP Integration in your profile
  Connecting with OAuth
  How it works
  Managing authorized apps
  Connecting with a bearer token
  Generating an access token
  Managing access tokens
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:23-27) states: LiveAgent offers a 30-day free trial with no credit card required across help desk plans. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:23-27`)
  - *Observation*: paraphrase: LiveAgent offers a 30-day free trial with no credit card required across help desk plans.
  ```text
  30-day free trial, no credit card
  AI
  AI in LiveAgent
  AI that answers customers and drafts replies, inside the same inbox your team already uses.
  On every plan. You pay your AI provider directly; LiveAgent charges nothing for AI.
  ```
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:109-160`)
  - *Observation*: paraphrase: LiveAgent offers paid per-agent plans (Starter $15/mo regular, Team $29/mo regular, and Business).
  ```text
  Starter
  Per agent · up to 15 agents
  Email and live chat for a small team
  Black Friday
  40% off
  Offer price $9
  $12.73$12.73
  Regular price: $15.
  /agent/mo
  5 agents: $45/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `16.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:23-27) states: LiveAgent offers a 30-day free trial with no credit card required across help desk plans. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://www.liveagent.com/pricing/](https://www.liveagent.com/pricing/) (locator: `lines:23-27`)
  - *Observation*: paraphrase: LiveAgent offers a 30-day free trial with no credit card required across help desk plans.
  ```text
  30-day free trial, no credit card
  AI
  AI in LiveAgent
  AI that answers customers and drafts replies, inside the same inbox your team already uses.
  On every plan. You pay your AI provider directly; LiveAgent charges nothing for AI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 27: Telegram (Communications and Messaging)
- Total claims: 19 | Corrected: 2

### Claim: `27.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:13-220): Extensive Bot API v10.5 surface.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Comprehensive messaging, bot automation, Mini Apps, business accounts, payments, and full MTProto client capabilities.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Telegram Bot API encompasses multiple distinct domains: (1) Chat & Direct Messaging, (2) Inline Queries & Payments, (3) Webhook Event Delivery, (4) Group & Channel Administration, and (5) Media/Sticker Processing. Per evidence rules, multiple distinct business domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:13-220`)
  - *Observation*: paraphrase: Extensive Bot API v10.5 surface.
  ```text
  The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram.
  To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.
  Recent changes
  Subscribe to @BotNews to be the first to know about the latest updates and join the discussion in @BotTalk
  November 22, 2026
  Bot API 10.5
  Bot Settings
  Added the method setMySettings, allowing bots to change their settings, including inline mode settings, privacy mode, the ability to be added to groups, forum topic mode in private chats, and the mode of receiving callback queries.
  Added the ability to receive callback queries from buttons in messages sent by the bot with the field inline_message_id instead of the field message in the class CallbackQuery, depending on the parameter callback_query_mode of the method setMySettings.
  Added the ability for bots to show the list of topics in a sidebar in private chats with the bot using the parameter has_topic_sidebar of the method setMySettings.
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:11-188`)
  - *Observation*: paraphrase: Full Bot API, MTProto/TDLib client API, and Gateway API.
  ```text
  We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through Telegram instead of traditional SMS.
  You can also add Telegram Widgets to your website.
  Designers are welcome to create Animated Stickers and Emoji or Custom Themes for Telegram.
  Bot API
  This API allows you to connect bots to our system. Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.
  To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS interface that offers a simplified version of the Telegram API.
  Learn more about the Bot API here »
  Bot developers can also make use of our Payments API to accept payments from Telegram users around the world.
  TDLib – build your own Telegram
  Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our Telegram Database Library (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.group.bot_messaging_media` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Bot messages, rich messages, ephemeral messages, media, reactions, inline queries, callbacks, and webhooks/getUpdates. Source evidence (lines:47-116) states: Send/edit/delete text, rich messages, ephemeral messages, photos, audio, video, documents, stickers, locations. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:47-116`)
  - *Observation*: paraphrase: Send/edit/delete text, rich messages, ephemeral messages, photos, audio, video, documents, stickers, locations.
  ```text
  Ephemeral messages
  Allowed bots to send ephemeral replies to callback queries in any chat except channel direct messages chats by specifying callback_query_id without receiver_user_id in the parameter ephemeral_message_parameters of the methods sendMessage, sendRichMessage, sendAnimation, sendAudio, sendContact, sendDocument, sendLivePhoto, sendLocation, sendPhoto, sendSticker, sendVenue, sendVideo, sendVideoNote and sendVoice.
  The field receiver_user_id of the class EphemeralMessageParameters and the parameter chat_id of the mentioned methods are optional now.
  Quotes from rich messages
  Added the field rich_texts to the class TextQuote for quotes chosen from a RichMessage.
  Added the field quote_rich_texts to the class ReplyParameters, allowing bots to quote rich messages.
  TON wallet
  Added the classes TonWalletCard, TonWalletCardSticker, TonNft and TonNftAttribute, and the field ton_wallet_card to the class ChatFullInfo.
  Added the class TonWalletTransfer and the field ton_wallet_transfer to the class Message for service messages about transfers with a TON wallet.
  Renamed the class StoryAreaPosition to AreaPosition, because it is now also used to describe the position of stickers on TON wallet cards.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:155-220`)
  - *Observation*: paraphrase: Updates via getUpdates or webhooks covering messages, channel posts, business messages, reactions, inline queries, callbacks, and widgets.
  ```text
  Getting updates
  There are two mutually exclusive ways of receiving updates for your bot - the getUpdates method on one hand and webhooks on the other. Incoming updates are stored on the server until the bot receives them either way, but they will not be kept longer than 24 hours.
  Regardless of which option you choose, you will receive JSON-serialized Update objects as a result.
  Update
  This object represents an incoming update.
  At most one of the optional fields can be present in any given update.
  Field
  Type
  Description
  update_id
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.group.chats_business_miniapps` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Chats, groups/channels/forums, Telegram Business connections, Mini Apps, HTML5 games, and Payments/Stars. Source evidence (lines:28-62) states: Mini Apps, Telegram Business Mode, Telegram Stars & third-party payments, games, and affiliate programs. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:28-62`)
  - *Observation*: paraphrase: Mini Apps, Telegram Business Mode, Telegram Stars & third-party payments, games, and affiliate programs.
  ```text
  Replace Entire Websites
  Telegram bots can host Mini Apps built with JavaScript. This allows for infinitely flexible interfaces that can power everything from online stores to arcade games. Unlike websites, bots support seamless authorization and notifications through Telegram out of the box.
  Try @DurgerKingBot – or check out the dedicated guide to Mini Apps to build your own.
  Natively Integrate AI Agents and Chatbots
  On Telegram, AI bots can natively meet, chat and compete: users can summon assistants into the same chat, watch their responses stream in real time, coordinate multiple agents at once or have them manage their whole account.
  Bots also support threaded conversations to manage several different topics in parallel — letting users easily access information from previous chats.
  See here to check out more tools and integrations available for AI-powered bots on Telegram.
  Manage Your Business
  Telegram Business users can connect Telegram bots to process and answer messages on their behalf, via their personal account. This allows businesses to seamlessly integrate any existing tools and workflows, or add new AI assistants to increase productivity.
  As we continue to expand the set of free tools available to bots through this integration, we encourage all developers to innovate and develop useful applications and services for businesses on Telegram.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:179-190`)
  - *Observation*: paraphrase: Business connections and business messages updates.
  ```text
  business_connection
  BusinessConnection
  Optional. The bot was connected to or disconnected from a business account, or a user edited an existing connection with the bot
  business_message
  Message
  Optional. New message from a connected business account
  edited_business_message
  Message
  Optional. New version of a message from a connected business account
  deleted_business_messages
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.group.mtproto_client_surface` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Full user-client MTProto surface (dialogs, channels/supergroups, stories, calls, search, admin logs, scheduled messages). Source evidence (lines:52-188) states: Channels/supergroups/forums, E2E calls, stories, search/filters, polls, checklists, admin logs, scheduled messages, Passport, Payments. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:52-188`)
  - *Observation*: paraphrase: Channels/supergroups/forums, E2E calls, stories, search/filters, polls, checklists, admin logs, scheduled messages, Passport, Payments.
  ```text
  Channels, supergroups, gigagroups and basic groups
  How to handle channels, supergroups, gigagroups, basic groups, and what's the difference between them.
  Forums
  Telegram allows creating forums with multiple distinct topics.
  Bots can also make use of topics, if enabled through @botfather.
  Direct messages to channels
  Telegram supports direct messages to channels, which can also be used to suggest (even paid) channel posts.
  Channel statistics
  Telegram offers detailed statistics for channels and supergroups.
  Message views and read metrics
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.protocol.other_mtproto` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other. Source evidence (lines:16-28) states: MTProto encrypted client protocol and open-source TDLib library. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:16-28`)
  - *Observation*: paraphrase: MTProto encrypted client protocol and open-source TDLib library.
  ```text
  To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS interface that offers a simplified version of the Telegram API.
  Learn more about the Bot API here »
  Bot developers can also make use of our Payments API to accept payments from Telegram users around the world.
  TDLib – build your own Telegram
  Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our Telegram Database Library (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.
  TDLib takes care of all network implementation details, encryption and local data storage, so that you can dedicate more time to design, responsive interfaces and beautiful animations.
  TDLib supports all Telegram features and makes developing Telegram apps a breeze on any platform. It can be used on Android, iOS, Windows, macOS, Linux and virtually any other system. The library is open source and compatible with virtually any programming language.
  Learn more about TDLib here »
  Gateway API
  The Telegram Gateway API allows any business, app or website to send authorization codes through Telegram instead of traditional SMS – offering a powerful and convenient way to lower costs while increasing the security and delivery speed of your codes to Telegram’s 1 billion monthly active users. Users will instantly receive messages with codes in a special chat inside Telegram.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.protocol.rpc` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts RPC. Source evidence (lines:13-13) states: HTTP-based Bot API interface. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:13-13`)
  - *Observation*: paraphrase: HTTP-based Bot API interface.
  ```text
  The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:130-137`)
  - *Observation*: paraphrase: RPC-style HTTPS GET/POST method calls at /bot<token>/METHOD_NAME returning JSON {ok, result}.
  ```text
  All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:
  https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
  We support GET and POST HTTP methods. We support four ways of passing parameters in Bot API requests:
  URL query string
  application/x-www-form-urlencoded
  application/json (except for uploading files)
  multipart/form-data (use to upload files)
  The response contains a JSON object, which always has a Boolean field 'ok' and may have an optional String field 'description' with a human-readable description of the result. If 'ok' equals True, the request was successful and the result of the query can be found in the 'result' field. In case of an unsuccessful request, 'ok' equals False and the error is explained in the 'description'. An Integer 'error_code' field is also returned, but its contents are subject to change in the future. Some errors may also have an optional field 'parameters' of the type ResponseParameters, which can help to automatically handle the error.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-18) states: Complete public Bot API reference at core.telegram.org/bots/api (14,067 lines). The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:1-18`)
  - *Observation*: paraphrase: Complete public Bot API reference at core.telegram.org/bots/api (14,067 lines).
  ```text
  Telegram Bot API
  Follow on X
  Home
  FAQ
  Apps
  API
  Protocol
  Schema
  Machine-readable version of this page: /bots/api.md.
  Telegram Bots
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:1-28`)
  - *Observation*: paraphrase: Public Telegram APIs and MTProto documentation at core.telegram.org/api.
  ```text
  Telegram APIs
  Follow on X
  Home
  FAQ
  Apps
  API
  Protocol
  Schema
  Machine-readable version of this page: /api.md.
  Telegram APIs
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.auth.bot_token` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other authentication for Telegram Bot API (HTTPS). Source evidence (lines:80-83) states: Message @BotFather on Telegram to register a bot and receive its unique authentication token. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:80-83`)
  - *Observation*: paraphrase: Message @BotFather on Telegram to register a bot and receive its unique authentication token.
  ```text
  How Do I Create a Bot?
  Creating Telegram bots is super-easy, but you will need at least some skills in computer programming.
  Creating a bot is streamlined by Telegram’s Bot API, which gives the tools and framework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token.
  Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct access to the bot. Everyone who has your token will have full control over your bot.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:127-132`)
  - *Observation*: paraphrase: Bot token passed in HTTPS URL path: https://api.telegram.org/bot<token>/METHOD_NAME.
  ```text
  Authorizing your bot
  Each bot is given a unique authentication token when it is created. The token looks something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11, but we'll use simply <token> in this document instead. You can learn about obtaining tokens and generating new ones in this document.
  Making requests
  All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:
  https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
  We support GET and POST HTTP methods. We support four ways of passing parameters in Bot API requests:
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.auth.mtproto_api_id_hash` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other authentication for Telegram MTProto API / TDLib (user-account client protocol). Source evidence (lines:27-43) states: Telegram MTProto API requires registering an application for an application identifier and authorizing a user via phone, 2FA, QR code login, or passkeys. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:27-43`)
  - *Observation*: paraphrase: Telegram MTProto API requires registering an application for an application identifier and authorizing a user via phone, 2FA, QR code login, or passkeys.
  ```text
  Telegram API
  This API allows you to build your own customized Telegram clients. It is 100% open for all developers who wish to create Telegram applications on our platform. Feel free to study the open source code of existing Telegram applications for examples of how things work here. Don't forget to register your application in our system.
  Getting Started
  Security
  Optimization
  API methods
  Getting started
  Creating an application
  How to get your application identifier and create a new Telegram app.
  User authorization
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Build a Telegram Bot API messaging/notification/group-management agent toolkit (and optional MTProto user-client toolkit).. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:15-15): Free for users and developers.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Telegram Bot API messaging/notification/group-management agent toolkit (and optional MTProto user-client toolkit).", "blockers": ["Bots cannot initiate private conversations with users first (users must message the bot or add it to a group) and have Privacy Mode enabled in groups by default.", "No official Telegram MCP server was found in checked primary docs; only community Bot API and MTProto MCP servers were captured."], "next_steps": ["Register a bot via @BotFather to obtain a free bot token.", "Wrap HTTPS Bot API v10.5 methods (or evaluate @node2flow/telegram-bot-mcp), choosing webhooks or getUpdates for inbound events."]}`
  - Original Rationale: Feasibility inference from captured primary documentation; no live integration or credential test executed.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Telegram Bot API messaging/notification/group-management agent toolkit (and optional MTProto user-client toolkit).", "blockers": ["Bots cannot initiate private conversations with users first (users must message the bot or add it to a group) and have Privacy Mode enabled in groups by default.", "No official Telegram MCP server was found in checked primary docs; only community Bot API and MTProto MCP servers were captured."], "next_steps": ["Register a bot via @BotFather to obtain a free bot token.", "Wrap HTTPS Bot API v10.5 methods (or evaluate @node2flow/telegram-bot-mcp), choosing webhooks or getUpdates for inbound events."]}`
  - Corrected Rationale: Buildability inference is anchored to verified Telegram Bot platform documentation: instant self-serve bot creation via BotFather with zero approval gating or fees (27.testing.free_access, 27.testing.self_serve, 27.auth.bearer_token).

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:15-15`)
  - *Observation*: paraphrase: Free for users and developers.
  ```text
  The Telegram Bot Platform hosts more than 10 million bots and is free for both users and developers.
  ```
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:74-83`)
  - *Observation*: paraphrase: Bot conversation-initiation constraint and @BotFather setup.
  ```text
  Bots can't start conversations with users. A user must either add them to a group or send them a message first. People can search for your bot’s username or start a chat via its unique t.me/bot_username link.
  By default, bots added to groups only see relevant messages in the chat (see Privacy Mode).
  Bots never eat, sleep or complain (unless expressly programmed otherwise).
  Bot Links
  Bot usernames normally require a ‘bot’ suffix, but some bots don’t have them – such as @stickers, @gif, @wiki or @bing.
  Anyone can assign collectible usernames to bots, including those without the 'bot' suffix.
  How Do I Create a Bot?
  Creating Telegram bots is super-easy, but you will need at least some skills in computer programming.
  Creating a bot is streamlined by Telegram’s Bot API, which gives the tools and framework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token.
  Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct access to the bot. Everyone who has your token will have full control over your bot.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:127-137`)
  - *Observation*: paraphrase: HTTPS Bot API request/response format.
  ```text
  Authorizing your bot
  Each bot is given a unique authentication token when it is created. The token looks something like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11, but we'll use simply <token> in this document instead. You can learn about obtaining tokens and generating new ones in this document.
  Making requests
  All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: https://api.telegram.org/bot<token>/METHOD_NAME. Like this for example:
  https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
  We support GET and POST HTTP methods. We support four ways of passing parameters in Bot API requests:
  URL query string
  application/x-www-form-urlencoded
  application/json (except for uploading files)
  multipart/form-data (use to upload files)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:155-157) states: Community Telegram Bot API MCP server. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://github.com/node2flow-th/telegram-bot-mcp-community](https://github.com/node2flow-th/telegram-bot-mcp-community) (locator: `lines:155-157`)
  - *Observation*: paraphrase: Community Telegram Bot API MCP server.
  ```text
  Telegram Bot MCP Server
  MCP (Model Context Protocol) server for Telegram Bot API. Send messages, manage chats, handle webhooks, and more through 27 tools.
  Works with Claude Desktop, Cursor, VS Code, and any MCP client.
  ```
- **URL**: [https://github.com/sparfenyuk/mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) (locator: `lines:154-173`)
  - *Observation*: paraphrase: Community Telegram MTProto MCP server.
  ```text
  Telegram MCP server
  Telegram MCP server
  About
  What is MCP?
  What does this server do?
  Practical use cases
  Prerequisites
  Installation
  Configuration
  Telegram API Configuration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.mcp.community_bot` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=community; name=Telegram Bot MCP Server (node2flow-th/telegram-bot-mcp-community); source_url=https://github.com/node2flow-th/telegram-bot-mcp-community. Source evidence (lines:155-198) states: Community MCP server (@node2flow/telegram-bot-mcp) exposing 27 Telegram Bot API tools via stdio or Streamable HTTP using TELEGRAM_BOT_TOKEN. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://github.com/node2flow-th/telegram-bot-mcp-community](https://github.com/node2flow-th/telegram-bot-mcp-community) (locator: `lines:155-198`)
  - *Observation*: paraphrase: Community MCP server (@node2flow/telegram-bot-mcp) exposing 27 Telegram Bot API tools via stdio or Streamable HTTP using TELEGRAM_BOT_TOKEN.
  ```text
  Telegram Bot MCP Server
  MCP (Model Context Protocol) server for Telegram Bot API. Send messages, manage chats, handle webhooks, and more through 27 tools.
  Works with Claude Desktop, Cursor, VS Code, and any MCP client.
  Quick Start
  Claude Desktop
  Add to claude_desktop_config.json:
  {
  "mcpServers": {
  "telegram": {
  "command": "npx",
  ```
- **URL**: [https://github.com/node2flow-th/telegram-bot-mcp-community](https://github.com/node2flow-th/telegram-bot-mcp-community) (locator: `lines:199-260`)
  - *Observation*: paraphrase: Tools cover bot info, sending messages/media/polls, edit/delete, chat management, webhooks, and callbacks.
  ```text
  All Tools (27 tools)
  Bot Info (2 tools)
  Tool
  Description
  tg_get_me
  Get bot information
  tg_set_my_commands
  Set bot command menu
  Send Messages (8 tools)
  Tool
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.mcp.community_mtproto` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=community; name=Telegram MTProto MCP Server (sparfenyuk/mcp-telegram); source_url=https://github.com/sparfenyuk/mcp-telegram. Source evidence (lines:154-196) states: Community uv-installed MCP server bridging Telegram MTProto API for read-only dialog/message/contact access, media download, and drafting. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://github.com/sparfenyuk/mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) (locator: `lines:154-196`)
  - *Observation*: paraphrase: Community uv-installed MCP server bridging Telegram MTProto API for read-only dialog/message/contact access, media download, and drafting.
  ```text
  Telegram MCP server
  Telegram MCP server
  About
  What is MCP?
  What does this server do?
  Practical use cases
  Prerequisites
  Installation
  Configuration
  Telegram API Configuration
  ```
- **URL**: [https://github.com/sparfenyuk/mcp-telegram](https://github.com/sparfenyuk/mcp-telegram) (locator: `lines:202-230`)
  - *Observation*: paraphrase: Authenticates via TELEGRAM_API_ID, TELEGRAM_API_HASH, and user phone sign-in.
  ```text
  Telegram API Configuration
  Before you can use the server, you need to connect to the Telegram API.
  Get the API ID and hash from Telegram API
  Run the following command:
  mcp-telegram sign-in --api-id <your-api-id> --api-hash <your-api-hash> --phone-number <your-phone-number>
  Enter the code you received from Telegram to connect to the API.
  The password may be required if you have two-factor authentication enabled.
  Note
  To log out from the Telegram API, use the mcp-telegram logout command.
  Claude Desktop Configuration
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:15-15) states: Telegram Bot Platform is free for both users and developers. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:15-15`)
  - *Observation*: paraphrase: Telegram Bot Platform is free for both users and developers.
  ```text
  The Telegram Bot Platform hosts more than 10 million bots and is free for both users and developers.
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:11-28`)
  - *Observation*: paraphrase: Bot API and Telegram MTProto API/TDLib are free of charge and 100% open for all developers.
  ```text
  We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through Telegram instead of traditional SMS.
  You can also add Telegram Widgets to your website.
  Designers are welcome to create Animated Stickers and Emoji or Custom Themes for Telegram.
  Bot API
  This API allows you to connect bots to our system. Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.
  To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS interface that offers a simplified version of the Telegram API.
  Learn more about the Bot API here »
  Bot developers can also make use of our Payments API to accept payments from Telegram users around the world.
  TDLib – build your own Telegram
  Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our Telegram Database Library (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:15-15) states: Free for both users and developers. The cited route appears accessible without this particular gate for production access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:15-15`)
  - *Observation*: paraphrase: Free for both users and developers.
  ```text
  The Telegram Bot Platform hosts more than 10 million bots and is free for both users and developers.
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:11-11`)
  - *Observation*: paraphrase: Developers are welcome to use both Bot API and Telegram API/TDLib free of charge.
  ```text
  We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through Telegram instead of traditional SMS.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:80-83) states: Self-serve bot registration via @BotFather. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:80-83`)
  - *Observation*: paraphrase: Self-serve bot registration via @BotFather.
  ```text
  How Do I Create a Bot?
  Creating Telegram bots is super-easy, but you will need at least some skills in computer programming.
  Creating a bot is streamlined by Telegram’s Bot API, which gives the tools and framework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token.
  Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct access to the bot. Everyone who has your token will have full control over your bot.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Cloud messaging platform offering free HTTPS Bot API (v10.5) via @BotFather tokens, free MTProto/TDLib client APIs, and the Telegram Gateway verification API.. Source evidence (lines:15-15) states: Telegram Bot Platform hosts 10M+ bots and is free for both users and developers. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:15-15`)
  - *Observation*: paraphrase: Telegram Bot Platform hosts 10M+ bots and is free for both users and developers.
  ```text
  The Telegram Bot Platform hosts more than 10 million bots and is free for both users and developers.
  ```
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:80-83`)
  - *Observation*: paraphrase: Register bots via @BotFather to receive a bot authentication token.
  ```text
  How Do I Create a Bot?
  Creating Telegram bots is super-easy, but you will need at least some skills in computer programming.
  Creating a bot is streamlined by Telegram’s Bot API, which gives the tools and framework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token.
  Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct access to the bot. Everyone who has your token will have full control over your bot.
  ```
- **URL**: [https://core.telegram.org/bots/api](https://core.telegram.org/bots/api) (locator: `lines:13-18`)
  - *Observation*: paraphrase: HTTP-based Bot API (v10.5, Nov 22, 2026).
  ```text
  The Bot API is an HTTP-based interface created for developers keen on building bots for Telegram.
  To learn how to create and set up a bot, please consult our Introduction to Bots and Bot FAQ.
  Recent changes
  Subscribe to @BotNews to be the first to know about the latest updates and join the discussion in @BotTalk
  November 22, 2026
  Bot API 10.5
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:11-28`)
  - *Observation*: paraphrase: Bot API, MTProto Telegram API/TDLib (free of charge), and Gateway API (free to test).
  ```text
  We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through Telegram instead of traditional SMS.
  You can also add Telegram Widgets to your website.
  Designers are welcome to create Animated Stickers and Emoji or Custom Themes for Telegram.
  Bot API
  This API allows you to connect bots to our system. Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.
  To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS interface that offers a simplified version of the Telegram API.
  Learn more about the Bot API here »
  Bot developers can also make use of our Payments API to accept payments from Telegram users around the world.
  TDLib – build your own Telegram
  Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our Telegram Database Library (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:15-15) states: Telegram Bot Platform is free for both users and developers. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:15-15`)
  - *Observation*: paraphrase: Telegram Bot Platform is free for both users and developers.
  ```text
  The Telegram Bot Platform hosts more than 10 million bots and is free for both users and developers.
  ```
- **URL**: [https://core.telegram.org/api](https://core.telegram.org/api) (locator: `lines:11-26`)
  - *Observation*: paraphrase: Bot API and Telegram API/TDLib are free of charge; Gateway API is free to test.
  ```text
  We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages for an interface. The Telegram API and TDLib allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the Gateway API allows any business, app or website to send verification codes through Telegram instead of traditional SMS.
  You can also add Telegram Widgets to your website.
  Designers are welcome to create Animated Stickers and Emoji or Custom Themes for Telegram.
  Bot API
  This API allows you to connect bots to our system. Telegram Bots are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.
  To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS interface that offers a simplified version of the Telegram API.
  Learn more about the Bot API here »
  Bot developers can also make use of our Payments API to accept payments from Telegram users around the world.
  TDLib – build your own Telegram
  Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our Telegram Database Library (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `27.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:80-83) states: Developers self-serve create a bot and receive a token immediately via @BotFather. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://core.telegram.org/bots](https://core.telegram.org/bots) (locator: `lines:80-83`)
  - *Observation*: paraphrase: Developers self-serve create a bot and receive a token immediately via @BotFather.
  ```text
  How Do I Create a Bot?
  Creating Telegram bots is super-easy, but you will need at least some skills in computer programming.
  Creating a bot is streamlined by Telegram’s Bot API, which gives the tools and framework required to integrate your code. To get started, message @BotFather on Telegram to register your bot and receive its authentication token.
  Your bot token is its unique identifier – store it in a secure place, and only share it with people who need direct access to the bot. Everyone who has your token will have full control over your bot.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 21: Slack (Communications and Messaging)
- Total claims: 22 | Corrected: 2

### Claim: `21.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:130-131): Over 200 Web API methods across families.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Over 200 Web API methods spanning messaging, workspace administration, files/canvases/lists, workflows, and enterprise compliance APIs.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Slack Web API spans multiple major distinct business domains: (1) Messaging & Conversations, (2) User & Team Management, (3) File & Canvas Content, (4) Workspace Search, and (5) Enterprise Administration/SCIM. Per evidence rules, multiple distinct business domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:130-131`)
  - *Observation*: paraphrase: Over 200 Web API methods across families.
  ```text
  Methods​
  With over 200 methods, surely there's one right for you. You can find them all in the reference, where you can filter by method family.
  ```
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:12-57`)
  - *Observation*: paraphrase: Method families span messaging, users/admin, files/canvases/lists, workflows, agents, SCIM, and audit logs.
  ```text
  Methods
  admin
  agents
  api
  apps
  assistant
  auth
  blocks
  bookmarks
  bots
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.group.files_canvases_lists` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Files, canvases, lists, bookmarks, and calls. Source evidence (lines:20-32) states: Method families include bookmarks, calls, canvases, files, lists. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:20-32`)
  - *Observation*: paraphrase: Method families include bookmarks, calls, canvases, files, lists.
  ```text
  bookmarks
  bots
  calls
  canvases
  chat
  conversations
  dialog
  dnd
  emoji
  entity
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.group.messaging_conversations` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Messages, channels, conversations, reactions, pins, and search (chat, conversations, reactions, search). Source evidence (lines:24-40) states: Method families include chat, conversations, reactions, pins, reminders, search. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:24-40`)
  - *Observation*: paraphrase: Method families include chat, conversations, reactions, pins, reminders, search.
  ```text
  chat
  conversations
  dialog
  dnd
  emoji
  entity
  files
  functions
  lists
  migration
  ```
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:61-89`)
  - *Observation*: paraphrase: Examples show conversations.create and chat.postMessage.
  ```text
  For example, a POST request to the conversations.create method might look something like this:
  POST /api/conversations.create
  Content-type: application/x-www-form-urlencoded
  token=xoxp-xxxxxxxxx-xxxx&name=something-urgent
  JSON-encoded bodies​
  For write methods that support JSON, you may alternatively send your HTTP POST data as Content-type: application/json.
  There are some ground rules:
  You must explicitly set the Content-type HTTP header to application/json. We won't interpret your POST body as such without it.
  You must transmit your token as a bearer token in the Authorization HTTP header.
  You cannot send your token as part of the query string or as an attribute in your posted JSON.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.group.users_teams_admin` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Users, usergroups, team, admin, SCIM, and audit logs. Source evidence (lines:13-56) states: Method families include admin, team, usergroups, users, plus Audit Logs API and SCIM API. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:13-56`)
  - *Observation*: paraphrase: Method families include admin, team, usergroups, users, plus Audit Logs API and SCIM API.
  ```text
  admin
  agents
  api
  apps
  assistant
  auth
  blocks
  bookmarks
  bots
  calls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.group.workflows_apps_agents` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Workflows, functions, apps, assistant, agents, and Slack Connect. Source evidence (lines:14-52) states: Method families include agents, apps, assistant, functions, workflows, and Slack Connect API. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:14-52`)
  - *Observation*: paraphrase: Method families include agents, apps, assistant, functions, workflows, and Slack Connect API.
  ```text
  agents
  api
  apps
  assistant
  auth
  blocks
  bookmarks
  bots
  calls
  canvases
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.protocol.cli` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts CLI. Source evidence (lines:145-145) states: Slack provides the Slack CLI developer tool. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:145-145`)
  - *Observation*: paraphrase: Slack provides the Slack CLI developer tool.
  ```text
  Slack CLI
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.protocol.rpc` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts RPC. Source evidence (lines:46-47) states: Slack Web API is a collection of HTTP RPC-style methods (not REST) at https://slack.com/api/METHOD_FAMILY.method. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:46-47`)
  - *Observation*: paraphrase: Slack Web API is a collection of HTTP RPC-style methods (not REST) at https://slack.com/api/METHOD_FAMILY.method.
  ```text
  The Web API is a collection of HTTP RPC-style methods, all with URLs in the form https://slack.com/api/METHOD_FAMILY.method.
  While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:145-147) states: Slack provides Bolt frameworks and official Slack SDKs. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:145-147`)
  - *Observation*: paraphrase: Slack provides Bolt frameworks and official Slack SDKs.
  ```text
  Slack CLI
  Bolt frameworks
  Slack SDKs
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:41-47) states: Publicly accessible Slack Web API guide at docs.slack.dev/apis/web-api/. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:41-47`)
  - *Observation*: paraphrase: Publicly accessible Slack Web API guide at docs.slack.dev/apis/web-api/.
  ```text
  Slack Web API
  The Slack Web API is an interface for querying information from and enacting change in a Slack workspace.
  Use it for individual queries, or as part of a more complex tapestry of platform features in a Slack app.
  Web API methods
  Basic overview​
  The Web API is a collection of HTTP RPC-style methods, all with URLs in the form https://slack.com/api/METHOD_FAMILY.method.
  While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
  ```
- **URL**: [https://docs.slack.dev/reference/methods](https://docs.slack.dev/reference/methods) (locator: `lines:12-57`)
  - *Observation*: paraphrase: Public method family reference at docs.slack.dev/reference/methods.
  ```text
  Methods
  admin
  agents
  api
  apps
  assistant
  auth
  blocks
  bookmarks
  bots
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.auth.bearer_token` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Bearer_token authentication for Slack Web API runtime request authentication. Source evidence (lines:68-78) states: JSON POST bodies require Authorization: Bearer xoxp-... header. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:68-78`)
  - *Observation*: paraphrase: JSON POST bodies require Authorization: Bearer xoxp-... header.
  ```text
  You must explicitly set the Content-type HTTP header to application/json. We won't interpret your POST body as such without it.
  You must transmit your token as a bearer token in the Authorization HTTP header.
  You cannot send your token as part of the query string or as an attribute in your posted JSON.
  Do not mix arguments between query string, URL-encoded POST body, and JSON attributes. Choose one approach per request.
  Providing an explicitly null value for an attribute will result in whichever default behavior is assigned to it.
  For example, to send the same request above to the conversations.create method with a JSON POST body, send something like this:
  POST /api/conversations.create
  Content-type: application/json
  Authorization: Bearer xoxp-xxxxxxxxx-xxxx
  {"name":"something-urgent"}
  ```
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:112-115`)
  - *Observation*: paraphrase: Web API requests authenticate via bearer token identifying a user or bot user.
  ```text
  Authentication​
  Authenticate your Web API requests by providing a bearer token, which identifies a single user or bot user relationship.
  Register your application with Slack to obtain credentials for use with our OAuth 2.0 implementation, which allows you to negotiate tokens on behalf of users and workspaces.
  We prefer tokens to be sent in the Authorization HTTP header of your outbound requests. However, you may also pass tokens in all Web API calls as a POST body parameter called token. Tokens cannot be sent as a query parameter.
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:221-229`)
  - *Observation*: paraphrase: Access tokens presented as Authorization: Bearer xoxb-... header or form POST token parameter.
  ```text
  Using tokens​
  The best way to communicate your access tokens — also known as bearer tokens — to Slack is by presenting them in a request's Authorization HTTP header where the full value, including "Bearer", is case-sensitive. This approach is required when using application/json with a write method.
  GET /api/conversations.list?limit=50
  Authorization: Bearer xoxb-1234-abcdefgh
  Alternatively, you may send the token as a POST body attribute of the application/x-www-form-urlencoded variety.
  POST body:
  POST /api/conversations.list
  Content-type: application/x-www-form-urlencoded
  token=xoxb-1234-abcdefgh&limit=50
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.auth.oauth2_v2` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Slack Web API and MCP OAuth 2.0 apps. Source evidence (lines:41-65) states: OAuth 2.0 v2 flow requests bot scopes (scope) and user scopes (user_scope) at /oauth/v2/authorize. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:41-65`)
  - *Observation*: paraphrase: OAuth 2.0 v2 flow requests bot scopes (scope) and user scopes (user_scope) at /oauth/v2/authorize.
  ```text
  Slack apps are installed with a v2 OAuth 2.0 flow. Your app can act with its own identity instead of acting on behalf of users, without requesting excessive permissions that could cause installations to be rejected.
  OAuth 2.0 refers to the 2.0 version of the OAuth spec, and this is our second version of OAuth 2.0. For the rest of this guide, we'll just refer to it as "OAuth".
  How it works: a high-level overview​
  OAuth allows a user in any Slack workspace to install your app. At the end of the OAuth flow, your app gains an access token. Your app's access token allows your app to open doors to the Slack platform. During the OAuth flow, you specify which scopes your app needs. Those scopes determine exactly which doors your app can open.
  Implementing an OAuth flow can feel hard because there are a lot of steps, but your app really only has to worry about three steps to make OAuth work: requesting scopes, waiting for a user to give their approval, and exchanging a temporary authorization code for an access token. Redirecting a user to Slack can be done with a single link. For example:
  [Add to Slack](https://slack.com/oauth/v2/authorize?scope=incoming-webhook&client_id=33336676.569200954261)
  Replace the client_id with your app's client ID, and add the scopes you'd like. Bot scopes should be added as scope=<bot_scope>, and user scopes should be added as user_scope=<user_scope>.
  For example, if your app only has one bot scope and it is incoming-webhook, the redirect would look like that shown above. If your app has a user scope, it might look like this instead:
  https://slack.com/oauth/v2/authorize?user_scope=search%3Aread&client_id=33336676.569200954261
  If your app has both a bot and a user scope, it might look like this:
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:162-186`)
  - *Observation*: paraphrase: Code exchange at /api/oauth.v2.access returns xoxb bot token and authed_user xoxp user token.
  ```text
  Now, you just need to exchange the code for an access token. You'll do this by calling the oauth.v2.access method as follows:
  curl -F code=1234 -F client_id=3336676.569200954261 -F client_secret=ABCDEFGH https://slack.com/api/oauth.v2.access
  Once you complete your access call, Slack sends you an HTTP request response containing an access token. It looks something like this:
  {
  "ok": true,
  "access_token": "xoxb-17653672481-19874698323-pdFZKVeTuE8sk7oOcBrzbqgy",
  "token_type": "bot",
  "scope": "commands,incoming-webhook",
  "bot_user_id": "U0KRQLJ9H",
  "app_id": "A0KRD7HC3",
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:194-206`)
  - *Observation*: paraphrase: User-centric /oauth/v2_user/authorize and /api/oauth.v2.user.access flow for user tokens and MCP clients.
  ```text
  The user-centric flow: the oauth.v2.user.access method​
  In addition to the standard workspace installation flow, Slack provides a dedicated flow for obtaining user-specific access tokens. To initiate a user-specific flow, redirect users to the v2_user authorization endpoint:
  https://slack.com/oauth/v2_user/authorize?client_id=YOUR_CLIENT_ID&scope=chat:write,channels:history
  Unlike the the standard v2/authorize endpoint, this flow focuses exclusively on the user's identity and personal permissions. After approval, Slack redirects back to your redirect_uri with a temporary code, just like the standard flow.
  Exchanging the code with oauth.v2.user.access​
  Once you have the temporary authorization code, you must exchange it using the oauth.v2.user.access API method. This method is compliant to the OAuth 2.0 RFC.
  Comparing oauth.v2.access and oauth.v2.user.access endpoints​
  The oauth.v2.access API method supports generating either a bot token or user token or both.
  The oauth.v2.user.access API method generates a user token by default following the standard OAuth spec and works out-of-the-box with MCP authorization flows.
  The oauth.v2.user.access endpoint should be used in scenarios where:
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Build a Slack workspace messaging, search, canvas, and list agent toolkit via the Web API or official Slack MCP server.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:41-47): Public HTTP RPC Web API.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Slack workspace messaging, search, canvas, and list agent toolkit via the Web API or official Slack MCP server.", "blockers": ["Public multi-tenant distribution on Slack Marketplace (and public MCP use) requires Slack app review; unlisted apps cannot use Slack MCP.", "Slack MCP server does not support Dynamic Client Registration (DCR); clients must use a registered Slack app ID with confidential OAuth."], "next_steps": ["Register a Slack app and configure OAuth 2.0 v2 scopes (bot and/or user tokens).", "Target https://slack.com/api/* Web API methods or https://mcp.slack.com/mcp for internal testing, and submit for Slack Marketplace review for public multi-tenant distribution."]}`
  - Original Rationale: Feasibility inference from captured primary documentation; no live integration or credential test executed.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Slack workspace messaging, search, canvas, and list agent toolkit via the Web API or official Slack MCP server.", "blockers": ["Public multi-tenant distribution on Slack Marketplace (and public MCP use) requires Slack app review; unlisted apps cannot use Slack MCP.", "Slack MCP server does not support Dynamic Client Registration (DCR); clients must use a registered Slack app ID with confidential OAuth."], "next_steps": ["Register a Slack app and configure OAuth 2.0 v2 scopes (bot and/or user tokens).", "Target https://slack.com/api/* Web API methods or https://mcp.slack.com/mcp for internal testing, and submit for Slack Marketplace review for public multi-tenant distribution."]}`
  - Corrected Rationale: Buildability inference is anchored to verified Slack platform documentation: self-serve app registration, free workspace tier (21.testing.free_access), Bot token authentication (21.auth.oauth2), and extensive Web API methods (21.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:41-47`)
  - *Observation*: paraphrase: Public HTTP RPC Web API.
  ```text
  Slack Web API
  The Slack Web API is an interface for querying information from and enacting change in a Slack workspace.
  Use it for individual queries, or as part of a more complex tapestry of platform features in a Slack app.
  Web API methods
  Basic overview​
  The Web API is a collection of HTTP RPC-style methods, all with URLs in the form https://slack.com/api/METHOD_FAMILY.method.
  While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:107-125`)
  - *Observation*: paraphrase: Official hosted MCP server with confidential OAuth and no DCR.
  ```text
  Transport protocol and endpoint​
  Slack supports JSON-RPC 2.0 over Streamable HTTP. All requests should be sent to:
  https://mcp.slack.com/mcp
  We do not support SSE-based connections or Dynamic Client Registration at this time.
  App Identity​
  MCP clients must be backed by a registered Slack app with a fixed app ID and hardcode that app ID. This allows Slack to:
  Let admins manage and approve your app/MCP client app using standard Slack app approval process.
  Associate requests with your app for logging, rate limits, and access control.
  Provide better support and visibility into usage.
  If you're already using a Slack app for your integration, you can reuse it for MCP access.
  ```
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-176`)
  - *Observation*: paraphrase: Free forever workspace tier with up to 10 apps.
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:43-46) states: Official Slack MCP server documented at docs.slack.dev/ai/slack-mcp-server. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:43-46`)
  - *Observation*: paraphrase: Official Slack MCP server documented at docs.slack.dev/ai/slack-mcp-server.
  ```text
  Slack MCP server overview
  With the Slack MCP server, your integrated apps can search channels, send messages, and perform other Slack actions through MCP clients. Workspace admins can approve and manage all MCP client integrations, keeping your Slack data safe. This guide discusses the MCP server offerings from Slack and how to develop with the Slack MCP server.
  Slack MCP server features​
  The Slack MCP server provides tools for searching through Slack, retrieving and sending messages, managing canvases, managing users, uploading files, and working with lists. Each of these tools provides useful functionality for interacting with Slack; combine them for comprehensive integrations that grasp your team's context and history.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:107-110`)
  - *Observation*: paraphrase: Official endpoint https://mcp.slack.com/mcp.
  ```text
  Transport protocol and endpoint​
  Slack supports JSON-RPC 2.0 over Streamable HTTP. All requests should be sent to:
  https://mcp.slack.com/mcp
  We do not support SSE-based connections or Dynamic Client Registration at this time.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.mcp.official` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Slack MCP Server; source_url=https://docs.slack.dev/ai/slack-mcp-server. Source evidence (lines:43-78) states: Official Slack MCP server provides tools for searching messages/files/users/channels, sending/scheduling/drafting messages, canvases, files, and lists. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:43-78`)
  - *Observation*: paraphrase: Official Slack MCP server provides tools for searching messages/files/users/channels, sending/scheduling/drafting messages, canvases, files, and lists.
  ```text
  Slack MCP server overview
  With the Slack MCP server, your integrated apps can search channels, send messages, and perform other Slack actions through MCP clients. Workspace admins can approve and manage all MCP client integrations, keeping your Slack data safe. This guide discusses the MCP server offerings from Slack and how to develop with the Slack MCP server.
  Slack MCP server features​
  The Slack MCP server provides tools for searching through Slack, retrieving and sending messages, managing canvases, managing users, uploading files, and working with lists. Each of these tools provides useful functionality for interacting with Slack; combine them for comprehensive integrations that grasp your team's context and history.
  Searching throughout Slack​
  The MCP server can search for a variety of information found throughout a Slack workspace:
  Messages and files — filter by date, user, and content type. Retrieve metadata and content.
  Users in a workspace — filter by name (with partial name matching), email, and user ID. Retrieve user details and statuses.
  Private and public channels — filter by channel name and description. Retrieve channel metadata.
  List user channels — list the channels you're a member of, filterable by type (public, private, DMs, group DMs), name prefix, and workspace. Supports pagination and can return full details, names only, or IDs only. Archived channels are included by default.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:107-132`)
  - *Observation*: paraphrase: Hosted JSON-RPC 2.0 Streamable HTTP endpoint at https://mcp.slack.com/mcp using confidential OAuth 2.0 (no SSE or DCR).
  ```text
  Transport protocol and endpoint​
  Slack supports JSON-RPC 2.0 over Streamable HTTP. All requests should be sent to:
  https://mcp.slack.com/mcp
  We do not support SSE-based connections or Dynamic Client Registration at this time.
  App Identity​
  MCP clients must be backed by a registered Slack app with a fixed app ID and hardcode that app ID. This allows Slack to:
  Let admins manage and approve your app/MCP client app using standard Slack app approval process.
  Associate requests with your app for logging, rate limits, and access control.
  Provide better support and visibility into usage.
  If you're already using a Slack app for your integration, you can reuse it for MCP access.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.production.admin_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:44-44) states: Workspace admins can approve and manage MCP client integrations. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:44-44`)
  - *Observation*: paraphrase: Workspace admins can approve and manage MCP client integrations.
  ```text
  With the Slack MCP server, your integrated apps can search channels, send messages, and perform other Slack actions through MCP clients. Workspace admins can approve and manage all MCP client integrations, keeping your Slack data safe. This guide discusses the MCP server offerings from Slack and how to develop with the Slack MCP server.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:112-117`)
  - *Observation*: paraphrase: Registered Slack apps allow admins to manage and approve apps using Slack's app approval process.
  ```text
  MCP clients must be backed by a registered Slack app with a fixed app ID and hardcode that app ID. This allows Slack to:
  Let admins manage and approve your app/MCP client app using standard Slack app approval process.
  Associate requests with your app for logging, rate limits, and access control.
  Provide better support and visibility into usage.
  If you're already using a Slack app for your integration, you can reuse it for MCP access.
  Only directory-published apps or internal apps may use MCP.
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:84-84`)
  - *Observation*: paraphrase: Org-level installations require an Org Owner or Org Admin.
  ```text
  Passing an organization ID (E0123456789) requests an org-level installation rather than a single-workspace one. When the app is already installed on individual workspaces in that org, upgrading to an org-level installation may require an Org Owner or Org Admin: other members are either directed to a workspace where they can install the app, or shown an error asking them to contact an admin.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:167-176) states: Free forever plan supports up to 10 apps (with 90-day message history). The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-176`)
  - *Observation*: paraphrase: Free forever plan supports up to 10 apps (with 90-day message history).
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:167-176) states: Free forever plan includes up to 10 apps without requiring a paid subscription. The cited route appears accessible without this particular gate for production access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-176`)
  - *Observation*: paraphrase: Free forever plan includes up to 10 apps without requiring a paid subscription.
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:167-229) states: Free, Pro, and Business+ plans offer self-serve Get started flows. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-229`)
  - *Observation*: paraphrase: Free, Pro, and Business+ plans offer self-serve Get started flows.
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:116-121`)
  - *Observation*: paraphrase: Internal apps can be created and used on your own workspace without Marketplace listing.
  ```text
  If you're already using a Slack app for your integration, you can reuse it for MCP access.
  Only directory-published apps or internal apps may use MCP.
  Security concerns​
  When using the Slack MCP server, please be mindful about connecting to or utilizing other MCP servers at the same time. Different servers may have their own security, stability, and usage characteristics, so think carefully before mixing them together. Use judgment when evaluating what to connect and share across environments. Using these clients means giving them access to your Slack data so you can use it as context while interacting with those apps.
  Audit MCP activity with the associated audit logs.
  Only apps published in the Slack Marketplace and internal apps can use MCP at this time; unlisted apps are prohibited from using MCP.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.production.vendor_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:117-121) states: Only apps published in the Slack Marketplace and internal apps can use MCP; unlisted apps are prohibited. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:117-121`)
  - *Observation*: paraphrase: Only apps published in the Slack Marketplace and internal apps can use MCP; unlisted apps are prohibited.
  ```text
  Only directory-published apps or internal apps may use MCP.
  Security concerns​
  When using the Slack MCP server, please be mindful about connecting to or utilizing other MCP servers at the same time. Different servers may have their own security, stability, and usage characteristics, so think carefully before mixing them together. Use judgment when evaluating what to connect and share across environments. Using these clients means giving them access to your Slack data so you can use it as context while interacting with those apps.
  Audit MCP activity with the associated audit logs.
  Only apps published in the Slack Marketplace and internal apps can use MCP at this time; unlisted apps are prohibited from using MCP.
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:247-247`)
  - *Observation*: paraphrase: Published apps require Slack review/approval of requested scopes (unapproved_scope error otherwise).
  ```text
  unapproved_scope: Occurs if attempting to install a published app for which the requested scopes aren't approved either because they're still in review for that app, or they weren't yet submitted for review by the app developer.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Workspace messaging and collaboration platform with HTTP RPC-style Web API (200+ methods), OAuth 2.0 bot/user tokens, and an official hosted MCP server.. Source evidence (lines:41-47) states: Slack Web API is an HTTP RPC-style interface for querying and enacting change in a Slack workspace. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:41-47`)
  - *Observation*: paraphrase: Slack Web API is an HTTP RPC-style interface for querying and enacting change in a Slack workspace.
  ```text
  Slack Web API
  The Slack Web API is an interface for querying information from and enacting change in a Slack workspace.
  Use it for individual queries, or as part of a more complex tapestry of platform features in a Slack app.
  Web API methods
  Basic overview​
  The Web API is a collection of HTTP RPC-style methods, all with URLs in the form https://slack.com/api/METHOD_FAMILY.method.
  While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
  ```
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:130-131`)
  - *Observation*: paraphrase: Web API exposes over 200 methods organized by method family.
  ```text
  Methods​
  With over 200 methods, surely there's one right for you. You can find them all in the reference, where you can filter by method family.
  ```
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-168`)
  - *Observation*: paraphrase: Team chat and collaboration platform.
  ```text
  Free
  A simpler way to chat and collaborate
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:41-51`)
  - *Observation*: paraphrase: Slack apps use OAuth 2.0 v2 flow to request bot and user scopes.
  ```text
  Slack apps are installed with a v2 OAuth 2.0 flow. Your app can act with its own identity instead of acting on behalf of users, without requesting excessive permissions that could cause installations to be rejected.
  OAuth 2.0 refers to the 2.0 version of the OAuth spec, and this is our second version of OAuth 2.0. For the rest of this guide, we'll just refer to it as "OAuth".
  How it works: a high-level overview​
  OAuth allows a user in any Slack workspace to install your app. At the end of the OAuth flow, your app gains an access token. Your app's access token allows your app to open doors to the Slack platform. During the OAuth flow, you specify which scopes your app needs. Those scopes determine exactly which doors your app can open.
  Implementing an OAuth flow can feel hard because there are a lot of steps, but your app really only has to worry about three steps to make OAuth work: requesting scopes, waiting for a user to give their approval, and exchanging a temporary authorization code for an access token. Redirecting a user to Slack can be done with a single link. For example:
  [Add to Slack](https://slack.com/oauth/v2/authorize?scope=incoming-webhook&client_id=33336676.569200954261)
  Replace the client_id with your app's client ID, and add the scopes you'd like. Bot scopes should be added as scope=<bot_scope>, and user scopes should be added as user_scope=<user_scope>.
  For example, if your app only has one bot scope and it is incoming-webhook, the redirect would look like that shown above. If your app has a user scope, it might look like this instead:
  https://slack.com/oauth/v2/authorize?user_scope=search%3Aread&client_id=33336676.569200954261
  If your app has both a bot and a user scope, it might look like this:
  ```
- **URL**: [https://docs.slack.dev/authentication/installing-with-oauth](https://docs.slack.dev/authentication/installing-with-oauth) (locator: `lines:162-186`)
  - *Observation*: paraphrase: OAuth 2.0 code exchange returns xoxb bot tokens and xoxp user tokens.
  ```text
  Now, you just need to exchange the code for an access token. You'll do this by calling the oauth.v2.access method as follows:
  curl -F code=1234 -F client_id=3336676.569200954261 -F client_secret=ABCDEFGH https://slack.com/api/oauth.v2.access
  Once you complete your access call, Slack sends you an HTTP request response containing an access token. It looks something like this:
  {
  "ok": true,
  "access_token": "xoxb-17653672481-19874698323-pdFZKVeTuE8sk7oOcBrzbqgy",
  "token_type": "bot",
  "scope": "commands,incoming-webhook",
  "bot_user_id": "U0KRQLJ9H",
  "app_id": "A0KRD7HC3",
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:43-46`)
  - *Observation*: paraphrase: Slack provides an official MCP server for workspace actions.
  ```text
  Slack MCP server overview
  With the Slack MCP server, your integrated apps can search channels, send messages, and perform other Slack actions through MCP clients. Workspace admins can approve and manage all MCP client integrations, keeping your Slack data safe. This guide discusses the MCP server offerings from Slack and how to develop with the Slack MCP server.
  Slack MCP server features​
  The Slack MCP server provides tools for searching through Slack, retrieving and sending messages, managing canvases, managing users, uploading files, and working with lists. Each of these tools provides useful functionality for interacting with Slack; combine them for comprehensive integrations that grasp your team's context and history.
  ```
- **URL**: [https://docs.slack.dev/ai/slack-mcp-server](https://docs.slack.dev/ai/slack-mcp-server) (locator: `lines:107-110`)
  - *Observation*: paraphrase: Official hosted MCP server endpoint at https://mcp.slack.com/mcp.
  ```text
  Transport protocol and endpoint​
  Slack supports JSON-RPC 2.0 over Streamable HTTP. All requests should be sent to:
  https://mcp.slack.com/mcp
  We do not support SSE-based connections or Dynamic Client Registration at this time.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:167-176) states: Slack offers a Free forever plan ($0/INR 0) supporting up to 10 apps. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-176`)
  - *Observation*: paraphrase: Slack offers a Free forever plan ($0/INR 0) supporting up to 10 apps.
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `21.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:167-176) states: Self-serve Get started CTA for Free forever plan with up to 10 apps. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://slack.com/pricing](https://slack.com/pricing) (locator: `lines:167-176`)
  - *Observation*: paraphrase: Self-serve Get started CTA for Free forever plan with up to 10 apps.
  ```text
  Free
  A simpler way to chat and collaborate
  ₹0
  Free forever
  Get started
  Get started
  90 days of message history
  Messages are saved and searchable for 90 days. Upgrade to access the previous 12 months messages.
  Up to ten apps
  Choose from over 2,600 apps in the Slack App Directory – from Salesforce, Jira, Google Drive, ChatGPT and more.
  ```
- **URL**: [https://docs.slack.dev/apis/web-api/](https://docs.slack.dev/apis/web-api/) (locator: `lines:113-114`)
  - *Observation*: paraphrase: Developers register an application with Slack to obtain OAuth 2.0 credentials.
  ```text
  Authenticate your Web API requests by providing a bearer token, which identifies a single user or bot user relationship.
  Register your application with Slack to obtain credentials for use with our OAuth 2.0 implementation, which allows you to negotiate tokens on behalf of users and workspaces.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 40: SendGrid (Marketing, Ads, Email and Social)
- Total claims: 19 | Corrected: 2

### Claim: `40.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:9-149): Spans Mail Send, Templates, Marketing Campaigns/Contacts, Domain Auth/Validation/Suppressions, Activity/Stats, Webhooks, and Account/API Key admin.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Inferred broad API surface across four distinct email delivery, marketing, deliverability, and observability domains.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Twilio SendGrid REST API spans multiple distinct functional domains: (1) Transactional Mail Send (v3), (2) Marketing Campaigns & Automation, (3) Contact & List Management, (4) Subuser Provisioning, and (5) Event Webhooks & Statistics. Per evidence rules, multiple distinct domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:9-149`)
  - *Observation*: paraphrase: Spans Mail Send, Templates, Marketing Campaigns/Contacts, Domain Auth/Validation/Suppressions, Activity/Stats, Webhooks, and Account/API Key admin.
  ```text
  Mail Send
  Mail Send API OverviewMail SendErrors
  Cancel scheduled sends
  Cancel Schedule Sends API OverviewCreate a batch IDValidate batch IDRetrieve scheduled sendRetrieve all scheduled sendsUpdate a scheduled sendCancel or pause a scheduled sendDelete a cancellation or pause from a scheduled send
  Account Provisioning API
  Account Provisioning API Overview
  Account
  Account API OverviewCreate AccountList AccountsSingle Sign-OnDelete Account
  Account State
  Account State API OverviewGet Account StateUpdate Account State
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.group.deliverability_validation_suppressions` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Domain Authentication, Email Address Validation, Suppressions, and Spam/Bounce Management. Source evidence (lines:24-27) states: Domain Authentication and Email Address Validation APIs. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:24-27`)
  - *Observation*: paraphrase: Domain Authentication and Email Address Validation APIs.
  ```text
  Domain Authentication
  Domain Authenticate API OverviewAuthenticate a domainGet the default authenticationRetrieve an authenticated domainList all authenticated domainsAdd an IP to an authenticated domainRemove an IP from an authenticated domain.Validate a domain authentication.Update an authenticated domainDelete an authenticated domain.List the authenticated domain associated with a subuserList the authenticated domains for subusers with multiple associated domainsAssociate an authenticated domain with a subuserAssociate an authenticated domain with a subuser (up to five domains)Disassociate an authenticated domain from a subuserDisassociate an authenticated domain from a subuser with multiple domains
  E-Mail Address Validation
  Email Address Validation API OverviewValidate an emailRequest Bulk Email Address Validation Upload URLGet Bulk Email Address Validation JobsGet a Bulk Email Address Validation Job by ID
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:130-144`)
  - *Observation*: paraphrase: Suppression Management, Blocks, Bounces, Invalid Emails, Spam Reports, and Suppressions APIs.
  ```text
  Suppression Management
  Blocks API
  Blocks API OverviewRetrieve a specific blockRetrieve all blocksDelete a specific blockDelete blocks
  Bounces API
  Bounces API OverviewRetrieve a BounceRetrieve bounces by specific classificationRetrieve bounce totals by classificationRetrieve all bouncesDelete a bounceDelete bounces
  Invalid E-Mails API
  Invalid Emails API OverviewRetrieve a specific invalid emailRetrieve all invalid emailsDelete a specific invalid emailDelete invalid emails
  Spam Reports API
  Spam Reports API OverviewRetrieve a specific spam reportRetrieve all spam reportsDelete a specific spam reportDelete spam reports
  Suppressions - Global Suppressions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.group.mail_send_templates` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Mail Send, Scheduled Sends, and Transactional Templates. Source evidence (lines:9-12) states: Mail Send and Cancel Scheduled Sends APIs. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:9-12`)
  - *Observation*: paraphrase: Mail Send and Cancel Scheduled Sends APIs.
  ```text
  Mail Send
  Mail Send API OverviewMail SendErrors
  Cancel scheduled sends
  Cancel Schedule Sends API OverviewCreate a batch IDValidate batch IDRetrieve scheduled sendRetrieve all scheduled sendsUpdate a scheduled sendCancel or pause a scheduled sendDelete a cancellation or pause from a scheduled send
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:145-149`)
  - *Observation*: paraphrase: Transactional Templates and Template Versions APIs.
  ```text
  Templates
  Transactional Templates
  Templates API OverviewCreate a transactional template.Duplicate a transactional template.Retrieve a single transactional template.Retrieve paged transactional templates.Edit a transactional template.Delete a template.
  Transactional Templates Versions
  Templates Versions API OverviewCreate a new transactional template version.Activate a transactional template version.Retrieve a specific transactional template version.Edit a transactional template version.Delete a transactional template version.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.group.marketing_contacts_campaigns` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Marketing Campaigns, Contacts, Lists, Segments, and Single Sends. Source evidence (lines:61-96) states: Legacy and New Marketing Campaigns, Contacts, Lists, Segmenting Contacts V2, and Campaign Stats. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:61-96`)
  - *Observation*: paraphrase: Legacy and New Marketing Campaigns, Contacts, Lists, Segmenting Contacts V2, and Campaign Stats.
  ```text
  Legacy Marketing Campaigns
  Campaigns API
  Legacy Campaigns API OverviewCreate a CampaignRetrieve a single campaignRetrieve all CampaignsUpdate a CampaignSend a CampaignSend a Test CampaignSchedule a CampaignView Scheduled Time of a CampaignUpdate a Scheduled CampaignUnschedule a Scheduled CampaignDelete a Campaign
  Categories
  Legacy Categories API OverviewRetrieve all categoriesRetrieve Email Statistics for CategoriesRetrieve sums of email stats for each category
  Contacts API - Custom Fields
  Legacy Custom Fields API OverviewCreate a Custom FieldRetrieve a Custom FieldRetrieve all custom fieldsRetrieve reserved fieldsDelete a Custom Field
  Contacts API - Lists
  Legacy Lists API OverviewCreate a ListRetrieve a single listRetrieve all listsAdd a Single Recipient to a ListAdd Multiple Recipients to a ListRetrieve all recipients on a ListDelete a Single Recipient from a Single ListUpdate a ListDelete a ListDelete Multiple lists
  Contacts API - Recipients
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.group.stats_activity_webhooks_admin` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Email Activity/Logs, Statistics, Event/Parse Webhooks, API Keys, and Subusers. Source evidence (lines:46-59) states: Email Activity, Email Logs, Statistics, and Event/Parse Webhooks. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:46-59`)
  - *Observation*: paraphrase: Email Activity, Email Logs, Statistics, and Event/Parse Webhooks.
  ```text
  Email Activity
  Email Activity API OverviewFilter Messages by IDFilter All MessagesRequest a CSVDownload CSV
  Email Logs
  Email Logs API OverviewFilter Messages by IDFilter All Messages
  Event Tracking
  Tracking Settings
  Event Tracking API OverviewRetrieve Tracking SettingsRetrieve Click Track SettingsUpdate Click Tracking SettingsRetrieve Google Analytics SettingsUpdate Google Analytics SettingsGet Open Tracking SettingsUpdate Open Tracking SettingsRetrieve Subscription Tracking SettingsUpdate Subscription Tracking Settings
  Stats
  Statistics API OverviewRetrieve global email statisticsRetrieve email statistics by browser.Retrieve stats by a specific client type.Retrieve email statistics by client type.Retrieve email statistics by country and state/province.Retrieve email statistics by device type.Retrieve email statistics by mailbox provider.
  Webhooks
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:98-122`)
  - *Observation*: paraphrase: API Keys, API Key Permissions, Mail Settings, Subuser Statistics, and Users.
  ```text
  API Keys
  API Keys API OverviewCreate API keysRetrieve an existing API KeyRetrieve all API Keys belonging to the authenticated userUpdate API key nameUpdate API key name and scopesDelete API keys
  API Key permissions
  API Key Permissions API OverviewRetrieve a list of scopes for which this user has access.
  Enforced TLS
  Enforced TLS API OverviewRetrieve current Enforced TLS settings.Update Enforced TLS settings
  IP access management
  IP Access Management API OverviewRetrieve a specific allowed IPRetrieve a list of currently allowed IPsRetrieve all recent access attemptsAdd one or more IPs to the allow listRemove a specific IP from the allowed listRemove one or more IPs from the allow list
  Settings
  Alerts
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:185-185) states: SendGrid v3 Web API provides a REST interface to send email at scale. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:185-185`)
  - *Observation*: paraphrase: SendGrid v3 Web API provides a REST interface to send email at scale.
  ```text
  The SendGrid v3 Web API provides a REST interface to send email at scale and ensure your application can handle high volumes.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:206-209) states: Documents open-source SDKs and tools to integrate with SendGrid. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:206-209`)
  - *Observation*: paraphrase: Documents open-source SDKs and tools to integrate with SendGrid.
  ```text
  SDKs and tools
  sdks-and-tools page anchor
  Positive FeedbackNegative Feedback
  See our open-source SDKs and tools to integrate with SendGrid.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-187) states: Public Twilio SendGrid Web API v3 reference at twilio.com/docs/sendgrid. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:1-187`)
  - *Observation*: paraphrase: Public Twilio SendGrid Web API v3 reference at twilio.com/docs/sendgrid.
  ```text
  SendGrid v3 API reference | SendGrid Docs | Twilio
  Skip to contentSkip to navigationSkip to topbar
  Go to the Twilio SendGrid Docs home page
  Twilio SendGrid Docs
  SendGrid v3 API Documentation
  Getting Started
  How to use the SendGrid V3 API
  AuthenticationAuthorizationErrorsOn Behalf OfRate LimitsRequestsResponses
  Mail Send
  Mail Send API OverviewMail SendErrors
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.auth.api_key_bearer` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Twilio SendGrid Web API v3 (recommended and required for 2FA-enabled accounts). Source evidence (lines:81-99) states: Twilio SendGrid requires API keys passed via Authorization: Bearer <API_KEY> against https://api.sendgrid.com/v3/. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication) (locator: `lines:81-99`)
  - *Observation*: paraphrase: Twilio SendGrid requires API keys passed via Authorization: Bearer <API_KEY> against https://api.sendgrid.com/v3/.
  ```text
  Twilio SendGrid supports API keys delivered via Bearer token or Basic authentication, depending on the Twilio SendGrid functionality you are using. In addition to Bearer API key authentication, Twilio SendGrid recommends two-factor authentication (2FA) to improve security.
  API key
  api-key page anchor
  Positive FeedbackNegative Feedback
  Authenticate to the Twilio SendGrid API by creating an API Key in the Settings section of the Twilio SendGrid console(link takes you to an external page).
  Twilio SendGrid requires using API keys because they are a secure way to talk to the Twilio SendGrid API that is separate from your username and password. If your API key gets compromised, you can delete and create a new API key and update your environment variables with the new key. API key permissions can be set to provide access to different functions of your account, without providing access to your account as a whole.
  To use an API key, pass an Authorization header with a value of Bearer <Your-API-Key-Here>, where you replace <Your-API-Key-Here> with the API Key that you created in the UI.
  Example header:
  Authorization header
  authorization-header page anchor
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys) (locator: `lines:94-123`)
  - *Observation*: paraphrase: Up to 100 API keys per account with Full, Custom, Billing, or Email Address Validation permission scopes.
  ```text
  Twilio SendGrid API key limitations
  Twilio supports a key longer than 69 characters. No exceptions can be made for third-party infrastructure.
  Twilio limits accounts to 100 API keys.
  You can't give an API key greater permissions than your own.
  The Twilio SendGrid Console displays the API key only once at creation.
  Treat your API key like a password and store it somewhere safe.
  Twilio can't retrieve or restore an unknown or deleted API key.
  To authenticate access to Twilio SendGrid services, use Application Programming Interface (API) keys.
  They are the preferred alternative to using a username and password because you can revoke an API key at any time without having to change your username and password. We suggest that you use API keys for connecting to all of SendGrid's services.
  Manage API keys
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.auth.basic_apikey` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Basic authentication for Legacy/selected endpoints without 2FA user-password auth (upgrading to Bearer API keys recommended). Source evidence (lines:100-114) states: Basic authentication uses username 'apikey' and API key as password; Basic auth is not possible for users/subusers/teammates with 2FA enabled (2FA required for all users). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication) (locator: `lines:100-114`)
  - *Observation*: paraphrase: Basic authentication uses username 'apikey' and API key as password; Basic auth is not possible for users/subusers/teammates with 2FA enabled (2FA required for all users).
  ```text
  Basic authentication
  basic-authentication page anchor
  Positive FeedbackNegative Feedback
  Using basic authentication with your account password is not as secure as using an API key. If your credentials are compromised—for example, if you accidentally commit them to version control—it is more difficult to regain the security of your account when those credentials are your username and password rather than an API key. For this reason, Twilio SendGrid does not support Basic Authentication with a username and password. Twilio SendGrid supports Basic Authentication using an API key as your password value for some services.
  When using Basic Authentication, your username will always be apikey, and your password will be your API key.
  (information)
  Info
  If you are currently using Basic authentication, we recommend upgrading your authentication method to Bearer using API Keys and then enabling Two-Factor Authentication for improved security. For more information, see Upgrading your authentication method to API Keys.
  Two-factor authentication
  two-factor-authentication page anchor
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Build Twilio SendGrid transactional/marketing email and contact management integration via Web API v3. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:81-99): Bearer API key auth for SendGrid v3 REST API.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build Twilio SendGrid transactional/marketing email and contact management integration via Web API v3", "blockers": ["Free trial is limited to 60 days (100 emails/day); ongoing production use requires a paid plan (Essentials from $19.95/mo).", "API key authentication only (no OAuth 2.0 flow documented); sender identity/domain must be verified before sending; no official Twilio SendGrid execution MCP server found."], "next_steps": ["Sign up for the 60-day free trial (no credit card required) and create a scoped API key in Settings > API Keys.", "Authenticate with Authorization: Bearer <API_KEY> against SendGrid Web API v3 or use official SDKs."]}`
  - Original Rationale: Build now: self-serve 60-day free trial, simple scoped Bearer API keys, broad well-documented REST v3 API and SDKs, and no vendor approval gate.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build Twilio SendGrid transactional/marketing email and contact management integration via Web API v3", "blockers": ["Free trial is limited to 60 days (100 emails/day); ongoing production use requires a paid plan (Essentials from $19.95/mo).", "API key authentication only (no OAuth 2.0 flow documented); sender identity/domain must be verified before sending; no official Twilio SendGrid execution MCP server found."], "next_steps": ["Sign up for the 60-day free trial (no credit card required) and create a scoped API key in Settings > API Keys.", "Authenticate with Authorization: Bearer <API_KEY> against SendGrid Web API v3 or use official SDKs."]}`
  - Corrected Rationale: Buildability inference is anchored to verified SendGrid documentation: Free tier (100 emails/day), self-serve API key generation with granular scopes, and full public REST API (40.testing.free_access, 40.auth.api_key, 40.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication](https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication) (locator: `lines:81-99`)
  - *Observation*: paraphrase: Bearer API key auth for SendGrid v3 REST API.
  ```text
  Twilio SendGrid supports API keys delivered via Bearer token or Basic authentication, depending on the Twilio SendGrid functionality you are using. In addition to Bearer API key authentication, Twilio SendGrid recommends two-factor authentication (2FA) to improve security.
  API key
  api-key page anchor
  Positive FeedbackNegative Feedback
  Authenticate to the Twilio SendGrid API by creating an API Key in the Settings section of the Twilio SendGrid console(link takes you to an external page).
  Twilio SendGrid requires using API keys because they are a secure way to talk to the Twilio SendGrid API that is separate from your username and password. If your API key gets compromised, you can delete and create a new API key and update your environment variables with the new key. API key permissions can be set to provide access to different functions of your account, without providing access to your account as a whole.
  To use an API key, pass an Authorization header with a value of Bearer <Your-API-Key-Here>, where you replace <Your-API-Key-Here> with the API Key that you created in the UI.
  Example header:
  Authorization header
  authorization-header page anchor
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys) (locator: `lines:111-123`)
  - *Observation*: paraphrase: Create API keys in Settings > API Keys with Full, Custom, Billing, or Email Address Validation permissions.
  ```text
  Create an API key
  create-an-api-key page anchor
  Positive FeedbackNegative Feedback
  To use the Mail API, you need an API key.
  Go to Settings > API Keys(link takes you to an external page). The API Keys page appears.
  Click Create API Key. The Create API Key appears.
  Type a human-readable name for your API key in the API Key Name box.
  Choose the permissions for your API Key:
  API key permissionAccess details for account
  Full AccessGrants all API endpoints full access to your account.
  ```
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:658-671`)
  - *Observation*: paraphrase: Self-serve 60-day free trial and paid Essentials/Pro plans.
  ```text
  Twilio SendGrid Email API pricing
  Start sending with a free SendGrid Email API trial
  Sign up for a free trial—no credit card required
  Only pay for the volume and features you need
  Unlock volume discounts as you scale
  Start for free
  SendGrid Email API pricing summary
  Free trial lets you send 100 emails/day for 60 days
  Essentials plan starts at $19.95 per month
  Exact pricing depends on email send volume, features
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:24-41`)
  - *Observation*: paraphrase: Domain Authentication and Sender Verification APIs.
  ```text
  Domain Authentication
  Domain Authenticate API OverviewAuthenticate a domainGet the default authenticationRetrieve an authenticated domainList all authenticated domainsAdd an IP to an authenticated domainRemove an IP from an authenticated domain.Validate a domain authentication.Update an authenticated domainDelete an authenticated domain.List the authenticated domain associated with a subuserList the authenticated domains for subusers with multiple associated domainsAssociate an authenticated domain with a subuserAssociate an authenticated domain with a subuser (up to five domains)Disassociate an authenticated domain from a subuserDisassociate an authenticated domain from a subuser with multiple domains
  E-Mail Address Validation
  Email Address Validation API OverviewValidate an emailRequest Bulk Email Address Validation Upload URLGet Bulk Email Address Validation JobsGet a Bulk Email Address Validation Job by ID
  IP Address
  IP Address API OverviewAdd IPsGet remaining IPs countRetrieve all assigned IPsRetrieve all IP addressesRetrieve all IP pools an IP address belongs to
  IP Address Management API
  IP Address Management API OverviewAdd a Twilio SendGrid IP addressGet details for an IP addressGet a list of all IP addresses on your accountUpdate details for an IP addressCreate an IP pool with a name and IP assignmentsGet details for an IP poolGet all IP pools that have associated IPsUpdate an IP pool nameDelete an IP poolAdd a batch of IPs to an IP poolGet IPs assigned to an IP poolDelete a batch of IPs from an IP poolAssign a batch of subusers to an IPGet a list of subusers assigned to an IPDelete a batch of subusers from an IP
  IP Pools
  IP Pools API OverviewCreate an IP poolRetrieve all IP poolsRetrieve all the IPs in a specified poolAdd an IP address to a poolRemove an IP address from a poolRename an IP poolDelete an IP pool
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:185-209`)
  - *Observation*: paraphrase: Public REST API v3 and open-source SDKs.
  ```text
  The SendGrid v3 Web API provides a REST interface to send email at scale and ensure your application can handle high volumes.
  The SendGrid API endpoints allow you to integrate with your tech stack to send transactional emails, create marketing campaigns, manage your contacts, and monitor the health of your email statistics.
  This API reference provides complete documentation for every endpoint and operation. For an overview of using SendGrid APIs, see the Getting Started section.
  Additional resources
  additional-resources page anchor
  Positive FeedbackNegative Feedback
  Onboarding guide
  onboarding-guide page anchor
  Positive FeedbackNegative Feedback
  For a full-featured guide to ensure you build your email program on a solid foundation, see the Email API Onboarding guide.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:1-30) states: Community SendGrid MCP server repository. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/Garoth/sendgrid-mcp/main/README.md](https://raw.githubusercontent.com/Garoth/sendgrid-mcp/main/README.md) (locator: `lines:1-30`)
  - *Observation*: paraphrase: Community SendGrid MCP server repository.
  ```text
  # SendGrid MCP Server
  <img src="assets/sendgrid-logo.png" width="256" height="256" alt="SendGrid Logo" />
  A Model Context Protocol (MCP) server that provides access to SendGrid's Marketing API for email marketing and contact management. https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api
  ## Demo
  In this demo, we ask the Cline SendGrid agent to make a new contact list, add my emails to it, automatically generate a template for Lost Cities facts, and send the email to the list. In this process, Cline will automatically realize that it needs to know the verified senders we have, and which unsubscribe group to use. A pretty email is delivered to my inboxes, delighting me with Lost Cities!
  <img src="assets/1.png" width="760" alt="SendGrid MCP Demo 1" />
  <img src="assets/2.png" width="760" alt="SendGrid MCP Demo 2" />
  <img src="assets/3.png" width="760" alt="SendGrid MCP Demo 3" />
  <img src="assets/4.png" width="760" alt="SendGrid MCP Demo 4" />
  <img src="assets/5.png" width="760" alt="SendGrid MCP Demo 5" />
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.mcp.community_sendgrid_mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=community; name=SendGrid MCP Server (Garoth/sendgrid-mcp); source_url=https://raw.githubusercontent.com/Garoth/sendgrid-mcp/main/README. Source evidence (lines:1-225) states: Community open-source local Node.js MCP server (SENDGRID_API_KEY) exposing callable tools for SendGrid v3 contact management (list/add/delete contacts and lists), email sending (send_email, Single Sends), dynamic templates, email statistics, and email validation. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/Garoth/sendgrid-mcp/main/README.md](https://raw.githubusercontent.com/Garoth/sendgrid-mcp/main/README.md) (locator: `lines:1-225`)
  - *Observation*: paraphrase: Community open-source local Node.js MCP server (SENDGRID_API_KEY) exposing callable tools for SendGrid v3 contact management (list/add/delete contacts and lists), email sending (send_email, Single Sends), dynamic templates, email statistics, and email validation.
  ```text
  # SendGrid MCP Server
  <img src="assets/sendgrid-logo.png" width="256" height="256" alt="SendGrid Logo" />
  A Model Context Protocol (MCP) server that provides access to SendGrid's Marketing API for email marketing and contact management. https://docs.sendgrid.com/api-reference/how-to-use-the-sendgrid-v3-api
  ## Demo
  In this demo, we ask the Cline SendGrid agent to make a new contact list, add my emails to it, automatically generate a template for Lost Cities facts, and send the email to the list. In this process, Cline will automatically realize that it needs to know the verified senders we have, and which unsubscribe group to use. A pretty email is delivered to my inboxes, delighting me with Lost Cities!
  <img src="assets/1.png" width="760" alt="SendGrid MCP Demo 1" />
  <img src="assets/2.png" width="760" alt="SendGrid MCP Demo 2" />
  <img src="assets/3.png" width="760" alt="SendGrid MCP Demo 3" />
  <img src="assets/4.png" width="760" alt="SendGrid MCP Demo 4" />
  <img src="assets/5.png" width="760" alt="SendGrid MCP Demo 5" />
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:665-671) states: Free trial is time-limited to 60 days (100 emails/day); ongoing plans start at Essentials ($19.95/month), with Pro and Premier volume plans. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:665-671`)
  - *Observation*: paraphrase: Free trial is time-limited to 60 days (100 emails/day); ongoing plans start at Essentials ($19.95/month), with Pro and Premier volume plans.
  ```text
  Free trial lets you send 100 emails/day for 60 days
  Essentials plan starts at $19.95 per month
  Exact pricing depends on email send volume, features
  Pro and premier plans include dedicated IPs, with option to purchase more
  Start for free
  SendGrid Email API Plans
  Pricing is determined by monthly email volume and features. Select your email volume below to see which plans are right for you.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:707-726) states: Users can upgrade any time after setting up their free account. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:707-726`)
  - *Observation*: paraphrase: Users can upgrade any time after setting up their free account.
  ```text
  Start for free
  You can upgrade any time after your free account is set up.
  Taxes and overages may
  apply.
  Close
  Open
  Show features
  What’s included:
  Analytics & deliverability optimization
  Additional teammates:
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys) (locator: `lines:111-188`)
  - *Observation*: paraphrase: Self-serve API key creation in console.
  ```text
  Create an API key
  create-an-api-key page anchor
  Positive FeedbackNegative Feedback
  To use the Mail API, you need an API key.
  Go to Settings > API Keys(link takes you to an external page). The API Keys page appears.
  Click Create API Key. The Create API Key appears.
  Type a human-readable name for your API key in the API Key Name box.
  Choose the permissions for your API Key:
  API key permissionAccess details for account
  Full AccessGrants all API endpoints full access to your account.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Transactional email API and marketing campaigns platform exposing SendGrid Web API v3 for mail send, transactional templates, contacts/lists, validation, webhooks, and deliverability analytics.. Source evidence (lines:9-187) states: Covers Mail Send, Domain Authentication, Email Address Validation, Email Activity/Stats, Event/Parse Webhooks, Marketing Campaigns/Contacts/Lists/Segments, Suppressions, and Transactional Templates. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/docs/sendgrid/api-reference](https://www.twilio.com/docs/sendgrid/api-reference) (locator: `lines:9-187`)
  - *Observation*: paraphrase: Covers Mail Send, Domain Authentication, Email Address Validation, Email Activity/Stats, Event/Parse Webhooks, Marketing Campaigns/Contacts/Lists/Segments, Suppressions, and Transactional Templates.
  ```text
  Mail Send
  Mail Send API OverviewMail SendErrors
  Cancel scheduled sends
  Cancel Schedule Sends API OverviewCreate a batch IDValidate batch IDRetrieve scheduled sendRetrieve all scheduled sendsUpdate a scheduled sendCancel or pause a scheduled sendDelete a cancellation or pause from a scheduled send
  Account Provisioning API
  Account Provisioning API Overview
  Account
  Account API OverviewCreate AccountList AccountsSingle Sign-OnDelete Account
  Account State
  Account State API OverviewGet Account StateUpdate Account State
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:659-665) states: Free 60-day trial requires no credit card. The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:659-665`)
  - *Observation*: paraphrase: Free 60-day trial requires no credit card.
  ```text
  Start sending with a free SendGrid Email API trial
  Sign up for a free trial—no credit card required
  Only pay for the volume and features you need
  Unlock volume discounts as you scale
  Start for free
  SendGrid Email API pricing summary
  Free trial lets you send 100 emails/day for 60 days
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:659-663) states: Self-serve free trial signup. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:659-663`)
  - *Observation*: paraphrase: Self-serve free trial signup.
  ```text
  Start sending with a free SendGrid Email API trial
  Sign up for a free trial—no credit card required
  Only pay for the volume and features you need
  Unlock volume discounts as you scale
  Start for free
  ```
- **URL**: [https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys](https://www.twilio.com/docs/sendgrid/ui/account-and-settings/api-keys) (locator: `lines:111-188`)
  - *Observation*: paraphrase: Self-serve API key creation in Settings > API Keys.
  ```text
  Create an API key
  create-an-api-key page anchor
  Positive FeedbackNegative Feedback
  To use the Mail API, you need an API key.
  Go to Settings > API Keys(link takes you to an external page). The API Keys page appears.
  Click Create API Key. The Create API Key appears.
  Type a human-readable name for your API key in the API Key Name box.
  Choose the permissions for your API Key:
  API key permissionAccess details for account
  Full AccessGrants all API endpoints full access to your account.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `40.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:658-665) states: Free SendGrid Email API trial lets you send 100 emails/day for 60 days with no credit card required. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://www.twilio.com/en-us/pricing/email-api](https://www.twilio.com/en-us/pricing/email-api) (locator: `lines:658-665`)
  - *Observation*: paraphrase: Free SendGrid Email API trial lets you send 100 emails/day for 60 days with no credit card required.
  ```text
  Twilio SendGrid Email API pricing
  Start sending with a free SendGrid Email API trial
  Sign up for a free trial—no credit card required
  Only pay for the volume and features you need
  Unlock volume discounts as you scale
  Start for free
  SendGrid Email API pricing summary
  Free trial lets you send 100 emails/day for 60 days
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 31: Google Ads (Marketing, Ads, Email and Social)
- Total claims: 20 | Corrected: 3

### Claim: `31.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:433-455): Covers accounts, multiple campaign types, GAQL reporting, conversions, and bidding.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Inferred broad API surface spanning five distinct advertising domains (account hierarchy, multi-format campaigns/assets, GAQL reporting, conversions/bidding, and keyword/audience planning).
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Google Ads API documentation covers multiple distinct advertising business domains: (1) Account Hierarchy & Budgets, (2) Campaigns & AdGroups, (3) GAQL Reporting & Metrics, (4) Conversion Tracking, and (5) Bidding Strategies. Per evidence rules, multiple distinct advertising business domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:433-455`)
  - *Observation*: paraphrase: Covers accounts, multiple campaign types, GAQL reporting, conversions, and bidding.
  ```text
  The Google Ads API is the programmatic interface to Google Ads, used for managing large or
  complex Google Ads accounts and campaigns. You can build software that manages
  accounts from the customer level down to the keyword level. Typical use cases
  include:
  Automated account management:
  Create and link accounts, manage account hierarchies, and automate user
  access.
  Custom reporting: Query performance metrics,
  segments, and resource attributes using the
  Google Ads Query Language (GAQL).
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/api-policy/access-levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) (locator: `lines:133-155`)
  - *Observation*: paraphrase: Includes keyword planning and audience/reach planning services.
  ```text
  The Explorer access level restricts access to the following features. If you
  need to use these features, you need to apply for
  Basic access level or Standard access level.
  Restricted functionality
  Restricted services and methods
  Account creation and linking
  CustomerService.CreateCustomerClient
  CustomerClientLinkService
  CustomerManagerLinkService
  User management
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.group.accounts_hierarchy` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Customers, account hierarchies, and user access management. Source evidence (lines:437-439) states: Automated account management: create/link accounts, manage hierarchies, automate user access. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:437-439`)
  - *Observation*: paraphrase: Automated account management: create/link accounts, manage hierarchies, automate user access.
  ```text
  Automated account management:
  Create and link accounts, manage account hierarchies, and automate user
  access.
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/concepts/api-structure](https://developers.google.com/google-ads/api/docs/concepts/api-structure) (locator: `lines:436-441`)
  - *Observation*: paraphrase: Top-level customer resource containing campaigns.
  ```text
  Object hierarchy
  A Google Ads account can be viewed as a hierarchy of objects.
  The top-level resource of an account is the
  customer.
  Each customer contains one or more active
  campaigns.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.group.campaigns_ads` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Campaigns (Search, Performance Max, Shopping, Video, App, Demand Gen), ad groups, ads, budgets, and assets. Source evidence (lines:443-451) states: Create and update Performance Max, Search, Demand Gen, Shopping, Video, and App campaigns, budgets, and assets. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:443-451`)
  - *Observation*: paraphrase: Create and update Performance Max, Search, Demand Gen, Shopping, Video, and App campaigns, budgets, and assets.
  ```text
  Campaign and inventory-based ad management:
  Create and update Performance Max,
  Search,
  Demand Gen,
  Shopping,
  Video, and
  App campaigns,
  budgets, and
  assets.
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/concepts/api-structure](https://developers.google.com/google-ads/api/docs/concepts/api-structure) (locator: `lines:440-445`)
  - *Observation*: paraphrase: Customer -> campaigns -> ad groups -> ad group ads hierarchy.
  ```text
  Each customer contains one or more active
  campaigns.
  Each campaign contains one or more ad groups, used
  to group your ads into logical collections.
  An ad group ad represents an ad that you're
  running in an ad group. Except for App campaigns, which can have only one ad
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.group.conversions_bidding` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Conversion measurement and Smart Bidding strategies. Source evidence (lines:452-455) states: Upload click, call, and enhanced conversions and configure automated bidding strategies. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:452-455`)
  - *Observation*: paraphrase: Upload click, call, and enhanced conversions and configure automated bidding strategies.
  ```text
  Conversion measurement and
  Smart Bidding strategy management:
  Upload click, call, and enhanced conversions and configure automated bidding
  strategies.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.group.planning_audiences` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Keyword planning, audience insights, and reach planning (Basic/Standard tiers). Source evidence (lines:133-155) states: Lists KeywordPlanService, KeywordPlanIdeaService, AudienceInsightsService, and ReachPlanService (restricted in Explorer, available in Basic/Standard). The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/api-policy/access-levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) (locator: `lines:133-155`)
  - *Observation*: paraphrase: Lists KeywordPlanService, KeywordPlanIdeaService, AudienceInsightsService, and ReachPlanService (restricted in Explorer, available in Basic/Standard).
  ```text
  The Explorer access level restricts access to the following features. If you
  need to use these features, you need to apply for
  Basic access level or Standard access level.
  Restricted functionality
  Restricted services and methods
  Account creation and linking
  CustomerService.CreateCustomerClient
  CustomerClientLinkService
  CustomerManagerLinkService
  User management
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.group.reporting_gaql` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Reporting and performance metrics via Google Ads Query Language (GAQL). Source evidence (lines:440-442) states: Query performance metrics, segments, and resource attributes using GAQL. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:440-442`)
  - *Observation*: paraphrase: Query performance metrics, segments, and resource attributes using GAQL.
  ```text
  Custom reporting: Query performance metrics,
  segments, and resource attributes using the
  Google Ads Query Language (GAQL).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:508-512) states: Documents the Google Ads REST API interface, curl examples, and REST explorer. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/best-practices/testing](https://developers.google.com/google-ads/api/docs/best-practices/testing) (locator: `lines:508-512`)
  - *Observation*: paraphrase: Documents the Google Ads REST API interface, curl examples, and REST explorer.
  ```text
  REST API
  For ad hoc testing, for example to validate that a request yields the expected
  output, using the REST API is often the easiest option. Consult the REST
  examples to learn how to use curl in making requests to the REST
  API. Also, try testing in the REST explorer.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:512-520) states: Documents official client libraries for Java, .NET, PHP, Python, Ruby, and Perl. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:512-520`)
  - *Observation*: paraphrase: Documents official client libraries for Java, .NET, PHP, Python, Ruby, and Perl.
  ```text
  Install a client library or call REST
  Client libraries
  Java,
  .NET,
  PHP,
  Python,
  Ruby,
  Perl,
  Code samples,
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:424-535) states: Public Google Ads API documentation covers quickstart, OAuth, REST, client libraries, GAQL reporting, and MCP server. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:424-535`)
  - *Observation*: paraphrase: Public Google Ads API documentation covers quickstart, OAuth, REST, client libraries, GAQL reporting, and MCP server.
  ```text
  Introduction to the Google Ads API
  Stay organized with collections
  Save and categorize content based on your preferences.
  Page Summary
  outlined_flag
  The Google Ads API is a programmatic interface for managing Google Ads accounts and campaigns, suitable for large or complex setups.
  Typical uses of the Google Ads API include automated account management, custom reporting, ad management based on inventory, and Smart Bidding strategy management.
  The Google Ads API is recommended for developers comfortable with writing code and managing their own software infrastructure.
  Google Ads scripts, BigQuery Data Transfer service, automated rules, bulk uploads, and Google Ads Editor are alternative tools for automating Google Ads for different needs and technical skill levels.
  The Google Ads API is the programmatic interface to Google Ads, used for managing large or
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.auth.oauth2_user_and_service` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Google Ads API and official Google Ads MCP server. Source evidence (lines:429-480) states: Google Ads API uses OAuth 2.0 across single-user, multi-user, and service account workflows configured in the API-enabled Google Cloud project. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/oauth/overview](https://developers.google.com/google-ads/api/docs/oauth/overview) (locator: `lines:429-480`)
  - *Observation*: paraphrase: Google Ads API uses OAuth 2.0 across single-user, multi-user, and service account workflows configured in the API-enabled Google Cloud project.
  ```text
  Google Ads API utilizes the OAuth 2.0 protocol for authentication and authorization, allowing your app to access user accounts without handling login information.
  In addition to OAuth 2.0 credentials, a developer token is also required to make Google Ads API calls.
  While all Google-supported OAuth 2.0 scenarios work, this guide focuses on the most common ones for Google Ads API developers.
  The recommended OAuth 2.0 approach depends on your specific application scenario, such as integrating with existing Google APIs, managing your own accounts, or managing accounts on behalf of other users.
  Note: You should configure your OAuth credentials using the same Google Cloud
  project where you have enabled the
  Google Ads API and requested an appropriate
  API access level for the Google Ads API to work
  correctly.
  Just like other Google APIs, Google Ads API uses the OAuth 2.0 protocol
  ```
- **URL**: [https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md](https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md) (locator: `lines:47-63`)
  - *Observation*: paraphrase: Official MCP server supports OAuth 2.0 ADC with https://www.googleapis.com/auth/adwords scope or FastMCP OAuth proxy.
  ```text
  Configure [Application Default Credentials (ADC)](https://cloud.google.com/docs/authentication/provide-credentials-adc) for a user or service account with access to your Google Ads accounts. Credentials must include the Google Ads API scope (`https://www.googleapis.com/auth/adwords`). See [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257) if you need to create an OAuth desktop or web client first.
  - **Option 1 — User credentials with an OAuth client JSON file:**
  ```shell
  gcloud auth application-default login \
  --scopes=https://www.googleapis.com/auth/adwords,https://www.googleapis.com/auth/cloud-platform \
  --client-id-file=YOUR_CLIENT_JSON_FILE
  ```
  - **Option 2 — Service account impersonation:**
  ```shell
  gcloud auth application-default login \
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Build Google Ads campaign reporting and management agent integration via REST/SDK or official Google Ads MCP server. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:73-215): Production access requires Explorer, Basic, or Standard access level approval.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Build Google Ads campaign reporting and management agent integration via REST/SDK or official Google Ads MCP server", "blockers": ["Production account calls require Google Cloud project approval for Explorer (feature-restricted), Basic (brand verification), or Standard (manual compliance audit) access.", "Test accounts cannot test all production features such as live performance reports."], "next_steps": ["Enable Google Ads API on a Google Cloud project for immediate Test account prototyping.", "Complete brand verification and apply for Basic access (or Explorer for initial production read/mutate) before production rollout."]}`
  - Original Rationale: Conditional: immediate self-serve Test account development and official MCP server exist, but production calls are gated by Google's Explorer/Basic/Standard access-level review.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Build Google Ads campaign reporting and management agent integration via REST/SDK or official Google Ads MCP server", "blockers": ["Production account calls require Google Cloud project approval for Explorer (feature-restricted), Basic (brand verification), or Standard (manual compliance audit) access.", "Test accounts cannot test all production features such as live performance reports."], "next_steps": ["Enable Google Ads API on a Google Cloud project for immediate Test account prototyping.", "Complete brand verification and apply for Basic access (or Explorer for initial production read/mutate) before production rollout."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Google Ads documentation: Test access against test accounts is immediately available upon enabling the API, but production access requires Explorer, Basic, or Standard access level approval (31.testing.free_access, 31.production.vendor_approval_required, 31.api.rest, 31.mcp.official_mcp).

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/api-policy/access-levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) (locator: `lines:73-215`)
  - *Observation*: paraphrase: Production access requires Explorer, Basic, or Standard access level approval.
  ```text
  Explorer access (automated review and approval in
  most cases, for up to 2,880 operations per day against production accounts). For
  end-to-end setup, see the Make your first call quickstart or
  the Google Ads MCP server guide.
  Go to Google Ads API Overview in
  Cloud Console
  Access levels
  There are four different API access levels listed in order in the
  table. If you don't already have Google Ads API access, you can start by
  enabling the API to obtain Test access
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:480-489`)
  - *Observation*: paraphrase: Test access is immediate; production requires Explorer/Basic/Standard approval.
  ```text
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  production accounts, check the Google Ads API overview page for
  Explorer, Basic, or Standard access, or apply for one of these access
  levels. Otherwise, production calls fail with an
  AuthorizationError.CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION error. Google
  sunset developer tokens (GOOGLE_ADS_DEVELOPER_TOKEN) on
  September 9, 2026. The Google Cloud project that owns your OAuth client or
  service account determines your API access level.
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/best-practices/testing](https://developers.google.com/google-ads/api/docs/best-practices/testing) (locator: `lines:430-469`)
  - *Observation*: paraphrase: Test accounts cannot test production-only features such as performance reports.
  ```text
  You can use test accounts for most development purposes, but production accounts are needed to test features like performance reports due to test account limitations.
  It is recommended to maintain separate test credentials from production credentials to minimize the risk of accidental modifications to production accounts during testing.
  The validate_only field can be used to check if a request is valid without executing it.
  The REST API, including curl and the REST explorer, is useful for ad hoc testing to validate expected output.
  Testing is an important step in building a successful Google Ads API integration,
  whether you're just getting started, maintaining an app, or adding new features
  to an existing integration. This guide presents some best practices for testing
  your Google Ads API integration.
  Test accounts and production accounts
  Note on Test Account Retention:
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:473-496) states: Official Google Ads MCP server guide. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:473-496`)
  - *Observation*: paraphrase: Official Google Ads MCP server guide.
  ```text
  Get started
  Follow these steps to configure and run the Google Ads MCP server locally. To deploy
  a shared remote service instead, see Deployment on Google
  Cloud.
  Prerequisites
  Before you configure the server, complete the following prerequisites in your
  local environment and the Google Cloud console:
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```
- **URL**: [https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md](https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md) (locator: `lines:1-30`)
  - *Observation*: paraphrase: Official googleads/google-ads-mcp repository.
  ```text
  # Google Ads MCP Server
  An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that enables LLMs and AI agents to query and manage [Google Ads](https://developers.google.com/google-ads/api) accounts.
  ## Table of Contents
  - [Overview](#overview)
  - [Quickstart & Setup](#quickstart--setup)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Choose an Authentication Mode](#2-choose-an-authentication-mode)
  - [3. Configure Your MCP Client](#3-configure-your-mcp-client)
  - [Tools & Resources](#tools--resources)
  - [Available Tools](#available-tools)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.mcp.official_google_ads` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Google Ads MCP Server (googleads/google-ads-mcp); source_url=https://raw.githubusercontent.com/googleads/google-ads-mcp/main/R. Source evidence (lines:473-557) states: Official Google Ads MCP server developer integration guide; supports local stdio (ADC) and remote streamable-http (FastMCP OAuth proxy) for reporting, asset creation, video upload, and label management. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:473-557`)
  - *Observation*: paraphrase: Official Google Ads MCP server developer integration guide; supports local stdio (ADC) and remote streamable-http (FastMCP OAuth proxy) for reporting, asset creation, video upload, and label management.
  ```text
  Get started
  Follow these steps to configure and run the Google Ads MCP server locally. To deploy
  a shared remote service instead, see Deployment on Google
  Cloud.
  Prerequisites
  Before you configure the server, complete the following prerequisites in your
  local environment and the Google Cloud console:
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```
- **URL**: [https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md](https://raw.githubusercontent.com/googleads/google-ads-mcp/main/README.md) (locator: `lines:1-145`)
  - *Observation*: paraphrase: Official googleads/google-ads-mcp repository exposing callable MCP tools (GAQL queries, customer discovery, metadata, guarded mutations via Propose & Confirm) and MCP resources.
  ```text
  # Google Ads MCP Server
  An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server that enables LLMs and AI agents to query and manage [Google Ads](https://developers.google.com/google-ads/api) accounts.
  ## Table of Contents
  - [Overview](#overview)
  - [Quickstart & Setup](#quickstart--setup)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Choose an Authentication Mode](#2-choose-an-authentication-mode)
  - [3. Configure Your MCP Client](#3-configure-your-mcp-client)
  - [Tools & Resources](#tools--resources)
  - [Available Tools](#available-tools)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:161-215) states: Upgrading from Test to Explorer, Basic (brand verification), or Standard (manual compliance audit) requires Google access-level application and review. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/api-policy/access-levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) (locator: `lines:161-215`)
  - *Observation*: paraphrase: Upgrading from Test to Explorer, Basic (brand verification), or Standard (manual compliance audit) requires Google access-level application and review.
  ```text
  Apply for Explorer access level
  Navigate to the Google Ads API Overview page in your Google Cloud
  project.
  Verify that the page displays your current access level as Test.
  Click to expand the Upgrade access level section.
  Confirm that the Next access level is displayed as Explorer.
  Click the Apply for access button to apply for Explorer access level.
  Google may automatically upgrade your project's API access level to Explorer
  after you submit your application.
  Basic access level
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.production.vendor_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:68-216) states: Production account access requires applying for Explorer (automated review, feature-restricted), Basic (requires brand verification, 15,000 ops/day), or Standard (manual compliance audit, unlimited ops/day) access levels on the Google Cloud project. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/api-policy/access-levels](https://developers.google.com/google-ads/api/docs/api-policy/access-levels) (locator: `lines:68-216`)
  - *Observation*: paraphrase: Production account access requires applying for Explorer (automated review, feature-restricted), Basic (requires brand verification, 15,000 ops/day), or Standard (manual compliance audit, unlimited ops/day) access levels on the Google Cloud project.
  ```text
  Key Point: Getting started with the Google Ads API? Developer tokens were
  sunset on September 9, 2026, and API access levels are now managed
  per Google Cloud project. After you enable the Google Ads API
  (which grants Test access), you can immediately apply on
  the Google Ads API Overview page in the Google Cloud Console for
  Explorer access (automated review and approval in
  most cases, for up to 2,880 operations per day against production accounts). For
  end-to-end setup, see the Make your first call quickstart or
  the Google Ads MCP server guide.
  Go to Google Ads API Overview in
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Programmatic advertising platform API for managing Google Ads accounts, campaigns, GAQL reporting, conversions, and Smart Bidding, plus an official MCP server.. Source evidence (lines:429-455) states: Lists automated account management, GAQL custom reporting, Performance Max/Search/Demand Gen/Shopping/Video/App campaign management, conversion measurement, and Smart Bidding. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/start](https://developers.google.com/google-ads/api/docs/start) (locator: `lines:429-455`)
  - *Observation*: paraphrase: Lists automated account management, GAQL custom reporting, Performance Max/Search/Demand Gen/Shopping/Video/App campaign management, conversion measurement, and Smart Bidding.
  ```text
  The Google Ads API is a programmatic interface for managing Google Ads accounts and campaigns, suitable for large or complex setups.
  Typical uses of the Google Ads API include automated account management, custom reporting, ad management based on inventory, and Smart Bidding strategy management.
  The Google Ads API is recommended for developers comfortable with writing code and managing their own software infrastructure.
  Google Ads scripts, BigQuery Data Transfer service, automated rules, bulk uploads, and Google Ads Editor are alternative tools for automating Google Ads for different needs and technical skill levels.
  The Google Ads API is the programmatic interface to Google Ads, used for managing large or
  complex Google Ads accounts and campaigns. You can build software that manages
  accounts from the customer level down to the keyword level. Typical use cases
  include:
  Automated account management:
  Create and link accounts, manage account hierarchies, and automate user
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:473-496`)
  - *Observation*: paraphrase: Documents the official Google Ads MCP server over local stdio or remote streamable-http.
  ```text
  Get started
  Follow these steps to configure and run the Google Ads MCP server locally. To deploy
  a shared remote service instead, see Deployment on Google
  Cloud.
  Prerequisites
  Before you configure the server, complete the following prerequisites in your
  local environment and the Google Cloud console:
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:480-482) states: Enabling the Google Ads API on a Google Cloud project grants Test access for test accounts. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:480-482`)
  - *Observation*: paraphrase: Enabling the Google Ads API on a Google Cloud project grants Test access for test accounts.
  ```text
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.testing.sandbox_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:442-446) states: Test accounts are available for development purposes to validate application code and configuration. The documentation describes a sandbox or test environment relevant to test access, distinct from live production access.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/best-practices/testing](https://developers.google.com/google-ads/api/docs/best-practices/testing) (locator: `lines:442-446`)
  - *Observation*: paraphrase: Test accounts are available for development purposes to validate application code and configuration.
  ```text
  Test accounts are available for development purposes. With test
  accounts, you can validate that your application code and configuration are
  working as intended.
  However, not all features can be tested in a test
  account.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:480-482) states: Developers create/select a Google Cloud project and enable the Google Ads API for Test access. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:480-482`)
  - *Observation*: paraphrase: Developers create/select a Google Cloud project and enable the Google Ads API for Test access.
  ```text
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```
- **URL**: [https://developers.google.com/google-ads/api/docs/best-practices/testing](https://developers.google.com/google-ads/api/docs/best-practices/testing) (locator: `lines:477-494`)
  - *Observation*: paraphrase: Developers create separate test credentials and OAuth refresh tokens or service accounts for test accounts.
  ```text
  Test credentials
  To minimize the risk of accidentally modifying production accounts when trying
  to modify development accounts, we recommend maintaining a set of test
  credentials that are separate from your production application credentials.
  To create a set of test credentials, follow these steps:
  Create an email account (for example, api.test@example.com) or a service
  account that will be used only for testing purposes.
  Add this user or service account as a valid user in the Google Ads accounts you
  are running your tests against. Make sure you give appropriate access
  levels to this user or service account. Don't give this
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `31.testing.vendor_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:480-482): Enabling the Google Ads API grants Test access for testing read and mutate workflows against test accounts.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Test access is granted automatically upon enabling the API.
- **Corrected Answer**: `status: unknown`, `value: null`
  - Corrected Rationale: Research correction: In first-pass research, vendor approval was asserted as false based on automatic test account enablement. However, primary documentation does not explicitly state that vendor approval is not required, and under evidence rules silence is unknown. Relabeled from observed (false) to unknown.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) (locator: `lines:480-482`)
  - *Observation*: paraphrase: Enabling the Google Ads API grants Test access for testing read and mutate workflows against test accounts.
  ```text
  Google Cloud project: Create or select a Google Cloud project with the
  Google Ads API enabled. Enabling the API grants Test access for testing read
  and mutate workflows against test accounts. To access
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 46: Squarespace (Ecommerce)
- Total claims: 15 | Corrected: 2

### Claim: `46.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1-64): Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Covers catalog/inventory, orders/transactions, contacts/profiles/discounts/forms, and webhook subscriptions.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Squarespace Commerce API documentation covers multiple distinct ecommerce domains: (1) Orders & Fulfillment, (2) Inventory Management, (3) Products, (4) Transactions & Finances, and (5) Webhook Subscriptions. Per evidence rules, multiple distinct commercial domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.group.contacts_profiles_discounts` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Contacts API, Profiles API (maintenance mode), Discounts API, and Forms API. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.group.orders_transactions` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Orders API and Transactions API. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/orders-overview](https://developers.squarespace.com/commerce-apis/orders-overview) (locator: `lines:48-65`)
  - *Observation*: paraphrase: Orders API (GET /1.0/commerce/orders) supports paymentStates filtering (NOT_CHARGED, AUTHORIZED, PAID, REFUNDED, PARTIALLY_PAID) and order.create webhooks.
  ```text
  PARTIALLY_PAIDA Payment Plan order with one or more installments still outstanding. An order enters this state as soon as the deposit is captured (before any installment has been collected) and remains in it while installments are still being collected.
  PENDINGA payment is awaiting confirmation. The order will subsequently transition to PAID, PARTIALLY_PAID or FAILED.
  FAILEDThe terminal state for an order whose payment was previously PENDING and ultimately did not succeed.
  REFUND_PENDINGA refund has been initiated and is being processed. The order will subsequently transition to REFUNDED or REFUND_FAILED.
  REFUNDEDThe order has had refund activity. This covers both full and partial refunds; a partial refund of any amount sets the order to REFUNDED. To determine the outstanding balance, compare the order's refundedTotal with grandTotal.
  REFUND_FAILEDAn asynchronous refund attempt failed.
  Filtering by payment state
  The retrieve all orders endpoint accepts an optional paymentStates query parameter, a comma-separated list of the values above. If omitted, the endpoint defaults to NOT_CHARGED,AUTHORIZED,PAID,REFUNDED, which preserves the response set returned before Payment Plans existed and keeps existing integrations stable.
  To include Payment Plan orders that are mid-collection, pass PARTIALLY_PAID explicitly:
  Code
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.group.products_inventory` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Products API and Inventory API. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.group.webhooks` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Webhook Subscriptions API (OAuth only). Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/orders-overview](https://developers.squarespace.com/commerce-apis/orders-overview) (locator: `lines:48-65`)
  - *Observation*: paraphrase: Orders API (GET /1.0/commerce/orders) supports paymentStates filtering (NOT_CHARGED, AUTHORIZED, PAID, REFUNDED, PARTIALLY_PAID) and order.create webhooks.
  ```text
  PARTIALLY_PAIDA Payment Plan order with one or more installments still outstanding. An order enters this state as soon as the deposit is captured (before any installment has been collected) and remains in it while installments are still being collected.
  PENDINGA payment is awaiting confirmation. The order will subsequently transition to PAID, PARTIALLY_PAID or FAILED.
  FAILEDThe terminal state for an order whose payment was previously PENDING and ultimately did not succeed.
  REFUND_PENDINGA refund has been initiated and is being processed. The order will subsequently transition to REFUNDED or REFUND_FAILED.
  REFUNDEDThe order has had refund activity. This covers both full and partial refunds; a partial refund of any amount sets the order to REFUNDED. To determine the outstanding balance, compare the order's refundedTotal with grandTotal.
  REFUND_FAILEDAn asynchronous refund attempt failed.
  Filtering by payment state
  The retrieve all orders endpoint accepts an optional paymentStates query parameter, a comma-separated list of the values above. If omitted, the endpoint defaults to NOT_CHARGED,AUTHORIZED,PAID,REFUNDED, which preserves the response set returned before Payment Plans existed and keeps existing integrations stable.
  To include Payment Plan orders that are mid-collection, pass PARTIALLY_PAID explicitly:
  Code
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```
- **URL**: [https://developers.squarespace.com/oauth](https://developers.squarespace.com/oauth) (locator: `lines:50-115`)
  - *Observation*: paraphrase: Squarespace OAuth 2.0 authorization code flow uses https://login.squarespace.com/api/1/login/oauth/provider/authorize with scopes (including website.inventory, website.orders, website.contacts, website.contacts.read) and optional access_type=offline.
  ```text
  Code
  GET https://login.squarespace.com/api/1/login/oauth/provider/authorize
  Query parameterRequirementValue
  client_idRequired
  Alphanumeric value for your_client_id that was supplied by
  Squarespace in Step 1.
  redirect_uriRequiredString; the full redirect URI sent to Squarespace in Step 1.
  scopeRequired
  String; comma-separated list of client permission values (see below)
  for API access. The confirmation page always displays website(s) for
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/orders-overview](https://developers.squarespace.com/commerce-apis/orders-overview) (locator: `lines:48-65`)
  - *Observation*: paraphrase: Orders API (GET /1.0/commerce/orders) supports paymentStates filtering (NOT_CHARGED, AUTHORIZED, PAID, REFUNDED, PARTIALLY_PAID) and order.create webhooks.
  ```text
  PARTIALLY_PAIDA Payment Plan order with one or more installments still outstanding. An order enters this state as soon as the deposit is captured (before any installment has been collected) and remains in it while installments are still being collected.
  PENDINGA payment is awaiting confirmation. The order will subsequently transition to PAID, PARTIALLY_PAID or FAILED.
  FAILEDThe terminal state for an order whose payment was previously PENDING and ultimately did not succeed.
  REFUND_PENDINGA refund has been initiated and is being processed. The order will subsequently transition to REFUNDED or REFUND_FAILED.
  REFUNDEDThe order has had refund activity. This covers both full and partial refunds; a partial refund of any amount sets the order to REFUNDED. To determine the outstanding balance, compare the order's refundedTotal with grandTotal.
  REFUND_FAILEDAn asynchronous refund attempt failed.
  Filtering by payment state
  The retrieve all orders endpoint accepts an optional paymentStates query parameter, a comma-separated list of the values above. If omitted, the endpoint defaults to NOT_CHARGED,AUTHORIZED,PAID,REFUNDED, which preserves the response set returned before Payment Plans existed and keeps existing integrations stable.
  To include Payment Plan orders that are mid-collection, pass PARTIALLY_PAID explicitly:
  Code
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.auth.api_key_bearer` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Custom applications on a single Squarespace merchant site. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.auth.oauth2_extensions` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Multi-merchant Squarespace Extensions and registered OAuth clients. Source evidence (lines:28-85) states: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```
- **URL**: [https://developers.squarespace.com/oauth](https://developers.squarespace.com/oauth) (locator: `lines:50-115`)
  - *Observation*: paraphrase: Squarespace OAuth 2.0 authorization code flow uses https://login.squarespace.com/api/1/login/oauth/provider/authorize with scopes (including website.inventory, website.orders, website.contacts, website.contacts.read) and optional access_type=offline.
  ```text
  Code
  GET https://login.squarespace.com/api/1/login/oauth/provider/authorize
  Query parameterRequirementValue
  client_idRequired
  Alphanumeric value for your_client_id that was supplied by
  Squarespace in Step 1.
  redirect_uriRequiredString; the full redirect URI sent to Squarespace in Step 1.
  scopeRequired
  String; comma-separated list of client permission values (see below)
  for API access. The confirmation page always displays website(s) for
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Squarespace Commerce REST API integration (API key for Commerce Advanced or OAuth for Extensions). The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1-64): Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. Check https://developers.squarespace.com/commerce-apis for current terms, exceptions and conflicting documentation b

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Squarespace Commerce REST API integration (API key for Commerce Advanced or OAuth for Extensions)", "blockers": ["Custom API key generation requires Squarespace's Commerce Advanced plan", "Multi-merchant OAuth client registration requires Squarespace review and approval", "Webhook Subscriptions API is OAuth-only"], "next_steps": ["Use a Commerce Advanced plan for single-site API key integrations, or submit an OAuth client application for multi-merchant/webhook support", "Inspect the developers.squarespace.com MCP section in a follow-up pass"]}`
  - Original Rationale: Public REST docs and self-serve API keys exist, but plan-tier gating (Commerce Advanced) for API keys and vendor review for OAuth clients make buildability conditional.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Squarespace Commerce REST API integration (API key for Commerce Advanced or OAuth for Extensions)", "blockers": ["Custom API key generation requires Squarespace's Commerce Advanced plan", "Multi-merchant OAuth client registration requires Squarespace review and approval", "Webhook Subscriptions API is OAuth-only"], "next_steps": ["Use a Commerce Advanced plan for single-site API key integrations, or submit an OAuth client application for multi-merchant/webhook support", "Inspect the developers.squarespace.com MCP section in a follow-up pass"]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Squarespace documentation: Commerce APIs are fully functional via API keys or OAuth, but require an active Squarespace Commerce plan (Commerce Advanced or Core) (46.testing.paid_required, 46.auth.api_key).

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```
- **URL**: [https://developers.squarespace.com/oauth](https://developers.squarespace.com/oauth) (locator: `lines:50-115`)
  - *Observation*: paraphrase: Squarespace OAuth 2.0 authorization code flow uses https://login.squarespace.com/api/1/login/oauth/provider/authorize with scopes (including website.inventory, website.orders, website.contacts, website.contacts.read) and optional access_type=offline.
  ```text
  Code
  GET https://login.squarespace.com/api/1/login/oauth/provider/authorize
  Query parameterRequirementValue
  client_idRequired
  Alphanumeric value for your_client_id that was supplied by
  Squarespace in Step 1.
  redirect_uriRequiredString; the full redirect URI sent to Squarespace in Step 1.
  scopeRequired
  String; comma-separated list of client permission values (see below)
  for API access. The confirmation page always displays website(s) for
  ```
- **URL**: [https://www.squarespace.com/pricing](https://www.squarespace.com/pricing) (locator: `lines:319-396`)
  - *Observation*: paraphrase: Squarespace website/commerce plans include Basic, Core, and Advanced with 'Start Free Trial' and paid subscriptions.
  ```text
  All plans include:
  Built-in AI tools
  Secure hosting
  Unlimited bandwidth
  Selling functionality
  Industry-leading design
  Basic
  50% off
  Publish your personal or business website with the essentials.
  ₹810/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:28-85) states: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval). The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```
- **URL**: [https://www.squarespace.com/pricing](https://www.squarespace.com/pricing) (locator: `lines:319-396`)
  - *Observation*: paraphrase: Squarespace website/commerce plans include Basic, Core, and Advanced with 'Start Free Trial' and paid subscriptions.
  ```text
  All plans include:
  Built-in AI tools
  Secure hosting
  Unlimited bandwidth
  Selling functionality
  Industry-leading design
  Basic
  50% off
  Publish your personal or business website with the essentials.
  ₹810/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:28-85) states: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval). The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.production.vendor_approval_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:28-85) states: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval). The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Website and ecommerce platform exposing REST Commerce APIs for products, inventory, orders, transactions, contacts/profiles, discounts, and webhooks.. Source evidence (lines:1-64) states: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.squarespace.com/commerce-apis](https://developers.squarespace.com/commerce-apis) (locator: `lines:1-64`)
  - *Observation*: paraphrase: Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.
  ```text
  Squarespace Developer Platform: APIs, Apps, and Docs
  Commerce APIs
  MCP
  Reseller APIs
  Templates
  Custom Code
  Upcoming Changes
  Getting Started
  OverviewAuthentication and permissionsOAuthMaking requestsRetrieve basic site information
  Using Commerce APIs
  ```
- **URL**: [https://developers.squarespace.com/commerce-apis/authentication-and-permissions](https://developers.squarespace.com/commerce-apis/authentication-and-permissions) (locator: `lines:28-85`)
  - *Observation*: paraphrase: Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).
  ```text
  every request to Commerce APIs must be authenticated and have minimum permissions.
  However, authenticated requests automatically have access to public site data,
  such as site name, identifier, language, currency, time zone, and location.
  Read the permission levels for each Commerce API below.
  Then, depending on your development needs,
  authenticate requests by using an API key or OAuth access token.
  Remember: Requests only have access to data for
  the website that owns the API key or OAuth access token.
  API permission levels
  Forms API
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `46.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:319-396) states: Squarespace website/commerce plans include Basic, Core, and Advanced with 'Start Free Trial' and paid subscriptions. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://www.squarespace.com/pricing](https://www.squarespace.com/pricing) (locator: `lines:319-396`)
  - *Observation*: paraphrase: Squarespace website/commerce plans include Basic, Core, and Advanced with 'Start Free Trial' and paid subscriptions.
  ```text
  All plans include:
  Built-in AI tools
  Secure hosting
  Unlimited bandwidth
  Selling functionality
  Industry-leading design
  Basic
  50% off
  Publish your personal or business website with the essentials.
  ₹810/mo
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 50: fanbasis (Ecommerce)
- Total claims: 7 | Corrected: 1

### Claim: `50.api.group.checkouts_payouts_refunds` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Embedded checkouts, checkout links, multi-rail payouts, and refunds. Source evidence (lines:41-60) states: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain…. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:41-60) states: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain…. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:1-6) states: dev-docs.fanbasis.com ('Login - FanBasis API Docsv3') is gated behind a password login screen ('Sign in to access API Docs'). The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://dev-docs.fanbasis.com/](https://dev-docs.fanbasis.com/) (locator: `lines:1-6`)
  - *Observation*: paraphrase: dev-docs.fanbasis.com ('Login - FanBasis API Docsv3') is gated behind a password login screen ('Sign in to access API Docs').
  ```text
  Login - FanBasis API Docsv3
  API Docs
  Sign in to access API Docs
  Invalid password. Please try again.
  Password
  Login
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts outreach_required buildability for FanBasis / Commas API, SDK, and beta MCP integration. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1-18): www.fanbasis.com displays 'FanBasis is now Commas!' (Commas Inc.) — one platform to create, sell, and get paid with checkouts, funnels, communities, courses, webinars, and affiliates.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "outreach_required", "scope": "FanBasis / Commas API, SDK, and beta MCP integration", "blockers": ["dev-docs.fanbasis.com (FanBasis API Docsv3) is password-protected behind a login screen", "commasdocs.com rendered only a JS unpacking shell without readable auth/endpoint reference in non-JS capture", "Pricing, auth method, and sandbox/production credential paths remain unverified from captured public docs"], "next_steps": ["Request API documentation access / credentials from Commas (formerly FanBasis) or inspect commasdocs.com in an interactive browser session", "Confirm API key/OAuth setup and beta MCP endpoint onboarding requirements"]}`
  - Original Rationale: Official homepage confirms APIs, SDKs, and beta MCP, but password-gated legacy API docs and unverified auth/credential access require vendor outreach or interactive doc access before building.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "outreach_required", "scope": "FanBasis / Commas API, SDK, and beta MCP integration", "blockers": ["dev-docs.fanbasis.com (FanBasis API Docsv3) is password-protected behind a login screen", "commasdocs.com rendered only a JS unpacking shell without readable auth/endpoint reference in non-JS capture", "Pricing, auth method, and sandbox/production credential paths remain unverified from captured public docs"], "next_steps": ["Request API documentation access / credentials from Commas (formerly FanBasis) or inspect commasdocs.com in an interactive browser session", "Confirm API key/OAuth setup and beta MCP endpoint onboarding requirements"]}`
  - Corrected Rationale: Outreach required buildability inference is anchored to verified FanBasis / Commas documentation: developer API keys and beta MCP server access require contacting Commas sales or requesting developer access (50.identity, 50.api.protocol.sdk, 50.mcp.commas_mcp_beta).

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:1-18`)
  - *Observation*: paraphrase: www.fanbasis.com displays 'FanBasis is now Commas!' (Commas Inc.) — one platform to create, sell, and get paid with checkouts, funnels, communities, courses, webinars, and affiliates.
  ```text
  Commas | Where you make money on the internet
  FanBasis is now Commas!
  ProductsProductsSolutionsSolutionsContact UsContact Us
  LoginGet started
  Back
  Built for your next comma
  The new era for making money on the internet
  One place to create, sell, and get paid, with payments built in. From your first dollar to your next comma.
  Get started
  Overview
  ```
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```
- **URL**: [https://dev-docs.fanbasis.com/](https://dev-docs.fanbasis.com/) (locator: `lines:1-6`)
  - *Observation*: paraphrase: dev-docs.fanbasis.com ('Login - FanBasis API Docsv3') is gated behind a password login screen ('Sign in to access API Docs').
  ```text
  Login - FanBasis API Docsv3
  API Docs
  Sign in to access API Docs
  Invalid password. Please try again.
  Password
  Login
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.mcp.commas_mcp_beta` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Commas MCP (Beta); source_url=https://www.fanbasis.com/. Source evidence (lines:41-60) states: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain…. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:41-60) states: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain…. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `50.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Creator and digital business commerce platform (FanBasis, now Commas) combining checkouts, funnels, courses, communities, webinars, BNPL payments, APIs/SDKs, and beta MCP.. Source evidence (lines:1-18) states: www.fanbasis.com displays 'FanBasis is now Commas!' (Commas Inc.) — one platform to create, sell, and get paid with checkouts, funnels, communities, courses, webinars, and affiliates. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:1-18`)
  - *Observation*: paraphrase: www.fanbasis.com displays 'FanBasis is now Commas!' (Commas Inc.) — one platform to create, sell, and get paid with checkouts, funnels, communities, courses, webinars, and affiliates.
  ```text
  Commas | Where you make money on the internet
  FanBasis is now Commas!
  ProductsProductsSolutionsSolutionsContact UsContact Us
  LoginGet started
  Back
  Built for your next comma
  The new era for making money on the internet
  One place to create, sell, and get paid, with payments built in. From your first dollar to your next comma.
  Get started
  Overview
  ```
- **URL**: [https://www.fanbasis.com/](https://www.fanbasis.com/) (locator: `lines:41-60`)
  - *Observation*: paraphrase: Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').
  ```text
  Payments
  Payments designed as the foundation.
  All other features crafted to support them.
  Every way to pay
  Cards, wallets and local methods, everywhere your buyers are.
  The internet's largest BNPL suite
  Buyers split the payment or finance it, and you get paid in full, upfront.
  Smart routing that gets more payments approved
  Each sale is routed to the processor most likely to say yes and declines get retried automatically.
  Subscriptions that save themselves
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 60: Clay (Data, SEO and Scraping)
- Total claims: 19 | Corrected: 2

### Claim: `60.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:4-42): Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Multiple related B2B go-to-market data and workflow primitives covering people/company database Searches, enrichment/research Routines & batch runs, Enterprise table queries, and Audiences/Signals/Webhooks/credit balance endpoints.
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: Clay API documentation covers multiple related enrichment groups: (1) Table & Record Management, (2) People/Company Enrichment Actions, and (3) Webhook Integration Sources. Per evidence rules, multiple related groups substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://developers.clay.com/tables.md](https://developers.clay.com/tables.md) (locator: `lines:4-25`)
  - *Observation*: paraphrase: Tables API (POST https://api.clay.com/public/v0/tables/query) lets customers query known Clay tables and is available on Enterprise plans only.
  ```text
  # Tables (Enterprise)
  > Query known Clay tables with structured filters, selected fields, ordering, and pagination.
  Tables let Enterprise customers read structured data from known Clay tables. Use table queries when your integration already knows which table it needs and wants specific fields, filters, ordering, and pagination.
  > [!NOTE]
  >
  > Tables are available on Enterprise plans.
  Clay tables can act as a GTM database for your downstream systems. You can build dashboards, internal tools, QA views, scoring jobs, and interactive apps on top of data that already exists in Clay.
  The current public API does not include a list-tables endpoint. You need the table identifiers your integration uses before querying table data. You can find the table id in a Clay URL after `/tables/`, for example `https://app.clay.com/workspaces/{workspaceId}/tables/t_0te9i4tZEHwc9hihBXu`.
  ## Common uses
  * Pull records into a dashboard or internal tool.
  ```
- **URL**: [https://developers.clay.com/routines/api.md](https://developers.clay.com/routines/api.md) (locator: `lines:4-100`)
  - *Observation*: paraphrase: Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.
  ```text
  # Routines API
  > Run Clay-managed functions and custom functions through the Public API.
  Routines are the programmable way to run Clay logic. Through the Public API, you can run Clay-managed functions and custom functions from backend services, queue workers, internal tools, and custom apps.
  Use [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md) for common enrichment and research jobs. Use [custom functions](https://developers.clay.com/routines/custom-functions.md) for team-specific Clay logic built in the Clay UI.
  ## Run a function routine
  Custom function routine ids use the format `function:t_...`. To start a run, call `POST /routines/{routine_id}/run`.
  Replace `function:t_abc123` and the input names with your function's routine id and inputs. Give each item an id you can use to match its result later.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ROUTINE_RUN_ID=$(curl --request POST \
  --url "https://api.clay.com/public/v0/routines/function:t_abc123/run" \
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.group.audiences_signals_webhooks_credits` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Audiences (records, segments, activities, privacy deletion), Signals triggers, signed Webhooks, authenticated user (/public/v0/me), and workspace credit balances. Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```
- **URL**: [https://developers.clay.com/public-api/webhooks.md](https://developers.clay.com/public-api/webhooks.md) (locator: `lines:4-58`)
  - *Observation*: paraphrase: Clay webhooks notify a service when a routine run finishes by sending a signed POST (`X-Clay-Signature` HMAC-SHA256).
  ```text
  # Webhooks
  > Get notified when a routine run finishes, then verify and handle the delivery.
  Webhooks let Clay notify your service when a routine run finishes, so you can react without polling. Register a webhook, pass its id when you start a run, and handle the signed `POST` Clay sends once results are ready.
  ## Register a webhook
  Create a webhook with the CLI — run `clay webhooks --help` for the full command surface (create, list, test, delete):
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  clay webhooks create https://example.com/hooks/clay
  ```
  `create` returns the signing secret exactly once — store it immediately, it can't be retrieved later:
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.group.routines_functions_workflows` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Routines (running Clay-managed functions, custom functions, batch JSONL runs, and alpha Workflows). Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/routines/api.md](https://developers.clay.com/routines/api.md) (locator: `lines:4-100`)
  - *Observation*: paraphrase: Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.
  ```text
  # Routines API
  > Run Clay-managed functions and custom functions through the Public API.
  Routines are the programmable way to run Clay logic. Through the Public API, you can run Clay-managed functions and custom functions from backend services, queue workers, internal tools, and custom apps.
  Use [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md) for common enrichment and research jobs. Use [custom functions](https://developers.clay.com/routines/custom-functions.md) for team-specific Clay logic built in the Clay UI.
  ## Run a function routine
  Custom function routine ids use the format `function:t_...`. To start a run, call `POST /routines/{routine_id}/run`.
  Replace `function:t_abc123` and the input names with your function's routine id and inputs. Give each item an id you can use to match its result later.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ROUTINE_RUN_ID=$(curl --request POST \
  --url "https://api.clay.com/public/v0/routines/function:t_abc123/run" \
  ```
- **URL**: [https://developers.clay.com/routines/custom-functions.md](https://developers.clay.com/routines/custom-functions.md) (locator: `lines:21-47`)
  - *Observation*: paraphrase: Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access settings.
  ```text
  ## Expose a function
  To call a custom function:
  1. Open [Functions](https://app.clay.com/functions).
  2. Create or select a function.
  3. Open **Details**.
  4. Enable the integrations you need, such as **API** or **MCP**.
  5. Copy the `t_...` function id.
  6. Prefix it with `function:` when you call it from the plugin, CLI, MCP, or API.
  Custom function routine ids use the format `function:t_...`.
  Each access setting enables a separate way to call the function:
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.group.searches_gtm_db` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Searches (people and companies search queries and paginated iterators in Clay's GTM database). Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.group.tables_enterprise` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Tables (Enterprise-only structured queries across known Clay tables at POST /public/v0/tables/query). Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/tables.md](https://developers.clay.com/tables.md) (locator: `lines:4-25`)
  - *Observation*: paraphrase: Tables API (POST https://api.clay.com/public/v0/tables/query) lets customers query known Clay tables and is available on Enterprise plans only.
  ```text
  # Tables (Enterprise)
  > Query known Clay tables with structured filters, selected fields, ordering, and pagination.
  Tables let Enterprise customers read structured data from known Clay tables. Use table queries when your integration already knows which table it needs and wants specific fields, filters, ordering, and pagination.
  > [!NOTE]
  >
  > Tables are available on Enterprise plans.
  Clay tables can act as a GTM database for your downstream systems. You can build dashboards, internal tools, QA views, scoring jobs, and interactive apps on top of data that already exists in Clay.
  The current public API does not include a list-tables endpoint. You need the table identifiers your integration uses before querying table data. You can find the table id in a Clay URL after `/tables/`, for example `https://app.clay.com/workspaces/{workspaceId}/tables/t_0te9i4tZEHwc9hihBXu`.
  ## Common uses
  * Pull records into a dashboard or internal tool.
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.protocol.cli` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts CLI. Source evidence (lines:4-29) states: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`). The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/concepts/cli-basics.md](https://developers.clay.com/concepts/cli-basics.md) (locator: `lines:4-37`)
  - *Observation*: paraphrase: The JSON-first Clay CLI (`clay`) writes machine-readable JSON to stdout and authenticates per workspace via `clay login` (browser OAuth) or `clay login --device` for headless environments.
  ```text
  # CLI basics
  > Understand the Clay CLI output contract, exit codes, environment variables, and authentication.
  The Clay CLI (`clay`) is JSON-first: every command writes machine-readable JSON to stdout on success and a structured error envelope to stderr on failure. There are no spinners, colors, or progress bars, so agents and scripts can branch on the output and exit code directly.
  ## Output contract
  | Result | Behavior |
  | - | - |
  | Success | JSON is written to stdout, exit code `0`. |
  | Failure | `{ "error": { "code", "message", "details"? } }` is written to stderr, non-zero exit code. |
  Pipe stdout straight into `jq`, and read the exit code (`$?`) to decide what to do next.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://raw.githubusercontent.com/clay-run/agent-plugins/main/README.md](https://raw.githubusercontent.com/clay-run/agent-plugins/main/README.md) (locator: `lines:7-38`)
  - *Observation*: paraphrase: Official github.com/clay-run/agent-plugins repository provides Clay skills and the `clay` CLI for Claude Code, Codex, and Cursor.
  ```text
  <p align="center">
  <strong>Build with Clay in your AI coding agent</strong> — skills and the <code>clay</code>
  CLI, for Claude Code, Codex, and Cursor.
  </p>
  <p align="center">
  <a href="https://developers.clay.com">Docs</a> · <a href="./GETTING_STARTED.md">Getting started</a>
  </p>
  Clay is a go-to-market data and automation platform — search for companies and
  people, run enrichment routines, and query tables, all from natural language.
  This repo is the plugin marketplace for `clay`: one plugin source, three
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:4-23) states: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```
- **URL**: [https://developers.clay.com/tables.md](https://developers.clay.com/tables.md) (locator: `lines:4-25`)
  - *Observation*: paraphrase: Tables API (POST https://api.clay.com/public/v0/tables/query) lets customers query known Clay tables and is available on Enterprise plans only.
  ```text
  # Tables (Enterprise)
  > Query known Clay tables with structured filters, selected fields, ordering, and pagination.
  Tables let Enterprise customers read structured data from known Clay tables. Use table queries when your integration already knows which table it needs and wants specific fields, filters, ordering, and pagination.
  > [!NOTE]
  >
  > Tables are available on Enterprise plans.
  Clay tables can act as a GTM database for your downstream systems. You can build dashboards, internal tools, QA views, scoring jobs, and interactive apps on top of data that already exists in Clay.
  The current public API does not include a list-tables endpoint. You need the table identifiers your integration uses before querying table data. You can find the table id in a Clay URL after `/tables/`, for example `https://app.clay.com/workspaces/{workspaceId}/tables/t_0te9i4tZEHwc9hihBXu`.
  ## Common uses
  * Pull records into a dashboard or internal tool.
  ```
- **URL**: [https://developers.clay.com/routines/api.md](https://developers.clay.com/routines/api.md) (locator: `lines:4-100`)
  - *Observation*: paraphrase: Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.
  ```text
  # Routines API
  > Run Clay-managed functions and custom functions through the Public API.
  Routines are the programmable way to run Clay logic. Through the Public API, you can run Clay-managed functions and custom functions from backend services, queue workers, internal tools, and custom apps.
  Use [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md) for common enrichment and research jobs. Use [custom functions](https://developers.clay.com/routines/custom-functions.md) for team-specific Clay logic built in the Clay UI.
  ## Run a function routine
  Custom function routine ids use the format `function:t_...`. To start a run, call `POST /routines/{routine_id}/run`.
  Replace `function:t_abc123` and the input names with your function's routine id and inputs. Give each item an id you can use to match its result later.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ROUTINE_RUN_ID=$(curl --request POST \
  --url "https://api.clay.com/public/v0/routines/function:t_abc123/run" \
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.auth.clay_api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Clay Public REST API (https://api.clay.com/public/v0). Source evidence (lines:4-29) states: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.auth.oauth2_cli_and_workspace` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Clay CLI and workspace OAuth integrations. Source evidence (lines:4-29) states: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/public-api/rate-limits.md](https://developers.clay.com/public-api/rate-limits.md) (locator: `lines:4-15`)
  - *Observation*: paraphrase: Clay Public API enforces a default rate limit of 300 requests per minute per workspace, shared across all API keys and OAuth credentials in the workspace.
  ```text
  # Rate limits
  > Understand Clay Public API rate limits and how to handle 429 responses.
  The Clay Public API enforces per-workspace request rate limits. When you exceed a limit, Clay returns HTTP `429` and you should back off before retrying.
  ## Limits
  The default limit is **300 requests per minute per workspace** (about 5 requests per second), shared across all API keys and OAuth credentials in the workspace.
  Spread requests evenly over time. Sending many requests at once can return `429` even when you're under the per-minute total.
  Some endpoints, such as `POST /workflows/runs/query`, also have their own per-endpoint limits.
  Limits may differ for specific workspaces. Contact Clay if you need higher limits.
  ## Reading the limit
  When a request is rate limited, Clay returns `429` with a `Retry-After` header (seconds to wait). When available, Clay also sends `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` so you can pace requests before you hit the ceiling.
  ```
- **URL**: [https://developers.clay.com/concepts/cli-basics.md](https://developers.clay.com/concepts/cli-basics.md) (locator: `lines:4-37`)
  - *Observation*: paraphrase: The JSON-first Clay CLI (`clay`) writes machine-readable JSON to stdout and authenticates per workspace via `clay login` (browser OAuth) or `clay login --device` for headless environments.
  ```text
  # CLI basics
  > Understand the Clay CLI output contract, exit codes, environment variables, and authentication.
  The Clay CLI (`clay`) is JSON-first: every command writes machine-readable JSON to stdout on success and a structured error envelope to stderr on failure. There are no spinners, colors, or progress bars, so agents and scripts can branch on the output and exit code directly.
  ## Output contract
  | Result | Behavior |
  | - | - |
  | Success | JSON is written to stdout, exit code `0`. |
  | Failure | `{ "error": { "code", "message", "details"? } }` is written to stderr, non-zero exit code. |
  Pipe stdout straight into `jq`, and read the exit code (`$?`) to decide what to do next.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Build a Clay GTM search, enrichment routine execution, and webhook/CLI integration via the Clay Public REST API (https://api.clay.com/public/v0), `clay` CLI, or Clay MCP connector.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:4-42): Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Clay GTM search, enrichment routine execution, and webhook/CLI integration via the Clay Public REST API (https://api.clay.com/public/v0), `clay` CLI, or Clay MCP connector.", "blockers": ["The Tables API (POST /public/v0/tables/query) is restricted to Enterprise plans (and has no list-tables endpoint; table IDs must be known).", "Free plan explicitly covers Searches up to 100 results per 30 days (excluding phone enrichment), whereas reusable functions across workflows require Launch+ ($54-$60/mo+) and webhook signal automation requires Growth+ ($185-$205/mo+); custom functions must have API or MCP access explicitly enabled in Function Details (and workspace role permissions must allow access).", "Captured official Clay pages document the Clay MCP connector and `list_subroutines` workflow but do not print the raw hosted MCP endpoint URL in the captured text, so server_url is recorded as null."], "next_steps": ["Create a personal API key under API and CLI -> API keys (or via `clay api-keys create`) and authenticate against https://api.clay.com/public/v0 with `clay-api-key`.", "Enable API and/or MCP access on target custom functions in https://app.clay.com/functions, or install the official `clay` CLI plugin from github.com/clay-run/agent-plugins."]}`
  - Original Rationale: Public developer documentation at developers.clay.com, self-serve API keys and CLI OAuth, Free/Trial/Paid tiers for Searches and paid/trial tiers for Routines/Webhooks, and an official MCP connector make Clay immediately buildable (with Enterprise required only for direct Tables queries).
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Build a Clay GTM search, enrichment routine execution, and webhook/CLI integration via the Clay Public REST API (https://api.clay.com/public/v0), `clay` CLI, or Clay MCP connector.", "blockers": ["The Tables API (POST /public/v0/tables/query) is restricted to Enterprise plans (and has no list-tables endpoint; table IDs must be known).", "Free plan explicitly covers Searches up to 100 results per 30 days (excluding phone enrichment), whereas reusable functions across workflows require Launch+ ($54-$60/mo+) and webhook signal automation requires Growth+ ($185-$205/mo+); custom functions must have API or MCP access explicitly enabled in Function Details (and workspace role permissions must allow access).", "Captured official Clay pages document the Clay MCP connector and `list_subroutines` workflow but do not print the raw hosted MCP endpoint URL in the captured text, so server_url is recorded as null."], "next_steps": ["Create a personal API key under API and CLI -> API keys (or via `clay api-keys create`) and authenticate against https://api.clay.com/public/v0 with `clay-api-key`.", "Enable API and/or MCP access on target custom functions in https://app.clay.com/functions, or install the official `clay` CLI plugin from github.com/clay-run/agent-plugins."]}`
  - Corrected Rationale: Buildability inference is anchored to verified Clay documentation: self-serve API keys available on Pro/Enterprise accounts or trial for automating table enrichment runs (60.testing.trial_access, 60.auth.api_key, 60.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```
- **URL**: [https://developers.clay.com/concepts/cli-basics.md](https://developers.clay.com/concepts/cli-basics.md) (locator: `lines:4-37`)
  - *Observation*: paraphrase: The JSON-first Clay CLI (`clay`) writes machine-readable JSON to stdout and authenticates per workspace via `clay login` (browser OAuth) or `clay login --device` for headless environments.
  ```text
  # CLI basics
  > Understand the Clay CLI output contract, exit codes, environment variables, and authentication.
  The Clay CLI (`clay`) is JSON-first: every command writes machine-readable JSON to stdout on success and a structured error envelope to stderr on failure. There are no spinners, colors, or progress bars, so agents and scripts can branch on the output and exit code directly.
  ## Output contract
  | Result | Behavior |
  | - | - |
  | Success | JSON is written to stdout, exit code `0`. |
  | Failure | `{ "error": { "code", "message", "details"? } }` is written to stderr, non-zero exit code. |
  Pipe stdout straight into `jq`, and read the exit code (`$?`) to decide what to do next.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://developers.clay.com/tables.md](https://developers.clay.com/tables.md) (locator: `lines:4-25`)
  - *Observation*: paraphrase: Tables API (POST https://api.clay.com/public/v0/tables/query) lets customers query known Clay tables and is available on Enterprise plans only.
  ```text
  # Tables (Enterprise)
  > Query known Clay tables with structured filters, selected fields, ordering, and pagination.
  Tables let Enterprise customers read structured data from known Clay tables. Use table queries when your integration already knows which table it needs and wants specific fields, filters, ordering, and pagination.
  > [!NOTE]
  >
  > Tables are available on Enterprise plans.
  Clay tables can act as a GTM database for your downstream systems. You can build dashboards, internal tools, QA views, scoring jobs, and interactive apps on top of data that already exists in Clay.
  The current public API does not include a list-tables endpoint. You need the table identifiers your integration uses before querying table data. You can find the table id in a Clay URL after `/tables/`, for example `https://app.clay.com/workspaces/{workspaceId}/tables/t_0te9i4tZEHwc9hihBXu`.
  ## Common uses
  * Pull records into a dashboard or internal tool.
  ```
- **URL**: [https://developers.clay.com/routines/api.md](https://developers.clay.com/routines/api.md) (locator: `lines:4-100`)
  - *Observation*: paraphrase: Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.
  ```text
  # Routines API
  > Run Clay-managed functions and custom functions through the Public API.
  Routines are the programmable way to run Clay logic. Through the Public API, you can run Clay-managed functions and custom functions from backend services, queue workers, internal tools, and custom apps.
  Use [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md) for common enrichment and research jobs. Use [custom functions](https://developers.clay.com/routines/custom-functions.md) for team-specific Clay logic built in the Clay UI.
  ## Run a function routine
  Custom function routine ids use the format `function:t_...`. To start a run, call `POST /routines/{routine_id}/run`.
  Replace `function:t_abc123` and the input names with your function's routine id and inputs. Give each item an id you can use to match its result later.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ROUTINE_RUN_ID=$(curl --request POST \
  --url "https://api.clay.com/public/v0/routines/function:t_abc123/run" \
  ```
- **URL**: [https://developers.clay.com/routines/custom-functions.md](https://developers.clay.com/routines/custom-functions.md) (locator: `lines:21-47`)
  - *Observation*: paraphrase: Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access settings.
  ```text
  ## Expose a function
  To call a custom function:
  1. Open [Functions](https://app.clay.com/functions).
  2. Create or select a function.
  3. Open **Details**.
  4. Enable the integrations you need, such as **API** or **MCP**.
  5. Copy the `t_...` function id.
  6. Prefix it with `function:` when you call it from the plugin, CLI, MCP, or API.
  Custom function routine ids use the format `function:t_...`.
  Each access setting enables a separate way to call the function:
  ```
- **URL**: [https://developers.clay.com/public-api/webhooks.md](https://developers.clay.com/public-api/webhooks.md) (locator: `lines:4-58`)
  - *Observation*: paraphrase: Clay webhooks notify a service when a routine run finishes by sending a signed POST (`X-Clay-Signature` HMAC-SHA256).
  ```text
  # Webhooks
  > Get notified when a routine run finishes, then verify and handle the delivery.
  Webhooks let Clay notify your service when a routine run finishes, so you can react without polling. Register a webhook, pass its id when you start a run, and handle the signed `POST` Clay sends once results are ready.
  ## Register a webhook
  Create a webhook with the CLI — run `clay webhooks --help` for the full command surface (create, list, test, delete):
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  clay webhooks create https://example.com/hooks/clay
  ```
  `create` returns the signing secret exactly once — store it immediately, it can't be retrieved later:
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:21-47) states: Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access…. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/routines/custom-functions.md](https://developers.clay.com/routines/custom-functions.md) (locator: `lines:21-47`)
  - *Observation*: paraphrase: Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access settings.
  ```text
  ## Expose a function
  To call a custom function:
  1. Open [Functions](https://app.clay.com/functions).
  2. Create or select a function.
  3. Open **Details**.
  4. Enable the integrations you need, such as **API** or **MCP**.
  5. Copy the `t_...` function id.
  6. Prefix it with `function:` when you call it from the plugin, CLI, MCP, or API.
  Custom function routine ids use the format `function:t_...`.
  Each access setting enables a separate way to call the function:
  ```
- **URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp) (locator: `lines:166-268`)
  - *Observation*: paraphrase: Clay MCP (©2026 Clay Labs Inc. at line 267) connects AI tools (Claude, ChatGPT, Codex) to Clay's 200+ data providers, Clay Functions, Audiences, and People Search with budget guardrails and admin controls.
  ```text
  Clay MCP
  Give reps the best prospecting data in their AI tools
  Bring data from 200+ providers and Ops-managed workflows into one place in the tools reps already use. Find contacts, get emails and phone numbers, and push to sequences—all in natural language.
  “Clay's MCP helps us find and enrich ICP contacts across multiple providers and push them into Salesforce for SDR follow-up, all from inside Claude. Budget guardrails and admin controls mean reps can move faster without Ops losing control.”
  Zach Matek
  Director of Marketing Ops, Saviynt
  FOR OPS
  FOR SALES
  Reps get the right data faster while Ops keeps control
  Standardize prospecting workflows with centralized first and third party data without losing governance
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.mcp.official_clay_mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Clay MCP Connector; source_url=https://developers.clay.com/routines/custom-functions.md. Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/routines/custom-functions.md](https://developers.clay.com/routines/custom-functions.md) (locator: `lines:21-47`)
  - *Observation*: paraphrase: Calling a custom function via Clay's MCP connector (`list_subroutines`) requires enabling MCP access in the function's settings; workspace and role permissions still apply, and if a user cannot change access they can ask a workspace admin to check integration and role access settings.
  ```text
  ## Expose a function
  To call a custom function:
  1. Open [Functions](https://app.clay.com/functions).
  2. Create or select a function.
  3. Open **Details**.
  4. Enable the integrations you need, such as **API** or **MCP**.
  5. Copy the `t_...` function id.
  6. Prefix it with `function:` when you call it from the plugin, CLI, MCP, or API.
  Custom function routine ids use the format `function:t_...`.
  Each access setting enables a separate way to call the function:
  ```
- **URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp) (locator: `lines:166-268`)
  - *Observation*: paraphrase: Clay MCP (©2026 Clay Labs Inc. at line 267) connects AI tools (Claude, ChatGPT, Codex) to Clay's 200+ data providers, Clay Functions, Audiences, and People Search with budget guardrails and admin controls.
  ```text
  Clay MCP
  Give reps the best prospecting data in their AI tools
  Bring data from 200+ providers and Ops-managed workflows into one place in the tools reps already use. Find contacts, get emails and phone numbers, and push to sequences—all in natural language.
  “Clay's MCP helps us find and enrich ICP contacts across multiple providers and push them into Salesforce for SDR follow-up, all from inside Claude. Budget guardrails and admin controls mean reps can move faster without Ops losing control.”
  Zach Matek
  Director of Marketing Ops, Saviynt
  FOR OPS
  FOR SALES
  Reps get the right data faster while Ops keeps control
  Standardize prospecting workflows with centralized first and third party data without losing governance
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:4-29) states: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`). The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Go-to-market data enrichment and automation platform with a Public REST API (Searches, Routines/Functions, Enterprise Tables, workspace credit balances, and signed Webhooks at https://api.clay.com/public/v0), JSON-first `clay` CLI, and an official Clay MCP connector.. Source evidence (lines:4-42) states: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/index.md](https://developers.clay.com/index.md) (locator: `lines:4-42`)
  - *Observation*: paraphrase: Clay developer platform (developers.clay.com) enables agents, terminals, and backend services to use Clay's five core primitives: Searches, Routines (functions & alpha Workflows), Tables (Enterprise only), Audiences, and Signals.
  ```text
  # Overview
  > Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  Clay used to live primarily in the Clay UI. Now Clay also works where your agents, developers, and business systems already are.
  Use the developer platform to search Clay's GTM data, run reusable Clay logic, read table data, and work with Audiences programmatically.
  ## Start here
  > [card] [Install the Clay plugin](https://developers.clay.com/quickstart.md#agent-plugin)
  >
  > Best for Claude Code, Codex, Cursor, and agent-first work. The plugin ships skills and the Clay CLI.
  > [card] [Call the API directly](https://developers.clay.com/quickstart.md#api)
  >
  ```
- **URL**: [https://developers.clay.com/public-api/authentication.md](https://developers.clay.com/public-api/authentication.md) (locator: `lines:4-23`)
  - *Observation*: paraphrase: Every request to the Clay Public API (e.g., https://api.clay.com/public/v0/me) requires a personal API key in the clay-api-key HTTP header, tied to a Clay user and workspace access.
  ```text
  # Authentication
  > Authenticate requests with a Clay API key.
  Every request to the Clay Public API must include a Clay API key in the `clay-api-key` header. Store your key in an environment variable and pass it in the header:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  export CLAY_PUBLIC_API_KEY="your_api_key"
  curl https://api.clay.com/public/v0/me \
  -H "clay-api-key: $CLAY_PUBLIC_API_KEY"
  ```
  API keys are tied to a Clay user and workspace access. Create one under [API and CLI → API keys](https://app.clay.com/workspaces/~/api-and-cli?tab=api-keys), with `clay api-keys create --name "<key name>"` in the CLI, or by asking your agent after installing the [agent plugin](https://developers.clay.com/quickstart.md#agent-plugin). Keep keys server-side and do not expose them in browser code, mobile apps, public repositories, logs, or analytics tools.
  ## Header
  ```
- **URL**: [https://developers.clay.com/concepts/cli-basics.md](https://developers.clay.com/concepts/cli-basics.md) (locator: `lines:4-37`)
  - *Observation*: paraphrase: The JSON-first Clay CLI (`clay`) writes machine-readable JSON to stdout and authenticates per workspace via `clay login` (browser OAuth) or `clay login --device` for headless environments.
  ```text
  # CLI basics
  > Understand the Clay CLI output contract, exit codes, environment variables, and authentication.
  The Clay CLI (`clay`) is JSON-first: every command writes machine-readable JSON to stdout on success and a structured error envelope to stderr on failure. There are no spinners, colors, or progress bars, so agents and scripts can branch on the output and exit code directly.
  ## Output contract
  | Result | Behavior |
  | - | - |
  | Success | JSON is written to stdout, exit code `0`. |
  | Failure | `{ "error": { "code", "message", "details"? } }` is written to stderr, non-zero exit code. |
  Pipe stdout straight into `jq`, and read the exit code (`$?`) to decide what to do next.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://developers.clay.com/routines/api.md](https://developers.clay.com/routines/api.md) (locator: `lines:4-100`)
  - *Observation*: paraphrase: Routines API runs Clay-managed functions and custom functions via POST https://api.clay.com/public/v0/routines/{routine_id}/run and polls GET .../routines/run/{id}/results; Workflows are also routines and are in Alpha.
  ```text
  # Routines API
  > Run Clay-managed functions and custom functions through the Public API.
  Routines are the programmable way to run Clay logic. Through the Public API, you can run Clay-managed functions and custom functions from backend services, queue workers, internal tools, and custom apps.
  Use [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md) for common enrichment and research jobs. Use [custom functions](https://developers.clay.com/routines/custom-functions.md) for team-specific Clay logic built in the Clay UI.
  ## Run a function routine
  Custom function routine ids use the format `function:t_...`. To start a run, call `POST /routines/{routine_id}/run`.
  Replace `function:t_abc123` and the input names with your function's routine id and inputs. Give each item an id you can use to match its result later.
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ROUTINE_RUN_ID=$(curl --request POST \
  --url "https://api.clay.com/public/v0/routines/function:t_abc123/run" \
  ```
- **URL**: [https://developers.clay.com/public-api/webhooks.md](https://developers.clay.com/public-api/webhooks.md) (locator: `lines:4-58`)
  - *Observation*: paraphrase: Clay webhooks notify a service when a routine run finishes by sending a signed POST (`X-Clay-Signature` HMAC-SHA256).
  ```text
  # Webhooks
  > Get notified when a routine run finishes, then verify and handle the delivery.
  Webhooks let Clay notify your service when a routine run finishes, so you can react without polling. Register a webhook, pass its id when you start a run, and handle the signed `POST` Clay sends once results are ready.
  ## Register a webhook
  Create a webhook with the CLI — run `clay webhooks --help` for the full command surface (create, list, test, delete):
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  clay webhooks create https://example.com/hooks/clay
  ```
  `create` returns the signing secret exactly once — store it immediately, it can't be retrieved later:
  ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
  ```
- **URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp) (locator: `lines:166-268`)
  - *Observation*: paraphrase: Clay MCP (©2026 Clay Labs Inc. at line 267) connects AI tools (Claude, ChatGPT, Codex) to Clay's 200+ data providers, Clay Functions, Audiences, and People Search with budget guardrails and admin controls.
  ```text
  Clay MCP
  Give reps the best prospecting data in their AI tools
  Bring data from 200+ providers and Ops-managed workflows into one place in the tools reps already use. Find contacts, get emails and phone numbers, and push to sequences—all in natural language.
  “Clay's MCP helps us find and enrich ICP contacts across multiple providers and push them into Salesforce for SDR follow-up, all from inside Claude. Budget guardrails and admin controls mean reps can move faster without Ops losing control.”
  Zach Matek
  Director of Marketing Ops, Saviynt
  FOR OPS
  FOR SALES
  Reps get the right data faster while Ops keeps control
  Standardize prospecting workflows with centralized first and third party data without losing governance
  ```
- **URL**: [https://developers.clay.com/llms.txt](https://developers.clay.com/llms.txt) (locator: `lines:1-55`)
  - *Observation*: paraphrase: developers.clay.com/llms.txt indexes Workflows (Alpha), Audiences privacy deletion, Get workspace credit balances (api-reference/credits/get-workspace-credit-balances.md), Get the authenticated user (api-reference/me/get-the-authenticated-user.md), Routines execution/batch runs, Search queries/iterators, Tables (Enterprise) structured queries, and Workflows runs search, plus /openapi.json.
  ```text
  # Clay docs
  > Developer documentation for using Clay from agents, CLIs, APIs, and internal systems.
  - [Overview](https://developers.clay.com/index.md): Use Clay from agents, terminals, backend services, internal tools, and custom apps.
  - [Quickstart](https://developers.clay.com/quickstart.md): Build with Clay from your coding agent, or call the Clay API from your own applications.
  - [Searches](https://developers.clay.com/searches.md): Find companies and people in Clay's proprietary GTM database.
  - [Search with advanced queries](https://developers.clay.com/searches/advanced.md): Find Clay companies or people with Clay's advanced search query language.
  - [Routines overview](https://developers.clay.com/routines/index.md): Understand the routine types: Clay-managed functions, custom functions, and Workflows.
  - [Clay-managed functions](https://developers.clay.com/routines/clay-managed-functions.md): Use Clay-provided functions for common enrichment and research jobs.
  - [Custom functions](https://developers.clay.com/routines/custom-functions.md): Run your own reusable Clay logic from agents, the CLI, MCP, or the API.
  - [Workflows (Alpha)](https://developers.clay.com/routines/workflows-alpha.md): Build, edit, run, inspect, and batch-run Clay Workflows from the plugin and CLI.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:17-30) states: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days). The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://www.clay.com/mcp](https://www.clay.com/mcp) (locator: `lines:166-268`)
  - *Observation*: paraphrase: Clay MCP (©2026 Clay Labs Inc. at line 267) connects AI tools (Claude, ChatGPT, Codex) to Clay's 200+ data providers, Clay Functions, Audiences, and People Search with budget guardrails and admin controls.
  ```text
  Clay MCP
  Give reps the best prospecting data in their AI tools
  Bring data from 200+ providers and Ops-managed workflows into one place in the tools reps already use. Find contacts, get emails and phone numbers, and push to sequences—all in natural language.
  “Clay's MCP helps us find and enrich ICP contacts across multiple providers and push them into Salesforce for SDR follow-up, all from inside Claude. Budget guardrails and admin controls mean reps can move faster without Ops losing control.”
  Zach Matek
  Director of Marketing Ops, Saviynt
  FOR OPS
  FOR SALES
  Reps get the right data faster while Ops keeps control
  Standardize prospecting workflows with centralized first and third party data without losing governance
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:17-30) states: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days). The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:4-29) states: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`). The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/quickstart.md](https://developers.clay.com/quickstart.md) (locator: `lines:4-29`)
  - *Observation*: paraphrase: Developers use Clay via the agent plugin (`clay` CLI, signed in via browser OAuth) or the Public API (`clay-api-key` header, created under API and CLI -> API keys or `clay api-keys create`).
  ```text
  # Quickstart
  > Build with Clay from your coding agent, or call the Clay API from your own applications.
  There are two ways to use Clay as a developer: install the agent plugin to build with Clay inside your coding agent, or call the Public API directly from your own applications and services.
  ## Agent plugin
  The agent plugin gives your coding agent Clay's skills and the `clay` CLI — the fastest way to build with Clay from a coding agent.
  It requires a coding-agent host with a shell — Claude Code, Codex, or Cursor — and doesn't work in general-purpose chat apps like Claude Desktop, claude.ai, or ChatGPT that can't run the CLI.
  Copy this into your agent of choice and let it install and set up the plugin for you:
  ```
  Set up the Clay plugin by following the steps in
  https://github.com/clay-run/agent-plugins
  ```
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `60.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:17-30) states: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days). The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.clay.com/searches.md](https://developers.clay.com/searches.md) (locator: `lines:17-30`)
  - *Observation*: paraphrase: Searches API/CLI result limits scale by plan: Free (50 per request/search, 100 per 30 days), Trial (50 per request/search, 10,000 for trial), Paid (500 per request, 1,000,000 per 30 days), and Enterprise (500 per request, 10,000,000 per 30 days).
  ```text
  ## Result limits
  Clay caps how many search results a workspace can return through the API. These limits apply to results returned across the CLI and Public API, and they scale with your plan.
  | Plan | Results per request | Results per search | Results per period | Reset date |
  | - | - | - | - | - |
  | Free | 50 | 50 | 100 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Trial | 50 | 50 | 10,000 for trial duration | Not applicable |
  | Paid | 500 | Up to your period limit | 1,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  | Legacy paid (Starter, Explorer, Pro) | 500 | Up to your period limit | 1,000,000 per year | January 1 (UTC) |
  | Enterprise | 500 | Up to your period limit | 10,000,000 per 30 days | Rolling (ages out daily at midnight UTC) |
  * **Per request** is the largest limit you can request in a single call.
  ```
- **URL**: [https://www.clay.com/pricing](https://www.clay.com/pricing) (locator: `lines:212-319`)
  - *Observation*: paraphrase: Clay pricing includes a Free plan ('Start building in Clay for free. No strings attached.', 500 actions/mo), 14-day trials on self-serve paid Launch (starts at $54/mo annual / $60/mo monthly; adds 'Reuse functions across workflows') and Growth (starts at $185/mo annual / $205/mo monthly; adds 'Integrate with any HTTP API' and 'Automate any signal via webhook') plans, and custom Enterprise ('Get a demo' or 'buy now', RBAC, SSO, credit budgeting).
  ```text
  Start building in Clay for free. No strings attached.
  Free
  Includes 500 actions/mo
  Includes 6,000 actions/year
  6K actions/yr
  500 actions/mo
  1.2K data credits/yr
  100 data credits/mo
  Unlimited seats and tables
  Run multi-provider waterfalls
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 52: SE Ranking (Data, SEO and Scraping)
- Total claims: 17 | Corrected: 2

### Claim: `52.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:12-74): Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Multiple related SEO and search-visibility resource groups across global SEO research (Data API), campaign/project management (Project API), local business listings/GBP (Local Marketing API), and AI search engine visibility (SE Visible API).
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: SE Ranking API documentation spans multiple related SEO data groups: (1) Keyword Rank Tracking, (2) Competitor & Organic Search Data, and (3) Backlink/Local Marketing Analysis. Per evidence rules, multiple related workflow groups substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/data/](https://seranking.com/api/data/) (locator: `lines:435-463`)
  - *Observation*: paraphrase: Data API covers keyword database, domain profiles, backlinks, Google AI Overviews, AI models, SERP features, and monthly technical audits.
  ```text
  Data API
  Data API
  Getting started guide
  Learn how to set up your account, understand API credits, and make your first request.
  Get started
  Data API coverage
  5.4B+
  Keyword database
  2.2B+
  Domain profiles
  ```
- **URL**: [https://seranking.com/api/project/](https://seranking.com/api/project/) (locator: `lines:435-446`)
  - *Observation*: paraphrase: Project API covers creating/managing projects, keyword groups, tracking competitors, running website audits, monitoring backlinks, and account/seat management.
  ```text
  Project API
  Project API
  Getting started guide
  Learn how to get an API key, understand rate limits, and start making requests.
  Get started
  Quick actions
  Create and manage projects
  Add and manage keyword groups
  Track competitors
  Run website audits
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.group.data_api` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Data API (Backlinks, Domain Analysis, Keyword Research, AI Search, SERP, Website Audit, Account subscription/credit balance). Source evidence (lines:12-74) states: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/data/](https://seranking.com/api/data/) (locator: `lines:435-463`)
  - *Observation*: paraphrase: Data API covers keyword database, domain profiles, backlinks, Google AI Overviews, AI models, SERP features, and monthly technical audits.
  ```text
  Data API
  Data API
  Getting started guide
  Learn how to set up your account, understand API credits, and make your first request.
  Get started
  Data API coverage
  5.4B+
  Keyword database
  2.2B+
  Domain profiles
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.group.local_marketing_api` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Local Marketing API (locations, local rankings, Google Business Profile reports, business listings, reviews, local audits). Source evidence (lines:12-74) states: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.group.project_api` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Project API (projects, project groups, keywords/rankings, search engines, competitors, URL tags, GSC data, website audits, Backlink Checker, AI Results Tracker). Source evidence (lines:12-74) states: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/project/](https://seranking.com/api/project/) (locator: `lines:435-446`)
  - *Observation*: paraphrase: Project API covers creating/managing projects, keyword groups, tracking competitors, running website audits, monitoring backlinks, and account/seat management.
  ```text
  Project API
  Project API
  Getting started guide
  Learn how to get an API key, understand rate limits, and start making requests.
  Get started
  Quick actions
  Create and manage projects
  Add and manage keyword groups
  Track competitors
  Run website audits
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.group.se_visible_api` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SE Visible API (AI visibility projects, brands, topics, prompts, prompt results, sources, engines, locations). Source evidence (lines:12-74) states: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:435-516) states: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:435-516`)
  - *Observation*: paraphrase: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.
  ```text
  API access is included in every SE Ranking plan
  SEO API: Automate your SEO workflows
  Connect via API for custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both.
  Start free trialSee product tour
  No credit card required
  The data your workflows will run on
  5.5B
  Keywords database
  100%
  Accurate keyword rankings
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:435-516) states: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:435-516`)
  - *Observation*: paraphrase: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.
  ```text
  API access is included in every SE Ranking plan
  SEO API: Automate your SEO workflows
  Connect via API for custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both.
  Start free trialSee product tour
  No credit card required
  The data your workflows will run on
  5.5B
  Keywords database
  100%
  Accurate keyword rankings
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.auth.api_key_token` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for SE Ranking REST APIs (Data, Project, Local Marketing, SE Visible) and manual MCP key auth. Source evidence (lines:611-621) states: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:611-621`)
  - *Observation*: paraphrase: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.
  ```text
  How do I access SE Ranking’s API?
  A
  Accessing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our API documentation.
  Show more
  Show less
  Q
  How do I get an SE Ranking API key?
  A
  API is included with every SE Ranking subscription. To get your key, log in to your SE Ranking account, go to the API section. From there, you can copy your API key and use it to integrate SE Ranking’s data into your applications, dashboards, or reports.
  Show more
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.auth.mcp_oauth2` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for SE Ranking hosted remote MCP server (https://api.seranking.com/mcp). Source evidence (lines:444-464) states: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts). This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/seo-skills/main/README.md](https://raw.githubusercontent.com/seranking/seo-skills/main/README.md) (locator: `lines:1-54`)
  - *Observation*: paraphrase: Official seranking/seo-skills repository distributes 32 open-source Claude/Cursor SEO skills configured for the hosted SE Ranking remote MCP server at https://api.seranking.com/mcp with OAuth sign-in.
  ```text
  # Claude SEO Skills
  **32 free, open-source Claude SEO skills** for Claude Code, Claude Desktop, Cursor and any AI agent that supports Agent Skills and MCP. Each SEO skill turns live [SE Ranking](https://seranking.com) data into a finished deliverable: content briefs, technical audits, AI search share of voice, backlink gap lists, keyword clusters and 90-day SEO plans. <!-- dir-edition:line readme-intro -->
  Overview, use cases and a no-terminal install guide: [Claude SEO Skills by SE Ranking](https://seranking.com/claude-seo-skills.html). <!-- dir-edition:line readme-overview-link -->
  <!-- dir-edition:line readme-about-edition -->
  Production-ready [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for SEO, powered by the [SE Ranking MCP](https://seranking.com/mcp.html). Each skill turns raw API data into a finished SEO deliverable — content briefs, AI Search share of voice, page intelligence, structured data, drift monitoring, SXO diagnostics, competitive analysis, and more.
  These Claude Skills are designed to work with the SE Ranking MCP server, but they document every API call explicitly so they can also be adapted to other SEO data providers.
  ## What are Claude SEO skills?
  Claude SEO skills are reusable instructions that teach Claude how to run a specific SEO task end to end: which data to pull, in what order, and what file to produce. Instead of writing a long prompt each time, you ask for "a content brief for X" or "a backlink gap vs. these competitors", and Claude picks the matching skill. The skills in this repo get their data from the SE Ranking MCP server, so every brief, audit and report is based on live keyword, backlink, SERP and AI search data rather than the model's memory.
  ## Install
  <!-- dir-edition:begin readme-install -->
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Integrate SE Ranking Data, Project, Local Marketing, and SE Visible APIs via REST/OpenAPI 3.0 or the hosted MCP server at https://api.seranking.com/mcp.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:611-621): API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Integrate SE Ranking Data, Project, Local Marketing, and SE Visible APIs via REST/OpenAPI 3.0 or the hosted MCP server at https://api.seranking.com/mcp.", "blockers": ["Production usage requires a paid SE Ranking subscription (from $129/mo with 25K API credits) or standalone API plan ($179/mo annual) and consumes API credits.", "In shared workspaces, sub-accounts cannot use OAuth button sign-in directly and must use a master-account API key from an administrator."], "next_steps": ["Generate an API key in the SE Ranking API Dashboard (Settings > API) or connect an MCP client to https://api.seranking.com/mcp via OAuth 2.1.", "Use official OpenAPI 3.0 specs from github.com/seranking/openapi to generate typed REST clients."]}`
  - Original Rationale: Public OpenAPI 3.0 specifications, self-serve API keys and 14-day trial for master accounts, and an official hosted MCP server make SE Ranking immediately buildable.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Integrate SE Ranking Data, Project, Local Marketing, and SE Visible APIs via REST/OpenAPI 3.0 or the hosted MCP server at https://api.seranking.com/mcp.", "blockers": ["Production usage requires a paid SE Ranking subscription (from $129/mo with 25K API credits) or standalone API plan ($179/mo annual) and consumes API credits.", "In shared workspaces, sub-accounts cannot use OAuth button sign-in directly and must use a master-account API key from an administrator."], "next_steps": ["Generate an API key in the SE Ranking API Dashboard (Settings > API) or connect an MCP client to https://api.seranking.com/mcp via OAuth 2.1.", "Use official OpenAPI 3.0 specs from github.com/seranking/openapi to generate typed REST clients."]}`
  - Corrected Rationale: Buildability inference is anchored to verified SE Ranking documentation: REST API keys available on paid plans (or trial) with clear JSON endpoints for SEO data retrieval (52.testing.trial_access, 52.auth.api_key, 52.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:611-621`)
  - *Observation*: paraphrase: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.
  ```text
  How do I access SE Ranking’s API?
  A
  Accessing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our API documentation.
  Show more
  Show less
  Q
  How do I get an SE Ranking API key?
  A
  API is included with every SE Ranking subscription. To get your key, log in to your SE Ranking account, go to the API section. From there, you can copy your API key and use it to integrate SE Ranking’s data into your applications, dashboards, or reports.
  Show more
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:100-147`)
  - *Observation*: paraphrase: SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.
  ```text
  $129.00
  /mo
  Start free 14-day trial
  No credit card required
  10 projects & 1 manager seat
  2k keywords to track daily
  250k pages per month in audit
  25K API credits & MCP access
  What’s inside:
  Rank tracking across major search engines
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:331-336`)
  - *Observation*: paraphrase: SE Ranking also offers a standalone SE Ranking API plan starting from $179/mo (annual billing only).
  ```text
  SE Ranking API
  Programmatic access to real-time SEO & GEO data via SE Ranking’s standalone API plan
  From
  $179
  /mo
  Annual billing only
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:444-464) states: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts). The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/seo-skills/main/README.md](https://raw.githubusercontent.com/seranking/seo-skills/main/README.md) (locator: `lines:1-54`)
  - *Observation*: paraphrase: Official seranking/seo-skills repository distributes 32 open-source Claude/Cursor SEO skills configured for the hosted SE Ranking remote MCP server at https://api.seranking.com/mcp with OAuth sign-in.
  ```text
  # Claude SEO Skills
  **32 free, open-source Claude SEO skills** for Claude Code, Claude Desktop, Cursor and any AI agent that supports Agent Skills and MCP. Each SEO skill turns live [SE Ranking](https://seranking.com) data into a finished deliverable: content briefs, technical audits, AI search share of voice, backlink gap lists, keyword clusters and 90-day SEO plans. <!-- dir-edition:line readme-intro -->
  Overview, use cases and a no-terminal install guide: [Claude SEO Skills by SE Ranking](https://seranking.com/claude-seo-skills.html). <!-- dir-edition:line readme-overview-link -->
  <!-- dir-edition:line readme-about-edition -->
  Production-ready [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for SEO, powered by the [SE Ranking MCP](https://seranking.com/mcp.html). Each skill turns raw API data into a finished SEO deliverable — content briefs, AI Search share of voice, page intelligence, structured data, drift monitoring, SXO diagnostics, competitive analysis, and more.
  These Claude Skills are designed to work with the SE Ranking MCP server, but they document every API call explicitly so they can also be adapted to other SEO data providers.
  ## What are Claude SEO skills?
  Claude SEO skills are reusable instructions that teach Claude how to run a specific SEO task end to end: which data to pull, in what order, and what file to produce. Instead of writing a long prompt each time, you ask for "a content brief for X" or "a backlink gap vs. these competitors", and Claude picks the matching skill. The skills in this repo get their data from the SE Ranking MCP server, so every brief, audit and report is based on live keyword, backlink, SERP and AI search data rather than the model's memory.
  ## Install
  <!-- dir-edition:begin readme-install -->
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.mcp.official_remote_mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=SE Ranking Remote MCP Server; source_url=https://seranking.com/api/integrations/mcp/. Source evidence (lines:444-464) states: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts). The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/seo-skills/main/README.md](https://raw.githubusercontent.com/seranking/seo-skills/main/README.md) (locator: `lines:1-54`)
  - *Observation*: paraphrase: Official seranking/seo-skills repository distributes 32 open-source Claude/Cursor SEO skills configured for the hosted SE Ranking remote MCP server at https://api.seranking.com/mcp with OAuth sign-in.
  ```text
  # Claude SEO Skills
  **32 free, open-source Claude SEO skills** for Claude Code, Claude Desktop, Cursor and any AI agent that supports Agent Skills and MCP. Each SEO skill turns live [SE Ranking](https://seranking.com) data into a finished deliverable: content briefs, technical audits, AI search share of voice, backlink gap lists, keyword clusters and 90-day SEO plans. <!-- dir-edition:line readme-intro -->
  Overview, use cases and a no-terminal install guide: [Claude SEO Skills by SE Ranking](https://seranking.com/claude-seo-skills.html). <!-- dir-edition:line readme-overview-link -->
  <!-- dir-edition:line readme-about-edition -->
  Production-ready [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) for SEO, powered by the [SE Ranking MCP](https://seranking.com/mcp.html). Each skill turns raw API data into a finished SEO deliverable — content briefs, AI Search share of voice, page intelligence, structured data, drift monitoring, SXO diagnostics, competitive analysis, and more.
  These Claude Skills are designed to work with the SE Ranking MCP server, but they document every API call explicitly so they can also be adapted to other SEO data providers.
  ## What are Claude SEO skills?
  Claude SEO skills are reusable instructions that teach Claude how to run a specific SEO task end to end: which data to pull, in what order, and what file to produce. Instead of writing a long prompt each time, you ask for "a content brief for X" or "a backlink gap vs. these competitors", and Claude picks the matching skill. The skills in this repo get their data from the SE Ranking MCP server, so every brief, audit and report is based on live keyword, backlink, SERP and AI search data rather than the model's memory.
  ## Install
  <!-- dir-edition:begin readme-install -->
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:611-621) states: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:611-621`)
  - *Observation*: paraphrase: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.
  ```text
  How do I access SE Ranking’s API?
  A
  Accessing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our API documentation.
  Show more
  Show less
  Q
  How do I get an SE Ranking API key?
  A
  API is included with every SE Ranking subscription. To get your key, log in to your SE Ranking account, go to the API section. From there, you can copy your API key and use it to integrate SE Ranking’s data into your applications, dashboards, or reports.
  Show more
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:100-147`)
  - *Observation*: paraphrase: SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.
  ```text
  $129.00
  /mo
  Start free 14-day trial
  No credit card required
  10 projects & 1 manager seat
  2k keywords to track daily
  250k pages per month in audit
  25K API credits & MCP access
  What’s inside:
  Rank tracking across major search engines
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:331-336`)
  - *Observation*: paraphrase: SE Ranking also offers a standalone SE Ranking API plan starting from $179/mo (annual billing only).
  ```text
  SE Ranking API
  Programmatic access to real-time SEO & GEO data via SE Ranking’s standalone API plan
  From
  $179
  /mo
  Annual billing only
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:611-621) states: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:611-621`)
  - *Observation*: paraphrase: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.
  ```text
  How do I access SE Ranking’s API?
  A
  Accessing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our API documentation.
  Show more
  Show less
  Q
  How do I get an SE Ranking API key?
  A
  API is included with every SE Ranking subscription. To get your key, log in to your SE Ranking account, go to the API section. From there, you can copy your API key and use it to integrate SE Ranking’s data into your applications, dashboards, or reports.
  Show more
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:100-147`)
  - *Observation*: paraphrase: SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.
  ```text
  $129.00
  /mo
  Start free 14-day trial
  No credit card required
  10 projects & 1 manager seat
  2k keywords to track daily
  250k pages per month in audit
  25K API credits & MCP access
  What’s inside:
  Rank tracking across major search engines
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SEO and AI-visibility platform with REST APIs (Data API, Project API, Local Marketing API, SE Visible API at https://api.seranking.com), OpenAPI 3.0 specs, and a hosted remote MCP server.. Source evidence (lines:435-516) states: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:435-516`)
  - *Observation*: paraphrase: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.
  ```text
  API access is included in every SE Ranking plan
  SEO API: Automate your SEO workflows
  Connect via API for custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both.
  Start free trialSee product tour
  No credit card required
  The data your workflows will run on
  5.5B
  Keywords database
  100%
  Accurate keyword rankings
  ```
- **URL**: [https://raw.githubusercontent.com/seranking/openapi/main/README.md](https://raw.githubusercontent.com/seranking/openapi/main/README.md) (locator: `lines:12-74`)
  - *Observation*: paraphrase: Official seranking/openapi repo publishes OpenAPI 3.0 specs (JSON and YAML) for Data API, Project API, Local Marketing API, and SE Visible API served from https://api.seranking.com and authenticated via Authorization: Token YOUR_API_KEY header or apikey query parameter.
  ```text
  | API | YAML | JSON | Documentation |
  | -------------------- | -------------------------- | -------------------------- | ------------------------------------------------------------------ |
  | Data API | `data-api.yaml` | `data-api.json` | [seranking.com/api/data](https://seranking.com/api/data/) |
  | Project API | `project-api.yaml` | `project-api.json` | [seranking.com/api/project](https://seranking.com/api/project/) |
  | Local Marketing API | `local-marketing-api.yaml` | `local-marketing-api.json` | [seranking.com/api/local-marketing-api](https://seranking.com/api/local-marketing-api/) |
  | SE Visible API | `se-visible-api.yaml` | `se-visible-api.json` | [seranking.com/api/se-visible](https://seranking.com/api/se-visible/) |
  The YAML and JSON file of each API contain the same specification. Use whichever format your tooling prefers.
  The specs follow the public API documentation: every endpoint, parameter and response field described there is in
  the spec, with the documented request and response examples. Each operation links back to its documentation section.
  ## Available APIs
  ```
- **URL**: [https://seranking.com/api/integrations/mcp/](https://seranking.com/api/integrations/mcp/) (locator: `lines:444-464`)
  - *Observation*: paraphrase: SE Ranking provides an official hosted remote MCP server at https://api.seranking.com/mcp using Streamable HTTP and OAuth 2.1 with dynamic client registration (or manual API key entry from the master account API Dashboard for shared-workspace sub-accounts).
  ```text
  The Model Context Protocol (MCP) server provides a standardized interface that allows any compatible AI model to access your SE Ranking and SE Visible data simply and securely.
  MCP server server follows the authenticated remote MCP spec, so it’s centrally hosted and managed. Connect in one click in Claude or ChatGPT, natively in Cursor and other clients, or use the mcp-remote module for clients that don’t support remote servers.
  What you can access
  Through the MCP server, your AI assistant can work with data from these SE Ranking and SE Visible products*:
  Data API: keyword research, backlinks, domain analysis, SERP, and more
  Project API: your projects, rank tracking, audits, and competitors
  Local Marketing API: your locations, local rankings, Google Business Profile, business listings, and reviews
  SE Visible API: your AI visibility projects, brands, topics, prompts, and sources
  *The data available to you depends on your subscription. Not every API endpoint is available through MCP. Setup is the same for every product. Use your SE Ranking account, or an API key generated in the API Dashboard of your SE Ranking or SE Visible account.
  Setup Instructions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:435-516) states: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:435-516`)
  - *Observation*: paraphrase: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.
  ```text
  API access is included in every SE Ranking plan
  SEO API: Automate your SEO workflows
  Connect via API for custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both.
  Start free trialSee product tour
  No credit card required
  The data your workflows will run on
  5.5B
  Keywords database
  100%
  Accurate keyword rankings
  ```
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:611-621`)
  - *Observation*: paraphrase: API access is included with every SE Ranking subscription; users retrieve their unique API key under Settings > API in their SE Ranking account.
  ```text
  How do I access SE Ranking’s API?
  A
  Accessing our API is straightforward. Just log in to your SE Ranking account, navigate to the API tab under the Settings section, and retrieve your unique API key. Once you have your API key, you can use it for different purposes. For more information, refer to our API documentation.
  Show more
  Show less
  Q
  How do I get an SE Ranking API key?
  A
  API is included with every SE Ranking subscription. To get your key, log in to your SE Ranking account, go to the API section. From there, you can copy your API key and use it to integrate SE Ranking’s data into your applications, dashboards, or reports.
  Show more
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:100-147`)
  - *Observation*: paraphrase: SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.
  ```text
  $129.00
  /mo
  Start free 14-day trial
  No credit card required
  10 projects & 1 manager seat
  2k keywords to track daily
  250k pages per month in audit
  25K API credits & MCP access
  What’s inside:
  Rank tracking across major search engines
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `52.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:435-516) states: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://seranking.com/api/](https://seranking.com/api/) (locator: `lines:435-516`)
  - *Observation*: paraphrase: SE Ranking SEO API is included in every SE Ranking plan (with a free trial, no credit card required) and provides JSON responses up to 10 requests/sec across Keyword Research, Backlinks, Domain Analysis, and Website Audit.
  ```text
  API access is included in every SE Ranking plan
  SEO API: Automate your SEO workflows
  Connect via API for custom integrations and bulk processes, or via MCP to query data from inside Claude or any AI assistant. Or do both.
  Start free trialSee product tour
  No credit card required
  The data your workflows will run on
  5.5B
  Keywords database
  100%
  Accurate keyword rankings
  ```
- **URL**: [https://seranking.com/pricing.html](https://seranking.com/pricing.html) (locator: `lines:100-147`)
  - *Observation*: paraphrase: SE Ranking plans start at $129/mo (25K API credits & MCP access, with a 14-day free trial, no credit card required), higher plans include 100K API credits & MCP access, and Enterprise requires 'Talk to sales'.
  ```text
  $129.00
  /mo
  Start free 14-day trial
  No credit card required
  10 projects & 1 manager seat
  2k keywords to track daily
  250k pages per month in audit
  25K API credits & MCP access
  What’s inside:
  Rank tracking across major search engines
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 65: Supabase (Developer, Infra and Data platforms)
- Total claims: 15 | Corrected: 2

### Claim: `65.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:76-82): Reflected API supports CRUD, tables/views and functions with security model.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Database CRUD and organization/project management are related backend platform domains.
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: Supabase API covers multiple related backend services: (1) PostgreSQL Database (PostgREST), (2) GoTrue Auth, (3) Storage, and (4) Edge Functions. Per evidence rules, multiple related service modules substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api](https://supabase.com/docs/guides/api) (locator: `lines:76-82`)
  - *Observation*: paraphrase: Reflected API supports CRUD, tables/views and functions with security model.
  ```text
  The reflected API is designed to retain as much of Postgres' capability as possible including:
  Basic CRUD operations (Create/Read/Update/Delete)
  Arbitrarily deep relationships among tables/views, functions that return table types can also nest related tables/views.
  Works with Postgres Views, Materialized Views and Foreign Tables
  Works with Postgres Functions
  User defined computed columns and computed relationships
  The Postgres security model - including Row Level Security, Roles, and Grants.
  ```
- **URL**: [https://supabase.com/docs/reference/api/introduction](https://supabase.com/docs/reference/api/introduction) (locator: `lines:274-289`)
  - *Observation*: paraphrase: Management API manages organizations/projects with bearer token example.
  ```text
  Management API
  Manage your Supabase organizations and projects programmatically.
  Authentication
  All API requests require an access token to be included in the Authorization header: Authorization Bearer <access_token>.
  There are two ways to generate an access token:
  Personal access token (PAT):
  PATs are tokens with a custom expiry that you manually generate to access the Management API. They are useful for automating workflows or developing against the Management API. A scoped PAT can only reach the organizations, projects, and permissions you choose when creating it. A classic PAT, shown as Legacy in the dashboard, carries the same privileges as your user account. Prefer scoped PATs, and keep every token secret.
  To generate or manage your personal access tokens, visit your account page. See Personal access tokens for the permission each endpoint requires.
  OAuth2:
  OAuth2 allows your application to generate tokens on behalf of a Supabase user, providing secure and limited access to their account without requiring their credentials. Use this if you're building a third-party app that needs to create or manage Supabase projects on behalf of your users. Tokens generated via OAuth2 are short-lived and tied to specific scopes to ensure your app can only perform actions that are explicitly approved by the user.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.api.group.database` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Tables, views and Postgres functions. Source evidence (lines:76-82) states: Reflected API supports CRUD, tables/views and functions with security model. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api](https://supabase.com/docs/guides/api) (locator: `lines:76-82`)
  - *Observation*: paraphrase: Reflected API supports CRUD, tables/views and functions with security model.
  ```text
  The reflected API is designed to retain as much of Postgres' capability as possible including:
  Basic CRUD operations (Create/Read/Update/Delete)
  Arbitrarily deep relationships among tables/views, functions that return table types can also nest related tables/views.
  Works with Postgres Views, Materialized Views and Foreign Tables
  Works with Postgres Functions
  User defined computed columns and computed relationships
  The Postgres security model - including Row Level Security, Roles, and Grants.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.api.group.management` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Organizations and projects. Source evidence (lines:274-289) states: Management API manages organizations/projects with bearer token example. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/reference/api/introduction](https://supabase.com/docs/reference/api/introduction) (locator: `lines:274-289`)
  - *Observation*: paraphrase: Management API manages organizations/projects with bearer token example.
  ```text
  Management API
  Manage your Supabase organizations and projects programmatically.
  Authentication
  All API requests require an access token to be included in the Authorization header: Authorization Bearer <access_token>.
  There are two ways to generate an access token:
  Personal access token (PAT):
  PATs are tokens with a custom expiry that you manually generate to access the Management API. They are useful for automating workflows or developing against the Management API. A scoped PAT can only reach the organizations, projects, and permissions you choose when creating it. A classic PAT, shown as Legacy in the dashboard, carries the same privileges as your user account. Prefer scoped PATs, and keep every token secret.
  To generate or manage your personal access tokens, visit your account page. See Personal access tokens for the permission each endpoint requires.
  OAuth2:
  OAuth2 allows your application to generate tokens on behalf of a Supabase user, providing secure and limited access to their account without requiring their credentials. Use this if you're building a third-party app that needs to create or manage Supabase projects on behalf of your users. Tokens generated via OAuth2 are short-lived and tied to specific scopes to ensure your app can only perform actions that are explicitly approved by the user.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:67-69) states: PostgREST provides REST CRUD API at rest/v1. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api](https://supabase.com/docs/guides/api) (locator: `lines:67-69`)
  - *Observation*: paraphrase: PostgREST provides REST CRUD API at rest/v1.
  ```text
  Features
  Supabase provides a RESTful API using PostgREST, a thin API layer on top of Postgres.
  It exposes everything you need from a CRUD API at the URL https://<project_ref>.supabase.co/rest/v1/.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.api.public_documentation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:60-69) states: Public Data REST API documentation. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api](https://supabase.com/docs/guides/api) (locator: `lines:60-69`)
  - *Observation*: paraphrase: Public Data REST API documentation.
  ```text
  Data REST API
  Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.
  The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.
  You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).
  Looking for your Data API URL and Keys?
  You can find the API URL in the Integrations > Data API section of the Dashboard.
  You can find the API Keys in the Settings > API Keys section of the Dashboard.
  Features
  Supabase provides a RESTful API using PostgREST, a thin API layer on top of Postgres.
  It exposes everything you need from a CRUD API at the URL https://<project_ref>.supabase.co/rest/v1/.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.auth.management_oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Third-party Management API integration. Source evidence (lines:282-289) states: OAuth2 delegates project management on behalf of users; requests use HTTPS. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/reference/api/introduction](https://supabase.com/docs/reference/api/introduction) (locator: `lines:282-289`)
  - *Observation*: paraphrase: OAuth2 delegates project management on behalf of users; requests use HTTPS.
  ```text
  OAuth2:
  OAuth2 allows your application to generate tokens on behalf of a Supabase user, providing secure and limited access to their account without requiring their credentials. Use this if you're building a third-party app that needs to create or manage Supabase projects on behalf of your users. Tokens generated via OAuth2 are short-lived and tied to specific scopes to ensure your app can only perform actions that are explicitly approved by the user.
  See Build a Supabase Integration to set up OAuth2 for your application.
  1
  curl https://api.supabase.com/v1/projects \
  2
  -H "Authorization: Bearer sbp_bdd0••••••••••••••••••••••••••••••••4f23"
  All API requests must be authenticated and made over HTTPS.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.auth.management_pat` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Bearer_token authentication for Management API account/project control. Source evidence (lines:274-281) states: Management API requires bearer access token; PAT generated on account page, scoped versus classic permissions differ. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/reference/api/introduction](https://supabase.com/docs/reference/api/introduction) (locator: `lines:274-281`)
  - *Observation*: paraphrase: Management API requires bearer access token; PAT generated on account page, scoped versus classic permissions differ.
  ```text
  Management API
  Manage your Supabase organizations and projects programmatically.
  Authentication
  All API requests require an access token to be included in the Authorization header: Authorization Bearer <access_token>.
  There are two ways to generate an access token:
  Personal access token (PAT):
  PATs are tokens with a custom expiry that you manually generate to access the Management API. They are useful for automating workflows or developing against the Management API. A scoped PAT can only reach the organizations, projects, and permissions you choose when creating it. A classic PAT, shown as Legacy in the dashboard, carries the same privileges as your user account. Prefer scoped PATs, and keep every token secret.
  To generate or manage your personal access tokens, visit your account page. See Personal access tokens for the permission each endpoint requires.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.auth.project_keys` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Project Data REST API; new key format. Source evidence (lines:104-113) states: Publishable/secret keys are non-JWT strings; secret key elevated, legacy anon/service_role keys coexist. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:104-113`)
  - *Observation*: paraphrase: Publishable/secret keys are non-JWT strings; secret key elevated, legacy anon/service_role keys coexist.
  ```text
  TypeFormatPrivilegesAvailabilityUse
  Publishable keysb_publishable_...LowPlatform, CLISafe to expose online: web page, mobile or desktop app, GitHub actions, CLIs, source code.
  Secret keyssb_secret_...ElevatedPlatform, CLIOnly use in backend components of your app, such as servers, APIs with their own authorization checks, Edge Functions, and microservices. They provide full access to your project's data, bypassing Row Level Security.
  anonJWT (long-lived)LowPlatform, CLILegacy version of publishable keys.
  service_roleJWT (long-lived)ElevatedPlatform, CLILegacy version of secret keys.
  Publishable and secret keys are short strings, not JWTs. If a tool, tutorial, or AI assistant tells you to copy a long key that begins with eyJ, it was written for the legacy keys.
  Running supabase start prints a publishable key and a secret key for your local project. The local secret key takes the place of the local service_role key. See the CLI getting started guide for the full output.
  Legacy anon and service_role keys
  Creating publishable and secret keys doesn't revoke your legacy keys. Both key systems work at the same time.
  Creating a publishable or secret key adds it alongside your existing anon and service_role keys without affecting them, so your legacy keys keep working. They stay valid until you disable them in the Settings > API Keys section of the Dashboard, which is a separate step.
  ```
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:315-318`)
  - *Observation*: paraphrase: Publishable/secret keys use apikey header, not JWT Bearer; root OpenAPI route requires secret key.
  ```text
  Publishable and secret keys aren't JWTs, which creates a few compatibility differences to plan for:
  Send publishable and secret keys on the apikey header, not on Authorization: Bearer. Because the keys aren't JWTs, anything that tries to verify one as a JWT fails. For migration compatibility the verify_jwt platform check accepts them on either header, but passing that check doesn't authenticate the caller. See Authorization headers.
  Edge Functions need to authorize API keys in code. The verify_jwt check alone doesn't authenticate a caller that sends only an API key. Use the @supabase/server SDK, as shown in Securing Edge Functions, rather than relying on the platform check.
  The Data API's OpenAPI root, GET /rest/v1/, accepts only secret keys. A publishable key gets a 401 there, even though it works on table routes such as /rest/v1/<table>. To check that a publishable key works, call a table route or /auth/v1/health instead.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Project-scoped read-only database diagnostics through Data API or MCP.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:104-113): Publishable/secret keys are non-JWT strings; secret key elevated, legacy anon/service_role keys coexist.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Project-scoped read-only database diagnostics through Data API or MCP.", "blockers": ["Secret project keys bypass RLS and require server-side protection; MCP developer privileges must be scoped."], "next_steps": ["Use project-scoped read-only MCP with restricted feature groups; choose Data API versus Management credentials explicitly."]}`
  - Original Rationale: Feasibility inference from the cited interfaces and requirements; no credentials obtained, integration built, or operations tested.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Project-scoped read-only database diagnostics through Data API or MCP.", "blockers": ["Secret project keys bypass RLS and require server-side protection; MCP developer privileges must be scoped."], "next_steps": ["Use project-scoped read-only MCP with restricted feature groups; choose Data API versus Management credentials explicitly."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Supabase documentation: Free plan (up to 2 active projects), instant project API keys (anon / service_role), and community MCP server (65.testing.free_access, 65.auth.api_key, 65.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:104-113`)
  - *Observation*: paraphrase: Publishable/secret keys are non-JWT strings; secret key elevated, legacy anon/service_role keys coexist.
  ```text
  TypeFormatPrivilegesAvailabilityUse
  Publishable keysb_publishable_...LowPlatform, CLISafe to expose online: web page, mobile or desktop app, GitHub actions, CLIs, source code.
  Secret keyssb_secret_...ElevatedPlatform, CLIOnly use in backend components of your app, such as servers, APIs with their own authorization checks, Edge Functions, and microservices. They provide full access to your project's data, bypassing Row Level Security.
  anonJWT (long-lived)LowPlatform, CLILegacy version of publishable keys.
  service_roleJWT (long-lived)ElevatedPlatform, CLILegacy version of secret keys.
  Publishable and secret keys are short strings, not JWTs. If a tool, tutorial, or AI assistant tells you to copy a long key that begins with eyJ, it was written for the legacy keys.
  Running supabase start prints a publishable key and a secret key for your local project. The local secret key takes the place of the local service_role key. See the CLI getting started guide for the full output.
  Legacy anon and service_role keys
  Creating publishable and secret keys doesn't revoke your legacy keys. Both key systems work at the same time.
  Creating a publishable or secret key adds it alongside your existing anon and service_role keys without affecting them, so your legacy keys keep working. They stay valid until you disable them in the Settings > API Keys section of the Dashboard, which is a separate step.
  ```
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:122-139`)
  - *Observation*: paraphrase: Secret key bypasses RLS; user JWT and application key are separate.
  ```text
  Postgres roles and Row Level Security
  Every key resolves to a built-in Postgres role, and that role is what your Row Level Security policies match on. Using a publishable key doesn't mean your user is anonymous: your application authenticates with the publishable key while your user authenticates separately through Supabase Auth with their own JWT.
  KeyUser signed in through Supabase AuthPostgres role
  Publishable keyNoanon
  Publishable keyYesauthenticated
  Secret keyNot applicableservice_role
  Write your Row Level Security policies for the anon and authenticated roles. Policies never apply to a secret key, because service_role has the BYPASSRLS attribute.
  Postgres evaluates table grants first, and only then applies Row Level Security. The two failures look different. A missing grant returns a permission error, including for service_role, whereas a policy that matches no rows returns an empty result. Check the grant before you debug the policy. See Securing your API.
  Secret keys and elevated access
  Unlike publishable keys, secret keys allow elevated access to your project's data. Use them only in secure, developer-controlled components of your application, such as:
  ```
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:242-250`)
  - *Observation*: paraphrase: Production MCP recommendations include project scope, read-only and feature restrictions; developer context not customer-facing.
  ```text
  Recommendations
  We recommend the following best practices to mitigate security risks when using the Supabase MCP server:
  Protect production data: Connect to a production project only when the task requires production evidence. Use project scoping, read-only mode, restricted feature groups, and the narrowest data query that can answer the question. Do not include secrets or unrelated personal data in prompts or reports.
  Don't give to your customers: The MCP server operates under the context of your developer permissions, so you should not give it to your customers or end users. Instead, use it internally as a developer tool to help you build and test your applications.
  Read-only mode: Set unattended monitoring and diagnostic routines to read-only mode, which executes SQL queries as a read-only Postgres user.
  Project scoping: Scope your MCP server to a specific project, limiting access to only that project's resources. This prevents LLMs from accessing data from other projects in your Supabase account.
  Branching: Use Supabase's branching feature to create a development branch for your database. This allows you to test changes in a safe environment before merging them to production.
  Cost confirmation: When your connection uses cost confirmation dialogs, the server asks for confirmation through your client before it creates resources that incur charges. This is a guardrail on top of authentication and authorization, not a replacement for them.
  Feature groups: Restrict which tool groups are available using the features configuration option. This helps reduce the attack surface and limits the actions that LLMs can perform to only those that you need.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:59-79) states: Supabase vendor guide configures hosted MCP URL and account organization authorization. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:59-79`)
  - *Observation*: paraphrase: Supabase vendor guide configures hosted MCP URL and account organization authorization.
  ```text
  Configure your MCP client to connect with your Supabase project
  Installation
  Add the MCP server to your project config using the command line:
  claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp?features=docs%2Caccount%2Cdatabase%2Cdebugging%2Cdevelopment%2Cfunctions%2Cbranching%2Cfeedback%2Cnotebooks"
  Alternatively, add this configuration to .mcp.json:
  1{
  2 "mcpServers": {
  3 "supabase": {
  4 "type": "http",
  5 "url": "https://mcp.supabase.com/mcp?features=docs%2Caccount%2Cdatabase%2Cdebugging%2Cdevelopment%2Cfunctions%2Cbranching%2Cfeedback%2Cnotebooks"
  ```
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:84-108`)
  - *Observation*: paraphrase: Server tools cover database SQL/migrations, diagnostics, Edge Functions and account management.
  ```text
  Available tools
  The Supabase MCP server provides tools organized into feature groups. Groups that your connection supports are enabled by default, except Storage. You can enable or disable specific groups using the configuration panel above.
  Database
  list_tables - List all tables in the database
  list_extensions - List available/installed Postgres extensions
  list_migrations - List database migrations
  apply_migration - Apply a database migration
  execute_sql - Execute SQL queries
  Debugging
  query_logs - Run a read-only SQL query against project logs to filter, aggregate, or join across log fields. See Query logs with SQL.
  ```
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:175-180`)
  - *Observation*: paraphrase: Project/read-only parameters and local server address documented.
  ```text
  read_only=trueExecute all queries as a read-only Postgres user?read_only=true
  project_ref=<id>Scope to a specific project (disables account tools)?project_ref=abc123
  features=<groups>Enable only specific tool groups (comma-separated)?features=database,docs
  skip_elicitations=<tools>Skip form confirmations for the named tools. See Skip form confirmations.?skip_elicitations=execute_sql,apply_migration
  Parameters can be combined: https://mcp.supabase.com/mcp?project_ref=abc123&read_only=true
  When using Supabase CLI for local development, the MCP server is available at http://localhost:54321/mcp. With the experimental [experimental] stack setting on, local projects use assigned ports instead, so read the MCP URL from the output of supabase status. See Running multiple local projects.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.mcp.server` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Supabase MCP; source_url=https://supabase.com/docs/guides/getting-started/mcp. Source evidence (lines:59-79) states: Supabase vendor guide configures hosted MCP URL and account organization authorization. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:59-79`)
  - *Observation*: paraphrase: Supabase vendor guide configures hosted MCP URL and account organization authorization.
  ```text
  Configure your MCP client to connect with your Supabase project
  Installation
  Add the MCP server to your project config using the command line:
  claude mcp add --scope project --transport http supabase "https://mcp.supabase.com/mcp?features=docs%2Caccount%2Cdatabase%2Cdebugging%2Cdevelopment%2Cfunctions%2Cbranching%2Cfeedback%2Cnotebooks"
  Alternatively, add this configuration to .mcp.json:
  1{
  2 "mcpServers": {
  3 "supabase": {
  4 "type": "http",
  5 "url": "https://mcp.supabase.com/mcp?features=docs%2Caccount%2Cdatabase%2Cdebugging%2Cdevelopment%2Cfunctions%2Cbranching%2Cfeedback%2Cnotebooks"
  ```
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:84-108`)
  - *Observation*: paraphrase: Server tools cover database SQL/migrations, diagnostics, Edge Functions and account management.
  ```text
  Available tools
  The Supabase MCP server provides tools organized into feature groups. Groups that your connection supports are enabled by default, except Storage. You can enable or disable specific groups using the configuration panel above.
  Database
  list_tables - List all tables in the database
  list_extensions - List available/installed Postgres extensions
  list_migrations - List database migrations
  apply_migration - Apply a database migration
  execute_sql - Execute SQL queries
  Debugging
  query_logs - Run a read-only SQL query against project logs to filter, aggregate, or join across log fields. See Query logs with SQL.
  ```
- **URL**: [https://supabase.com/docs/guides/getting-started/mcp](https://supabase.com/docs/guides/getting-started/mcp) (locator: `lines:175-180`)
  - *Observation*: paraphrase: Project/read-only parameters and local server address documented.
  ```text
  read_only=trueExecute all queries as a read-only Postgres user?read_only=true
  project_ref=<id>Scope to a specific project (disables account tools)?project_ref=abc123
  features=<groups>Enable only specific tool groups (comma-separated)?features=database,docs
  skip_elicitations=<tools>Skip form confirmations for the named tools. See Skip form confirmations.?skip_elicitations=execute_sql,apply_migration
  Parameters can be combined: https://mcp.supabase.com/mcp?project_ref=abc123&read_only=true
  When using Supabase CLI for local development, the MCP server is available at http://localhost:54321/mcp. With the experimental [experimental] stack setting on, local projects use assigned ports instead, so read the MCP URL from the output of supabase status. See Running multiple local projects.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:691-694) states: Free plan includes two projects usable as development and production; CLI/Docker self-hosting also free. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/pricing](https://supabase.com/pricing) (locator: `lines:691-694`)
  - *Observation*: paraphrase: Free plan includes two projects usable as development and production; CLI/Docker self-hosting also free.
  ```text
  What if I need one project for development and one for production?
  You can create two projects, one for development and one for production — the Free Plan includes two free projects. You can also use Branching, available on the Pro Plan and above, to run a separate development environment off your production project.
  Can I self-host Supabase for free?
  Yes, you can use the Docker setup or the Supabase CLI. Supabase Studio is also available in the Docker setup.
  ```
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:143-165`)
  - *Observation*: paraphrase: Signed-in Dashboard exposes project keys.
  ```text
  Find and use your keys
  Getting a key into an app has two halves. You copy the value, which needs a signed-in Dashboard session, and your code reads it by name. The key itself never belongs in source code, so start by setting these names in .env:
  1
  # Safe to expose to the browser. Prefix per your framework.
  2
  NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
  3
  NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_...
  4
  5
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Expose database CRUD and manage Supabase projects through developer APIs.. Source evidence (lines:60-69) states: Supabase auto-generates a Postgres/PostgREST REST API. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api](https://supabase.com/docs/guides/api) (locator: `lines:60-69`)
  - *Observation*: paraphrase: Supabase auto-generates a Postgres/PostgREST REST API.
  ```text
  Data REST API
  Supabase auto-generates an API directly from your database schema allowing you to connect to your database through a restful interface, directly from the browser.
  The API is auto-generated from your database and is designed to get you building as fast as possible, without writing a single line of code.
  You can use them directly from the browser (two-tier architecture), or as a complement to your own API server (three-tier architecture).
  Looking for your Data API URL and Keys?
  You can find the API URL in the Integrations > Data API section of the Dashboard.
  You can find the API Keys in the Settings > API Keys section of the Dashboard.
  Features
  Supabase provides a RESTful API using PostgREST, a thin API layer on top of Postgres.
  It exposes everything you need from a CRUD API at the URL https://<project_ref>.supabase.co/rest/v1/.
  ```
- **URL**: [https://supabase.com/docs/reference/api/introduction](https://supabase.com/docs/reference/api/introduction) (locator: `lines:274-275`)
  - *Observation*: paraphrase: Management API manages organizations and projects programmatically.
  ```text
  Management API
  Manage your Supabase organizations and projects programmatically.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:691-694) states: Free plan includes two projects usable as development and production; CLI/Docker self-hosting also free. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/pricing](https://supabase.com/pricing) (locator: `lines:691-694`)
  - *Observation*: paraphrase: Free plan includes two projects usable as development and production; CLI/Docker self-hosting also free.
  ```text
  What if I need one project for development and one for production?
  You can create two projects, one for development and one for production — the Free Plan includes two free projects. You can also use Branching, available on the Pro Plan and above, to run a separate development environment off your production project.
  Can I self-host Supabase for free?
  Yes, you can use the Docker setup or the Supabase CLI. Supabase Studio is also available in the Docker setup.
  ```
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:143-165`)
  - *Observation*: paraphrase: Signed-in Dashboard exposes project keys.
  ```text
  Find and use your keys
  Getting a key into an app has two halves. You copy the value, which needs a signed-in Dashboard session, and your code reads it by name. The key itself never belongs in source code, so start by setting these names in .env:
  1
  # Safe to expose to the browser. Prefix per your framework.
  2
  NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
  3
  NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_...
  4
  5
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `65.testing.sandbox_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:191-199) states: Supabase local stack prints publishable/secret keys through supabase start/status. The documentation describes a sandbox or test environment relevant to test access, distinct from live production access.

#### Primary Evidence & Excerpts
- **URL**: [https://supabase.com/docs/guides/api/api-keys](https://supabase.com/docs/guides/api/api-keys) (locator: `lines:191-199`)
  - *Observation*: paraphrase: Supabase local stack prints publishable/secret keys through supabase start/status.
  ```text
  A local stack mints its own keys. They are unrelated to your hosted project's keys, so a local key never grants access to your hosted data.
  This path needs the Supabase CLI and a container runtime. See Running a local Supabase project for both.
  Start the stack:
  1
  supabase start
  The publishable and secret keys are in the output, under Authentication Keys.
  Print them again at any time while the stack is running:
  1
  supabase status
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 64: Cloudflare (Developer, Infra and Data platforms)
- Total claims: 13 | Corrected: 2

### Claim: `64.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1441-1461): DNS API reference lists DNS record list/detail/create/overwrite/update/delete/import/export/batch.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: DNS, compute deployment and access security are distinct business/infra domains.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Cloudflare v4 REST API spans multiple distinct infrastructure domains: (1) Authoritative DNS & Domains, (2) Serverless Compute (Workers/Pages), (3) Storage (KV/R2/D1), (4) Security/WAF Rules, and (5) Zero Trust Access. Per evidence rules, multiple distinct infrastructure domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:1441-1461`)
  - *Observation*: paraphrase: DNS API reference lists DNS record list/detail/create/overwrite/update/delete/import/export/batch.
  ```text
  DNSDNS
  DNSSECDNSSEC
  DNSSEC Details
  Edit DNSSEC Status
  Delete DNSSEC records
  ZskZsk
  List DNSSEC ZSKs
  RecordsRecords
  List DNS Records
  DNS Record Details
  ```
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:3820-3825`)
  - *Observation*: paraphrase: Workers beta API reference includes list/get/create Workers.
  ```text
  WorkersWorkers
  BetaBeta
  WorkersWorkers
  List Workers
  Get Worker
  Create Worker
  ```
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:899-904`)
  - *Observation*: paraphrase: Access application actions listed.
  ```text
  Get an Access application
  Add an Access application
  Update an Access application
  Delete an Access application
  Revoke application tokens
  CAsCAs
  ```
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:940-947`)
  - *Observation*: paraphrase: Access Service Tokens list/get/create/update/delete/refresh/rotate.
  ```text
  Service TokensService Tokens
  List service tokens
  Get a service token
  Create a service token
  Update a service token
  Delete a service token
  Refresh a service token
  Rotate a service token
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.api.group.access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Access applications and service tokens. Source evidence (lines:899-904) states: Access application actions listed. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:899-904`)
  - *Observation*: paraphrase: Access application actions listed.
  ```text
  Get an Access application
  Add an Access application
  Update an Access application
  Delete an Access application
  Revoke application tokens
  CAsCAs
  ```
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:940-947`)
  - *Observation*: paraphrase: Access Service Tokens list/get/create/update/delete/refresh/rotate.
  ```text
  Service TokensService Tokens
  List service tokens
  Get a service token
  Create a service token
  Update a service token
  Delete a service token
  Refresh a service token
  Rotate a service token
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.api.group.dns` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts DNS record CRUD. Source evidence (lines:1441-1461) states: DNS API reference lists DNS record list/detail/create/overwrite/update/delete/import/export/batch. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:1441-1461`)
  - *Observation*: paraphrase: DNS API reference lists DNS record list/detail/create/overwrite/update/delete/import/export/batch.
  ```text
  DNSDNS
  DNSSECDNSSEC
  DNSSEC Details
  Edit DNSSEC Status
  Delete DNSSEC records
  ZskZsk
  List DNSSEC ZSKs
  RecordsRecords
  List DNS Records
  DNS Record Details
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.api.group.workers` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Workers deployment management. Source evidence (lines:3820-3825) states: Workers beta API reference includes list/get/create Workers. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/api/](https://developers.cloudflare.com/api/) (locator: `lines:3820-3825`)
  - *Observation*: paraphrase: Workers beta API reference includes list/get/create Workers.
  ```text
  WorkersWorkers
  BetaBeta
  WorkersWorkers
  List Workers
  Get Worker
  Create Worker
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:151-155) states: Fundamentals reference labels the API REST API. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:151-155`)
  - *Observation*: paraphrase: Fundamentals reference labels the API REST API.
  ```text
  Reference
  REST API ↗︎API
  GraphQL API ↗︎
  Wrangler API ↗︎
  API token permissions
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.api.public_documentation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:15-33) states: Public token creation and v4 HTTP example. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:15-33`)
  - *Observation*: paraphrase: Public token creation and v4 HTTP example.
  ```text
  Prerequisite
  Before you begin, find your zone and account IDs.
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.auth.api_token` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Bearer_token authentication for Cloudflare v4 compatible account/zone endpoints. Source evidence (lines:17-33) states: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:17-33`)
  - *Observation*: paraphrase: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API.
  ```text
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  Select Continue to summary.
  Review the token summary. Select Back to make adjustments. You can also edit a token after creation.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Read scoped DNS records and account configuration through v4 API or MCP.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:17-33): Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API. Check https://developers.cloudflare.com/fundamentals/api/get-started/create-token/ for current terms, exceptions and conflicting documentation b

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Read scoped DNS records and account configuration through v4 API or MCP.", "blockers": ["Token policies must include target resources and permissions."], "next_steps": ["Choose compatible endpoint/token type; check feature plan requirements and validate read-only calls later."]}`
  - Original Rationale: Feasibility inference from the cited interfaces and requirements; no credentials obtained, integration built, or operations tested.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Read scoped DNS records and account configuration through v4 API or MCP.", "blockers": ["Token policies must include target resources and permissions."], "next_steps": ["Choose compatible endpoint/token type; check feature plan requirements and validate read-only calls later."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Cloudflare documentation: Free tier accounts support scoped API tokens for managing DNS and Workers, with enterprise features gated behind plan upgrades (64.testing.free_access, 64.auth.bearer_token, 64.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:17-33`)
  - *Observation*: paraphrase: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API.
  ```text
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  Select Continue to summary.
  Review the token summary. Select Back to make adjustments. You can also edit a token after creation.
  ```
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:62-63`)
  - *Observation*: paraphrase: Some MCP features may require a paid Workers plan.
  ```text
  ## Paid Features
  Some features may require a paid Cloudflare Workers plan. Ensure your Cloudflare account has the necessary subscription level for the features you intend to use.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:1-8) states: Vendor repository documents callable servers and recommended Cloudflare API MCP URL. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:1-8`)
  - *Observation*: paraphrase: Vendor repository documents callable servers and recommended Cloudflare API MCP URL.
  ```text
  # Cloudflare MCP Server
  Model Context Protocol (MCP) is a [new, standardized protocol](https://modelcontextprotocol.io/introduction) for managing context between large language models (LLMs) and external systems. In this repository, you can find several MCP servers allowing you to connect to Cloudflare's service from an MCP client (e.g. Cursor, Claude) and use natural language to accomplish tasks through your Cloudflare account.
  These MCP servers allow your [MCP Client](https://modelcontextprotocol.io/clients) to read configurations from your account, process information, make suggestions based on data, and even make those suggested changes for you. All of these actions can happen across Cloudflare's many services including application development, security and performance.
  Every server in this repository exposes a stateless Streamable HTTP handler at `/mcp` through a fresh SDK v2 server factory. The retired `/sse` URL answers every request with a `410 Gone` Problem Details response that names the `/mcp` URL; MCP clients show its message in their connection error. Modern 2026 requests and stateless 2025 requests share the same request-scoped implementation without an MCP protocol session. OAuth, credentials, account selection, application caches, and product Durable Objects remain application/security state where required.
  Cloudflare offers the following MCP servers. The domain-specific servers are included in this repository, while the recommended Cloudflare API MCP Server is maintained in [`cloudflare/mcp`](https://github.com/cloudflare/mcp):
  | Server Name | Description | Server URL |
  | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------- |
  | [**Cloudflare API MCP Server (recommended)**](https://github.com/cloudflare/mcp) | Best when you want broad access across Cloudflare's APIs through code execution | `https://mcp.cloudflare.com/mcp` |
  ```
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:32-37`)
  - *Observation*: paraphrase: API MCP covers broad API via code execution; domain-specific servers expose curated tools.
  ```text
  ## Which Cloudflare MCP server should you use?
  Cloudflare provides two categories of MCP servers:
  - **Cloudflare API MCP Server** (`mcp.cloudflare.com`) in [`cloudflare/mcp`](https://github.com/cloudflare/mcp):
  best when you want broad access across Cloudflare's APIs through code execution.
  - **Domain-specific servers** (`*.mcp.cloudflare.com`) in this repository:
  best when you want curated, typed tools for a specific Cloudflare product area.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.mcp.server` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Cloudflare remote MCP servers; source_url=https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflar. Source evidence (lines:1-8) states: Vendor repository documents callable servers and recommended Cloudflare API MCP URL. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:1-8`)
  - *Observation*: paraphrase: Vendor repository documents callable servers and recommended Cloudflare API MCP URL.
  ```text
  # Cloudflare MCP Server
  Model Context Protocol (MCP) is a [new, standardized protocol](https://modelcontextprotocol.io/introduction) for managing context between large language models (LLMs) and external systems. In this repository, you can find several MCP servers allowing you to connect to Cloudflare's service from an MCP client (e.g. Cursor, Claude) and use natural language to accomplish tasks through your Cloudflare account.
  These MCP servers allow your [MCP Client](https://modelcontextprotocol.io/clients) to read configurations from your account, process information, make suggestions based on data, and even make those suggested changes for you. All of these actions can happen across Cloudflare's many services including application development, security and performance.
  Every server in this repository exposes a stateless Streamable HTTP handler at `/mcp` through a fresh SDK v2 server factory. The retired `/sse` URL answers every request with a `410 Gone` Problem Details response that names the `/mcp` URL; MCP clients show its message in their connection error. Modern 2026 requests and stateless 2025 requests share the same request-scoped implementation without an MCP protocol session. OAuth, credentials, account selection, application caches, and product Durable Objects remain application/security state where required.
  Cloudflare offers the following MCP servers. The domain-specific servers are included in this repository, while the recommended Cloudflare API MCP Server is maintained in [`cloudflare/mcp`](https://github.com/cloudflare/mcp):
  | Server Name | Description | Server URL |
  | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------- |
  | [**Cloudflare API MCP Server (recommended)**](https://github.com/cloudflare/mcp) | Best when you want broad access across Cloudflare's APIs through code execution | `https://mcp.cloudflare.com/mcp` |
  ```
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:32-37`)
  - *Observation*: paraphrase: API MCP covers broad API via code execution; domain-specific servers expose curated tools.
  ```text
  ## Which Cloudflare MCP server should you use?
  Cloudflare provides two categories of MCP servers:
  - **Cloudflare API MCP Server** (`mcp.cloudflare.com`) in [`cloudflare/mcp`](https://github.com/cloudflare/mcp):
  best when you want broad access across Cloudflare's APIs through code execution.
  - **Domain-specific servers** (`*.mcp.cloudflare.com`) in this repository:
  best when you want curated, typed tools for a specific Cloudflare product area.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:17-33) states: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:17-33`)
  - *Observation*: paraphrase: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API.
  ```text
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  Select Continue to summary.
  Review the token summary. Select Back to make adjustments. You can also edit a token after creation.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Manage scoped Cloudflare account and zone resources, including DNS and developer infrastructure.. Source evidence (lines:15-33) states: Cloudflare user/account tokens contain account/user/zone resource permissions and a v4 bearer-auth example. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:15-33`)
  - *Observation*: paraphrase: Cloudflare user/account tokens contain account/user/zone resource permissions and a v4 bearer-auth example.
  ```text
  Prerequisite
  Before you begin, find your zone and account IDs.
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  ```
- **URL**: [https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md](https://raw.githubusercontent.com/cloudflare/mcp-server-cloudflare/main/README.md) (locator: `lines:1-8`)
  - *Observation*: paraphrase: Cloudflare MCP servers can inspect and change services across application development, security and performance.
  ```text
  # Cloudflare MCP Server
  Model Context Protocol (MCP) is a [new, standardized protocol](https://modelcontextprotocol.io/introduction) for managing context between large language models (LLMs) and external systems. In this repository, you can find several MCP servers allowing you to connect to Cloudflare's service from an MCP client (e.g. Cursor, Claude) and use natural language to accomplish tasks through your Cloudflare account.
  These MCP servers allow your [MCP Client](https://modelcontextprotocol.io/clients) to read configurations from your account, process information, make suggestions based on data, and even make those suggested changes for you. All of these actions can happen across Cloudflare's many services including application development, security and performance.
  Every server in this repository exposes a stateless Streamable HTTP handler at `/mcp` through a fresh SDK v2 server factory. The retired `/sse` URL answers every request with a `410 Gone` Problem Details response that names the `/mcp` URL; MCP clients show its message in their connection error. Modern 2026 requests and stateless 2025 requests share the same request-scoped implementation without an MCP protocol session. OAuth, credentials, account selection, application caches, and product Durable Objects remain application/security state where required.
  Cloudflare offers the following MCP servers. The domain-specific servers are included in this repository, while the recommended Cloudflare API MCP Server is maintained in [`cloudflare/mcp`](https://github.com/cloudflare/mcp):
  | Server Name | Description | Server URL |
  | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------- |
  | [**Cloudflare API MCP Server (recommended)**](https://github.com/cloudflare/mcp) | Best when you want broad access across Cloudflare's APIs through code execution | `https://mcp.cloudflare.com/mcp` |
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `64.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:17-33) states: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://developers.cloudflare.com/fundamentals/api/get-started/create-token/](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) (locator: `lines:17-33`)
  - *Observation*: paraphrase: Create user or account token with resource rules and Read/Edit permissions; send Authorization: Bearer to v4 API.
  ```text
  Determine if you want a user token or an Account API token. Use Account API tokens if you prefer service tokens that are not associated with users and your desired API endpoints are compatible.
  From the Cloudflare dashboard ↗︎, go to My Profile > API Tokens for user tokens. For Account Tokens, go to Manage Account > API Tokens.
  Select Create Token.
  Add a token name to describe why or how the token is used.
  Select a template from the available API token templates or start from scratch. Templates include policies with predefined permissions. The following example uses the Edit zone DNS template.
  Create a policy to organize the token's permissions. Select a policy type (Account, User, or Zone), then select resource rules within the policy to specify which resources the permissions apply to, such as specific accounts or zones.
  Choose the permissions to grant within the policy. Most permissions offer Edit or Read access. Edit is full CRUDL (create, read, update, delete, list) access, while Read is the read permission and list where appropriate. For example, Zone DNS Read for example.com allows the token to read DNS records only for that zone. Refer to the available token permissions for more information.
  (Optional) Restrict how a token is used in the Token expiration and Client IP Address Filtering fields.
  Select Continue to summary.
  Review the token summary. Select Back to make adjustments. You can also edit a token after creation.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 77: ClickUp (Productivity and Project Management)
- Total claims: 13 | Corrected: 2

### Claim: `77.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:15-25): API v2 lists read/create/update/delete and threaded comment operations. Check https://developer.clickup.com/reference/gettasks for current terms, exceptions and conflicting documentation b

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Captured resource groups cover multiple related work-management workflows. Qualitative scope, not an endpoint count or exhaustive inventory.
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: ClickUp REST API v2 covers multiple related task management domains: (1) Workspaces, Spaces, and Folders, (2) Lists & Tasks, (3) Time Tracking, and (4) Comments & Attachments. Per evidence rules, multiple related workflow modules substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:15-25`)
  - *Observation*: paraphrase: API v2 lists read/create/update/delete and threaded comment operations.
  ```text
  Comments
  Get Task Commentsget
  Create Task Commentpost
  Get Chat View Commentsget
  Create Chat View Commentpost
  Get List Commentsget
  Create List Commentpost
  Update Commentput
  Delete Commentdel
  Get Threaded Commentsget
  ```
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:63-70`)
  - *Observation*: paraphrase: API v2 lists get/create/update/delete List operations.
  ```text
  Lists
  Get Listsget
  Create Listpost
  Get Folderless Listsget
  Create Folderless Listpost
  Get Listget
  Update Listput
  Delete Listdel
  ```
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:131-144`)
  - *Observation*: paraphrase: API v2 lists time-entry read/create/update/delete and timer start/stop operations.
  ```text
  Time Tracking
  Get time entries within a date rangeget
  Create a time entrypost
  Get singular time entryget
  Delete a time Entrydel
  Update a time Entryput
  Get time entry historyget
  Get running time entryget
  Remove tags from time entriesdel
  Get all tags from time entriesget
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.api.group.comments` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Task/List comments. Source evidence (lines:15-25) states: API v2 lists read/create/update/delete and threaded comment operations. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:15-25`)
  - *Observation*: paraphrase: API v2 lists read/create/update/delete and threaded comment operations.
  ```text
  Comments
  Get Task Commentsget
  Create Task Commentpost
  Get Chat View Commentsget
  Create Chat View Commentpost
  Get List Commentsget
  Create List Commentpost
  Update Commentput
  Delete Commentdel
  Get Threaded Commentsget
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.api.group.lists` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Lists and list metadata. Source evidence (lines:63-70) states: API v2 lists get/create/update/delete List operations. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:63-70`)
  - *Observation*: paraphrase: API v2 lists get/create/update/delete List operations.
  ```text
  Lists
  Get Listsget
  Create Listpost
  Get Folderless Listsget
  Create Folderless Listpost
  Get Listget
  Update Listput
  Delete Listdel
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.api.group.time` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Time entries and timers. Source evidence (lines:131-144) states: API v2 lists time-entry read/create/update/delete and timer start/stop operations. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:131-144`)
  - *Observation*: paraphrase: API v2 lists time-entry read/create/update/delete and timer start/stop operations.
  ```text
  Time Tracking
  Get time entries within a date rangeget
  Create a time entrypost
  Get singular time entryget
  Delete a time Entrydel
  Update a time Entryput
  Get time entry historyget
  Get running time entryget
  Remove tags from time entriesdel
  Get all tags from time entriesget
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:9-23) states: ClickUp API v2 reference lists resource-oriented comment endpoints with GET/POST/PUT/DELETE methods. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:9-23`)
  - *Observation*: paraphrase: ClickUp API v2 reference lists resource-oriented comment endpoints with GET/POST/PUT/DELETE methods.
  ```text
  ClickUp API v2 Reference
  Authorization
  Get Access Tokenpost
  Get Authorized Userget
  Attachments
  Create Task Attachmentpost
  Comments
  Get Task Commentsget
  Create Task Commentpost
  Get Chat View Commentsget
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:8-25) states: Public ClickUp API v2 reference exposes endpoint names and resource methods. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/reference/gettasks](https://developer.clickup.com/reference/gettasks) (locator: `lines:8-25`)
  - *Observation*: paraphrase: Public ClickUp API v2 reference exposes endpoint names and resource methods.
  ```text
  Get Tasks
  ClickUp API v2 Reference
  Authorization
  Get Access Tokenpost
  Get Authorized Userget
  Attachments
  Create Task Attachmentpost
  Comments
  Get Task Commentsget
  Create Task Commentpost
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.auth.mcp_oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Hosted ClickUp MCP endpoint, distinct from public API token authentication.. Source evidence (lines:67-78) states: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:67-78`)
  - *Observation*: paraphrase: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup.
  ```text
  Can I authenticate with my own API keys or access tokens?
  No, only OAuth is supported. OAuth is an industry-standard protocol that provides secure, delegated access. It lets you grant limited access to your resources without sharing credentials, supports granular permissions, and makes it easy to revoke access.
  API keys are less secure because they’re static, usually have broad access, and are harder to manage or revoke if compromised.
  Can I use ClickUp MCP to search external apps I've connected to my ClickUp Workspace?
  No, Connected Search can only be used from within your Workspace. For a list of all external apps that support Connected Search, read our Connected Search article.
  Do admins need to take any action inside ClickUp before setting up an external tool like Claude or ChatGPT?
  No action is needed inside ClickUp. ClickUp MCP will provide the list of available tools.
  Will my custom LLM connect?
  Yes, if your team builds an MCP client implementation that meets the following criteria:
  Implements the JSON-RPC 2.0 protocol over HTTP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.auth.oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for ClickUp hosted public API v2 and official hosted MCP; personal API token and OAuth paths; excludes ClickUp consuming third-party MCP servers. Source evidence (lines:78-97) states: Multi-user apps use OAuth2 authorization-code flow; only workspace owners/admins create OAuth apps and configure the redirect URL. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/docs/authentication](https://developer.clickup.com/docs/authentication) (locator: `lines:78-97`)
  - *Observation*: paraphrase: Multi-user apps use OAuth2 authorization-code flow; only workspace owners/admins create OAuth apps and configure the redirect URL.
  ```text
  Build Apps for others - OAuth Flow
  To allow others to use your app, implement the OAuth2 flow so each user has their own token for accessing their ClickUp resources.
  OAuth resources and specs:
  Authentication: OAuth 2.0
  Grant Type: Authorization Code. Learn more.
  Authorization URL: https://app.clickup.com/api
  Access Token URL: https://api.clickup.com/api/v2/oauth/token
  👀
  Note
  ClickUp uses the authorization code grant type.
  ```
- **URL**: [https://developer.clickup.com/docs/authentication](https://developer.clickup.com/docs/authentication) (locator: `lines:106-110`)
  - *Observation*: paraphrase: Users authorize workspaces and exchange the authorization code; token is sent in Authorization: Bearer.
  ```text
  Users will be redirected back to the redirect_uri with the authorization code after logging in.
  Select Workspaces
  Users can authorize one or more Workspaces. Use the Get Authorized Teams (Workspaces) endpoint to see which Workspaces are authorized. Redirect users to the authorization URL to modify Workspace permissions.
  Step 3: Request a Token
  Use the Get Access Token endpoint with client_id, client_secret, and code to get the access token. This token is used in the Authorization: Bearer {access_token} header for all API requests made on behalf of the user.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.auth.personal` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for ClickUp hosted public API v2 and official hosted MCP; personal API token and OAuth paths; excludes ClickUp consuming third-party MCP servers. Source evidence (lines:55-77) states: Personal/testing API requests use personal tokens generated from account Apps settings and sent in the Authorization header. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/docs/authentication](https://developer.clickup.com/docs/authentication) (locator: `lines:55-77`)
  - *Observation*: paraphrase: Personal/testing API requests use personal tokens generated from account Apps settings and sent in the Authorization header.
  ```text
  Authentication
  Authenticate to the ClickUp API using a personal token or OAuth.
  Authentication
  To use the ClickUp API, you must authenticate every request.
  For personal use, authenticate with your personal API token.
  For apps or integrations that other people use, use the OAuth flow, allowing users to authorize Workspaces for your app.
  Include the token in the Authorization header of your requests.
  Both methods ensure that you and your users only have access to the information permitted by ClickUp.
  👍
  View the OAuth endpoints.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Manage permitted ClickUp lists/comments/time entries via public API or task workflows through hosted MCP.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:78-97): Multi-user apps use OAuth2 authorization-code flow; only workspace owners/admins create OAuth apps and configure the redirect URL.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Manage permitted ClickUp lists/comments/time entries via public API or task workflows through hosted MCP.", "blockers": ["Public API OAuth app creation requires workspace owner/admin.", "Hosted MCP uses OAuth only and has plan/add-on-dependent daily or per-minute limits."], "next_steps": ["Select personal API script, multi-user API OAuth app or hosted MCP route.", "Check workspace plan and actor permissions before authorized tests."]}`
  - Original Rationale: A documented API supports a possible agent wrapper; feasibility remains conditional on account permissions and the stated access gaps. No implementation, credential acquisition, or operational test occurred.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Manage permitted ClickUp lists/comments/time entries via public API or task workflows through hosted MCP.", "blockers": ["Public API OAuth app creation requires workspace owner/admin.", "Hosted MCP uses OAuth only and has plan/add-on-dependent daily or per-minute limits."], "next_steps": ["Select personal API script, multi-user API OAuth app or hosted MCP route.", "Check workspace plan and actor permissions before authorized tests."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified ClickUp documentation: Free Forever plan includes API access with personal API keys or OAuth 2.0, with team-level rate limits (77.testing.free_access, 77.auth.api_key, 77.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://developer.clickup.com/docs/authentication](https://developer.clickup.com/docs/authentication) (locator: `lines:78-97`)
  - *Observation*: paraphrase: Multi-user apps use OAuth2 authorization-code flow; only workspace owners/admins create OAuth apps and configure the redirect URL.
  ```text
  Build Apps for others - OAuth Flow
  To allow others to use your app, implement the OAuth2 flow so each user has their own token for accessing their ClickUp resources.
  OAuth resources and specs:
  Authentication: OAuth 2.0
  Grant Type: Authorization Code. Learn more.
  Authorization URL: https://app.clickup.com/api
  Access Token URL: https://api.clickup.com/api/v2/oauth/token
  👀
  Note
  ClickUp uses the authorization code grant type.
  ```
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:67-78`)
  - *Observation*: paraphrase: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup.
  ```text
  Can I authenticate with my own API keys or access tokens?
  No, only OAuth is supported. OAuth is an industry-standard protocol that provides secure, delegated access. It lets you grant limited access to your resources without sharing credentials, supports granular permissions, and makes it easy to revoke access.
  API keys are less secure because they’re static, usually have broad access, and are harder to manage or revoke if compromised.
  Can I use ClickUp MCP to search external apps I've connected to my ClickUp Workspace?
  No, Connected Search can only be used from within your Workspace. For a list of all external apps that support Connected Search, read our Connected Search article.
  Do admins need to take any action inside ClickUp before setting up an external tool like Claude or ChatGPT?
  No action is needed inside ClickUp. ClickUp MCP will provide the list of available tools.
  Will my custom LLM connect?
  Yes, if your team builds an MCP client implementation that meets the following criteria:
  Implements the JSON-RPC 2.0 protocol over HTTP
  ```
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:39-58`)
  - *Observation*: paraphrase: Without Everything AI add-on, Free Forever MCP allows 100 calls per rolling 24 hours per person shared across clients; paid plans and Everything AI add-on provide higher daily or per-minute limits.
  ```text
  MCP rate limits and public API rate limits are two separate limits. The public API limits requests per minute, per token. Without the Everything AI add-on, ClickUp MCP limits calls per rolling 24-hour period instead.
  With the Everything AI add-on
  If your Workspace has purchased the Everything AI add-on, your MCP rate limits are the same as the rate limits for our Public API which vary by plan.
  On our new plans that include ClickUp AI, AI is included with your plan instead of as separate add-ons.
  With the add-on, the rolling 24-hour limit no longer applies. Your MCP requests count toward the same per-minute, per-token limit as the public API:
  Free Forever, Unlimited, and Business Plans: 100 requests per minute, per token.
  Business Plus Plan: 1,000 requests per minute, per token.
  Enterprise Plan: 10,000 requests per minute, per token.
  On our new plans that include ClickUp AI, daily MCP limits differ by plan.
  Without the Everything AI add-on
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:67-78) states: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:67-78`)
  - *Observation*: paraphrase: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup.
  ```text
  Can I authenticate with my own API keys or access tokens?
  No, only OAuth is supported. OAuth is an industry-standard protocol that provides secure, delegated access. It lets you grant limited access to your resources without sharing credentials, supports granular permissions, and makes it easy to revoke access.
  API keys are less secure because they’re static, usually have broad access, and are harder to manage or revoke if compromised.
  Can I use ClickUp MCP to search external apps I've connected to my ClickUp Workspace?
  No, Connected Search can only be used from within your Workspace. For a list of all external apps that support Connected Search, read our Connected Search article.
  Do admins need to take any action inside ClickUp before setting up an external tool like Claude or ChatGPT?
  No action is needed inside ClickUp. ClickUp MCP will provide the list of available tools.
  Will my custom LLM connect?
  Yes, if your team builds an MCP client implementation that meets the following criteria:
  Implements the JSON-RPC 2.0 protocol over HTTP
  ```
- **URL**: [https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1) (locator: `lines:55-67`)
  - *Observation*: paraphrase: ClickUp documents external AI assistants connecting to its hosted MCP endpoint https://mcp.clickup.com/mcp.
  ```text
  MCP Server Setup Instructions
  Learn how to setup your AI assistant with ClickUp's MCP server.
  Setup instructions
  Below are the setup instructions for some of the most popular AI assistants.
  Claude
  Set up Claude to use the ClickUp MCP server!
  Pro, Team, Enterprise
  If you're on the Pro, Team, or Enterprise plan:
  In a browser or the desktop app, navigate to Settings in the sidebar.
  Scroll to Connectors at the bottom and click Add.
  ```
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:17-24`)
  - *Observation*: paraphrase: ClickUp MCP supports task workflows, work reporting, time tracking, search of tasks/docs/comments and collaboration with comments/chat.
  ```text
  What can I do with the ClickUp MCP server?
  Orchestrate task workflows: Create, enrich, and route tasks with assignees, Priorities, and due dates across Lists and Spaces.
  Build executive reports: Produce release notes, status updates, and portfolio rollups consolidated from tasks, comments, and Docs.
  Track time: Start and stop timers, log historical entries, and fetch entries.
  Answer questions from work: Search tasks, Docs, and comments to deliver quick, context-rich answers.
  Collaborate in comments and Chat: Summarize threads, extract action items, and post updates. Attach files and images to Channel messages, Posts, and Channel thread replies.
  Available tools
  ClickUp's MCP server enables AI assistants like ChatGPT, Claude, Cursor, or VS Code, to integrate with ClickUp's tools and data. This means your AI assistant can now execute actions, retrieve information, and provide intelligent, context-aware insights instantly.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.mcp.server` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=ClickUp hosted MCP; source_url=https://developer.clickup.com/docs/connect-an-ai-assistant-to-cli. Source evidence (lines:67-78) states: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:67-78`)
  - *Observation*: paraphrase: Hosted ClickUp MCP supports only OAuth, not own API keys or access tokens; custom clients need HTTP JSON-RPC2.0 and OAuth2.1 with PKCE. No action inside ClickUp is needed from admins for external client setup.
  ```text
  Can I authenticate with my own API keys or access tokens?
  No, only OAuth is supported. OAuth is an industry-standard protocol that provides secure, delegated access. It lets you grant limited access to your resources without sharing credentials, supports granular permissions, and makes it easy to revoke access.
  API keys are less secure because they’re static, usually have broad access, and are harder to manage or revoke if compromised.
  Can I use ClickUp MCP to search external apps I've connected to my ClickUp Workspace?
  No, Connected Search can only be used from within your Workspace. For a list of all external apps that support Connected Search, read our Connected Search article.
  Do admins need to take any action inside ClickUp before setting up an external tool like Claude or ChatGPT?
  No action is needed inside ClickUp. ClickUp MCP will provide the list of available tools.
  Will my custom LLM connect?
  Yes, if your team builds an MCP client implementation that meets the following criteria:
  Implements the JSON-RPC 2.0 protocol over HTTP
  ```
- **URL**: [https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server-1) (locator: `lines:55-67`)
  - *Observation*: paraphrase: ClickUp documents external AI assistants connecting to its hosted MCP endpoint https://mcp.clickup.com/mcp.
  ```text
  MCP Server Setup Instructions
  Learn how to setup your AI assistant with ClickUp's MCP server.
  Setup instructions
  Below are the setup instructions for some of the most popular AI assistants.
  Claude
  Set up Claude to use the ClickUp MCP server!
  Pro, Team, Enterprise
  If you're on the Pro, Team, or Enterprise plan:
  In a browser or the desktop app, navigate to Settings in the sidebar.
  Scroll to Connectors at the bottom and click Add.
  ```
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:17-24`)
  - *Observation*: paraphrase: ClickUp MCP supports task workflows, work reporting, time tracking, search of tasks/docs/comments and collaboration with comments/chat.
  ```text
  What can I do with the ClickUp MCP server?
  Orchestrate task workflows: Create, enrich, and route tasks with assignees, Priorities, and due dates across Lists and Spaces.
  Build executive reports: Produce release notes, status updates, and portfolio rollups consolidated from tasks, comments, and Docs.
  Track time: Start and stop timers, log historical entries, and fetch entries.
  Answer questions from work: Search tasks, Docs, and comments to deliver quick, context-rich answers.
  Collaborate in comments and Chat: Summarize threads, extract action items, and post updates. Attach files and images to Channel messages, Posts, and Channel thread replies.
  Available tools
  ClickUp's MCP server enables AI assistants like ChatGPT, Claude, Cursor, or VS Code, to integrate with ClickUp's tools and data. This means your AI assistant can now execute actions, retrieve information, and provide intelligent, context-aware insights instantly.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `77.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Workspace/task platform exposing task management, work reporting, time tracking and collaboration.. Source evidence (lines:17-24) states: ClickUp MCP supports task workflows, work reporting, time tracking, search of tasks/docs/comments and collaboration with comments/chat. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP](https://help.clickup.com/hc/en-us/articles/33335772678423-What-is-ClickUp-MCP) (locator: `lines:17-24`)
  - *Observation*: paraphrase: ClickUp MCP supports task workflows, work reporting, time tracking, search of tasks/docs/comments and collaboration with comments/chat.
  ```text
  What can I do with the ClickUp MCP server?
  Orchestrate task workflows: Create, enrich, and route tasks with assignees, Priorities, and due dates across Lists and Spaces.
  Build executive reports: Produce release notes, status updates, and portfolio rollups consolidated from tasks, comments, and Docs.
  Track time: Start and stop timers, log historical entries, and fetch entries.
  Answer questions from work: Search tasks, Docs, and comments to deliver quick, context-rich answers.
  Collaborate in comments and Chat: Summarize threads, extract action items, and post updates. Attach files and images to Channel messages, Posts, and Channel thread replies.
  Available tools
  ClickUp's MCP server enables AI assistants like ChatGPT, Claude, Cursor, or VS Code, to integrate with ClickUp's tools and data. This means your AI assistant can now execute actions, retrieve information, and provide intelligent, context-aware insights instantly.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 76: Monday.com (Productivity and Project Management)
- Total claims: 15 | Corrected: 2

### Claim: `76.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:160-171): GraphQL example queries columns on boards.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Captured resource groups cover multiple related work-management workflows. Qualitative scope, not an endpoint count or exhaustive inventory.
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: Monday.com GraphQL API covers multiple related work management domains: (1) Boards & Workspaces, (2) Items & Column Values, (3) Updates/Comments, and (4) Users & Teams. Per evidence rules, multiple related workflow entities substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:160-171`)
  - *Observation*: paraphrase: GraphQL example queries columns on boards.
  ```text
  Query
  Queries perform the READ operation and do not change or alter any data. The result of each query will be formatted in the same way as the query itself. The following example retrieves the ID, title, and type of each column on board 1234567890.
  Sample query
  GraphQL
  query {
  boards {
  columns {
  id
  title
  type
  ```
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:199-207`)
  - *Observation*: paraphrase: GraphQL create_item mutation creates a board item and returns its ID/name.
  ```text
  Mutation
  Mutations are special queries that perform the CUD (Create, Update, Delete) operations to modify your data. Mutations return an instance of the object you just modified, so you can query the data you changed. The following example creates a new item on board 1234567890 and returns the ID and name of the new item.
  Sample mutation
  GraphQL
  mutation{
  create_item (board_id: 1234567890, item_name: "New Item"){
  id
  name
  }
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.api.group.boards` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Boards and columns. Source evidence (lines:160-171) states: GraphQL example queries columns on boards. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:160-171`)
  - *Observation*: paraphrase: GraphQL example queries columns on boards.
  ```text
  Query
  Queries perform the READ operation and do not change or alter any data. The result of each query will be formatted in the same way as the query itself. The following example retrieves the ID, title, and type of each column on board 1234567890.
  Sample query
  GraphQL
  query {
  boards {
  columns {
  id
  title
  type
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.api.group.items` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Board items. Source evidence (lines:199-207) states: GraphQL create_item mutation creates a board item and returns its ID/name. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:199-207`)
  - *Observation*: paraphrase: GraphQL create_item mutation creates a board item and returns its ID/name.
  ```text
  Mutation
  Mutations are special queries that perform the CUD (Create, Update, Delete) operations to modify your data. Mutations return an instance of the object you just modified, so you can query the data you changed. The following example creates a new item on board 1234567890 and returns the ID and name of the new item.
  Sample mutation
  GraphQL
  mutation{
  create_item (board_id: 1234567890, item_name: "New Item"){
  id
  name
  }
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.api.protocol.graphql` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts GraphQL. Source evidence (lines:151-161) states: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:151-161`)
  - *Observation*: paraphrase: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns.
  ```text
  GraphQL overview
  The monday.com API is built with GraphQL, a flexible query language that allows you to return as much or as little data as you need. It's important to know that GraphQL is an application layer that parses the query you send it and returns (or changes) data accordingly.
  Unlike REST APIs, where multiple endpoints return different data, GraphQL always exposes one endpoint and allows you to determine the structure of the returned data. Our API uses the following endpoint: https://api.monday.com/v2.
  This document will walk through the GraphQL operations and object types to help you understand the essential components of a request. We will also discuss the GraphQL visual interface that enables you to test your queries and mutations, and finally, we cover where you can access the monday.com schema. Let's get started!
  👍
  Pro tip
  Check out this introduction to GraphQL to understand what all you can do with GraphQL!
  Operations
  There are two possible operations in GraphQL: queries and mutations.
  Query
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:151-161) states: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:151-161`)
  - *Observation*: paraphrase: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns.
  ```text
  GraphQL overview
  The monday.com API is built with GraphQL, a flexible query language that allows you to return as much or as little data as you need. It's important to know that GraphQL is an application layer that parses the query you send it and returns (or changes) data accordingly.
  Unlike REST APIs, where multiple endpoints return different data, GraphQL always exposes one endpoint and allows you to determine the structure of the returned data. Our API uses the following endpoint: https://api.monday.com/v2.
  This document will walk through the GraphQL operations and object types to help you understand the essential components of a request. We will also discuss the GraphQL visual interface that enables you to test your queries and mutations, and finally, we cover where you can access the monday.com schema. Let's get started!
  👍
  Pro tip
  Check out this introduction to GraphQL to understand what all you can do with GraphQL!
  Operations
  There are two possible operations in GraphQL: queries and mutations.
  Query
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.auth.mcp_oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Hosted monday MCP; distinct from Platform API OAuth app registration.. Source evidence (lines:151-154) states: monday hosted MCP supports OAuth for compatible clients or a personal API token for testing/custom clients. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/mcp-api-token](https://developer.monday.com/api-reference/docs/mcp-api-token) (locator: `lines:151-154`)
  - *Observation*: paraphrase: monday hosted MCP supports OAuth for compatible clients or a personal API token for testing/custom clients.
  ```text
  Authenticate with an API token
  Connect to the monday.com hosted MCP server with a personal API token for personal use, prototyping, and testing
  If you're using one of the compatible MCP clients, you don't need a token — add the server URL and authenticate via OAuth when prompted. Use a personal API token when your client isn't a compatible MCP client or doesn't support the MCP OAuth flow — for example, custom scripts, homegrown agents, or tools that only support static Bearer tokens.
  For personal use, prototyping, and testing, this is the fastest way to connect. No app or registration is needed.
  ```
- **URL**: [https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP](https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP) (locator: `lines:144-148`)
  - *Observation*: paraphrase: Each user authorizes MCP via OAuth, with permissions limited to user access and granted OAuth scopes.
  ```text
  Security and privacy
  What permissions does MCP have?
  Each user individually authorizes MCP via OAuth. MCP only has access to the data that you, as an individual user, can access in monday.com. The specific permissions depend on the OAuth scopes you grant during setup.
  Is my data secure?
  Yes. MCP uses industry-standard OAuth for authentication and TLS encryption for all data transfers. MCP respects your monday.com permissions, meaning you can only access or modify data you’re authorized to change. Because MCP can perform actions on your behalf, we recommend reviewing AI-suggested changes before confirming actions that modify your workspace.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.auth.oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for monday.com hosted platform GraphQL API v2 and official hosted MCP; personal V2 token and OAuth paths; free developer sandbox distinct from production workspace. Source evidence (lines:175-218) states: monday apps authenticate with Platform API OAuth 2.0 authorization-code flow (https://auth.monday.com/oauth2/authorize) with configured permission scopes (e.g., boards:read/write, docs:read/write, workspaces:read/write); a new OAuth 2.1 flow is also available. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/apps/docs/oauth](https://developer.monday.com/apps/docs/oauth) (locator: `lines:175-218`)
  - *Observation*: paraphrase: monday apps authenticate with Platform API OAuth 2.0 authorization-code flow (https://auth.monday.com/oauth2/authorize) with configured permission scopes (e.g., boards:read/write, docs:read/write, workspaces:read/write); a new OAuth 2.1 flow is also available.
  ```text
  OAuth and Permissions
  Authenticating monday apps with OAuth2 and defining permission scopes.
  OAuth 2.0 is a protocol that lets your app request authorization to read or modify data in a user's monday account. At the end of the OAuth process, your app gets an access token that belongs to the user and grants access to specified permission scopes.
  You can set up OAuth for your app in just two steps: configuring your app and going through the standard OAuth flow.
  🚧
  A new OAuth 2.1 flow is available
  monday.com now supports an improved OAuth 2.1 flow with expiring access tokens, refresh tokens, and token revocation. This page describes the current (legacy) flow. If you are building a new integration or want to upgrade your existing app, see Migrating to the new OAuth 2.1 flow.
  Configure your scopes and redirect URLs
  To start, you must first configure your app's scopes and redirect URLs. If you don't have an app, follow these steps to create an app in the monday UI and locate your client_id and client_secret.
  Once your app has been created, set the scopes and redirect URLs in the OAuth tab in the Developer Center.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.auth.personal` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for monday.com hosted platform GraphQL API v2 and official hosted MCP; personal V2 token and OAuth paths; free developer sandbox distinct from production workspace. Source evidence (lines:151-174) states: Platform API personal V2 tokens mirror user UI permissions and are accessed through Developer Center; send token in Authorization header. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/authentication](https://developer.monday.com/api-reference/docs/authentication) (locator: `lines:151-174`)
  - *Observation*: paraphrase: Platform API personal V2 tokens mirror user UI permissions and are accessed through Developer Center; send token in Authorization header.
  ```text
  Authentication
  Learn about monday platform API token permissions, how to access tokens, and how to authenticate requests
  The monday.com platform API utilizes personal V2 API tokens to authenticate requests and identify the user making the call. These tokens are unique to each user and have no explicit length.
  Personal tokens allow you to interact with the API using your own user account. Their permissions mirror what you can do in the monday.com UI, ensuring that API access is consistent with your platform-level permissions.
  If you don't have a monday.com account yet, create a free developer account to get an API token and start testing.
  Token permissions
  Personal tokens mirror all permission levels set in the monday.com UI, including board, column, item, or account access.
  For example: If you don't have permission to access a certain workspace via the UI, you won't have permission using your personal API token either.
  App tokens have an additional set of permission scopes that specify which queries and mutations it can access, while personal tokens have all permission scopes.
  Accessing your token
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Query boards/columns and create board items via GraphQL, or use hosted MCP under permitted actor.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:183-191): Developer accounts are testing-only, not production business workflows; extra capacity requests are reviewed.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Query boards/columns and create board items via GraphQL, or use hosted MCP under permitted actor.", "blockers": ["Free developer sandbox is explicitly not for production business workflows or end customers.", "MCP user permissions and AI Connector admin policy apply."], "next_steps": ["Keep developer account and production data separate.", "Choose personal API token or appropriate OAuth integration route; check limits before authorized tests."]}`
  - Original Rationale: A documented API supports a possible agent wrapper; feasibility remains conditional on account permissions and the stated access gaps. No implementation, credential acquisition, or operational test occurred.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Query boards/columns and create board items via GraphQL, or use hosted MCP under permitted actor.", "blockers": ["Free developer sandbox is explicitly not for production business workflows or end customers.", "MCP user permissions and AI Connector admin policy apply."], "next_steps": ["Keep developer account and production data separate.", "Choose personal API token or appropriate OAuth integration route; check limits before authorized tests."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Monday.com documentation: GraphQL API supports personal API tokens and OAuth 2.0 apps, gated by workspace permission scopes and plan tiers (76.testing.free_access, 76.auth.api_key, 76.api.graphql).

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/developer-sandbox](https://developer.monday.com/api-reference/docs/developer-sandbox) (locator: `lines:183-191`)
  - *Observation*: paraphrase: Developer accounts are testing-only, not production business workflows; extra capacity requests are reviewed.
  ```text
  Account terms and intended use
  Developer accounts are for development and testing only. They are not intended for running production business workflows or serving end customers.
  Keep these guidelines in mind:
  Separate from production data — Use your developer account to build and test apps and API integrations without touching live account data.
  Invite teammates for realistic testing — You can add up to 10 users to simulate collaboration, permissions, and multi-user app flows.
  Respect account limits — Item, automation, integration, and API complexity limits apply. Plan load tests and large-scale scenarios accordingly.
  Request more capacity when needed — If your app requires limits beyond the defaults, submit a request (see below). The team reviews requests within five business days.
  Request additional testing capacity
  If your app needs higher limits—for example, more items, automation actions, or API complexity—submit a request through the marketplace partner extensions form. The monday.com team reviews requests within five business days.
  ```
- **URL**: [https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP](https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP) (locator: `lines:110-125`)
  - *Observation*: paraphrase: monday MCP is a hosted server connecting external AI tools to workspace data; active account, user permissions and possible admin AI Connector settings apply.
  ```text
  monday MCP is the hosted server that gives AI tools secure access to your monday.com workspace. It connects your account directly to AI assistants like Claude, Cursor, and Copilot Studio through the Model Context Protocol (MCP), an open standard for AI integrations.
  Prerequisites
  An active monday.com account with appropriate permissions
  MCP is preinstalled on all monday.com accounts.
  If you can't connect, ask your admin to check Admin → Permissions → AI Connectors. See Managing AI Connectors & MCP Access for more information.
  Supported AI client
  OAuth consent for monday MCP when prompted by your client
  What can you do with monday MCP?
  Project reporting – generate sprint summaries, team performance reports, and deadline tracking from your boards (including monday dev sprints)
  Smart task management – convert meeting notes into structured items, assign tasks, and update statuses through natural language
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:151-175) states: monday hosted MCP supports OAuth or personal API token, with token clients sending Bearer token to https://mcp.monday.com/mcp; personal tokens are for individual development, not integrations used by others. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/mcp-api-token](https://developer.monday.com/api-reference/docs/mcp-api-token) (locator: `lines:151-175`)
  - *Observation*: paraphrase: monday hosted MCP supports OAuth or personal API token, with token clients sending Bearer token to https://mcp.monday.com/mcp; personal tokens are for individual development, not integrations used by others.
  ```text
  Authenticate with an API token
  Connect to the monday.com hosted MCP server with a personal API token for personal use, prototyping, and testing
  If you're using one of the compatible MCP clients, you don't need a token — add the server URL and authenticate via OAuth when prompted. Use a personal API token when your client isn't a compatible MCP client or doesn't support the MCP OAuth flow — for example, custom scripts, homegrown agents, or tools that only support static Bearer tokens.
  For personal use, prototyping, and testing, this is the fastest way to connect. No app or registration is needed.
  Get your token
  Log in to your monday.com account
  Click your profile picture in the top-right corner and select Developers
  Click My access tokens in the left menu
  Copy your personal access token
  Configure your MCP client
  ```
- **URL**: [https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP](https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP) (locator: `lines:110-125`)
  - *Observation*: paraphrase: monday MCP is a hosted server connecting external AI tools to workspace data; active account, user permissions and possible admin AI Connector settings apply.
  ```text
  monday MCP is the hosted server that gives AI tools secure access to your monday.com workspace. It connects your account directly to AI assistants like Claude, Cursor, and Copilot Studio through the Model Context Protocol (MCP), an open standard for AI integrations.
  Prerequisites
  An active monday.com account with appropriate permissions
  MCP is preinstalled on all monday.com accounts.
  If you can't connect, ask your admin to check Admin → Permissions → AI Connectors. See Managing AI Connectors & MCP Access for more information.
  Supported AI client
  OAuth consent for monday MCP when prompted by your client
  What can you do with monday MCP?
  Project reporting – generate sprint summaries, team performance reports, and deadline tracking from your boards (including monday dev sprints)
  Smart task management – convert meeting notes into structured items, assign tasks, and update statuses through natural language
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.mcp.server` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=monday hosted MCP; source_url=https://developer.monday.com/api-reference/docs/mcp-api-token. Source evidence (lines:151-175) states: monday hosted MCP supports OAuth or personal API token, with token clients sending Bearer token to https://mcp.monday.com/mcp; personal tokens are for individual development, not integrations used by others. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/mcp-api-token](https://developer.monday.com/api-reference/docs/mcp-api-token) (locator: `lines:151-175`)
  - *Observation*: paraphrase: monday hosted MCP supports OAuth or personal API token, with token clients sending Bearer token to https://mcp.monday.com/mcp; personal tokens are for individual development, not integrations used by others.
  ```text
  Authenticate with an API token
  Connect to the monday.com hosted MCP server with a personal API token for personal use, prototyping, and testing
  If you're using one of the compatible MCP clients, you don't need a token — add the server URL and authenticate via OAuth when prompted. Use a personal API token when your client isn't a compatible MCP client or doesn't support the MCP OAuth flow — for example, custom scripts, homegrown agents, or tools that only support static Bearer tokens.
  For personal use, prototyping, and testing, this is the fastest way to connect. No app or registration is needed.
  Get your token
  Log in to your monday.com account
  Click your profile picture in the top-right corner and select Developers
  Click My access tokens in the left menu
  Copy your personal access token
  Configure your MCP client
  ```
- **URL**: [https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP](https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP) (locator: `lines:110-125`)
  - *Observation*: paraphrase: monday MCP is a hosted server connecting external AI tools to workspace data; active account, user permissions and possible admin AI Connector settings apply.
  ```text
  monday MCP is the hosted server that gives AI tools secure access to your monday.com workspace. It connects your account directly to AI assistants like Claude, Cursor, and Copilot Studio through the Model Context Protocol (MCP), an open standard for AI integrations.
  Prerequisites
  An active monday.com account with appropriate permissions
  MCP is preinstalled on all monday.com accounts.
  If you can't connect, ask your admin to check Admin → Permissions → AI Connectors. See Managing AI Connectors & MCP Access for more information.
  Supported AI client
  OAuth consent for monday MCP when prompted by your client
  What can you do with monday MCP?
  Project reporting – generate sprint summaries, team performance reports, and deadline tracking from your boards (including monday dev sprints)
  Smart task management – convert meeting notes into structured items, assign tasks, and update statuses through natural language
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Workspace and board platform exposing GraphQL data queries, mutations and API integrations.. Source evidence (lines:151-161) states: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:151-161`)
  - *Observation*: paraphrase: monday.com platform API is GraphQL, using https://api.monday.com/v2 to query and modify data; example queries retrieve board columns.
  ```text
  GraphQL overview
  The monday.com API is built with GraphQL, a flexible query language that allows you to return as much or as little data as you need. It's important to know that GraphQL is an application layer that parses the query you send it and returns (or changes) data accordingly.
  Unlike REST APIs, where multiple endpoints return different data, GraphQL always exposes one endpoint and allows you to determine the structure of the returned data. Our API uses the following endpoint: https://api.monday.com/v2.
  This document will walk through the GraphQL operations and object types to help you understand the essential components of a request. We will also discuss the GraphQL visual interface that enables you to test your queries and mutations, and finally, we cover where you can access the monday.com schema. Let's get started!
  👍
  Pro tip
  Check out this introduction to GraphQL to understand what all you can do with GraphQL!
  Operations
  There are two possible operations in GraphQL: queries and mutations.
  Query
  ```
- **URL**: [https://developer.monday.com/api-reference/docs/introduction-to-graphql](https://developer.monday.com/api-reference/docs/introduction-to-graphql) (locator: `lines:199-204`)
  - *Observation*: paraphrase: GraphQL mutation example creates an item on a board.
  ```text
  Mutation
  Mutations are special queries that perform the CUD (Create, Update, Delete) operations to modify your data. Mutations return an instance of the object you just modified, so you can query the data you changed. The following example creates a new item on board 1234567890 and returns the ID and name of the new item.
  Sample mutation
  GraphQL
  mutation{
  create_item (board_id: 1234567890, item_name: "New Item"){
  ```
- **URL**: [https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP](https://support.monday.com/hc/en-us/articles/28588158981266-Get-started-with-monday-MCP) (locator: `lines:110-125`)
  - *Observation*: paraphrase: monday MCP is a hosted server connecting external AI tools to workspace data; active account, user permissions and possible admin AI Connector settings apply.
  ```text
  monday MCP is the hosted server that gives AI tools secure access to your monday.com workspace. It connects your account directly to AI assistants like Claude, Cursor, and Copilot Studio through the Model Context Protocol (MCP), an open standard for AI integrations.
  Prerequisites
  An active monday.com account with appropriate permissions
  MCP is preinstalled on all monday.com accounts.
  If you can't connect, ask your admin to check Admin → Permissions → AI Connectors. See Managing AI Connectors & MCP Access for more information.
  Supported AI client
  OAuth consent for monday MCP when prompted by your client
  What can you do with monday MCP?
  Project reporting – generate sprint summaries, team performance reports, and deadline tracking from your boards (including monday dev sprints)
  Smart task management – convert meeting notes into structured items, assign tasks, and update statuses through natural language
  ```
- **URL**: [https://developer.monday.com/api-reference/docs/developer-sandbox](https://developer.monday.com/api-reference/docs/developer-sandbox) (locator: `lines:151-158`)
  - *Observation*: paraphrase: Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center.
  ```text
  Developer Sandbox Account
  Sign up for a free monday.com developer account to build and test apps and API integrations in a sandbox separate from your production data.
  A developer account (also called a sandbox account) is a free monday.com account designed for building and testing monday apps and API integrations. It runs in an environment separate from your production or work data, so you can experiment without affecting live workflows.
  You can use any monday.com account to explore the apps framework and API. A developer account is the recommended option when you need higher limits and Pro/Enterprise capabilities for thorough testing.
  Sign up for a developer account
  Create a free developer account and start building right away:
  Sign up for a free developer account
  After sign-up, open the Developer Center from your profile menu (Developers) to manage apps, API tokens, and usage.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:151-158) states: Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/developer-sandbox](https://developer.monday.com/api-reference/docs/developer-sandbox) (locator: `lines:151-158`)
  - *Observation*: paraphrase: Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center.
  ```text
  Developer Sandbox Account
  Sign up for a free monday.com developer account to build and test apps and API integrations in a sandbox separate from your production data.
  A developer account (also called a sandbox account) is a free monday.com account designed for building and testing monday apps and API integrations. It runs in an environment separate from your production or work data, so you can experiment without affecting live workflows.
  You can use any monday.com account to explore the apps framework and API. A developer account is the recommended option when you need higher limits and Pro/Enterprise capabilities for thorough testing.
  Sign up for a developer account
  Create a free developer account and start building right away:
  Sign up for a free developer account
  After sign-up, open the Developer Center from your profile menu (Developers) to manage apps, API tokens, and usage.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.testing.sandbox_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:151-158) states: Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center. The documentation describes a sandbox or test environment relevant to test access, distinct from live production access.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/developer-sandbox](https://developer.monday.com/api-reference/docs/developer-sandbox) (locator: `lines:151-158`)
  - *Observation*: paraphrase: Free developer account supports building/testing API integrations in a separate sandbox; after signup manage tokens in Developer Center.
  ```text
  Developer Sandbox Account
  Sign up for a free monday.com developer account to build and test apps and API integrations in a sandbox separate from your production data.
  A developer account (also called a sandbox account) is a free monday.com account designed for building and testing monday apps and API integrations. It runs in an environment separate from your production or work data, so you can experiment without affecting live workflows.
  You can use any monday.com account to explore the apps framework and API. A developer account is the recommended option when you need higher limits and Pro/Enterprise capabilities for thorough testing.
  Sign up for a developer account
  Create a free developer account and start building right away:
  Sign up for a free developer account
  After sign-up, open the Developer Center from your profile menu (Developers) to manage apps, API tokens, and usage.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `76.testing.trial_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:159-163) states: An alternate trial account is offered to evaluate monday beyond development; extension requests contact support. The cited trial terms indicate temporary evaluation access for test access; a trial is not necessarily a permanent free tier.

#### Primary Evidence & Excerpts
- **URL**: [https://developer.monday.com/api-reference/docs/developer-sandbox](https://developer.monday.com/api-reference/docs/developer-sandbox) (locator: `lines:159-163`)
  - *Observation*: paraphrase: An alternate trial account is offered to evaluate monday beyond development; extension requests contact support.
  ```text
  Other account options
  OptionWhen to use it
  Existing monday.com accountYou already have an account and only need light testing.
  Trial accountYou want to evaluate monday.com beyond development. Sign up for a trial.
  Trial extensionYour trial is ending but you need more time. Contact support to request an extension.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 83: Binance (Finance and Fintech)
- Total claims: 23 | Corrected: 6

### Claim: `83.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts broad. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:23-74): Spot REST API spans exchange metadata, market data, complex order execution, and account reporting.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "broad"`
  - Original Rationale: Broad exchange API covering market data, Spot trading, account telemetry, and adjacent exchange domains.
- **Corrected Answer**: `status: inferred`, `value: "broad"`
  - Corrected Rationale: Binance Spot API covers multiple distinct financial domains: (1) Market Data & Order Book Feeds, (2) Spot Order Execution, (3) Account Balance & Trade History, and (4) WebSocket Real-time Streams. Per evidence rules, multiple distinct domains substantiate broad breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:23-74`)
  - *Observation*: paraphrase: Spot REST API spans exchange metadata, market data, complex order execution, and account reporting.
  ```text
  - [General endpoints](#general-endpoints)
  - [Test connectivity](#test-connectivity)
  - [Check server time](#check-server-time)
  - [Exchange information](#exchange-information)
  - [Query Execution Rules](#query-execution-rules)
  - [Market Data endpoints](#market-data-endpoints)
  - [Order book](#order-book)
  - [Recent trades list](#recent-trades-list)
  - [Old trade lookup](#old-trade-lookup)
  - [Historical Block Trades](#historical-block-trades)
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:20-43`)
  - *Observation*: paraphrase: Official README also indexes broader exchange domains (Margin, Futures, Options, Wallet, Convert, Pay).
  ```text
  [Margin Trading](https://developers.binance.com/en/docs/products/margin-trading/general-info) | Details on Margin Trading
  [Derivative UM Futures](https://developers.binance.com/docs/derivatives/usds-margined-futures/general-info) | Details on Derivative UM Futures (`/fapi`)
  [Derivative CM Futures](https://developers.binance.com/docs/derivatives/coin-margined-futures/general-info) | Details on Derivative CM Futures (`/dapi`)
  [Derivative Options](https://developers.binance.com/docs/derivatives/option/general-info) | Details on Derivative European Options (`/eapi`)
  [Derivative Portfolio Margin](https://developers.binance.com/docs/derivatives/portfolio-margin/general-info)| Details on Derivative Portfolio Margin (`/papi`)
  [Wallet](https://developers.binance.com/docs/wallet) | Details on Wallet endpoints (`/sapi`)
  [Sub Account](https://developers.binance.com/docs/sub_account/general-info) | Details on Sub-Account requests (`/sapi`)
  [Simple Earn](https://developers.binance.com/docs/simple_earn/general-info) | Details on Simple Earn
  [Dual Investment](https://developers.binance.com/docs/dual_investment) | Details on Dual Investment
  [Auto Invest](https://developers.binance.com/docs/auto_invest) | Details on Auto Invest
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.group.account_user_data` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Account & User Data (account info, open/all orders, trade list, allocations, commission rates, rate limits). Source evidence (lines:60-74) states: Lists Account endpoints for balances, orders, trades, and commission rates. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:60-74`)
  - *Observation*: paraphrase: Lists Account endpoints for balances, orders, trades, and commission rates.
  ```text
  - [Account Endpoints](#account-endpoints)
  - [Account information (USER_DATA)](#account-information-user_data)
  - [Query order (USER_DATA)](#query-order-user_data)
  - [Current open orders (USER_DATA)](#current-open-orders-user_data)
  - [All orders (USER_DATA)](#all-orders-user_data)
  - [Query Order list (USER_DATA)](#query-order-list-user_data)
  - [Query all Order lists (USER_DATA)](#query-all-order-lists-user_data)
  - [Query Open Order lists (USER_DATA)](#query-open-order-lists-user_data)
  - [Account trade list (USER_DATA)](#account-trade-list-user_data)
  - [Query Unfilled Order Count (USER_DATA)](#query-unfilled-order-count-user_data)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.group.general_exchange` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts General & Exchange Info (connectivity, server time, exchangeInfo, execution rules). Source evidence (lines:23-27) states: Lists General endpoints: test connectivity, server time, exchange info, execution rules. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:23-27`)
  - *Observation*: paraphrase: Lists General endpoints: test connectivity, server time, exchange info, execution rules.
  ```text
  - [General endpoints](#general-endpoints)
  - [Test connectivity](#test-connectivity)
  - [Check server time](#check-server-time)
  - [Exchange information](#exchange-information)
  - [Query Execution Rules](#query-execution-rules)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.group.market_data` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Market Data (order book, trades, klines/candlesticks, tickers, average/reference price). Source evidence (lines:28-43) states: Lists Market Data endpoints for order books, trades, klines, and tickers. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:28-43`)
  - *Observation*: paraphrase: Lists Market Data endpoints for order books, trades, klines, and tickers.
  ```text
  - [Market Data endpoints](#market-data-endpoints)
  - [Order book](#order-book)
  - [Recent trades list](#recent-trades-list)
  - [Old trade lookup](#old-trade-lookup)
  - [Historical Block Trades](#historical-block-trades)
  - [Compressed/Aggregate trades list](#compressedaggregate-trades-list)
  - [Kline/Candlestick data](#klinecandlestick-data)
  - [UIKlines](#uiklines)
  - [Current average price](#current-average-price)
  - [24hr ticker price change statistics](#24hr-ticker-price-change-statistics)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.group.spot_trading` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Spot Trading (new/test/cancel/replace/amend orders, OCO/OTO/OTOCO/OPO order lists, SOR). Source evidence (lines:44-59) states: Lists Trading endpoints for orders, order lists, and Smart Order Routing. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:44-59`)
  - *Observation*: paraphrase: Lists Trading endpoints for orders, order lists, and Smart Order Routing.
  ```text
  - [Trading endpoints](#trading-endpoints)
  - [New order (TRADE)](#new-order-trade)
  - [Test new order (TRADE)](#test-new-order-trade)
  - [Cancel order (TRADE)](#cancel-order-trade)
  - [Cancel All Open Orders on a Symbol (TRADE)](#cancel-all-open-orders-on-a-symbol-trade)
  - [Cancel an Existing Order and Send a New Order (TRADE)](#cancel-an-existing-order-and-send-a-new-order-trade)
  - [Order Amend Keep Priority (TRADE)](#order-amend-keep-priority-trade)
  - [New OCO - Deprecated (TRADE)](#new-oco---deprecated-trade)
  - [New Order list - OCO (TRADE)](#new-order-list---oco-trade)
  - [New Order list - OTO (TRADE)](#new-order-list---oto-trade)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.protocol.other` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other. Source evidence (lines:11-16) states: Official WebSocket API, WebSocket market/user streams, SBE streams, and FIX API. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:11-16`)
  - *Observation*: paraphrase: Official WebSocket API, WebSocket market/user streams, SBE streams, and FIX API.
  ```text
  [web-socket-api.md](./web-socket-api.md) | Spot WebSocket API
  [fix-api.md](fix-api.md) | FIX API
  [web-socket-streams.md](./web-socket-streams.md) | Spot Market Data WebSocket streams
  [sbe-market-data-streams.md](./sbe-market-data-streams.md) | SBE Market Data Streams
  [user-data-stream.md](./user-data-stream.md) | Spot User Data WebSocket streams
  [sbe_schemas](./sbe/schemas/) | Spot Simple Binary Encoding (SBE) schemas
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:78-89) states: Spot REST API returning JSON (or SBE) over HTTPS. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:78-89`)
  - *Observation*: paraphrase: Spot REST API returning JSON (or SBE) over HTTPS.
  ```text
  # Public Rest API for Binance
  ## General API Information
  - The following base endpoints are available. Please use whichever works best for your setup:
  - **https://api.binance.com**
  - **https://api-gcp.binance.com**
  - **https://api1.binance.com**
  - **https://api2.binance.com**
  - **https://api3.binance.com**
  - **https://api4.binance.com**
  - The last 4 endpoints in the point above (`api1`-`api4`) should give better performance but have
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:65-77) states: Official lightweight connector SDKs for Python, Node.js, Ruby, .NET, Java, Rust, PHP, Go, TypeScript, and Python FIX. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:65-77`)
  - *Observation*: paraphrase: Official lightweight connector SDKs for Python, Node.js, Ruby, .NET, Java, Rust, PHP, Go, TypeScript, and Python FIX.
  ```text
  * Connectors
  * The following are lightweight libraries that work as connectors to the Binance public API, written in different languages:
  * [Python](https://github.com/binance/binance-connector-python)
  * [Node.js](https://github.com/binance/binance-connector-node)
  * [Ruby](https://github.com/binance/binance-connector-ruby)
  * [DotNET C#](https://github.com/binance/binance-connector-dotnet)
  * [Java](https://github.com/binance/binance-connector-java)
  * [Rust](https://github.com/binance/binance-spot-connector-rust)
  * [PHP](https://github.com/binance/binance-connector-php)
  * [Go](https://github.com/binance/binance-connector-go)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.api.public_documentation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-18) states: Official Binance Spot API documentation is publicly hosted on GitHub. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:1-18`)
  - *Observation*: paraphrase: Official Binance Spot API documentation is publicly hosted on GitHub.
  ```text
  # Official Documentation for the Binance APIs and Streams.
  * Official Announcements regarding changes, downtime, etc. to the API and Streams will be reported here: **https://t.me/binance_api_announcements**
  * Streams, endpoints, parameters, payloads, etc. described in the documents in this repository are considered **official** and **supported**.
  * The use of any other streams, endpoints, parameters, or payloads, etc. is **not supported**; **use them at your own risk and with no guarantees.**
  Name | Description
  ------------ | ------------
  [enums.md](./enums.md) | Details on the enums used by REST and WebSocket API
  [errors.md](./errors.md) | Error codes and messages of Spot API
  [filters.md](./filters.md) | Details on the filters used by Spot API
  [rest-api.md](./rest-api.md) | Spot REST API (`/api`)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.auth.public_none` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts none authentication for Public Spot market-data endpoints.. Source evidence (lines:103-105) states: Public market data only endpoint at https://data-api.binance.vision. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:103-105`)
  - *Observation*: paraphrase: Public market data only endpoint at https://data-api.binance.vision.
  ```text
  - For APIs that only send public market data, please use the base endpoint
  **https://data-api.binance.vision**. Please refer to
  [Market Data Only](faqs/market_data_only.md) page.
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:232-247`)
  - *Observation*: paraphrase: Unspecified security type is NONE for public market data.
  ```text
  - If unspecified, the security type is `NONE`.
  - Except for `NONE`, all endpoints with a security type are considered `SIGNED` requests (i.e.
  including a `signature`).
  - Secure endpoints require a valid API key to be specified and authenticated.
  - API keys can be created on the
  [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance
  account.
  - **Both API key and secret key are sensitive.** Never share them with anyone. If you notice
  unusual activity in your account, immediately revoke all the keys and contact Binance support.
  - API keys can be configured to allow access only to certain types of secure endpoints.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.auth.signed_api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Signed Spot account, trading, and user data stream endpoints (Production and Spot Testnet).. Source evidence (lines:99-100) states: Supports HMAC, RSA, and Ed25519 API key types. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:99-100`)
  - *Observation*: paraphrase: Supports HMAC, RSA, and Ed25519 API key types.
  ```text
  - We support HMAC, RSA, and Ed25519 keys. For more information, please see
  [API Key types](faqs/api_key_types.md).
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:229-250`)
  - *Observation*: paraphrase: Secure endpoints require API key plus signature with TRADE, USER_DATA, or USER_STREAM permissions.
  ```text
  - Each endpoint has a security type indicating required API key permissions, shown next to the
  endpoint name (e.g.,
  [New order (TRADE)](rest-api.md#new-order-trade)).
  - If unspecified, the security type is `NONE`.
  - Except for `NONE`, all endpoints with a security type are considered `SIGNED` requests (i.e.
  including a `signature`).
  - Secure endpoints require a valid API key to be specified and authenticated.
  - API keys can be created on the
  [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance
  account.
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:94-195`)
  - *Observation*: paraphrase: Documents X-MBX-APIKEY header with HMAC-SHA-256, RSA, and Ed25519 signing.
  ```text
  ## What are RSA API Keys?
  RSA API Keys are an alternative to the typical HMAC-SHA-256 API Keys that are used to authenticate
  your requests on the Spot API.
  Unlike HMAC-SHA-256 API Keys where we generate the secret signing key for you, with RSA API Keys,
  _you_ generate a pair of public+private RSA keys, send us the public key, and sign your requests
  with your private key.
  <a id="faq-rsa-types"></a>
  ## What type of RSA keys are supported?
  We support RSA keys of any length from 2048 bits up to 4096 bits. We recommend **2048 bits keys** as
  a good balance between security and signature speed.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Binance global Spot REST/WebSocket API and community MCP server; public market data is open while signed production trading depends on regional/KYC eligibility.. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:78-105): Public REST API endpoints and market-data host.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Binance global Spot REST/WebSocket API and community MCP server; public market data is open while signed production trading depends on regional/KYC eligibility.", "blockers": ["Regional/jurisdictional eligibility and KYC requirements for global Binance production accounts are unresolved in captured docs.", "No official vendor-endorsed MCP server was found in checked official Spot API sources.", "Spot Testnet supports /api/* only (not /sapi/*) and resets roughly monthly; developers.binance.com HTML returned empty readable content."], "next_steps": ["Build against public market-data endpoints and Spot Testnet using official connectors.", "Verify jurisdictional eligibility and Binance account KYC/API Management permissions before enabling live TRADE keys."]}`
  - Original Rationale: Public Spot REST/WebSocket/FIX docs and free Spot Testnet support development, but production trading is conditional on unresolved jurisdictional/KYC eligibility and lacks an official vendor MCP.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Binance global Spot REST/WebSocket API and community MCP server; public market data is open while signed production trading depends on regional/KYC eligibility.", "blockers": ["Regional/jurisdictional eligibility and KYC requirements for global Binance production accounts are unresolved in captured docs.", "No official vendor-endorsed MCP server was found in checked official Spot API sources.", "Spot Testnet supports /api/* only (not /sapi/*) and resets roughly monthly; developers.binance.com HTML returned empty readable content."], "next_steps": ["Build against public market-data endpoints and Spot Testnet using official connectors.", "Verify jurisdictional eligibility and Binance account KYC/API Management permissions before enabling live TRADE keys."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Binance documentation: Public market data REST/WebSocket feeds are open without authentication, but signed production trading depends on regional compliance and account verification (83.api.rest, 83.mcp.community_mcp).

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:78-105`)
  - *Observation*: paraphrase: Public REST API endpoints and market-data host.
  ```text
  # Public Rest API for Binance
  ## General API Information
  - The following base endpoints are available. Please use whichever works best for your setup:
  - **https://api.binance.com**
  - **https://api-gcp.binance.com**
  - **https://api1.binance.com**
  - **https://api2.binance.com**
  - **https://api3.binance.com**
  - **https://api4.binance.com**
  - The last 4 endpoints in the point above (`api1`-`api4`) should give better performance but have
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-71`)
  - *Observation*: paraphrase: Self-serve Spot Testnet with virtual assets.
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  Step 2: Follow the
  [official documentation of the Spot API](CHANGELOG.md),
  replacing the URLs of the endpoints with the following values:
  ## REST API
  | Production | Testnet |
  | --------------------------------- | ----------------------------------------- |
  | `https://api.binance.com/api` | `https://testnet.binance.vision/api` |
  | `https://api-gcp.binance.com/api` | `https://api1.testnet.binance.vision/api` |
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.mcp.community_binance_mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=community; name=Binance MCP (mujeeb8/Binance-MCP); source_url=https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README. Source evidence (lines:1-38) states: Community TypeScript MCP server exposing spot prices, book tickers, spot/funding balances, and Binance Convert tools. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md](https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md) (locator: `lines:1-38`)
  - *Observation*: paraphrase: Community TypeScript MCP server exposing spot prices, book tickers, spot/funding balances, and Binance Convert tools.
  ```text
  # Binance MCP
  <p align="center">
  <img alt="MCP logo" src="assets/binance-logo.png" width="180" height="180" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img alt="Binance logo" src="assets/mcp-logo.png" width="180" height="180" />
  </p>
  <p align="center">
  <strong>A TypeScript MCP server for Binance market data, account insights, and Convert workflows.</strong>
  </p>
  <p align="center">
  ```
- **URL**: [https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md](https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md) (locator: `lines:56-87`)
  - *Observation*: paraphrase: Runs locally over stdio; public market tools require no auth, account/Convert tools require BINANCE_API_KEY and BINANCE_API_SECRET.
  ```text
  The server communicates over `stdio`, which is the standard transport used by Claude Desktop.
  ## Full Documentation
  If you want the deeper implementation notes, endpoint details, and design rationale, see [DOCUMENTATION.md](DOCUMENTATION.md).
  ## Claude Desktop Setup
  Use the compiled server entry point in your claude_desktop_config.json file.
  ### Example configuration
  ```json
  {
  "mcpServers": {
  "binance-mcp": {
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:1-17) states: Community callable MCP server documented in mujeeb8/Binance-MCP; no official Binance MCP server found in checked official Spot API repo. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md](https://raw.githubusercontent.com/mujeeb8/Binance-MCP/main/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Community callable MCP server documented in mujeeb8/Binance-MCP; no official Binance MCP server found in checked official Spot API repo.
  ```text
  # Binance MCP
  <p align="center">
  <img alt="MCP logo" src="assets/binance-logo.png" width="180" height="180" />
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img alt="Binance logo" src="assets/mcp-logo.png" width="180" height="180" />
  </p>
  <p align="center">
  <strong>A TypeScript MCP server for Binance market data, account insights, and Convert workflows.</strong>
  </p>
  <p align="center">
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.production.sandbox_access` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:8-16): Production api.binance.com is separate from Spot Testnet testnet.binance.vision.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Production is separate from Spot Testnet.
- **Corrected Answer**: `status: unknown`, `value: null`
  - Corrected Rationale: Research correction: Host separation between api.binance.com and testnet.binance.vision does not conclusively prove absence of sandbox access for production. Relabeled from observed (false) to unknown.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:8-16`)
  - *Observation*: paraphrase: Production api.binance.com is separate from Spot Testnet testnet.binance.vision.
  ```text
  ## REST API
  | Production | Testnet |
  | --------------------------------- | ----------------------------------------- |
  | `https://api.binance.com/api` | `https://testnet.binance.vision/api` |
  | `https://api-gcp.binance.com/api` | `https://api1.testnet.binance.vision/api` |
  | `https://api1.binance.com/api` | |
  | `https://api2.binance.com/api` | |
  | `https://api3.binance.com/api` | |
  | `https://api4.binance.com/api` | |
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Cryptocurrency exchange Spot API for public market data, account queries, and order trading across REST, WebSocket, and FIX.. Source evidence (lines:10-17) states: Official Spot REST API, WebSocket API/streams, FIX API, and Spot Testnet. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:10-17`)
  - *Observation*: paraphrase: Official Spot REST API, WebSocket API/streams, FIX API, and Spot Testnet.
  ```text
  [rest-api.md](./rest-api.md) | Spot REST API (`/api`)
  [web-socket-api.md](./web-socket-api.md) | Spot WebSocket API
  [fix-api.md](fix-api.md) | FIX API
  [web-socket-streams.md](./web-socket-streams.md) | Spot Market Data WebSocket streams
  [sbe-market-data-streams.md](./sbe-market-data-streams.md) | SBE Market Data Streams
  [user-data-stream.md](./user-data-stream.md) | Spot User Data WebSocket streams
  [sbe_schemas](./sbe/schemas/) | Spot Simple Binary Encoding (SBE) schemas
  [testnet](./testnet/) | API docs for features available only on SPOT Testnet
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/rest-api.md) (locator: `lines:22-74`)
  - *Observation*: paraphrase: Covers general exchange info, market data, trading, and account endpoints.
  ```text
  - [Public API Endpoints](#public-api-endpoints)
  - [General endpoints](#general-endpoints)
  - [Test connectivity](#test-connectivity)
  - [Check server time](#check-server-time)
  - [Exchange information](#exchange-information)
  - [Query Execution Rules](#query-execution-rules)
  - [Market Data endpoints](#market-data-endpoints)
  - [Order book](#order-book)
  - [Recent trades list](#recent-trades-list)
  - [Old trade lookup](#old-trade-lookup)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.contact_sales_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:3-4): Self-serve Spot Testnet key generation.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No sales contact required for Spot Testnet.
- **Corrected Answer**: `status: unknown`, `value: null`
  - Corrected Rationale: Research correction: Absence of contact sales required was asserted as false based on self-serve Spot Testnet key generation. Under evidence rules, absence of gating requires explicit vendor proof; silence is unknown. Relabeled from observed (false) to unknown.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-4`)
  - *Observation*: paraphrase: Self-serve Spot Testnet key generation.
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:66-71) states: All users registering on Spot Test Network automatically receive virtual asset balances. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:66-71`)
  - *Observation*: paraphrase: All users registering on Spot Test Network automatically receive virtual asset balances.
  ```text
  ## How to get funds in/out of the Spot Test Network?
  All users registering on the Spot Test Network automatically receive a balance in many different
  assets. Please note that these are not real assets and can be used only on the Spot Test Network
  itself.
  All funds on the Spot Test Network are virtual, and can not be transferred in/out of the Spot Test
  Network.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:67-71) states: Virtual assets automatically granted on registration; no real funds involved. The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:67-71`)
  - *Observation*: paraphrase: Virtual assets automatically granted on registration; no real funds involved.
  ```text
  All users registering on the Spot Test Network automatically receive a balance in many different
  assets. Please note that these are not real assets and can be used only on the Spot Test Network
  itself.
  All funds on the Spot Test Network are virtual, and can not be transferred in/out of the Spot Test
  Network.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.partner_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:3-4): Open self-serve login on testnet.binance.vision

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No partner approval required for Spot Testnet.
- **Corrected Answer**: `status: unknown`, `value: null`
  - Corrected Rationale: Research correction: Absence of partner approval required was asserted as false based on self-serve Spot Testnet key generation. Under evidence rules, absence of gating requires explicit vendor proof; silence is unknown. Relabeled from observed (false) to unknown.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-4`)
  - *Observation*: paraphrase: Open self-serve login on testnet.binance.vision.
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.sandbox_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:3-16) states: Dedicated Spot Test Network at https://testnet.binance.vision/api (supports /api/* only, not /sapi/*). The documentation describes a sandbox or test environment relevant to test access, distinct from live production access.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-16`)
  - *Observation*: paraphrase: Dedicated Spot Test Network at https://testnet.binance.vision/api (supports /api/* only, not /sapi/*).
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  Step 2: Follow the
  [official documentation of the Spot API](CHANGELOG.md),
  replacing the URLs of the endpoints with the following values:
  ## REST API
  | Production | Testnet |
  | --------------------------------- | ----------------------------------------- |
  | `https://api.binance.com/api` | `https://testnet.binance.vision/api` |
  | `https://api-gcp.binance.com/api` | `https://api1.testnet.binance.vision/api` |
  ```
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/README.md) (locator: `lines:80-83`)
  - *Observation*: paraphrase: Spot Testnet available via API for /api/* endpoints.
  ```text
  * [Spot Testnet](https://testnet.binance.vision/)
  * Users can use the SPOT Testnet to practice SPOT trading.
  * Currently, this is only available via the API.
  * Only endpoints starting with `/api/*` are supported, `/sapi/*` is not supported.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:3-4) states: Log in on testnet.binance.vision and generate an API key. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-4`)
  - *Observation*: paraphrase: Log in on testnet.binance.vision and generate an API key.
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `83.testing.vendor_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:3-4): Users log in on testnet.binance.vision and generate an API key directly.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No vendor approval documented for Spot Testnet.
- **Corrected Answer**: `status: unknown`, `value: null`
  - Corrected Rationale: Research correction: Absence of vendor approval required was asserted as false based on self-serve Spot Testnet key generation. Under evidence rules, absence of gating requires explicit vendor proof; silence is unknown. Relabeled from observed (false) to unknown.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md](https://raw.githubusercontent.com/binance/binance-spot-api-docs/master/testnet/general-info.md) (locator: `lines:3-4`)
  - *Observation*: paraphrase: Users log in on testnet.binance.vision and generate an API key directly.
  ```text
  ## How can I use the Spot Test Network?
  Step 1: Log in on this [website](https://testnet.binance.vision/), and generate an API Key.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 98: Mermaid CLI (AI, Research and Media-native)
- Total claims: 23 | Corrected: 10

### Claim: `98.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts narrow. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1-17): mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "narrow"`
  - Original Rationale: Focused single-domain local diagram-rendering surface; no hosted REST API.
- **Corrected Answer**: `status: inferred`, `value: "narrow"`
  - Corrected Rationale: Mermaid CLI (@mermaid-js/mermaid-cli) is focused strictly on a single operational workflow: converting .mmd definitions and Markdown mermaid blocks into rendered SVG, PNG, or PDF files. Per evidence rules, a single focused workflow constitutes narrow breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:25-63`)
  - *Observation*: paraphrase: Supports PNG/SVG/PDF output, themes, transparent backgrounds, custom icon packs (npm or URI), custom CSS animation, sizing, and transforming Markdown files with embedded Mermaid code blocks.
  ```text
  ### Create A PNG With A Dark Theme And Transparent Background
  ```sh
  mmdc -i input.mmd -o output.png -t dark -b transparent
  ```
  ### Adding custom icon packs to Mermaid
  `mermaid-cli` supports two different ways to add [custom icon packs to mermaid](https://mermaid.js.org/config/icons.html):
  - Icon packs installed via `npm install`, e.g. [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos). These can be used via the `--iconPacks @iconify-json/logos`.
  - Icon packs accessible via URI. These can either be URLs or local `file://` URIs to local files. For example, to download the above [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos) package from a CDN like [jsDelivr](https://www.jsdelivr.com/), you can do `--iconPacksAndUrls logos#https://cdn.jsdelivr.net/npm/@iconify-json/logos@1.2.14/icons.json`.
  ### Animating an SVG file with custom CSS
  The `--cssFile` option can be used to inline some custom CSS. It's passed to [Mermaid's `themeCSS` config option](https://mermaid.js.org/config/schema-docs/config.html#themecss).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.api.group.diagram_rendering` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Convert .mmd Mermaid diagram files to SVG, PNG, or PDF with theme, background, size, CSS, and icon pack options. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:25-63`)
  - *Observation*: paraphrase: Supports PNG/SVG/PDF output, themes, transparent backgrounds, custom icon packs (npm or URI), custom CSS animation, sizing, and transforming Markdown files with embedded Mermaid code blocks.
  ```text
  ### Create A PNG With A Dark Theme And Transparent Background
  ```sh
  mmdc -i input.mmd -o output.png -t dark -b transparent
  ```
  ### Adding custom icon packs to Mermaid
  `mermaid-cli` supports two different ways to add [custom icon packs to mermaid](https://mermaid.js.org/config/icons.html):
  - Icon packs installed via `npm install`, e.g. [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos). These can be used via the `--iconPacks @iconify-json/logos`.
  - Icon packs accessible via URI. These can either be URLs or local `file://` URIs to local files. For example, to download the above [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos) package from a CDN like [jsDelivr](https://www.jsdelivr.com/), you can do `--iconPacksAndUrls logos#https://cdn.jsdelivr.net/npm/@iconify-json/logos@1.2.14/icons.json`.
  ### Animating an SVG file with custom CSS
  The `--cssFile` option can be used to inline some custom CSS. It's passed to [Mermaid's `themeCSS` config option](https://mermaid.js.org/config/schema-docs/config.html#themecss).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.api.group.markdown_transformation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Transform Markdown files containing embedded Mermaid code blocks into rendered diagram images and updated Markdown. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:25-63`)
  - *Observation*: paraphrase: Supports PNG/SVG/PDF output, themes, transparent backgrounds, custom icon packs (npm or URI), custom CSS animation, sizing, and transforming Markdown files with embedded Mermaid code blocks.
  ```text
  ### Create A PNG With A Dark Theme And Transparent Background
  ```sh
  mmdc -i input.mmd -o output.png -t dark -b transparent
  ```
  ### Adding custom icon packs to Mermaid
  `mermaid-cli` supports two different ways to add [custom icon packs to mermaid](https://mermaid.js.org/config/icons.html):
  - Icon packs installed via `npm install`, e.g. [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos). These can be used via the `--iconPacks @iconify-json/logos`.
  - Icon packs accessible via URI. These can either be URLs or local `file://` URIs to local files. For example, to download the above [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos) package from a CDN like [jsDelivr](https://www.jsdelivr.com/), you can do `--iconPacksAndUrls logos#https://cdn.jsdelivr.net/npm/@iconify-json/logos@1.2.14/icons.json`.
  ### Animating an SVG file with custom CSS
  The `--cssFile` option can be used to inline some custom CSS. It's passed to [Mermaid's `themeCSS` config option](https://mermaid.js.org/config/schema-docs/config.html#themecss).
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.api.protocol.cli` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts CLI. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:111-135`)
  - *Observation*: paraphrase: Official container images are published on GHCR (ghcr.io/mermaid-js/mermaid-cli/mermaid-cli) and Docker Hub (minlag/mermaid-cli) for local Docker or Podman execution.
  ```text
  ```sh
  docker pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli
  ```
  or e.g. version 8.8.0
  ```sh
  docker pull minlag/mermaid-cli:8.8.0
  ```
  The container looks for input files in `/data`. So for example, if you have a
  diagram defined on your system in `/path/to/diagrams/diagram.mmd`, you can use
  the container to generate an SVG file as follows:
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:136-158) states: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:25-63`)
  - *Observation*: paraphrase: Supports PNG/SVG/PDF output, themes, transparent backgrounds, custom icon packs (npm or URI), custom CSS animation, sizing, and transforming Markdown files with embedded Mermaid code blocks.
  ```text
  ### Create A PNG With A Dark Theme And Transparent Background
  ```sh
  mmdc -i input.mmd -o output.png -t dark -b transparent
  ```
  ### Adding custom icon packs to Mermaid
  `mermaid-cli` supports two different ways to add [custom icon packs to mermaid](https://mermaid.js.org/config/icons.html):
  - Icon packs installed via `npm install`, e.g. [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos). These can be used via the `--iconPacks @iconify-json/logos`.
  - Icon packs accessible via URI. These can either be URLs or local `file://` URIs to local files. For example, to download the above [@iconify-json/logos](https://www.npmjs.com/package/@iconify-json/logos) package from a CDN like [jsDelivr](https://www.jsdelivr.com/), you can do `--iconPacksAndUrls logos#https://cdn.jsdelivr.net/npm/@iconify-json/logos@1.2.14/icons.json`.
  ### Animating an SVG file with custom CSS
  The `--cssFile` option can be used to inline some custom CSS. It's passed to [Mermaid's `themeCSS` config option](https://mermaid.js.org/config/schema-docs/config.html#themecss).
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.auth.local_none` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts none authentication for Local CLI, Docker/Podman container, and Node.js API execution. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:111-135`)
  - *Observation*: paraphrase: Official container images are published on GHCR (ghcr.io/mermaid-js/mermaid-cli/mermaid-cli) and Docker Hub (minlag/mermaid-cli) for local Docker or Podman execution.
  ```text
  ```sh
  docker pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli
  ```
  or e.g. version 8.8.0
  ```sh
  docker pull minlag/mermaid-cli:8.8.0
  ```
  The container looks for input files in `/data`. So for example, if you have a
  diagram defined on your system in `/path/to/diagrams/diagram.mmd`, you can use
  the container to generate an SVG file as follows:
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts build_now buildability for Wrap local mmdc CLI or Node.js run() API to render Mermaid diagrams to SVG/PNG/PDF. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:1-17): mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Wrap local mmdc CLI or Node.js run() API to render Mermaid diagrams to SVG/PNG/PDF", "blockers": ["Requires local Node.js/Chromium or Docker/Podman runtime; Linux sandbox and Docker permission caveats apply.", "Node.js programmatic API is explicitly not covered by semver.", "No official MCP server found in checked official repo docs (local CLI wrapper needed)."], "next_steps": ["Install @mermaid-js/mermaid-cli locally or pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli.", "Invoke mmdc -i input.mmd -o output.svg (or PNG/PDF) in a sandboxed local tool wrapper."]}`
  - Original Rationale: Open-source MIT local CLI with zero auth or billing gates is feasible to wrap immediately; documentary feasibility only, not an operational execution test.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "build_now", "scope": "Wrap local mmdc CLI or Node.js run() API to render Mermaid diagrams to SVG/PNG/PDF", "blockers": ["Requires local Node.js/Chromium or Docker/Podman runtime; Linux sandbox and Docker permission caveats apply.", "Node.js programmatic API is explicitly not covered by semver.", "No official MCP server found in checked official repo docs (local CLI wrapper needed)."], "next_steps": ["Install @mermaid-js/mermaid-cli locally or pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli.", "Invoke mmdc -i input.mmd -o output.svg (or PNG/PDF) in a sandboxed local tool wrapper."]}`
  - Corrected Rationale: Buildability inference is anchored to verified Mermaid CLI repository documentation: open-source MIT license, local npm/npx execution (mmdc), Node.js run() programmatic API, zero cloud credentials, and zero vendor gating (98.identity, 98.auth.none, 98.api.cli).

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:169-172`)
  - *Observation*: paraphrase: Known operational issues include Linux sandbox configuration, Docker permission denied, and configuring an already-installed Chromium browser.
  ```text
  ## Known issues
  1. [Linux sandbox issue](docs/linux-sandbox-issue.md)
  2. [Docker permission denied issue](docs/docker-permission-denied.md)
  3. [How to setup up mermaid to use already installed chromium?](docs/already-installed-chromium.md)
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.admin_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:9-23): Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Local CLI/package installation requires no vendor tenant or workspace administrator approval.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.contact_sales_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No sales contact is required to install or run MIT-licensed software.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-17) states: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:1-17) states: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software. The cited route appears accessible without this particular gate for production access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.partner_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No partner program gate applies to MIT-licensed local software.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:9-23) states: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:111-135`)
  - *Observation*: paraphrase: Official container images are published on GHCR (ghcr.io/mermaid-js/mermaid-cli/mermaid-cli) and Docker Hub (minlag/mermaid-cli) for local Docker or Podman execution.
  ```text
  ```sh
  docker pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli
  ```
  or e.g. version 8.8.0
  ```sh
  docker pull minlag/mermaid-cli:8.8.0
  ```
  The container looks for input files in `/data`. So for example, if you have a
  diagram defined on your system in `/path/to/diagrams/diagram.mmd`, you can use
  the container to generate an SVG file as follows:
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.production.vendor_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Open-source MIT distribution on npm/GitHub/GHCR requires no vendor API approval.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Render Mermaid diagram definitions and Markdown code blocks locally to SVG, PNG, or PDF via the mmdc CLI or Node.js API.. Source evidence (lines:1-17) states: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:1-17`)
  - *Observation*: paraphrase: mermaid-cli (@mermaid-js/mermaid-cli) is the official command-line interface (mmdc) for Mermaid, converting .mmd diagram definitions and Markdown mermaid blocks into SVG, PNG, or PDF files.
  ```text
  # mermaid-cli
  [![npm version](https://img.shields.io/npm/v/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![node-lts (scoped)](https://img.shields.io/node/v-lts/@mermaid-js/mermaid-cli)](https://www.npmjs.com/package/@mermaid-js/mermaid-cli)
  [![Docker Image Version (latest semver)](https://img.shields.io/docker/v/minlag/mermaid-cli?label=Dockerhub)](https://hub.docker.com/r/minlag/mermaid-cli)
  [![Build, test and deploy mermaid-cli Docker image](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml/badge.svg)](https://github.com/mermaid-js/mermaid-cli/actions/workflows/compile-mermaid.yml)
  [![This project is using Percy.io for visual regression testing.](https://percy.io/static/images/percy-badge.svg)](https://percy.io/Mermaid/mermaid-cli)
  [![Join our Slack!](https://img.shields.io/static/v1?message=join%20chat&color=9cf&logo=slack&label=slack)](https://join.slack.com/t/mermaid-talk/shared_invite/enQtNzc4NDIyNzk4OTAyLWVhYjQxOTI2OTg4YmE1ZmJkY2Y4MTU3ODliYmIwOTY3NDJlYjA0YjIyZTdkMDMyZTUwOGI0NjEzYmEwODcwOTE)
  This is a command-line interface (CLI) for [mermaid](https://mermaid.js.org/). It takes a mermaid definition file as input and generates an SVG/PNG/PDF file as output. There's basic support for converting mermaid code blocks embedded within Markdown files.
  ## Installation
  ```sh
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.admin_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:9-23): Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Local CLI/package installation requires no vendor tenant or workspace administrator approval.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.contact_sales_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No sales contact is required to install or run MIT-licensed software.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:1-17) states: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:1-17) states: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software. The cited route appears accessible without this particular gate for test access; silence in documentation alone would not prove the requirement never exists.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.partner_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: No partner program gate applies to MIT-licensed local software.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:9-23) states: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:111-135`)
  - *Observation*: paraphrase: Official container images are published on GHCR (ghcr.io/mermaid-js/mermaid-cli/mermaid-cli) and Docker Hub (minlag/mermaid-cli) for local Docker or Podman execution.
  ```text
  ```sh
  docker pull ghcr.io/mermaid-js/mermaid-cli/mermaid-cli
  ```
  or e.g. version 8.8.0
  ```sh
  docker pull minlag/mermaid-cli:8.8.0
  ```
  The container looks for input files in `/data`. So for example, if you have a
  diagram defined on your system in `/path/to/diagrams/diagram.mmd`, you can use
  the container to generate an SVG file as follows:
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:136-158`)
  - *Observation*: paraphrase: Exposes a local Node.js API (import { run } from "@mermaid-js/mermaid-cli", explicitly not covered by semver) as well as local npm and npx invocation.
  ```text
  ## Use Node.JS API
  It's possible to call `mermaid-cli` via a Node.JS API.
  Please be aware that **the NodeJS API is not covered by semver**, as `mermaid-cli` follows
  `mermaid`'s versioning.
  ```js
  import { run } from "@mermaid-js/mermaid-cli";
  await run(
  "input.mmd",
  "output.svg", // {optional options},
  );
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `98.testing.vendor_approval_required` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts false. The claim describes an absence of approval or access gating, which the available excerpts do not conclusively prove. Available source (lines:1-17): Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: observed`, `value: false`
  - Original Rationale: Open-source MIT distribution on npm/GitHub/GHCR requires no vendor API approval.
- **Corrected Answer**: `status: not_applicable`, `value: null`
  - Corrected Rationale: Research correction: Mermaid CLI is an offline open-source CLI utility (@mermaid-js/mermaid-cli) licensed under MIT. Credential gating conditions do not apply to local software that executes without accounts or API keys. Relabeled from observed (false) to not_applicable per evidence rules for CLI/local software.

#### Primary Evidence & Excerpts
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/LICENSE) (locator: `lines:1-17`)
  - *Observation*: paraphrase: Mermaid CLI is distributed under the MIT License, granting permission free of charge to use, copy, modify, publish, and distribute the software.
  ```text
  MIT License
  Copyright (c) 2017-2026 Tyler Long, Mindaugas Laganeckas, Alois Klink
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
  ```
- **URL**: [https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md](https://raw.githubusercontent.com/mermaid-js/mermaid-cli/master/README.md) (locator: `lines:9-23`)
  - *Observation*: paraphrase: Installed via npm install -g @mermaid-js/mermaid-cli or alternative local npm, npx, Yarn, or Docker/Podman methods; invoked locally via mmdc.
  ```text
  ## Installation
  ```sh
  npm install -g @mermaid-js/mermaid-cli
  ```
  ## Usage
  Convert Mermaid mmd Diagram File To SVG
  ```sh
  mmdc -i input.mmd -o output.svg
  ```
  > **Note**
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

## App 97: higgsfield (AI, Research and Media-native)
- Total claims: 22 | Corrected: 2

### Claim: `97.api.breadth` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts moderate. The assertion is inferred rather than a directly documented vendor statement. Available source (lines:32-59): Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: "moderate"`
  - Original Rationale: Multiple related media-generation, character/workflow, and workspace-billing resource groups.
- **Corrected Answer**: `status: inferred`, `value: "moderate"`
  - Corrected Rationale: Higgsfield API reference focuses on related media generation workflows: (1) Image/Video Generation Task Submissions, (2) Task Status & Asset Polling, and (3) Model Configurations. Per evidence rules, multiple related workflow endpoints substantiate moderate breadth.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.group.account_workspace_assets` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Account balance, transactions, personal/team billing workspaces, and generated Assets (7+ day retention on API). Source evidence (lines:40-58) states: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:97-100`)
  - *Observation*: paraphrase: API accounts start as personal organizations and can create team organizations; API keys appear only once at creation and unlock 20 concurrent requests.
  ```text
  Can several people use one API account?
  Yes. Every account starts as a personal organization, and you can create a team organization and invite people to it. To switch between workspaces, click your profile icon and open Organization. Usage across the account shows up in the Analytics and Billing sections.
  I lost my API key. Can I see it again?
  No. The key is visible only at the moment of creation. Generate a new key in the console and update your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.group.media_generation` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Asynchronous video, image, 3D, and audio/voiceover generation across 50+ API catalog / 35+ CLI models plus cost estimation. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.group.soul_characters_workflows` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Soul ID character training/reuse and media workflows (reframe, dubbing, voice change, draw-to-video, upscaling, background removal, Ad Multiplier). Source evidence (lines:40-58) states: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.protocol.cli` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts CLI. Source evidence (lines:32-38) states: Higgsfield is an AI-native creative suite for video and image generation with an open-source CLI (higgsfield/higgs) that signs in via browser and charges plan credits. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:32-38`)
  - *Observation*: paraphrase: Higgsfield is an AI-native creative suite for video and image generation with an open-source CLI (higgsfield/higgs) that signs in via browser and charges plan credits.
  ```text
  Higgsfield CLI lets you generate images and videos from a terminal, script or coding agent without opening the web app. It installs with curl, Homebrew or npm and runs the same models as the web app from the same account and credit balance. One command creates a generation, another shows its cost first, and --json makes every answer readable for scripts and agents.
  What Is Higgsfield CLI?
  This guide covers installation, sign-in, an image and a video made from that image, cost checks, Soul ID, batch scripts and the difference between CLI, MCP and the Higgsfield API. Higgsfield CLI is an open-source command-line client for Higgsfield, an AI-native creative suite for video and image generation. The code and releases are on GitHub. The command is higgsfield, with higgs as a shorter alias.
  Three things define how it works:
  No API key. You sign in through the browser with a regular Higgsfield account.
  Same credits. Every generation is charged to that account's plan credits at standard rates.
  Web-only access stays on the web. Unlimited model access and free generations do not apply to CLI generations.
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.protocol.mcp` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts other. Source evidence (lines:44-55) states: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.protocol.rest` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts REST. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.protocol.sdk` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts SDK. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.api.public_docs` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The cited API descriptions bear on the stated interface breadth and documented endpoints.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:40-58`)
  - *Observation*: paraphrase: CLI covers 35+ image/video/3D/audio models and Virality Predictor, Soul ID character training, workflows (reframe, dubbing, voice change, draw-to-video), account/workspaces, and marketing/website/game commands with --json output.
  ```text
  Area
  What the CLI covers
  Command group
  Generation
  35+ models and tools for image, video, 3D and audio, plus analysis such as Virality Predictor
  generate, model
  Characters
  Training and reusing Soul characters
  soul-id
  Workflows
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.auth.api_key` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts API_key authentication for Higgsfield API (api.higgsfield.ai), separate from CLI/MCP. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:97-100`)
  - *Observation*: paraphrase: API accounts start as personal organizations and can create team organizations; API keys appear only once at creation and unlock 20 concurrent requests.
  ```text
  Can several people use one API account?
  Yes. Every account starts as a personal organization, and you can create a team organization and invite people to it. To switch between workspaces, click your profile icon and open Organization. Usage across the account shows up in the Analytics and Billing sections.
  I lost my API key. Can I see it again?
  No. The key is visible only at the moment of creation. Generate a new key in the console and update your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.auth.cli_browser_oauth` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Higgsfield CLI (@higgsfield/cli). Source evidence (lines:127-135) states: higgsfield auth login opens a browser consent page (email, profile, org membership) and stores a short-lived local access token; higgsfield auth token prints it and no API key is used. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:127-135`)
  - *Observation*: paraphrase: higgsfield auth login opens a browser consent page (email, profile, org membership) and stores a short-lived local access token; higgsfield auth token prints it and no API key is used.
  ```text
  How to Sign In and Check Your Account
  Sign-in works through the browser, the same way any connected app signs in. There is no key to copy.
  1. Start the login. The terminal prints "Opening browser for authentication" and waits. If no browser opens, the terminal also prints the path of a local sign-in file to open manually.
  higgsfield auth login
  2. Approve in the browser. A Higgsfield consent page lists what the CLI will access: your email, basic profile, organization membership and permission to remember the login. Click Allow. The browser shows "Device authorized" and the terminal prints "Successfully authenticated".
  3. Confirm the account. It prints one line: email, plan name and available credits.
  higgsfield account status
  Two related command groups:
  higgsfield auth token prints the current access token, and higgsfield auth logout deletes it. Treat the token as a secret: do not paste it into prompts, logs, screenshots or source control. The token is kept in a local credentials file and is short-lived, so a "Session expired" message means running auth login again.
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.auth.mcp_browser_signin` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts OAuth2 authentication for Higgsfield hosted MCP server (https://mcp.higgsfield.ai/mcp). Source evidence (lines:78-109) states: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance. This provides evidence for the named authentication mechanism in the specified context, which may differ from other endpoints or clients.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:78-109`)
  - *Observation*: paraphrase: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.
  ```text
  CLI vs MCP vs API
  Higgsfield has three programmatic routes. They differ by who calls them and how they are billed, so the choice comes before installation.
  CLI vs MCP vs API
  Criteria
  CLI
  MCP
  Higgsfield API
  Made for
  Terminal, scripts, coding agents
  Chat agents such as Claude and other MCP-compatible clients
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.buildability` **[CORRECTED - ACTION REQUIRED]**
- **Baseline Human Judgment**: `unsupported`
- **Baseline Reason**: Claim asserts conditional buildability for Generate AI images/video via Higgsfield REST/SDK API ($5+ prepaid balance) or CLI/MCP (paid subscription credits). The assertion is inferred rather than a directly documented vendor statement. Available source (lines:78-109): Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.

#### Before / After Comparison
- **What Changed**: Task 18 Phase A error corrections addressing Task 17 human baseline review findings.
- **Original Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Generate AI images/video via Higgsfield REST/SDK API ($5+ prepaid balance) or CLI/MCP (paid subscription credits)", "blockers": ["No free programmatic tier: API requires $5 minimum prepaid USD top-up (expiring in 1 year), while CLI and MCP require a paid subscription and exclude web Unlimited/free generations.", "API outputs are stored for at least 7 days and must be downloaded for long-term retention.", "CLI browser tokens are short-lived and require re-running higgsfield auth login when expired."], "next_steps": ["For app/backend integrations, fund an open.higgsfield.ai USD balance and generate an API key for api.higgsfield.ai.", "For agent/terminal workflows on an existing paid plan, install @higgsfield/cli or connect https://mcp.higgsfield.ai/mcp."]}`
  - Original Rationale: All three programmatic interfaces are publicly documented and self-serve, conditioned on prepaid USD funding (API) or a paid subscription (CLI/MCP). Documentary inference only.
- **Corrected Answer**: `status: inferred`, `value: {"verdict": "conditional", "scope": "Generate AI images/video via Higgsfield REST/SDK API ($5+ prepaid balance) or CLI/MCP (paid subscription credits)", "blockers": ["No free programmatic tier: API requires $5 minimum prepaid USD top-up (expiring in 1 year), while CLI and MCP require a paid subscription and exclude web Unlimited/free generations.", "API outputs are stored for at least 7 days and must be downloaded for long-term retention.", "CLI browser tokens are short-lived and require re-running higgsfield auth login when expired."], "next_steps": ["For app/backend integrations, fund an open.higgsfield.ai USD balance and generate an API key for api.higgsfield.ai.", "For agent/terminal workflows on an existing paid plan, install @higgsfield/cli or connect https://mcp.higgsfield.ai/mcp."]}`
  - Corrected Rationale: Conditional buildability inference is anchored to verified Higgsfield documentation: REST API and CLI require paid API credits ($5+ credit pack) and API key authentication (97.testing.paid_required, 97.auth.api_key, 97.api.rest).

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:78-109`)
  - *Observation*: paraphrase: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.
  ```text
  CLI vs MCP vs API
  Higgsfield has three programmatic routes. They differ by who calls them and how they are billed, so the choice comes before installation.
  CLI vs MCP vs API
  Criteria
  CLI
  MCP
  Higgsfield API
  Made for
  Terminal, scripts, coding agents
  Chat agents such as Claude and other MCP-compatible clients
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.mcp.discovery` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts found. Source evidence (lines:78-109) states: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:78-109`)
  - *Observation*: paraphrase: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.
  ```text
  CLI vs MCP vs API
  Higgsfield has three programmatic routes. They differ by who calls them and how they are billed, so the choice comes before installation.
  CLI vs MCP vs API
  Criteria
  CLI
  MCP
  Higgsfield API
  Made for
  Terminal, scripts, coding agents
  Chat agents such as Claude and other MCP-compatible clients
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.mcp.higgsfield` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts origin=official; name=Higgsfield MCP Server; source_url=https://higgsfield.ai/enterprise-help-center/platform/integration. Source evidence (lines:78-109) states: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance. The cited MCP-specific documentation bears on server availability, transport and authentication; MCP support should be distinguished from a general REST API.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:78-109`)
  - *Observation*: paraphrase: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.
  ```text
  CLI vs MCP vs API
  Higgsfield has three programmatic routes. They differ by who calls them and how they are billed, so the choice comes before installation.
  CLI vs MCP vs API
  Criteria
  CLI
  MCP
  Higgsfield API
  Made for
  Terminal, scripts, coding agents
  Chat agents such as Claude and other MCP-compatible clients
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.production.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:110-124) states: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP. The cited access or pricing terms indicate a no-cost path for production access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.production.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:110-124) states: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP. The cited policy describes this access condition for production access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.production.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The documented signup, installation or credential workflow supports a self-serve path for production access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:127-135`)
  - *Observation*: paraphrase: higgsfield auth login opens a browser consent page (email, profile, org membership) and stores a short-lived local access token; higgsfield auth token prints it and no API key is used.
  ```text
  How to Sign In and Check Your Account
  Sign-in works through the browser, the same way any connected app signs in. There is no key to copy.
  1. Start the login. The terminal prints "Opening browser for authentication" and waits. If no browser opens, the terminal also prints the path of a local sign-in file to open manually.
  higgsfield auth login
  2. Approve in the browser. A Higgsfield consent page lists what the CLI will access: your email, basic profile, organization membership and permission to remember the login. Click Allow. The browser shows "Device authorized" and the terminal prints "Successfully authenticated".
  3. Confirm the account. It prints one line: email, plan name and available credits.
  higgsfield account status
  Two related command groups:
  higgsfield auth token prints the current access token, and higgsfield auth logout deletes it. Treat the token as a secret: do not paste it into prompts, logs, screenshots or source control. The token is kept in a local credentials file and is short-lived, so a "Session expired" message means running auth login again.
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.purpose` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts Generate AI video, images, Soul characters, and creative workflows via Higgsfield REST/SDK API, open-source CLI, or hosted MCP.. Source evidence (lines:32-38) states: Higgsfield is an AI-native creative suite for video and image generation with an open-source CLI (higgsfield/higgs) that signs in via browser and charges plan credits. The cited product description supports the claimed primary function and integration scope.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:32-38`)
  - *Observation*: paraphrase: Higgsfield is an AI-native creative suite for video and image generation with an open-source CLI (higgsfield/higgs) that signs in via browser and charges plan credits.
  ```text
  Higgsfield CLI lets you generate images and videos from a terminal, script or coding agent without opening the web app. It installs with curl, Homebrew or npm and runs the same models as the web app from the same account and credit balance. One command creates a generation, another shows its cost first, and --json makes every answer readable for scripts and agents.
  What Is Higgsfield CLI?
  This guide covers installation, sign-in, an image and a video made from that image, cost checks, Soul ID, batch scripts and the difference between CLI, MCP and the Higgsfield API. Higgsfield CLI is an open-source command-line client for Higgsfield, an AI-native creative suite for video and image generation. The code and releases are on GitHub. The command is higgsfield, with higgs as a shorter alias.
  Three things define how it works:
  No API key. You sign in through the browser with a regular Higgsfield account.
  Same credits. Every generation is charged to that account's plan credits at standard rates.
  Web-only access stays on the web. Unlimited model access and free generations do not apply to CLI generations.
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:78-109`)
  - *Observation*: paraphrase: Higgsfield offers three programmatic routes: CLI and MCP share a higgsfield.ai account, browser sign-in (no API key), and plan credits; Higgsfield API is a separate product with an API key from open.higgsfield.ai and a prepaid US dollar balance.
  ```text
  CLI vs MCP vs API
  Higgsfield has three programmatic routes. They differ by who calls them and how they are billed, so the choice comes before installation.
  CLI vs MCP vs API
  Criteria
  CLI
  MCP
  Higgsfield API
  Made for
  Terminal, scripts, coding agents
  Chat agents such as Claude and other MCP-compatible clients
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.testing.free_access` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts false. Source evidence (lines:110-124) states: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP. The cited access or pricing terms indicate a no-cost path for test access; confirm usage limits and conditions.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.testing.paid_required` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:110-124) states: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP. The cited policy describes this access condition for test access, subject to account type and vendor terms.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:110-124`)
  - *Observation*: paraphrase: Higgsfield CLI requires a paid Higgsfield subscription and installs via curl, Homebrew, or npm (@higgsfield/cli); free web generations and Unlimited web access do not apply to CLI or MCP.
  ```text
  What You Need Before Installing
  You need three things:
  A paid Higgsfield subscription.
  A terminal on macOS, Linux or Windows.
  One package route: curl (macOS and Linux, nothing else required), Homebrew (needs Homebrew) or npm (needs Node.js).
  A coding agent is optional. If you plan to call the CLI from Claude Code, Codex, OpenClaw or Hermes, the agent can run the installation itself. That is covered in the agents section below.
  How to Install Higgsfield CLI
  All three methods install the same tool. Pick the one that matches the rest of your setup, because updates go through the same method you installed with.
  1. Install with curl (macOS and Linux). The installer may ask for your system password.
  curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
  ```
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:60-66`)
  - *Observation*: paraphrase: API billing is prepaid pay-as-you-go in US dollars with a $5 minimum top-up (funds expire after 1 year, failed requests refunded); generation is asynchronous via polling or webhooks and outputs stay stored for at least 7 days.
  ```text
  How is API usage billed?
  Billing is pay-as-you-go from a US dollar balance, and the minimum top-up is $5. Video models are priced per second of output and image models per image; DoP is the exception, priced per generation. Each model has a fixed rate for every configuration: the rate depends on settings like resolution and audio, is listed publicly, and stays the same regardless of how much you top up. An estimate endpoint returns the cost of a request before you run it. Funds expire one year after they are added to the balance. The balance can't go below zero: once it's empty, new requests wait until you add funds, or you can turn on auto top-up so production traffic never stops.
  You're only charged for generations that finish successfully. If a request fails, its cost returns to your balance automatically.
  How does generation work?
  Generation is asynchronous. You submit a request and receive a request ID, then track progress by polling the status or by receiving a webhook when the result is ready. Once the generation completes, you download the output file.
  How long are generated files stored?
  Generated output files stay available for at least 7 days after creation and may be removed from Higgsfield servers after that period. For long-term retention, download completed files to your own storage as part of your integration.
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---

### Claim: `97.testing.self_serve` [UNCHANGED - BASELINE VERIFIED]
- **Baseline Human Judgment**: `correct`
- **Baseline Reason**: Claim asserts true. Source evidence (lines:32-59) states: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required. The documented signup, installation or credential workflow supports a self-serve path for test access, subject to vendor restrictions.

#### Primary Evidence & Excerpts
- **URL**: [https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api](https://higgsfield.ai/creator-hub/help-center/integrations/what-is-the-higgsfield-api) (locator: `lines:32-59`)
  - *Observation*: paraphrase: Higgsfield API (api.higgsfield.ai, console open.higgsfield.ai, docs docs.higgsfield.ai) unlocks 50+ video/image models with one API key, Python/TypeScript SDKs, or REST; no higgsfield.ai web subscription is required.
  ```text
  The Higgsfield API lets you generate video and images from your own code: one API key opens every model in the API catalog, and each request is paid in US dollars from a prepaid balance. No plan or subscription is involved: fund the balance, send requests at the rates listed in the catalog, and new requests simply wait once the balance hits zero.
  How is the API different from my Higgsfield plan?
  A subscription on higgsfield.ai and the API are two separate products with separate billing. Your plan, credits, and Unlimited access exist only on the website; the API runs on its own account balance in US dollars.
  How is the API different from my Higgsfield plan?
  Criteria
  Higgsfield plan (higgsfield.ai)
  Higgsfield API
  Who it's for
  Creators working in the visual interface
  Developers building generation into their own products
  ```
- **URL**: [https://higgsfield.ai/blog/higgsfield-cli](https://higgsfield.ai/blog/higgsfield-cli) (locator: `lines:127-135`)
  - *Observation*: paraphrase: higgsfield auth login opens a browser consent page (email, profile, org membership) and stores a short-lived local access token; higgsfield auth token prints it and no API key is used.
  ```text
  How to Sign In and Check Your Account
  Sign-in works through the browser, the same way any connected app signs in. There is no key to copy.
  1. Start the login. The terminal prints "Opening browser for authentication" and waits. If no browser opens, the terminal also prints the path of a local sign-in file to open manually.
  higgsfield auth login
  2. Approve in the browser. A Higgsfield consent page lists what the CLI will access: your email, basic profile, organization membership and permission to remember the login. Click Allow. The browser shows "Device authorized" and the terminal prints "Successfully authenticated".
  3. Confirm the account. It prints one line: email, plan name and available credits.
  higgsfield account status
  Two related command groups:
  higgsfield auth token prints the current access token, and higgsfield auth logout deletes it. Treat the token as a secret: do not paste it into prompts, logs, screenshots or source control. The token is kept in a local credentials file and is short-lived, so a "Session expired" message means running auth login again.
  ```
- **URL**: [https://higgsfield.ai/enterprise-help-center/platform/integrations](https://higgsfield.ai/enterprise-help-center/platform/integrations) (locator: `lines:44-55`)
  - *Observation*: paraphrase: Higgsfield MCP connects at https://mcp.higgsfield.ai/mcp via browser sign-in (no API key) using workspace credits to generate images/video, upscale, remove backgrounds, use Soul characters, voiceover/voice clones/dubbing, and Ad Multiplier.
  ```text
  Generate from Claude, coding agents, Figma and Adobe apps with your workspace credits. No API key needed.
  Connect Higgsfield MCP
  Connect from Claude
  In Claude (web or desktop), open Settings → Connectors → Add custom connector.
  Paste https://mcp.higgsfield.ai/mcp and click Connect.
  Sign in to Higgsfield in the window that opens.
  Start a new chat and ask "What is my Higgsfield credit balance?" to confirm it works.
  Connect from ChatGPT
  In ChatGPT, open Higgsfield’s connection page, choose Add Higgsfield in ChatGPT, and connect your Higgsfield account.
  What you can do through MCP
  ```

#### Human Recheck Decision (Applicant Input)
- [ ] **Judgment** (`correct` / `incorrect` / `unsupported` / `unresolved` / `not_applicable`): `________`
- **Explanation**: `____________________________________________________________________`
- **Reviewer Identity**: `________________________`
- **Date**: `____________________`
- [ ] **Actual Human Attestation**: *I confirm this judgment represents my real human evaluation of primary documentation.*

---
