"""Synthetic format/grounding regressions. No real app research or network."""
import copy
import importlib.util
import json
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import unittest
import urllib.error

import research_pipeline as p

fixture_module = importlib.util.spec_from_file_location("synthetic_extractor", p.ROOT / "tests/fixtures/synthetic_extractor.py")
fixture = importlib.util.module_from_spec(fixture_module)
fixture_module.loader.exec_module(fixture)


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        scratch = p.ROOT / "work/task-03-agent"
        scratch.mkdir(parents=True, exist_ok=True)
        cls.store = Path(tempfile.mkdtemp(prefix="synthetic-tests-", dir=scratch))
        cls.spec = p.read_json(p.ROOT / "tests/fixtures/sources.json")["sources"][0]
        cls.raw = p.create_run(cls.store, "captured", ids=[2], source_specs=[cls.spec], synthetic=True)
        cls.extraction = fixture.extract(p.read_json(cls.raw / "packet.json"))
        cls.done = p.create_run(cls.store, "extracted", parent_id="captured", extraction=copy.deepcopy(cls.extraction), reason="Synthetic first extraction")
        cls.base = p.read_json(cls.done / "records.json")[0]
        cls.roster = {a["id"]: a for a in p.read_json(p.ROOT / "data/apps.json")["apps"]}
        cls.captures = p.read_json(cls.done / "captures.json")

    def check_record(self, record):
        p.validate_record(record, self.roster[2], self.done, self.captures, p.ancestors(self.store, "extracted"))

    def rejected(self, edit, pattern):
        record = copy.deepcopy(self.base)
        edit(record)
        with self.assertRaisesRegex(ValueError, pattern):
            self.check_record(record)

    def test_01_capture_extract_and_packet(self):
        self.assertEqual(p.validation(self.done)["structure_and_grounding"], "passed")
        packet = p.read_json(self.raw / "packet.json")
        self.assertTrue(packet["synthetic"])
        self.assertGreater(len(packet["candidate_excerpts"]), 3)
        self.assertNotIn("SECRET_SCRIPT_TEXT", packet["sources"][0]["numbered_text"])
        self.assertEqual(len(self.base["auth"]["items"]), 2)
        self.assertEqual(self.base["credential_eligibility"]["production"]["free_access"]["status"], "not_researched")
        for event in (self.done / "events.jsonl").read_text().splitlines():
            json.loads(event)

    def test_02_external_adapter_cli(self):
        argv = [sys.executable, "-B", str(p.ROOT / "tests/fixtures/synthetic_extractor.py")]
        result = subprocess.run([sys.executable, "-B", str(p.ROOT / "research_pipeline.py"), "--store", str(self.store), "extract", "--run-id", "external", "--parent", "captured", "--reason", "Synthetic adapter integration", "--extractor-command-json", json.dumps(argv), "--extractor-label", "deterministic-fixture-v1"], capture_output=True, text=True, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(p.verify_seal(self.store / "external")["synthetic"])
        self.assertEqual(p.read_json(self.store / "external/manifest.json")["config"]["extractor_label"], "deterministic-fixture-v1")

    def test_03_schema_rejects_evidence_free_assertion(self):
        record = copy.deepcopy(self.base)
        record["purpose"]["evidence"] = []
        with self.assertRaisesRegex(ValueError, "Schema"):
            p.validate_shape([record], p.ROOT / "schemas/record.json")

    def test_04_roster_and_identity_gate(self):
        self.rejected(lambda r: r["identity"].update(app="Another product"), "Roster")
        self.rejected(lambda r: r["identity"]["resolution"].update(status="unknown", value=None), "identity unresolved")
        record = p.empty_record(self.roster[84], self.base["run"])
        record["purpose"] = copy.deepcopy(self.base["purpose"])
        record["purpose"]["claim_id"] = "84.purpose"
        with self.assertRaises(ValueError):
            p.validate_record(record, self.roster[84], self.done, self.captures, {})

    def test_05_duplicate_missing_self_and_cyclic_refs(self):
        self.rejected(lambda r: r["purpose"].update(claim_id=r["identity"]["resolution"]["claim_id"]), "Duplicate")
        self.rejected(lambda r: r["buildability"].update(supporting_claim_refs=["2.missing"]), "reference")
        self.rejected(lambda r: r["purpose"].update(supporting_claim_refs=["2.purpose"]), "self")
        def cycle(r):
            r["purpose"]["supporting_claim_refs"] = ["2.identity"]
            r["identity"]["resolution"]["supporting_claim_refs"] = ["2.purpose"]
        self.rejected(cycle, "Cyclic")

    def test_06_hash_path_locator_and_literal_anchor(self):
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(content_sha256="0" * 64), "hash mismatch")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(snapshot_ref="../outside.txt"), "escapes")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(locator="lines:999"), "outside")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(observation="quote: Invented literal observation"), "not anchored")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(snapshot_ref="snapshots/invented.txt"), "Missing")

    def test_07_source_attribution_date_and_scope(self):
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(source_kind="community_docs"), "attribution")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(captured_on="2099-01-01"), "future")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(captured_on="2026-99-99"), "month")
        self.rejected(lambda r: r["purpose"].update(context="Different edition"), "unique captured")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(source_url="file:///invented"), "HTTP")
        self.rejected(lambda r: r["purpose"]["evidence"][0].update(source_kind="assignment"), "Assignment")

    def test_08_credential_environment(self):
        def wrong_environment(r):
            claim = copy.deepcopy(r["credential_eligibility"]["testing"]["free_access"])
            claim["claim_id"] = "2.production.free_access"
            r["credential_eligibility"]["production"]["free_access"] = claim
        self.rejected(wrong_environment, "environment")

    def test_09_breadth_and_buildability_dependencies(self):
        self.rejected(lambda r: r["api_surface"]["breadth"].update(status="observed"), "explicit inference")
        self.rejected(lambda r: r["api_surface"]["breadth"].update(supporting_claim_refs=["2.purpose"]), "resource-group")
        self.rejected(lambda r: r["buildability"].update(supporting_claim_refs=["2.purpose"]), "identity and API")
        def build_now(r):
            r["buildability"]["value"]["verdict"] = "build_now"
        self.rejected(build_now, "auth and credential")
        self.rejected(lambda r: r["buildability"].update(supporting_claim_refs=["2.api.public_documentation"]), "unknown claim")

    def test_10_collection_and_mcp_guards(self):
        self.rejected(lambda r: r["auth"].update(coverage_status="not_researched"), "Assertions under")
        self.rejected(lambda r: r["mcp"].update(entries=[]), "MCP found")
        self.rejected(lambda r: r["mcp"]["discovery"].update(status="unknown", value=None), "MCP found")
        self.rejected(lambda r: r["mcp"]["entries"][0]["value"].update(scope="client-only connection"), "direction")
        self.rejected(lambda r: r["mcp"]["entries"][0]["value"].update(server_url="https://invented.example/mcp"), "not present")
        self.rejected(lambda r: r["purpose"].update(status="not_found_in_checked_sources", value=None), "only applies to MCP")
        self.rejected(lambda r: r["mcp"]["entries"][0]["value"]["operational_check"].update(status="observed", value=True), "Operational")

    def test_11_correction_and_conflict_references(self):
        self.rejected(lambda r: r["run"].update(correction_refs=[dict(run_id="nonexistent", claim_id="2.purpose", reason="fixture")]), "correction")
        self.rejected(lambda r: r.update(conflicts=[dict(claim_refs=["2.purpose", "2.nope"], description="fixture", detected_on=p.today())]), "conflict")

    def test_12_immutable_parent_child_and_replay(self):
        before = p.digest((self.raw / "records.json").read_bytes())
        child = p.create_run(self.store, "replayed", parent_id="captured", replay=True)
        self.assertEqual(p.digest((self.raw / "records.json").read_bytes()), before)
        self.assertEqual(p.read_json(child / "captures.json"), p.read_json(self.raw / "captures.json"))
        with self.assertRaises(FileExistsError):
            p.create_run(self.store, "captured", ids=[2], synthetic=True)
        self.assertTrue(p.read_json(self.done / "changes.json"))
        self.assertTrue(self.base["run"]["correction_refs"])

    def test_13_failure_recovery_and_failure_receipt(self):
        bad = dict(self.spec, fixture="tests/fixtures/missing.html")
        failed = p.create_run(self.store, "fetch-failed", ids=[2], source_specs=[bad], synthetic=True, retries=0)
        self.assertEqual(p.read_json(failed / "captures.json"), [])
        self.assertIsNone(p.metrics(self.store, "fetch-failed")["overall"]["accuracy"])
        recovered = p.create_run(self.store, "recovered", parent_id="fetch-failed", source_specs=[self.spec])
        self.assertEqual(len(p.read_json(recovered / "captures.json")), 1)
        incoming = copy.deepcopy(self.extraction)
        incoming["records"][0]["purpose"]["evidence"] = []
        with self.assertRaisesRegex(ValueError, "Schema"):
            p.create_run(self.store, "rejected", parent_id="captured", extraction=incoming, reason="Synthetic invalid intake")
        self.assertEqual(p.read_json(self.store / "rejected/manifest.json")["status"], "incomplete")
        with self.assertRaisesRegex(ValueError, "rejected"):
            p.verify_seal(self.store / "rejected")

    def test_14_bounded_retries_status_and_redaction(self):
        spec = {k: v for k, v in self.spec.items() if k != "fixture"}
        calls = []
        def getter(url, timeout):
            calls.append(timeout)
            if len(calls) == 1:
                raise urllib.error.URLError(socket.gaierror("secret exception text"))
            return 200, url, "text/plain", b"Synthetic retry success\n"
        attempts, capture, text = p.collect_source(spec, False, retries=1, getter=getter)
        self.assertEqual([a["status"] for a in attempts], ["dns_error", "fetched"])
        self.assertNotIn("secret", json.dumps(attempts))
        self.assertEqual(len(calls), 2)
        def forbidden(url, timeout):
            raise urllib.error.HTTPError(url, 403, "private", {}, None)
        attempts, _, _ = p.collect_source(spec, False, retries=3, getter=forbidden)
        self.assertEqual(len(attempts), 1)
        self.assertEqual(attempts[0]["status"], "blocked")
        with self.assertRaises(ValueError):
            p.collect_source(spec, False, timeout=999)
        with self.assertRaises(ValueError):
            p.public_url("https://user:secret@example.com/docs")
        with self.assertRaises(ValueError):
            p.public_url("https://example.com/docs?token=secret&language=en")

    def test_15_review_metrics_and_unknown_denominators(self):
        empty = p.metrics(self.store, "captured")
        self.assertEqual(empty["app_findings_total"], 0)
        self.assertIsNone(empty["overall"]["accuracy"])
        ids = [i["claim_id"] for i in p.read_json(self.done / "inventory.json") if i["eligible"]]
        evidence = self.base["purpose"]["evidence"]
        judgments = [dict(claim_id=claim_id, judgment=outcome, reason="Synthetic adjudication; no real accuracy measured", evidence=evidence, original_run_id="extracted") for claim_id, outcome in zip(ids, ["correct", "incorrect", "unsupported", "unresolved", "not_applicable"])]
        reviewer = dict(id="independent-synthetic-reviewer", type="ai", records={"2": judgments})
        p.create_run(self.store, "reviewed", parent_id="extracted", reviewer=reviewer)
        report = p.metrics(self.store, "reviewed", "extracted")
        self.assertEqual(report["overall"]["denominator"], 3)
        self.assertAlmostEqual(report["overall"]["accuracy"], 1 / 3)
        self.assertEqual(report["overall"]["unresolved"], 1)
        self.assertEqual(report["overall"]["pending"], len(ids) - 5)
        self.assertEqual(report["app_findings_total"], 0)
        self.assertEqual(report["overall"]["eligible"], len(ids))

    def test_16_review_identity_and_targets(self):
        def self_review(r):
            r["review"] = dict(status="completed", reviewer=dict(id=r["run"]["producer"]["id"], type="ai"), reviewed_on=p.today(), adjudications=[])
        self.rejected(self_review, "Self-review")
        def wrong_target(r):
            r["review"] = dict(status="completed", reviewer=dict(id="someone-else", type="ai"), reviewed_on=p.today(), adjudications=[dict(claim_id="2.purpose", judgment="unresolved", evidence=[], reason="fetches[0]", original_run_id="missing")])
        self.rejected(wrong_target, "target")
        with self.assertRaisesRegex(ValueError, "attestation"):
            p.create_run(self.store, "false-human", parent_id="extracted", reviewer=dict(id="person", type="human", records={}))

    def test_17_same_page_multiple_scopes(self):
        other = dict(self.spec, scope="SYNTHETIC second scope")
        directory = p.create_run(self.store, "two-scopes", ids=[2], source_specs=[self.spec, other], synthetic=True)
        extracted = fixture.extract(p.read_json(directory / "packet.json"))
        child = p.create_run(self.store, "two-scopes-extracted", parent_id="two-scopes", extraction=extracted, reason="Synthetic scope matching")
        self.assertEqual(p.validation(child)["structure_and_grounding"], "passed")

    def test_18_seal_detects_mutation(self):
        child = p.create_run(self.store, "tampered", parent_id="captured", replay=True)
        # Deliberate integrity-test corruption of this test's own disposable run only.
        (child / "records.json").write_bytes(b"[]")
        with self.assertRaisesRegex(ValueError, "seal mismatch"):
            p.verify_seal(child)

    def test_19_malformed_extraction_is_not_a_collector_run(self):
        for index, payload in enumerate(({}, [], {"records": None}, {"records": "invalid"})):
            with self.subTest(payload=payload):
                with self.assertRaisesRegex(ValueError, "records list"):
                    p.create_run(self.store, "bad-extraction-" + str(index), parent_id="captured", extraction=payload, reason="Synthetic malformed input")
                self.assertFalse((self.store / ("bad-extraction-" + str(index))).exists())
        # CLI null is invalid extraction; Python None remains the explicit no-extraction default.
        with self.assertRaisesRegex(ValueError, "null/empty"):
            p.main(["--store", str(self.store), "extract", "--run-id", "null-extraction", "--parent", "captured", "--reason", "Synthetic null output", "--extractor-label", "null-fixture", "--extractor-command-json", json.dumps([sys.executable, "-c", "print('null')"])])
        self.assertFalse((self.store / "null-extraction").exists())

    def test_20_vendor_vs_partner_approval_v1_1(self):
        self.assertEqual(self.base["schema_version"], "1.1")
        for env in ("testing", "production"):
            self.assertIn("vendor_approval_required", self.base["credential_eligibility"][env])
            self.assertIn("partner_approval_required", self.base["credential_eligibility"][env])
        example = p.read_json(p.ROOT / "examples/unresearched-record.json")
        self.assertEqual(p.validate_shape([example], p.ROOT / "schemas/record.json"), "Python jsonschema Draft202012Validator")
        broken = copy.deepcopy(example)
        del broken["credential_eligibility"]["production"]["vendor_approval_required"]
        with self.assertRaisesRegex(ValueError, "Schema"):
            p.validate_shape([broken], p.ROOT / "schemas/record.json")

    def test_21_collector_guard_codes_and_max_bytes(self):
        spec = {k: v for k, v in self.spec.items() if k != "fixture"}
        big = b"<html><body><p>" + (b"a" * 200_000) + b"</p></body></html>"
        attempts, cap, _ = p.collect_source(spec, False, retries=0, getter=lambda u, t: (200, u, "text/html", big), max_bytes=150_000)
        self.assertIsNone(cap)
        self.assertEqual(attempts[0]["error"], "Capture failed: size_limit_exceeded")
        attempts_ok, cap_ok, _ = p.collect_source(spec, False, retries=0, getter=lambda u, t: (200, u, "text/html", big), max_bytes=300_000)
        self.assertIsNotNone(cap_ok)
        self.assertEqual(attempts_ok[0]["status"], "fetched")
        attempts_ct, cap_ct, _ = p.collect_source(spec, False, retries=0, getter=lambda u, t: (200, u, "application/pdf", b"%PDF-1.4"))
        self.assertIsNone(cap_ct)
        self.assertEqual(attempts_ct[0]["error"], "Capture failed: unsupported_content_type")
        attempts_empty, cap_empty, _ = p.collect_source(spec, False, retries=0, getter=lambda u, t: (200, u, "text/html", b"<html><body><script>var x=1;</script></body></html>"))
        self.assertIsNone(cap_empty)
        self.assertEqual(attempts_empty[0]["error"], "Capture failed: empty_readable_content")

    def test_22_html_hydration_json_stripping(self):
        hydration = '{"docsConfig":{"name":"Demo"},"compiledSource":"' + ("x" * 600) + '"}'
        html = f"<html><body><h1>Usage</h1><p>Visible line</p><template>Hidden template</template><p>{hydration}</p></body></html>".encode("utf-8")
        text = p.readable(html, "text/html")
        self.assertIn("Visible line", text)
        self.assertNotIn("Hidden template", text)
        self.assertNotIn("compiledSource", text)
        # Non-HTML application/json must NOT be stripped
        raw_json = hydration.encode("utf-8")
        self.assertIn("compiledSource", p.readable(raw_json, "application/json"))

    def test_23_reproducible_stratified_sampling(self):
        m1 = p.build_sample(seed="unit-test-seed-v1", per_category=2)
        m2 = p.build_sample(seed="unit-test-seed-v1", per_category=2)
        self.assertEqual(m1["selected_ids"], m2["selected_ids"])
        self.assertEqual(m1["total_selected"], 20)
        self.assertEqual(len(set(m1["selected_ids"])), 20)
        self.assertEqual(len(m1["category_counts"]), 10)
        self.assertIn("Support and Helpdesk", m1["category_counts"])
        self.assertTrue(all(v == 2 for v in m1["category_counts"].values()))
        out_path = self.store / "frozen-sample.json"
        p.build_sample(seed="unit-test-seed-v1", per_category=2, output_path=out_path)
        self.assertTrue(out_path.is_file())
        with self.assertRaises(FileExistsError):
            p.build_sample(seed="unit-test-seed-v1", per_category=2, output_path=out_path)


if __name__ == "__main__":
    unittest.main()
