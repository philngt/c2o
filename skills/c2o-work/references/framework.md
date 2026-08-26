# C2O Framework Reference

## Contents

1. Intervention levels
2. Work-state gates
3. Information classes
4. Stage contracts
5. Delegation packet
6. Completion contract

## Intervention levels

Choose the lowest level that still controls likely cost or risk.

| Level | Use when | Maximum ceremony |
|---:|---|---|
| 0 | Clear question or tiny edit | Direct answer or action |
| 1 | Several easy-to-miss checks | Short checklist |
| 2 | Meaningful choice among options | Decision note, up to three options |
| 3 | Handoff or multi-step implementation | Mini-spec and acceptance criteria |
| 4 | Cross-component work or costly rollback | Spec, vertical slice, verification plan |
| 5 | High-stakes or effectively irreversible work | Independent evidence, risk review, rollout and recovery plan |

Lower the level when the change is small, reversible, familiar, and locally testable. Raise it when ambiguity, blast radius, cost of reversal, novelty, or safety risk increases.

## Work-state gates

| State | Exit condition |
|---|---|
| `CAPTURED` | The request and task class are understood |
| `SHAPED` | Actor, situation, outcome, boundary, and success signal are clear |
| `DECIDED` | Blocking alternatives are resolved or a reversible default is accepted |
| `SPECIFIED` | Behavior, constraints, failure states, acceptance, and non-goals are explicit |
| `READY` | A coherent vertical slice can be executed safely |
| `EXECUTING` | The approved slice is implemented without uncontrolled expansion |
| `VERIFYING` | Each material criterion has evidence or is marked untested |
| `DONE` | The requested outcome is accepted and durable learning is captured |

Skip gates when their exit condition is already satisfied. Never force an answer-only request through execution.

## Information classes

- **Known:** Explicit user input or direct evidence.
- **Safely inferable:** A reversible default with low downside. State it when it affects the outcome.
- **Requires decision:** Alternatives lead to materially different user outcomes, costs, or irreversible paths.
- **Verify later:** Information cheaper to learn from a prototype, test, or observation than from discussion.

## Stage contracts

### Shape

Input: rough intent.

Output: actor, triggering situation, current difficulty, observable outcome, constraints, scope, non-goals, acceptance signals, assumptions, and readiness.

### Decide

Input: one blocking choice.

Output: criteria, up to three viable options, evidence and assumptions, recommendation, accepted trade-off, and revisit trigger.

### Spec

Input: shaped outcome and resolved blocking decisions.

Output: primary scenario, requirements, constraints, failure states, acceptance criteria, non-goals, assumptions, and verification approach.

### Slice

Input: specification too large for one safe pass.

Output: trigger-to-result path, explicit exclusions, risk learned, acceptance, and demonstration method.

### Execute

Input: approved slice.

Output: the smallest coherent change plus actual checks.

### Verify

Input: result and acceptance contract.

Output: criterion-by-criterion evidence with `pass`, `partial`, `fail`, or `not-tested`.

### Learn

Input: expected outcome, observed result, feedback, and verification.

Output: updated durable context without conversation noise.

## Delegation packet

Delegate only a bounded task with this contract:

```yaml
task:
  type: investigate | critique | verify
  question: "One answerable question"
scope:
  include: []
  exclude: []
context:
  facts: []
deliverable:
  - required output
done_when:
  - observable condition
constraints:
  - read-only or permitted mutations
```

The orchestrator retains scope, resolves conflicts, and synthesizes the result. Do not delegate the final decision merely to create distance from responsibility.

## Completion contract

A task is complete only when:

1. the requested observable outcome exists;
2. the work remains within agreed scope;
3. relevant acceptance criteria have evidence;
4. untested areas are explicit;
5. material decisions and changed assumptions are retained;
6. no unsafe or destructive follow-up is implied as already authorized.
