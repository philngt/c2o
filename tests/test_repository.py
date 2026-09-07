"""Tests for structural validation; these are not model behavior evaluations."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_c2o", ROOT / "scripts/validate_c2o.py")
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class MetadataTests(unittest.TestCase):
    def sample(self, name="c2o-work", description="Perform bounded work."):
        return f"---\nname: {name}\ndescription: {description}\n---\n\n# Work\n"

    def test_valid(self):
        self.assertEqual(CHECKER.metadata(self.sample())["name"], "c2o-work")

    def test_missing_opening(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata("name: c2o-work\n")

    def test_missing_closing(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata("---\nname: c2o-work\n")

    def test_duplicate_name(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata(self.sample().replace("name: c2o-work", "name: c2o-work\nname: c2o-work"))

    def test_empty_description(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata(self.sample(description=" "))

    def test_long_description(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata(self.sample(description="x" * 1025))

    def test_invalid_names(self):
        for name in ("C2O-work", "-work", "work-", "c2o--work", "a" * 65):
            with self.subTest(name=name), self.assertRaises(ValueError):
                CHECKER.metadata(self.sample(name=name))

    def test_unsupported_multiline_is_explicit(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata(self.sample(description="|\n  Multiline description."))

    def test_ambiguous_yaml_scalar(self):
        with self.assertRaises(ValueError):
            CHECKER.metadata(self.sample(description="Example: a value"))


class LinkTests(unittest.TestCase):
    def check(self, body, with_target=False):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "guide.md"
            path.write_text(body, encoding="utf-8")
            if with_target:
                (root / "target.md").write_text("# Target\n", encoding="utf-8")
            return CHECKER.local_link_errors(path, root)

    def test_existing_target(self):
        self.assertEqual(self.check("[target](target.md)", True), [])

    def test_missing_target(self):
        self.assertTrue(self.check("[target](missing.md)"))

    def test_outside_repository(self):
        self.assertTrue(self.check("[target](../outside.md)"))

    def test_external_and_anchor(self):
        self.assertEqual(self.check("[web](https://example.com) [here](#section)"), [])

    def test_fenced_example_ignored(self):
        self.assertEqual(self.check("```markdown\n[x](missing.md)\n```\n"), [])

    def test_fragment_on_existing_file(self):
        self.assertEqual(self.check("[target](target.md#heading)", True), [])


class ScenarioTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))

    def test_valid_fixtures(self):
        self.assertEqual(CHECKER.scenario_errors(self.data), [])

    def test_all_three_groups_and_eleven_skills_covered(self):
        self.assertEqual({case["group"] for case in self.data["cases"]}, CHECKER.GROUPS)
        self.assertEqual({name for case in self.data["cases"] for name in case["skills"]}, CHECKER.SKILLS)

    def test_duplicate_case_id(self):
        self.data["cases"].append(copy.deepcopy(self.data["cases"][0]))
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_unknown_skill(self):
        self.data["cases"][0]["skills"] = ["c2o-made-up"]
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_nonstring_skill(self):
        self.data["cases"][0]["skills"] = [{}]
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_missing_authorization(self):
        del self.data["cases"][0]["environment"]["authorization"]
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_unsafe_fixture_paths(self):
        for name in ("../secret", "/tmp/file", "C:\\temp\\file", "a/../../file", ".", "", "null\0file"):
            with self.subTest(name=name):
                data = copy.deepcopy(self.data)
                data["cases"][0]["fixtures"] = {name: "content"}
                self.assertTrue(CHECKER.scenario_errors(data))

    def test_missing_negative_expectation(self):
        self.data["cases"][0]["must_not"] = []
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_fixtures_cannot_claim_executed(self):
        self.data["execution_status"] = "pass"
        self.assertTrue(CHECKER.scenario_errors(self.data))

    def test_malformed_suite_and_case(self):
        for data in (None, [], {}, {"schema_version": 1, "cases": [None]}):
            with self.subTest(data=data):
                self.assertTrue(CHECKER.scenario_errors(data))

    def test_nonstring_group(self):
        self.data["cases"][0]["group"] = []
        self.assertTrue(CHECKER.scenario_errors(self.data))


class RepositoryTests(unittest.TestCase):
    def test_repository_structure(self):
        self.assertEqual(CHECKER.validate(ROOT), [])

    def test_missing_repository_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertTrue(CHECKER.validate(Path(directory)))

    def test_cli_failure_exit_status(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/validate_c2o.py"), "--root", directory],
                text=True, capture_output=True, check=False,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL", result.stdout)

    def test_cli_success_does_not_claim_model_evaluation(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/validate_c2o.py"), "--root", str(ROOT)],
            text=True, capture_output=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("behavioral evaluations were not executed", result.stdout)


if __name__ == "__main__":
    unittest.main()
