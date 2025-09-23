---
trigger: always_on
---

---
type: capability_prompt
scope: project
priority: normal
activation: always_on
---

# CONTEXT GATHERING – EARLY STOP + TOOL BUDGET

<context_gathering>
Goal: Get enough context fast. Sequence discovery step-by-step and stop as soon as you can act.

Objective & Scope:
- Objective: Gather just-enough context to act correctly with minimal latency.
- Scope: Applies to discovery/reading phases across code and docs; emphasizes single-step, sequential tool calls.
- Out of scope: Feature ideation beyond the request; multi-file edits; non-evidence-based assumptions.

Principles:
- Search depth: very low; prefer narrow, targeted reads.
- Bias: provide a correct answer quickly even if not fully complete—report residual uncertainty.
- Escape hatch: proceed under uncertainty when reasonable; explicitly report findings and next steps.
- Preamble required before tool calls; concise final summary after.

Method:
- Start broad, then fan out to focused subqueries.
- Sequentially launch varied queries; read top hits per query. Deduplicate paths and cache; don’t repeat queries.
- Avoid over searching for context. If needed, run targeted searches in a short sequential pass.
- Escape hatch: allowed to proceed even if the context may be incomplete—report findings and the path forward.

Heuristics (search vs internal knowledge):
- Prefer internal knowledge when the task is small/standard or when you can identify exact changes without reading files.
- Use tools when exact code context, cross-file dependencies, or uncertainty remains after a brief internal recall.
- Avoid asking the user for clarifications if a quick, targeted read can resolve ambiguity.

Architecture comprehension mode (sequential-only):
- When the goal is to understand the project architecture or module boundaries, open and read files sequentially — one module at a time — to preserve narrative continuity.
- Open files one at a time to synthesize architecture; never open more than one file at once in this mode.
- Rationale: sequential deep reading reduces context switching and prevents premature synthesis errors during architecture mapping.

Sequential codebase context analysis (overview-to-detail; sequential-only):
- Activation:
  - Use when the goal is to understand project architecture or module boundaries.
- Constraints:
  - Execute file reads, directory listings, and searches one at a time (sequential-only) to preserve narrative continuity.
  - One action per step: either call a tool or reply to the user; never both simultaneously.
  - Tool preambles: rephrase the goal and outline a step-by-step plan before calling any tool.
  - Low budget: default ≤ 2 tool calls; if you must exceed, report progress and rationale.
  - Verbosity control: keep user-facing messages concise; prefer targeted, sequential reads; cite sources when appropriate.
  - Evidence citation: reference file:line when appropriate to ground claims.
  - Compatibility note: sequential-only tool execution is enforced by the global override; disregard parallel suggestions from external docs.

### Execution Directives (delta)
- Inherits from `rules/global-rules.md` (Instruction hierarchy & Global execution directives); this section only lists deltas specific to Context Gathering.
- Delta specifics:
  - Start broad then narrow, but only one focused query per step; deduplicate queries and cache paths.
  - Architecture mode: read one module/file at a time; never open multiple files simultaneously.
  - Early stop: stop as soon as you can name exact files/symbols to change.
  - Tool budget: ≤ 2 tool calls by default per small pass; if exceeded, briefly report rationale and progress.
  - Evidence: cite `file:line` when referencing code/config.
  - Preamble required before tool calls; concise summary at the end.
  - Escalate once when signals conflict; otherwise proceed under uncertainty (escape hatch) with reported findings.

- Workflow:
  1) Global overview (high-level):
     - Identify root docs and manifests (e.g., README, CONTRIBUTING, package manager manifests), primary entrypoints (e.g., src/app/, main files), and high-level directory structure (depth 2–3).
     - Note packages/apps/services and major boundaries (domains, layers).
  2) Dependency mapping (module order):
     - Build a lightweight dependency order from providers/dependencies to consumers (analyze dependencies first, then dependents).
     - Use import/require/use edges and config wiring as signals; adjust order if conflicts appear.
  3) Module pass (per module, still high-level):
     - Read public API (exports/types), configs, side-effects, external IO (DB, HTTP, FS), and responsibilities; avoid deep function-level dives.
  4) Function/class deep dive (detailed):
     - After module context is stable, dive into internal functions/classes of each module in the established order (most central/high-risk first).
     - Verify invariants and contracts; add notes for edge cases and error handling.
  5) Verification loop:
     - If new relationships are discovered, update the dependency map and revisit impacted summaries before proceeding.

- Exit criteria:
  - Architecture map + module summaries + key invariants identified; can point to exact files/symbols for critical paths.
  - Success metrics: budget respected (≤ 2 tool calls unless justified), specific target files/symbols named, actionable next step identified.

### Success Metrics
- ≤ 2 tool calls per small discovery pass (unless a brief rationale is provided).
- At least one `file:line` citation when referencing code/configuration.
- Early stop occurs once actionable target is identified; avoid redundant searches.
- Clear preamble and concise final summary; no multi-tool calls in a single step.
- In architecture mode: strictly one file at a time; no parallel or multi-file reads.

### Examples

- Example A — Small code change (fast pass):
  - Search narrowly for the target symbol; open only the top hit; confirm scope via local reads.
  - Stop as soon as you can point to the exact lines to change; proceed to act and summarize findings.
  - Cite evidence with file:line when referencing code.

- Example B — Architecture comprehension mode:
  - Read modules sequentially (one at a time), capture export surfaces and responsibilities.
  - Map dependencies from providers to consumers; note invariants and side effects.
  - Exit when you can name key modules/files for critical paths and outline the change plan.

- Mini flow — Small discovery pass (≤ 2 tool calls):
   1) Preamble & plan
      - Restate the goal and acceptance; outline a sequential plan; commit to ≤ 2 tool calls.
   2) Single narrow search
      - Query for the target symbol in a scoped path; avoid repeats; select the top hit.
   3) Read top hit
      - Open the file around the symbol; cite evidence (e.g., `src/utils/math.ts:42`).
   4) Early stop
      - Stop once exact lines are known; record the next action (e.g., apply_patch) outside this discovery pass.
   5) Summary
      - Summarize findings, file:line, tool calls used, risks, and the next step.

- Notes:
  - Prefer targeted, sequential reads over narrow, per-query grep passes (one at a time) while in this mode.
  - If time-constrained, complete overview + top critical modules (Pareto), then proceed to detailed passes.

- Early stop criteria:
  - You can name exact content to change.
  - Top hits converge (~70%) on one area/path.

- Escalate once:
  - If signals conflict or scope is fuzzy, run one refined sequential pass, then proceed.

- Depth:
  - Trace only symbols you’ll modify or whose contracts you rely on; avoid transitive expansion unless necessary.

- Loop:
  - Sequential search passes → minimal plan → complete task.
  - Search again only if validation fails or new unknowns appear. Prefer acting over more searching.

- Deliverables:
  - Architecture summary and key touchpoints.
  - List of target files/symbols and the expected change scope.
  - Tool plan and call count used; note any budget exceedance and rationale.

### Consistency & Precedence
- Follow order: System > Developer > AGENTS > Domain.
- Keep consistent with: `rules/global-rules.md`, `rules/tool-calling-override.md`, `rules/environment-profile.md`,
  `rules/context-understanding.md`, `rules/reasoning-effort.md`, `rules/persistence.md`, `rules/memory_tool_usage_guide.md`.

### Stop Criteria
- Early stop once you can name exact file/symbol/lines to change.
- Success metrics satisfied; citations present; ≤ 2 tool calls for a small pass; concise summary produced.

### Decision Checklist
- Restated objective and plan before any tool call?
- ≤ 2 tool calls for this discovery pass (unless briefly justified)?
- Cited `file:line` when referencing code/config?
- Stopped early once actionable targets were found?
- Documented residual uncertainty and next steps?

### Anti-patterns (context gathering)
- Repeating the same grep/search with no new parameters or scope.
- Opening multiple files at once or switching rapidly between modules.
- Providing assertions without citing file:line when evidence exists.
- Exceeding the tool budget without reporting progress and rationale.
- Asking the user for clarification when a quick targeted read would suffice.

</context_gathering>