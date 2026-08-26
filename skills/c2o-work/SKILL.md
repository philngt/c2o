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

## Enter deep inquiry only when needed

Insert the optional `INQUIRING` gate when the user explicitly asks to be grilled or when intervention level 4–5 contains several consequential decisions with dependencies. Apply the sibling `c2o-grill` skill when available, using the host's normal invocation (`$c2o:c2o-grill` in Codex or `/c2o:c2o-grill` in Claude Code).

Do not grill merely because a request is vague. Stay in the normal flow when shaping, one decision, a safe reversible default, or a prototype can resolve the uncertainty more cheaply.

If a sibling skill cannot be loaded, preserve the minimum protocol:

1. Map fact, decision, and experiment nodes with prerequisites.
2. Research facts instead of asking the user.
3. Ask only the currently unblocked, independent decisions and give a recommendation for each.
4. Route questions that talking cannot settle to a prototype or vertical slice.
5. Recompute dependent decisions after every answer.
6. Require the user to confirm shared understanding before specification or execution.

## Run the loop

Move only as far as the task requires:

`CAPTURED -> SHAPED -> [INQUIRING] -> DECIDED -> SPECIFIED -> READY -> EXECUTING -> VERIFYING -> DONE`

- Skip gates for small, clear, reversible work.
- Treat `INQUIRING` as optional. Never use it to manufacture questions or delay a cheap experiment.
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

Add `--agents` only in Codex when the user wants project-scoped custom agent templates. Claude Code should use its native subagent support instead. The script creates missing files and never overwrites existing ones.

## Finish

Return a compact handoff containing:

- outcome reached;
- evidence or artifact produced;
- decisions and assumptions that materially affected it;
- unresolved risk, if any;
- the next meaningful step only when one exists.

Do not claim completion when acceptance criteria are untested. Say `not verified` where evidence is unavailable.
