#!/usr/bin/env python3
"""Automatic synchronization helper for AGENTS.md and rules index."""
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / "agent" / "rules"
WORKFLOWS_DIR = ROOT / "agent" / "workflows"
AGENTS_PATH = ROOT / "AGENTS.md"


def latest_mtime(directory: Path) -> float:
    mtimes = [directory.stat().st_mtime]
    for path in directory.rglob("*.md"):
        mtimes.append(path.stat().st_mtime)
    return max(mtimes)


def needs_sync() -> bool:
    if not AGENTS_PATH.exists():
        return True
    base_time = AGENTS_PATH.stat().st_mtime
    rules_time = latest_mtime(RULES_DIR)
    workflows_time = latest_mtime(WORKFLOWS_DIR)
    return max(rules_time, workflows_time) > base_time


def run_builder(dry_run: bool) -> int:
    if dry_run:
        print("[DRY-RUN] Sẽ chạy: python3 scripts/build_agents_manifest.py --rebuild-index")
        print("[DRY-RUN] Sẽ chạy: python3 scripts/build_agents_manifest.py")
        return 0

    cmds = [
        ["python3", "scripts/build_agents_manifest.py", "--rebuild-index"],
        ["python3", "scripts/build_agents_manifest.py"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, cwd=ROOT, check=False)
        if result.returncode != 0:
            return result.returncode
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Ensure AGENTS.md is in sync with rule sources.")
    parser.add_argument("--force", action="store_true", help="Luôn tái tạo dù không phát hiện thay đổi")
    parser.add_argument("--dry-run", action="store_true", help="Chỉ in ra các lệnh sẽ chạy")
    args = parser.parse_args()

    if not args.force and not needs_sync():
        print("AGENTS.md đã đồng bộ.")
        return

    exit_code = run_builder(args.dry_run)
    if exit_code == 0:
        print("Đã đồng bộ AGENTS.md và rules.index.json." if not args.dry_run else "Dry-run hoàn tất.")
    else:
        raise SystemExit(exit_code)


if __name__ == "__main__":
    main()
