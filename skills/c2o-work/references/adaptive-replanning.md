# Adaptive Replanning

Use when evidence could materially change an ongoing approach or the next meaningful action. Keep `c2o-work` as the orchestrator. This is optional guidance, not a new skill, mandatory stage, planning engine, or permission system. Handle tiny tasks and ordinary local repairs directly.

## 1. Establish the trigger and preserve the commitment

Recover the current goal, required coverage, acceptance criteria, plan/progress, fixed methods, delegated choices, available capabilities, and remaining budget. Preserve completed work and observations before changing direction. Do not overwrite another task's plan or interrupt independent useful work merely to run this protocol.

Reconsider the approach when a material premise is contradicted, sources conflict in a decision-relevant way, repeated attempts leave the important uncertainty unresolved, a useful source or method becomes available, or the remaining resources no longer fit the plan. Distinguish measured effort/results from estimates. Time already spent alone does not prove that switching is better.

State the specific trigger and what decision it could change. Retaining the current approach is a valid result. Do not reopen settled choices without cause, evaluate the whole project after every observation, or impose a universal iteration count or invented information-gain score.

## 2. Reconstruct the current understanding from evidence

Inspect the smallest relevant source set using [domain-context.md](domain-context.md). Combine existing findings into a provisional account of the system or problem. Separate observations, reports, inferences, hypotheses, and unknowns; retain material contradictions and failed probes. Track both evidence about the subject and evidence about the effectiveness of the approach.

For decision-critical evidence, retain available source/locator, revision or observation time, actual result, and the claim or decision it affects. Link to native artifacts and records rather than copying logs into context. A source match or hash establishes identity, not whether an interpretation is supported. Repeated summaries of one source are not independent corroboration.

Distinguish these capabilities explicitly when they matter:

| Capability | What can be claimed |
|---|---|
| Original record is accessible | The saved observation can be inspected; record the version/state it describes. |
| A check can be repeated | Inputs, procedure/command, relevant tool/environment versions, and expected comparison are available; execution may still be not-run. |
| A check was repeated | Record the actual inputs/state, output, comparison, and limitations. Matching results, disagreement, and an inconclusive check are different outcomes. |

Use only existing authority to rerun checks; record unavailable capabilities or missing inputs instead of inventing them. Never reconstruct missing historical evidence from memory or generated text. A new observation of a changed system is new evidence, not recovery of the old event. Define meaningful comparison conditions before rerunning; exact output equality is not always appropriate.

## 3. Choose the next informative action

Identify the unresolved question that can change progress toward the agreed outcome. Compare up to three materially different approaches only when needed, including continuing the current method. Use `c2o-decide` for meaningful trade-offs; use `c2o-shape` if the problem premise needs reconsideration. Do not require every specialist for each update.

Prefer a bounded inspection or probe when evidence cannot yet justify switching. State which competing explanations it can distinguish, the input/source and observation needed, how results would support or weaken each explanation, and the applicable effort/resource limit. Choose by decision relevance, expected useful information, cost, risk, and reversibility; label estimates as estimates. Do not confuse more observations with more useful knowledge or treat an untested alternative as an improvement.

Keep user-owned goals, required coverage, deliberate methods, and action boundaries intact. Change specialist means or ordering within existing delegation without repeat approval. If a proposed change crosses that boundary, present its concrete impact and obtain only the missing decision. Preserve the full commitment while that decision is pending.

## 4. Record the change to the plan

Reference the previous plan or current progress before updating it. Record only consequential changes: which actions are kept, changed, added, deferred, or removed, why, and which evidence or unresolved hypothesis supports the change. Cancel redundant steps only when required coverage remains intact; deferring a deliverable does not remove the commitment. Distinguish a proposed revision from one accepted or covered by delegation.

Identify dependent decisions and checks affected by changed premises, artifacts, or environment. Retain valid unaffected work/evidence and recheck only affected criteria and relevant regressions. An affected check remains a historical observation and must not establish a pass for the changed subject until revalidated. Unaffected evidence retains its original scope and provenance. Never lower acceptance to make the revised plan appear successful.

Use a compact note in the conversation or the existing task record; this is not a required schema or separate evidence database:

```markdown
Goal, constraints, and previous plan/reference:
Trigger and evidence actually inspected:
Changed understanding and remaining uncertainty:
Selected approach, alternatives when material, and authority/status:
Plan changes and reasons: keep / change / add / defer / remove
Evidence retained and dependent checks needing revalidation:
Next action or probe, distinguishing observation, budget, and stop/revisit condition:
```

## 5. Resume, verify, and retain useful learning

Let `c2o-work` select the next authorized action. Route a probe or delivery slice to the relevant existing specialist, verification to `c2o-verify`, and durable findings to `c2o-learn` only when needed. A directly invoked specialist returns its result to the caller; it does not recursively invoke itself or restart `c2o-work`. In review-only or planning-only work, return findings and proposed plan changes without modifying the subject or starting implementation.

Follow [context-schema.md](context-schema.md): update only relevant decisions, assumptions, acceptance, and progress when persistence changes future work. Retain superseded rationale and links to evidence; do not initialize context or create parallel ledgers for a small task. Learning may happen during work, but each probe need not produce a durable lesson.

Stop reconsidering when the next authorized action is sufficiently supported, the original requested outcome is verified complete, or a real evidence/capability/authority or budget limit prevents progress. If repeated probes add no decision-relevant evidence, change the check when justified or report the dependent work blocked/partial with the missing evidence and revisit condition. Do not loop through reflection indefinitely or label a reduced, budget-limited result complete.
