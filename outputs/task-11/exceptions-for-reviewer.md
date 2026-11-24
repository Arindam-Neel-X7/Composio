# Task 11: Exceptions, Unknowns & Reviewer Notes (Ecommerce, IDs 41–50)

- **Target Run**: `work/research-runs/task11-first-pass-004`
- **Review Status**: `pending` (`accuracy: null`, `review_coverage: 0.0%`). No independent review or human check has been performed.

## 1. Frozen 20-App Sample Members in This Batch
- **App 46 (Squarespace)**: Included in `outputs/task-06/sampling-manifest.json`. `developers.squarespace.com/commerce-apis` top navigation lists `MCP`, but no MCP doc page was captured in this pass, so `46.mcp.discovery` is preserved as `unknown`.
- **App 50 (fanbasis)**: Included in `outputs/task-06/sampling-manifest.json`. Official homepage `www.fanbasis.com` redirects/displays `FanBasis is now Commas!` (Commas Inc.) with `Enterprise & APIs` and `MCP (beta)`. Legacy `dev-docs.fanbasis.com` (`FanBasis API Docsv3`) is password-protected (`Sign in to access API Docs`), and `commasdocs.com` rendered only a 2-line JS `Unpacking...` shell. Auth methods, credential eligibility booleans, wire protocol, and API breadth remain honestly `unknown` / `partial` pending accessible documentation or vendor outreach.

## 2. HTTP 403 / 404 / Timeout / JS-Shell Captures
- **App 41 (Shopify)**: `shopify.dev/docs/apps/build/authentication`, `authorization-code-grant`, `ai-toolkit`, `customer-accounts/mcp`, and `github.com/Shopify/dev-mcp` returned HTTP 404. Client credentials grant, GraphQL Admin API (`X-Shopify-Access-Token`), Dev stores, Pricing, and Shop MCP (`shopify.dev/docs/agents`) were captured cleanly.
- **App 44 (Salesforce Commerce Cloud)**: `developer.salesforce.com/docs/commerce/commerce-api/guide/*` returned HTTP 403 (`blocked`). Findings are grounded in official `SalesforceCommerceCloud` GitHub repos (`commerce-sdk`, `commerce-sdk-isomorphic`, `b2c-developer-tooling`) and `salesforce.com/commerce/pricing/`. `44.api.public_docs` is kept `unknown` rather than inferred.
- **App 45 (Magento / Adobe Commerce)**: `business.adobe.com/products/magento/pricing.html` timed out and `gs-authentication-token` returned HTTP 404. REST, GraphQL, Authentication overview, and `github.com/magento/magento2` (OSL 3.0) were captured cleanly.
- **App 46 (Squarespace)**: `developers.squarespace.com/commerce-apis/orders-api` returned HTTP 404 (replaced by `orders-overview`) and `support.squarespace.com` article timed out (`squarespace.com/pricing` captured 774 lines cleanly).
- **App 47 (Ecwid)**: `docs.ecwid.com/api-reference/rest-api/authentication` returned HTTP 404; OAuth 2.0 model and 600 req/min rate limit are confirmed on `docs.ecwid.com/api-reference/rest-api/overview`.
- **App 48 (Gumroad)**: `gumroad.com/api` and `help.gumroad.com/article/280-create-application-api` rendered 1-line JS shells and are excluded from all claim citations. Findings are grounded in `gumroad.com/pricing`, official `github.com/antiwork/gumroad`, official `github.com/antiwork/gumroad-cli` (`gumroad mcp`), and community `github.com/rmarescu/gumroad-mcp` (MCP entry only). `48.api.public_docs` is kept `unknown`.
- **App 49 (Amazon Selling Partner)**: Legacy URLs `onboarding-as-a-developer` and `connect-to-the-sp-api` returned 21-line `Page Not Found` pages and are excluded from all citations. Active SP-API docs (`what-is-the-selling-partner-api`, `registering-as-a-developer`, `authorizing-selling-partner-api-applications`, `connecting-to-the-selling-partner-api`, `the-selling-partner-api-sandbox`), official `amzn/selling-partner-agentic-toolkit` (`https://sellingpartner-ai.amazon.com/mcp`), and community `jay-trivedi/amazon_sp_mcp` were captured cleanly.

## 3. Immutable Run History
- `task11-capture-001`: failed pre-check under global Python (lacked `jsonschema`); preserved untouched.
- `task11-capture-002`: sandboxed run under `.venv` (DNS blocked, 0 captures); preserved untouched.
- `task11-capture-003`: initial live capture (42 captures); preserved untouched.
- `task11-capture-004`: supplementary live capture (57 captures total); parent of extraction.
- `task11-first-pass-001`: rejected by runtime validator (community repo attached to App 48 product claims); preserved untouched.
- `task11-first-pass-002`: rejected by runtime validator (App 50 MCP scope wording lacked explicit 'server'); preserved untouched.
- `task11-first-pass-003`: initial sealed first-pass run (remediated after independent AI audit identified 4 locator line-range defects on Apps 44, 46, and 50); preserved untouched.
- `task11-first-pass-004`: sealed, validated, remediated first-pass deliverable run.
