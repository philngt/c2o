"""Structural integration tests, not evaluations of an agent's expertise."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_c2o_suites", ROOT / "scripts/validate_c2o.py")
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class SuiteDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "evals").mkdir()
        original = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
        self.suite = copy.deepcopy(original)
        self.suite["cases"] = self.suite["cases"][:1]
        self.write("scenarios.json", self.suite)

    def write(self, name, data):
        (self.root / "evals" / name).write_text(json.dumps(data), encoding="utf-8")

    def second_suite(self):
        data = copy.deepcopy(self.suite)
        data["cases"][0]["id"] = "second-fixture"
        return data

    def test_original_suite_remains_supported(self):
        self.assertEqual(CHECKER.scenario_suite_errors(self.root), [])

    def test_additional_suite_is_checked(self):
        data = self.second_suite()
        data["cases"][0]["skills"] = ["unknown-skill"]
        self.write("expertise-scenarios.json", data)
        self.assertTrue(any("unknown skill" in e for e in CHECKER.scenario_suite_errors(self.root)))

    def test_multiple_valid_suites(self):
        self.write("expertise-scenarios.json", self.second_suite())
        self.assertEqual(CHECKER.scenario_suite_errors(self.root), [])

    def test_duplicate_ids_across_suites(self):
        self.write("expertise-scenarios.json", self.suite)
        self.assertTrue(any("across suites" in e for e in CHECKER.scenario_suite_errors(self.root)))

    def test_missing_original_is_not_hidden_by_an_extra_suite(self):
        (self.root / "evals/scenarios.json").unlink()
        self.write("expertise-scenarios.json", self.second_suite())
        self.assertTrue(any("missing required" in e for e in CHECKER.scenario_suite_errors(self.root)))

    def test_invalid_json_is_reported_with_file(self):
        path = self.root / "evals/expertise-scenarios.json"
        path.write_text("{", encoding="utf-8")
        errors = CHECKER.scenario_suite_errors(self.root)
        self.assertTrue(any(str(path) in e and "scenario fixtures" in e for e in errors))

    def test_nonobject_suite_is_rejected_without_crashing(self):
        self.write("expertise-scenarios.json", [])
        self.assertTrue(CHECKER.scenario_suite_errors(self.root))

    def test_malformed_cases_are_rejected_without_crashing(self):
        for cases in (None, {}, [None], [{"id": []}]):
            with self.subTest(cases=cases):
                data = self.second_suite()
                data["cases"] = cases
                self.write("expertise-scenarios.json", data)
                self.assertTrue(CHECKER.scenario_suite_errors(self.root))

    def test_extra_suite_cannot_claim_execution(self):
        data = self.second_suite()
        data["execution_status"] = "pass"
        self.write("expertise-scenarios.json", data)
        self.assertTrue(any("executed results" in e for e in CHECKER.scenario_suite_errors(self.root)))

    def test_nonfixture_result_json_is_not_a_suite(self):
        self.write("results.json", {"status": "not-run"})
        self.assertEqual(CHECKER.scenario_suite_errors(self.root), [])

    def test_symlink_suite_is_rejected(self):
        target = self.root / "outside-scope.json"
        target.write_text("not JSON and must not be read", encoding="utf-8")
        link = self.root / "evals/expertise-scenarios.json"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable")
        errors = CHECKER.scenario_suite_errors(self.root)
        self.assertTrue(any("non-symlink" in e for e in errors))
        self.assertFalse(any("Expecting value" in e for e in errors))


class DiscoveryIntegrationTests(unittest.TestCase):
    def test_all_entrypoints_link_to_the_existing_shared_protocol(self):
        expected = (ROOT / "skills/c2o-work/references/expertise-discovery.md").resolve()
        self.assertTrue(expected.is_file())
        for name in CHECKER.SKILLS:
            path = ROOT / "skills" / name / "SKILL.md"
            targets = [match.group(1) for match in CHECKER.LINK.finditer(path.read_text(encoding="utf-8"))]
            with self.subTest(skill=name):
                self.assertTrue(any((path.parent / target).resolve() == expected for target in targets))
                self.assertEqual(CHECKER.local_link_errors(path, ROOT), [])

    def test_both_real_fixture_suites_validate_without_running_them(self):
        self.assertEqual(CHECKER.scenario_suite_errors(ROOT), [])
        paths = sorted((ROOT / "evals").glob("*scenarios.json"))
        self.assertIn(ROOT / "evals/expertise-scenarios.json", paths)
        self.assertIn(ROOT / "evals/scenarios.json", paths)
        for path in paths:
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["execution_status"], "not-run")
            self.assertEqual(CHECKER.scenario_errors(data), [])


if __name__ == "__main__":
    unittest.main()
