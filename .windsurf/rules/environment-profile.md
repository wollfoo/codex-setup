---
trigger: always_on
---

---
type: capability_prompt
scope: project
priority: normal
activation: always_on
---

# ENVIRONMENT PROFILE – Codex CLI Runtime


<environment_profile>
- Sandbox: `workspace-write` — read/write only within the workspace; writing outside or performing operations requires privilege escalation.
- Approvals: `on-request` — escalate only when truly necessary, with a concise justification.
- Network: `restricted` — avoid commands that require network; if necessary, request escalation with a clear reason.
- Output limit: terminal output is truncated at ~10KB or 256 lines; prefer reading in small chunks.
- Read rule: read at most 250 lines per file read; if longer, split into multiple consecutive reads.
- Search rule: prefer `rg`/`rg --files` over `ls -R/find/grep`.
- Escalation: when network access or writing outside the workspace is needed, set `with_escalated_permissions: true` and provide a one-sentence justification.

## Assumptions & OS specifics
- **OS/Terminal**: Windows with PowerShell. Use the run-command tool accordingly; outputs may be truncated.
- **Working directory**: always set `Cwd` in tool calls. Do not include `cd` in the command string.
- **Pager**: terminal runs with `PAGER=cat`; avoid commands expecting interactive paging.

## Command execution guidance
- **Safety first**: only auto-run commands that are unquestionably safe (non-destructive, read-only). Otherwise, request approval.
- **Cwd over cd**: specify the working directory via tool parameters; never embed `cd` in commands.
- **Blocking vs non-blocking**: use blocking for short, critical commands where immediate output matters; prefer non-blocking for long-running processes.
- **Timeouts and chunking**: constrain timeouts; for long logs, request limited output and paginate.
- **Quoting (PowerShell)**: prefer double quotes for variable interpolation; escape as needed.

## I/O & output limits
- **Output cap**: expect ~10KB/256-line truncation; tailor commands to limit output (e.g., `-n`, `Select-Object -First N`).
- **File reads**: read ≤250 lines per call; for longer files, read in consecutive chunks with explicit `head`/`tail` or line ranges.
- **Binary/special files**: avoid reading non-text via text tools; use appropriate media readers if available.

## Search & read rules
- **Preferred tools**: use ripgrep (`rg`) instead of `ls -R/find/grep` to reduce noise and permission issues.
- **Scope narrowing**: filter by path and patterns; avoid broad root-level scans when unnecessary.
- **Evidence citation**: when forming conclusions, cite `file:line` for traceability.

## Network & escalation
- **Restricted network**: do not run commands requiring network by default.
- **Escalation**: when network or out-of-workspace writes are required, set `with_escalated_permissions: true` and provide a concise justification.
- **Secrets**: never print or log credentials or tokens; redact sensitive values in outputs.

## Sequential-only compliance
- **One tool call per step**: execute commands strictly sequentially; never run in parallel.
- **Plan + preamble**: before execution, restate the goal and outline steps.
- **Early stop**: stop gathering more context once you can act; proceed with the smallest correct action.
- **Tool budget (small tasks)**: default ≤ 2 tool calls; if exceeding, report rationale.

## Examples
- **Safe read-only command (auto-run allowed)**:
```powershell
# List last 20 git commits safely (bounded output)
git log -n 20 --oneline
```
- **Potentially unsafe command (requires approval)**:
```powershell
# Installs a package (side effects) – do NOT auto-run
npm install
```
- **Scoped file read (bounded)**:
```powershell
# Show first 200 lines only
Get-Content -TotalCount 200 .\\path\\to\\file.txt
```

## Success metrics
- **Sandbox respected**: no writes outside workspace without escalation.
- **No unintended network access**: network commands only after explicit escalation.
- **Output bounded**: large outputs are chunked/limited; no pagination stalls.
- **Traceability**: conclusions reference `file:line` when applicable.
- **Sequential-only**: strictly one tool call per step; plans/preambles present.

## Anti-patterns
- Running networked or state-mutating commands without approval.
- Embedding `cd` in command strings instead of setting `Cwd`.
- Broad, noisy scans (e.g., `ls -R` at repo root) when `rg` with filters suffices.
- Dumping huge outputs without bounds; ignoring the 10KB/256-line cap.
- Exposing secrets in logs or outputs.

## Stop criteria
- The immediate objective is achieved with bounded outputs and traceable evidence; or
- The action would require network/out-of-workspace writes without explicit escalation/approval; or
- More data/confirmation is required from the user to proceed safely.

## Consistency & Precedence
- Follow `rules/rule-precedence.md` (System > Developer > AGENTS > Domain).
- Respect sequential-only tool calls per `rules/tool-calling-override.md`.
- Align with `rules/context-gathering.md`, `rules/context-understanding.md`, `rules/tool-preambles.md`, and `rules/reasoning-effort.md`.

## Data Safety & Privacy
- Avoid printing PII and secrets; redact sensitive values in logs.
- Minimize data exposure in outputs; cite only necessary `file:line`.
- Comply with organizational policies and local regulations when handling data.

</environment_profile>