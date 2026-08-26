# C2O Framework Reference

## Contents

1. Intervention levels
2. Work-state gates
3. Decision ownership
4. Information classes
5. Stage contracts
6. Delegation packet
7. Completion contract

## Intervention levels

Choose the lowest level that still controls likely cost or risk.

| Level | Use when | Maximum ceremony |
|---:|---|---|
| 0 | Clear question or tiny edit | Direct answer or action |
| 1 | Several easy-to-miss checks | Short checklist |
| 2 | Meaningful choice among options | Decision note, up to three options |
| 3 | Handoff or multi-step creation or delivery | Mini-spec or creative contract and acceptance criteria |
| 4 | Cross-component or cross-workstream change with costly rollback | Spec, end-to-end slice, verification plan |
| 5 | High-stakes or effectively irreversible work | Independent evidence, risk review, rollout and recovery plan |

Lower the level when the change is small, reversible, familiar, and locally testable. Raise it when ambiguity, blast radius, cost of reversal, novelty, or safety risk increases.

## Work-state gates

| State | Exit condition |
|---|---|
| `CAPTURED` | The request and task class are understood |
| `SHAPED` | Actor, situation, outcome, boundary, and success signal are clear |
| `INQUIRING` | Dependent material decisions are exposed, evidence gaps are explicit, and the user confirms shared understanding |
| `DECIDED` | Blocking alternatives are resolved or a reversible default is accepted |
| `SPECIFIED` | Behavior, constraints, failure states, acceptance, and non-goals are explicit |
| `READY` | A coherent vertical slice can be executed safely |
| `EXECUTING` | The approved slice is created, delivered, or implemented without uncontrolled expansion |
| `VERIFYING` | Each material criterion has evidence or is marked untested |
| `DONE` | The requested outcome is accepted and durable learning is captured |

Skip gates when their exit condition is already satisfied. Never force an answer-only request through execution.

## Decision ownership

| Owner | C2O behavior | Examples |
|---|---|---|
| User | Explain consequences and obtain the user's judgment or authority | Outcome, values, priorities, taste, budget, risk tolerance, commitments, approval |
| Advisor-led | Research and recommend one specialist choice; apply only within existing authorization | Method, tool, technique, architecture, implementation detail, reversible professional default |
| Qualified reviewer | Prepare evidence and options but keep expert approval explicit | Consequential legal, medical, financial, safety, regulatory, or licensed judgment |

Default to plain language. Do not transfer a specialist choice to the user merely because several technical options exist. A recommendation becomes a decision only when the user accepts it, delegates that reversible class of choice, or already authorized the applicable execution boundary.

## Information classes

- **Known:** Explicit user input or direct evidence.
- **Safely inferable or advisor-recommended:** A supported professional choice or reversible default. State its consequence and confidence when material.
- **Requires user decision:** Alternatives depend on the user's values, authority, commitments, or acceptable risk.
- **Requires qualified review:** A consequential regulated or licensed judgment that C2O must not present as approved.
- **Verify later:** Information cheaper to learn from a prototype, test, or observation than from discussion.

## Stage contracts

### Shape

Input: rough intent, weak signal, complaint, or poorly described problem.

Output: either a shaped brief or a problem direction containing the initial signal, representative example, actor and trigger, actual result, desired observable change, impact, direct evidence, clearly labeled hypotheses, material unknowns, recommended next investigation or stage, and readiness.

When the user cannot describe the problem, ask one observable question at a time, inspect accessible evidence directly, and never ask them to supply a root cause or preferred solution. Stop when the next useful action is clear.

### Decide

Input: one blocking choice.

Output: criteria, up to three viable options, evidence and assumptions, recommendation, accepted trade-off, and revisit trigger.

### Grill

Input: a shaped level 4–5 problem with several dependent decisions, or an explicit request to stress-test thinking.

Output: a prerequisite-aware decision tree, researched facts, plain-language expert recommendations, explicit experiments for unanswerable uncertainties, accepted choices, qualified-review boundaries, deferred branches, and user confirmation of shared understanding.

Skip this stage for simple, reversible, or independently decidable work. Do not proceed from Grill to Spec, Create, Deliver, or Execute without confirmation.

### Spec

Input: shaped outcome and resolved blocking decisions.

Output: primary scenario, requirements, constraints, failure states, acceptance criteria, non-goals, assumptions, and verification approach.

### Slice

Input: specification too large for one safe pass.

Output: trigger-to-result path, explicit exclusions, risk learned, acceptance, and demonstration method.

### Create

Input: a shaped creative brief or approved creative outcome.

Output: materially distinct directions when needed, an explicit selection, the produced creative artifact, rendered critique, and an accurate production or publication state.

### Execute

Input: approved software slice.

Output: the smallest coherent source-code or system change plus actual checks.

### Deliver

Input: approved non-software slice.

Output: a usable artifact, analysis, process, or authorized operational change plus actual checks and an explicit external-action status.

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
6. shared understanding was confirmed when the optional deep-inquiry gate was used;
7. required qualified review remains explicit and is not claimed as completed;
8. no unsafe or destructive follow-up is implied as already authorized.
