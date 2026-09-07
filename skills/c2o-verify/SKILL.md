---
name: c2o-verify
description: Verify an artifact, implementation, plan, or claimed result against the original requirements and intended use with direct evidence. Use before verified completion or for independent review. Distinguish compliance, outcome fit, and unobserved effects. Do not repair during review-only work.
---

# C2O Verify

Judge the result against the user's contract and actual evidence, not effort or the creator's narrative.

## Recover the contract independently

Read the original request, accepted decisions, required deliverables, completion level, and acceptance criteria alongside the actual artifact. Do not rely only on the executor's summary. If criteria are missing, derive a conservative minimum and label them inferred; do not erase explicit requirements or choose easier tests after seeing the result.

Use [outcome-contract.md](../c2o-work/references/outcome-contract.md) for criterion origin, status aggregation, and evidence validity. For creative work separate objective checks, quality judgments, and effects requiring later observation.

## Check two layers

- Compliance: all requested deliverables, constraints, behaviors, and quality commitments are covered; relevant regressions and failure states are checked.
- Outcome fit: exercise a representative intended-use scenario. An artifact may meet a narrow spec yet fail the user's goal. Report that gap and recommend a decision or experiment; do not silently rewrite scope.

An agent walkthrough is not a real user study. A polished artifact is not proof of business impact. Keep unobserved effects explicitly unmeasured.

## Gather and assess evidence

1. Choose the strongest appropriate safe method per criterion: direct tests, calculations/source reconciliation, structural inspection, rendered/interactive checks, reproducible walkthrough, operational observation, or required human review. Use inference only as a labeled last resort.
2. Inspect the actual artifact or environment. Include negative, permission, empty, interrupted, compatibility, and recovery cases when relevant. Start narrow and broaden based on risk.
3. Record criterion origin, method, artifact/revision or observed state, result, evidence location, and reviewer when applicable. Tie evidence to the version actually checked; invalidate affected checks after material changes.
4. Label each criterion `pass`, `partial`, `fail`, or `not-tested`. Missing tools, unavailable credentials, stale evidence, and pending mandatory human review are not passing evidence.
5. Rank gaps by effect on the requested outcome. A required failure makes the result fail; missing required evidence prevents an overall pass. Do not hide a blocker inside an average score.

Read-only review must not repair source artifacts or change the subject's state. Tests that write caches or build outputs need an authorized disposable workspace. If unavailable, report them not tested instead of weakening the sandbox or using live credentials.

## Output

```markdown
## Verification
| Criterion / origin | Required? | Status | Method / artifact revision / evidence |
|---|---|---|---|

Compliance: pass | partial | fail | insufficient-evidence
Outcome fit: pass | partial | fail | insufficient-evidence | not-applicable
Overall artifact verdict: pass | partial | fail | insufficient-evidence
Real-world effects: observed evidence | unmeasured | not-applicable
Review task: completed | blocked
Blocking gaps:
Non-blocking risks:
Checks not run or invalidated:
Recommended next action:
```

Use not-applicable only with a reason tied to the requested boundary, never to hide an untested required criterion. A completed review may legitimately report a failed artifact. During authorized production, hand defects back to the executor for bounded repair and then reverify; during review-only work, report without repairing.
