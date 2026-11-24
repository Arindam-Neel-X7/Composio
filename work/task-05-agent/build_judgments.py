"""Build work/task-05-agent/judgments.json for independent AI review of pilot-first-pass-001."""
import json
from pathlib import Path

RUN_DIR = Path("work/task-04-runs/pilot-first-pass-001")
OUT_PATH = Path("work/task-05-agent/judgments.json")


def iter_claims(obj, path=()):
    if isinstance(obj, dict):
        if "claim_id" in obj and "status" in obj and "evidence" in obj:
            yield path, obj
        for k, v in obj.items():
            yield from iter_claims(v, path + (k,))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            yield from iter_claims(item, path + (i,))


def make_ev(captures_by_url, app_id, url, locator, observation):
    c = captures_by_url[(app_id, url)]
    return {
        "source_url": c["spec"]["url"],
        "source_kind": c["spec"]["kind"],
        "locator": locator,
        "observation": observation,
        "captured_on": c["captured_on"],
        "capture_method": c["capture_method"],
        "content_sha256": c["content_sha256"],
        "snapshot_ref": c["snapshot_ref"],
        "hash_unavailable_reason": None,
        "document_version": c["spec"].get("document_version"),
        "document_date": c["spec"].get("document_date"),
    }


def main():
    records = json.loads((RUN_DIR / "records.json").read_text(encoding="utf-8"))
    captures = json.loads((RUN_DIR / "captures.json").read_text(encoding="utf-8"))
    inv = json.loads((RUN_DIR / "inventory.json").read_text(encoding="utf-8"))

    captures_by_url = {(c["spec"]["app_id"], c["spec"]["url"]): c for c in captures}
    eligible_ids = {(i["app_id"], i["claim_id"]) for i in inv if i["eligible"]}

    # Specific overrides for unsupported claims or claims with important review caveats
    overrides = {
        # App 2 caveats (correct under stated legacy-path rationale, with scope caveat noted)
        "2.production.free_access": (
            "correct",
            "Verified for the explicitly scoped existing legacy private-app path: legacy-apps/private-apps/overview lines 130-134 list Free and Starter rate limits, and lines 55-56 confirm existing legacy apps remain supported even though new creation ended 2026-10-26. Caveat: claim.context uses the broad app-wide string rather than a legacy-only scope.",
            None,
        ),
        "2.production.paid_required": (
            "correct",
            "Verified for the explicitly scoped existing legacy private-app path using Free-tier features only (legacy-apps/private-apps/overview lines 130-134). Caveat: does not establish paid_required=false for new current developer-platform production onboarding.",
            None,
        ),
        "2.production.admin_approval_required": (
            "correct",
            "Verified for the explicitly scoped existing legacy private-app path: legacy-apps/private-apps/overview line 59 explicitly states 'You must be a super admin to access private apps in your HubSpot account.'",
            None,
        ),
        "2.api.group.content": (
            "correct",
            "Verified: api-reference/latest/overview lines 43-52 (inside cited lines 38-52) list CMS, Blogs, Content audit, Domains, HubDB, Media Bridge, Pages, Site Search, Source code, and URL mapping. Minor locator note: lines 38-42 cover OAuth tokens and Automation before the CMS heading at line 43.",
            None,
        ),
        # App 31 unsupported findings
        "31.production.admin_approval_required": (
            "unsupported",
            "Unsupported inference: best-practices/testing lines 481-487 describe adding a test user/service account to test accounts (and explicitly warn 'Don't give this user or service account access to any production accounts'), while oauth/overview lines 438-441 only state that the authorized user or service account must have access to the target Google Ads accounts. Neither cited passage documents that admin approval is required for production credentials.",
            [
                make_ev(
                    captures_by_url,
                    31,
                    "https://developers.google.com/google-ads/api/docs/best-practices/testing",
                    "lines:481-487",
                    "quote: user or service account access to any production accounts.",
                ),
                make_ev(
                    captures_by_url,
                    31,
                    "https://developers.google.com/google-ads/api/docs/oauth/overview",
                    "lines:438-441",
                    "quote: Make sure your authorized user or your service account has access to",
                ),
            ],
        ),
        "31.production.partner_approval_required": (
            "unsupported",
            "Unsupported taxonomy mapping: access-levels lines 123-169 document Google vendor API-access approval (Explorer/Basic/Standard application in Google Cloud Console, which may be automatically approved), not partner approval or a partner program. The researcher's rationale itself acknowledges this is 'not a commercial partnership contract'; asserting partner_approval_required=true as observed is unsubstantiated by the cited text and reflects a schema gap (no vendor_approval_required field).",
            [
                make_ev(
                    captures_by_url,
                    31,
                    "https://developers.google.com/google-ads/api/docs/api-policy/access-levels",
                    "lines:161-169",
                    "quote: Google may automatically upgrade your project's API access level to Explorer",
                ),
            ],
        ),
        "31.buildability": (
            "correct",
            "Verified: all material details of the conditional verdict, scope, blockers ('Production project needs Explorer or higher approval and target-account access', 'Test accounts cannot establish realistic performance-report behavior'), and next steps are directly supported by the four attached primary-doc passages. Note: supporting_claim_refs includes 31.production.partner_approval_required, which requires taxonomy cleanup in Task 06.",
            None,
        ),
        # App 91 unsupported findings
        "91.purpose": (
            "unsupported",
            "Unsupported material detail in attached evidence: the claim asserts 'programmatic notebook and source management', but its sole attached citation (api-notebooks lines 148-155) only documents notebook management (create, retrieve, list, delete, share) and does not mention source management. Source management is documented in api-notebooks-sources lines 148-156 (captured in this run) but was omitted from 91.purpose's own evidence array.",
            [
                make_ev(
                    captures_by_url,
                    91,
                    "https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks",
                    "lines:148-155",
                    "quote: This page describes the APIs that let you",
                ),
                make_ev(
                    captures_by_url,
                    91,
                    "https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources",
                    "lines:148-156",
                    "quote: This page describes how to perform the following tasks:",
                ),
            ],
        ),
        "91.mcp": (
            "unsupported",
            "Unsupported on two grounds: (1) edition/scope mismatch — asserts app-level mcp.discovery='found' on a NotebookLM Enterprise API record based solely on a community repo for personal notebooklm.google.com internal APIs/cookies that explicitly states 'May work with NotebookLM Enterprise accounts but has not been tested' (line 157); (2) locator truncation — ev[0] cites lines:151-165, which stops at the table header ('Tool / Description') and omits the actual tool rows beginning at line 166.",
            [
                make_ev(
                    captures_by_url,
                    91,
                    "https://github.com/Morfeu333/notebooklm-mcp",
                    "lines:155-167",
                    "quote: May work with NotebookLM Enterprise accounts but has not been tested.",
                ),
                make_ev(
                    captures_by_url,
                    91,
                    "https://github.com/Morfeu333/notebooklm-mcp",
                    "lines:220-224",
                    "quote: Use at your own risk for personal/experimental purposes.",
                ),
            ],
        ),
        "91.mcp.personal_community": (
            "unsupported",
            "Unsupported due to locator truncation: although the entry's value.scope accurately distinguishes personal notebooklm.google.com internal APIs from Enterprise REST, ev[0] cites lines:151-165 with the paraphrase 'and lists notebook tools', but lines 151-165 end at the table header ('Tool / Description') and exclude the actual callable tool rows beginning at line 166 ('notebook_list', 'notebook_create', etc.).",
            [
                make_ev(
                    captures_by_url,
                    91,
                    "https://github.com/Morfeu333/notebooklm-mcp",
                    "lines:163-171",
                    "quote: notebook_list",
                ),
            ],
        ),
    }

    out = {"records": {}}
    total = 0
    for rec in records:
        app_id = rec["identity"]["id"]
        adjs = []
        for path, claim in iter_claims(rec):
            cid = claim["claim_id"]
            if (app_id, cid) not in eligible_ids:
                continue
            total += 1
            if cid in overrides:
                judgment, reason, custom_ev = overrides[cid]
                ev = custom_ev if custom_ev is not None else claim["evidence"]
            else:
                judgment = "correct"
                basis = "documentary observation" if claim["status"] == "observed" else "inference"
                reason = f"Independent AI review verified {basis} against captured primary documentation; all material details hold for the declared scope."
                ev = claim["evidence"]
            adjs.append(
                {
                    "claim_id": cid,
                    "original_run_id": "pilot-first-pass-001",
                    "judgment": judgment,
                    "reason": reason,
                    "evidence": ev,
                }
            )
        out["records"][str(app_id)] = adjs

    assert total == 92, f"Expected 92 eligible claims, got {total}"
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {total} adjudications to {OUT_PATH}")


if __name__ == "__main__":
    main()
