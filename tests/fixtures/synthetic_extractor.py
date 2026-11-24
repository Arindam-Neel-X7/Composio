"""Offline adapter fixture; refuses real packets. These are not app findings."""
import copy
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import research_pipeline as pipeline


def extract(packet):
    pipeline.require(packet["synthetic"] is True, "Fixture extractor accepts synthetic packets only")
    records = copy.deepcopy(packet["records"])
    for record in records:
        source = next(s for s in packet["sources"] if s["capture"]["spec"]["app_id"] == record["identity"]["id"])
        capture = source["capture"]
        numbered = source["numbered_text"].splitlines()
        lines = [line.split(": ", 1)[1] for line in numbered]
        scope = capture["spec"]["scope"]
        prefix = str(record["identity"]["id"]) + "."

        def observed(claim_id, value, contains):
            index = next(i for i, text in enumerate(lines, 1) if contains in text)
            return dict(claim_id=claim_id, status="observed", value=value, context=scope, evidence=[pipeline.evidence_for(capture, index, lines[index - 1])], supporting_claim_refs=[], rationale="Synthetic fixture extraction; not an app finding")

        record["identity"]["resolution"] = observed(prefix + "identity", "Synthetic stand-in identity only", "Example Service")
        record["purpose"] = observed(prefix + "purpose", "Synthetic workflow test product", "Example Service")
        record["auth"] = dict(coverage_status="partial", notes="Synthetic methods only; not exhaustive", items=[observed(prefix + "auth.oauth2", dict(method="OAuth2", context=scope, scopes=[], details="Authorization code; scopes not captured"), "OAuth2 authorization"), observed(prefix + "auth.key", dict(method="API_key", context=scope, scopes=[], details="Test-workspace API key"), "API key credentials")])
        record["api_surface"]["protocols"] = dict(coverage_status="partial", notes="Synthetic REST example", items=[observed(prefix + "api.rest", "REST", "A REST API")])
        record["api_surface"]["resource_groups"] = dict(coverage_status="partial", notes="One captured group, not complete inventory", items=[observed(prefix + "api.contacts", "Contacts", "A REST API")])
        breadth = observed(prefix + "api.breadth", "narrow", "A REST API")
        breadth.update(status="inferred", supporting_claim_refs=[prefix + "api.contacts"], rationale="One focused group in the synthetic evidence; no endpoint count claimed")
        record["api_surface"]["breadth"] = breadth
        for key in ("free_access", "sandbox_access", "self_serve"):
            record["credential_eligibility"]["testing"][key] = observed(prefix + "testing." + key, True, "Free sandbox credentials")
        entry = observed(prefix + "mcp.server", dict(origin="official", name="Synthetic callable server", source_url=capture["spec"]["url"], repository_url="https://synthetic.example/repository", server_url="https://synthetic.example/mcp", scope="Callable MCP server for synthetic workflow tools", operational_check=pipeline.unknown(prefix + "mcp.operational", scope)), "official callable MCP server")
        record["mcp"] = dict(discovery=observed(prefix + "mcp", "found", "official callable MCP server"), entries=[entry])
        build = observed(prefix + "buildability", dict(verdict="conditional", scope=scope, blockers=["Real product research and production eligibility still required"], next_steps=["Research actual primary documentation in the later pilot"]), "A REST API")
        build.update(status="inferred", supporting_claim_refs=[prefix + "identity", prefix + "api.rest"], rationale="Synthetic interface exists in fixture; this is not production feasibility evidence")
        record["buildability"] = build
    return dict(records=records)


if __name__ == "__main__":
    print(json.dumps(extract(json.load(sys.stdin))))
