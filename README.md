# Codex CLI Setup

This repo captures a portable configuration for OpenAI Codex CLI. It includes:

- `config/config.example.toml`: starter config (sanitize secrets before copying to `~/.codex/config.toml`).
- `config/AGENTS.md`: compiled rulebook.
- `agent/rules` & `agent/workflows`: rule files + playbooks.
- `scripts/`: helper automation (`build_agents_manifest.py`, `startup_checklist.py`, `auto_sync_agents.py`).

## Usage

1. **Clone repo** then copy folders into your Codex home (`~/.codex` on Linux/WSL, `C:\Users\<you>\.codex` on Windows).
2. Update `config.example.toml` with real secrets / paths and rename to `config.toml`.
3. Run `python3 scripts/auto_sync_agents.py --force` to rebuild `AGENTS.md` and `rules.index.json`.
4. Execute `python3 scripts/startup_checklist.py` to verify.

> Do not commit real API keys (e.g. Brave Search) – keep placeholders.
