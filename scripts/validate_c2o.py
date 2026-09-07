#!/usr/bin/env python3
"""Dependency-free structural checks; does not execute or grade an AI agent."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKILLS = frozenset(
    f"c2o-{name}" for name in
    "work shape decide grill spec slice create deliver execute verify learn".split()
)
GROUPS = frozenset({"clarify", "produce", "coordinate"})
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^\s)]+)(?:\s+[^)]*)?\)")
FENCE = re.compile(r"(?ms)^```[^\n]*\n.*?^```[ \t]*$")


def metadata(text: str) -> dict[str, str]:
    """Check this repo's one-line name/description convention, not general YAML."""
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    header, separator, _ = text[4:].partition("\n---\n")
    if not separator:
        raise ValueError("missing closing frontmatter delimiter")
    result = {}
    for field in ("name", "description"):
        values = re.findall(rf"^{field}:[ \t]*(.*)$", header, flags=re.MULTILINE)
        if len(values) != 1 or not values[0].strip():
            raise ValueError(f"expected one non-empty {field}")
        value = values[0].strip()
        if value.startswith(('"', "'", "|", ">")):
            raise ValueError(f"{field}: checker expects the repo's plain one-line scalar")
        if ": " in value or " #" in value:
            raise ValueError(f"{field}: ambiguous plain scalar; review YAML syntax")
        result[field] = value
    if len(result["name"]) > 64 or not NAME.fullmatch(result["name"]):
        raise ValueError("invalid skill name")
    if len(result["description"]) > 1024:
        raise ValueError("description exceeds 1024 characters")
    return result


def local_link_errors(path: Path, root: Path) -> list[str]:
    """Check inline local link paths outside backtick fences; not URLs/anchors."""
    errors = []
    text = FENCE.sub("", path.read_text(encoding="utf-8"))
    for match in LINK.finditer(text):
        target = match.group(1)
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        destination = (path.parent / unquote(parsed.path)).resolve()
        if not destination.is_relative_to(root.resolve()):
            errors.append(f"{path}: link escapes repository: {target}")
        elif not destination.exists():
            errors.append(f"{path}: missing link target: {target}")
    return errors


def scenario_errors(data: object) -> list[str]:
    errors = []
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        return ["invalid scenario schema_version"]
    if data.get("kind") != "synthetic-behavioral-scenarios":
        errors.append("scenarios must identify synthetic fixture provenance")
    if data.get("execution_status") != "not-run":
        errors.append("fixtures must not be presented as executed results")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        return errors + ["cases must be a non-empty list"]
    seen = set()
    for index, case in enumerate(cases):
        label = f"case[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{label}: expected object")
            continue
        identifier = case.get("id")
        if not isinstance(identifier, str) or not NAME.fullmatch(identifier):
            errors.append(f"{label}: invalid id")
        elif identifier in seen:
            errors.append(f"{label}: duplicate id {identifier}")
        else:
            seen.add(identifier)
        if not isinstance(case.get("group"), str) or case["group"] not in GROUPS:
            errors.append(f"{label}: invalid group")
        for field in ("skills", "must", "must_not", "evidence"):
            value = case.get(field)
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
                errors.append(f"{label}: {field} must be a non-empty string list")
        if isinstance(case.get("skills"), list) and any(not isinstance(x, str) or x not in SKILLS for x in case["skills"]):
            errors.append(f"{label}: unknown skill")
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"{label}: missing prompt")
        env = case.get("environment")
        if not isinstance(env, dict):
            errors.append(f"{label}: missing environment")
        else:
            tools = env.get("tools")
            if not isinstance(tools, list) or not all(isinstance(t, str) and t for t in tools):
                errors.append(f"{label}: tools must be a string list")
            if not isinstance(env.get("authorization"), str) or not env["authorization"].strip():
                errors.append(f"{label}: missing authorization boundary")
        fixtures = case.get("fixtures")
        if not isinstance(fixtures, dict):
            errors.append(f"{label}: fixtures must be an object")
        else:
            for name, content in fixtures.items():
                if (not isinstance(name, str) or not name or name in {".", ".."}
                        or "\\" in name or ":" in name or name.startswith("/")
                        or ".." in name.split("/") or any(ord(char) < 32 for char in name)
                        or not isinstance(content, str)):
                    errors.append(f"{label}: unsafe fixture path or non-text content")
    return errors



def scenario_suite_errors(root: Path) -> list[str]:
    """Validate all fixture suites and case-ID uniqueness; never run a model."""
    root = root.resolve()
    paths = sorted((root / "evals").glob("*scenarios.json"))
    errors: list[str] = []
    seen: dict[str, Path] = {}
    if root / "evals/scenarios.json" not in paths:
        errors.append("scenario fixtures: missing required evals/scenarios.json")
    for path in paths:
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            errors.append(f"{path}: scenario suite must be a local non-symlink file")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as exc:
            errors.append(f"{path}: scenario fixtures: {exc}")
            continue
        errors.extend(f"{path}: {error}" for error in scenario_errors(data))
        cases = data.get("cases", []) if isinstance(data, dict) else []
        if not isinstance(cases, list):
            continue
        for case in cases:
            identifier = case.get("id") if isinstance(case, dict) else None
            if not isinstance(identifier, str) or not NAME.fullmatch(identifier):
                continue
            if identifier in seen and seen[identifier] != path:
                errors.append(f"{path}: duplicate case id across suites: {identifier} ({seen[identifier]})")
            else:
                seen[identifier] = path
    return errors


def validate(root: Path) -> list[str]:
    errors = []
    root = root.resolve()
    paths = sorted((root / "skills").glob("*/SKILL.md"))
    if {p.parent.name for p in paths} != SKILLS:
        errors.append("expected exactly the eleven C2O skills")
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
            fields = metadata(text)
            if fields["name"] != path.parent.name:
                errors.append(f"{path}: name does not match directory")
            if len(text.splitlines()) >= 500:
                errors.append(f"{path}: keep instructions under 500 lines")
        except (ValueError, OSError) as exc:
            errors.append(f"{path}: {exc}")
    for folder in ("skills", "docs", "evals"):
        for path in (root / folder).rglob("*.md"):
            try:
                errors.extend(local_link_errors(path, root))
            except (ValueError, OSError) as exc:
                errors.append(f"{path}: {exc}")
    for path in sorted(root.glob("*.md")):
        try:
            errors.extend(local_link_errors(path, root))
        except (ValueError, OSError) as exc:
            errors.append(f"{path}: {exc}")
    errors.extend(scenario_suite_errors(root))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print("PASS: structural checks only; host and behavioral evaluations were not executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
