"""Guard catalog coverage and catch structural drift without editing templates."""

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


FRAMEWORK = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("template_check", FRAMEWORK / "tools/template_check.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class TemplateCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(FRAMEWORK / "templates", self.root / "templates")
        (self.root / "documentation").mkdir()
        self.registry_path = self.root / checker.REGISTRY
        shutil.copyfile(FRAMEWORK / checker.REGISTRY, self.registry_path)
        self.brief = self.root / "templates/brief.md"

    def registry(self):
        return json.loads(self.registry_path.read_text(encoding="utf-8"))

    def write_registry(self, value):
        self.registry_path.write_text(json.dumps(value), encoding="utf-8")

    def invalid(self, message):
        result = checker.validate(self.root)
        self.assertEqual(result["status"], "TEMPLATES_INVALID")
        self.assertTrue(any(message in item for item in result["errors"]), result)

    def test_real_catalog_is_valid_and_read_only(self):
        before = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        result = checker.validate(self.root)
        self.assertEqual(result["status"], "TEMPLATES_VALID", result)
        self.assertEqual(result["checked"], len(self.registry()["templates"]))
        self.assertEqual(before, {path: path.read_bytes() for path in before})

    def test_metadata_cannot_confuse_decision_state_with_document_state(self):
        original = self.brief.read_text(encoding="utf-8")
        for replacement, error in [
            ("| Trạng thái tài liệu | `selected` |", "default to draft"),
            ("| Trạng thái tài liệu | |", "empty contract field"),
            ("| Trạng thái quyết định | `draft` |", "field names/order"),
        ]:
            with self.subTest(replacement=replacement):
                self.brief.write_text(original.replace("| Trạng thái tài liệu | `draft` |", replacement), encoding="utf-8")
                self.invalid(error)

    def test_registry_detects_unregistered_missing_and_duplicate_templates(self):
        original = self.registry()
        value = self.registry()
        value["templates"].pop()
        self.write_registry(value)
        self.invalid("unregistered template")
        self.write_registry(original)
        self.brief.unlink()
        self.invalid("registered template missing")
        shutil.copyfile(FRAMEWORK / "templates/brief.md", self.brief)
        value = self.registry()
        value["templates"].append(value["templates"][0].copy())
        self.write_registry(value)
        self.invalid("duplicate template ID")
        self.invalid("duplicate template path")

    def test_malformed_registry_is_an_error_not_a_crash(self):
        for value in ([], {"schema_version": "future"}, {"schema_version": "1.0", "standard_version": "1.0.0", "templates": [None]}):
            with self.subTest(value=value):
                self.write_registry(value)
                self.assertEqual(checker.validate(self.root)["status"], "TEMPLATES_INVALID")
        self.registry_path.write_text('{"schema_version":"1.0","schema_version":"1.0"}', encoding="utf-8")
        self.invalid("duplicate JSON key")

    def test_registry_rejects_path_escape_and_version_mismatch(self):
        original = self.registry()
        value = self.registry()
        value["templates"][0]["path"] = "../outside.md"
        self.write_registry(value)
        self.invalid("unsafe or unsupported template path")
        value = original
        value["templates"][0]["version"] = "1.0.1"
        self.write_registry(value)
        self.invalid("template version differs")

    def test_handoff_is_last_and_not_pre_checked(self):
        original = self.brief.read_text(encoding="utf-8")
        self.brief.write_text(original + "\n## Late instructions\n\nA competing final section.\n", encoding="utf-8")
        self.invalid("last H2")
        self.brief.write_text(original.replace("- [ ]", "- [x]", 1), encoding="utf-8")
        self.invalid("must not be pre-checked")

    def test_literal_pipe_requires_escaping_in_metadata(self):
        original = self.brief.read_text(encoding="utf-8")
        self.brief.write_text(original.replace("[YYYY-MM-DD]", "date | revision"), encoding="utf-8")
        self.invalid("two columns")
        self.brief.write_text(original.replace("[YYYY-MM-DD]", r"date \| revision"), encoding="utf-8")
        self.assertEqual(checker.validate(self.root)["status"], "TEMPLATES_VALID")

    def test_metadata_table_cannot_be_split_by_blank_line_or_prose(self):
        original = self.brief.read_text(encoding="utf-8")
        for separator in ("\n", "Unexpected paragraph.\n"):
            with self.subTest(separator=separator):
                self.brief.write_text(original.replace("| Owner |", separator + "| Owner |"), encoding="utf-8")
                self.invalid("contiguous table")

    def test_unresolvable_symlink_returns_invalid_instead_of_crashing(self):
        self.brief.unlink()
        try:
            self.brief.symlink_to("brief.md")
            root_loop = self.root / "root-loop"
            root_loop.symlink_to("root-loop")
        except (OSError, NotImplementedError) as error:
            self.skipTest("symlinks unavailable: " + str(error))
        self.assertEqual(checker.validate(self.root)["status"], "TEMPLATES_INVALID")
        self.assertEqual(checker.validate(root_loop)["status"], "TEMPLATES_INVALID")

    def test_other_task_list_bullets_cannot_hide_pre_checked_items(self):
        original = self.brief.read_text(encoding="utf-8")
        for item in ("+ [x] Checked", "  - [x] Checked", "1. [x] Checked"):
            with self.subTest(item=item):
                self.brief.write_text(original + "\n" + item + "\n", encoding="utf-8")
                self.invalid("must not be pre-checked")

    def test_fence_with_info_is_not_a_closing_fence(self):
        original = self.brief.read_text(encoding="utf-8")
        example = "```text\n```python\n# Example inside code\n```\n\n"
        self.brief.write_text(original.replace("## Kiểm tra trước bàn giao", example + "## Kiểm tra trước bàn giao"), encoding="utf-8")
        self.assertEqual(checker.validate(self.root)["status"], "TEMPLATES_VALID")

    def test_standard_reference_is_a_real_inline_markdown_link(self):
        original = self.brief.read_text(encoding="utf-8")
        link = "[Chuẩn template](../documentation/template-standard.md)"
        self.assertIn(link, original)
        for replacement in ("(../documentation/template-standard.md)", "`" + link + "`"):
            with self.subTest(replacement=replacement):
                self.brief.write_text(original.replace(link, replacement), encoding="utf-8")
                self.invalid("must link")


if __name__ == "__main__":
    unittest.main()
