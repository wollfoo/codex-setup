---
trigger: always_on
---
type: capability_prompt
scope: project
priority: normal
activation: always_on
---
# LANGUAGE RULES – Profiles

<language_profile>

- Default: follow the Codex CLI Developer Guidelines (language/format as specified by the Developer).
- VI Profile (manual activation):
  - Respond in Vietnamese.
  - For English terms, add a brief Vietnamese explanation when clarity is needed.
- EN Profile (manual activation):
  - Respond in standard English.

## Standard Syntax (when providing term glossaries)
`<English Term>` (Vietnamese description – function/purpose)

## Examples
- `Tool Calling` (invoking tools – triggering functions/external actions to perform a task)
- `Responses API` (response API – reuse context/reasoning across tool calls)
- `Reasoning Effort` (level of reasoning – control depth of thinking and propensity to call tools)
- `Persistence` (perseverance – continue until the request is fully completed before ending the turn)
- `Markdown` (formatting – use semantically; backticks for file/directory/function/class names; \( \) and \[ \] for formulas)
- `Apply Patch` (apply a patch – edit files using the V4A diff standard via `apply_patch`)

</language_profile>
