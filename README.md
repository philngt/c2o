# Context to Outcome (C2O)

C2O is a Codex plugin that turns rough requests into the smallest verified outcome. It packages eight focused skills that can be used independently or coordinated through `c2o-work`.

## Skills

| Skill | Purpose |
| --- | --- |
| `c2o-work` | Orchestrate the full context-to-outcome loop. |
| `c2o-shape` | Turn a vague request into an observable, bounded outcome. |
| `c2o-decide` | Compare viable options and resolve consequential trade-offs. |
| `c2o-spec` | Produce a concise, implementation-ready mini-spec. |
| `c2o-slice` | Reduce large work to the smallest valuable vertical slice. |
| `c2o-execute` | Implement an approved slice while preserving scope and evidence. |
| `c2o-verify` | Verify claims against acceptance criteria using direct evidence. |
| `c2o-learn` | Preserve durable decisions, assumptions, progress, and learning. |

## Plugin layout

```text
.codex-plugin/plugin.json
assets/
  icon.svg
skills/
  c2o-work/
  c2o-shape/
  c2o-decide/
  c2o-spec/
  c2o-slice/
  c2o-execute/
  c2o-verify/
  c2o-learn/
```

The manifest exposes the plugin metadata and points Codex to `./skills/`. Each skill keeps its own instructions, UI metadata, references, scripts, and assets together.
