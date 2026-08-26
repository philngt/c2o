# Context to Outcome (C2O)

![Context flows through decisions and delivery into a verified outcome](assets/c2o-readme-banner.png)

> Start with a rough request or weak signal. Reach the smallest verified outcome.

C2O is an outcome workflow for knowledge, creative, and software work, packaged as a skills-only plugin for Codex, Claude Code, and Google Antigravity (AGY). Give it an idea, weak signal, creative brief, problem, or change request; it helps discover what is actually wrong, clarify the outcome, control scope, produce only what is needed, and verify the result.

You do **not** need to learn all eleven skills before using C2O. Start with `c2o-work`; choose a specialist skill only when you already know which stage you need.

## New here? Start with these three steps

### 1. Install C2O in your agent

Install only the one you use.

**Codex**

```bash
codex plugin marketplace add philngt/c2o --ref main
codex plugin add c2o@c2o
```

**Claude Code**

```bash
claude plugin marketplace add philngt/c2o@main
claude plugin install c2o@c2o
```

**Google Antigravity (AGY CLI)**

```bash
agy plugin install https://github.com/philngt/c2o
```

### 2. Start a new session

| Host | Start command |
| --- | --- |
| Codex | `codex` |
| Claude Code | `claude` |
| Antigravity CLI | `agy` |

Plugins are loaded at session start, so use a fresh session after installation.

### 3. Paste your first request

The same prompt works in all three hosts:

```text
Use the installed c2o-work skill to turn this rough request into the smallest verified outcome:

"Something seems wrong with our customer-support onboarding. New agents appear
to struggle, but I do not know exactly where or how to describe the problem."

Start from what I can observe. Ask one plain-language question at a time and do
not ask me for the root cause, solution, method, or tool. Inspect any evidence
you can access, separate observations from hypotheses, and recommend where to
investigate next. Do not change the live process until the problem is clear.
```

C2O will normally:

1. start from a concrete signal even when you cannot name the problem;
2. separate observations, reports, hypotheses, and unknowns;
3. research facts and explain unfamiliar choices plainly;
4. recommend the next investigation or specialist choice;
5. find the smallest useful slice;
6. create, deliver, or implement only when you ask for action;
7. verify the result against explicit acceptance criteria.

A one-sentence symptom is enough to begin. C2O should not require you to arrive with a diagnosis or proposed solution.

## New to the domain? You still own the right decisions

| Decision owner | What that means |
| --- | --- |
| You | Choose the outcome, values, priorities, taste, budget, acceptable risk, commitments, and approvals. |
| C2O as advisor | Research and recommend methods, tools, techniques, architecture, and other specialist means. |
| Qualified professional | Review consequential legal, medical, financial, safety, regulatory, or licensed judgments. |

You can answer `use your recommendation` when C2O has explained a specialist choice and its trade-off. C2O will not treat that as permission to publish, spend money, change production, cross another action boundary, or waive qualified review.

## How the workflow fits together

```text
rough request or weak signal
    → problem direction or shaped outcome
    → optional expert-guided inquiry
    → resolved decision
    → mini-spec or creative contract
    → smallest end-to-end slice
    → creation, delivery, or implementation
    → verification evidence
    → durable learning
```

`c2o-work` coordinates this flow and skips stages that a small, clear task does not need. It enters deep inquiry only when you explicitly ask to be challenged or several consequential decisions depend on one another.

The skill names are the same in all three hosts; only the invocation prefix changes:

| Host | Default workflow | Specialist example |
| --- | --- | --- |
| Codex | `$c2o:c2o-work` | `$c2o:c2o-grill` |
| Claude Code | `/c2o:c2o-work` | `/c2o:c2o-grill` |
| Antigravity CLI | `/c2o:c2o-work` | `/c2o:c2o-grill` |

## Where C2O helps

| Domain | Example outcome |
| --- | --- |
| Problem discovery | Turn “something is wrong” into an evidence-backed direction for the next investigation. |
| Product | Turn a broad feature idea into one testable pilot. |
| Operations | Design and deliver a bounded process improvement with clear handoffs. |
| Research and strategy | Separate facts from decisions, compare options, and preserve assumptions. |
| Design and creative | Explore distinct directions, select deliberately, produce the artifact, and critique it against the brief. |
| Content and communication | Produce an approved brief, playbook, or content package without silently publishing it. |
| Software | Specify, implement, and verify the smallest coherent code change. |

## Copy-paste examples

The examples below use Codex syntax. In Claude Code or Antigravity CLI, replace `$c2o:` with `/c2o:`; the rest of each prompt stays the same.

### Clarify a problem you cannot yet describe

```text
Use $c2o:c2o-shape to help me understand this problem:
"Customers seem to abandon onboarding, but I do not know where or why."

Ask one observable question at a time. Start with a representative case, inspect
available evidence, and separate facts from hypotheses. Do not ask me to diagnose
the cause or choose a solution. Recommend the next useful investigation.
```

### Compare an important business decision

```text
Use $c2o:c2o-decide to compare hiring a full-time support specialist,
using a contractor, and outsourcing the function.

Base the recommendation on actual demand, coverage hours, quality control,
ramp-up time, cost, and reversibility. Separate evidence from assumptions.
```

### Stress-test a complex plan before action

```text
Use $c2o:c2o-grill to challenge our plan to enter the German market before we act.

I have not led an international expansion before. Act as an experienced market-entry
advisor: research facts, explain each decision in plain language, and recommend the
specialist choices with evidence, trade-offs, and confidence. Ask me only about our
goals, constraints, acceptable risk, and approvals. Do not move to delivery until
I confirm our shared understanding.
```

Use Grill for branching, consequential decisions—not for a vague request that shaping, one expert recommendation, or a cheap prototype can resolve faster.

### Prepare work for handoff

```text
Use $c2o:c2o-spec to turn the approved support-response pilot into a mini-spec.

Include the target queue, primary scenario, handoffs, deliverables, failure states,
acceptance criteria, non-goals, and verification approach.
```

### Find the smallest valuable pilot

```text
Use $c2o:c2o-slice to reduce our company-wide support redesign to one end-to-end pilot.

Cover one real path from ticket arrival to a useful first response. The pilot must
test the riskiest useful assumption. Explicitly list what is deferred.
```

### Develop a creative direction

```text
Use $c2o:c2o-create to develop a launch visual direction for a privacy-first
journaling app.

The audience is privacy-conscious first-time users; the intended response is
"calm, trustworthy, and personal." Create three materially distinct directions
at style-frame fidelity. Explain the rationale and trade-off of each, recommend
one, but do not treat it as selected or publish anything until I approve it.
```

`c2o-create` can use an available image-generation or media skill for production. Use `c2o-execute` after a UI direction is approved and must become product code; use `c2o-deliver` when the finished artifact must be packaged, sent, or published.

### Deliver a non-software outcome

```text
Use $c2o:c2o-deliver to produce the approved customer-escalation playbook.

Use our existing policies as the source of truth, cover the required scenarios,
and return acceptance evidence. Prepare the playbook, but do not publish it or
notify the team.
```

### Implement a bounded software change

```text
Use $c2o:c2o-execute to implement the approved onboarding slice in this repository.

Preserve existing work, implement the smallest coherent slice, run the relevant
checks, and return acceptance evidence.
```

### Review a result without changing it

```text
Use $c2o:c2o-verify to review the customer-escalation playbook against
docs/support-pilot-spec.md.

Report each acceptance criterion as pass, partial, fail, or not tested.
Do not repair failures.
```

## Which skill should I use?

| If you need to… | Codex | Claude Code / AGY CLI |
| --- | --- | --- |
| Move a rough request all the way to a verified result | `$c2o:c2o-work` | `/c2o:c2o-work` |
| Clarify an idea or a problem you cannot describe yet | `$c2o:c2o-shape` | `/c2o:c2o-shape` |
| Compare options with meaningful trade-offs | `$c2o:c2o-decide` | `/c2o:c2o-decide` |
| Get expert-guided advice through several dependent decisions | `$c2o:c2o-grill` | `/c2o:c2o-grill` |
| Write a small action-ready specification | `$c2o:c2o-spec` | `/c2o:c2o-spec` |
| Cut a large initiative into one valuable end-to-end slice | `$c2o:c2o-slice` | `/c2o:c2o-slice` |
| Explore, select, and refine a design or creative direction | `$c2o:c2o-create` | `/c2o:c2o-create` |
| Deliver an approved document, analysis, process, or operational change | `$c2o:c2o-deliver` | `/c2o:c2o-deliver` |
| Implement an approved software slice | `$c2o:c2o-execute` | `/c2o:c2o-execute` |
| Check a result against explicit criteria | `$c2o:c2o-verify` | `/c2o:c2o-verify` |
| Preserve useful decisions and learning after completion | `$c2o:c2o-learn` | `/c2o:c2o-learn` |

When unsure, use `c2o-work`: `$c2o:c2o-work` in Codex or `/c2o:c2o-work` in Claude Code and AGY CLI.

## Installation details

### Requirements

- [Codex CLI](https://developers.openai.com/codex/cli/), [Claude Code](https://code.claude.com/docs/en/setup), or [Antigravity CLI](https://www.agy.dev/docs/cli/installation/)
- Git access to GitHub

### Codex

If Codex CLI is not installed yet:

```bash
npm install --global @openai/codex
```

Then add the C2O marketplace and install the plugin:

```bash
codex plugin marketplace add philngt/c2o --ref main
codex plugin add c2o@c2o
```

To confirm that Codex can see it:

```bash
codex plugin marketplace list
codex plugin list --marketplace c2o
```

You can also start `codex`, enter `/plugins`, choose the **Context to Outcome (C2O)** marketplace, and manage the plugin from the plugin browser.

If C2O does not appear immediately, restart Codex or the ChatGPT desktop app and begin a new session.

### Claude Code

Add the marketplace and install C2O from your terminal:

```bash
claude plugin marketplace add philngt/c2o@main
claude plugin install c2o@c2o
```

To confirm that Claude Code can see it:

```bash
claude plugin marketplace list
claude plugin list
```

You can also run these commands inside a Claude Code session:

```text
/plugin marketplace add philngt/c2o
/plugin install c2o@c2o
```

Start a fresh session after installation, then invoke the main workflow with `/c2o:c2o-work`.

To try a local clone without installing it:

```bash
claude --plugin-dir .
```

### Google Antigravity (AGY CLI)

Install C2O directly from GitHub:

```bash
agy plugin install https://github.com/philngt/c2o
```

Confirm that AGY loaded the plugin:

```bash
agy plugin list
```

Start a fresh session with `agy`, then invoke the main workflow with `/c2o:c2o-work`.

## Plugin contents

| Skill | Purpose |
| --- | --- |
| `c2o-work` | Orchestrate the complete context-to-outcome loop. |
| `c2o-shape` | Turn a vague request or weak signal into a bounded problem direction. |
| `c2o-decide` | Compare viable options and resolve consequential trade-offs. |
| `c2o-grill` | Guide dependent decisions with researched, plain-language expert recommendations. |
| `c2o-spec` | Produce a concise, action-ready mini-spec. |
| `c2o-slice` | Reduce large work to the smallest valuable end-to-end slice. |
| `c2o-create` | Explore, select, produce, and critique a creative outcome. |
| `c2o-deliver` | Produce an approved non-software outcome within explicit action boundaries. |
| `c2o-execute` | Implement an approved software slice while preserving scope and evidence. |
| `c2o-verify` | Verify claims against acceptance criteria using direct evidence. |
| `c2o-learn` | Preserve durable decisions, assumptions, progress, and learning. |

## Repository layout

```text
.agents/plugins/marketplace.json
.claude-plugin/
  marketplace.json
  plugin.json
.codex-plugin/plugin.json
plugin.json
assets/
  c2o-readme-banner.png
  icon.svg
skills/
  c2o-work/
  c2o-shape/
  c2o-decide/
  c2o-grill/
  c2o-spec/
  c2o-slice/
  c2o-create/
  c2o-deliver/
  c2o-execute/
  c2o-verify/
  c2o-learn/
```

The Codex, Claude Code, and Antigravity manifests all use the same `./skills/` directory, so the workflow stays consistent across hosts. Each skill keeps its instructions, UI metadata, references, scripts, and assets together.
