---
name: c2o-grill
description: Stress-test a consequential plan, decision, or idea by mapping dependent decisions, researching facts, interviewing the user in prerequisite-aware rounds, and requiring confirmation before action. Use when the user explicitly asks to be grilled or challenged, or when C2O intervention level 4–5 contains several branching decisions whose answers depend on one another. Avoid for small reversible tasks, already-clear specifications, or questions that require a prototype or direct evidence rather than more discussion.
---

# C2O Grill

Expose hidden decisions without replacing the user's judgment. Treat this as an optional deep-inquiry stage between shaping and deciding, not as the entire C2O workflow.

## Establish the boundary

1. State the outcome being protected by the inquiry.
2. Define the subject boundary and explicit non-goals.
3. Load only relevant facts, decisions, and assumptions from project context.
4. Confirm that the issue contains dependent, consequential decisions. Exit to normal C2O flow when a reversible default or a single decision is sufficient.

## Build the decision tree

Represent each unresolved node with:

- `kind`: fact, decision, or experiment;
- `question`: one answerable uncertainty;
- `prerequisites`: nodes that must settle first;
- `consequence`: what changes based on its answer;
- `status`: open, researching, provisional, settled, or deferred;
- `evidence`: direct observation or source when available.

Use the shaped outcome as the root. Add a branch only when its answer can materially change scope, behavior, architecture, cost, risk, or verification.

## Work the frontier

Repeat:

1. Recompute the frontier: every open node whose prerequisites are settled.
2. Resolve fact nodes through files, tools, documents, tests, or bounded read-only exploration. Do not ask the user for facts the environment can establish.
3. Convert uncertainties that discussion cannot settle into experiment nodes. Propose the smallest prototype or observation and pause only the dependent branch.
4. Ask the user every independent decision in the current manageable frontier. If the frontier is too large for one coherent round, split the subject into independent subtrees and let the user choose the order; do not silently truncate it.
5. Wait for answers. Recommendations do not become decisions until the user explicitly accepts them.
6. Record settled decisions and changed assumptions, then recompute the tree. Never pre-write later rounds.

Ask one question at a time when the user requests it or when language, accessibility, or cognitive-load needs make rounds counterproductive.

## Format a round

```markdown
## Decision round <n>

### Q1 — <decision title>
Why this is decidable now:
Question:
Options:
Recommendation:
Accepted trade-off if chosen:

### Q2 — <decision title>
...

Answer by number. “Use your recommendation” counts as an explicit decision.
```

Offer no more than three viable options per decision unless the domain genuinely requires more. Include `do nothing` when credible. Distinguish evidence, inference, and assumption.

## Handle unknowns honestly

- Research an answerable fact.
- Propose a cheap reversible experiment when evidence is missing.
- Route questions about appearance, feel, or emergent behavior to a prototype or C2O vertical slice.
- Accept “I do not know” as information; do not pressure the user into false certainty.
- Mark an irrelevant branch as a non-goal.
- Split the inquiry when the tree reveals that the original scope contains several independent outcomes.

Do not invent numeric thresholds without a baseline or explicit constraint.

## Preserve context

When `.context/` exists, store only durable results:

- accepted choices and revisit triggers in `decisions.md`;
- open, confirmed, or disproved beliefs in `assumptions.md`;
- unresolved material branches in `open-questions.md`;
- the current state as `INQUIRING` in `current-goal.md`.

Do not save the interview transcript or every discarded possibility.

## Exit gate

Finish only when:

1. no material decision node remains silently open;
2. unresolved fact or experiment nodes are explicit;
3. the user confirms that the shared understanding is sufficient for the next step.

Do not implement during this skill. Return:

```markdown
## Grill summary
Outcome:
Scope and non-goals:
Decisions accepted:
Assumptions:
Evidence still needed:
Deferred branches:
Revisit triggers:
Shared understanding: confirmed | awaiting-confirmation
Recommended next C2O stage:
```

Move to C2O Spec only after confirmation. Move to C2O Slice first when an experiment or prototype is needed.
