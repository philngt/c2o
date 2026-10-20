# C2O Design agent entry point

Use these optional resources when they help the current product-design decision or check. The existing C2O skills, outcome contract, user instructions, project decisions, selected acceptance/evidence sources and action boundary remain authoritative. This is not another skill, mandatory workflow or automatic hook. A small task can stay in the conversation without documents, `.design`, JSON or template metadata.

## Load only what is needed

1. Read the project's existing brief/spec, relevant code and design conventions. Reuse existing context instead of creating competing documents.
2. Read relevant sections of `core/principles.md` as design guidance relative to this resource root. Check applicability and exceptions against the project contract; the resource does not become canonical policy by being loaded.
3. Read the selected acceptance/evidence source when needed: the existing conversation, `.context/acceptance.md`, or native project artifact/system. Read `.design` JSON only if its optional profile was explicitly selected; generated or example records do not establish authority.
4. Read only the relevant profile: `profiles/swiftui.md` or `profiles/web.md`. For mixed products, assign acceptance to each surface.
5. Use relevant design activities from `core/workflow.md` within the current C2O gate; do not restart a second loop. Read `core/evidence.md` when planning/reporting design checks or explicitly using the legacy JSON profile. Open templates only when missing content would help.
6. For a new app or unresolved direction, read `use-cases/new-app.md` and `core/exploration.md`. For layout proposals, read `core/layout.md`; for cross-screen consistency, read `core/baseline.md`; for artwork, icons or motion, read `core/assets.md`. These are selective resources within the existing C2O work, not required stages.
7. For a new or changed screen structure, read `core/ui-composition.md`. Read `core/components.md` when choosing or changing component behavior; read `core/data-views.md` when presenting or transforming data. Open the relevant entries in `catalog/components.md`, `catalog/data-view-patterns.md`, `catalog/layout-patterns.md` and `catalog/screen-patterns.md`; the existence of a catalog does not require using every pattern or creating every document.
8. For a new Apple app, read `app-templates/README.md`, the selected Lifestyle/Utility category and only the supported platform recipes. Use `app-templates/module-matrix.md` to decide capabilities. If source scaffolding is requested, use `starters/apple/README.md` and its generator in a new directory; inspect actual source and native acceptance before claiming readiness. Blueprint cases, generator success and native test results are separate evidence.
9. For business design, product blueprints, PRDs, domain/feature/technical specs, delivery or release documentation, read `documentation/README.md` and `documentation/traceability.md`. Resolve the existing canonical document/index first. A small app may use one product pack; split only where ownership or change needs justify it. Treat hypotheses, adopted decisions, source implementation and runtime evidence as distinct. Reuse the selected criteria and evidence source; never overwrite real verification with an example report or create a competing JSON authority.
10. When authoring the bundled catalog templates, follow `documentation/template-standard.md`. Its twelve-field metadata structure applies to the 24 catalog source templates. Project work may reuse a useful section or an existing artifact without metadata, an index, status migration or reformatting. Retain useful provenance and repair links when copying; identify the selected source before replacing one. `tools/template_check.py` checks catalog structure only, not filled project documents or product behavior.


Write user-facing work in the user's language. Keep identifiers and code in the project's conventions.

## Establish the work

Reuse the observable outcome, full requested deliverables, scope and lowest sufficient intervention level already established by C2O. `quick`, `standard`, `deep` are optional historical design-depth labels, not required modes or stored fields. Distinguish facts, assumptions, decisions and experiments.

Proceed on small reversible decisions using existing context. Ask only when the answer materially changes the next action and cannot be established by reading or a cheap experiment. Do not add approval gates that the project or user did not require.

## Design and implement

Inspect, Frame, Design, Build, Verify and Learn are local activity headings mapped to existing C2O skills in `core/workflow.md`; skip satisfied work and stop at the requested boundary. Model the task, data, flow and applicable states before choosing visual treatment. Reuse working patterns, semantic tokens and platform controls. Add custom behavior only for a concrete need and verify the responsibilities it introduces.

Keep visual preferences configurable. Do not ban equal cards, emoji, black/white, particular punctuation or native controls as universal laws. Explain choices by their effect on the user's task and the project direction.

For implementation, distinguish experiment and delivery slices and deliver the agreed usable flow with real state transitions. One slice never completes a larger commitment; preserve and track every remaining required deliverable. Preserve unrelated work. Design-only work returns its specified artifact and review; review-only work reports findings without repairs. Do not silently implement or publish.

## Select and compose UI

Start with the user's task and the data meaning, then choose representation, interactions, regions and reusable components. Compare alternatives only when the choice is consequential. A card is a container; a CSS grid is layout; neither alone specifies data semantics or keyboard behavior. A table with controls is not automatically an interactive grid. Use platform semantics and actual supported APIs.

For each data view, retain stable identity, field meaning, units, time, source, uncertainty and dataset scope. Distinguish unknown from zero and missing from permission-restricted. Specify query, filter, sort, selection, aggregation, paging and export only where the task needs them. Preserve context when adapting a layout; do not hide required comparison fields merely to fit a narrow screen.

Choose reuse, variant, composition or a new component based on responsibilities. Define content, anatomy, semantics, applicable states and emitted events. Identify who owns query, selection, draft, committed data and operation status. Components can have concurrent states; do not force all behavior into one loading/empty/error enum. Do not make a row or field silently commit domain data or discard a screen's draft.

Map screen regions to data views, component contracts, state owners and acceptance criteria. Catalog IDs (`CP`, `DVP`, `LP`, `SP`) name reference patterns; project IDs (`CMP`, `DV`, `L`, `SCR`) name scoped decisions. Contracts are not implemented UI, and illustrative examples are not runtime evidence. Reuse the project's existing contracts instead of duplicating canonical data rules.

## Explore, choose, keep a baseline

Generate alternatives only for meaningful unresolved decisions. Separate product concepts, interaction/information architecture, layout and visual expression. Compare equivalent tasks, data and artifact fidelity; use hard constraints before tradeoffs. Record selected option, reasons, uncertainty and revisit triggers. Preserve the project's decision status and acceptance/delegation source. A local `selected` label is not a test pass, user approval or a new gate.

Keep the chosen baseline revision, canonical documents and representative references available to later screens. Layout proposals include regions, priority, actions, scrolling, state, adaptations, asset slots and fallback. Images support the baseline alongside tokens and behavior contracts; use platform and accessibility requirements to justify intentional differences.

## Asset work

Keep actual UI text, controls, state and data in implementation code. Prefer suitable system symbols and existing assets before producing bespoke art. Treat genuine record/product photos differently from generated illustration; do not invent evidence about a real object.

Inventory assets by purpose, source, production route, placement, output requirements, variants and fallback. Use the right available tool for raster, vector, code and runtime review; do not assume a specific provider, model, price or plugin installation. Respect the user's established authorization and budget, and use bounded iteration. A crop may be a legitimate reference or deliverable when the source, quality and task support it.

Inspect candidates and final exports at intended display sizes and in their actual UI context. Preserve source/derived files and record meaningful provenance. Separate export/format checks from runtime rendering, motion and accessibility. Metrics diagnose scoped differences; they do not establish semantic correctness, complete screen coverage or native readiness.

The asset manifest and option/decision/baseline/layout/component/data-view/screen IDs are descriptive contracts. The Python checker does not validate their semantics or automatically resolve their links. Add relevant contract files and actual implementation dependencies to declared verification inputs and review the content yourself.

## Verify honestly

Map each claim to an existing criterion and method. Source checks, rendered inspection, interaction tests and expert critique prove different things. C2O reports `pass`, `partial`, `fail`, `not-tested`; keep missing-tool/environment/data reasons and pending review explicit. N/A is an applicability decision with rationale, not a pass. Preserve partial evidence; do not map `partial` to legacy `PASS`. A skipped check or empty test run is not a pass.

Use the project's actual build/test/render tools. The optional legacy JSON validator only validates its evidence records; it does not test the application. Snapshot hashes do not establish a pass, authenticity or complete dependency coverage.

Only when the legacy JSON profile is explicitly selected and checking its records is useful, use the checker with the actual checkout and record paths. For example:

```bash
python3 /path/to/c2o/skills/c2o-work/assets/product-design/tools/design_check.py validate --root . --project .design/project.json --report .design/verification.json
```

Replace example paths with the actual selected locations. Uppercase statuses and `RECORDS_READY` retain their checker-profile meaning; they do not replace C2O verdicts or completion. Read the underlying evidence, preserve the selected acceptance source and report the actual checker result. No checker run is required to use these design resources.

## Review and finish

For critique, load the brief/criteria and inspect the actual artifact. Each finding identifies location, observation, user impact, severity and how to verify a fix. Separate suggestions from defects. Return zero findings when justified; do not manufacture a rejection quota.

During authorized production, fix required problems within scope and recheck affected criteria; stop optional polishing once acceptance is supported. During review-only work, report defects without changing the subject. Retain scoped decisions/findings that materially help future work; propose shared-resource changes through their owner rather than automatically writing global rules.

Finish with the outcome, full deliverable coverage, artifact/change, evidence, remaining gaps and one next action when needed. Separate task progress, artifact verdict and external delivery. A completed review can judge its subject fail; required untested implementation remains partial or blocked; prepared is not sent/released. State whether a limitation concerns the app, optional records or the environment.
