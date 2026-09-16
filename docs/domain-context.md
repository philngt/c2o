# Optional Domain Context in C2O

C2O can use structured domain guidance without becoming a knowledge engine. The shared [domain-context reference](../skills/c2o-work/references/domain-context.md) helps select relevant sources, test applicability and exceptions, explain a decision briefly, and verify the actual result. It is guidance for an agent, not a guarantee that the agent follows it or has acquired expertise.

## Scope and compatibility

This change is independent of contextd and of any contextd PR or release. No new package, command, runtime, parser, graph database, manifest, permission mechanism, or persistent-context schema is added. The eleven skills and their host invocation names remain unchanged. Existing .context records remain optional and are not migrated or overwritten.

A contextd artifact may be supplied as an ordinary source, just like Markdown or another provider's output. That does not mean C2O implements contextd's format, runs its CLI, installs it, or treats diagnostic metadata as execution-ready context. Material warnings and unavailable source bodies remain visible.

## Where the protocol is used

| Existing skill | Selective use |
|---|---|
| c2o-work | Identify the knowledge gap, select a bounded source set, preserve source/gap handoffs |
| c2o-shape | Connect signals to testable mechanism hypotheses, not a guessed diagnosis |
| c2o-decide | Compare applicable strategies, constraints, exceptions, and evidence |
| c2o-create | Ground direction and critique in the task and approved system, not generic taste |
| c2o-verify | Separate recommended checks from actual evidence for the current artifact |
| c2o-learn | Propose evidence-backed, scoped corrections without automatic global writes |

These entrypoints link directly to the same reference and retain minimum fallback boundaries. Other skills retain their existing contracts; work can pass a concise source/gap note to a relevant specialist. Do not force a new domain-context stage onto every invocation.

## Examples without a provider

The paths below are illustrative project inputs, not files C2O installs. Substitute available project files. Plain-language requests avoid dependence on a host-specific invocation prefix.

```text
Use c2o-work to investigate why the comparison screen is hard to use.
Read our approved brief and the supplied design-guidance.md.
Separate observed problems from mechanism hypotheses, check exceptions to the
rules, and recommend the smallest useful investigation. Do not redesign yet.
```

```text
Use c2o-create to develop the approved comparison interface.
Preserve the deliberate dense layout and the requirement to compare two items
side by side. Use our project guidance where applicable, not as a reason to
hide a required action. Produce a reviewable prototype, not a published change.
```

```text
Use c2o-verify to review the current artifact against the original brief.
The supplied context summary lists selected sources but omits their bodies.
Inspect accessible sources and report unavailable evidence; do not repair the
artifact or treat the summary's self-check as a passing result.
```

When no relevant provider/document is available, proceed from accessible evidence and safe reversible defaults within authority. Report uncertainty; research only with available authorized tools. Missing required evidence or qualified review still blocks the dependent conclusion. Do not invent a provider, install tools, widen access, or stall independent safe work.

## Evaluation, not capability claims

The [domain-context scenarios](../evals/domain-context-scenarios.json) are synthetic, unrun definitions. Follow the [behavioral evaluation protocol](../evals/README.md), using main commit ae4366b55df2b0ae9ac85f84c0d4981d3470c834 as this change's baseline and the actual candidate commit. Keep model/version, host, tools, authority, input fixtures, and budget fixed. Test both work-orchestrated and direct specialist invocations without exposing evaluator rubrics to the agent.

Include missing-provider/reference, conflicting/wrong-scope sources, metadata-only input, adversarial instructions, rule exceptions, stale evidence, review-only, scoped learning, cross-domain, qualified-review, and tiny-task controls. Score actual artifact/evidence quality and boundary preservation, not use of cognition terminology or the persuasiveness of a rationale. Measure time/tokens only when recorded; report missing measurements honestly.

Run structural checks from a checkout:

```bash
python3 scripts/validate_c2o.py
python3 -m unittest discover -s tests -v
```

The PR validation workflow runs these checks on an ephemeral checkout with read-only repository permissions and no model/API keys. It does not run behavioral evaluations, validate live host integration, or demonstrate improved design quality, intelligence, or AGI progress. Keep real evaluation results separate from fixture definitions.
