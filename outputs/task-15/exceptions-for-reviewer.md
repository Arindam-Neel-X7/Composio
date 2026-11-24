# Task 15: Exceptions, Unknowns & Review Notes (IDs 81–90)

- **Run ID**: `task15-first-pass-002`
- **Independent Review**: Pending (no accuracy or human-verification claims).

## 1. Unresolved Identity — ID 84 (Paygent Connect)
- `data/apps.json` flags Paygent Connect as `identity_status: "unresolved"` with original hint `paygent (NMI-powered)` and explicitly warns that legacy lead `paygentglobal.com` has no established identity match.
- Primary web search and captures of `https://www.nmi.com/` and `https://docs.nmi.com/` confirm NMI is a general white-label gateway platform and do **not** link NMI to a product named "Paygent Connect" (Japanese Paygent Co., Ltd. is a separate NTT DATA / MUFG NICOS gateway and is not substituted).
- Per `docs/evidence-rules.md`, `84.identity.resolution` and all product-specific claims remain `unknown`.

## 2. Complete Primary Capture Block — ID 90 (PitchBook)
- All 7 official PitchBook URLs (`pitchbook.com` and `www.pitchbook.com` help/product pages) returned **HTTP 403 (`blocked`)** across `task15-capture-001` through `task15-capture-003` (`fetches[0..6]`).
- Per `docs/evidence-rules.md`, HTTP 403 is not proof of no API/MCP, and third-party/search snippets cannot establish vendor product claims. All PitchBook claims remain `unknown` pending an approved browser/receipt capture path.

## 3. JS SPA Shells & Attribution Nuance — ID 85 (iPayX)
- Static HTTP captures of `ipayx.ai/docs`, `/docs/api`, `/docs/mcp`, `/api-terms`, and `www.ipayx.ai/` returned a single-line SPA title (`iPayX Protocol — FINTRAC-registered FX forensic audit layer`), and `/pricing` timed out.
- `raw.githubusercontent.com/iPAYX-Technologies/mcp-fx-audit/main/README.md` (105 lines) documents a remote streamable-HTTP MCP server at `https://mcp.ipayx.ai/mcp` (v1.4.0, 4 tools, Bearer key for `full_forensic_fx_report`). Because the vendor-domain SPA did not render a link verifying ownership of the GitHub org, it is conservatively tagged `community_repository` (`origin: "community"`) and cited **only** for MCP claims, leaving primary REST API, auth, and pricing as `unknown`.

## 4. Partial Capture Gaps on Other Apps
- **ID 83 (Binance)**: `developers.binance.com` HTML returned `empty_readable_content` (3 failed fetches); resolved via official GitHub repository `binance/binance-spot-api-docs` (`rest-api.md`, `testnet/general-info.md`, `README.md`). Global production KYC/jurisdictional eligibility remains `unknown`; only a community MCP (`mujeeb8/Binance-MCP`) was found in checked sources.
- **ID 86 (QuickBooks)**: `all-entities` HTML failed (timeout / HTTP 403) and `tos.html` timed out; API resource groups were grounded in Intuit's official `intuit/quickbooks-online-mcp-server` README (29 CRUD entities + 11 financial reports), while API ToS/billing terms remain `unknown`. Note: `mcp-connector.html` describes the "Intuit Developer Plugin" AI onboarding assistant rather than a runtime QBO data MCP server.
- **ID 87 (Xero)**: 4 `developer.xero.com/documentation/*` pages rendered as 1-line JS SPA shells; resolved via non-SPA `developer.xero.com/pricing`, `/faq/remote-mcp`, `/faq/custom-integration`, `/faq/getting-started`, and official `XeroAPI/Xero-OpenAPI`, `XeroAPI/xero-node`, and `XeroAPI/xero-mcp-server` repositories. Note upcoming deprecation: new Custom Connection creation closes 1 December 2026.
- **ID 88 (Brex)**: `developer.brex.com/docs/mcp-server` returned HTTP 404; resolved via official `developer.brex.com/docs/mcp.md`. Own-account customers have no sandbox (`api.brex.com` production only), while partner staging (`api-staging.brex.com`) requires partner approval and Unilateral API Access Agreement.
- **ID 89 (Ramp)**: HTML pages under `docs.ramp.com/developer-api/v1/*` are 16-line JS shells; resolved via official `llms.txt`, `llms-api.txt`, and `llms-guides/*.txt`. However, `llms-guides/sandbox-access.txt` had an empty body (4 lines), leaving sandbox approval policy `unknown`. Ramp also references a second `Ramp Data MCP` (benchmarks) in `llms.txt` L55/61 without a captured server URL.

## 5. Preserved Rejected / Unused Runs
- `task15-capture-004`: network-isolated sandbox capture attempt (unused branch; `task15-capture-005` branched cleanly from `task15-capture-003`).
- `task15-first-pass-001`: rejected ingest where community MCP READMEs were accidentally attached to `83.buildability` and `85.buildability`; fixed in `task15-first-pass-002`.
