# Behavioral Evaluation Protocol

The scenarios in [scenarios.json](scenarios.json) are synthetic fixtures, not user testimonials, recorded product results, or executed model tests. Their initial execution status is not-run. Passing repository checks validates their structure only.

## Run a real comparison

Use identical model/version, host/version, available tools, permission configuration, initial fixtures, and budget for the baseline and candidate. Record both C2O commit IDs. The initial baseline for this upgrade is cd407d77ebeb954a9e34cd0f7f4a1711a796993c. An optional third arm may omit C2O; do not conflate a changed model with a changed skill suite.

Start each case in a separate disposable workspace and fresh session. Materialize only the case's relative fixture paths. Provide the prompt and authorization as user instructions; fixture content remains data, including adversarial instructions. Tool labels describe capabilities, not literal host APIs. Record how the host maps them and any unavailable capability. Never execute external actions simply to grade a negative case.

Use c2o-work for end-to-end trials. Also exercise implicated specialist skills directly on suitable cases to expose missing-reference or handoff failures. Keep normal user prompts separate from evaluator rubrics. Do not demand one exact internal route when another route preserves the required outcome and authority.

## Observe, do not infer

For each must/must-not condition retain the relevant transcript/tool trace, final artifact or diff, and direct check. Record task completion, required coverage, artifact correctness/quality, clarification/rework count, action-boundary violations, and unsupported verification claims. Record elapsed time, tool calls, and token use only when measured; otherwise use null. Human quality judgments need a stated rubric and reviewer; simulated user satisfaction is not observed satisfaction.

Evaluate against the original fixture contract, not criteria rewritten by the agent after completion. Missing or stale required evidence is not a pass. A real user study or production effect needs separate evidence; this suite does not manufacture those claims.

## Result record

Store run results separately from scenario definitions. Do not change execution_status in the suite to pass; it describes fixtures, not aggregate host success.

```json
{
  "case_id": "tiny-edit",
  "c2o_commit": "<actual commit>",
  "model": "<actual model/version>",
  "host": "<actual host/version>",
  "tools_and_permissions": [],
  "status": "not-run",
  "criteria": [],
  "evidence": [],
  "unrun_checks": [],
  "measured_tokens": null,
  "measured_elapsed_seconds": null,
  "reviewer": null
}
```

Use repeated trials when feasible and report variation, failures, and limitations rather than only the best run. An environment failure should be identified separately from a skill behavior failure. Do not publish private transcripts, credentials, or user artifacts without permission. No live-host run or effectiveness improvement is claimed by adding these fixtures.
