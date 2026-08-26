# Context to Outcome (C2O)

![Context flows through decisions and execution into a verified outcome](assets/c2o-readme-banner.png)

> Turn a rough request into the smallest verified outcome.

C2O is a skills-only plugin for Codex and Claude Code. It is designed for work that starts fuzzy and needs to end with evidence. Give it an idea, problem, or change request; it helps clarify the outcome, control scope, implement only what is needed, and verify the result.

You do **not** need to learn all nine skills before using C2O. Start with `c2o-work`; choose a specialist skill only when you already know which stage you need.

## New here? Start with these three steps

### 1. Install C2O in your coding agent

Choose the one you use. You do not need to install both.

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

### 2. Start a new session

For Codex:

```bash
codex
```

For Claude Code:

```bash
claude
```

Plugins are loaded at session start, so use a fresh session after installation.

### 3. Paste your first request

If you use **Codex**, paste:

```text
Use $c2o:c2o-work to turn this rough request into the smallest verified outcome:

"I want the onboarding flow to be easier for first-time users."

First clarify the observable outcome and acceptance signals. Ask only questions
that would change the next action. Do not implement until the scope is clear.
```

If you use **Claude Code**, paste:

```text
Use /c2o:c2o-work to turn this rough request into the smallest verified outcome:

"I want the onboarding flow to be easier for first-time users."

First clarify the observable outcome and acceptance signals. Ask only questions
that would change the next action. Do not implement until the scope is clear.
```

C2O will normally:

1. restate what should observably change;
2. separate facts, assumptions, and decisions;
3. find the smallest useful slice;
4. implement only when you ask for a change;
5. verify the result against explicit acceptance criteria.

## How the workflow fits together

```text
rough request
    → shaped outcome
    → optional deep inquiry
    → resolved decision
    → mini-spec
    → smallest vertical slice
    → execution
    → verification evidence
    → durable learning
```

`c2o-work` coordinates this flow and skips stages that a small, clear task does not need. It enters deep inquiry only when you explicitly ask to be challenged or several consequential decisions depend on one another.

The skill names are the same in both hosts; only the invocation prefix changes:

| Host | Default workflow | Specialist example |
| --- | --- | --- |
| Codex | `$c2o:c2o-work` | `$c2o:c2o-grill` |
| Claude Code | `/c2o:c2o-work` | `/c2o:c2o-grill` |

## Copy-paste examples

The examples below use Codex syntax. In Claude Code, replace `$c2o:` with `/c2o:`; the rest of each prompt stays the same.

### Turn a vague idea into a clear brief

```text
Use $c2o:c2o-shape to clarify this idea:
"Make our weekly project updates more useful."

Identify the actor, current difficulty, desired observable change, scope,
non-goals, assumptions, and acceptance signals. Do not design a solution yet.
```

### Compare an important technical decision

```text
Use $c2o:c2o-decide to compare SQLite and Postgres for this project.

Base the recommendation on our actual scale, deployment model, operational
capacity, migration cost, and reversibility. Separate evidence from assumptions.
```

### Stress-test a complex plan before action

```text
Use $c2o:c2o-grill to challenge this multi-region migration plan before we act.

Map the dependent fact, decision, and experiment nodes. Research facts instead
of asking me. Interview me only about decisions whose prerequisites are settled,
and do not implement anything until I confirm our shared understanding.
```

Use Grill for branching, consequential decisions—not for a vague request that shaping or a cheap prototype can resolve faster.

### Prepare work for implementation

```text
Use $c2o:c2o-spec to turn the approved onboarding brief into a mini-spec.

Include the primary scenario, in-scope behavior, important failure states,
acceptance criteria, non-goals, and a verification approach.
```

### Find the smallest valuable implementation

```text
Use $c2o:c2o-slice to reduce this feature to one end-to-end slice.

The slice must produce an observable user result and test the riskiest useful
assumption. Explicitly list what is deferred.
```

### Implement and verify a bounded change

```text
Use $c2o:c2o-work to implement the approved mini-spec in this repository.

Preserve existing work, implement the smallest coherent slice, run the relevant
checks, and return criterion-by-criterion evidence.
```

### Review a result without changing it

```text
Use $c2o:c2o-verify to review the current implementation against
docs/onboarding-spec.md.

Report each acceptance criterion as pass, partial, fail, or not tested.
Do not repair failures.
```

## Which skill should I use?

| If you need to… | Codex | Claude Code |
| --- | --- | --- |
| Move a rough request all the way to a verified result | `$c2o:c2o-work` | `/c2o:c2o-work` |
| Clarify an idea before choosing a solution | `$c2o:c2o-shape` | `/c2o:c2o-shape` |
| Compare options with meaningful trade-offs | `$c2o:c2o-decide` | `/c2o:c2o-decide` |
| Stress-test several dependent decisions before action | `$c2o:c2o-grill` | `/c2o:c2o-grill` |
| Write a small implementation-ready specification | `$c2o:c2o-spec` | `/c2o:c2o-spec` |
| Cut a large feature into one valuable end-to-end slice | `$c2o:c2o-slice` | `/c2o:c2o-slice` |
| Implement an already approved slice | `$c2o:c2o-execute` | `/c2o:c2o-execute` |
| Check a result against explicit criteria | `$c2o:c2o-verify` | `/c2o:c2o-verify` |
| Preserve useful decisions and learning after completion | `$c2o:c2o-learn` | `/c2o:c2o-learn` |

When unsure, use `c2o-work`: `$c2o:c2o-work` in Codex or `/c2o:c2o-work` in Claude Code.

## Installation details

### Requirements

- [Codex CLI](https://developers.openai.com/codex/cli/) or [Claude Code](https://code.claude.com/docs/en/setup)
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

## Plugin contents

| Skill | Purpose |
| --- | --- |
| `c2o-work` | Orchestrate the complete context-to-outcome loop. |
| `c2o-shape` | Turn a vague request into an observable, bounded outcome. |
| `c2o-decide` | Compare viable options and resolve consequential trade-offs. |
| `c2o-grill` | Expose dependent decisions through prerequisite-aware inquiry. |
| `c2o-spec` | Produce a concise, implementation-ready mini-spec. |
| `c2o-slice` | Reduce large work to the smallest valuable vertical slice. |
| `c2o-execute` | Implement an approved slice while preserving scope and evidence. |
| `c2o-verify` | Verify claims against acceptance criteria using direct evidence. |
| `c2o-learn` | Preserve durable decisions, assumptions, progress, and learning. |

## Repository layout

```text
.agents/plugins/marketplace.json
.claude-plugin/
  marketplace.json
  plugin.json
.codex-plugin/plugin.json
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
  c2o-execute/
  c2o-verify/
  c2o-learn/
```

The Codex and Claude Code manifests both point to the same `./skills/` directory, so the workflow stays consistent across hosts. Each skill keeps its instructions, UI metadata, references, scripts, and assets together.
