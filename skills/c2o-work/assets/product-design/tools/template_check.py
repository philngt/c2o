#!/usr/bin/env python3
"""Read-only structural check for the reusable Markdown template catalog.

This does not validate product semantics, filled project documents or runtime.
Python 3.9+, standard library only.
"""

import argparse
import json
import re
from pathlib import Path


STANDARD_VERSION = "1.0.0"
FIELDS = (
    "Template ID", "Phiên bản template", "Mục đích", "Dùng khi", "Đầu vào",
    "Đầu ra / bàn giao", "Nguồn chuẩn", "Owner", "Revision tài liệu",
    "Ngày cập nhật", "Trạng thái tài liệu", "Phạm vi áp dụng",
)
CONTRACT = "Hợp đồng tài liệu"
HANDOFF = "Kiểm tra trước bàn giao"
REGISTRY = "documentation/template-registry.json"


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def visible_lines(content):
    """Ignore fenced examples when checking headings and checklists."""
    result = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                if token[0] == "`" and "`" in marker.group(2):
                    result.append(line)
                    continue
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not marker.group(2).strip():
                fence = None
            result.append("")
        else:
            result.append(line if fence is None else "")
    return result


def plain(value):
    return value.strip().strip("`")


def check_document(path, entry):
    errors = []
    content = path.read_text(encoding="utf-8")
    lines = visible_lines(content)
    h1 = [i for i, line in enumerate(lines) if re.match(r"^#\s+\S", line)]
    first = next((i for i, line in enumerate(lines) if line.strip()), -1)
    if len(h1) != 1 or h1[0] != first:
        errors.append("exactly one H1 must begin the document")
    h2 = [(i, line[3:].strip()) for i, line in enumerate(lines) if line.startswith("## ")]
    names = [name for _, name in h2]
    if names.count(CONTRACT) != 1 or not names or names[0] != CONTRACT:
        errors.append("first H2 must be the unique document contract")
    if names.count(HANDOFF) != 1 or not names or names[-1] != HANDOFF:
        errors.append("last H2 must be the unique handoff checklist")
    if CONTRACT in names:
        position = names.index(CONTRACT)
        start = h2[position][0] + 1
        end = h2[position + 1][0] if position + 1 < len(h2) else len(lines)
        row_positions = [i for i in range(start, end) if lines[i].strip().startswith("|")]
        rows = [lines[i].strip() for i in row_positions]
        if row_positions and row_positions != list(range(row_positions[0], row_positions[-1] + 1)):
            errors.append("contract metadata must be one contiguous table block")
        cells = [re.split(r"(?<!\\)\|", row.strip("|").strip()) for row in rows]
        cells = [[cell.strip() for cell in row] for row in cells]
        if any(len(row) != 2 for row in cells):
            errors.append("contract table must have two columns; escape literal pipes")
        elif len(cells) != len(FIELDS) + 2:
            errors.append("contract table must contain a header, separator and 12 fields")
        elif cells[0] != ["Thuộc tính", "Giá trị"] or any(
            not re.fullmatch(r":?-{3,}:?", cell) for cell in cells[1]
        ):
            errors.append("contract table header/separator does not match the standard")
        else:
            metadata = cells[2:]
            if tuple(row[0] for row in metadata) != FIELDS:
                errors.append("contract field names/order do not match the standard")
            values = dict(metadata)
            for name, value in metadata:
                if not plain(value):
                    errors.append("empty contract field: " + name)
            if plain(values.get("Template ID", "")) != entry["id"]:
                errors.append("Template ID differs from registry")
            if plain(values.get("Phiên bản template", "")) != entry["version"]:
                errors.append("template version differs from registry")
            if plain(values.get("Trạng thái tài liệu", "")) != "draft":
                errors.append("unfilled reusable templates must default to draft")
        standard_link = (
            "../../documentation/template-standard.md" if entry["family"] == "product"
            else "../documentation/template-standard.md"
        )
        contract_text = re.sub(r"`[^`\n]*`", "", "\n".join(lines[start:end]))
        link_pattern = r"(?<![!\\])\[[^\]\n]+\]\(" + re.escape(standard_link) + r"\)"
        if not re.search(link_pattern, contract_text):
            errors.append("contract must link to the template standard")
    if HANDOFF in names:
        start = h2[names.index(HANDOFF)][0] + 1
        checklist = lines[start:]
        bullet = r"^\s*(?:[-+*]|\d+[.)])\s+"
        unchecked = sum(bool(re.match(bullet + r"\[ \] \S", line)) for line in checklist)
        if not 4 <= unchecked <= 6:
            errors.append("handoff must contain four to six unchecked items")
        if any(re.match(bullet + r"\[[xX]\]", line) for line in checklist):
            errors.append("reusable handoff checklist must not be pre-checked")
    return errors


def validate(root):
    try:
        root = Path(root).resolve()
    except (OSError, RuntimeError) as error:
        return {"status": "TEMPLATES_INVALID", "checked": 0, "errors": ["framework root: " + str(error)]}
    errors = []
    checked = 0
    registry_path = root / REGISTRY
    try:
        if not registry_path.resolve().is_relative_to(root):
            raise ValueError("registry must remain inside framework root")
        registry = json.loads(registry_path.read_text(encoding="utf-8"), object_pairs_hook=unique_keys)
        if not isinstance(registry, dict):
            raise ValueError("registry must be an object")
        if registry.get("schema_version") != "1.0" or registry.get("standard_version") != STANDARD_VERSION:
            raise ValueError("unsupported registry schema or template standard version")
        entries = registry.get("templates")
        if not isinstance(entries, list) or not entries:
            raise ValueError("registry templates must be a nonempty list")
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        return {"status": "TEMPLATES_INVALID", "checked": 0, "errors": [str(error)]}

    ids = set()
    paths = set()
    for index, entry in enumerate(entries):
        label = "registry entry " + str(index + 1)
        if not isinstance(entry, dict) or set(entry) != {"id", "path", "version", "family"}:
            errors.append(label + ": expected id/path/version/family")
            continue
        if not all(isinstance(value, str) for value in entry.values()):
            errors.append(label + ": all fields must be strings")
            continue
        identifier, relative = entry["id"], entry["path"]
        if not re.fullmatch(r"TPL-[A-Z0-9]+(?:-[A-Z0-9]+)*", identifier):
            errors.append(label + ": invalid template ID")
        if identifier in ids:
            errors.append(label + ": duplicate template ID " + identifier)
        ids.add(identifier)
        if not re.fullmatch(r"templates/(?:product/)?[a-z0-9]+(?:-[a-z0-9]+)*\.md", relative):
            errors.append(label + ": unsafe or unsupported template path")
            continue
        if relative in paths:
            errors.append(label + ": duplicate template path " + relative)
            continue
        paths.add(relative)
        if not re.fullmatch(r"\d+\.\d+\.\d+", entry["version"]):
            errors.append(relative + ": invalid template version")
        expected_family = "product" if relative.startswith("templates/product/") else "ux-ui"
        if entry["family"] != expected_family:
            errors.append(relative + ": family must match template directory")
        path = root / relative
        try:
            if not path.resolve().is_relative_to(root):
                raise ValueError("template must remain inside framework root")
            errors.extend(relative + ": " + error for error in check_document(path, entry))
            checked += 1
        except (OSError, UnicodeError, ValueError, RuntimeError) as error:
            errors.append(relative + ": " + str(error))
    actual = {path.relative_to(root).as_posix() for path in (root / "templates").rglob("*.md")}
    errors.extend("unregistered template: " + path for path in sorted(actual - paths))
    errors.extend("registered template missing: " + path for path in sorted(paths - actual))
    return {
        "status": "TEMPLATES_INVALID" if errors else "TEMPLATES_VALID",
        "standard_version": STANDARD_VERSION,
        "checked": checked,
        "registered": len(entries),
        "errors": errors,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="framework root (default: parent of tools/)")
    result = validate(parser.parse_args().root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "TEMPLATES_VALID" else 2


if __name__ == "__main__":
    raise SystemExit(main())
