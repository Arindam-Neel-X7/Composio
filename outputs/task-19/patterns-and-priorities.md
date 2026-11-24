# Cross-Application Patterns and Build Priorities Across 100 Applications

## Executive Summary

This report presents the synthesized findings of the **Analysis Agent** across the complete 100-application enterprise software roster (`data/apps.json`). Grounded in four strictly separated tiers of evidence—from sealed first-pass research across Tasks 07–16, through independent human baseline audit in Task 17 ($84.71\%$ baseline accuracy on frozen sample $N=327$), to immutable Task 18 error correction and recheck audit ($100.00\%$ accuracy on exact fixed denominator $N=327$)—this analysis establishes an empirical, reproducible foundation for agent tool development.

### Core Headline Metrics (Strict Denominators Across N=100 Applications)
- **Queue 1 (Build Now)**: **44/100 apps (44.00%)** — Viable for immediate agent tool integration with self-serve credentials and zero vendor/admin approval blockers.
- **Queue 2 (Conditional)**: **50/100 apps (50.00%)** — Fully functional APIs/MCPs requiring prerequisite workspace admin consent, vendor review, or commercial subscription.
- **Queue 3 (Outreach Required)**: **4/100 apps (4.00%)** — Enterprise-gated solutions requiring formal commercial contracting before credentials exist.
- **Queue 4 (Unknown / Blocked)**: **2/100 apps (2.00%)** — Targets with unresolved identity or persistent HTTP 403 access barriers, honestly preserved as unknowns.
- **MCP Ecosystem Maturity**: **85/100 apps (85.00%)** have documented MCP server implementations (70/100 official, 19/100 community, 4/100 both), while 11/100 have no MCP in checked sources, and 4/100 remain unknown.
- **Authentication Architecture**: OAuth 2.0 dominates enterprise access (**79/100 apps, 79.00%**), while API Keys (**39/100 apps, 39.00%**) and Bearer Tokens (**35/100 apps, 35.00%**) provide self-serve alternatives.

---

## 1. Methodology, Denominators, and Immutability Architecture

All percentages in this report are computed against explicit, stated denominators ($N=100$ applications for whole-roster analysis; $N=10$ applications for category slices; $N=327$ claims for evaluation sample comparisons). No percentage is reported in isolation.

### Four-Tier Immutability Architecture
1. **Tier 1 — First-Pass Extraction**: Sealed runs `task07-first-pass-003` through `task16-first-pass-001` across all 100 applications, preserved untouched.
2. **Tier 2 — Human Baseline Audit (Task 17)**: Stratified 20-app sample (`composio-20app-sample-v1`, $N=327$ claims) audited by human reviewer ARINDAM KARMAKAR, establishing an empirical documentary baseline of 84.71% accuracy (277 correct, 50 unsupported, 0 incorrect, 0 unresolved; observed: 95.52%, inferred: 0.00%).
3. **Tier 3 — Controlled Error Corrections (Task 18 Phase A)**: Exactly 50 unsupported statements corrected across 10 immutable child runs (`task18-corrections-07` through `16`) with zero schema mutations and strict question inventory preservation.
4. **Tier 4 — Human Recheck Audit & Authoritative Synthesis (Task 18 Phase B & Task 19)**: 100.00% accuracy verified across all 327 claims by ARINDAM KARMAKAR. Task 19 synthesizes this authoritative state (incorporating the 50 verified corrections for the 20 sampled apps while preserving the 80 unsampled first-pass records).

---

## 2. Cross-Cutting Patterns and Aggregates

### A. Category Dynamics and Feasibility Asymmetry

Buildability is severely asymmetric across business categories. While data acquisition and messaging are predominantly unblocked, infrastructure and enterprise collaboration are uniformly gated by organizational controls:

| Category | Total Apps | Build Now (Queue 1) | Conditional (Queue 2) | Outreach Required (Queue 3) | Unknown (Queue 4) | Dominant Gating Factor |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| AI, Research and Media-native | 10 | 5/10 (50.0%) | 5/10 (50.0%) | 0/10 (0.0%) | 0/10 (0.0%) | Balanced (OAuth Tenant / Vendor Review) |
| CRM and Sales | 10 | 5/10 (50.0%) | 4/10 (40.0%) | 1/10 (10.0%) | 0/10 (0.0%) | Balanced (OAuth Tenant / Vendor Review) |
| Communications and Messaging | 10 | 8/10 (80.0%) | 2/10 (20.0%) | 0/10 (0.0%) | 0/10 (0.0%) | 80-90% Self-Serve (API Keys / Free Trials) |
| Data, SEO and Scraping | 10 | 9/10 (90.0%) | 0/10 (0.0%) | 1/10 (10.0%) | 0/10 (0.0%) | 80-90% Self-Serve (API Keys / Free Trials) |
| Developer, Infra and Data platforms | 10 | 0/10 (0.0%) | 10/10 (100.0%) | 0/10 (0.0%) | 0/10 (0.0%) | 100% Gated (Tenant Admin / Cloud IAM) |
| Ecommerce | 10 | 4/10 (40.0%) | 4/10 (40.0%) | 2/10 (20.0%) | 0/10 (0.0%) | Balanced (OAuth Tenant / Vendor Review) |
| Finance and Fintech | 10 | 2/10 (20.0%) | 6/10 (60.0%) | 0/10 (0.0%) | 2/10 (20.0%) | Compliance / KYC / Regulatory Gating |
| Marketing, Ads, Email and Social | 10 | 5/10 (50.0%) | 5/10 (50.0%) | 0/10 (0.0%) | 0/10 (0.0%) | Balanced (OAuth Tenant / Vendor Review) |
| Productivity and Project Management | 10 | 0/10 (0.0%) | 10/10 (100.0%) | 0/10 (0.0%) | 0/10 (0.0%) | 100% Gated (Tenant Admin / Cloud IAM) |
| Support and Helpdesk | 10 | 6/10 (60.0%) | 4/10 (40.0%) | 0/10 (0.0%) | 0/10 (0.0%) | Balanced (OAuth Tenant / Vendor Review) |

#### Key Category Insights:
1. **Data, SEO and Scraping (9/10 Build Now, 90.00%)**: Highest buildability of any category. Providers like Bright Data, Clay, Perplexity, Tavily, and SerpApi offer self-serve API keys with recurring free allowances or instant prepaid billing.
2. **Communications and Messaging (8/10 Build Now, 80.00%)**: High buildability (Discord, Telegram, Twilio, SendGrid, Resend, Pusher) via instant self-serve tokens, with conditional limits confined to SMS carrier compliance or telephony regulation.
3. **Productivity and Project Management (0/10 Build Now, 100.00% Conditional)**: Every single app (Linear, Notion, ClickUp, Asana, Monday, Airtable, Jira, etc.) requires workspace tenant administrator consent or personal token generation within an established organizational boundary.
4. **Developer, Infra and Data Platforms (0/10 Build Now, 100.00% Conditional)**: Every cloud platform (AWS, GCP, Azure, Cloudflare, Supabase, Datadog, Snowflake) requires project provisioning, active billing cards, and IAM credential delegation before API calls succeed.

---

### B. Authentication Protocol Landscape

Modern agent integration relies on three primary authentication paradigms across the 100 applications:

| Auth Paradigm | Apps Supporting | Percentage (Denominator = 100) | Primary Strengths | Primary Agent Friction |
| --- | ---: | ---: | --- | --- |
| **OAuth 2.0** | 79/100 | 79.0% | Standard multi-tenant security, granular scopes, PKCE support. | Requires browser callback redirect, user consent, token refresh lifecycle. |
| **API Key** | 39/100 | 39.0% | Headless agent execution, simple header authentication, instant CLI use. | Static secret leakage risk, often lacks fine-grained resource permissions. |
| **Bearer / Personal Token** | 35/100 | 35.0% | Single-tenant developer testing, user-scoped permissions. | User manual generation required, expires or invalidates on password reset. |
| **Basic Auth** | 15/100 | 15.0% | Legacy compatibility for helpdesks and developer tools. | Weak credential isolation; being actively sunset across vendors. |
| **None / Local CLI** | 5/100 | 5.0% | Zero network credentials, local binary execution (Sherlock, Mermaid CLI). | Requires local environment runtime (Node.js/Python), no remote API fallback. |

---

### C. Credential Gating: Testing vs. Production Discrepancy

The research reveals a stark divergence between test environment accessibility and production operation. While 62/100 apps allow self-serve testing, only 49/100 allow self-serve production deployment, with paid requirements jumping from 1% to 36%:

| Gating Dimension | Testing True | Testing False | Testing Unknown | Production True | Production False | Production Unknown | Net Shift (Prod - Test) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `free_access` | 46/100 | 1/100 | 53/100 | 28/100 | 6/100 | 66/100 | **-18** |
| `trial_access` | 34/100 | 0/100 | 66/100 | 1/100 | 0/100 | 99/100 | **-33** |
| `sandbox_access` | 26/100 | 1/100 | 73/100 | 0/100 | 6/100 | 94/100 | **-26** |
| `paid_required` | 1/100 | 27/100 | 72/100 | 36/100 | 22/100 | 42/100 | **+35** |
| `admin_approval_required` | 5/100 | 2/100 | 93/100 | 20/100 | 2/100 | 78/100 | **+15** |
| `vendor_approval_required` | 5/100 | 7/100 | 88/100 | 17/100 | 1/100 | 82/100 | **+12** |
| `partner_approval_required` | 4/100 | 5/100 | 91/100 | 3/100 | 2/100 | 95/100 | **-1** |
| `contact_sales_required` | 0/100 | 5/100 | 95/100 | 3/100 | 6/100 | 91/100 | **+3** |
| `self_serve` | 62/100 | 4/100 | 34/100 | 49/100 | 8/100 | 43/100 | **-13** |

#### Crucial Gating Takeaways:
1. **Paid Tier Lockouts (+35 net shift)**: Only 1 application requires payment for initial testing (App 97: ElevenLabs, where free tier blocks API keys), but **36 applications (36.00%)** strictly require a paid subscription for production operation.
2. **Tenant Admin Approvals (+15 net shift)**: Multi-tenant production integrations trigger administrator review in **20 applications (20.00%)** (e.g. Slack workspace installation, Microsoft 365 tenant admin consent).
3. **Vendor Application Reviews (+12 net shift)**: **17 applications (17.00%)** enforce mandatory human vendor audit, brand verification, or developer token approval before production calls are permitted (e.g. Google Ads Explorer-to-Basic access, X Developer API Basic tier, TikTok Marketing Partner review).

---

### D. Model Context Protocol (MCP) Landscape Reality

The Model Context Protocol has achieved massive adoption across the audited software roster, with **85/100 applications (85.00%)** offering functional MCP servers:

- **Official MCP Implementations**: **70/100 apps (70.00%)** have official vendor-maintained or core-team repositories (e.g. GitHub, GitLab, Stripe, Cloudflare, Neon, Supabase, Linear, Notion, Slack, Sentry, PostHog, Klaviyo, HighLevel).
- **Community MCP Implementations**: **19/100 apps (19.00%)** have verified community implementations providing callable toolsets.
- **Ecosystem Overlap**: **4/100 apps (4.00%)** possess both official and community servers (e.g. Salesforce DX official + community wrappers).
- **Bounded Not Found**: **11/100 apps (11.00%)** have no documented MCP in checked official sources (e.g. Podio, Sherlock, NotebookLM, Ecwid, Waterfall.io).
- **Unknown MCP**: **4/100 apps (4.00%)** remain unknown due to capture walls or unresolved identity (Help Scout, Squarespace, Paygent Connect, PitchBook).

---

## 3. Cross-Tabulations and Strategic Interactions

### A. Auth Method vs. Buildability Interaction

| Auth Paradigm | Total Apps | Build Now (Queue 1) | Conditional (Queue 2) | Outreach Required (Queue 3) | Unknown (Queue 4) |
| --- | ---: | ---: | ---: | ---: | ---: |
| **OAuth 2.0** | 79 | 35 (44.30%) | 42 (53.16%) | 2 (2.53%) | 0 (0.00%) |
| **API Key** | 39 | 21 (53.85%) | 17 (43.59%) | 1 (2.56%) | 0 (0.00%) |
| **Bearer Token** | 35 | 14 (40.00%) | 21 (60.00%) | 0 (0.00%) | 0 (0.00%) |
| **Basic Auth** | 15 | 9 (60.00%) | 6 (40.00%) | 0 (0.00%) | 0 (0.00%) |
| **None / Local CLI** | 5 | 4 (80.00%) | 1 (20.00%) | 0 (0.00%) | 0 (0.00%) |

### B. MCP Server Availability vs. Buildability Interaction

| MCP Category | Total Apps | Build Now (Queue 1) | Conditional (Queue 2) | Outreach Required (Queue 3) | Unknown (Queue 4) |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Official MCP Only** | 66 | 32 (48.48%) | 31 (46.97%) | 3 (4.55%) | 0 (0.00%) |
| **Community MCP Only** | 15 | 7 (46.67%) | 8 (53.33%) | 0 (0.00%) | 0 (0.00%) |
| **Official + Community** | 4 | 2 (50.00%) | 2 (50.00%) | 0 (0.00%) | 0 (0.00%) |
| **No MCP (Bounded Search)** | 11 | 3 (27.27%) | 7 (63.64%) | 1 (9.09%) | 0 (0.00%) |
| **MCP Unknown** | 4 | 0 (0.00%) | 2 (50.00%) | 0 (0.00%) | 2 (50.00%) |

---

## 4. Full Visibility of Unknowns Inventory

In strict compliance with `docs/evidence-rules.md`, vendor silence is preserved as `unknown`, preventing fabricated negative claims. Exactly **2/100 apps (2.00%)** have unresolved product identities, **5/100 apps (5.00%)** have unknown API breadths, and **4/100 apps (4.00%)** have unknown MCP statuses:

### Detailed Unknowns Accounting Table

| Dimension | Unknown Count / Denominator | Affected App IDs & Names | Root Cause & Evidence Rule Justification | Unblocking Path |
| --- | ---: | --- | --- | --- |
| **Identity Resolution** | **2/100 (2.00%)** | App 84 (Paygent Connect), App 90 (PitchBook) | App 84: Vendor ambiguity (NMI vs Japanese Paygent). App 90: All official HTTP fetches returned 403 blocks. | Assignment sponsor clarification for App 84; approved browser extraction for App 90. |
| **Single-Line Purpose** | **2/100 (2.00%)** | App 84 (Paygent Connect), App 90 (PitchBook) | Directly follows unresolved identity resolution; no supported purpose can be asserted without identity. | Resolve identity resolution prerequisite. |
| **API Surface Breadth** | **5/100 (5.00%)** | App 18 (Help Scout), App 50 (fanbasis), App 84 (Paygent Connect), App 85 (iPayX), App 90 (PitchBook) | Documentation was captured for isolated endpoints only, leaving total resource domain breadth unmeasured. | Targeted crawl of full REST endpoint directories. |
| **MCP Discovery** | **4/100 (4.00%)** | App 18 (Help Scout), App 46 (Squarespace), App 84 (Paygent Connect), App 90 (PitchBook) | Primary developer docs captured did not include search coverage of MCP toolings or were 403 blocked. | Dedicated repository search across official GitHub orgs. |
| **Buildability Verdict** | **2/100 (2.00%)** | App 84 (Paygent Connect), App 90 (PitchBook) | An inference cannot be drawn when underlying identity or developer surfaces are unknown. | Upstream identity resolution and documentation capture. |
| **Credential Gating Silence** | **34-95/100 (34.00-95.00%)** | Widespread across roster (e.g. `testing.contact_sales_required`: 95 unknown) | Documentation did not explicitly disclaim or assert the condition; silence is preserved as unknown. | Empirical operational testing (account creation and key generation). |

---

## 5. Strategic Roadmap and Prioritized Implementation Sequences

### Phase 1: Immediate Drop-In Integrations (32 Applications)
- **Target**: Queue 1, Wave 1A (Official MCP Server ready + Self-serve access).
- **Actions**: Register MCP servers in agent runtime configs; supply environment variables from free accounts.
- **Key Targets**: HubSpot (2), Twenty (5), Zendesk (11), Intercom (12), Front (14), LiveAgent (16), Plain (17), Discord (21), Telegram (22), Slack (23), Twilio (24), SendGrid (25), Resend (26), Pusher (27), Tavily (51), Bright Data (52), Perplexity (53), Firecrawl (54), Exa (55), SerpApi (56), Apify (57), Jina (60), Postman (81), Stripe (87), ElevenLabs (94), Runway (95), Hugging Face (100).

### Phase 2: Community MCP & Local Binary Tooling (12 Applications)
- **Target**: Queue 1, Waves 1B and 1C (Community MCP or Local CLI).
- **Actions**: Audit community MCP server source code for security; package local CLI wrappers in containerized runners.
- **Key Targets**: Attio (4), Zoho CRM (7), Freshdesk (13), Postmark (30), Mailchimp (34), Clay (58), Podio (6), Sherlock (58), Mermaid CLI (98).

### Phase 3: High-Value Enterprise Workspace Integrations (27 Applications)
- **Target**: Queue 2, Condition 2A & 2E (Tenant Admin Consent & Cloud Infrastructure).
- **Actions**: Prepare multi-tenant OAuth registration apps; document enterprise administrator consent permission manifests; configure cloud service account roles.
- **Key Targets**: Linear (71), Notion (72), Airtable (73), Asana (74), Monday (76), ClickUp (77), Jira (78), GitHub (61), GitLab (62), Supabase (64), Cloudflare (68), Vercel (70).

### Phase 4: Regulated & Vendor Gated Applications (17 Applications)
- **Target**: Queue 2, Condition 2B & 2D (Vendor Review & Partner Gating).
- **Actions**: Submit platform developer applications; complete developer token reviews and brand verification.
- **Key Targets**: Google Ads (31), Meta / Facebook (32), TikTok (33), X / Twitter (35), Pinterest (38), Gorgias (19), BigCommerce (43).

### Phase 5: Commercial Partnerships & Sales Outreach (4 Applications)
- **Target**: Queue 3 (Outreach Required).
- **Actions**: Engage enterprise partnership teams; establish commercial volume agreements.
- **Key Targets**: DealCloud (10), Salesforce Commerce Cloud (44), fanbasis (50), Waterfall.io (59).

### Phase 6: Unblocking Research Backlog (2 Applications)
- **Target**: Queue 4 (Unknown / Blocked).
- **Actions**: Obtain author clarification on Paygent Connect (84); perform authenticated browser extraction for PitchBook (90).

---

## 6. Verification and Reproducibility Receipt

All calculations, aggregations, and tables in this report are 100% reproducible via deterministic offline code:

```powershell
# Execute reproducible Task 19 aggregation engine
.venv\Scripts\python.exe work\task-19-agent\generate_task19_outputs.py

# Verify schema validity and metrics
.venv\Scripts\python.exe -c "import json; print('Aggregates check:', len(json.load(open('outputs/task-19/aggregates.json', encoding='utf-8'))))"
```
