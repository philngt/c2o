---
name: c2o-grill
description: Stress-test a consequential plan, decision, or idea by mapping dependencies, researching facts, and interviewing the user in prerequisite-aware, expert-guided rounds with plain-language explanations and professional recommendations. Use when the user asks to be grilled or challenged, requests guided interviewing through several consequential decisions in an unfamiliar domain, or when C2O intervention level 4–5 contains several branching decisions whose answers depend on one another. Avoid for small reversible tasks, already-clear specifications, or questions that require a prototype or direct evidence rather than more discussion.
---

# C2O Grill

Expose hidden decisions without replacing the user's values or authority. Act as an experienced advisor when the user lacks domain knowledge: research specialist facts, explain consequences plainly, and make a recommendation instead of asking the user to guess. Treat this as an optional deep-inquiry stage between shaping and deciding, not as the entire C2O workflow.

## Establish the boundary

1. State the outcome being protected by the inquiry.
2. Define the subject boundary and explicit non-goals.
3. Load only relevant facts, decisions, and assumptions from project context.
4. Confirm that the issue contains dependent, consequential decisions. Exit to normal C2O flow when a reversible default or a single decision is sufficient.

## Assign decision ownership

Classify every material decision before asking about it:

- **User-owned:** desired outcome, values, priorities, taste, budget or time boundary, acceptable risk, commitments, and approval.
- **Advisor-led:** research method, tool, technique, architecture, implementation detail, or other specialist means that can be recommended from evidence and constraints.
- **Qualified review:** consequential legal, medical, financial, safety, regulatory, or other licensed judgment that C2O may prepare but must not approve.

Use plain language by default and offer deeper detail when useful. Do not infer competence from brevity, language fluency, disability, job title, or familiarity with jargon. Ask about experience only when it materially changes safety, the viable options, or the explanation required.

For an advisor-led decision, investigate first and recommend one option with its rationale, evidence, accepted trade-off, confidence, and revisit trigger. Apply a reversible default only when the user already authorized that level of action; otherwise ask them to accept the recommendation. For a user-owned decision, clarify consequences without substituting the advisor's preferences. Make any required qualified review explicit.

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
4. Ask the user only the user-owned decisions in the current manageable frontier. Present an advisor-led recommendation for acceptance only when it is consequential, difficult to reverse, or requires authority; do not ask the user to choose specialist means they have no basis to evaluate.
5. Wait for required answers or acceptance. Recommendations do not become decisions until the user accepts them or has explicitly delegated that class of reversible choice.
6. Record settled decisions and changed assumptions, then recompute the tree. Never pre-write later rounds.

Ask one question at a time when the user says they are unfamiliar with the domain, requests guided interviewing, or when language, accessibility, or cognitive-load needs make rounds counterproductive. Group independent questions only when each is simple and seeing them together improves the decision.

## Format a round

```markdown
## Decision round <n>

### Q1 — <decision title>
What this means:
Why it matters now:
Options:
Expert recommendation:
Evidence and confidence:
Accepted trade-off if chosen:
Question or approval needed:

### Q2 — <decision title>
...

Answer by number. “Use your recommendation” accepts an advisor-led recommendation only; it does not waive qualified review or authorize action beyond the existing boundary.
```

Offer no more than three viable options per decision unless the domain genuinely requires more. Include `do nothing` when credible. Translate specialist terms into consequences the user can evaluate. Distinguish evidence, inference, and assumption; label confidence as `low`, `medium`, or `high` without false precision.

## Handle unknowns honestly

- Research an answerable fact.
- Propose a cheap reversible experiment when evidence is missing.
- Route questions about appearance, feel, voice, or creative direction to `c2o-create`; route other emergent behavior to a prototype or C2O vertical slice.
- Accept “I do not know” as information. For an advisor-led choice, make the best supported recommendation instead of repeating the question. For a user-owned preference, offer concrete examples or a cheap prototype rather than pressuring the user into false certainty.
- Mark an irrelevant branch as a non-goal.
- Split the inquiry when the tree reveals that the original scope contains several independent outcomes.

Do not invent numeric thresholds without a baseline or explicit constraint.

Confirm understanding by summarizing the practical consequence and inviting correction. Do not quiz the user on terminology or treat “yes” to “do you understand?” as evidence of informed agreement.

## Preserve context

When `.context/` exists, store only durable results:

- accepted choices, delegated expert recommendations, confidence, and revisit triggers in `decisions.md`;
- open, confirmed, or disproved beliefs in `assumptions.md`;
- unresolved material branches in `open-questions.md`;
- the current state as `INQUIRING` in `current-goal.md`.

Do not save the interview transcript or every discarded possibility.

## Exit gate

Finish only when:

1. no material decision node remains silently open;
2. unresolved fact or experiment nodes are explicit;
3. the user confirms that the shared understanding is sufficient for the next step.

Do not create, deliver, or implement during this skill. Return:

```markdown
## Grill summary
Outcome:
Scope and non-goals:
Decisions accepted:
Expert recommendations accepted or delegated:
Assumptions:
Evidence still needed:
Deferred branches:
Revisit triggers:
Qualified review required:
Shared understanding: confirmed | awaiting-confirmation
Recommended next C2O stage:
```

Move to C2O Spec only after confirmation. Move to C2O Slice first when an experiment or prototype is needed.
