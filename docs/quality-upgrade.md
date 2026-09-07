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

## Cross-domain expertise discovery and request validation

The [shared discovery protocol](../skills/c2o-work/references/expertise-discovery.md) is part of shaping, not a new skill or a mandatory interview. Work selects it when a missing professional decision, dubious premise, or delegated unfamiliar process can affect the outcome. All eleven specialist entrypoints link to it for their relevant responsibilities.

Separate the user's goal from a proposed method. Keep statement source, kind, evidence state, and decision authority distinct: a user report is not automatically a verified fact, and an agent recommendation is not approval. Preserve intentional constraints and taste. Explain material revisions and obtain acceptance unless that class of choice was already delegated.

Discover missing dimensions from intended use, inputs, structure/process, quality, failures, continued use, and verification. For each material addition, explain the outcome it serves, the consequence of omitting it, and the lightest adequate treatment. This includes professional quality decisions the user may not know to name; it does not mandate a catalogue of documents or a design system for every task.

Synthetic examples:

| Request | Discovery target, not an automatic prescription |
|---|---|
| Make this scaffold feel finished | Determine unsettled experience/visual decisions, reuse real approved constraints, and produce coherent output without asking for specialist vocabulary. |
| Add a cache because the export is slow | Inspect the relevant timing evidence before accepting the proposed cause or replacing the explicit method. |
| Prove this campaign succeeded | Check the conclusion against data and provide truthful findings rather than forcing the requested narrative. |
| Have managers approve every reply | Investigate the actual error types, consequences, and handoffs before recommending proportional controls. |

Delegating the process permits only agreed classes of choices inside the existing boundary. It does not authorize spending, publishing, changing access, or production actions. Agent assumptions receive the same scrutiny as user assumptions; high-stakes judgments retain qualified review.

A tiny, well-founded task stays direct. A settled method is not reopened without new conflicting evidence. Converge when the next step is justified and authorized, with residual uncertainties explicitly testable; continue independent safe work. This is cross-domain prompt guidance, not a certified SwiftUI design system or proof that every professional omission will be discovered.

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
