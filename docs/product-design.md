# Product and UI design with C2O

C2O includes an optional product and UI design resource pack for choosing product structure, designing flows and states, composing interfaces, and verifying the result. Start with the existing `c2o-work` skill. Use `c2o-create`, `c2o-spec`, `c2o-execute`, or `c2o-verify` directly when that is already the stage you need.

The integration keeps the original eleven skills and their roles. The pack supplies reusable knowledge and artifacts within that workflow. The [agent routing guide](../skills/c2o-work/references/product-design.md) explains selective loading and source authority; the [resource index](../skills/c2o-work/assets/product-design/README.md) lists the available material.

## What is included

| Resource | Use it for |
| --- | --- |
| Product and UI guidance | Outcome, experience, visual decisions, platform behavior, and evidence |
| Component, data-view, layout, and screen catalogs | Comparing relevant patterns and defining responsibilities |
| 24 Markdown templates | Missing sections or documents, from a brief and product pack to domain, feature, UI, technical, validation, and delivery specifications |
| SwiftUI and web profiles | Selecting applicable implementation and verification checks |
| Lifestyle and Utility Apple app recipes | Choosing a starting category and platform-specific behavior |
| SwiftUI source and a Python generator | Creating a separate source project when scaffolding is requested |
| Examples and optional Python checkers | Understanding contracts and checking template or evidence-record structure |

The catalogs describe patterns and contracts; they are not a complete implemented component library. Example decisions and business hypotheses are illustrative. Source code, plans, and populated templates do not constitute runtime or user-research evidence.

## Adopt only the parts your task needs

1. Read the existing request, repository instructions, brief/spec, decisions, acceptance, and relevant code or artifact.
2. Identify the next unresolved product or interface decision, missing specification detail, or required check.
3. Open only the corresponding resource through the [routing guide](../skills/c2o-work/references/product-design.md). Continue through the existing C2O stage.
4. Reuse current documents and IDs. Add a section or select a template only when it makes the next action clearer.
5. Produce the requested scope and inspect the actual result with appropriate evidence.

A small UI correction can remain a local edit with a few relevant checks. A new app can start from a combined [product pack](../skills/c2o-work/assets/product-design/templates/product/product-pack.md); separate documents are useful when responsibilities or change needs justify them. The existence of 24 templates does not make 24 documents necessary. Existing project documents need no template metadata retrofit.

Existing sources retain their roles. If `.context/acceptance.md`, a project spec, or another native system already owns acceptance, keep it. Do not create a second writable source merely to use this pack. Selected documents and directions inherit the current task's authority; they do not create new approval gates or permission to publish.

The pack's `quick`, `standard`, and `deep` labels describe how much guidance may be useful. They do not replace C2O's intervention levels or add another required workflow. A representative quality slice still leads to all committed deliverables; it does not reduce the requested scope.

## Example requests

Use the normal invocation syntax for your host. These examples use Codex; replace `$c2o:` with `/c2o:` for Claude Code or Antigravity CLI.

### Improve an existing interface

```text
Use $c2o:c2o-work to fix the confusing save/cancel behavior in this editor.
Inspect the current code and acceptance first. Use the product-design resources
only where they clarify state ownership or recovery. Preserve the current
design system and implement and verify the smallest complete correction.
```

### Explore a new direction

```text
Use $c2o:c2o-create to explore the collection flow for this app.
Use the relevant product-design resources to compare interaction and layout
choices with the same task and data. Produce reviewable directions at useful
fidelity and explain the trade-offs. This request ends at design artifacts.
```

### Write a useful specification

```text
Use $c2o:c2o-spec for this approved flow. Reuse our existing brief and
.context/acceptance.md. Add only missing domain rules, UI states, failure paths,
and verification methods from the product-design resources. Keep existing
sources authoritative; a new product-document set is not required.
```

### Review without changing the result

```text
Use $c2o:c2o-verify to review this implementation against the existing spec.
Use relevant product-design checks and inspect the current artifact.
Report pass, partial, fail, or not-tested with evidence. Do not repair the app
or change acceptance during this review.
```

## Optional records and checkers

The imported design `project.json` / `verification.json` format is optional. Deliberately select it for a scope when it is useful; existing delegated choices do not need another approval. It can own records for a new scope or be a clearly identified derived checker input. It must not silently replace an existing acceptance source.

The [tools guide](../skills/c2o-work/assets/product-design/tools/README.md) explains the Python checkers. `TEMPLATES_VALID` checks reusable template structure. `RECORDS_READY` checks declared records, coverage flags, and file hashes. Neither result proves product behavior, visual quality, authentic manual observations, complete dependency coverage, or release authorization.

C2O keeps its existing verification vocabulary. Optional JSON `PASS` and `FAIL` require evidence inspection; `NOT_RUN` and `BLOCKED` retain untested work and its reason. C2O `partial` has no lossless equivalent in that format and must remain visible in the C2O report and evidence without creating competing records. An applicability exemption cannot hide an untested requirement. See the [status mapping](../skills/c2o-work/references/product-design.md#preserve-verification-meaning).

## Apple source starter

Use the [starter](../skills/c2o-work/assets/product-design/starters/apple/README.md) only when creating source scaffolding is part of the task. It provides Lifestyle collection and Utility text-workbench flows, shared Swift source, and optional widget source. Choose an authorized new output directory outside the starter; the generator refuses an existing destination.

The generated root `project.json` is an **XcodeGen specification**, used to generate an Xcode project. The generated `.design/project.json` is a **separate design acceptance scaffold**, and `.design/verification.json` begins with unrun checks. Similar filenames do not make these interchangeable. The generator emits these design records for a new starter; adopting them as the project's canonical records remains a deliberate choice.

The generator does not install XcodeGen, modify Apple accounts, register App Groups, build, sign, or publish. The [getting-started instructions](../skills/c2o-work/assets/product-design/starters/apple/GETTING_STARTED.md) and [native checks](../skills/c2o-work/assets/product-design/starters/apple/NATIVE_CHECKS.md) describe subsequent work. Follow existing authorization and verify actual available tools before taking those steps.

This import includes Swift and XCTest source without native build or runtime evidence. Source generation and Python checker results do not establish compilation, persistence, navigation, widget behavior, accessibility, signing, or distribution readiness. Native claims require current evidence from the actual generated project and target environment. Starter UI strings are in Vietnamese; reviewed localization for other languages is not included.

## Provenance and maintenance

The resource pack was adapted from the standalone **C2O Design 1.5.0** materials developed for this integration. That version identifies the source collection; it does not change the C2O plugin version or certify an app. Many source documents and templates remain in Vietnamese. The [source notes](../skills/c2o-work/assets/product-design/SOURCES.md) retain reference provenance and limitations.

The standalone PDF, standalone release history, validation report, and checksum manifest are not bundled. The current repository changes and checks describe this integration; historical standalone results must not be presented as current verification of the adapted files.

Maintain only evidence-backed lessons with clear applicability. Keep local product facts in their existing project sources. Shared template or pack changes are separate proposals for authorized review, and changing a pack version does not automatically migrate project documents or revalidate an app.
