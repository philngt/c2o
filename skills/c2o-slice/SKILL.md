---
name: c2o-slice
description: Reduce a large initiative, project, feature, or specification to the smallest end-to-end slice that delivers observable value and tests the riskiest useful assumption. Use when planned software or knowledge work crosses several layers or workstreams and feels too large to deliver and verify safely in one pass. Avoid horizontal slices that complete only one document, function, or technical layer without a usable result.
---

# C2O Slice

Find a thin, complete path through the system rather than a broad unfinished layer.

## Slice

1. Identify the triggering event and the final observable result.
2. Trace the minimum path connecting them.
3. Identify the assumption most worth learning now.
4. Remove variants, extra formats or channels, optimization, automation, configuration, migration, polish, and generalized abstractions unless required for the path to work.
5. Preserve enough error handling and safety for the slice to be usable.
6. Define how the slice will be demonstrated or tested.
7. Confirm that completing it changes knowledge or value, not merely output volume.

Prefer one real case over a framework for all future cases. Prefer one supported path over several partially supported paths.

## Output

```markdown
## Vertical slice
Trigger:
End result:
Minimum path:
Included behavior:
Explicit exclusions:
Risk or assumption tested:
Acceptance criteria:
Demo or verification:
What becomes possible next:
```

Reject a proposed slice when it cannot be exercised end to end, has no observable result, or still contains multiple independently valuable outcomes.
