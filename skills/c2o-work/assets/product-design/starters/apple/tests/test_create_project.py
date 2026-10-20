import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("create_project", ROOT / "create_project.py")
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


class CreateProjectTests(unittest.TestCase):
    def test_both_categories_with_and_without_widgets(self):
        for category in ["lifestyle", "utility"]:
            for widgets in [False, True]:
                with self.subTest(category=category, widgets=widgets), tempfile.TemporaryDirectory() as tmp:
                    out = Path(tmp) / "App"
                    generator.create_project(out, "MyApp", "com.example.myapp", category, "Ứng dụng", widgets)
                    project = json.loads((out / "project.json").read_text())
                    self.assertEqual(len(project["targets"]), 4 if widgets else 2)
                    self.assertTrue((out / "StarterCore/Package.swift").is_file())
                    self.assertEqual((out / "Widgets").exists(), widgets)
                    self.assertTrue(any((out / "App").rglob("*.swift")))
                    for name, target in project["targets"].items():
                        info = target["info"]["properties"]
                        self.assertEqual(info["C2OCategory"], category)
                        self.assertEqual(info["C2OWidgetsEnabled"], widgets)
                        for source in target["sources"]:
                            self.assertTrue((out / source["path"]).is_dir())
                        for dependency in target["dependencies"]:
                            if "target" in dependency:
                                self.assertIn(dependency["target"], project["targets"])
                        if widgets:
                            self.assertEqual(target["entitlements"]["properties"]["com.apple.security.application-groups"], ["group.com.example.myapp"])
                    contract = json.loads((out / ".design/project.json").read_text())
                    report = json.loads((out / ".design/verification.json").read_text())
                    self.assertEqual({c["id"] for c in contract["criteria"]}, {r["criterion_id"] for r in report["results"]})
                    self.assertTrue(all(r["status"] == "NOT_RUN" for r in report["results"]))
                    self.assertEqual(any(c["id"].startswith("WID-") for c in contract["criteria"]), widgets)

    def test_existing_directory_is_not_touched(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "Existing"
            out.mkdir()
            sentinel = out / "keep.txt"
            sentinel.write_text("original")
            with self.assertRaises(FileExistsError):
                generator.create_project(out, "App", "com.example.app", "utility", "App")
            self.assertEqual(sentinel.read_text(), "original")
            self.assertEqual(list(out.iterdir()), [sentinel])

    def test_dangling_symlink_is_not_followed(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "Link"
            out.symlink_to(Path(tmp) / "Missing", target_is_directory=True)
            with self.assertRaises(FileExistsError):
                generator.create_project(out, "App", "com.example.app", "lifestyle", "App")
            self.assertFalse((Path(tmp) / "Missing").exists())

    def test_invalid_identifiers_do_not_create_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "New"
            for name, bundle_id in [("../Bad", "com.example.app"), ("App", "$(SHELL)")]:
                with self.assertRaises(ValueError):
                    generator.create_project(out, name, bundle_id, "utility", "App")
                self.assertFalse(out.exists())

    def test_targets_use_distinct_bundle_ids_and_share_only_profile_snapshot_group(self):
        result = generator.project_spec("Life", "com.example.life", "lifestyle", "Life", True,
                                        "group.com.example.shared", "ABCDE12345")
        targets = result["targets"]
        ids = [t["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"] for t in targets.values()]
        self.assertEqual(len(ids), len(set(ids)))
        for suffix in ["iOS", "macOS"]:
            app = targets["Life_" + suffix]
            widget = targets["Life_" + suffix + "Widgets"]
            self.assertTrue(widget["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"].startswith(app["settings"]["base"]["PRODUCT_BUNDLE_IDENTIFIER"] + "."))
            self.assertEqual(app["info"]["properties"]["C2OURLScheme"], widget["info"]["properties"]["C2OURLScheme"])
        self.assertEqual(result["settings"]["base"]["DEVELOPMENT_TEAM"], "ABCDE12345")

    def test_deep_link_schemes_do_not_collapse_distinct_bundle_ids(self):
        schemes = []
        for bundle_id in ["com.example.a-b", "com.example.a.b"]:
            result = generator.project_spec("App", bundle_id, "utility", "App", True)
            self.assertEqual(result["settings"]["base"]["SWIFT_VERSION"], "5.0")
            for suffix in ["iOS", "macOS"]:
                schemes.append(result["targets"]["App_" + suffix]["info"]["properties"]["C2OURLScheme"])
        self.assertEqual(len(schemes), len(set(schemes)))

    def test_failed_publication_cleans_its_new_directory_and_allows_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "New"
            original_move = generator.shutil.move
            calls = 0

            def failing_move(source, target):
                nonlocal calls
                calls += 1
                if calls == 2:
                    raise OSError("Injected publication failure")
                return original_move(source, target)

            with mock.patch.object(generator.shutil, "move", side_effect=failing_move):
                with self.assertRaises(OSError):
                    generator.create_project(out, "App", "com.example.app", "utility", "App")
            self.assertFalse(out.exists())
            generator.create_project(out, "App", "com.example.app", "utility", "App")
            self.assertTrue((out / "project.json").is_file())


if __name__ == "__main__":
    unittest.main()
