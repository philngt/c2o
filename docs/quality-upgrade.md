# Outcome and Quality Upgrade

This change preserves the eleven skill names and existing installation/invocation paths. It strengthens contracts, not a model-specific runtime. Use c2o-work as before; specialist skills also retain the minimum rules needed when called directly.

## Three groups

| Group | Upgraded responsibility |
|---|---|
| Shape, Decide, Grill, Spec, Slice | Fill expertise gaps without inventing scope; establish completion/quality; choose useful evidence; preserve the full commitment. |
| Create, Deliver, Execute | Apply relevant quality guidance; prove a representative slice when useful; observe real output; repair material gaps within authority; hand off usable results. |
| Work, Verify, Learn | Route by current blockers and actual capabilities; keep authority and coverage; check compliance and outcome fit; retain applicable evidence-backed lessons. |

## Working contract, not more ceremony

A small edit still needs a small edit, not a project directory, multiple alternatives, or every template field. Use shared references only when they change the action or verification:

- [Outcome contract](../skills/c2o-work/references/outcome-contract.md): requirements, completion, authority, evidence, and status rules.
- [Quality loop](../skills/c2o-work/references/quality-loop.md): observe, repair, recheck, stop, and hand off.
- [Quality profiles](../skills/c2o-work/references/quality-profiles.md): selective starting lenses, not automatic requirements or certified standards.

## Example: a vertical photo viewer

This is a synthetic example, not an audit or performance claim about a deployed website.

Request: build a usable mobile photo viewer from provided sample images, without login; prepare locally and do not deploy.

The agent preserves the required image experience and no-login constraint. It may identify necessary loading and broken-image handling, recommend implementation means, and keep accounts/comments/admin tools outside scope. If publishing images affects privacy or authority, it resolves that before acting.

For repeated UI, one representative path demonstrates the selected design and implementation quality. It is a baseline, not permission to omit remaining requested flows. The agent opens/runs the artifact with available tools and checks the intended interactions. If no browser is available, it reports exactly which checks are structural rather than claiming interaction was tested.

The handoff contains the artifact, minimal use instructions, observed checks, unresolved gaps, and prepared-not-deployed state. An agent walkthrough is not evidence of real user satisfaction or business impact.

## Existing projects

No context migration or automatic overwrite is required. Existing .context files remain usable. Add fields only where helpful for the active task, keep other tasks' goals intact, and retain accepted decisions. The initializer copies missing files but does not update existing context files or custom agent TOML files. Review and deliberately update copied verifier templates when adopting the new guidance.

No new permissions, tools, paid services, packages, host APIs, or model names are assumed. Cross-skill references live inside the shared skills directory packaged by this plugin. A separately copied specialist skill without sibling references cannot load the extended guides; its core scope/authority rules still apply, and it must not claim it loaded missing guidance.

## Validation

Python 3.10+ is sufficient for the added local validation tools; no third-party package is needed.

```bash
python3 scripts/validate_c2o.py
python3 -m unittest discover -s tests -v
```

Structural checks validate the repository's simple frontmatter conventions, local Markdown links, skill set, and evaluation-fixture shape. Unit tests test the checker itself. They do not execute a model, enforce permissions, judge design quality, prove correctness of every claim, or verify host installation.

Use [the evaluation protocol](../evals/README.md) for actual before/after host runs. Record missing tools and real execution evidence rather than inferring a pass from compliant-looking text.

## Deliberate limits

The plugin is still instructions, not a security sandbox, workflow engine, independent expert, or guarantee of behavior. No concurrent-context locking, unattended publishing, telemetry, automatic global skill rewriting, or benchmark claim is added. Domain-specific requirements must come from the approved brief and applicable authoritative guidance.
