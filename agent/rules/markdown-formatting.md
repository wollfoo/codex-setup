---
trigger: always_on
---


---
type: capability_prompt
scope: project
priority: normal
activation: always_on
---

 # MARKDOWN FORMATTING – SEMANTIC USE ONLY

 <markdown_spec>
 - Use Markdown **only where semantically correct** (e.g., `inline code`, ```code fences```, lists, tables).
 - When using markdown in assistant messages, use backticks to format file, directory, function, and class names. Use \( and \) for inline math, \[ and \] for block math.
 - Protocol preamble exception: Protocol-required literal preambles (e.g., Odyssey header/divider/prefix per `sovereign-agent-directive.md:28-35`) may appear at the very top and are not Markdown structures. Apply semantic Markdown rules to the body immediately after the preamble.
 - Two-layer contract: (1) Protocol Header Block (exact literals, topmost). (2) Markdown Body begins on the next line after the preamble. Do not wrap the preamble in code fences or blockquotes, and do not insert any content between the required literal lines.
 - Bilingual note placement: If a Vietnamese explanation is needed for an English literal, place it immediately after the preamble block as the first Markdown line, not interleaved within the preamble.
 </markdown_spec>