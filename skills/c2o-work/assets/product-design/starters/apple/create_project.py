#!/usr/bin/env python3
"""Create a fresh Apple starter directory. Python 3.9+, standard library only.

This writes source/configuration; XcodeGen and Xcode run separately on a Mac.
Existing destinations are refused, including empty directories and symlinks.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate_options(name: str, bundle_id: str, category: str, display_name: str,
                     app_group: str, team: str) -> None:
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9]*", name):
        raise ValueError("Project name must start with a letter and contain ASCII letters/digits only.")
    if not re.fullmatch(r"(?:[A-Za-z][A-Za-z0-9-]*\.){2,}[A-Za-z][A-Za-z0-9-]*", bundle_id):
        raise ValueError("Use a reverse-DNS bundle identifier such as com.example.myapp.")
    if category not in {"lifestyle", "utility"}:
        raise ValueError("Category must be lifestyle or utility.")
    if not display_name.strip() or any(c in display_name for c in "\x00\r\n$"):
        raise ValueError("Display name must be nonempty, one line and contain no build-setting expansion.")
    if app_group and not re.fullmatch(r"group\.(?:[A-Za-z0-9-]+\.)+[A-Za-z0-9-]+", app_group):
        raise ValueError("App group must use a registered group.example.identifier form.")
    if team and not re.fullmatch(r"[A-Z0-9]{10}", team):
        raise ValueError("Team must be a 10-character Apple Developer team identifier.")


def project_spec(name: str, bundle_id: str, category: str, display_name: str,
                 widgets: bool, app_group: str = "", team: str = "") -> dict:
    validate_options(name, bundle_id, category, display_name, app_group, team)
    group = app_group or ("group." + bundle_id if widgets else "")
    profile = {
        "C2OCategory": category, "C2OAppDisplayName": display_name,
        "C2OAppGroupID": group,
        "C2OWidgetsEnabled": widgets,
    }
    settings = {
        "SWIFT_VERSION": "5.0", "MARKETING_VERSION": "0.1.0",
        "CURRENT_PROJECT_VERSION": "1", "CODE_SIGN_STYLE": "Automatic",
        "SWIFT_STRICT_CONCURRENCY": "targeted",
    }
    if team:
        settings["DEVELOPMENT_TEAM"] = team
    spec = {
        "name": name,
        "options": {"minimumXcodeGenVersion": "2.44.0", "developmentLanguage": "vi"},
        "settings": {"base": settings},
        "packages": {"StarterCore": {"path": "StarterCore"}},
        "targets": {}, "schemes": {},
    }
    for suffix, platform, version in [("iOS", "iOS", "17.0"), ("macOS", "macOS", "14.0")]:
        target = name + "_" + suffix
        app_id = bundle_id + "." + suffix.lower()
        # Dots are valid in URL schemes. Keep them to avoid a-b/a.b collisions,
        # and distinguish native Mac from a separately installed iOS app on Mac.
        scheme = app_id.lower()
        platform_profile = dict(profile, C2OURLScheme=scheme)
        info = dict(platform_profile)
        info.update({
            "CFBundleDisplayName": display_name,
            "CFBundleURLTypes": [{"CFBundleURLName": app_id, "CFBundleURLSchemes": [scheme]}],
        })
        base = {"PRODUCT_BUNDLE_IDENTIFIER": app_id}
        entitlements = {}
        if platform == "iOS":
            base.update({"TARGETED_DEVICE_FAMILY": "1,2", "SUPPORTS_MACCATALYST": False})
            info.update({
                "UIApplicationSceneManifest": {"UIApplicationSupportsMultipleScenes": False},
                "UILaunchScreen": {},
                "UISupportedInterfaceOrientations": [
                    "UIInterfaceOrientationPortrait", "UIInterfaceOrientationLandscapeLeft",
                    "UIInterfaceOrientationLandscapeRight"],
                "UISupportedInterfaceOrientations~ipad": [
                    "UIInterfaceOrientationPortrait", "UIInterfaceOrientationPortraitUpsideDown",
                    "UIInterfaceOrientationLandscapeLeft", "UIInterfaceOrientationLandscapeRight"],
            })
        else:
            base["ENABLE_APP_SANDBOX"] = True
            entitlements["com.apple.security.app-sandbox"] = True
            info["LSApplicationCategoryType"] = (
                "public.app-category.lifestyle" if category == "lifestyle" else "public.app-category.utilities")
        if widgets:
            entitlements["com.apple.security.application-groups"] = [group]
        app = {
            "type": "application", "platform": platform, "deploymentTarget": version,
            "sources": [{"path": "App"}],
            "dependencies": [{"package": "StarterCore"}],
            "settings": {"base": base},
            "info": {"path": f"Config/{suffix}-Info.plist", "properties": info},
        }
        if entitlements:
            app["entitlements"] = {"path": f"Config/{suffix}.entitlements", "properties": entitlements}
        if widgets:
            widget_target = target + "Widgets"
            app["dependencies"].append({"target": widget_target, "embed": True, "link": False})
            widget_info = dict(platform_profile)
            widget_info.update({
                "CFBundleDisplayName": display_name + " Widget",
                "NSExtension": {"NSExtensionPointIdentifier": "com.apple.widgetkit-extension"},
            })
            widget_settings = {
                "PRODUCT_BUNDLE_IDENTIFIER": app_id + ".widgets",
                "APPLICATION_EXTENSION_API_ONLY": True, "SKIP_INSTALL": True,
            }
            if platform == "iOS":
                widget_settings["TARGETED_DEVICE_FAMILY"] = "1,2"
            else:
                widget_settings["ENABLE_APP_SANDBOX"] = True
            spec["targets"][widget_target] = {
                "type": "app-extension", "platform": platform, "deploymentTarget": version,
                "sources": [{"path": "Widgets"}],
                "dependencies": [{"package": "StarterCore"}],
                "settings": {"base": widget_settings},
                "info": {"path": f"Config/{suffix}-Widget-Info.plist", "properties": widget_info},
                "entitlements": {"path": f"Config/{suffix}-Widget.entitlements", "properties": dict(entitlements)},
            }
        spec["targets"][target] = app
        spec["schemes"][target] = {"build": {"targets": {target: "all"}}, "run": {"config": "Debug"}}
    return spec


def design_records(name: str, category: str, widgets: bool) -> tuple[dict, dict]:
    criteria = [
        ("APP-01", "Build and launch the iOS/iPadOS app on the selected supported SDK and configuration"),
        ("APP-02", "Build and launch the native macOS app and use menus, keyboard and Settings"),
        ("APP-03", "Storage read/write failures preserve user work and never replace unreadable data with an empty store"),
        ("APP-04", "Selected phone, resizable iPad and Mac layouts remain usable with large text and accessibility input"),
        ("APP-05", "Valid deep links open the right context; invalid links do not mutate data or discard drafts"),
    ]
    if category == "lifestyle":
        criteria += [
            ("LIF-01", "Create, search, open, edit and favorite the correct record by stable ID; changes persist after reopening"),
            ("LIF-02", "Cancel and delete show the declared outcome; unsaved edits and failed saves remain recoverable"),
        ]
    else:
        criteria += [
            ("UTL-01", "Normalize whitespace and count graphemes, whitespace-delimited tokens and lines according to the declared rules"),
            ("UTL-02", "Copy/share the actual result; input is preserved; history is off by default and opt-in retention/clear behavior is accurate"),
        ]
    if widgets:
        criteria += [
            ("WID-01", "Both widget extensions build with the intended signing/App Group and read only the published summary"),
            ("WID-02", "Small, medium and large widget states keep privacy, timestamp/fallback and valid app navigation without promising an exact refresh time"),
        ]
    project = {
        "schema_version": "1.0", "framework_version": "1.5.0", "project_name": name,
        "platform": "swiftui", "mode": "standard", "category": category,
        "outcome": "Adapt and verify the selected local Apple starter for the project's actual user task.",
        "scope": {"included": [category + " starter", "iOS/iPadOS", "native macOS"] + (["summary widgets"] if widgets else []),
                  "deferred": ["cloud sync", "accounts", "payments", "notifications", "interactive widget intents", "Live Activities"]},
        "criteria": [{"id": id_, "title": title, "required": True, "allow_not_applicable": False}
                     for id_, title in criteria],
    }
    report = {"schema_version": "1.0", "project_sha256": None,
              "results": [{"criterion_id": id_, "status": "NOT_RUN",
                           "rationale": "Generated starter; collect evidence on the actual project and Apple runtime.",
                           "inputs": [], "evidence": []} for id_, _ in criteria]}
    return project, report


def create_project(output: Path, name: str, bundle_id: str, category: str,
                   display_name: str, widgets: bool = False,
                   app_group: str = "", team: str = "") -> Path:
    spec = project_spec(name, bundle_id, category, display_name, widgets, app_group, team)
    output = output.expanduser().absolute()
    if output.exists() or output.is_symlink():
        raise FileExistsError("Destination already exists; choose a new directory. No files were overwritten.")
    if output.resolve().is_relative_to(ROOT):
        raise ValueError("Generate outside the template source directory.")
    for required in ["App", "StarterCore"] + (["Widgets"] if widgets else []):
        if not (ROOT / required).is_dir():
            raise FileNotFoundError("Missing template directory: " + required)
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".c2o-starter-", dir=output.parent))
    created_output = False
    try:
        for folder in ["App", "StarterCore"] + (["Widgets"] if widgets else []):
            ignored = [".build", "__pycache__", "*.pyc", ".DS_Store"]
            if folder == "Widgets":
                # The framework README links to blueprint paths outside a generated project.
                ignored.append("README.md")
            shutil.copytree(ROOT / folder, staging / folder,
                            ignore=shutil.ignore_patterns(*ignored))
        (staging / "Config").mkdir()
        (staging / "project.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        design = staging / ".design"
        design.mkdir()
        project, report = design_records(name, category, widgets)
        for filename, data in [("project.json", project), ("verification.json", report)]:
            (design / filename).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        for filename in ["GETTING_STARTED.md", "NATIVE_CHECKS.md"]:
            if (ROOT / filename).is_file():
                shutil.copy2(ROOT / filename, staging / filename)
        (staging / "STARTER.json").write_text(json.dumps({
            "framework_version": "1.5.0", "name": name, "category": category,
            "widgets": widgets, "deployment": {"iOS": "17.0", "macOS": "14.0"},
            "status": "SOURCE_SCAFFOLD_NATIVE_NOT_RUN", "xcodegen_spec": "project.json",
        }, indent=2) + "\n", encoding="utf-8")
        # Reserve the destination only at publication time; never replace an existing directory.
        output.mkdir(exist_ok=False)
        created_output = True
        for path in staging.iterdir():
            shutil.move(str(path), str(output / path.name))
    except BaseException:
        # Remove only the new directory created by this invocation, never a pre-existing target.
        if created_output:
            shutil.rmtree(output, ignore_errors=True)
        raise
    finally:
        shutil.rmtree(staging, ignore_errors=True)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--category", choices=["lifestyle", "utility"], required=True)
    parser.add_argument("--name", required=True, help="ASCII project identifier, e.g. MyCollection")
    parser.add_argument("--display-name", help="User-facing app name; defaults to --name")
    parser.add_argument("--bundle-id", required=True, help="Reverse-DNS base; .ios/.macos are appended")
    parser.add_argument("--output", type=Path, required=True, help="A new directory; existing paths are refused")
    parser.add_argument("--widgets", action="store_true", help="Include iOS/macOS summary widget targets")
    parser.add_argument("--app-group", default="", help="Registered group identifier, with --widgets")
    parser.add_argument("--team", default="", help="Your 10-character Apple Developer team ID, optional")
    args = parser.parse_args()
    if args.app_group and not args.widgets:
        parser.error("--app-group requires --widgets")
    try:
        path = create_project(args.output, args.name, args.bundle_id, args.category,
                              args.display_name or args.name, args.widgets, args.app_group, args.team)
    except (OSError, ValueError) as error:
        parser.exit(2, f"Cannot create starter: {error}\n")
    print(json.dumps({"created": str(path), "category": args.category, "widgets": args.widgets,
                      "native_build": "NOT_RUN", "next": "On a Mac: xcodegen generate --spec project.json"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
