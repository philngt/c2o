---
name: c2o-decide
description: Frame and resolve a consequential choice by comparing viable options against explicit criteria, reversibility, evidence, cost, and risk, then record the recommendation and assumptions. Use for architecture, product, creative direction, workflow, tooling, prioritization, or implementation decisions where trade-offs matter. Avoid when there is only one viable option or a trivial reversible default.
---

# C2O Decide

Produce a decision, not an unranked catalogue of possibilities.

## Decide

1. Express the decision as one mutually exclusive question.
2. State why it must be decided now and what can remain deferred.
3. Classify reversibility:
   - easy to reverse;
   - costly to reverse;
   - effectively irreversible.
4. Select three to five criteria tied to the outcome. Weight only when priorities genuinely differ.
5. Compare no more than three viable options. Include `do nothing` when it is credible.
6. Distinguish evidence, inference, and assumption.
7. Recommend one option. Prefer the cheapest reversible experiment when uncertainty dominates.
8. State what evidence would cause the decision to be revisited.

Avoid false numerical precision. Do not let a scoring table override a dominant constraint.

## Output

```markdown
## Decision
Question:
Why now:
Reversibility:

| Criterion | Option A | Option B | Option C |
|---|---|---|---|

Recommendation:
Reason:
Accepted trade-off:
Assumptions:
Revisit trigger:
Next action:
```
