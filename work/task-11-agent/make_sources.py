"""Generate initial primary-source list for Task 11 (Ecommerce, IDs 41-50)."""
import json
from pathlib import Path

ATTRIBUTION_BY = "task11-research-agent-gemini"

SCOPES = {
    41: "Shopify Admin GraphQL/REST and Storefront APIs, OAuth 2.0 and access token auth, Partner development stores/paid plans, and official/community MCP servers",
    42: "WooCommerce REST API and Store API, consumer key/secret Basic/OAuth1 and WordPress Application Password auth, open-source self-hosted/WordPress ecosystem, and official MCP adapter",
    43: "BigCommerce Management REST and Storefront GraphQL APIs, OAuth 2.0 and store-level X-Auth-Token auth, Partner sandboxes/paid plans, and official MCP servers",
    44: "Salesforce B2C Commerce API (SCAPI), SLAS OAuth 2.0 and Account Manager OAuth 2.0 auth, enterprise licensing/sandboxes, and official/community MCP ecosystem",
    45: "Magento / Adobe Commerce REST and GraphQL APIs (PaaS/Open Source and SaaS), token/OAuth 1.0a and Adobe IMS OAuth 2.0 auth, open-source vs paid enterprise licensing, and MCP ecosystem",
    46: "Squarespace Commerce APIs (Orders, Inventory, Products, Transactions, Profiles, Webhook Subscriptions), API Key Bearer and OAuth 2.0 auth, paid plan tiers, and MCP ecosystem",
    47: "Ecwid by Lightspeed REST API, OAuth 2.0 and secret/public access token auth, free/paid plan tiers, and MCP ecosystem",
    48: "Gumroad v2 REST API, OAuth 2.0 and generated access token auth, flat transaction-fee pricing, and community MCP ecosystem",
    49: "Amazon Selling Partner API (SP-API), Login with Amazon (LWA) OAuth 2.0 auth, developer registration/approval and sandbox environment, and official/community MCP ecosystem",
    50: "FanBasis (rebranded to Commas) REST API, API key and OAuth auth, sandbox/production environments, transaction-fee pricing, and official remote MCP server",
}


def src(app_id, url, kind, envs, basis="Vendor-controlled official documentation or product page"):
    return {
        "app_id": app_id,
        "url": url,
        "kind": kind,
        "scope": SCOPES[app_id],
        "environments": envs,
        "attribution_basis": basis,
        "attribution_by": ATTRIBUTION_BY,
    }


SOURCES = [
    # 41. Shopify
    src(41, "https://shopify.dev/docs/api", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/api/admin-graphql", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/apps/build/authentication", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/apps/build/authentication-authorization/access-tokens/client-credentials-grant", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/api/development-stores", "primary_docs", ["testing", "production"]),
    src(41, "https://shopify.dev/docs/agents", "primary_docs", ["testing", "production"]),
    src(41, "https://github.com/Shopify/dev-mcp", "official_repository", ["testing", "production"], "Official Shopify GitHub repository for Dev MCP server"),
    src(41, "https://www.shopify.com/pricing", "official_product_page", ["testing", "production"]),

    # 42. WooCommerce
    src(42, "https://developer.woocommerce.com/docs/apis/rest-api/", "primary_docs", ["testing", "production"]),
    src(42, "https://woocommerce.github.io/woocommerce-rest-api-docs/", "primary_docs", ["testing", "production"]),
    src(42, "https://developer.woocommerce.com/docs/features/mcp/", "primary_docs", ["testing", "production"]),
    src(42, "https://woocommerce.com/pricing/", "official_product_page", ["testing", "production"]),
    src(42, "https://github.com/woocommerce/woocommerce", "official_repository", ["testing", "production"], "Official WooCommerce GitHub repository"),

    # 43. BigCommerce
    src(43, "https://developer.bigcommerce.com/docs/start/authentication", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/start/about/sandboxes", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/rest-management", "primary_docs", ["testing", "production"]),
    src(43, "https://developer.bigcommerce.com/docs/storefront/graphql", "primary_docs", ["testing", "production"]),
    src(43, "https://www.bigcommerce.com/essentials/pricing/", "official_product_page", ["testing", "production"]),
    src(43, "https://docs.bigcommerce.com/llms.txt", "primary_docs", ["testing", "production"]),

    # 44. Salesforce Commerce Cloud
    src(44, "https://developer.salesforce.com/docs/commerce/commerce-api/guide/get-started.html", "primary_docs", ["testing", "production"]),
    src(44, "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-shopper-apis.html", "primary_docs", ["testing", "production"]),
    src(44, "https://developer.salesforce.com/docs/commerce/commerce-api/guide/authorization-for-admin-apis.html", "primary_docs", ["testing", "production"]),
    src(44, "https://www.salesforce.com/commerce/pricing/", "official_product_page", ["testing", "production"]),
    src(44, "https://github.com/SalesforceCommerceCloud/b2c-developer-tooling", "official_repository", ["testing", "production"], "Official Salesforce Commerce Cloud GitHub repository"),

    # 45. Magento (Adobe Commerce)
    src(45, "https://developer.adobe.com/commerce/webapi/rest/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/graphql/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/get-started/authentication/", "primary_docs", ["testing", "production"]),
    src(45, "https://developer.adobe.com/commerce/webapi/get-started/authentication/gs-authentication-token/", "primary_docs", ["testing", "production"]),
    src(45, "https://business.adobe.com/products/magento/pricing.html", "official_product_page", ["testing", "production"]),
    src(45, "https://github.com/magento/magento2", "official_repository", ["testing", "production"], "Official Magento Open Source GitHub repository"),

    # 46. Squarespace
    src(46, "https://developers.squarespace.com/commerce-apis", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/commerce-apis/authentication-and-permissions", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/oauth", "primary_docs", ["testing", "production"]),
    src(46, "https://developers.squarespace.com/commerce-apis/orders-api", "primary_docs", ["testing", "production"]),
    src(46, "https://www.squarespace.com/pricing", "official_product_page", ["testing", "production"]),

    # 47. Ecwid
    src(47, "https://docs.ecwid.com/api-reference/rest-api/overview", "primary_docs", ["testing", "production"]),
    src(47, "https://docs.ecwid.com/api-reference/rest-api/authentication", "primary_docs", ["testing", "production"]),
    src(47, "https://api-docs.ecwid.com/reference/overview", "primary_docs", ["testing", "production"]),
    src(47, "https://www.ecwid.com/pricing", "official_product_page", ["testing", "production"]),

    # 48. Gumroad
    src(48, "https://gumroad.com/api", "primary_docs", ["testing", "production"]),
    src(48, "https://gumroad.com/pricing", "official_product_page", ["testing", "production"]),
    src(48, "https://help.gumroad.com/article/280-create-application-api", "primary_docs", ["testing", "production"]),
    src(48, "https://github.com/antiwork/gumroad", "official_repository", ["testing", "production"], "Official Gumroad GitHub repository"),

    # 49. Amazon Selling Partner
    src(49, "https://developer-docs.amazon.com/sp-api/docs/what-is-the-selling-partner-api", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/onboarding-as-a-developer", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/connect-to-the-sp-api", "primary_docs", ["testing", "production"]),
    src(49, "https://developer-docs.amazon.com/sp-api/docs/the-selling-partner-api-sandbox", "primary_docs", ["testing", "production"]),
    src(49, "https://github.com/amzn/selling-partner-api-models", "official_repository", ["testing", "production"], "Official Amazon SP-API OpenAPI models GitHub repository"),
    src(49, "https://github.com/amzn/selling-partner-agentic-toolkit", "official_repository", ["testing", "production"], "Official Amazon SP-API Agentic Toolkit GitHub repository"),

    # 50. fanbasis
    src(50, "https://www.fanbasis.com/", "official_product_page", ["testing", "production"]),
    src(50, "https://commas.com/", "official_product_page", ["testing", "production"]),
    src(50, "https://commasdocs.com/", "primary_docs", ["testing", "production"]),
    src(50, "https://commasdocs.com/llms.txt", "primary_docs", ["testing", "production"]),
    src(50, "https://dev-docs.fanbasis.com/", "primary_docs", ["testing", "production"]),
]


def main():
    out = Path(__file__).resolve().parent / "sources-001.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(SOURCES)} sources to {out}")


if __name__ == "__main__":
    main()
