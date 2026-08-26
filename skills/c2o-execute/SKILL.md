---
name: c2o-execute
description: Implement an approved, bounded software slice while preserving existing work, controlling scope, following repository instructions, and producing verification evidence. Use when the user has authorized a concrete source-code, configuration, migration, or software-system change and the expected outcome is sufficiently clear. Avoid for non-software documents, analysis, content, or operational delivery, which should use c2o-deliver, and for diagnosis, review, explanation, or planning unless implementation was also requested.
---

# C2O Execute

Deliver the approved outcome with the smallest coherent change.

## Execute

1. Load applicable repository instructions and inspect the real execution path before editing.
2. Restate the outcome, acceptance criteria, and non-goals internally. Resolve only ambiguity that changes the implementation.
3. Check the working tree and preserve unrelated user changes.
4. Choose the smallest design consistent with current evidence. Reuse established patterns before adding abstractions or dependencies.
5. Implement one coherent slice. Do not opportunistically refactor adjacent code unless required for correctness.
6. Validate at the narrowest useful level first, then run broader safe checks when relevant.
7. Inspect the resulting diff for accidental scope expansion, missing error paths, security regressions, and unverified assumptions.

Stop and request direction before destructive actions, irreversible migrations, production writes, meaningful scope expansion, or choices with substantially different user outcomes.

## Finish

Report:

- behavior changed;
- key files or artifacts;
- tests and checks actually run;
- acceptance status;
- limitations or unverified areas.

Never describe an unrun check as passing.
