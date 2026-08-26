---
name: c2o-deliver
description: Produce an approved, bounded non-software outcome such as a document, research synthesis, decision memo, operating procedure, content package, analysis, or reversible workflow change while controlling scope and returning evidence. Use when the user has authorized concrete knowledge-work or operational delivery and the desired result is clear enough to act. Avoid for creative work that still needs concept exploration or art direction, which should use c2o-create, source-code implementation, planning-only requests, or external publishing, sending, purchasing, or production actions without explicit authorization.
---

# C2O Deliver

Turn an approved outcome into a usable non-software result. A draft, recommendation, or plan is not evidence that an external effect occurred.

## Establish the delivery contract

1. Identify the audience or operator, triggering situation, and observable result.
2. Classify the delivery mode:
   - artifact: brief, document, content, presentation, spreadsheet, or template;
   - analysis: research synthesis, evaluation, forecast, or decision support;
   - process: checklist, operating procedure, workflow, or training material;
   - bounded operation: an authorized, reversible change using available tools.
3. Confirm acceptance criteria, authoritative inputs, format, destination, constraints, and non-goals.
4. Distinguish the requested state: `drafted`, `prepared`, `applied`, `published`, or `sent`.
5. Resolve only ambiguity that changes the result or crosses an action boundary. Route an unclear outcome through `c2o-shape` or `c2o-spec` first.

Use `c2o-create` first when a design or creative artifact still needs divergent directions, selection, prototyping, or critique. Resume delivery after the creative direction is approved when packaging, handoff, publishing, or another operational action remains.

## Deliver

1. Load the smallest relevant set of source material, existing artifacts, templates, and specialist skills. Prefer the native tool or format-specific skill when one exists.
2. Inspect the current state and preserve user-owned work. Treat approved source material as authoritative over generic conventions.
3. Choose the smallest coherent deliverable or operational slice that can be used and verified end to end.
4. Produce the result without adding unsupported claims, invented metrics, decorative sections, or adjacent work.
5. Preserve provenance for material facts, calculations, decisions, and assumptions.
6. Run the strongest proportionate checks: structural inspection, calculation reconciliation, source comparison, rendered review, reproducible walkthrough, or direct observation.
7. Inspect the final result for scope drift, missing states, audience mismatch, confidentiality risk, and claims that exceed the evidence.

C2O controls the outcome and evidence; it does not replace domain expertise. For legal, medical, financial, safety-critical, or regulated work, use authoritative sources, label uncertainty, and preserve required expert review.

## Respect the action boundary

- Create or edit local artifacts when that is within the request.
- Do not send messages, publish content, change production systems, spend money, alter access, make commitments, or perform destructive operations unless the user explicitly authorized that exact action.
- Before a consequential external action, show what will happen, identify the target, and resolve any choice that could materially change the outcome.
- Report `prepared, not sent` or the equivalent whenever execution stopped at the boundary.

## Finish

Return:

- result delivered and its location or form;
- intended audience and use;
- acceptance evidence;
- material sources and assumptions;
- external actions performed or deliberately not performed;
- remaining gap or review requirement.

Do not claim delivery beyond the state actually reached. If independent verification matters, hand the completed result and acceptance contract to `c2o-verify`.
