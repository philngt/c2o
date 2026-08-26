---
name: c2o-learn
description: Distill completed work, feedback, failures, and verification results into durable project context by updating decisions, assumptions, current goals, and progress without preserving noisy conversation history. Use after meaningful evidence changes what future work should know or when closing a work loop. Avoid recording transient details, guesses, or information already recoverable from source code and version history.
---

# C2O Learn

Preserve only information that would materially improve a future decision or execution.

## Distill

1. Compare expected and observed results.
2. Identify which assumptions were confirmed, weakened, or disproved.
3. Record decisions only when a real alternative was considered or a costly constraint was established.
4. Promote durable facts to project context; keep task-local details in progress.
5. Remove or mark stale statements superseded by new evidence.
6. Preserve provenance: test, user decision, production observation, document, or inference.
7. State the next meaningful step only if it follows from remaining evidence or risk.

When `.context/` exists, update the smallest applicable set:

- `decisions.md` for consequential choices and revisit triggers;
- `assumptions.md` for confidence changes and validation evidence;
- `current-goal.md` for outcome or scope changes;
- `progress.md` for verified completion, blockers, and next action;
- `open-questions.md` only for questions that can change future work.

Do not duplicate code, logs, full conversations, routine commands, or temporary debugging observations.

## Output

```markdown
## Learning captured
Confirmed:
Changed:
Disproved:
Context updated:
Stale context removed:
Remaining uncertainty:
Next meaningful step:
```
