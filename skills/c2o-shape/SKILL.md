---
name: c2o-shape
description: Turn a vague idea, complaint, weak signal, creative intention, or feature request into a shaped brief with observable evidence, outcome, scope, constraints, assumptions, and acceptance signals. Use when the user cannot describe the problem or lacks the specialist knowledge to specify it. Avoid when the request is already clear enough for direct action.
---

# C2O Shape

Convert intent into a decision-ready problem without demanding a diagnosis or prematurely designing the solution.

## Discover a poorly described problem

1. Start with the concrete signal that made the user notice something was wrong.
2. Ask one plain-language question at a time about a representative case, trigger, actual result, affected actor, impact, or recurrence. Skip fields that cannot change the next step.
3. Ask what observable change they would expect in that case rather than demanding an abstract goal.
4. Request the smallest useful artifact only when needed. Ask the user to omit secrets and unrelated personal or confidential data.
5. Inspect accessible files, tools, or artifacts yourself. Do not ask for facts the environment can establish.
6. Separate direct observation, user report, inference, working hypothesis, and unknown. Never rewrite a hypothesis as a finding.
7. Recommend the next investigation or stage, not an unsupported solution.

Do not ask for a root cause, domain label, method, architecture, or preferred tool. When the user says they do not know, anchor on a real example or inspect evidence instead of repeating the abstract question. Stop when the next useful action is clear.

## Fill the expertise gap without expanding scope

Use [outcome-contract.md](../c2o-work/references/outcome-contract.md) for consequential or multi-step work. Distinguish:

- explicit requirements: preserve the user's deliverables and constraints;
- necessary implications: conditions needed for those requirements to work safely and usefully;
- specialist choices: recommend means and explain trade-offs;
- optional enhancements: keep outside committed scope unless accepted.

For example, image-load failure handling may be necessary for a usable photo viewer; accounts, comments, and an administration console are separate product choices. Do not treat domain conventions as proof a feature is required. A necessary implication that changes cost, privacy, risk, or the action boundary still needs a decision.

## Shape

Identify the actor and trigger, current difficulty without a preferred solution, desired observable change, explicit constraints, smallest useful boundary, non-goals, and acceptance signals. Separate known facts from safe assumptions and decisions. Establish the requested completion level when it changes the next step: experiment, internal-use, usable product, or release candidate. Label inferred levels as provisional.

Recommend a specialist default instead of asking the user to choose jargon. Offer at most three meaningful choices when a user-owned decision actually blocks progress.

## Output

```markdown
## Shaped brief
Actor and situation:
Current difficulty:
Outcome and required deliverables:
Constraints and completion level:
Necessary implications and rationale:
Specialist choices or decision needed:
Non-goals and optional enhancements:
Acceptance signals:
Working assumptions:
Can wait until verification:
Readiness: ready | needs-decision | needs-evidence
```

For guided discovery, return a compact problem direction instead: initial signal, representative case, actual/desired result, impact, direct evidence, facts, hypotheses explicitly not findings, material unknowns, recommended next action, and readiness. Keep small briefs to a few lines.
