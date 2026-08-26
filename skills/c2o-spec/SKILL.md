---
name: c2o-spec
description: Convert a shaped outcome and resolved decisions into a concise, action-ready mini-spec with scope, requirements or deliverables, failure states, constraints, acceptance criteria, and non-goals. Use when software or knowledge work must be handed to another person or agent, executed across several steps, or preserved across sessions. Do not inflate a simple task into a full requirements document.
---

# C2O Spec

Write the smallest specification that prevents expensive misunderstanding in delivery or implementation.

## Readiness gate

Proceed when the actor, triggering situation, outcome, key constraint, and at least one acceptance signal are clear. Otherwise shape only the missing parts before continuing.

## Write the mini-spec

1. State context and outcome.
2. Describe the primary scenario as trigger, action, and observable result.
3. Define in-scope behavior in priority order.
4. Record data, interface, compatibility, privacy, operational, or technical constraints only when applicable.
5. Describe important empty, error, permission-denied, interrupted, and recovery states.
6. Map every requirement to an acceptance criterion.
7. Declare non-goals and deferred decisions.
8. Note assumptions whose failure would invalidate the spec.

Do not invent personas, metrics, features, processes, roles, architecture, analytics, accounts, backends, or rollout mechanisms without evidence that they are needed.

## Output

```markdown
# Mini-spec: <name>

## Context and outcome
## Primary scenario
## Scope
## Requirements or deliverables
## Constraints
## Failure and edge states
## Acceptance criteria
## Non-goals
## Assumptions and open questions
## Verification approach
```

Use testable language: `Given / When / Then`, examples, or explicit observations. Replace adjectives such as “fast” and “intuitive” with measurable or reviewable evidence.
