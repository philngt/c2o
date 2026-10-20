#!/usr/bin/env python3
"""Validate evidence records for declared design criteria; never execute checks.

Python 3.9+ standard library only. Exit 0 means records are ready for review,
not that a UI is correct, accessible, usable, or ready to release.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath, PureWindowsPath

VERSION = "1.0"
STATUSES = {"PASS", "FAIL", "BLOCKED", "NOT_RUN", "NOT_APPLICABLE"}
SHA = re.compile(r"^[0-9a-f]{64}$")
IDENTIFIER = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class CheckError(ValueError):
    pass


def nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def root_path(value):
    root = Path(value).resolve(strict=True)
    if not root.is_dir():
        raise CheckError("--root must name an existing directory")
    return root


def bounded_file(root, value, *, reference=False):
    if not nonblank(value):
        raise CheckError("file path must be a nonempty string")
    # Evidence paths are portable, project-relative POSIX paths. Reject traversal
    # even when normalization would happen to bring the path back inside root.
    if reference:
        parts = PurePosixPath(value).parts
        if ("\\" in value or ".." in parts or PurePosixPath(value).is_absolute()
                or PureWindowsPath(value).drive):
            raise CheckError("file reference must be relative to --root, without '..' or backslashes")
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(root)
    except ValueError as exc:
        raise CheckError("file resolves outside --root") from exc
    except (OSError, RuntimeError) as exc:
        raise CheckError("file does not exist or cannot be resolved: " + str(value)) from exc
    if not resolved.is_file():
        raise CheckError("path must name a regular file: " + str(value))
    return resolved


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise CheckError("duplicate JSON object key: " + key)
        result[key] = value
    return result


def read_json(path):
    def reject_constant(value):
        raise CheckError("non-finite JSON number: " + value)
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=unique_object,
                          parse_constant=reject_constant)
    if not isinstance(value, dict):
        raise CheckError("JSON document must be an object")
    return value


def problem(errors, code, message, context=None):
    item = {"code": code, "message": message}
    if context is not None:
        item["context"] = context
    errors.append(item)


def project_criteria(project, errors):
    if project.get("schema_version") != VERSION:
        problem(errors, "PROJECT_VERSION", "project.schema_version must be '1.0'")
    if not nonblank(project.get("project_name")):
        problem(errors, "PROJECT_NAME", "project_name must be a nonempty string")
    criteria = project.get("criteria")
    if not isinstance(criteria, list) or not criteria:
        problem(errors, "NO_CRITERIA", "criteria must be a nonempty array")
        return {}
    indexed = {}
    for position, criterion in enumerate(criteria):
        context = "criteria[" + str(position) + "]"
        if not isinstance(criterion, dict):
            problem(errors, "CRITERION_SHAPE", "criterion must be an object", context)
            continue
        identifier = criterion.get("id")
        if not isinstance(identifier, str) or not IDENTIFIER.fullmatch(identifier):
            problem(errors, "CRITERION_ID", "id must use letters, digits, dots, underscores or hyphens", context)
            continue
        if identifier in indexed:
            problem(errors, "DUPLICATE_CRITERION", "criterion id is declared more than once", identifier)
            continue
        indexed[identifier] = criterion
        if not nonblank(criterion.get("title")):
            problem(errors, "CRITERION_TITLE", "title must be a nonempty string", identifier)
        for field in ("required", "allow_not_applicable"):
            if not isinstance(criterion.get(field), bool):
                problem(errors, "CRITERION_BOOLEAN", field + " must be a boolean", identifier)
    if not any(c.get("required") is True for c in indexed.values()):
        problem(errors, "NO_REQUIRED_CRITERIA", "at least one criterion must be required")
    return indexed


def check_files(root, references, context, errors, stale):
    if not isinstance(references, list):
        problem(errors, "FILE_LIST", "inputs and evidence must be arrays", context)
        return
    seen = set()
    for reference in references:
        if not isinstance(reference, dict):
            problem(errors, "FILE_REFERENCE", "file reference must be an object", context)
            continue
        name, expected = reference.get("path"), reference.get("sha256")
        if not isinstance(expected, str) or not SHA.fullmatch(expected):
            problem(errors, "FILE_HASH", "sha256 must contain 64 lowercase hexadecimal characters", context)
        try:
            path = bounded_file(root, name, reference=True)
            if path in seen:
                problem(errors, "DUPLICATE_FILE", "file is declared twice in the same list", context)
            seen.add(path)
            actual = sha256(path)
            if isinstance(expected, str) and SHA.fullmatch(expected) and actual != expected:
                problem(stale, "FILE_CHANGED", "declared file hash no longer matches", context + ": " + name)
        except (CheckError, OSError, ValueError) as exc:
            problem(errors, "FILE_UNAVAILABLE", str(exc), context)


def validate(project, report, root, project_hash):
    errors, stale = [], []
    criteria = project_criteria(project, errors)
    if report.get("schema_version") != VERSION:
        problem(errors, "REPORT_VERSION", "report.schema_version must be '1.0'")
    expected_project = report.get("project_sha256")
    if "project_sha256" not in report:
        problem(errors, "PROJECT_BINDING", "report must declare project_sha256 (null for a pending report)")
    elif expected_project is not None:
        if not isinstance(expected_project, str) or not SHA.fullmatch(expected_project):
            problem(errors, "PROJECT_BINDING", "project_sha256 must be a full SHA-256 or null")
        elif expected_project != project_hash:
            problem(stale, "PROJECT_CHANGED", "project criteria or metadata changed after the report was bound")
    project_bound = expected_project == project_hash
    results = report.get("results")
    if not isinstance(results, list):
        problem(errors, "RESULTS_SHAPE", "results must be an array")
        results = []
    states = {}
    reported_failures = set()
    for position, record in enumerate(results):
        context = "results[" + str(position) + "]"
        if not isinstance(record, dict):
            problem(errors, "RESULT_SHAPE", "result must be an object", context)
            continue
        before = len(errors), len(stale)
        identifier = record.get("criterion_id")
        known = isinstance(identifier, str) and identifier in criteria
        if not known:
            problem(errors, "UNKNOWN_CRITERION", "criterion_id must name a declared criterion", context)
        elif identifier in states:
            problem(errors, "DUPLICATE_RESULT", "criterion has more than one result", identifier)
        status = record.get("status")
        if not isinstance(status, str) or status not in STATUSES:
            problem(errors, "RESULT_STATUS", "status must be PASS, FAIL, BLOCKED, NOT_RUN or NOT_APPLICABLE", context)
        rationale = record.get("rationale")
        if not isinstance(rationale, str):
            problem(errors, "RESULT_RATIONALE", "rationale must be a string (empty is allowed for NOT_RUN)", context)
        if status in ("BLOCKED", "NOT_APPLICABLE") and not nonblank(rationale):
            problem(errors, "RATIONALE_REQUIRED", status + " needs a nonempty rationale", context)
        if status == "NOT_APPLICABLE" and known and criteria[identifier].get("allow_not_applicable") is not True:
            problem(errors, "NA_NOT_ALLOWED", "this criterion does not allow NOT_APPLICABLE", identifier)
        if expected_project is None and status != "NOT_RUN":
            problem(errors, "UNBOUND_RESULT", "bind the report to project_sha256 before recording a result", context)
        for field in ("inputs", "evidence"):
            references = record.get(field)
            if status == "PASS" and (not isinstance(references, list) or not references):
                problem(errors, "PASS_WITHOUT_" + field.upper(), "PASS requires at least one " + field + " file", context)
            check_files(root, references, context + "." + field, errors, stale)
        if known:
            if status == "FAIL" and criteria[identifier].get("required") is True:
                reported_failures.add(identifier)
            if identifier not in states:
                states[identifier] = {"status": status, "valid": before == (len(errors), len(stale))}
    missing = sorted(set(criteria) - set(states))
    required = [identifier for identifier, criterion in criteria.items() if criterion.get("required") is True]
    passed, exempt, incomplete = [], [], []
    for identifier in required:
        state = states.get(identifier)
        if not state or not state["valid"] or not project_bound:
            incomplete.append(identifier)
        elif state["status"] == "PASS":
            passed.append(identifier)
        elif state["status"] == "NOT_APPLICABLE":
            exempt.append(identifier)
        elif state["status"] != "FAIL":
            incomplete.append(identifier)
    applicable = len(required) - len(exempt)
    coverage = "INCOMPLETE" if incomplete or not required or not applicable else (
        "FAILED" if reported_failures else "SATISFIED")
    validity = "INVALID" if errors else "STALE" if stale else (
        "INCOMPLETE" if missing or not project_bound else "VALID")
    outcome = validity if validity != "VALID" else (
        "INCOMPLETE" if coverage == "INCOMPLETE" else
        "REQUIREMENTS_FAILED" if coverage == "FAILED" else "RECORDS_READY")
    exit_code = 0 if outcome == "RECORDS_READY" else 1 if outcome == "REQUIREMENTS_FAILED" else 2
    return {
        "schema_version": VERSION, "outcome": outcome, "exit_code": exit_code,
        "record_validity": {"status": validity, "project_bound": project_bound,
                            "errors": errors, "stale": stale, "missing_results": missing},
        "required_coverage": {"status": coverage, "required_count": len(required),
                              "applicable_count": applicable, "passed": sorted(passed),
                              "reported_failures": sorted(reported_failures),
                              "not_applicable": sorted(exempt), "incomplete": sorted(incomplete)},
        "scope": "Evidence-record integrity and declared required criteria only; no checks were executed and evidence truth was not verified.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command in ("validate", "snapshot"):
        sub = commands.add_parser(command)
        sub.add_argument("--root", required=True, help="project root; relative file arguments resolve here")
        sub.add_argument("--project", required=True, help="project JSON inside --root")
        if command == "validate":
            sub.add_argument("--report", required=True, help="verification JSON inside --root")
        else:
            sub.add_argument("--path", action="append", default=[], help="project-relative file to hash; repeat as needed")
    args = parser.parse_args(argv)
    try:
        root = root_path(args.root)
        project_file = bounded_file(root, args.project)
        project = read_json(project_file)
        project_hash = sha256(project_file)
        if args.command == "validate":
            report = read_json(bounded_file(root, args.report))
            output = validate(project, report, root, project_hash)
            code = output["exit_code"]
        else:
            errors = []
            project_criteria(project, errors)
            if errors:
                raise CheckError("invalid project: " + "; ".join(e["message"] for e in errors))
            files, seen = [], set()
            for name in args.path:
                path = bounded_file(root, name, reference=True)
                if path in seen:
                    raise CheckError("duplicate snapshot path: " + name)
                seen.add(path)
                files.append({"path": PurePosixPath(name).as_posix(), "sha256": sha256(path)})
            output = {"schema_version": VERSION, "project_sha256": project_hash, "files": files,
                      "scope": "Hashes only. No criterion status was assigned or changed."}
            code = 0
    except (CheckError, OSError, ValueError, RuntimeError) as exc:
        output = {"schema_version": VERSION, "outcome": "INVALID", "exit_code": 2,
                  "record_validity": {"status": "INVALID", "errors": [{"code": "LOAD_ERROR", "message": str(exc)}]},
                  "required_coverage": {"status": "INCOMPLETE"}}
        code = 2
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
