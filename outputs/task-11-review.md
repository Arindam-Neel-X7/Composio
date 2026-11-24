# Task 11: Independent AI Review Report (Ecommerce, IDs 41–50)

- **Final Verdict**: **PASS** *(initial audit of `task11-first-pass-003` returned `NEEDS FIXES` for 4 locator line-range defects across Apps 44, 46, and 50; all 4 remediated in immutable child run `task11-first-pass-004` and independently re-verified on disk → `PASS`)*
- **Reviewed on**: 2026-11-23
- **Auditor**: Independent read-only AI research subagent (`c5aa7ba9-e3ee-416a-a9f1-b1f4930f818d`, context-isolated; shared model family disclosed; initial quota-interrupted attempt `2e5e4336-480f-426b-8f38-2eb26f91a657` disclosed). **AI review only; not human review.**
- **Accepted Run**: `work/research-runs/task11-first-pass-004` (`records.json` SHA-256 `888099c43e7221eb550e77c95128420a6c4cde83701792b3eb24fa3e37db5a16`, `seal.json` SHA-256 `d8da1a9403eea9acfae56ccc1ba4bd41cea28cc8a44619ec2bf95b40574ca68d`)
- **Superseded Run Preserved Untouched**: `work/research-runs/task11-first-pass-003` (`records.json` SHA-256 `eb1325e40187590002464eb75d286bef9a0386258d6ce6d2cc1640d836d5ec04`, `seal.json` SHA-256 `acb6243720b6c15ada82aa286b0afdec35a170028af49149a4a6e961a13cb8f3`)
- **Formal Blind Scoring**: Deferred to Task 17 (20-app stratified sample, which includes App `46` Squarespace and App `50` fanbasis); `task11-first-pass-004` keeps `review.status == "pending"` and `accuracy: null` (`166` eligible assertions: `147` observed, `19` inferred; `295` verified evidence observations).

---

## 1. Core Verification Checks (All PASS)

| Area | Status | Verified Evidence |
| --- | --- | --- |
| Baseline & prior-run immutability | **PASS** | `pilot-first-pass-001` (`records.json` `10ff5bdb...`, `seal.json` `eaebd62d...`), `task05-review-002` (`seal.json` `9713538d...`), `outputs/task-06/sampling-manifest.json` (`7f8a6111...`), `data/apps.json` (`6e3aada1...`), and superseded `task11-first-pass-003` (`records.json` `eb1325e4...`, `seal.json` `acb62437...`) all verified unchanged. All files in `task11-first-pass-004/seal.json` verified with 0 mismatches. |
| Schema & grounding validation | **PASS** | `research_pipeline.py validate --run-id task11-first-pass-004` passed (`Python jsonschema Draft202012Validator`, contract `v1.1`, `10/10` records matching `data/apps.json` IDs 41–50, `synthetic: false`). |
| Evidence-link & claim grounding | **PASS** | Direct line-by-line inspection of all 10 records against `task11-first-pass-004/snapshots/*.txt` confirmed all 4 locator line-range defects on Apps 44, 46, and 50 are resolved with 0 regressions (Apps 41, 42, 43, 45, 47, 48, and 49 had 0 defects on first pass). All 10 nested MCP `operational_check` claims remain `not_researched`, 0 claims cite the 6 excluded 404/JS-shell snapshots, and community repos (`rmarescu/gumroad-mcp`, `jay-trivedi/amazon_sp_mcp`) are restricted strictly to `mcp` claims. |
| Deliverables consistency | **PASS** | `outputs/task-11/{records.json, source-index.md, findings-matrix.md, batch-report.md, exceptions-for-reviewer.md, metrics.json}` match `task11-first-pass-004` hashes (`888099c4...`, seal `d8da1a94...`), counts (`57` captures, `166` eligible, `295` evidence refs), and disclose all 403/404/timeout/JS-shell/login-wall exceptions and AI-only review. |

---

## 2. Remediations Verified on Re-Review (PASS)

1. **App 44 (Salesforce Commerce Cloud — `commerce-sdk-isomorphic` Custom APIs locator)**: Expanded `https://github.com/SalesforceCommerceCloud/commerce-sdk-isomorphic` locator from `lines:213-323` to `lines:213-387` and updated the observation to include `B2C Commerce Custom APIs (callCustomEndpoint)` (`L348-L387`) across `44.purpose`, `44.auth.slas_oauth2_jwt`, `44.api.protocol.rest`, `44.api.protocol.sdk`, `44.api.group.shopper_catalog_search`, `44.api.group.shopper_login_custom`, `44.api.group.admin_mrt_ods`, and `44.api.breadth`.
2. **App 44 (Salesforce Commerce Cloud — `b2c-developer-tooling` auth strategies & MCP tools locator)**: Expanded `https://github.com/SalesforceCommerceCloud/b2c-developer-tooling` locator from `lines:1-246` to `lines:1-353` and updated the observation to include `b2c-tooling-sdk (OAuth, API Key, Basic auth strategies; MRT and ODS clients)` (`L319-L321`) and `b2c-dx-mcp (... including MCP docs_*, MCP validate_xml_schema, and B2C_INSTANCE=my-sandbox tooling)` (`L333-L352`) across `44.identity`, `44.purpose`, `44.api.protocol.cli`, `44.api.breadth`, `44.mcp.discovery`, `44.mcp.b2c_dx_mcp`, and `44.buildability`.
3. **App 46 (Squarespace — `developers.squarespace.com/oauth` scopes locator)**: Expanded `https://developers.squarespace.com/oauth` locator from `lines:93-115` to `lines:50-115` and included `website.contacts` and `website.contacts.read` (`L75-L78`) in the observation across `46.auth.oauth2_extensions`, `46.api.public_docs`, and `46.buildability`.
4. **App 50 (fanbasis / Commas — `www.fanbasis.com/` BNPL payments locator)**: Expanded `https://www.fanbasis.com/` locator from `lines:52-59` to `lines:41-60` and included `cards/wallets/BNPL payments, subscriptions` (`L41-L51`) in the observation across `50.purpose`, `50.api.protocol.sdk`, `50.api.group.checkouts_payouts_refunds`, `50.mcp.discovery`, `50.mcp.commas_mcp_beta`, and `50.buildability`.

---

## 3. Disposition

- **Task 11 status**: Accepted (**PASS**) after remediation in `work/research-runs/task11-first-pass-004` (AI review only; no human review; formal blind scoring of frozen sample apps `46` and `50` deferred to Task 17).
