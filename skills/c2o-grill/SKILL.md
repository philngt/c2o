---
name: c2o-grill
description: Stress-test a consequential plan through prerequisite-aware expert guidance, evidence gathering, and user-owned decisions. Use when explicitly asked to be grilled or when several consequential decisions depend on one another. Avoid small reversible tasks, settled specifications without new conflicting evidence, and uncertainties better resolved by direct observation or an authorized prototype.
---

# C2O Grill

Expose hidden decisions without replacing the user's values or authority. Research specialist facts and recommend means instead of asking an inexperienced user to guess. This is an optional deep-inquiry stage, not the whole workflow.

## Establish the boundary

State the protected outcome, full required scope, non-goals, and current authorization. Load only relevant facts and decisions. Exit to normal C2O flow when shaping, a reversible default, or one decision is sufficient.

Classify decisions before asking:

- user-owned: outcome, values, priorities, taste, budget, risk tolerance, commitments, approval;
- advisor-led: methods, tools, architecture, or implementation choices supportable from evidence;
- qualified review: consequential legal, medical, financial, safety, regulatory, or licensed judgment.

Use plain language. Do not infer competence from brevity, language fluency, disability, job title, or jargon. Ask about experience only when it changes safety, viable options, or useful explanation depth.

Use [expertise-discovery.md](../c2o-work/references/expertise-discovery.md) to expose missing professional dimensions and questionable premises before expanding the decision tree. Keep statement source and evidence separate from acceptance or delegation. A clearly stated method can still need validation; an intentional constraint must not be discarded. Research the premise before challenging it, and use a concrete comparison when preferences cannot be articulated. Do not add branches that cannot affect the next action, quality, or risk.

## Build and work the decision frontier

For each material node record kind (`fact`, `decision`, `experiment`), question, prerequisites, consequence, status (`open`, `researching`, `provisional`, `settled`, `deferred`), and evidence. Add branches only when they change outcome, scope, cost, risk, quality, or verification.

1. Resolve unblocked fact nodes through accessible sources or bounded read-only investigation. Do not ask the user for facts the environment can establish.
2. Choose the least costly useful evidence: inspect for facts, ask for user values, prototype for feel, test for behavior, and seek approval for authority. Talking is not a substitute for an observable experiment.
3. Convert empirically answerable uncertainty into an experiment proposal with a question, boundary, expected observation, and authorization needed. Pause only dependent branches; do not perform production work inside this inquiry skill.
4. Recommend advisor-led choices with rationale, evidence, trade-off, confidence, and revisit trigger. A reversible choice may proceed later only within existing delegated authority.
5. Ask only currently unblocked user-owned decisions and consequential approvals. Give at most three viable options unless the domain requires more; include doing nothing when credible.
6. Wait for necessary answers, record accepted decisions, and recompute dependencies. Do not pre-write later rounds or repeat settled questions.

Ask one question at a time for unfamiliar users or guided interviewing. Group independent simple questions only when it improves the decision. Accept not knowing: offer a concrete example, recommendation, or prototype proposal rather than pressuring the user into false certainty.

Use [outcome-contract.md](../c2o-work/references/outcome-contract.md) to keep necessary implications separate from optional additions. Do not invent numeric thresholds or let an expert recommendation silently reduce requested scope.

## Format a round

```markdown
## Decision round <n>
Question and owner:
What this means and why it matters now:
Viable options:
Recommendation:
Evidence, confidence, and trade-off:
Decision or approval needed:
```

Accepting a recommendation does not waive qualified review or authorize publishing, spending, production changes, or other new action boundaries.

## Preserve context and exit

Store only durable choices, assumptions, evidence gaps, and revisit triggers in relevant `.context/` files. Keep the current task in `INQUIRING`; never overwrite another active goal or save the interview transcript.

Finish when no material decision is silently open, remaining facts/experiments are explicit, and shared understanding is confirmed. Summarize practical consequences and invite correction, not a terminology quiz. An existing explicit approval of the same summary counts; changed material scope or risk requires renewed resolution.

Return outcome, scope/non-goals, accepted/delegated decisions, assumptions, experiments/evidence needed, deferred branches, qualified review, revisit triggers, and `shared understanding: confirmed | awaiting-confirmation`.

Do not create, deliver, or implement during this skill. Recommend Spec after confirmation, or Slice when an authorized experiment must be planned. Inquiry alone does not authorize that experiment.
