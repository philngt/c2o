# C2O Context Schema

## Contents

1. Context principles
2. File contracts
3. Read routing
4. Update rules

## Context principles

- Store decisions and evidence, not conversation transcripts.
- Keep source-of-truth facts in their native artifacts or systems; do not duplicate content, code, or configuration.
- Record uncertainty explicitly.
- Prefer one durable sentence over a chronological diary.
- Date entries when their validity may decay.

## File contracts

### `project.md`

Store the project, organization, product, or system purpose; users or actors; enduring constraints; working principles; and long-term non-goals. Change rarely.

### `current-goal.md`

Store one active outcome, actor and situation, scope, acceptance criteria, intervention level, and current gate.

### `decisions.md`

Use one entry per consequential choice:

```markdown
## YYYY-MM-DD — Decision title
- Status: proposed | accepted | superseded
- Context:
- Decision:
- Reason:
- Alternatives rejected:
- Accepted trade-off:
- Revisit when:
- Evidence:
```

### `assumptions.md`

Use a compact table:

```markdown
| Assumption | Confidence | Impact if false | Validation | Status |
|---|---|---|---|---|
```

Confidence is `low`, `medium`, or `high`; status is `open`, `confirmed`, or `disproved`.

### `open-questions.md`

Record only questions that can change scope, design, operations, architecture, user outcome, or next action. Include owner or evidence needed when known.

### `acceptance.md`

Store criterion, verification method, current status, and evidence. Treat `not-tested` as distinct from failure.

### `progress.md`

Store verified completed work, current action, blockers, and one next meaningful step. Avoid a detailed command log.

## Read routing

| Gate | Read first |
|---|---|
| Shape | `project.md`, `current-goal.md` |
| Inquire | `current-goal.md`, `decisions.md`, `assumptions.md`, `open-questions.md` |
| Decide | `current-goal.md`, `decisions.md`, `assumptions.md` |
| Spec or slice | `current-goal.md`, `decisions.md`, `acceptance.md` |
| Create, deliver, or execute | `current-goal.md`, `acceptance.md`, relevant decisions |
| Verify | `acceptance.md`, `current-goal.md` |
| Learn | all files that may receive a material update |

Do not read every file by default.

## Update rules

1. Update context after evidence or a user decision, not after every conversational turn.
2. Preserve explicit user constraints over inferred defaults.
3. Mark superseded decisions instead of silently erasing their rationale.
4. Replace stale progress rather than appending indefinitely.
5. Remove resolved open questions.
6. Link or name evidence without copying large outputs.
7. Keep files comprehensible to a fresh session in under two minutes.
