---
name: c2o-spec
description: Convert a shaped outcome and resolved decisions into a concise action-ready contract with required deliverables, completion level, quality criteria, failure states, constraints, and verification. Use for multi-step delivery, handoff, or work across sessions. Do not inflate a simple task into a full requirements document.
---

# C2O Spec

Write the smallest specification that prevents expensive misunderstanding without reducing what the user asked for.

## Readiness

Proceed when the actor, trigger, outcome, key constraints, and at least one acceptance signal are clear. Shape only missing parts. Resolve consequential choices; do not hide them in implementation defaults.

Use [expertise-discovery.md](../c2o-work/references/expertise-discovery.md) if a clear request rests on an untested consequential premise or omits professional decisions needed for its quality target. Preserve the original statement and distinguish its source, kind, evidence, and authority before promoting it into a requirement. Record accepted revisions and their reasons; an unresolved method remains a proposal or open decision, not a silently settled constraint. A necessary implication needs an outcome link, omission consequence, and proportionate treatment. Do not respecify settled work without new evidence.

## Write the contract

1. State the outcome and primary scenario as trigger, action, observable result.
2. Enumerate all explicitly requested deliverables, variants, formats, and flows. For larger work assign stable IDs so coverage can be checked.
3. Classify requirements as explicit, necessary implication, specialist choice, or optional enhancement using [outcome-contract.md](../c2o-work/references/outcome-contract.md). Record the source or rationale of material criteria.
4. Establish the completion level: experiment, internal-use, usable product, or release candidate. An inferred level is provisional, not permission to lower an explicit quality target.
5. Separate objective constraints, reviewable quality judgments, and real-world effects that require later observation. Translate words such as premium or intuitive into relevant reference attributes and observable review criteria, not invented scores.
6. Apply only relevant domain, interface, brand, accessibility, compatibility, privacy, or operational constraints. Use [quality-profiles.md](../c2o-work/references/quality-profiles.md) as a starting point, not universal requirements.
7. Include material empty, error, permission, interruption, and recovery states.
8. Map every required deliverable and requirement to acceptance, method, evidence expected, and reviewer when needed. Keep artifact acceptance separate from later business impact.
9. Declare non-goals, optional ideas, invalidating assumptions, action boundaries, and decisions still needed.

Do not invent personas, metrics, accounts, backends, analytics, roles, architecture, or rollout mechanisms without evidence of need. Necessary safeguards that alter cost, risk, or authority require an explicit decision. Acceptance must not be weakened after execution to make a result pass.

## Output

```markdown
# Mini-spec: <name>
## Context and outcome
## Required deliverables and primary scenario
## Completion level and quality references
## Requirements, origin, and constraints
## Failure and edge states
## Acceptance criteria and verification methods
## Authorization and user-owned decisions
## Non-goals and optional enhancements
## Assumptions and open questions
```

Use Given/When/Then, concrete examples, or observations. Keep a small contract in the conversation; persist only when handoff or future work benefits.
