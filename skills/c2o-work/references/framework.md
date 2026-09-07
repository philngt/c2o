# C2O Framework Reference

Use invariants and outcome contracts, not mandatory ceremony. Read only the section needed for the current blocker.

## Intervention levels

| Level | Use when | Maximum usual ceremony |
|---:|---|---|
| 0 | Clear question or tiny reversible edit | Direct answer or action |
| 1 | Several easy-to-miss checks | Short checklist |
| 2 | Meaningful choice among options | Decision note, up to three options |
| 3 | Handoff or multi-step production | Mini-spec/creative contract and acceptance |
| 4 | Cross-component work with costly rollback | Contract, delivery slices, verification plan |
| 5 | High-stakes or effectively irreversible work | Independent evidence, risk review, authorized rollout/recovery plan |

Lower intervention for small, familiar, reversible, locally testable work. Raise it for ambiguity, novelty, blast radius, reversal cost, or safety risk. A high quality target does not automatically require more documents.

## Work-state gates

| State | Exit condition |
|---|---|
| CAPTURED | Request and provisional task class understood |
| SHAPED | Actor, situation, outcome/direction, boundary, and success signal clear |
| INQUIRING | Material dependencies exposed, evidence gaps explicit, shared understanding confirmed |
| DECIDED | Blocking choices resolved or authorized reversible default selected |
| SPECIFIED | Full deliverables, completion level, quality, constraints, acceptance, and non-goals clear |
| READY | A coherent experiment or delivery slice can safely proceed within authority |
| EXECUTING | Current slice produced while preserving the full commitment |
| VERIFYING | Required criteria mapped to current evidence or marked untested |
| DONE | The requested task is complete and verification/delivery status honestly reported |

Skip satisfied gates. Do not force answer-only requests into execution. These states describe work; skill text does not enforce transitions or host permissions. A completed review can report a failed artifact. A larger implementation is not DONE merely because one slice passed. Capture durable learning when there is something material to retain, not as a ritual.

## Choose the next action

Evidence gaps call for inspection/research; user values call for a concrete decision; feel calls for an authorized prototype; behavior calls for a bounded test. Missing authority requires approval. Objective defects return to production for repair only when that is authorized. Invalidated assumptions may return to Shape/Decide; preserve unaffected work and invalidate affected checks.

Do not repeat questions already answered or run iterations without new evidence. Stop for completed scope/quality, a real blocker, a new action boundary, or disproportionate further effort. Report partial work honestly when constrained.

## Decision ownership and information

The user owns outcomes, values, priorities, taste, constraints, risk tolerance, commitments, and authority. The advisor researches and recommends specialist means within delegated bounds. Qualified reviewers retain consequential regulated or licensed judgments.

Separate known facts, reported observations, supported professional defaults, hypotheses, user decisions, qualified-review requirements, and facts best verified after a prototype. An accepted recommendation is not permission to cross an external action boundary.

See outcome-contract.md for requirement classes, quality levels, evidence validity, and separate task/verification/delivery states. Keep the contract in context unless persistence is useful.

## Stage contracts

| Stage | Result |
|---|---|
| Shape | Evidence-backed problem direction or brief, including necessary implications without optional scope expansion |
| Decide | Supported choice or bounded experiment proposal, ownership, acceptance state, and revisit trigger |
| Grill | Dependency-aware facts/decisions/experiments and confirmed shared understanding; no implementation |
| Spec | Full required deliverables, quality/completion level, criteria origins, acceptance methods, boundaries |
| Slice | Explicit experiment or delivery mode; current path, later committed slices, and true non-goals |
| Create | Distinct directions when needed, selection, representative quality slice, complete creative output, observed critique |
| Execute | Coherent implementation, actual checks, bounded repair, and coverage of the software commitment |
| Deliver | Usable non-software result, appropriate handoff, evidence, and exact external-action state |
| Verify | Independent compliance and outcome-fit checks with criterion-level evidence and limitations |
| Learn | Evidence-backed lessons with applicability, changed future action, and invalidation triggers |

## Delegation and completion

Delegate only bounded independent investigation, critique, or verification. Supply the original relevant requirements, artifact/revision, scope, allowed actions, evidence locations, and definition of done. Keep simple sequential work in the main thread. The orchestrator resolves disagreement by inspecting evidence, not majority vote.

Before reporting verified completion, check full requested coverage, agreed quality, current evidence for required acceptance, honest untested areas, material decisions/assumptions, and required human review. Report external actions only when actually performed with authority. Do not claim unobserved real-world effects.
