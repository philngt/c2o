---
name: c2o-verify
description: Verify an implementation, artifact, plan, or claimed result against explicit acceptance criteria using direct evidence, tests, inspection, or reproducible checks. Use before declaring work complete, during independent review, or when a plausible result may hide regressions or unsupported assumptions. Do not silently repair failures unless the user also asked for a fix.
---

# C2O Verify

Judge the result against the contract, not against effort or plausibility.

## Verify

1. Recover the intended outcome, scope, and acceptance criteria. If criteria are absent, derive a minimal review contract and label it as inferred.
   For creative work, separate objective constraints, judgment criteria, and real-world effects that are not yet observable.
2. Choose the strongest safe evidence available for each criterion:
   - automated test;
   - static or structural inspection;
   - rendered or interactive inspection;
   - source reconciliation or calculation check;
   - operational observation or stakeholder review;
   - reproducible manual check;
   - reasoned inference only as a last resort.
3. Run independent checks where practical. Include negative, permission, empty, interrupted, compatibility, and recovery cases only when relevant.
4. Record evidence exactly. Separate observed facts from inference.
5. Assign each criterion `pass`, `partial`, `fail`, or `not-tested`.
6. Rank gaps by their impact on the requested outcome.

Do not fix defects during a review-only request. A successful build is not proof of correct behavior; a polished artifact is not proof of real-world effect; a screenshot is not proof of hidden state; reasoning is not proof that a check passed.

## Output

```markdown
## Verification
| Criterion | Status | Evidence |
|---|---|---|

Overall: pass | partial | fail | insufficient-evidence
Blocking gaps:
Non-blocking risks:
Checks not run:
Recommended next action:
```
