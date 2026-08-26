---
name: c2o-work
description: Orchestrate a Context-to-Outcome work loop that turns a rough request into the smallest verified result. Use when a task is ambiguous, spans several stages, needs coordination across discovery, decisions, implementation, and verification, or when the user asks to manage work without already knowing how to write a complete specification. Avoid for simple questions or one-step edits that can be answered or completed directly.
---

# C2O Work

Own the outcome from intake through evidence. Scale the process to the task; do not manufacture project-management ceremony.

## Start

1. Classify the request as `answer`, `investigate`, `decide`, `change`, or `review`.
2. State the observable outcome in one sentence.
3. Separate information into:
   - known;
   - safely inferable;
   - requires a user decision;
   - can be verified after a prototype or implementation.
4. Select the lowest sufficient intervention level from [framework.md](references/framework.md).
5. Continue without questions when a reversible default is safe. Ask only questions that change the next action; offer at most three mutually exclusive choices and recommend one.

When the request asks what should be built, do not jump from a broad desire to one domain solution. First shape the desired change, then compare up to three materially different hypotheses. A recommended hypothesis remains an experiment until evidence supports it.

## Run the loop

Move only as far as the task requires:

`CAPTURED -> SHAPED -> DECIDED -> SPECIFIED -> READY -> EXECUTING -> VERIFYING -> DONE`

- Skip gates for small, clear, reversible work.
- Stop at the requested artifact for answer, planning, diagnosis, or review requests. Do not implement unless the user asked for a change.
- For a change, define acceptance before editing, implement one coherent slice, then gather evidence.
- Keep the main thread responsible for scope and synthesis. Delegate only bounded, independent investigations or checks using [agent-contracts.md](references/agent-contracts.md).
- Treat a plausible explanation as a hypothesis until evidence supports it.
- Do not invent numeric success thresholds without a baseline, business constraint, or explicit user target. Define the measurement method first and mark any proposed threshold as provisional.
- Never expand scope merely because a professional workflow often contains another phase, role, document, abstraction, or feature.

## Maintain context

If `.context/` exists, read only the files relevant to the current gate using [context-schema.md](references/context-schema.md). Update only material changes.

For a long-lived project with no context files, initialize them only when persistence will help future work. Announce the initialization, then run:

```bash
python3 <skill-dir>/scripts/init_c2o.py <project-root>
```

Add `--agents` only when the user wants project-scoped custom agent templates. The script creates missing files and never overwrites existing ones.

## Finish

Return a compact handoff containing:

- outcome reached;
- evidence or artifact produced;
- decisions and assumptions that materially affected it;
- unresolved risk, if any;
- the next meaningful step only when one exists.

Do not claim completion when acceptance criteria are untested. Say `not verified` where evidence is unavailable.
