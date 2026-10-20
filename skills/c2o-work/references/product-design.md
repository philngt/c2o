# Product and UI Design Resources

Use these optional resources when product structure, interface behavior, visual decisions, or platform checks can change the next action. They extend the existing C2O stages; they do not add a skill, work state, approval gate, runtime, or required directory. A tiny well-founded task still needs direct work.

The [resource index](../assets/product-design/README.md) contains the adapted C2O Design 1.5 material. This router and the [adoption guide](../../../docs/product-design.md) are in English; many source guides, templates, examples, and starter UI strings are in Vietnamese. Write user-facing work in the user's language and retain the project's identifiers.

## Preserve the current contract

- Recover the original request, accepted decisions, full deliverables, completion level, criteria, existing sources, and authorized actions before selecting resources.
- Apply [domain-context.md](domain-context.md): inspect the relevant content, its applicability and exceptions; distinguish guidance, accepted decisions, hypotheses, and actual evidence.
- The [framework](framework.md), [outcome contract](outcome-contract.md), existing project instructions, and the user's decisions retain their roles. The pack's principles and catalogs are conditional guidance, not a replacement source of authority.
- Continue reversible choices already delegated. Do not ask again for a settled decision or create a template approval ceremony. A selected direction, accepted document, or checker result grants no new external action authority.
- Preserve original scope and quality. A representative flow or quality slice establishes shared decisions; continue through every committed deliverable unless scope was explicitly changed or work is reported blocked.
- During review-only work, inspect and report without repairing the artifact, rewriting acceptance, or changing the subject's state. Production repair loops apply only within existing authorization.

For source conflicts, identify the actual scope, owner, accepted decision, and evidence. Resolve only the affected decision; continue independent authorized work. Do not make the latest file, a catalog default, or a new template override an established requirement.

## Route through existing skills

Select the row that addresses the current blocker. Do not read the whole pack or invoke every stage.

| Existing responsibility | Useful resources and intended use |
| --- | --- |
| `c2o-work` | Use this router to select a bounded source set and retain outcome, authority, scope, and synthesis. |
| `c2o-shape` | [New app guidance](../assets/product-design/use-cases/new-app.md) and the [document guide](../assets/product-design/documentation/README.md) can expose missing product or domain decisions; preserve observations and hypotheses. |
| `c2o-decide` / `c2o-grill` | [Exploration](../assets/product-design/core/exploration.md) supports meaningful unresolved alternatives. Grill remains conditional on its existing trigger; a new UI does not require deep inquiry. |
| `c2o-spec` / `c2o-slice` | Select sections from the [product pack](../assets/product-design/templates/product/product-pack.md), [traceability guide](../assets/product-design/documentation/traceability.md), or [delivery plan](../assets/product-design/templates/product/delivery-plan.md) to connect requirements, invariants, acceptance, and committed slices. |
| `c2o-create` | Use [composition](../assets/product-design/core/ui-composition.md), [exploration](../assets/product-design/core/exploration.md), [baseline](../assets/product-design/core/baseline.md), and [assets](../assets/product-design/core/assets.md) for the requested direction or artifact. Stop at design when implementation was not requested. |
| `c2o-execute` | Implement accepted behavior using relevant [SwiftUI](../assets/product-design/profiles/swiftui.md) or [web](../assets/product-design/profiles/web.md) guidance and the actual project patterns. The [Apple starter](../assets/product-design/starters/apple/README.md) is a separate optional source scaffold. |
| `c2o-deliver` | Use selected [documentation templates](../assets/product-design/documentation/README.md) for the requested handoff or package; retain the existing boundary for sending and publication. |
| `c2o-verify` | Inspect the actual artifact and native acceptance records. The [evidence guide](../assets/product-design/core/evidence.md) and [optional tools](../assets/product-design/tools/README.md) support evidence handling, not automatic product verification. |
| `c2o-learn` | Update existing relevant decisions and evidence with applicability and invalidation triggers. A reusable pack improvement remains a proposal for authorized review. |

## Select only needed design detail

Start with the user's task, data meaning, and applicable states, then inspect the resources that can change a decision or check:

| Gap | Read selectively |
| --- | --- |
| Interaction, state, or component ownership | [Component contracts](../assets/product-design/core/components.md) and relevant [component catalog entries](../assets/product-design/catalog/components.md) |
| Data representation or comparison | [Data views](../assets/product-design/core/data-views.md) and relevant [data-view patterns](../assets/product-design/catalog/data-view-patterns.md) |
| Regions, navigation, scrolling, or adaptation | [Layout](../assets/product-design/core/layout.md), [layout patterns](../assets/product-design/catalog/layout-patterns.md), and [screen patterns](../assets/product-design/catalog/screen-patterns.md) |
| A reusable rule across screens | [Baseline](../assets/product-design/core/baseline.md) with the existing design system, accepted references, and current implementation |
| New Apple app category or platform | [App templates](../assets/product-design/app-templates/README.md) and the [module matrix](../assets/product-design/app-templates/module-matrix.md), restricted to requested capabilities |

Catalog entries supply options, not implemented components or universal design laws. Verify material platform claims against the project's target and current authoritative documentation. A source example does not establish runtime behavior.

The pack's `quick`, `standard`, and `deep` labels describe reading depth. Its Inspect → Frame → Design → Build → Verify → Learn activities fit inside the existing C2O workflow. Neither replaces intervention levels, introduces required gates, or forces another planning loop.

## Keep existing records authoritative

Use the project's current brief/spec, native requirements and evidence, or relevant `.context/` records first. A small contract may stay in the conversation. Link to sources rather than copying their values into competing documents; preserve criterion origins, required status, accepted revisions, and evidence limits.

The [24-template catalog](../assets/product-design/documentation/template-registry.json) offers missing sections or new-document starting points. It does not require using every template, creating an index, assigning IDs to every paragraph, or adding metadata to existing project documents. The [template standard](../assets/product-design/documentation/template-standard.md) describes the reusable catalog; project instances may use equivalent existing formats and only useful fields.

Use one combined pack when useful, or split by real ownership and change needs. Copying a template does not transfer canonical ownership. Register a new source only when it actually replaces or fills a missing responsibility within the current task. Repair links when copying; keep provenance only where useful.

### Optional legacy JSON records

The imported `project.json` / `verification.json` evidence format and Python checker are optional. Use them only when deliberately selected for this scope; this choice may already be delegated and does not itself require another user approval. No `.design/` directory or JSON migration is required to use the design guidance.

If JSON is selected as the canonical acceptance/evidence format for a new scope, record that choice and avoid a second writable acceptance ledger. If it is a derived checker input, identify the native source, reconcile its current requirements and results, and keep the derived copy subordinate. A JSON hash does not establish that the native source or omitted dependencies are unchanged.

Never overwrite a live report with a scaffold or example. Never weaken a required criterion to satisfy the checker. Preserve current unaffected evidence, and invalidate checks affected by artifact, environment, source, or assumption changes.

## Preserve verification meaning

C2O reporting continues to use `pass`, `partial`, `fail`, and `not-tested`, with the existing aggregation in [outcome-contract.md](outcome-contract.md). The optional JSON vocabulary is a separate record format:

| JSON record | C2O interpretation after inspecting evidence |
| --- | --- |
| `PASS` | `pass` only for the current artifact and complete required scope actually supported by evidence |
| `FAIL` | `fail`; retain any untested coverage as well |
| `NOT_RUN` | `not-tested` |
| `BLOCKED` | `not-tested` with the actual blocker; preserve any separately observed partial coverage |
| `NOT_APPLICABLE` | A justified applicability decision permitted by the contract; never an automatic required pass |

There is no lossless JSON status for C2O `partial`. Preserve partial results in the C2O report and supporting evidence, retaining a native record where one already exists; do not create a competing ledger. Separate independently verifiable criteria when useful, without deleting committed coverage. Never convert partial coverage into `PASS` or erase a known failure because another case is blocked.

`RECORDS_READY` means declared records and hashes satisfy the checker's contract. `TEMPLATES_VALID` concerns reusable template structure. Neither establishes authentic observations, complete dependencies, visual quality, runtime behavior, outcome fit, qualified review, or permission to release. Read the evidence and report the C2O verdict separately.

Source review, compilation, rendered inspection, interaction, accessibility checks, and real user research support different claims. Missing tools or required human review remain explicit gaps. A completed review can report a failed artifact; a completed source scaffold is not a verified native app.

## Use the Apple generator only for requested scaffolding

Inspect the [starter guide](../assets/product-design/starters/apple/README.md), [generated-project instructions](../assets/product-design/starters/apple/GETTING_STARTED.md), and [native checks](../assets/product-design/starters/apple/NATIVE_CHECKS.md) when source scaffolding is part of the requested outcome.

- Select the relevant category and supported platforms from the actual product need; conditional blueprint capabilities are not all implemented.
- Use an authorized new output path outside the starter; the generator requires that destination not to exist. Preserve existing projects and unrelated work.
- The generated root `project.json` is an XcodeGen specification. It is distinct from `.design/project.json`, the optional design acceptance scaffold emitted by this generator, and `.design/verification.json`, whose results start unrun.
- Generator success proves source/configuration generation only. Inspect the generated result; obtain current build, rendering, interaction, persistence, and relevant widget evidence before making native readiness claims.
- The generator does not install XcodeGen, register an App Group, configure an Apple account, build, sign, or publish. Follow the existing authorization for any later action; do not assume unavailable tools or credentials.

The imported Swift source and XCTest files have no bundled evidence of native build or runtime success. Keep those checks `not-tested` until performed for the actual generated project and environment. The source contains Vietnamese UI strings; localization is a product-specific requirement, not an already completed capability.

## Fallback and completion

If the router's linked resources or optional tools cannot load, continue with the original C2O skills, available project documents, relevant authoritative sources, and actual artifacts. Do not install a provider, fetch a missing pack, create new records, or stop independent safe work merely to satisfy this guide. Report missing evidence only where it affects a required claim.

Return full deliverable coverage, the actual changes or artifacts, current acceptance evidence, material decisions, and remaining gaps. Keep task completion, verification, and external delivery state separate. Stop at the user's requested boundary and retain useful learning in the existing project context.
