"""Structural regression checks only; these do not execute or grade an agent."""
from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_c2o_domain", ROOT / "scripts/validate_c2o.py")
assert SPEC and SPEC.loader
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)
REFERENCE = ROOT / "skills/c2o-work/references/domain-context.md"
ENTRYPOINTS = ("work", "shape", "decide", "create", "verify", "learn")
SUITE = ROOT / "evals/domain-context-scenarios.json"
CONTROLS = frozenset(
    "plain-markdown no-provider missing-reference wrong-workspace untrusted-content "
    "rule-exception source-conflict metadata-only stale-evidence review-only "
    "scoped-learning cross-domain qualified-review tiny-task".split()
)


class DomainContextIntegrationTests(unittest.TestCase):
    def test_selected_entrypoints_link_to_one_shared_reference(self):
        self.assertTrue(REFERENCE.is_file())
        for name in ENTRYPOINTS:
            path = ROOT / f"skills/c2o-{name}/SKILL.md"
            targets = [match.group(1) for match in CHECKER.LINK.finditer(path.read_text(encoding="utf-8"))]
            with self.subTest(skill=name):
                self.assertEqual(
                    sum((path.parent / target).resolve() == REFERENCE.resolve() for target in targets),
                    1,
                )

    def test_entrypoint_metadata_and_size_remain_compatible(self):
        for name in ENTRYPOINTS:
            text = (ROOT / f"skills/c2o-{name}/SKILL.md").read_text(encoding="utf-8")
            with self.subTest(skill=name):
                self.assertEqual(CHECKER.metadata(text)["name"], f"c2o-{name}")
                self.assertLess(len(text.splitlines()), 500)

    def test_entrypoints_document_missing_reference_fallback(self):
        # A packaging/documentation check, not proof that a model follows a fallback.
        for name in ENTRYPOINTS:
            text = (ROOT / f"skills/c2o-{name}/SKILL.md").read_text(encoding="utf-8")
            paragraphs = [p for p in text.split("\n\n") if "domain-context.md" in p]
            with self.subTest(skill=name):
                self.assertEqual(len(paragraphs), 1)
                if name == "work":
                    self.assertIn("If the reference cannot load, retain these minimum rules", text)
                else:
                    self.assertRegex(paragraphs[0], r"If the reference|if the reference")

    def test_new_reference_and_guide_have_resolvable_local_links(self):
        for path in (REFERENCE, ROOT / "docs/domain-context.md"):
            with self.subTest(path=path):
                self.assertEqual(CHECKER.local_link_errors(path, ROOT), [])

    def test_shared_reference_remains_bounded_optional_guidance(self):
        text = REFERENCE.read_text(encoding="utf-8")
        self.assertLess(len(text.splitlines()), 180)
        self.assertIn("C2O works without a context provider", text)
        self.assertIn("not a required provider interchange schema", text)
        self.assertIn("not a validated intelligence hierarchy", text)


class DomainContextScenarioTests(unittest.TestCase):
    def setUp(self):
        self.suite = json.loads(SUITE.read_text(encoding="utf-8"))

    def test_fixture_suite_is_valid_and_not_presented_as_execution(self):
        self.assertEqual(CHECKER.scenario_errors(self.suite), [])
        self.assertEqual(self.suite["execution_status"], "not-run")
        self.assertEqual(self.suite["kind"], "synthetic-behavioral-scenarios")

    def test_required_regression_controls_remain_present(self):
        identifiers = {case["id"] for case in self.suite["cases"]}
        self.assertTrue({"domain-" + name for name in CONTROLS}.issubset(identifiers))
        self.assertEqual(len(identifiers), len(self.suite["cases"]))

    def test_fixture_cannot_claim_executed_success(self):
        self.suite["execution_status"] = "pass"
        self.assertTrue(any("executed results" in e for e in CHECKER.scenario_errors(self.suite)))

    def test_unknown_skill_is_rejected(self):
        self.suite["cases"][0]["skills"] = ["c2o-cognition"]
        self.assertTrue(any("unknown skill" in e for e in CHECKER.scenario_errors(self.suite)))

    def test_unsafe_fixture_paths_are_rejected(self):
        for path in ("../shared.md", "/etc/config", "C:\\config", "bad\nname"):
            with self.subTest(path=path):
                data = copy.deepcopy(self.suite)
                data["cases"][0]["fixtures"][path] = "not to be materialized"
                self.assertTrue(any("unsafe fixture" in e for e in CHECKER.scenario_errors(data)))

    def temporary_suites(self, duplicate=False):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / "evals").mkdir()
        baseline = copy.deepcopy(self.suite)
        baseline["cases"] = baseline["cases"][:1]
        if not duplicate:
            baseline["cases"][0]["id"] = "baseline-control"
        (root / "evals/scenarios.json").write_text(json.dumps(baseline), encoding="utf-8")
        (root / "evals/domain-context-scenarios.json").write_text(json.dumps(self.suite), encoding="utf-8")
        return root

    def test_existing_discovery_includes_new_suite(self):
        self.assertEqual(CHECKER.scenario_suite_errors(self.temporary_suites()), [])

    def test_duplicate_ids_across_suites_are_rejected(self):
        errors = CHECKER.scenario_suite_errors(self.temporary_suites(duplicate=True))
        self.assertTrue(any("duplicate case id across suites" in e for e in errors))

    def test_invalid_new_suite_does_not_hide_valid_baseline(self):
        root = self.temporary_suites()
        path = root / "evals/domain-context-scenarios.json"
        self.suite["cases"][0]["environment"].pop("authorization")
        path.write_text(json.dumps(self.suite), encoding="utf-8")
        errors = CHECKER.scenario_suite_errors(root)
        self.assertTrue(any(str(path) in e and "authorization boundary" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
