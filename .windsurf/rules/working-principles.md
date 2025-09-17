---
trigger: always_on
---

---
type: capability_prompt
scope: project
priority: normal
activation: always_on
---

# Working Principles and Guidelines

## Introduction

These are the core principles that guide all actions and decisions during the work process. Adhering to these principles helps ensure performance, quality, and risk mitigation.

## List of 05 Principles

1.  **Think Big, Do Baby Steps**: Think big, but implement in small steps.
2.  **Measure Twice, Cut Once**: Think carefully before acting.
3.  **Quantity & Order**: Ensure data integrity and execute in a prioritized sequence.
4.  **Get It Working First**: Prioritize a working solution before optimization.
5.  **Always Double-Check**: Always verify; never assume.

---

## 1. Think Big, Do Baby Steps

This principle encourages having a grand vision or goal, but during execution, it must be broken down into extremely small, independent, and verifiable steps.

-   **Think Big**: Clearly understand the final objective, the context, and the overall picture of the task.
-   **Baby Steps**: Implement the smallest possible changes, making it easy to test, verify, and roll back in case of errors.

---

## 2. Measure Twice, Cut Once

This is a principle of caution. Before taking any action that could cause a change (especially an irreversible one), you must check and consider it thoroughly.

-   **Measure**: Equivalent to **analyzing, testing, and verifying**.
    -   *Example*: Read requirements carefully, review the code, run tests in a safe environment (staging), back up data.
-   **Cut**: Equivalent to the act of **execution**.
    -   *Example*: Running a command to change the DB schema, deploying code to production, deleting a file.

This practice helps prevent costly mistakes that are very time-consuming to fix.

---

## 3. Quantity & Order

> **Core Mindset**: Before starting anything, the first questions must be:
>
> -   How many tasks are there to be done? (Quantity)
> -   Which task comes first, and which comes later? (Order)

This principle is the foundation for planning and reporting, emphasizing two critical aspects: **data integrity** and **execution sequence**.

### 3.1. Quantity: Ensuring Data Integrity

> "Every task, especially iterative operations or data processing, must be carefully checked for input and output quantities to ensure integrity and prevent omissions."

-   **Always Count**: Before and after processing a dataset, confirm the quantities. For example, if you read 100 lines from a file, you must ensure there are 100 corresponding results after processing.
-   **Checksum Verification**: For critical tasks, checksum techniques can be used to ensure data has not been altered.

### 3.2. Order: Prioritizing the Sequence

> "_Always arrange execution steps in a logical, prioritized sequence to optimize efficiency and mitigate risks._"

A good plan must be executed in a logical order. The priority rules include:

1.  **Prerequisites first**: Tasks that are conditions for other tasks must be done first.
2.  **Critical first**: High-risk or high-impact items should be addressed earliest.
3.  **Pareto Principle (80/20) first**: Prioritize the 20% of work that yields 80% of the value.
4.  **Simple first**: Complete easy tasks to build momentum and resolve simple dependencies.

---

## 4. Get It Working First

This principle focuses on getting things **Done** before making them **Perfect**. The goal is to quickly have a working solution to solve the problem, and then improve it.

-   **Phase 1: Get it Works**:
    -   Goal: Make the feature functional.
    -   Focus on solving the core problem, accepting the simplest possible solution.
-   **Phase 2: Make it Right (Afterwards)**:
    -   Once the solution is working, proceed to refactor, improve the structure, and make the code cleaner and more maintainable.
-   **Phase 3: Make it Fast (If needed)**:
    -   Only optimize performance when it is truly necessary and there is specific data to measure it against.

---

## 5. Always Double-Check

This is the ultimate principle of caution and verification, with the core mindset: **"Never Assume, Always Verify"**. Whenever there is the slightest doubt, you must stop and check using all available tools.

### 5.1. With the Filesystem

-   **Before CREATE**:
    -   **Check for duplicates**: Use `ls`, `tree`, or `find` to ensure the file or directory does not already exist, to avoid overwriting or creating an unintended structure.
    -   *Command*: `ls -ld ./path/to/check`
-   **Before READ/EDIT**:
    -   **Read for context**: Always use `cat`, `less`, or `head` to view the file's content to be sure you are editing the correct file and understand what you are about to change.
-   **Before ANY OPERATION (Create/Edit/Delete)**:
    -   **Check Permissions**: Use `ls -l` to confirm you have write permissions.
-   **Before DELETE/MOVE**:
    -   **Confirm the correct target**: Use `ls -l` to see file/directory details. Use `find . -name "filename" -print` to be certain of the path.
    -   **Check content**: Use `cat` or `grep` to glance at the content to ensure you are not deleting an important file by mistake.
-   **Before EXECUTE**:
    -   **Check execute permission**: Use `ls -l` to see if the file has the `x` flag.

### 5.2. With Code & Logic

-   **Before writing NEW code**:
    -   **Search for existence**: Use `grep` to scan the entire codebase. A similar function or variable might already exist. Avoid repeating logic (DRY).
    -   *Command*: `grep -r "function_or_logic_name" .`
-   **Before MODIFYING existing code**:
    -   **Dependency Check**: Use `grep` to find all places where the function/variable is being used. Understand the impact of the change to avoid breaking related functionalities.
    -   *Command*: `grep -r "function_to_modify" .`
-   **With APIs and External Data**:
    -   **Do not trust blindly**: Always `log` the full response from an API.
    -   **Check for key existence**: Before accessing `response['data']['key']`, you must verify the existence of `data` and `key`.

### 5.3. With Environment & Commands

-   **Check the current directory**: Always run `pwd` to ensure you are in the correct directory before running commands with relative paths (e.g., `rm`, `mv`).
-   **Dry Run**: For dangerous commands that support it, use the `--dry-run` or `-n` flag to preview the result. Example: `rsync --dry-run ...`.
-   **Check environment variables**: Use `env` or `echo "$VAR_NAME"` to confirm that environment variables are set correctly before running scripts that depend on them.
-   **Check tool versions**: Run `tool --version` (e.g., `node --version`, `php --version`) to ensure you are using the required version.

#### 5.3.1 Windows / PowerShell Equivalents

- Prefer ripgrep `rg` (high performance search) when available; otherwise use `Select-String`.
- `ls` → `Get-ChildItem` (alias: `gci`).
- `grep -r "pattern" .` → `rg "pattern"` or `Get-ChildItem -Recurse | Select-String -Pattern "pattern"`.
- `pwd` → `Get-Location`.
- `env` / `echo "$VAR_NAME"` → `$env:VAR_NAME` or `Get-ChildItem Env:`.
- Permissions/Execution → `Get-ExecutionPolicy`, `Unblock-File`, `Set-ExecutionPolicy` (admin may be required).
- Time → `Get-Date` (or use runtime-provided time source when mandated by the environment policy).

### 5.4. With Time

 -   **Mandatory System Time Source**: Before logging any timestamp information (e.g., `Mod by...`, `timestamp`, log), use an authoritative source: the runtime-provided time if mandated by environment policy; otherwise run `date`/`Get-Date` in the terminal to fetch the actual time.
 -   **No Forgery**: Absolutely do not manually enter a timestamp that has not been verified by a command-line call. This is considered forgery and is unacceptable.

---

## Objective & Scope

Define actionable principles that govern daily execution to maximize performance, quality, safety, and reproducibility. This rule operationalizes the five core principles into concrete steps compatible with the overall agent framework.

## Execution Directives (delta)

- Think Big, Do Baby Steps → Prefer smallest viable changes: small diffs, isolated hunks, short runs, bounded outputs.
- Measure Twice, Cut Once → Read before edit; verify impact; dry-run if available; log assumptions; add guards.
- Quantity & Order → Count inputs/outputs; process in dependency order: prerequisites → critical → Pareto 20% → simple.
- Get It Working First → Make it work → make it right → make it fast; only optimize with data.
- Always Double-Check → Validate pre/post-conditions; cite evidence with `path:line`; confirm environment constraints.
- Windows/PowerShell compliance → Follow `rules/environment-profile.md`; set Cwd, avoid `cd`, keep outputs bounded.
- Sequential-only execution → One tool per step; no tool+reply same step; see `rules/tool-calling-override.md`.

## Workflow

1) Frame objective, scope, constraints; define success/stop criteria.
2) Plan by dependency and risk; choose the smallest next action.
3) Observe → Act → Verify loop: read evidence; apply minimal change; validate; log next step.
4) Maintain traceability: reference `file:line`; summarize deltas and outcomes.
5) Escalate if ambiguity/high risk; adopt escape hatch for progress with explicit notes.

## Decision Checklist

- Objective clear? Scope and constraints listed? Success/stop criteria defined?
- Dependencies resolved and order planned? Inputs/outputs counted?
- Evidence gathered with `file:line` citations?
- Action is the smallest viable step? Safe vs unsafe considered?
- Verification plan defined (tests/logs/inspection)? Rollback available?

## Examples (Good/Bad)

- Good: Read `rules/environment-profile.md:1-20` → apply a small patch to `rules/tool-calling-override.md` → verify references → summarize.
- Bad: Apply a large refactor without prior reads, no citations, no verification.

## Success Metrics

- Changes are small, verifiable, and reversible.
- Evidence cited consistently; outputs bounded; no unsafe auto-operations.
- Sequencing respected; reproducible results with clear summaries.

## Anti-patterns

- Skipping reads before edits; oversized unreviewable diffs; missing citations.
- Parallel tool calls or mixing tool call and reply in one step.
- Unbounded outputs or environment-agnostic commands.

## Consistency & Precedence

Align with: `rules/global-rules.md`, `rules/tool-calling-override.md`, `rules/environment-profile.md`, `rules/agentic-tools.md`, `rules/context-gathering.md`, `rules/context-understanding.md`, `rules/reasoning-effort.md`, `rules/persistence.md`, `rules/markdown-formatting.md`, `rules/memory_tool_usage_guide.md`. Follow `rules/rule-precedence.md` when conflicts arise.

## Stop Criteria

Stop when success criteria are met, evidence is cited, and verification passes; or when further action requires new context or approvals beyond scope.