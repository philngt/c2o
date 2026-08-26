#!/usr/bin/env python3
"""Initialize non-destructive C2O context and optional Codex agent templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def copy_missing(source: Path, destination: Path) -> tuple[int, int]:
    created = 0
    skipped = 0
    destination.mkdir(parents=True, exist_ok=True)
    for item in sorted(source.iterdir()):
        target = destination / item.name
        if target.exists():
            skipped += 1
            continue
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)
        created += 1
    return created, skipped


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create missing .context files and optional .codex/agents templates."
    )
    parser.add_argument("project_root", type=Path)
    parser.add_argument(
        "--agents",
        action="store_true",
        help="Also create missing project-scoped C2O agent TOML files.",
    )
    args = parser.parse_args()

    root = args.project_root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        parser.error(f"project root is not a directory: {root}")

    skill_root = Path(__file__).resolve().parent.parent
    context_result = copy_missing(
        skill_root / "assets" / "context-template", root / ".context"
    )
    print(
        f"context: created={context_result[0]} skipped={context_result[1]} "
        f"path={root / '.context'}"
    )

    if args.agents:
        agent_result = copy_missing(
            skill_root / "assets" / "codex-agents", root / ".codex" / "agents"
        )
        print(
            f"agents: created={agent_result[0]} skipped={agent_result[1]} "
            f"path={root / '.codex' / 'agents'}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
