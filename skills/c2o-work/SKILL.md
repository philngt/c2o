---
name: c2o-work
description: Orchestrate a Context-to-Outcome work loop that turns a rough request or poorly described problem into the smallest verified result. Use when knowledge, creative, or software work is ambiguous, the user says something feels wrong or does not know where to start, several stages need coordination, or the user wants expert guidance without knowing how to specify the work completely. Avoid for simple questions or one-step actions that can be answered or completed directly.
---

# C2O Work

Own the outcome from intake through evidence. Scale the process to the task; do not manufacture project-management ceremony.

## Start

1. Classify the request provisionally as `answer`, `investigate`, `decide`, `change`, or `review`. Keep it provisional when the initial signal is too weak to distinguish the path.
2. Default to plain-language guidance. Ask about experience only when it changes safety, viable options, or the useful explanation depth.
3. State the observable outcome in one sentence when possible. Otherwise preserve the initial signal without inventing an outcome and use guided problem discovery.
4. Separate information into:
   - known;
   - safely inferable or advisor-recommended;
   - requires the user's values or authority;
   - requires qualified human review;
   - can be verified after a prototype, creation, delivery, or implementation.
5. Select the lowest sufficient intervention level from [framework.md](references/framework.md).
6. Continue without questions when a reversible default is safe. Ask only questions that change the next action and belong to the user; offer at most three mutually exclusive choices, explain their practical consequences, and recommend one only when the user's stated priorities support it.

The user owns outcomes, values, priorities, taste, constraints, acceptable risk, commitments, and approval. C2O owns fact-finding, plain-language explanation, and evidence-backed recommendations about specialist means. Do not ask an inexperienced user to choose a method, tool, architecture, or technique they cannot evaluate; recommend one, explain its practical consequence and confidence, then request acceptance only when needed. Preserve qualified review for consequential regulated or licensed judgments.

When the request asks what should be created or changed, do not jump from a broad desire to one domain solution. First shape the desired change, then compare up to three materially different hypotheses. A recommended hypothesis remains an experiment until evidence supports it.

## Discover an unclear problem first

When the user says they cannot describe the problem, do not know where to start, or only reports that something feels wrong:

1. Apply `c2o-shape` in guided problem-discovery mode.
2. Ask one observable, plain-language question at a time. Do not ask for a root cause, solution, domain label, tool, method, or architecture.
3. Anchor on one representative case and inspect available evidence yourself before requesting more description.
4. Separate observed or reported facts from inference, hypothesis, and unknown.
5. Return a compact problem direction and recommend the next route:
   - `investigate` when evidence can reveal why the observed result occurs;
   - `decide` when one user-owned trade-off blocks progress;
   - `change` only when the desired result and authorization are clear;
   - `review` when an existing result must be judged against a contract.

Do not begin implementation merely because one plausible solution appears during discovery.

## Enter deep inquiry only when needed

Insert the optional `INQUIRING` gate when the user explicitly asks to be grilled or when intervention level 4–5 contains several consequential decisions with dependencies. Apply the sibling `c2o-grill` skill when available, using the host's normal invocation (`$c2o:c2o-grill` in Codex or `/c2o:c2o-grill` in Claude Code and Antigravity CLI).

Do not grill merely because a request is vague or the user wants plain-language advice. Stay in the normal flow when shaping, one decision, a safe reversible default, or a prototype can resolve the uncertainty more cheaply; apply the same expert-guidance rules without creating an inquiry stage.

If a sibling skill cannot be loaded, preserve the minimum protocol:

1. Map fact, decision, and experiment nodes with prerequisites.
2. Classify decisions as user-owned, advisor-led, or requiring qualified review.
3. Research facts instead of asking the user.
4. Recommend advisor-led choices with evidence, trade-off, confidence, and a revisit trigger.
5. Ask only the currently unblocked user-owned decisions; explain their practical consequences plainly.
6. Route questions that talking cannot settle to a prototype or vertical slice.
7. Recompute dependent decisions after every answer.
8. Require the user to confirm shared understanding before specification, creation, delivery, or implementation.

## Run the loop

Move only as far as the task requires:

`CAPTURED -> SHAPED -> [INQUIRING] -> DECIDED -> SPECIFIED -> READY -> EXECUTING -> VERIFYING -> DONE`

- Skip gates for small, clear, reversible work.
- Treat `INQUIRING` as optional. Never use it to manufacture questions or delay a cheap experiment.
- Stop at the requested boundary for answer, planning, diagnosis, or review requests. Do not create, apply, publish, send, or implement beyond what the user requested.
- For an authorized change, define acceptance before acting. Route creative direction, concept exploration, and creative production through `c2o-create`; route source-code and system implementation through `c2o-execute`; route other non-software artifacts and operational delivery through `c2o-deliver`; then gather evidence.
- When a creative artifact also needs packaging, publishing, or another operational action, complete the creative loop first and then use `c2o-deliver` under its explicit action boundary.
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

Add `--agents` only in Codex when the user wants project-scoped custom agent templates. Claude Code and Antigravity should use their native subagent support instead. The script creates missing files and never overwrites existing ones.

## Finish

Return a compact handoff containing:

- outcome reached;
- evidence or artifact produced;
- decisions and assumptions that materially affected it;
- any qualified review still required;
- unresolved risk, if any;
- the next meaningful step only when one exists.

Do not claim completion when acceptance criteria are untested. Say `not verified` where evidence is unavailable.
