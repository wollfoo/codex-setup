#!/usr/bin/env python3
"""Run Codex CLI startup checks and record an audit log under sessions/."""
from __future__ import annotations

import json
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config.toml"
WORKFLOW_PATH = ROOT / "agent" / "workflows" / "deep-reasoning.md"
SESSIONS_ROOT = ROOT / "sessions"


def check_config() -> dict[str, object]:
    issues: list[str] = []
    if not CONFIG_PATH.exists():
        issues.append("Thiếu config.toml")
        return {"status": "error", "issues": issues}

    text = CONFIG_PATH.read_text(encoding="utf-8")
    if 'model = "gpt-5-codex"' not in text:
        issues.append("config.toml thiếu model = \"gpt-5-codex\"")
    if 'model_reasoning_effort = "high"' not in text:
        issues.append("config.toml nên đặt model_reasoning_effort = \"high\"")
    if "trust_level" not in text:
        issues.append("Thiếu cấu hình trust_level trong config.toml")
    status = "ok" if not issues else "warn"
    return {"status": status, "issues": issues}


def validate_rule_index() -> dict[str, object]:
    target = ["python3", str(ROOT / "scripts" / "build_agents_manifest.py"), "--skip-agents"]
    result = subprocess.run(target, capture_output=True, text=True, check=False)
    status = "ok" if result.returncode == 0 else "error"
    details = (result.stderr or result.stdout).strip()
    return {"status": status, "details": details}


def check_deep_reasoning_workflow() -> dict[str, object]:
    if not WORKFLOW_PATH.exists():
        return {"status": "error", "details": "Thiếu agent/workflows/deep-reasoning.md"}
    lines = WORKFLOW_PATH.read_text(encoding="utf-8").splitlines()
    heading = next((line.lstrip("# ").strip() for line in lines if line.startswith("#")), "")
    preview = "\n".join(lines[:20])
    return {"status": "ok", "title": heading, "preview": preview}


def write_audit_log(report: dict[str, object]) -> Path:
    now = datetime.utcnow()
    day_dir = SESSIONS_ROOT / f"{now:%Y}" / f"{now:%m}" / f"{now:%d}"
    day_dir.mkdir(parents=True, exist_ok=True)
    log_path = day_dir / f"startup-checklist-{now:%H%M%S}.json"
    payload = {"timestamp": now.isoformat() + "Z", "report": report}
    log_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return log_path


def main() -> None:
    config_status = check_config()
    rule_index_status = validate_rule_index()
    workflow_status = check_deep_reasoning_workflow()

    report = {
        "config": config_status,
        "rule_index": rule_index_status,
        "deep_reasoning_workflow": workflow_status,
    }

    log_path = write_audit_log(report)

    print("Checklist hoàn tất. Nhật ký lưu tại:", log_path)
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
