---
name: c2o-shape
description: Turn a vague idea, complaint, weak signal, poorly described problem, creative intention, feature request, or desired result into a shaped brief or problem direction with observable evidence, outcome, scope, constraints, assumptions, acceptance signals, and non-goals. Use when the user knows broadly what they want, says something feels wrong, cannot describe the problem, or does not know where to start. Do not use when the request is already clear enough for direct action.
---

# C2O Shape

Convert intent or an unclear signal into a decision-ready problem without demanding a diagnosis or prematurely designing the solution.

## Discover a poorly described problem

When the user cannot explain the problem, start from what they can observe:

1. Ask for the concrete signal that made them notice something was wrong.
2. Ask one plain-language question at a time about the triggering situation, actual result, affected actor, practical impact, recurrence, and a representative example. Skip fields that cannot change the next step.
3. Ask what improvement would be observable. If the user cannot state it abstractly, ask what they would expect to happen in the example instead.
4. Request the smallest useful artifact only when needed: screenshot, message, sample, document, log, recording, metric, or reproducible case. Ask the user to omit secrets and unrelated personal or confidential data.
5. Inspect accessible files, tools, records, or artifacts yourself. Do not ask the user for facts the environment can establish.
6. Separate direct observation, user report, inference, working hypothesis, and unknown. Never rewrite a hypothesis as the problem statement.
7. Recommend the next investigation or C2O stage; do not prescribe a solution before the direction is supported.

Do not ask the user for a root cause, domain classification, preferred method, tool, architecture, or solution. When they answer “I do not know,” offer concrete examples, anchor on one real case, or inspect evidence instead of repeating the abstract question. Stop discovery when the next useful action is clear, not when every uncertainty is resolved.

## Shape

1. Identify the actor and triggering situation.
2. Describe the current difficulty without embedding a preferred solution.
3. State the desired observable change.
4. Extract explicit constraints and preserve the user's wording where precision matters.
5. Separate known facts, safe working assumptions, user decisions, and facts that can wait for later verification.
6. Define the smallest useful boundary and explicit non-goals.
7. Write acceptance signals that can be observed, tested, or reviewed.

Do not ask for information that cannot change the next step. When a missing decision blocks progress, present at most three choices, their consequences, and one recommended default.

## Output

```markdown
## Shaped brief
Actor and situation:
Current difficulty:
Outcome:
Constraints:
In scope:
Non-goals:
Acceptance signals:
Working assumptions:
Decision required now:
Can wait until verification:
Readiness: ready | needs-decision | needs-evidence
```

Keep the brief proportional to the request. A small change may need only five lines.

For guided problem discovery, return this instead:

```markdown
## Problem direction
Initial signal:
Representative example:
Actor and triggering situation:
Actual result:
Desired observable change:
Practical impact:
Direct evidence:
Known facts:
Working hypotheses, not findings:
Unknowns that matter now:
Recommended next investigation or C2O stage:
Readiness: direction-clear | needs-example | needs-evidence | needs-user-decision
```
