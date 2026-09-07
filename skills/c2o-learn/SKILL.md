---
name: c2o-learn
description: Distill evidence, feedback, and completed work into scoped lessons that change future decisions or execution. Use after meaningful learning or when closing a work loop. Preserve provenance and applicability; avoid transcripts, transient details, unsupported preferences, and automatic changes to shared skills.
---

# C2O Learn

Keep learning only when it will change a future action under identifiable conditions.

## Distill

1. Compare expected and observed results, including what remains untested.
2. Identify assumptions confirmed, weakened, or disproved. Separate observation, feedback, and inference.
3. For each material lesson, record the evidence, applicable project/task/domain, future action it changes, and a revisit or invalidation trigger.
4. Retain consequential decisions and costly constraints, not every rejected possibility. Keep task-local facts local; promote only durable evidence.
5. Mark stale statements superseded and invalidate evidence affected by changed artifacts or assumptions. Do not erase the rationale of consequential decisions.
6. Do not infer a global user preference from one selection or a universal rule from one successful task. Confirm broader application when material.
7. Turn recurring, evidenced failures into proposed regression scenarios after removing secrets and unrelated personal data. Do not automatically modify shared skills, global policy, or other projects from local feedback.

For request-validation lessons, use [expertise-discovery.md](../c2o-work/references/expertise-discovery.md): retain which premise was tested, whether it came from the user or agent, what evidence changed it, and which revisions were accepted or delegated. Do not turn an uncertain correction into a fact or one expertise gap into a global judgment about the user. Preserve intentional constraints and record when a lesson should no longer apply.

## Update minimally

When `.context/` exists, use the smallest relevant set:

- `decisions.md`: accepted choices, evidence, applicability, and revisit triggers;
- `assumptions.md`: confidence and validation changes;
- `current-goal.md`: scope changes or remaining commitment for this task;
- `acceptance.md`: changed evidence and invalidated checks;
- `progress.md`: verified completion, blockers, and the next useful action;
- `open-questions.md`: only questions that can change future work.

Use [context-schema.md](../c2o-work/references/context-schema.md) for persistent work. Do not overwrite another task's goal, duplicate source artifacts, or store command logs and full conversations. No material learning is a valid result; do not manufacture a lesson to fill a template.

## Output

```markdown
## Learning captured
Observation and evidence:
Confirmed, changed, or disproved:
Applies when:
Future action changed:
Revisit or invalidate when:
Context updated and stale evidence marked:
Remaining uncertainty:
```
