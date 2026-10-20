"""Behavior tests for record integrity, coverage and project-root boundaries."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1] / "tools" / "design_check.py"


class DesignCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="c2o-design-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.project = {
            "schema_version": "1.0", "project_name": "Test project",
            "platform": "web", "mode": "review", "owners": ["Example"],
            "criteria": [
                {"id": "C-001", "title": "Primary action works", "required": True,
                 "allow_not_applicable": False, "method": "manual"},
                {"id": "C-002", "title": "Second check", "required": True,
                 "allow_not_applicable": True, "type": "accessibility"},
            ],
        }
        self.write("src/screen.html", "<button>Save</button>\n")
        self.write("src/theme.css", "button { color: black; }\n")
        self.write(".design/evidence/review.md", "Reviewer observed the Save action.\n")
        self.save_project()
        self.report = {"schema_version": "1.0", "project_sha256": self.digest(".design/project.json"),
                       "results": [self.result("C-001"), self.result("C-002")]}

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def digest(self, name):
        return hashlib.sha256((self.root / name).read_bytes()).hexdigest()

    def reference(self, name):
        return {"path": name, "sha256": self.digest(name)}

    def result(self, identifier, status="PASS"):
        return {"criterion_id": identifier, "status": status, "rationale": "Recorded by a reviewer.",
                "inputs": [self.reference("src/screen.html"), self.reference("src/theme.css")],
                "evidence": [self.reference(".design/evidence/review.md")]}

    def save_project(self):
        self.write(".design/project.json", json.dumps(self.project, indent=2))

    def rebind(self):
        self.save_project()
        self.report["project_sha256"] = self.digest(".design/project.json")

    def run_cli(self, *args):
        process = subprocess.run([sys.executable, str(TOOL), *args, "--root", str(self.root),
                                  "--project", ".design/project.json"],
                                 capture_output=True, text=True, timeout=10)
        self.assertEqual(process.stderr, "", process.stderr)
        return process.returncode, json.loads(process.stdout)

    def validate(self):
        self.write(".design/verification.json", json.dumps(self.report, indent=2))
        return self.run_cli("validate", "--report", ".design/verification.json")

    def test_complete_current_records_are_ready_but_claim_only_records(self):
        code, output = self.validate()
        self.assertEqual(code, 0)
        self.assertEqual(output["outcome"], "RECORDS_READY")
        self.assertEqual(output["record_validity"]["status"], "VALID")
        self.assertEqual(output["required_coverage"]["passed"], ["C-001", "C-002"])
        self.assertIn("evidence truth was not verified", output["scope"])

    def test_pass_needs_both_input_and_evidence_references(self):
        for field in ("inputs", "evidence"):
            with self.subTest(field=field):
                self.report["results"][0] = self.result("C-001")
                self.report["results"][0][field] = []
                code, output = self.validate()
                self.assertEqual(code, 2)
                self.assertEqual(output["outcome"], "INVALID")
                self.assertIn("C-001", output["required_coverage"]["incomplete"])

    def test_missing_declared_input_is_invalid(self):
        (self.root / "src/theme.css").unlink()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["record_validity"]["status"], "INVALID")
        self.assertTrue(any(e["code"] == "FILE_UNAVAILABLE" for e in output["record_validity"]["errors"]))

    def test_changed_secondary_css_invalidates_every_dependent_pass(self):
        self.write("src/theme.css", "button { color: white; background: white; }\n")
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "STALE")
        self.assertEqual(output["required_coverage"]["passed"], [])
        self.assertEqual(output["required_coverage"]["incomplete"], ["C-001", "C-002"])

    def test_changed_evidence_is_stale_even_if_input_is_unchanged(self):
        self.write(".design/evidence/review.md", "A different review.\n")
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "STALE")

    def test_changed_project_invalidates_its_binding(self):
        self.project["criteria"][0]["title"] = "A stronger acceptance condition"
        self.save_project()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "STALE")
        self.assertFalse(output["record_validity"]["project_bound"])

    def test_zero_criteria_never_looks_ready(self):
        self.project["criteria"] = []
        self.report["results"] = []
        self.rebind()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["required_coverage"]["status"], "INCOMPLETE")

    def test_all_optional_never_looks_ready(self):
        for criterion in self.project["criteria"]:
            criterion["required"] = False
        self.rebind()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["required_coverage"]["required_count"], 0)

    def test_all_na_never_looks_ready(self):
        for criterion in self.project["criteria"]:
            criterion["allow_not_applicable"] = True
        for record in self.report["results"]:
            record.update(status="NOT_APPLICABLE", rationale="Outside the agreed scope.", inputs=[], evidence=[])
        self.rebind()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["record_validity"]["status"], "VALID")
        self.assertEqual(output["required_coverage"]["applicable_count"], 0)

    def test_na_requires_permission_and_rationale(self):
        self.report["results"][0]["status"] = "NOT_APPLICABLE"
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertTrue(any(e["code"] == "NA_NOT_ALLOWED" for e in output["record_validity"]["errors"]))
        self.report["results"][0] = self.result("C-001")
        self.report["results"][1].update(status="NOT_APPLICABLE", rationale="  ")
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertTrue(any(e["code"] == "RATIONALE_REQUIRED" for e in output["record_validity"]["errors"]))

    def test_allowed_na_with_an_applicable_pass_can_be_ready(self):
        self.report["results"][1].update(status="NOT_APPLICABLE", rationale="This release has no second flow.", inputs=[], evidence=[])
        code, output = self.validate()
        self.assertEqual(code, 0)
        self.assertEqual(output["required_coverage"]["not_applicable"], ["C-002"])

    def test_required_fail_exits_one_and_preserves_failure(self):
        self.report["results"][0]["status"] = "FAIL"
        code, output = self.validate()
        self.assertEqual(code, 1)
        self.assertEqual(output["outcome"], "REQUIREMENTS_FAILED")
        self.assertEqual(output["required_coverage"]["reported_failures"], ["C-001"])

    def test_fail_plus_not_run_exits_two_and_preserves_both(self):
        self.report["results"][0]["status"] = "FAIL"
        self.report["results"][1].update(status="NOT_RUN", inputs=[], evidence=[])
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "INCOMPLETE")
        self.assertEqual(output["required_coverage"]["reported_failures"], ["C-001"])
        self.assertEqual(output["required_coverage"]["incomplete"], ["C-002"])

    def test_blocked_requires_reason_and_remains_incomplete(self):
        self.report["results"][0].update(status="BLOCKED", rationale="", inputs=[], evidence=[])
        self.assertEqual(self.validate()[1]["outcome"], "INVALID")
        self.report["results"][0]["rationale"] = "Device unavailable."
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "INCOMPLETE")

    def test_missing_unknown_duplicate_results_and_duplicate_criteria(self):
        original = copy.deepcopy(self.report)
        self.report["results"].pop()
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["record_validity"]["missing_results"], ["C-002"])
        for record in (self.result("UNKNOWN"), self.result("C-001")):
            with self.subTest(record=record["criterion_id"]):
                self.report = copy.deepcopy(original)
                self.report["results"].append(record)
                self.assertEqual(self.validate()[1]["outcome"], "INVALID")
        self.report = original
        self.project["criteria"].append(copy.deepcopy(self.project["criteria"][0]))
        self.rebind()
        self.assertEqual(self.validate()[1]["outcome"], "INVALID")

    def test_path_traversal_absolute_and_windows_paths_are_rejected(self):
        for bad in ("../outside.txt", "/etc/passwd", "C:\\Windows\\win.ini", "src/../src/screen.html"):
            with self.subTest(path=bad):
                self.report["results"][0]["inputs"][0]["path"] = bad
                code, output = self.validate()
                self.assertEqual(code, 2)
                self.assertEqual(output["outcome"], "INVALID")

    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory(prefix="c2o-outside-") as outside:
            foreign = Path(outside) / "file.txt"
            foreign.write_text("outside", encoding="utf-8")
            link = self.root / "escaped.txt"
            try:
                link.symlink_to(foreign)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks are unavailable on this platform")
            self.report["results"][0]["inputs"][0] = {"path": "escaped.txt", "sha256": hashlib.sha256(b"outside").hexdigest()}
            self.assertEqual(self.validate()[1]["outcome"], "INVALID")

    def test_pending_template_is_incomplete_and_unbound(self):
        self.report["project_sha256"] = None
        for record in self.report["results"]:
            record.update(status="NOT_RUN", rationale="", inputs=[], evidence=[])
        code, output = self.validate()
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "INCOMPLETE")
        self.assertFalse(output["record_validity"]["project_bound"])

    def test_pass_cannot_use_a_null_project_binding(self):
        self.report["project_sha256"] = None
        self.assertEqual(self.validate()[1]["outcome"], "INVALID")

    def test_snapshot_emits_real_full_hashes_and_does_not_change_report(self):
        self.write(".design/verification.json", json.dumps(self.report))
        before = (self.root / ".design/verification.json").read_bytes()
        code, output = self.run_cli("snapshot", "--path", "src/theme.css")
        self.assertEqual(code, 0)
        self.assertEqual(output["project_sha256"], self.digest(".design/project.json"))
        self.assertEqual(output["files"], [self.reference("src/theme.css")])
        self.assertNotIn("status", output)
        self.assertEqual((self.root / ".design/verification.json").read_bytes(), before)

    def test_snapshot_missing_file_fails_without_partial_success(self):
        code, output = self.run_cli("snapshot", "--path", "missing.txt")
        self.assertEqual(code, 2)
        self.assertEqual(output["outcome"], "INVALID")

    def test_duplicate_json_key_is_rejected(self):
        self.write(".design/verification.json", '{"schema_version":"1.0","schema_version":"1.0"}')
        code, output = self.run_cli("validate", "--report", ".design/verification.json")
        self.assertEqual(code, 2)
        self.assertIn("duplicate JSON object key", output["record_validity"]["errors"][0]["message"])

    def test_hashes_are_checked_on_not_run_and_na_records_too(self):
        self.report["results"][1]["status"] = "NOT_APPLICABLE"
        self.write("src/theme.css", "changed")
        self.assertEqual(self.validate()[1]["outcome"], "STALE")
        self.report["results"][1]["status"] = "NOT_RUN"
        self.assertEqual(self.validate()[1]["outcome"], "STALE")


if __name__ == "__main__":
    unittest.main()
