# Framework checks

These tools are optional resources inside the existing C2O workflow. The
project's current acceptance/evidence source remains authoritative; using a
design template does not require `.design/` files or either checker. Commands
below are written from this resource pack's root; for a separate application,
use the actual checker path and set `--root` to that application's root.

## Template catalog structure

`template_check.py` is a read-only Python 3.9+ standard-library tool for the
24 reusable Markdown templates. The [standard](../documentation/template-standard.md)
defines the format; the [registry](../documentation/template-registry.json)
declares each template ID, path, family and version.

```bash
python3 tools/template_check.py --root .
python3 -m unittest discover -s tests -p 'test_template_check.py' -v
```

The checker verifies registry coverage, unique IDs/paths, metadata field names
and order, nonempty values, matching template ID/version, the default `draft`
document status, the standard link, and first/last section placement. The
handoff checklist has four to six unchecked items. It ignores fenced examples.
It reads files and prints JSON without changing files or lifecycle state.

Exit `0` / `TEMPLATES_VALID` means these structural checks passed. Exit `2` /
`TEMPLATES_INVALID` lists errors. It does not judge whether prose is true,
complete or useful; it does not resolve every body link, validate domain IDs,
check filled project documents or execute native code. Project documents may
have real statuses and checked handoffs; do not run this template-only contract
on them. Review their content under the project's actual scope.

## Evidence-record checker

Use this section only after deliberately selecting the legacy JSON profile for
the relevant scope. It can own records for a new scope or consume a clearly
identified derived export from native records. Do not create two independently
writable acceptance or result ledgers, migrate existing records merely to use
the pack, or replace a live report with a scaffold.

`design_check.py` is an original Python 3.9+ standard-library tool. It checks the
integrity and coverage of declared verification records. It runs no browser,
simulator, accessibility audit, test command, or design review. It installs
nothing and has no network dependency.

**`RECORDS_READY` means the records satisfy this contract.** A person or agent
still needs to judge whether the criteria are sufficient, the evidence supports
the recorded result, and the product is ready for its intended use.

## Files and paths

Within the selected JSON profile, use a project file such as
`.design/project.json` and a report such as `.design/verification.json`. If the
scope has no such records, the [project template](../templates/project.json) and
[report template](../templates/verification-report.json) are starting points.
Reconcile criteria with the complete current contract before use; preserve
required coverage and existing evidence.

All relative command-line file arguments resolve against `--root`, including
`--project` and `--report`. These two arguments may also be absolute paths inside
that root. Input and evidence references must be project-relative POSIX paths:
use `src/Screen.swift`, including on Windows. The checker rejects absolute
references, `..`, backslashes, drive prefixes, missing files, directories, and
symlinks resolving outside the supplied root. It reads files and prints JSON;
it never changes a report.

Each project criterion requires:

| Field | Contract |
|---|---|
| `id` | Unique, stable identifier using letters, digits, `.`, `_`, or `-` |
| `title` | Nonempty acceptance condition a reviewer can assess |
| `required` | Boolean; at least one criterion must be required |
| `allow_not_applicable` | Boolean; explicit permission to record N/A with a rationale |

Project `schema_version` is `"1.0"`, `project_name` is nonempty, and `criteria`
cannot be empty. Extra metadata is allowed. Fields such as `platform`, `mode`,
`scope`, `owners`, `checks`, criterion `type`, and criterion `method` are
descriptive: they do not cause this tool to execute anything.

The JSON schemas in `../schemas/` help editors validate structure. The Python
checker implements the additional identity, coverage, path and hash rules
without needing a JSON Schema library. It also rejects duplicate JSON object
keys instead of silently keeping one value.

## Record an observation

1. Agree the criteria and the complete set of files relevant to each check.
2. Perform the actual check with the appropriate external tool or reviewer.
3. Save its evidence inside the project, such as a test log, screenshots with
   reviewed states, or a written manual observation. Record who checked what,
   how, and under which environment in that evidence.
4. Hash the project file, every declared input, and the evidence. Copy the
   resulting hashes into the report and set the status supported by the check.
5. Validate the report. A subsequent input, evidence, or project-file change
   requires rechecking the affected work before replacing its hashes.

The snapshot command helps with step 4:

```bash
python3 tools/design_check.py snapshot --root . --project .design/project.json --path src/Screen.swift --path .design/evidence/C-001-review.md
```

Repeat `--path` for every file to hash. Omit all `--path` flags to obtain only the
project hash. Output contains `schema_version`, `project_sha256`, and
`files: [{"path": "...", "sha256": "..."}]`. Copy file objects into the relevant
`inputs` or `evidence` array. Snapshot assigns no criterion status, updates no
report, and does not attest that a check occurred. Exit 0 from **snapshot** means
only that the requested hashes were produced.

Use the full 64-character SHA-256 values. Every declared file is checked on
every validation, for every status. Multiple criteria may reference the same
file; changing that file invalidates each dependent result. Duplicate paths
within one input or evidence list are rejected.

The project hash binds the report to the exact bytes of `.design/project.json`.
Changing metadata or formatting also invalidates that binding. A new pending
report may use `project_sha256: null` while every result is `NOT_RUN`. Bind the
report before recording any other status.

## Status meanings

C2O still reports `pass`, `partial`, `fail`, and `not-tested` using its native
aggregation rules. The following uppercase statuses belong only to this JSON
checker. There is no lossless representation of C2O `partial`: retain its
supported and missing coverage in the C2O report/evidence; do not turn it into
`PASS`. `RECORDS_READY` neither sets the C2O verdict nor marks work `DONE` or
authorizes publication.

| Status | Checker behavior |
|---|---|
| `PASS` | Requires at least one input and one evidence file, with current hashes. A rationale is recommended. The checker does not decide whether the evidence actually proves the claim. |
| `FAIL` | Preserves the reported failure. A valid, otherwise complete required failure yields exit 1. Evidence and a rationale are recommended, but missing evidence never upgrades a failure into a pass. |
| `BLOCKED` | Requires a nonempty rationale. A required blocked criterion remains incomplete. |
| `NOT_RUN` | Explicitly unperformed. A required criterion remains incomplete. Empty input/evidence arrays are appropriate in the starting template. |
| `NOT_APPLICABLE` | Requires permission in the criterion and a nonempty rationale. At least one required criterion must remain applicable; an all-N/A report is incomplete. |

There must be exactly one result for every declared criterion, including
optional criteria. Missing results are incomplete; unknown or duplicate IDs are
invalid. Explicit optional `NOT_RUN`, `BLOCKED`, or `FAIL` statuses do not block
required coverage, but malformed records, missing declared files, and stale
hashes anywhere in the report prevent readiness. Optional failures remain in
the source report for a reviewer to assess.

## Validate and interpret the result

```bash
python3 tools/design_check.py validate --root . --project .design/project.json --report .design/verification.json
```

JSON output separates `record_validity` from `required_coverage`.
`record_validity` reports malformed data, stale files, missing result IDs and the
project binding. `required_coverage` lists accepted current passes, allowed N/A,
incomplete criteria and `reported_failures`. Invalid or stale required records
do not count as covered passes. A failed criterion remains listed even when
other criteria are incomplete.

| Exit | Outcome | Meaning |
|---|---|---|
| `0` | `RECORDS_READY` | Valid current records, every criterion represented, at least one applicable required criterion, and all required criteria PASS or permitted N/A |
| `1` | `REQUIREMENTS_FAILED` | Valid current complete records contain a required FAIL |
| `2` | `INVALID`, `STALE`, or `INCOMPLETE` | Fix invalid records, recheck changed work, supply missing evidence, or finish required checks |

A `FAIL` plus a required `NOT_RUN` yields exit **2**, with the failure preserved
in `reported_failures`. An empty project, all-optional project, or all-N/A
required coverage never yields `RECORDS_READY`. The initial report is expected
to yield exit 2 because no check has run.

## Limits to retain in every agent handoff

Hashes provide traceability, not authenticity. An agent can write an inaccurate
manual record, omit an important dependency, or hash files without running any
check. This tool cannot discover those acts. Include all relevant source,
stylesheets, assets, configuration, test data, and environment records yourself;
automatic dependency discovery is outside its scope. A screenshot hash alone
does not establish accessibility, behavior, usability, or visual quality.

Validation is a filesystem snapshot, not a watcher or signed attestation.
Reviewers must still examine the evidence and rerun appropriate checks when the
work or environment changes. The tool never labels the UI or release ready.

## Run the tool's own tests

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

The tests cover validator behavior with temporary project fixtures. Their success
does not verify any application or any record in your project.
