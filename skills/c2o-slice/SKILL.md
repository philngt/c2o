---
name: c2o-slice
description: Break large software, creative, or knowledge work into coherent end-to-end slices while preserving the full requested scope. Use either an experiment slice to test a hypothesis or delivery slices to complete a larger commitment. Avoid horizontal unfinished layers and never silently replace a full delivery request with an MVP.
---

# C2O Slice

Minimize the path to value, not the promised result.

## Choose the slice mode

- `experiment`: the agreed outcome is learning about a hypothesis. A bounded prototype may satisfy this task; label what it does not establish.
- `delivery`: the agreed outcome contains all requested deliverables. Slices order implementation; they do not remove scope. Completing one slice is progress, not completion of the whole commitment.

Do not downgrade delivery into an experiment without the user's agreement. Preserve required flows, languages, formats, variants, and quality targets using [outcome-contract.md](../c2o-work/references/outcome-contract.md).

## Slice

1. Identify the trigger, final result, and full set of committed deliverables.
2. Trace the minimum usable end-to-end path and the assumption worth learning now.
3. Separate work excluded from this slice from work excluded from the whole task. Defer committed work to later delivery slices, not to non-goals.
4. Remove unsupported extras and unnecessary abstractions. Do not remove requested polish, accessibility, error handling, safety, or completeness merely to make a slice smaller.
5. For repeated screens, assets, or outputs, choose a representative quality slice when useful. Prove the quality and implementation approach, then apply it to the remaining committed work.
6. Define acceptance and a demonstration that can be exercised end to end.
7. In delivery mode, record coverage: complete, in-progress, blocked, or pending for every required deliverable. Continue authorized remaining work or report the concrete blocker.

Prefer one supported path over several broken paths within a slice. Never use that preference to claim a larger unfinished request is complete.

## Output

```markdown
## Vertical slice
Mode: experiment | delivery
Full commitment:
Current slice trigger and end result:
Minimum path and included behavior:
Risk or assumption tested:
Acceptance and demonstration:
Deferred to later delivery slices:
True non-goals:
Remaining commitment and blockers:
```

Reject a slice without a usable end-to-end result. Split independently valuable outcomes into separate slices while preserving the overall commitment.
