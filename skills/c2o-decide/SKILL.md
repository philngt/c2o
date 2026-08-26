---
name: c2o-decide
description: Frame and resolve a consequential choice by comparing viable options against explicit criteria, reversibility, evidence, cost, and risk, then record the recommendation and assumptions. Use for architecture, product, creative direction, workflow, tooling, prioritization, or implementation decisions where trade-offs matter, including when an inexperienced user needs a plain-language expert recommendation among viable choices. Avoid when there is only one viable option or a trivial reversible default.
---

# C2O Decide

Produce a decision, not an unranked catalogue of possibilities.

## Decide

1. Express the decision as one mutually exclusive question.
2. Classify it as user-owned, advisor-led, or requiring qualified review.
3. Explain the decision and its practical consequence in language the user can evaluate.
4. State why it must be decided now and what can remain deferred.
5. Classify reversibility:
   - easy to reverse;
   - costly to reverse;
   - effectively irreversible.
6. Select three to five criteria tied to the outcome. Weight only when priorities genuinely differ.
7. Compare no more than three viable options. Include `do nothing` when it is credible.
8. Distinguish evidence, inference, and assumption.
9. Recommend one option with a confidence level. Prefer the cheapest reversible experiment when uncertainty dominates.
10. State what evidence would cause the decision to be revisited.

For an advisor-led choice, investigate and recommend the specialist means instead of asking the user to select unfamiliar jargon. For a user-owned choice, explain consequences and ground the recommendation in the user's stated values rather than substituting the advisor's preferences. Make any required qualified review explicit.

Avoid false numerical precision. Do not let a scoring table override a dominant constraint.

## Output

```markdown
## Decision
Question:
Decision owner: user | advisor-led | qualified-review
Why now:
Reversibility:

| Criterion | Option A | Option B | Option C |
|---|---|---|---|

Recommendation:
Reason:
Confidence: low | medium | high
Accepted trade-off:
Assumptions:
Revisit trigger:
Next action:
```
