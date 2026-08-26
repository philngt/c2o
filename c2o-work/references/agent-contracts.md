# C2O Agent Contracts

## Contents

1. Delegation rule
2. Explorer
3. Critic
4. Verifier
5. Synthesis

## Delegation rule

Use a subagent only when its task is bounded, independently checkable, and can proceed without owning the final scope. Keep simple sequential stages in the main thread. Do not simulate a company hierarchy.

## Explorer

Purpose: gather direct evidence before a decision or change.

Constraints:

- remain read-only;
- trace real code, data, documents, or runtime paths;
- distinguish observation from inference;
- do not propose a broad redesign unless asked.

Return:

```yaml
findings: []
evidence: []
constraints: []
unknowns: []
```

## Critic

Purpose: independently challenge a proposal at intervention level 4 or 5, or when reversal is costly.

Constraints:

- evaluate against the stated outcome and acceptance criteria;
- search for hidden assumptions, failure paths, and unnecessary complexity;
- do not invent generic risks unrelated to the actual system;
- recommend the smallest material correction.

Return:

```yaml
blocking_issues: []
important_risks: []
unsupported_assumptions: []
unnecessary_complexity: []
recommended_changes: []
```

## Verifier

Purpose: produce evidence independent of the implementation narrative.

Constraints:

- do not modify the result during review-only work;
- map evidence to each acceptance criterion;
- label unrun checks and inference honestly;
- include negative or recovery cases only when relevant.

Return:

```yaml
status: pass | partial | fail | insufficient-evidence
criteria: []
evidence: []
remaining_gaps: []
```

## Synthesis

The orchestrator must resolve contradictory findings by inspecting evidence, not by majority vote. It owns:

- the final recommendation;
- scope changes;
- user questions;
- acceptance status;
- durable context updates.

