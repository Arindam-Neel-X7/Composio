"""Task 11 researcher-authored extraction (Ecommerce, IDs 41-50, contract v1.1).

Every claim and paraphrase was authored after directly reading the captured primary
and community snapshots in task11-capture-004. No model API, synthetic fixture,
authenticated account operation, independent review, or accuracy measurement occurs here.
"""
import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import research_pipeline as p
from make_sources import SCOPES


def build(capture_run: str, destination: Path):
    directory = ROOT / "work/research-runs" / capture_run
    p.verify_seal(directory)
    records = copy.deepcopy(p.read_json(directory / "records.json"))
    captures = p.read_json(directory / "captures.json")

    by_app_url = {}
    for c in captures:
        by_app_url[(c["spec"]["app_id"], c["spec"]["url"])] = c

    def find_cap(app_id: int, substr: str):
        exact = [c for (aid, u), c in by_app_url.items() if aid == app_id and u.endswith(substr)]
        if len(exact) == 1:
            return exact[0]
        matches = [c for (aid, u), c in by_app_url.items() if aid == app_id and substr in u]
        assert len(matches) == 1, f"Expected 1 match for ({app_id}, {substr!r}), got {len(matches)}"
        return matches[0]

    for r in records:
        app = r["identity"]["id"]
        scope = SCOPES[app]

        def E(substr: str, first: int, last: int, para: str):
            c = find_cap(app, substr)
            lines = (directory / c["snapshot_ref"]).read_text(encoding="utf-8").splitlines()
            assert 1 <= first <= last <= len(lines), (app, substr, first, last, len(lines))
            e = p.evidence_for(c, first, lines[first - 1])
            e.update(locator=f"lines:{first}-{last}", observation="paraphrase: " + para)
            return e

        def claim(key, value, ev=(), status="observed", refs=(),
                  rationale="Documentary observation only; independent review pending."):
            return {
                "claim_id": f"{app}.{key}",
                "status": status,
                "value": value,
                "context": scope,
                "evidence": list(ev),
                "supporting_claim_refs": [f"{app}.{x}" for x in refs],
                "rationale": rationale,
            }

        AUTH_MAP = {
            "oauth2": "OAuth2",
            "api_key": "API_key",
            "basic": "Basic",
            "bearer_token": "Bearer_token",
            "jwt": "JWT",
            "session_cookie": "session_cookie",
            "other": "other",
        }

        def auth(key, method, details, ev, subcontext, scopes=(), status="observed", refs=()):
            return claim(
                "auth." + key,
                {"method": AUTH_MAP.get(method, method), "context": subcontext, "scopes": list(scopes), "details": details},
                ev,
                status,
                refs,
                "Scoped mechanism from primary documentation; no credentials obtained or authenticated call executed.",
            )

        def items(target, entries, notes, cov="partial"):
            target.update(coverage_status=cov, items=entries, notes=notes)

        def elig(env, key, val, ev, rationale, status="observed", refs=()):
            r["credential_eligibility"][env][key] = claim(f"{env}.{key}", val, ev, status, refs, rationale)

        def group(key, value, ev):
            return claim("api.group." + key, value, ev)

        def breadth(value, groups, ev, reason):
            r["api_surface"]["breadth"] = claim(
                "api.breadth", value, ev, "inferred", ["api.group." + g for g in groups], reason
            )

        def set_mcp_entries(entries_spec, discovery_ev):
            out = []
            for key, origin, name, ev, substr, tool_scope, server, repo in entries_spec:
                op = claim(
                    f"mcp.{key}.operational",
                    None,
                    status="not_researched",
                    rationale="No MCP connection or tool call was attempted.",
                )
                c = find_cap(app, substr)
                out.append(claim(
                    "mcp." + key,
                    {
                        "origin": origin,
                        "name": name,
                        "source_url": c["spec"]["url"],
                        "repository_url": repo,
                        "server_url": server,
                        "scope": tool_scope,
                        "operational_check": op,
                    },
                    ev,
                    "observed",
                    (),
                    "MCP entry documented in captured source; operational execution remains not_researched.",
                ))
            r["mcp"]["discovery"] = claim(
                "mcp.discovery",
                "found",
                discovery_ev,
                "observed",
                (),
                "At least one callable MCP server entry matching the product scope was observed in captured sources.",
            )
            r["mcp"]["entries"] = out

        def set_mcp_not_found(ev, rationale):
            r["mcp"]["discovery"] = claim("mcp.discovery", None, ev, "not_found_in_checked_sources", (), rationale)
            r["mcp"]["entries"] = []

        def set_mcp_unknown(ev, rationale):
            r["mcp"]["discovery"] = claim("mcp.discovery", None, ev, "unknown", (), rationale)
            r["mcp"]["entries"] = []

        def buildability(verdict, bscope, blockers, next_steps, ev, refs, reason):
            r["buildability"] = claim(
                "buildability",
                {"verdict": verdict, "scope": bscope, "blockers": blockers, "next_steps": next_steps},
                ev,
                "inferred",
                refs,
                reason,
            )

        r["credential_eligibility"]["testing"]["context"] = scope
        r["credential_eligibility"]["production"]["context"] = scope

        # =====================================================================
        # 41. Shopify
        # =====================================================================
        if app == 41:
            e_api = E("/docs/api", 73, 106, "Shopify API reference covers GraphQL Admin API, legacy REST Admin API, events/webhooks, Payments Apps API, Partner API, and Shopify MCP.")
            e_gql = E("/docs/api/admin-graphql", 51, 53, "Shopify GraphQL Admin API reference for getting up and running with Shopify's GraphQL API.")
            e_gql_hdr = E("/docs/api/admin-graphql", 124, 177, "Every GraphQL Admin API request carries an access token in the X-Shopify-Access-Token header against https://{shop}.myshopify.com/admin/api/2026-10/graphql.json.")
            e_gql_res = E("/docs/api/admin-graphql", 32, 41, "GraphQL Admin API sidebar lists Customers, Inventory, Orders, and Products and collections.")
            e_ccg = E("/client-credentials-grant", 61, 93, "Client credentials grant exchanges Dev Dashboard Client ID and Client secret for an access token for server-side apps acting on stores in your own Shopify organization.")
            e_dev = E("/development-stores", 68, 96, "Dev stores are testing environments created via Shopify CLI or Dev Dashboard by a Shopify Partner account or merchant store with developer permissions.")
            e_agents = E("/docs/agents", 30, 53, "Shop MCP is Shopify's hosted Model Context Protocol (MCP) server for product discovery, carts, checkout, and order history; Global Catalog and Storefront Catalog are MCP servers for product discovery.")
            e_price = E("/pricing", 72, 120, "Shopify plans include Basic, Grow, Advanced, and Plus with 'Try 3 days free' trial and paid monthly tiers.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Shopify commerce platform and developer APIs (GraphQL Admin API, legacy REST Admin API, Storefront/Shop MCP) documented at shopify.dev.",
                [e_api],
            )
            r["purpose"] = claim(
                "purpose",
                "Ecommerce platform with GraphQL Admin API (products, customers, orders, inventory), legacy REST Admin API, and hosted Shop MCP server.",
                [e_api, e_agents],
            )
            items(
                r["auth"],
                [
                    auth("client_credentials_oauth2", "oauth2",
                         "OAuth 2.0 client credentials grant exchanging Dev Dashboard Client ID and Client secret for an Admin API access token for stores in your own organization.",
                         [e_ccg], "Server-side apps in your own Shopify organization"),
                    auth("admin_access_token", "bearer_token",
                         "Admin API access token sent in the X-Shopify-Access-Token HTTP header on GraphQL Admin API requests.",
                         [e_gql_hdr], "GraphQL Admin API requests"),
                ],
                "Authorization code grant doc URL returned HTTP 404; client credentials grant and X-Shopify-Access-Token header are verified from captured docs.",
            )
            elig("testing", "sandbox_access", True, [e_dev], "Dev stores provide testing environments via Shopify CLI or Dev Dashboard without affecting live stores.")
            elig("testing", "trial_access", True, [e_price], "Pricing page offers a 3-day free trial ('Try 3 days free') across Basic, Grow, and Advanced plans.")
            elig("testing", "self_serve", True, [e_dev], "Developers with a Shopify Partner account or merchant store with developer permissions can create dev stores via Shopify CLI or Dev Dashboard.")
            elig("production", "paid_required", True, [e_price], "Production merchant plans (Basic, Grow, Advanced, Plus) carry monthly subscription fees.")
            elig("production", "admin_approval_required", True, [e_ccg], "Apps must be installed on the target store and granted selected access scopes in the Dev Dashboard.")
            elig("production", "vendor_approval_required", True, [E("/docs/api", 83, 83, "Some Shopify APIs require Shopify's approval or a specific Shopify plan.")],
                 "Scoped to APIs that explicitly require Shopify's approval or a specific plan (e.g., protected/special APIs); standard Admin API access is scope-gated.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.graphql", "GraphQL", [e_gql, e_gql_hdr]),
                claim("api.protocol.rest", "REST", [E("/docs/api", 40, 40, "REST Admin API (legacy) is listed among Shopify APIs.")]),
                claim("api.protocol.cli", "CLI", [e_dev]),
            ], "GraphQL Admin API is primary; REST Admin API is marked legacy; Shopify CLI manages dev stores and apps.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_api, e_gql])
            items(r["api_surface"]["resource_groups"], [
                group("products_inventory", "Products, collections, and inventory management", [e_api, e_gql_res]),
                group("orders_customers", "Orders and customers", [e_api, e_gql_res]),
                group("payments_events", "Payments Apps API, events, and webhooks", [e_api]),
                group("partner_data", "Partner API (Partner organization transactions and payouts)", [E("/docs/api", 126, 126, "Partner API provides access to Partner organization business data such as transactions and payouts.")]),
            ], "Core Admin, Payments, Events, and Partner domains documented.")
            breadth("broad", ["products_inventory", "orders_customers", "payments_events", "partner_data"], [e_api, e_gql_res],
                    "Covers multiple distinct commerce domains: products/inventory, orders/customers, payments/events, and partner business data.")

            set_mcp_entries([
                ("shop_mcp", "official", "Shopify Shop MCP", [e_agents], "/docs/agents",
                 "Official hosted callable MCP server enabling buyer-facing agents to search products, build carts, complete checkout, and check order history.",
                 None, None),
            ], [e_agents])

            buildability(
                "build_now",
                "Shopify Admin GraphQL API and hosted Shop MCP integration",
                ["Some specialized APIs require Shopify approval or specific paid plans", "Public multi-merchant app distribution requires OAuth install and store scopes"],
                ["Create a Shopify Partner account and dev store via Shopify CLI or Dev Dashboard", "Configure Dev Dashboard app scopes and X-Shopify-Access-Token auth"],
                [e_api, e_gql_hdr, e_dev, e_agents],
                ["identity", "auth.client_credentials_oauth2", "auth.admin_access_token", "testing.sandbox_access", "api.protocol.graphql", "mcp.discovery"],
                "Public GraphQL Admin API docs, self-serve Partner dev stores, OAuth client credentials/access tokens, and official Shop MCP support immediate integration development.",
            )

        # =====================================================================
        # 42. WooCommerce
        # =====================================================================
        elif app == 42:
            e_rest = E("/docs/apis/rest-api/", 18, 29, "WooCommerce 2.6+ integrates with the WordPress REST API (current version v3) for CRUD operations in JSON format.")
            e_keys = E("/docs/apis/rest-api/", 104, 114, "Users generate REST API consumer key and consumer secret in WooCommerce with read/write permissions and authenticate via HTTP Basic Auth.")
            e_ref_auth = E("woocommerce-rest-api-docs/", 534, 625, "WooCommerce REST API v3 supports HTTP Basic Auth (consumer key/secret) over HTTPS and OAuth 1.0a one-legged authentication over HTTP.")
            e_ref_res = E("woocommerce-rest-api-docs/", 22, 168, "WooCommerce REST API v3 documents Coupons, Customers, Orders, Products, totals reports, and Webhooks.")
            e_mcp = E("/docs/features/mcp/", 35, 65, "WooCommerce registers product and order abilities in WordPress; installing the MCP Adapter plugin exposes them via /wp-json/mcp/mcp-adapter-default-server using WordPress Application Password (remote HTTP) or WP-CLI (local STDIO).")
            e_mcp_proxy = E("/docs/features/mcp/", 97, 124, "Remote WordPress sites connect via @automattic/mcp-wordpress-remote proxy with WP_API_URL, WP_API_USERNAME, and WP_API_PASSWORD.")
            e_price = E("/pricing/", 12, 49, "WooCommerce is a free, open-source ecommerce platform for WordPress with no monthly subscription and unlimited products, orders, and APIs.")

            r["identity"]["resolution"] = claim(
                "identity",
                "WooCommerce open-source ecommerce plugin for WordPress, documented at developer.woocommerce.com and github.com/woocommerce/woocommerce.",
                [e_rest, e_price],
            )
            r["purpose"] = claim(
                "purpose",
                "Free, open-source WordPress ecommerce platform with WordPress REST API v3 (products, orders, customers, coupons, webhooks) and developer-preview MCP Adapter integration.",
                [e_rest, e_price, e_mcp],
            )
            items(
                r["auth"],
                [
                    auth("basic_consumer_keys", "basic",
                         "HTTP Basic Auth over HTTPS using WooCommerce REST API Consumer Key as username and Consumer Secret as password with read/write permissions.",
                         [e_keys, e_ref_auth], "WooCommerce REST API v3 over HTTPS"),
                    auth("oauth1a_http", "other",
                         "OAuth 1.0a one-legged authentication using consumer key and consumer secret for REST API requests over HTTP.",
                         [e_ref_auth], "WooCommerce REST API v3 over HTTP"),
                    auth("wp_application_password_mcp", "basic",
                         "WordPress username and Application Password (WP_API_USERNAME / WP_API_PASSWORD) over HTTPS for remote MCP Adapter connections (not WooCommerce REST API keys).",
                         [e_mcp, e_mcp_proxy], "Remote HTTP MCP Adapter connections"),
                ],
                "REST API v3 supports Basic Auth (HTTPS) and OAuth 1.0a (HTTP); remote MCP uses WordPress Application Passwords while local STDIO uses WP-CLI --user.",
            )
            elig("testing", "free_access", True, [e_price], "Core WooCommerce software is free and open-source with unlimited products, orders, and APIs.")
            elig("testing", "self_serve", True, [e_keys, e_price], "Store owners/developers can install WooCommerce locally or on WordPress and generate REST API keys self-serve.")
            elig("production", "free_access", True, [e_price], "Core WooCommerce platform has no monthly subscription or revenue share (hosting and paid extensions are separate).")
            elig("production", "paid_required", False, [e_price], "Core WooCommerce platform and APIs are free with no platform fee or paid tier required for API access.")
            elig("production", "self_serve", True, [e_keys], "REST API keys and WordPress Application Passwords are generated directly in the site's WordPress/WooCommerce dashboard.")
            elig("production", "admin_approval_required", True, [e_keys, e_mcp], "Requires a WordPress user with appropriate WooCommerce permissions/capabilities to create keys or Application Passwords.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_rest]),
                claim("api.protocol.sdk", "SDK", [E("/docs/apis/rest-api/", 42, 50, "Official @woocommerce/woocommerce-rest-api JavaScript client library example.")]),
                claim("api.protocol.cli", "CLI", [e_mcp]),
            ], "REST API v3 is primary; official JS SDK and WP-CLI local MCP transport are documented.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_rest, e_ref_res])
            items(r["api_surface"]["resource_groups"], [
                group("products_coupons", "Products and coupons", [e_ref_res]),
                group("orders_payments", "Orders and WooPayments transactions/authorizations/payouts", [e_rest, e_ref_res]),
                group("customers", "Customers", [e_ref_res]),
                group("webhooks", "Webhooks", [e_ref_res]),
            ], "WordPress REST API v3 resource groups documented in official reference.")
            breadth("broad", ["products_coupons", "orders_payments", "customers", "webhooks"], [e_rest, e_ref_res],
                    "Spans catalog/promotions, orders/payments, customers, and event webhooks across full store operations.")

            set_mcp_entries([
                ("wp_mcp_adapter", "official", "WooCommerce / WordPress MCP Adapter Integration (Developer Preview)", [e_mcp, e_mcp_proxy], "/docs/features/mcp/",
                 "Official developer-preview callable MCP server exposed via WordPress MCP Adapter plugin at each store's /wp-json/mcp/mcp-adapter-default-server endpoint (or local WP-CLI STDIO) for product and order abilities.",
                 None, None),
            ], [e_mcp])

            buildability(
                "build_now",
                "WooCommerce REST API v3 and official WordPress MCP Adapter integration",
                ["Self-hosted WordPress deployment requires store-specific base URL and HTTPS for Basic/Application Password auth", "MCP integration is in developer preview and requires installing the separate mcp-adapter plugin"],
                ["Generate REST API Consumer Key/Secret in WooCommerce settings or WordPress Application Password for MCP", "Target /wp-json/wc/v3/ endpoints or /wp-json/mcp/mcp-adapter-default-server"],
                [e_rest, e_keys, e_price, e_mcp],
                ["identity", "auth.basic_consumer_keys", "testing.free_access", "production.paid_required", "api.protocol.rest", "mcp.discovery"],
                "Free open-source platform with self-serve API keys, comprehensive public REST v3 docs, and official MCP adapter support.",
            )

        # =====================================================================
        # 43. BigCommerce
        # =====================================================================
        elif app == 43:
            e_auth = E("/start/authentication", 60, 128, "BigCommerce offers OAuth-based store-level, app-level, and account-level API accounts issuing client_id, client_secret, and non-expiring access_token for REST and GraphQL APIs.")
            e_hdr = E("/start/authentication", 138, 150, "OAuth requests route to https://api.bigcommerce.com using the X-Auth-Token header; V3 APIs are accessible exclusively with OAuth.")
            e_gql = E("/storefront/graphql", 92, 134, "GraphQL Storefront API uses Authorization: Bearer storefront API token for product and storefront queries.")
            e_sbx = E("/about/sandboxes", 46, 73, "BigCommerce Partner Portal provides Partner Use Sandboxes and Deal Registration Sandboxes with 500,000/hr rate limits.")
            e_rest = E("/rest-management", 26, 79, "BigCommerce API reference lists REST Admin (Catalog, Content, Management: Carts, Channels, Checkouts, Customers, Inventory, Orders, Pricing, Promotions, Shipping, Tax, Payments, B2B), GraphQL (Storefront, Admin, Account, B2B), and MCP (Store Management MCP Beta, Storefront MCP, WebMCP, Docs MCP Server).")
            e_price = E("/essentials/pricing/", 132, 184, "BigCommerce plans (Core $39/mo, Growth $105/mo, Scale $399/mo, Performance starting at $1,499/mo billed annually) offer 'Start free trial' on Core, Growth, and Scale.")
            e_llms = E("/llms.txt", 1, 10, "BigCommerce docs llms.txt publishes the official Docs MCP server endpoint at https://docs.bigcommerce.com/_mcp/server.")

            r["identity"]["resolution"] = claim(
                "identity",
                "BigCommerce SaaS ecommerce platform and developer APIs (REST Management, REST/GraphQL Storefront, GraphQL Admin/Account) documented at developer.bigcommerce.com.",
                [e_auth, e_rest],
            )
            r["purpose"] = claim(
                "purpose",
                "SaaS ecommerce platform exposing OAuth-secured REST Management and GraphQL Storefront/Admin APIs, Partner sandboxes, and official Docs/Storefront/Store Management MCP servers.",
                [e_auth, e_rest, e_llms],
            )
            items(
                r["auth"],
                [
                    auth("oauth_api_accounts", "oauth2",
                         "OAuth-based store-level, app-level (OAuth callback code exchange), and account-level API accounts issuing scoped access_token sent via X-Auth-Token header.",
                         [e_auth, e_hdr], "BigCommerce REST Management, GraphQL Admin/Account, and V3 APIs"),
                    auth("storefront_graphql_bearer", "bearer_token",
                         "Bearer token sent in Authorization: Bearer header for GraphQL Storefront API queries.",
                         [e_gql], "BigCommerce GraphQL Storefront API"),
                ],
                "Legacy Basic Auth API accounts are no longer issued to new stores; OAuth is required for V3 APIs.",
            )
            elig("testing", "sandbox_access", True, [e_sbx], "Partner Use Sandboxes and Deal Registration Sandboxes are available through the BigCommerce Partner Portal.")
            elig("testing", "trial_access", True, [e_price], "Core, Growth, and Scale plans offer a free trial ('Start free trial').")
            elig("testing", "partner_approval_required", True, [e_sbx], "Partner Use and Deal Registration sandboxes are created inside the BigCommerce Partner Portal.")
            elig("production", "paid_required", True, [e_price], "Production store plans (Core, Growth, Scale, Performance) require paid monthly/annual subscriptions.")
            elig("production", "self_serve", True, [e_auth], "Merchants can generate store-level API credentials directly in Settings > Store-level API accounts.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_auth, e_rest]),
                claim("api.protocol.graphql", "GraphQL", [e_gql, e_rest]),
            ], "Supports REST (Store Management, Storefront, B2B) and GraphQL (Storefront, Admin, Account, B2B).")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_auth, e_rest, e_gql])
            items(r["api_surface"]["resource_groups"], [
                group("catalog_inventory", "Catalog, inventory, pricing, price lists, and promotions", [e_rest]),
                group("orders_checkouts", "Orders, order operations, carts, checkouts, abandoned carts, shipping, tax, and payments", [e_rest]),
                group("customers_b2b", "Customers, customer segmentation, subscribers, and B2B", [e_rest]),
                group("channels_sites", "Channels, sites, scripts, webhooks, and store settings", [e_rest]),
            ], "Comprehensive REST and GraphQL resource groups listed in official navigation.")
            breadth("broad", ["catalog_inventory", "orders_checkouts", "customers_b2b", "channels_sites"], [e_rest],
                    "Covers catalog, inventory, pricing, orders/checkouts, customers/B2B, channels, shipping, tax, and payments.")

            set_mcp_entries([
                ("docs_mcp", "official", "BigCommerce Docs MCP Server", [e_llms], "/llms.txt",
                 "Official hosted callable MCP server for AI clients (Claude Code, Cursor, etc.) to search and read BigCommerce developer documentation.",
                 "https://docs.bigcommerce.com/_mcp/server", None),
                ("store_mcp_suite", "official", "BigCommerce Store Management MCP (Beta) / Storefront MCP / WebMCP", [e_rest], "/rest-management",
                 "Official BigCommerce MCP server family listed in the API reference for store management (beta), storefront, and WebMCP callable tools.",
                 None, None),
            ], [e_llms, e_rest])

            buildability(
                "build_now",
                "BigCommerce REST Management / GraphQL APIs and official MCP servers",
                ["Partner sandboxes require BigCommerce Partner Portal enrollment", "Production stores require paid plans (Core/Growth/Scale/Performance)"],
                ["Start a free trial store or request a Partner Use Sandbox", "Create a store-level API account (X-Auth-Token) or app-level OAuth client with scoped permissions"],
                [e_auth, e_hdr, e_sbx, e_rest, e_llms],
                ["identity", "auth.oauth_api_accounts", "testing.trial_access", "api.protocol.rest", "api.protocol.graphql", "mcp.discovery"],
                "Public REST/GraphQL docs, self-serve store-level API accounts, free trial stores, Partner sandboxes, and official MCP servers enable immediate building.",
            )

        # =====================================================================
        # 44. Salesforce Commerce Cloud
        # =====================================================================
        elif app == 44:
            e_price = E("/commerce/pricing/", 1, 110, "Salesforce Commerce Cloud pricing page lists commerce editions with 'Contact for pricing' and 'Contact your account executive' across tiers.")
            e_sdk = E("/commerce-sdk", 208, 232, "Official Salesforce Commerce SDK for Node.js interacts with Salesforce B2C Commerce platform APIs (SCAPI) including Shopper Products, Shopper Context, and SLAS.")
            e_sdk_auth = E("/commerce-sdk", 307, 329, "SLAS (ShopperLogin) obtains OAuth 2.0 client_credentials JWT access token passed in the Authorization: Bearer header for Shopper API calls.")
            e_iso = E("/commerce-sdk-isomorphic", 213, 387, "Official commerce-sdk-isomorphic provides Browser & Node.js client for B2C Commerce Shopper APIs (ShopperLogin, ShopperSearch, ShopperProducts) and B2C Commerce Custom APIs (callCustomEndpoint) using Bearer tokens.")
            e_tool = E("/b2c-developer-tooling", 1, 353, "Official SalesforceCommerceCloud/b2c-developer-tooling repository provides b2c-cli, b2c-tooling-sdk (OAuth, API Key, Basic auth strategies; MRT and ODS clients), and b2c-dx-mcp (official MCP server for B2C Commerce developer experience tools including MCP docs_*, MCP validate_xml_schema, and B2C_INSTANCE=my-sandbox tooling).")

            r["identity"]["resolution"] = claim(
                "identity",
                "Salesforce Commerce Cloud (B2C Commerce / Agentforce Commerce B2C) enterprise ecommerce platform and SCAPI SDK/CLI/MCP tooling.",
                [e_price, e_sdk, e_tool],
            )
            r["purpose"] = claim(
                "purpose",
                "Enterprise B2C ecommerce platform providing SCAPI Shopper and Admin APIs via Node.js/isomorphic SDKs, B2C CLI, and official b2c-dx-mcp developer MCP server.",
                [e_sdk, e_iso, e_tool],
            )
            items(
                r["auth"],
                [
                    auth("slas_oauth2_jwt", "oauth2",
                         "Shopper Login and API Access Service (SLAS) OAuth 2.0 client_credentials grant issuing JWT access tokens sent via Authorization: Bearer header.",
                         [e_sdk_auth, e_iso], "B2C Commerce Shopper APIs (SCAPI)"),
                    auth("b2c_tooling_auth", "other",
                         "B2C Tooling SDK supports OAuth, API Key, and Basic authentication strategies for B2C Commerce developer/instance operations (MRT/ODS/WebDAV).",
                         [E("/b2c-developer-tooling", 319, 321, "b2c-tooling-sdk auth module implements OAuth, API Key, and Basic authentication strategies for MRT and ODS clients.")],
                         "B2C CLI / Tooling SDK operations"),
                ],
                "developer.salesforce.com/docs/commerce/commerce-api/guide/* returned HTTP 403 (blocked); auth findings are grounded in official SalesforceCommerceCloud GitHub repositories.",
            )
            elig("production", "contact_sales_required", True, [e_price], "Salesforce Commerce Cloud pricing page directs buyers to 'Contact for pricing' and 'Contact your account executive'.")
            elig("production", "paid_required", True, [e_price], "Enterprise Salesforce Commerce Cloud licensing is commercial/sales-quoted with no free production tier listed.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_sdk, e_iso]),
                claim("api.protocol.sdk", "SDK", [e_sdk, e_iso]),
                claim("api.protocol.cli", "CLI", [e_tool]),
            ], "SCAPI REST APIs accessed via official commerce-sdk, commerce-sdk-isomorphic, and b2c-cli.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", None,
                [e_sdk], "unknown", (),
                "Official GitHub SDK/CLI repos are public, but developer.salesforce.com/docs/commerce/commerce-api/guide/* returned HTTP 403 to automated capture; full doc accessibility is left unknown rather than inferred.",
            )
            items(r["api_surface"]["resource_groups"], [
                group("shopper_catalog_search", "Shopper Products, Shopper Search, and Shopper Context", [e_sdk, e_iso]),
                group("shopper_login_custom", "Shopper Login (SLAS) and B2C Commerce Custom APIs", [e_sdk_auth, e_iso]),
                group("admin_mrt_ods", "Admin APIs, Managed Runtime (MRT), and On-Demand Sandboxes (ODS) tooling", [e_iso, E("/b2c-developer-tooling", 319, 321, "Tooling SDK includes MRT and ODS platform clients.")]),
            ], "Resource groups observed across official SalesforceCommerceCloud SDK and tooling repositories.")
            breadth("moderate", ["shopper_catalog_search", "shopper_login_custom", "admin_mrt_ods"], [e_sdk, e_iso, e_tool],
                    "Captured official SDK/tooling repos establish Shopper APIs (Products, Search, Context, Login), Custom APIs, and Admin/MRT/ODS tooling; full SCAPI Admin catalog was blocked by HTTP 403 on developer.salesforce.com.")

            set_mcp_entries([
                ("b2c_dx_mcp", "official", "Salesforce B2C DX MCP Server (b2c-dx-mcp)", [e_tool], "/b2c-developer-tooling",
                 "Official callable MCP server in SalesforceCommerceCloud/b2c-developer-tooling providing B2C Commerce developer experience tools (docs search/read, XML schema validation, sandbox tooling).",
                 None, "https://github.com/SalesforceCommerceCloud/b2c-developer-tooling"),
            ], [e_tool])

            buildability(
                "outreach_required",
                "Salesforce B2C Commerce API (SCAPI) and official b2c-dx-mcp integration",
                ["Enterprise licensing requires contacting Salesforce sales/account executive", "developer.salesforce.com SCAPI guide pages returned HTTP 403 during capture, leaving self-serve sandbox eligibility unverified"],
                ["Obtain licensed B2C Commerce tenant/sandbox credentials and SLAS/Account Manager OAuth client IDs via customer or Salesforce partner channel", "Use official commerce-sdk / b2c-developer-tooling repos"],
                [e_price, e_sdk, e_tool],
                ["identity", "auth.slas_oauth2_jwt", "production.contact_sales_required", "api.protocol.sdk", "mcp.discovery"],
                "Official SDKs, CLI, and b2c-dx-mcp exist, but commercial licensing requires sales engagement and no self-serve public sandbox path was established in captured sources.",
            )

        # =====================================================================
        # 45. Magento (Adobe Commerce)
        # =====================================================================
        elif app == 45:
            e_rest = E("/webapi/rest/", 1, 42, "Adobe Commerce (PaaS / on-premises / Magento Open Source) and Adobe Commerce as a Cloud Service (SaaS) provide REST APIs; PaaS supports OAuth 1.0a, tokens, and login credentials, while SaaS requires Adobe IMS Authorization: Bearer tokens.")
            e_gql = E("/webapi/graphql/", 1, 13, "Adobe Commerce and Magento Open Source provide GraphQL APIs (core and B2B schemas for PaaS; supergraph for SaaS).")
            e_auth = E("/get-started/authentication/", 31, 97, "Adobe Commerce PaaS/Magento Open Source web APIs support Token-based Bearer authentication (admin/customer token service), OAuth-based third-party integration auth, and session cookie authentication, with ACL permissions (e.g., Magento_Customer::customer, Magento_Customer::manage).")
            e_gh = E("/magento/magento2", 203, 235, "Magento Open Source is open-source ecommerce software licensed under OSL 3.0; Adobe Commerce is the commercial cloud/enterprise edition.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Magento Open Source (OSL 3.0) and Adobe Commerce (PaaS on Cloud/on-premises and SaaS Cloud Service) ecommerce platforms documented at developer.adobe.com/commerce.",
                [e_rest, e_gh],
            )
            r["purpose"] = claim(
                "purpose",
                "Open-source (Magento Open Source) and enterprise (Adobe Commerce PaaS/SaaS) ecommerce platform with REST and GraphQL APIs for catalog, customer, and store operations.",
                [e_rest, e_gql, e_gh],
            )
            items(
                r["auth"],
                [
                    auth("paas_bearer_token", "bearer_token",
                         "Admin or customer token obtained from the Magento token service and passed in the Authorization: Bearer header (PaaS / Magento Open Source).",
                         [e_auth], "Adobe Commerce PaaS and Magento Open Source REST/GraphQL"),
                    auth("paas_oauth1a", "other",
                         "OAuth 1.0a authentication for third-party integrations registered in Adobe Commerce (PaaS / Magento Open Source).",
                         [e_rest, e_auth], "Third-party integrations on Adobe Commerce PaaS / Magento Open Source"),
                    auth("paas_session_cookie", "session_cookie",
                         "Session-based cookie authentication for storefront or Admin JavaScript widgets.",
                         [e_auth], "Storefront or Admin session widgets"),
                    auth("saas_adobe_ims_bearer", "oauth2",
                         "Adobe Identity Management Service (IMS) interactive user-based and automated server-to-server authentication passing Authorization: Bearer <token> (Adobe Commerce as a Cloud Service SaaS).",
                         [e_rest], "Adobe Commerce as a Cloud Service (SaaS) REST API"),
                ],
                "PaaS/Open Source uses OAuth 1.0a, Bearer tokens, and session cookies; SaaS requires Adobe IMS Bearer tokens.",
            )
            elig("testing", "free_access", True, [e_gh], "Magento Open Source (OSL 3.0) is freely available on GitHub for local/self-hosted development and testing.")
            elig("testing", "self_serve", True, [e_gh, e_auth], "Developers can self-host Magento Open Source and configure Admin/Integration tokens or OAuth credentials.")
            elig("production", "free_access", True, [e_gh], "Magento Open Source is licensed under OSL 3.0 without commercial license fees (separate from paid Adobe Commerce).")
            elig("production", "admin_approval_required", True, [e_auth], "Administrator defines ACL resource permissions in the Admin tree for admin users or registered integrations.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_rest]),
                claim("api.protocol.graphql", "GraphQL", [e_gql]),
            ], "Both REST and GraphQL APIs are documented across PaaS/Open Source and SaaS editions.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_rest, e_gql, e_auth])
            items(r["api_surface"]["resource_groups"], [
                group("customers_accounts", "Customers, customer accounts, and customer groups (REST /V1/customers, /V1/customerGroups)", [e_auth]),
                group("storefront_shopping_crm_erp", "Storefront shopping, guest/customer commerce workflows, and CRM/ERP backend integrations", [e_rest]),
                group("graphql_core_b2b", "GraphQL core and B2B commerce schemas", [e_gql]),
            ], "Resource groups observed in captured Adobe Commerce REST, GraphQL, and authentication documentation.")
            breadth("moderate", ["customers_accounts", "storefront_shopping_crm_erp", "graphql_core_b2b"], [e_rest, e_gql, e_auth],
                    "Captured overview docs establish REST and GraphQL across customer management, shopping/storefront, B2B schemas, and CRM/ERP integration; Adobe Commerce commercial pricing page timed out.")

            set_mcp_not_found(
                [e_rest, e_gql, e_gh],
                "No official or community MCP server was found in the checked developer.adobe.com/commerce/webapi/* or github.com/magento/magento2 pages.",
            )

            buildability(
                "conditional",
                "Magento Open Source / Adobe Commerce REST and GraphQL API integration",
                ["Distinct auth stacks between PaaS/Open Source (token/OAuth 1.0a) and SaaS (Adobe IMS OAuth 2.0)", "Commercial Adobe Commerce pricing/licensing page timed out during capture; enterprise SaaS access requires Adobe Commerce licensing"],
                ["Target Magento Open Source self-hosted instance for free development/testing", "Implement Bearer token/OAuth 1.0a for PaaS or Adobe IMS Bearer auth for SaaS"],
                [e_rest, e_gql, e_auth, e_gh],
                ["identity", "auth.paas_bearer_token", "auth.saas_adobe_ims_bearer", "testing.free_access", "api.protocol.rest", "api.protocol.graphql"],
                "Magento Open Source is freely buildable via public REST/GraphQL docs, while Adobe Commerce SaaS/Cloud commercial access and edition-specific auth paths make overall buildability conditional on target edition.",
            )

        # =====================================================================
        # 46. Squarespace
        # =====================================================================
        elif app == 46:
            e_ov = E("/commerce-apis", 1, 64, "Squarespace Developer Platform Commerce APIs expose https://api.squarespace.com endpoints (Products, Inventory, Orders, Transactions, Profiles, Contacts, WebhookSubscriptions) authenticated via Authorization: Bearer API key or OAuth access token.")
            e_ap = E("/authentication-and-permissions", 28, 85, "Squarespace Commerce APIs support generated API keys (requires Commerce Advanced plan; never expire while site is active) and OAuth 2.0 (required for Squarespace Extensions, which undergo OAuth client review and approval).")
            e_oa = E("/oauth", 50, 115, "Squarespace OAuth 2.0 authorization code flow uses https://login.squarespace.com/api/1/login/oauth/provider/authorize with scopes (including website.inventory, website.orders, website.contacts, website.contacts.read) and optional access_type=offline.")
            e_ord = E("/orders-overview", 48, 65, "Orders API (GET /1.0/commerce/orders) supports paymentStates filtering (NOT_CHARGED, AUTHORIZED, PAID, REFUNDED, PARTIALLY_PAID) and order.create webhooks.")
            e_price = E("/pricing", 319, 396, "Squarespace website/commerce plans include Basic, Core, and Advanced with 'Start Free Trial' and paid subscriptions.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Squarespace website and ecommerce platform with Commerce APIs documented at developers.squarespace.com.",
                [e_ov, e_price],
            )
            r["purpose"] = claim(
                "purpose",
                "Website and ecommerce platform exposing REST Commerce APIs for products, inventory, orders, transactions, contacts/profiles, discounts, and webhooks.",
                [e_ov, e_ap],
            )
            items(
                r["auth"],
                [
                    auth("api_key_bearer", "api_key",
                         "Merchant-generated Developer API Key (Settings > Advanced > Developer API Keys) sent as Authorization: Bearer <token>; requires Commerce Advanced plan and does not expire while site is active.",
                         [e_ov, e_ap], "Custom applications on a single Squarespace merchant site",
                         scopes=["CONTACT_READONLY", "CONTACT"]),
                    auth("oauth2_extensions", "oauth2",
                         "OAuth 2.0 authorization code flow via login.squarespace.com/api/1/login/oauth/provider/authorize (required for Squarespace Extensions; supports offline access_type and Webhook Subscriptions API).",
                         [e_ap, e_oa], "Multi-merchant Squarespace Extensions and registered OAuth clients",
                         scopes=["website.inventory", "website.orders", "website.contacts.read", "website.contacts"]),
                ],
                "Webhook Subscriptions API is OAuth-only; Profiles API is in maintenance mode in favor of Contacts API.",
            )
            elig("testing", "trial_access", True, [e_price], "Squarespace pricing page offers 'Start Free Trial' across Basic, Core, and Advanced plans.")
            elig("production", "paid_required", True, [e_ap, e_price], "Custom application API keys explicitly require Squarespace's Commerce Advanced plan; production sites require paid plans (Basic, Core, Advanced).")
            elig("production", "self_serve", True, [e_ap], "Merchants on the Commerce Advanced plan can self-serve generate Developer API Keys in Settings > Advanced > Developer API Keys.")
            elig("production", "vendor_approval_required", True, [e_ap], "Registering a Squarespace OAuth client requires review and approval by Squarespace (and listing in Squarespace Extensions is a separate process).")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_ov, e_ord]),
            ], "REST HTTP JSON APIs under https://api.squarespace.com.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_ov, e_ap, e_oa, e_ord])
            items(r["api_surface"]["resource_groups"], [
                group("products_inventory", "Products API and Inventory API", [e_ov, e_ap]),
                group("orders_transactions", "Orders API and Transactions API", [e_ov, e_ap, e_ord]),
                group("contacts_profiles_discounts", "Contacts API, Profiles API (maintenance mode), Discounts API, and Forms API", [e_ov, e_ap]),
                group("webhooks", "Webhook Subscriptions API (OAuth only)", [e_ov, e_ap]),
            ], "All Commerce API resource groups listed in official documentation.")
            breadth("broad", ["products_inventory", "orders_transactions", "contacts_profiles_discounts", "webhooks"], [e_ov, e_ap],
                    "Covers catalog/inventory, orders/transactions, contacts/profiles/discounts/forms, and webhook subscriptions.")

            set_mcp_unknown(
                [E("/commerce-apis", 1, 4, "Top navigation on developers.squarespace.com lists 'MCP' alongside 'Commerce APIs' and 'Reseller APIs', but no MCP documentation page was captured.")],
                "developers.squarespace.com top navigation includes an 'MCP' link, but the MCP page itself was not captured in this pass; left unknown rather than assuming scope or availability.",
            )

            buildability(
                "conditional",
                "Squarespace Commerce REST API integration (API key for Commerce Advanced or OAuth for Extensions)",
                ["Custom API key generation requires Squarespace's Commerce Advanced plan", "Multi-merchant OAuth client registration requires Squarespace review and approval", "Webhook Subscriptions API is OAuth-only"],
                ["Use a Commerce Advanced plan for single-site API key integrations, or submit an OAuth client application for multi-merchant/webhook support", "Inspect the developers.squarespace.com MCP section in a follow-up pass"],
                [e_ov, e_ap, e_oa, e_price],
                ["identity", "auth.api_key_bearer", "auth.oauth2_extensions", "production.paid_required", "production.vendor_approval_required", "api.protocol.rest"],
                "Public REST docs and self-serve API keys exist, but plan-tier gating (Commerce Advanced) for API keys and vendor review for OAuth clients make buildability conditional.",
            )

        # =====================================================================
        # 47. Ecwid
        # =====================================================================
        elif app == 47:
            e_ov = E("rest-api/overview", 43, 84, "Ecwid (Lightspeed) REST API manages store profile, orders, abandoned carts, products, categories, customers, discounts/coupons, shipping, and payment options using OAuth 2.0 authorization simplified for single-store customizations (600 requests/min per token).")
            e_ref = E("reference/overview", 23, 103, "Ecwid developer portal documents private and public Ecwid apps, REST API, Storefronts JS API (cart/checkout/customers), Webhooks, Payment API, and Shipping API.")
            e_price = E("/pricing", 127, 182, "Ecwid pricing lists paid monthly/annual tiers: Starter ($5/mo), Venture ($35/mo monthly / $29/mo annual; includes Access to App Market), Business ($65/$49), and Unlimited ($149/$119).")

            r["identity"]["resolution"] = claim(
                "identity",
                "Ecwid by Lightspeed ecommerce platform and REST/JS developer APIs documented at docs.ecwid.com and api-docs.ecwid.com.",
                [e_ov, e_ref],
            )
            r["purpose"] = claim(
                "purpose",
                "Embeddable ecommerce platform (by Lightspeed) with OAuth 2.0 REST API, Storefronts JS API, webhooks, and Payment/Shipping APIs.",
                [e_ov, e_ref],
            )
            items(
                r["auth"],
                [
                    auth("oauth2_rest", "oauth2",
                         "OAuth 2.0 authorization simplified for single-store customizations and used for private and public Ecwid apps (rate-limited at 600 requests per minute per token).",
                         [e_ov, e_ref], "Ecwid REST API for private and public apps"),
                ],
                "Specific OAuth token endpoint page returned HTTP 404 (docs.ecwid.com/api-reference/rest-api/authentication); OAuth 2.0 model is confirmed on the REST API overview.",
            )
            elig("production", "paid_required", True, [e_price], "Ecwid pricing page lists paid tiers starting at Starter ($5/mo), with Access to App Market starting on Venture ($29/mo annual / $35/mo monthly); no free tier is listed on the current pricing page.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_ov]),
                claim("api.protocol.sdk", "SDK", [e_ref]),
            ], "REST API and Storefronts JS API are documented.")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_ov, e_ref])
            items(r["api_surface"]["resource_groups"], [
                group("orders_carts", "Orders, abandoned carts, and checkout extra fields", [e_ov]),
                group("products_categories", "Products, product variations, reviews, and categories", [e_ov]),
                group("customers_discounts", "Customers, customer groups, promotions, and discount coupons", [e_ov]),
                group("store_shipping_payment_webhooks", "Store profile/reports, staff accounts, shipping/payment options, Payment/Shipping APIs, and webhooks", [e_ov, e_ref]),
            ], "Resource groups observed in Ecwid REST API overview and reference portal.")
            breadth("broad", ["orders_carts", "products_categories", "customers_discounts", "store_shipping_payment_webhooks"], [e_ov, e_ref],
                    "Covers orders/carts, products/categories, customers/discounts, store profile/staff, shipping/payments, and webhooks.")

            set_mcp_not_found(
                [e_ov, e_ref],
                "No official or community MCP server was found in the checked docs.ecwid.com and api-docs.ecwid.com documentation pages.",
            )

            buildability(
                "conditional",
                "Ecwid by Lightspeed REST API and Storefronts JS API integration",
                ["Current pricing page lists paid tiers starting at Starter ($5/mo) with App Market access on Venture+; free/sandbox developer store eligibility was not confirmed in captured docs", "Detailed OAuth token exchange page returned HTTP 404 and needs follow-up capture"],
                ["Capture the active Ecwid OAuth / custom app setup guide from docs.ecwid.com", "Verify whether a free developer test store is available or provision a Starter/Venture store"],
                [e_ov, e_ref, e_price],
                ["identity", "auth.oauth2_rest", "production.paid_required", "api.protocol.rest"],
                "Public REST API documentation and OAuth 2.0 model are established, but missing captured token-exchange/sandbox details and paid plan tiers make buildability conditional.",
            )

        # =====================================================================
        # 48. Gumroad
        # =====================================================================
        elif app == 48:
            e_price = E("/pricing", 7, 43, "Gumroad pricing has no monthly charges; charges 10% + $0.50 per direct transaction (30% via Discover) and acts as merchant of record for global sales tax.")
            e_repo = E("/antiwork/gumroad", 268, 268, "Gumroad is an e-commerce platform enabling creators to sell products directly to consumers (open-source web application at github.com/antiwork/gumroad).")
            e_cli = E("/antiwork/gumroad-cli", 172, 256, "Official Antiwork Gumroad CLI (github.com/antiwork/gumroad-cli) authenticates via OAuth device/browser authorization (gumroad auth login) or GUMROAD_ACCESS_TOKEN, manages user, products, sales, files, subscribers, payouts, licenses, offercodes, and webhooks, and runs an MCP server via 'gumroad mcp'.")
            e_cmcp = E("/rmarescu/gumroad-mcp", 156, 226, "Community MCP server rmarescu/gumroad-mcp connects AI clients to the Gumroad API using a generated Gumroad access token, exposing tools for products, sales, and offer codes.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Gumroad creator ecommerce platform (operated by Antiwork, open-source repo at github.com/antiwork/gumroad) with official CLI/MCP and REST API.",
                [e_repo, e_price],
            )
            r["purpose"] = claim(
                "purpose",
                "Creator ecommerce and merchant-of-record platform for digital products and memberships, with OAuth/token API, official Antiwork CLI (`gumroad mcp`), and community MCP server.",
                [e_repo, e_price, e_cli],
            )
            items(
                r["auth"],
                [
                    auth("oauth_device_browser", "oauth2",
                         "OAuth device authorization (`gumroad auth login`) and local browser OAuth (`gumroad auth login --web`) storing a seller access token.",
                         [e_cli], "Official Gumroad CLI / OAuth seller authentication"),
                    auth("seller_access_token", "bearer_token",
                         "Seller access token supplied via GUMROAD_ACCESS_TOKEN (or piped via `gumroad auth login --with-token`) for non-interactive API/CLI/MCP calls.",
                         [e_cli], "Gumroad API seller access token"),
                ],
                "gumroad.com/api and help.gumroad.com/article/280-create-application-api returned 1-line JS shells and are excluded from citations; auth is grounded in official antiwork/gumroad-cli.",
            )
            elig("testing", "free_access", True, [e_price], "Gumroad has no monthly subscription charges; fees are deducted only per sale.")
            elig("testing", "self_serve", True, [e_cli], "Creators/developers can authenticate self-serve via `gumroad auth login` or supply `GUMROAD_ACCESS_TOKEN`.")
            elig("production", "free_access", True, [e_price], "No monthly platform fee; Gumroad charges 10% + $0.50 per direct sale (30% via Discover).")
            elig("production", "paid_required", False, [e_price], "No upfront or monthly subscription fee is required to operate a Gumroad account (transaction fees apply on sales).")
            elig("production", "self_serve", True, [e_cli], "Seller OAuth login and access tokens are self-serve without sales or partner gating.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_cli]),
                claim("api.protocol.cli", "CLI", [e_cli]),
            ], "Gumroad API accessed via HTTP REST and official antiwork/gumroad-cli (`--json`, `--jq`).")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", None,
                [e_cli], "unknown", (),
                "Official antiwork/gumroad-cli and antiwork/gumroad repos are public, but gumroad.com/api rendered only a 1-line JS shell to non-JS HTTP capture.",
            )
            items(r["api_surface"]["resource_groups"], [
                group("products_files_offercodes", "Products, files, and offer codes", [e_cli]),
                group("sales_payouts_subscribers", "Sales, refunds, payouts, and subscribers", [e_cli]),
                group("licenses_webhooks", "Licenses, user info, and webhooks", [e_cli]),
            ], "Resource groups established from official antiwork/gumroad-cli command surface.")
            breadth("moderate", ["products_files_offercodes", "sales_payouts_subscribers", "licenses_webhooks"], [e_cli],
                    "Covers creator catalog/offer codes, sales/payouts/subscribers, and licenses/webhooks.")

            set_mcp_entries([
                ("official_gumroad_cli_mcp", "official", "Gumroad CLI MCP Server (`gumroad mcp`)", [e_cli], "/antiwork/gumroad-cli",
                 "Official callable local MCP server built into antiwork/gumroad-cli (`gumroad mcp`) for querying and managing Gumroad seller data.",
                 None, "https://github.com/antiwork/gumroad-cli"),
                ("community_gumroad_mcp", "community", "rmarescu/gumroad-mcp", [e_cmcp], "/rmarescu/gumroad-mcp",
                 "Community callable local stdio MCP server exposing tools for Gumroad products, sales, and offer codes via GUMROAD_ACCESS_TOKEN.",
                 None, "https://github.com/rmarescu/gumroad-mcp"),
            ], [e_cli, e_cmcp])

            buildability(
                "build_now",
                "Gumroad API, official antiwork/gumroad-cli (`gumroad mcp`), and community MCP integration",
                ["gumroad.com/api web docs require JavaScript rendering for direct reading"],
                ["Authenticate with `gumroad auth login` or generate a seller access token", "Integrate via official `gumroad mcp` / `gumroad-cli` or REST endpoints"],
                [e_price, e_cli],
                ["identity", "auth.oauth_device_browser", "auth.seller_access_token", "production.paid_required", "api.protocol.cli", "mcp.discovery"],
                "Zero monthly fee, self-serve OAuth/access-token auth, official CLI with built-in `gumroad mcp`, and community MCP support immediate building.",
            )

        # =====================================================================
        # 49. Amazon Selling Partner
        # =====================================================================
        elif app == 49:
            e_what = E("/what-is-the-selling-partner-api", 600, 617, "Amazon Selling Partner API (SP-API) is a REST-based API enabling Amazon sellers and vendors to automate orders, shipments, payments, inventory, listings, pricing, fulfillment, notifications, and tax/invoice workflows, with SDK generation, sandbox, and Data Kiosk API.")
            e_reg = E("/registering-as-a-developer", 600, 622, "Developers must register as an SP-API developer (submitting a developer profile with security control questions and role requests) before registering an application; private seller apps require a Professional selling account (Individual accounts ineligible), and public developers must list apps in the Selling Partner Appstore.")
            e_conn = E("/connecting-to-the-selling-partner-api", 604, 680, "SP-API uses Login with Amazon (LWA) OAuth 2.0 at https://api.amazon.com/auth/o2/token (refresh_token grant for selling-partner authorized calls; client_credentials grant with scope for grantless operations), passing the 1-hour LWA access token in the x-amz-access-token header (or RDT for restricted PII operations).")
            e_sbx = E("/the-selling-partner-api-sandbox", 716, 761, "SP-API provides hosted static and dynamic sandboxes across NA/EU/FE endpoints (e.g., https://sandbox.sellingpartnerapi-na.amazon.com) plus a local sample AI sandbox.")
            e_toolkit = E("/selling-partner-agentic-toolkit", 156, 195, "Official amzn/selling-partner-agentic-toolkit connects AI assistants to the official Amazon Selling Partner Connector (MCP) hosted at https://sellingpartner-ai.amazon.com/mcp, authorized via Seller Central OAuth consent flow with human-in-the-loop approval for writes.")
            e_cmcp = E("/jay-trivedi/amazon_sp_mcp", 168, 275, "Community MCP server jay-trivedi/amazon_sp_mcp connects AI agents to Amazon Seller Central via SP-API using LWA OAuth 2.0 (Client ID, Client Secret, Refresh Token) for sales, inventory, listings, and reports.")

            r["identity"]["resolution"] = claim(
                "identity",
                "Amazon Selling Partner API (SP-API) for Amazon sellers and vendors, documented at developer-docs.amazon.com/sp-api.",
                [e_what],
            )
            r["purpose"] = claim(
                "purpose",
                "Amazon's REST-based Selling Partner API (SP-API) for automating seller and vendor orders, inventory, listings, fulfillment, payments, and analytics, with official Selling Partner Connector MCP.",
                [e_what, e_toolkit],
            )
            items(
                r["auth"],
                [
                    auth("lwa_oauth2_refresh", "oauth2",
                         "Login with Amazon (LWA) OAuth 2.0 refresh_token grant at https://api.amazon.com/auth/o2/token exchanging client_id, client_secret, and refresh_token for a 1-hour LWA access token sent in the x-amz-access-token header (RDT used for restricted PII operations).",
                         [e_conn], "Selling-partner authorized SP-API operations"),
                    auth("lwa_oauth2_client_credentials", "oauth2",
                         "Login with Amazon (LWA) OAuth 2.0 client_credentials grant for grantless operations with explicit LWA scopes.",
                         [e_conn], "Grantless SP-API operations (Notifications, Application Management, Tracking)",
                         scopes=["sellingpartnerapi::notifications", "sellingpartnerapi::client_credential:rotation", "sellingpartnerapi::shipments:track"]),
                ],
                "Legacy onboarding-as-a-developer and connect-to-the-sp-api URLs returned 'Page Not Found' and are excluded; active SP-API docs confirm LWA OAuth 2.0.",
            )
            elig("testing", "sandbox_access", True, [e_what, e_sbx], "Hosted static and dynamic SP-API sandboxes (NA/EU/FE endpoints) and a local sample AI sandbox are documented.")
            elig("testing", "vendor_approval_required", True, [e_reg], "Developers must complete SP-API developer registration and profile/security review before registering applications.")
            elig("production", "paid_required", True, [e_reg], "Private seller SP-API apps require a Professional selling account in Seller Central (Individual accounts are not eligible).")
            elig("production", "vendor_approval_required", True, [e_reg], "SP-API developer registration requires submitting a developer profile with security control answers and role approval; public apps must list in the Amazon Selling Partner Appstore.")
            elig("production", "admin_approval_required", True, [e_reg], "You must be a primary account user to complete SP-API developer registration.")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.rest", "REST", [e_what, e_conn]),
                claim("api.protocol.sdk", "SDK", [e_what]),
            ], "REST-based SP-API with OpenAPI models and generated SDKs (C#, Java, JavaScript, Python).")
            r["api_surface"]["public_documentation"] = claim("api.public_docs", True, [e_what, e_reg, e_conn, e_sbx])
            items(r["api_surface"]["resource_groups"], [
                group("orders_fulfillment", "Orders, shipping confirmations, tracking, and fulfillment (including Vendor Direct Fulfillment)", [e_what]),
                group("listings_inventory_pricing", "Listings, catalog items, multi-warehouse inventory, and pricing", [e_what, e_conn]),
                group("finance_reports_notifications", "Payments, financial transactions, tax/invoices, Data Kiosk analytics, and event notifications", [e_what]),
            ], "Extensive seller and vendor SP-API domains documented.")
            breadth("broad", ["orders_fulfillment", "listings_inventory_pricing", "finance_reports_notifications"], [e_what],
                    "Covers orders/fulfillment, listings/catalog/inventory/pricing, finance/tax/invoices, analytics (Data Kiosk), and notifications across Seller and Vendor accounts.")

            set_mcp_entries([
                ("amazon_sp_connector_mcp", "official", "Amazon Selling Partner Connector (MCP)", [e_toolkit], "/selling-partner-agentic-toolkit",
                 "Official hosted callable MCP server at https://sellingpartner-ai.amazon.com/mcp authorized via Seller Central OAuth consent flow for inventory, sales/traffic analytics, listing issues, and human-in-the-loop drafted writes.",
                 "https://sellingpartner-ai.amazon.com/mcp", "https://github.com/amzn/selling-partner-agentic-toolkit"),
                ("community_amazon_sp_mcp", "community", "jay-trivedi/amazon_sp_mcp", [e_cmcp], "/jay-trivedi/amazon_sp_mcp",
                 "Community callable local MCP server connecting AI agents to Amazon Seller Central via SP-API LWA OAuth 2.0 for sales, inventory, listings, and reports.",
                 None, "https://github.com/jay-trivedi/amazon_sp_mcp"),
            ], [e_toolkit, e_cmcp])

            buildability(
                "conditional",
                "Amazon Selling Partner API (SP-API) and official Amazon Selling Partner Connector MCP",
                ["Requires SP-API developer registration, security control review, and role approval by Amazon", "Private seller apps require a Professional Seller Central account and primary account user", "Public apps must list in the Amazon Selling Partner Appstore"],
                ["Register as a public or private SP-API developer and complete Amazon's developer profile/security review", "Test against hosted SP-API sandbox endpoints using LWA OAuth 2.0 or evaluate the official Selling Partner Connector MCP"],
                [e_what, e_reg, e_conn, e_sbx, e_toolkit],
                ["identity", "auth.lwa_oauth2_refresh", "testing.sandbox_access", "production.vendor_approval_required", "api.protocol.rest", "mcp.discovery"],
                "Public REST docs, OpenAPI models, hosted sandboxes, and official hosted MCP exist, but mandatory Amazon developer/role approval and Professional account prerequisites make buildability conditional.",
            )

        # =====================================================================
        # 50. fanbasis (rebranded to Commas)
        # =====================================================================
        elif app == 50:
            e_home = E("www.fanbasis.com/", 1, 18, "www.fanbasis.com displays 'FanBasis is now Commas!' (Commas Inc.) — one platform to create, sell, and get paid with checkouts, funnels, communities, courses, webinars, and affiliates.")
            e_ent = E("www.fanbasis.com/", 41, 60, "Commas Payments & Enterprise/APIs offers cards/wallets/BNPL payments, subscriptions, embedded checkouts, multi-rail payouts, APIs, and SDKs, plus a beta MCP integration ('Run Commas from your AI assistant. Create checkout links, issue refunds and pull your numbers in plain English.').")
            e_gate = E("dev-docs.fanbasis.com/", 1, 6, "dev-docs.fanbasis.com ('Login - FanBasis API Docsv3') is gated behind a password login screen ('Sign in to access API Docs').")

            r["identity"]["resolution"] = claim(
                "identity",
                "FanBasis (officially rebranded to Commas / Commas Inc.; www.fanbasis.com serves 'FanBasis is now Commas!').",
                [e_home],
            )
            r["purpose"] = claim(
                "purpose",
                "Creator and digital business commerce platform (FanBasis, now Commas) combining checkouts, funnels, courses, communities, webinars, BNPL payments, APIs/SDKs, and beta MCP.",
                [e_home, e_ent],
            )
            items(
                r["auth"],
                [],
                "Authentication mechanism details are unknown from public captured sources: dev-docs.fanbasis.com is password-gated and commasdocs.com rendered only a 2-line JS 'Unpacking...' shell.",
                cov="partial",
            )
            # Credential eligibility fields remain honestly unknown because public pricing/API docs were not readable without login/JS
            elig("testing", "sandbox_access", None, [e_gate], "Unknown: dev-docs.fanbasis.com is password-gated and commasdocs.com rendered only a JS unpacking shell.", status="unknown")
            elig("production", "self_serve", None, [e_gate], "Unknown: API credential provisioning rules could not be verified from password-gated dev-docs.fanbasis.com or JS-shell commasdocs.com.", status="unknown")

            items(r["api_surface"]["protocols"], [
                claim("api.protocol.sdk", "SDK", [e_ent]),
            ], "Homepage confirms 'APIs and SDKs', while specific wire protocol (e.g., REST/GraphQL) and endpoint reference are behind password-gated dev-docs.fanbasis.com / JS-shell commasdocs.com.")
            r["api_surface"]["public_documentation"] = claim(
                "api.public_docs", False,
                [e_gate], "observed", (),
                "Legacy FanBasis API Docsv3 at dev-docs.fanbasis.com requires a password login ('Sign in to access API Docs'); commasdocs.com rendered only a 2-line JS 'Unpacking...' shell.",
            )
            items(r["api_surface"]["resource_groups"], [
                group("checkouts_payouts_refunds", "Embedded checkouts, checkout links, multi-rail payouts, and refunds", [e_ent]),
            ], "Only high-level capabilities stated on the official homepage are recorded; full endpoint groups remain unknown pending accessible API docs.")
            r["api_surface"]["breadth"] = claim(
                "api.breadth", None, [e_gate], "unknown", (),
                "Insufficient public API endpoint documentation captured (dev-docs.fanbasis.com is password-gated and commasdocs.com is a JS unpacking shell).",
            )

            set_mcp_entries([
                ("commas_mcp_beta", "official", "Commas MCP (Beta)", [e_ent], "www.fanbasis.com/",
                 "Official beta callable MCP server described on www.fanbasis.com to run Commas from an AI assistant: create checkout links, issue refunds, and pull numbers in plain English.",
                 None, None),
            ], [e_ent])

            buildability(
                "outreach_required",
                "FanBasis / Commas API, SDK, and beta MCP integration",
                ["dev-docs.fanbasis.com (FanBasis API Docsv3) is password-protected behind a login screen", "commasdocs.com rendered only a JS unpacking shell without readable auth/endpoint reference in non-JS capture", "Pricing, auth method, and sandbox/production credential paths remain unverified from captured public docs"],
                ["Request API documentation access / credentials from Commas (formerly FanBasis) or inspect commasdocs.com in an interactive browser session", "Confirm API key/OAuth setup and beta MCP endpoint onboarding requirements"],
                [e_home, e_ent, e_gate],
                ["identity", "api.public_docs", "api.protocol.sdk", "mcp.discovery"],
                "Official homepage confirms APIs, SDKs, and beta MCP, but password-gated legacy API docs and unverified auth/credential access require vendor outreach or interactive doc access before building.",
            )

    destination.write_text(json.dumps({"records": records}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {destination}")


if __name__ == "__main__":
    out_name = sys.argv[1] if len(sys.argv) > 1 else "extracted-records-002.json"
    build("task11-capture-004", Path(__file__).resolve().parent / out_name)
