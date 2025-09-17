# AGENTS – Compiled Rules

## Table of Contents
- [Rules Overview](#rules-overview)
  - [AGENTIC CODING – TOOL DEFINITIONS (Reference)](#rule-agentic-coding-tool-definitions-reference)
  - [CODE EDITING RULES – BLEND-IN](#rule-code-editing-rules-blend-in)
  - [CONTEXT GATHERING – EARLY STOP + TOOL BUDGET](#rule-context-gathering-early-stop-tool-budget)
  - [CONTEXT UNDERSTANDING – BALANCED THOROUGHNESS](#rule-context-understanding-balanced-thoroughness)
  - [CURSOR CODING STYLE – CLARITY + PROACTIVE](#rule-cursor-coding-style-clarity-proactive)
  - [CAREFLOW – DOMAIN RULES (Healthcare scheduling)](#rule-careflow-domain-rules-healthcare-scheduling)
  - [TAUBENCH RETAIL – MINIMAL REASONING INSTRUCTIONS](#rule-taubench-retail-minimal-reasoning-instructions)
  - [ENVIRONMENT PROFILE – Codex CLI Runtime](#rule-environment-profile-codex-cli-runtime)
  - [🎯 GOLDEN RULES](#rule-golden-rules)
  - [LANGUAGE RULES](#rule-language-rules)
  - [MARKDOWN FORMATTING – SEMANTIC USE ONLY](#rule-markdown-formatting-semantic-use-only)
  - [Memory Tool Usage Guide](#rule-memory-tool-usage-guide)
  - [PERSISTENCE – DO NOT HAND BACK EARLY](#rule-persistence-do-not-hand-back-early)
  - [REASONING EFFORT – CONTROL THINKING DEPTH + TOOL CALLING](#rule-reasoning-effort-control-thinking-depth-tool-calling)
  - [RULE PRECEDENCE – Conflict Resolution](#rule-rule-precedence-conflict-resolution)
  - [SWE-BENCH – VERIFIED DEVELOPER INSTRUCTIONS](#rule-swe-bench-verified-developer-instructions)
  - [TERMINAL-BENCH – PROMPT](#rule-terminal-bench-prompt)
  - [TOOL CALLING – GLOBAL SEQUENTIAL OVERRIDE](#rule-tool-calling-global-sequential-override)
  - [TOOL PREAMBLES – PLAN + PROGRESS UPDATES](#rule-tool-preambles-plan-progress-updates)
  - [Working Principles and Guidelines](#rule-working-principles-and-guidelines)
- [Workflows](#workflows)
  - [Code Editing Playbook](#workflow-code-editing-playbook)
  - [Communication & Language Style](#workflow-communication-language-style)
  - [Context Scan](#workflow-context-scan)
  - [Debug + Verification](#workflow-debug-verification)
  - [Deep Reasoning](#workflow-deep-reasoning)
  - [Memory Discipline](#workflow-memory-discipline)
  - [Reproducibility Runbook](#workflow-reproducibility-runbook)
  - [Rule Precedence & Escalation](#workflow-rule-precedence-escalation)
  - [SWE-Bench Mode](#workflow-swe-bench-mode)
  - [Tool Choreography](#workflow-tool-choreography)
  - [Activation Runbook](#workflow-activation-runbook)
  - [Working Principles Support Workflow](#workflow-working-principles-support-workflow)

## Rules Overview

### [RULE] AGENTIC CODING – TOOL DEFINITIONS (Reference)
- File: `agent/rules/agentic-tools.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Defines 4 core tool functions (`apply_patch`, `read_file`, `list_files`, `find_matches`) with standard signatures for consistent operation (`agent/rules/agentic-tools.md:15`).
  - Mandates one step/one tool, always include a preamble, maintain `reasoning_effort`, and limit context gathering to ≤2 commands for small tasks (`agent/rules/agentic-tools.md:40`).
  - V4A rules for `apply_patch`: edit one file per call, ≥3 context lines, use relative paths, and split unrelated hunks (`agent/rules/agentic-tools.md:75`).

### [RULE] CODE EDITING RULES – BLEND-IN
- File: `agent/rules/code-editing-rule.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Apply a 7-step workflow from preamble → scan → impact analysis → diff design → `apply_patch` → verify → summary; stop once the exact line to modify is identified (`agent/rules/code-editing-rule.md:43`).
  - V4A: ≥3 lines of context, do not bundle multiple files, always place imports at the top, and follow the default Next.js/Tailwind/shadcn structure (`agent/rules/code-editing-rule.md:34`).
  - Require responding in Vietnamese, store decisions in memory, and limit the tool budget to ≤2 for small tasks (`agent/rules/code-editing-rule.md:27`).

### [RULE] CONTEXT GATHERING – EARLY STOP + TOOL BUDGET
- File: `agent/rules/context-gathering.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Encourage minimal context gathering; stop as soon as the target file/symbol is identified; report if exceeding 2 tool calls (`agent/rules/context-gathering.md:52`).
  - Architecture reading mode: traverse modules sequentially, do not open multiple files at once, always include a preamble and a concise summary (`agent/rules/context-gathering.md:39`).

### [RULE] CONTEXT UNDERSTANDING – BALANCED THOROUGHNESS
- File: `agent/rules/context-understanding.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Focus on just-enough information to act; avoid repeated reading; if uncertain after edits, collect additional evidence (`agent/rules/context-understanding.md:15`).
  - Prefer searching yourself over asking the user when tools can resolve the issue (`agent/rules/context-understanding.md:20`).

### [RULE] CURSOR CODING STYLE – CLARITY + PROACTIVE
- File: `agent/rules/cursor-coding-style.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Write clear code, prefer intent-revealing names, avoid one-liners; proactively implement changes rather than asking for permission first (`agent/rules/cursor-coding-style.md:12`).
  - Keep user-facing messages concise, while patches must be easy to review and sufficiently informative (`agent/rules/cursor-coding-style.md:21`).

### [RULE] CAREFLOW – DOMAIN RULES (Healthcare scheduling)
- File: `agent/rules/domain-careflow.md`
- Highlights:
  - Defines priority classes Red/Orange/Yellow/Green with corresponding scheduling deadlines and the emergency 911 exception (`agent/rules/domain-careflow.md:18`).
  - Requires chart review, insurance check, and consent before scheduling; auto-book the earliest slot for Red/Orange cases (`agent/rules/domain-careflow.md:29`).

### [RULE] TAUBENCH RETAIL – MINIMAL REASONING INSTRUCTIONS
- File: `agent/rules/domain-retail-taubench.md`
- Highlights:
  - Requires verifying customer identity via email or name + area code before supporting orders (`agent/rules/domain-retail-taubench.md:29`).
  - Cancellations/returns must confirm the action, item list, and refund method (`agent/rules/domain-retail-taubench.md:71`).

### [RULE] ENVIRONMENT PROFILE – Codex CLI Runtime
- File: `agent/rules/environment-profile.md`
- Highlights:
  - Describes the `workspace-write` sandbox, restricted network, and the requirement to use `workdir` instead of `cd` (`agent/rules/environment-profile.md:9`).
  - Limits reads to ≤250 lines per call and prefers `rg` for searching (`agent/rules/environment-profile.md:15`).

### [RULE] 🎯 GOLDEN RULES
- File: `agent/rules/global-rules.md`
- Highlights:
  - Emphasizes the Evidence-Only principle, no creative assumptions, always respond in Vietnamese, and cite sources (`agent/rules/global-rules.md:12`).
  - Defines the computer scientist role; required outputs include objectives, hypotheses, evaluation, complexity, and a reproducibility plan (`agent/rules/global-rules.md:31`).

### [RULE] LANGUAGE RULES
- File: `agent/rules/language-rules.md`
- Highlights:
  - Default to Vietnamese responses and provide short annotations for English terms when needed (`agent/rules/language-rules.md:7`).

### [RULE] MARKDOWN FORMATTING – SEMANTIC USE ONLY
- File: `agent/rules/markdown-formatting.md`
- Highlights:
  - Use Markdown only where semantically appropriate; wrap file/directory/function names in backticks, and use \( \) and \[ \] for math (`agent/rules/markdown-formatting.md:7`).

### [RULE] Memory Tool Usage Guide
- File: `agent/rules/memory_tool_usage_guide.md`
- Highlights:
  - Always consider searching memory when context might be missing; store only new information and avoid duplicates (`agent/rules/memory_tool_usage_guide.md:22`).
  - Guidance on naming projects/sessions and using metadata for effective retrieval (`agent/rules/memory_tool_usage_guide.md:63`).

### [RULE] PERSISTENCE – DO NOT HAND BACK EARLY
- File: `agent/rules/persistence.md`
- Highlights:
  - Continue until the request is fully completed; do not hand back early when in doubt; make reasonable assumptions and update later if wrong (`agent/rules/persistence.md:9`).

### [RULE] REASONING EFFORT – CONTROL THINKING DEPTH + TOOL CALLING
- File: `agent/rules/reasoning-effort.md`
- Highlights:
  - Default `reasoning_effort = high` for complex tasks; lower to `medium` when flow is stable to reduce latency (`agent/rules/reasoning-effort.md:9`).
  - Require planning before tool calls and maintain persistence, with explicit stop criteria (`agent/rules/reasoning-effort.md:31`).

### [RULE] RULE PRECEDENCE – Conflict Resolution
- File: `agent/rules/rule-precedence.md`
- Highlights:
  - Order of precedence: System > Developer > AGENTS > Domain; apply domain rules only when they do not conflict with higher levels (`agent/rules/rule-precedence.md:12`).

### [RULE] SWE-BENCH – VERIFIED DEVELOPER INSTRUCTIONS
- File: `agent/rules/swe-bench.md`
- Highlights:
  - Always edit via `apply_patch` with V4A; verify thoroughly because hidden tests may exist (`agent/rules/swe-bench.md:7`).

### [RULE] TERMINAL-BENCH – PROMPT
- File: `agent/rules/terminal-bench.md`
- Highlights:
  - Permits code edits and running tests in the workspace; reminds not to add license headers and to check `git status` after completion (`agent/rules/terminal-bench.md:9`).

### [RULE] TOOL CALLING – GLOBAL SEQUENTIAL OVERRIDE
- File: `agent/rules/tool-calling-override.md`
- Highlights:
  - Disallows parallel execution; one tool per step, including file lookups (`agent/rules/tool-calling-override.md:12`).

### [RULE] TOOL PREAMBLES – PLAN + PROGRESS UPDATES
- File: `agent/rules/tool-preambles.md`
- Highlights:
  - Every tool use must start with a goal + plan, then narrate progress, and end with a summary (`agent/rules/tool-preambles.md:12`).

### [RULE] Working Principles and Guidelines
- File: `agent/rules/working-principles.md`
- Highlights:
  - Five principles: Think Big, Measure Twice, Quantity & Order, Get It Working First, Always Double-Check; emphasize pre/post checks for every operation (`agent/rules/working-principles.md:12`).

## Workflows

### [WORKFLOW] Code Editing Playbook
- File: `agent/workflows/code-editing-playbook.md`
- Highlights:
  - Standardizes the editing workflow from capability checklist to verification; cites V4A rules and the sequential tool constraint (`agent/workflows/code-editing-playbook.md:35`).

### [WORKFLOW] Communication & Language Style
- File: `agent/workflows/communication-language-style.md`
- Highlights:
  - Sets the communication tone: emphasizes friendly, concise Vietnamese and cites sources when needed (`agent/workflows/communication-language-style.md:20`).

### [WORKFLOW] Context Scan
- File: `agent/workflows/context-scan.md`
- Highlights:
  - Defines a short search sequence to locate files/symbols, aligned with the ≤2 tool-call limit (`agent/workflows/context-scan.md:18`).

### [WORKFLOW] Debug + Verification
- File: `agent/workflows/debug-verification.md`
- Highlights:
  - Recommends controlled logs/temporary tests, defines pass/fail criteria, and records results (`agent/workflows/debug-verification.md:28`).

### [WORKFLOW] Deep Reasoning
- File: `agent/workflows/deep-reasoning.md`
- Highlights:
  - Applies layered reasoning (strategic/structured/rigorous) with criteria for escalating depth (`agent/workflows/deep-reasoning.md:21`).

### [WORKFLOW] Memory Discipline
- File: `agent/workflows/memory-discipline.md`
- Highlights:
  - Mandatory sequence: check memory → use → update after significant tasks; avoid duplicate storage (`agent/workflows/memory-discipline.md:24`).

### [WORKFLOW] Reproducibility Runbook
- File: `agent/workflows/reproducibility-runbook.md`
- Highlights:
  - Requires recording seed, versions, environment, and providing a reproducibility guide (`agent/workflows/reproducibility-runbook.md:18`).

### [WORKFLOW] Rule Precedence & Escalation
- File: `agent/workflows/rule-precedence-escalation.md`
- Highlights:
  - When conflicts arise, verify the instruction level, record the rationale, and escalate if needed (`agent/workflows/rule-precedence-escalation.md:17`).

### [WORKFLOW] SWE-Bench Mode
- File: `agent/workflows/swe-bench-mode.md`
- Highlights:
  - Special mode for SWE-Bench tasks: prioritize accuracy, thorough testing, and leverage logs (`agent/workflows/swe-bench-mode.md:22`).

### [WORKFLOW] Tool Choreography
- File: `agent/workflows/tool-choreography.md`
- Highlights:
  - Orchestrates tools through the plan→act→verify cycle; ensure sequential execution and progress updates (`agent/workflows/tool-choreography.md:15`).

### [WORKFLOW] Activation Runbook
- File: `agent/workflows/activation-runbook.md`
- Highlights:
  - Standardizes activation: rebuild the manifest with `scripts/build_agents_manifest.py --rebuild-index` and run the startup checklist (`agent/workflows/activation-runbook.md:12`).
  - Requires verifying logs under `sessions/<YYYY>/<MM>/<DD>` to ensure an audit trail, along with a completion notice (`agent/workflows/activation-runbook.md:19`).

### [WORKFLOW] Working Principles Support Workflow
- File: `agent/workflows/working-principles.md`
- Highlights:
  - Guides applying the five principles to practical tasks; emphasizes counting quantities and execution order (`agent/workflows/working-principles.md:32`).
