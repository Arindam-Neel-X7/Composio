"""Task 12 source declarations (Data, SEO and Scraping, IDs 51-60). Attribution is researcher assertion, not proof."""
import json
from pathlib import Path

BY = "task12-research-agent-claude"

SCOPES = {
    51: "DataForSEO v3 REST APIs and official MCP server, HTTP Basic API login/password auth, sandbox and paid pay-as-you-go access",
    52: "SE Ranking Data API, Project API and hosted MCP server, API token auth and OAuth, paid plan and API credits",
    53: "Ahrefs API v3 and hosted MCP server, API key and OAuth auth, paid-plan/API-unit access (not the consumer web app)",
    54: "MrScraper hosted scraping API v3, MCP server and CLI, API token and OAuth auth, plan-based access",
    55: "Apify platform REST API v2, Apify MCP server, CLI and open-source Actors tooling, API token and OAuth auth, free and paid plans",
    56: "Firecrawl hosted API v2 and MCP server, API key auth, free credits and paid plans, plus open-source self-hosted edition",
    57: "Bright Data hosted APIs (Web Unlocker, SERP, Scrapers, datasets, account management) and official MCP server, API key auth, free tier and paid usage",
    58: "Sherlock Project open-source username-search CLI (sherlock-project), local installation, no hosted API",
    59: "Waterfall.io B2B contact and company enrichment REST API (docs.waterfall.io v1), x-api-key auth, access request/paid usage; not other products named Waterfall",
    60: "Clay (clay.com) GTM data-enrichment platform, Public API and hosted MCP server, API key and OAuth auth, plan-gated access",
}
ENV = ["testing", "production"]


def s(app, url, kind="primary_docs", envs=ENV, basis="Vendor/project-controlled documentation or product page selected by researcher"):
    return {"app_id": app, "url": url, "kind": kind, "scope": SCOPES[app], "environments": envs,
            "attribution_basis": basis, "attribution_by": BY}


PP = "official_product_page"
OR = "official_repository"
CR = "community_repository"

SOURCES = []
for u in ["https://docs.dataforseo.com/v3/", "https://docs.dataforseo.com/v3/auth/", "https://docs.dataforseo.com/v3/appendix/sandbox/",
          "https://docs.dataforseo.com/v3/serp/overview/", "https://docs.dataforseo.com/v3/keywords_data/overview/",
          "https://docs.dataforseo.com/v3/backlinks/overview/", "https://docs.dataforseo.com/v3/on_page/overview/",
          "https://docs.dataforseo.com/v3/dataforseo_labs/overview/", "https://docs.dataforseo.com/v3/business_data/overview/",
          "https://docs.dataforseo.com/v3/domain_analytics/overview/", "https://docs.dataforseo.com/v3/app_data/overview/",
          "https://docs.dataforseo.com/v3/merchant/overview/", "https://docs.dataforseo.com/v3/content_analysis/overview/",
          "https://docs.dataforseo.com/v3/ai_optimization/overview/"]:
    SOURCES.append(s(51, u))
SOURCES += [s(51, "https://dataforseo.com/pricing", PP), s(51, "https://dataforseo.com/apis", PP),
            s(51, "https://dataforseo.com/model-context-protocol", PP),
            s(51, "https://github.com/dataforseo/mcp-server-typescript", OR)]

for u in ["https://seranking.com/api/", "https://seranking.com/api/data/", "https://seranking.com/api/integrations/mcp/",
          "https://seranking.com/api/project/", "https://seranking.com/api/data/keyword-research/",
          "https://seranking.com/api/data/backlinks/", "https://seranking.com/api/data/domain-analysis/",
          "https://seranking.com/api/data/website-audit/", "https://seranking.com/api/data/ai-search/",
          "https://seranking.com/api/project/audit/", "https://seranking.com/api/mcp/"]:
    SOURCES.append(s(52, u, PP))
SOURCES += [s(52, "https://seranking.com/pricing.html", PP), s(52, "https://github.com/seranking", OR)]

for u in ["https://docs.ahrefs.com/api/docs/introduction.md", "https://docs.ahrefs.com/api/docs/free-test-queries.md",
          "https://docs.ahrefs.com/api/docs/api-keys-creation-and-management.md", "https://docs.ahrefs.com/api/docs/limits-consumption.md",
          "https://docs.ahrefs.com/mcp/docs/introduction.md", "https://docs.ahrefs.com/mcp/docs/tool-categories.md",
          "https://docs.ahrefs.com/mcp/docs/claude-code.md", "https://docs.ahrefs.com/llms.txt",
          "https://docs.ahrefs.com/reference/public.json", "https://docs.ahrefs.com/openapi.json"]:
    SOURCES.append(s(53, u))
SOURCES += [s(53, "https://ahrefs.com/pricing", PP), s(53, "https://docs.ahrefs.com/ahrefs-connect/docs/oauth-guide.md")]

for u in ["https://docs.mrscraper.com/llms.txt", "https://docs.mrscraper.com/docs/api/overview",
          "https://docs.mrscraper.com/docs/api/authentication", "https://docs.mrscraper.com/docs/getting-started/api-token",
          "https://docs.mrscraper.com/docs/getting-started/billing", "https://docs.mrscraper.com/docs/getting-started/mcp-server",
          "https://docs.mrscraper.com/docs/getting-started/cli", "https://docs.mrscraper.com/docs/getting-started/overview",
          "https://docs.mrscraper.com/docs/api/scraper-api/scrape-json", "https://docs.mrscraper.com/docs/api/v3/scraper/web-fetching-scraping"]:
    SOURCES.append(s(54, u))
SOURCES += [s(54, "https://mrscraper.com/pricing", PP)]

for u in ["https://docs.apify.com/api/v2.md", "https://docs.apify.com/platform/integrations/api.md",
          "https://docs.apify.com/platform/integrations/mcp.md", "https://docs.apify.com/llms.txt",
          "https://docs.apify.com/cli/docs", "https://docs.apify.com/platform/actors",
          "https://docs.apify.com/platform/integrations", "https://docs.apify.com/platform/security",
          "https://docs.apify.com/platform/actors/running/usage-and-resources",
          "https://docs.apify.com/platform/collaboration/access-rights",
          "https://docs.apify.com/api/client/js/", "https://docs.apify.com/api/client/python/"]:
    SOURCES.append(s(55, u))
SOURCES += [s(55, "https://apify.com/pricing", PP), s(55, "https://github.com/apify/apify-mcp-server", OR),
            s(55, "https://raw.githubusercontent.com/apify/apify-mcp-server/master/README.md", OR)]

for u in ["https://docs.firecrawl.dev/introduction.md", "https://docs.firecrawl.dev/api-reference/introduction.md",
          "https://docs.firecrawl.dev/mcp-server.md", "https://docs.firecrawl.dev/llms.txt",
          "https://docs.firecrawl.dev/_llms/en/v2/documentation.txt", "https://docs.firecrawl.dev/rate-limits",
          "https://docs.firecrawl.dev/features/scrape", "https://docs.firecrawl.dev/contributing/self-host"]:
    SOURCES.append(s(56, u))
SOURCES += [s(56, "https://www.firecrawl.dev/pricing", PP), s(56, "https://github.com/firecrawl/firecrawl-mcp-server", OR),
            s(56, "https://raw.githubusercontent.com/firecrawl/firecrawl-mcp-server/main/README.md", OR),
            s(56, "https://raw.githubusercontent.com/firecrawl/firecrawl/main/README.md", OR),
            s(56, "https://raw.githubusercontent.com/firecrawl/firecrawl/main/LICENSE", OR)]

for u in ["https://docs.brightdata.com/api-reference/authentication.md", "https://docs.brightdata.com/products/mcp-server/overview.md",
          "https://docs.brightdata.com/general/account/billing-and-pricing/free-tier.md", "https://docs.brightdata.com/llms.txt",
          "https://docs.brightdata.com/products/cli/overview.md", "https://docs.brightdata.com/products/web-unlocker/introduction.md",
          "https://docs.brightdata.com/products/serp-api/introduction.md", "https://docs.brightdata.com/products/scrapers/overview.md",
          "https://docs.brightdata.com/api-reference/marketplace-dataset-api/overview.md",
          "https://docs.brightdata.com/api-reference/account-management-api/Add_a_Zone.md",
          "https://docs.brightdata.com/products/scraping-browser/introduction.md"]:
    SOURCES.append(s(57, u))
SOURCES += [s(57, "https://brightdata.com/pricing", PP), s(57, "https://github.com/brightdata/brightdata-mcp", OR),
            s(57, "https://raw.githubusercontent.com/brightdata/brightdata-mcp/main/README.md", OR)]

SHE = []
SOURCES += [s(58, "https://github.com/sherlock-project/sherlock", OR, ["testing", "production"]),
            s(58, "https://raw.githubusercontent.com/sherlock-project/sherlock/master/LICENSE", OR, ["testing", "production"]),
            s(58, "https://raw.githubusercontent.com/sherlock-project/sherlock/master/pyproject.toml", OR, ["testing", "production"]),
            s(58, "https://sherlockproject.xyz/usage", PP, ["testing", "production"]),
            s(58, "https://sherlockproject.xyz/installation", PP, ["testing", "production"]),
            s(58, "https://sherlockproject.xyz/", PP, ["testing", "production"]),
            s(58, "https://pypi.org/project/sherlock-project/", PP, ["testing", "production"])]

for u in ["https://docs.waterfall.io/v1/overview.md", "https://docs.waterfall.io/v1/about-waterfall.md",
          "https://docs.waterfall.io/v1/authentication.md", "https://docs.waterfall.io/v1/quickstart.md",
          "https://docs.waterfall.io/v1/rate-limit.md", "https://docs.waterfall.io/v1/book-demo.md",
          "https://docs.waterfall.io/v1/faq.md", "https://docs.waterfall.io/v1/evaluate-waterfall.md",
          "https://docs.waterfall.io/v1/api-keys-overview.md", "https://docs.waterfall.io/v1/skills-overview.md",
          "https://docs.waterfall.io/llms.txt", "https://docs.waterfall.io/v1/company-enrichment-launcher.md",
          "https://docs.waterfall.io/v1/email-verifier.md", "https://docs.waterfall.io/v1/company-reveal-launcher.md",
          "https://docs.waterfall.io/v1/job-change-launcher.md", "https://docs.waterfall.io/v1/account-reporter-v2.md",
          "https://docs.waterfall.io/v1/openapi-spec.md"]:
    SOURCES.append(s(59, u))
SOURCES += [s(59, "https://waterfall.io/pricing", PP), s(59, "https://waterfall.io/", PP)]

SOURCES += [s(60, "https://www.clay.com/docs", PP), s(60, "https://docs.clay.com/", "primary_docs"),
            s(60, "https://www.clay.com/pricing", PP), s(60, "https://www.clay.com/mcp", PP)]

if __name__ == "__main__":
    out = Path(__file__).parent / "sources-001.json"
    out.write_text(json.dumps({"sources": SOURCES}, indent=2) + "\n", encoding="utf-8")
    print(len(SOURCES), "sources ->", out)
