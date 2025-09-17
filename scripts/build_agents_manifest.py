#!/usr/bin/env python3
"""Regenerate AGENTS.md from agent rule/workflow sources and validate rule index."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
RULES_DIR = ROOT / "agent" / "rules"
WORKFLOWS_DIR = ROOT / "agent" / "workflows"
INDEX_PATH = ROOT / "rules.index.json"
TARGET_PATH = ROOT / "AGENTS.md"


def slugify(text: str) -> str:
    """Convert a heading into a GitHub-compatible anchor."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_front_matter(lines: list[str]) -> tuple[dict[str, str], int]:
    """Return metadata dict and index where content begins."""
    meta: dict[str, str] = {}
    idx = 0

    while idx < len(lines) and lines[idx].strip() == "---":
        idx += 1
        while idx < len(lines) and lines[idx].strip() != "---":
            line = lines[idx].strip()
            if line and ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip()
            idx += 1
        if idx < len(lines) and lines[idx].strip() == "---":
            idx += 1
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
    return meta, idx


def read_section(path: Path, kind: str) -> dict[str, str | Path]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    meta, content_start = parse_front_matter(lines)

    title = None
    for line in lines[content_start:]:
        if line.startswith("#"):
            title = line.lstrip("#").strip()
            break
    if title is None:
        title = path.stem

    anchor = slugify(f"{kind} {title}")
    return {
        "title": title,
        "anchor": anchor,
        "meta": meta,
        "content": "\n".join(lines[content_start:]).strip(),
        "path": path.relative_to(ROOT),
    }


def gather_sections(directory: Path, kind: str) -> list[dict[str, str | Path]]:
    if not directory.exists():
        raise FileNotFoundError(f"Missing required directory: {directory}")
    return [read_section(path, kind) for path in sorted(directory.glob("*.md"))]


def parse_tags(value: str | None) -> list[str]:
    if not value:
        return []
    value = value.strip()
    if not value:
        return []
    if value.startswith("["):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return [str(item) for item in parsed]
        except json.JSONDecodeError:
            pass
    return [segment.strip() for segment in value.split(",") if segment.strip()]


def format_meta(meta: dict[str, str]) -> str:
    ordered_keys = ["priority", "activation", "trigger", "type", "scope", "tags", "alwaysApply"]
    parts = []
    for key in ordered_keys:
        value = meta.get(key)
        if value:
            parts.append(f"{key}: {value}")
    return " | ".join(parts)


def render_manifest(rules: list[dict[str, str | Path]], workflows: list[dict[str, str | Path]]) -> str:
    lines: list[str] = []
    lines.append("# AGENTS – Compiled Rules")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("- [Rules Overview](#rules-overview)")
    for section in rules:
        lines.append(f"  - [{section['title']}](#rule-{section['anchor']})")
    lines.append("- [Workflows](#workflows)")
    for section in workflows:
        lines.append(f"  - [{section['title']}](#workflow-{section['anchor']})")

    lines.append("")
    lines.append("## Rules Overview")
    for section in rules:
        header = f"### [RULE] {section['title']}"
        lines.append("")
        lines.append(header)
        lines.append(f"- File: `{section['path']}`")
        meta_summary = format_meta(section["meta"] or {})
        if meta_summary:
            lines.append(f"- Meta: {meta_summary}")
        lines.append("")
        lines.append("#### Nội dung")
        lines.append(section["content"] or "(No content)")

    lines.append("")
    lines.append("## Workflows")
    for section in workflows:
        header = f"### [WORKFLOW] {section['title']}"
        lines.append("")
        lines.append(header)
        lines.append(f"- File: `{section['path']}`")
        meta_summary = format_meta(section["meta"] or {})
        if meta_summary:
            lines.append(f"- Meta: {meta_summary}")
        lines.append("")
        lines.append("#### Nội dung")
        lines.append(section["content"] or "(No content)")

    lines.append("")
    return "\n".join(lines) + "\n"


def validate_rule_index() -> None:
    if not INDEX_PATH.exists():
        raise FileNotFoundError("rules.index.json not found")

    data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    changed = False
    missing: list[str] = []

    for entry in data:
        rel_path = Path(entry["file"])
        candidate = ROOT / rel_path
        if candidate.exists():
            continue
        alt = ROOT / "agent" / rel_path
        if alt.exists():
            entry["file"] = str(Path("agent") / rel_path).replace("\\", "/")
            changed = True
            continue
        missing.append(entry["file"])

    if missing:
        joined = ", ".join(missing)
        raise FileNotFoundError(f"Unresolved rule index paths: {joined}")

    if changed:
        INDEX_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rebuild_rule_index(sections: list[dict[str, str | Path]]) -> None:
    entries = []
    keys = ["priority", "activation", "trigger", "type", "scope", "alwaysApply", "tags"]
    for section in sections:
        meta = section["meta"] or {}
        tags = parse_tags(meta.get("tags"))
        entry = {
            "file": str(section["path"]).replace("\\", "/"),
            "title": section["title"],
            "priority": meta.get("priority", ""),
            "activation": meta.get("activation", ""),
            "trigger": meta.get("trigger", ""),
            "type": meta.get("type", ""),
            "scope": meta.get("scope", ""),
            "alwaysApply": meta.get("alwaysApply", ""),
            "tags": tags,
            "meta": {k: v for k, v in meta.items() if k not in keys},
        }
        entries.append(entry)

    entries.sort(key=lambda item: item["title"].lower())
    INDEX_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Rebuild AGENTS.md from rule assets.")
    parser.add_argument("--skip-agents", action="store_true", help="Only validate rules.index.json without writing AGENTS.md")
    parser.add_argument("--output", type=Path, default=TARGET_PATH, help="Optional output path for regenerated manifest")
    parser.add_argument("--rebuild-index", action="store_true", help="Recreate rules.index.json from agent/rules metadata")
    args = parser.parse_args()

    rule_sections = None
    if args.rebuild_index:
        rule_sections = gather_sections(RULES_DIR, "rule")
        rebuild_rule_index(rule_sections)
    validate_rule_index()
    if args.skip_agents:
        return

    if rule_sections is None:
        rule_sections = gather_sections(RULES_DIR, "rule")
    workflow_sections = gather_sections(WORKFLOWS_DIR, "workflow")
    content = render_manifest(rule_sections, workflow_sections)
    output_path = args.output if args.output else TARGET_PATH
    output_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
