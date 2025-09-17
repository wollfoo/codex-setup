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
  - Xác định 4 hàm công cụ cốt lõi (`apply_patch`, `read_file`, `list_files`, `find_matches`) cùng chữ ký chuẩn để vận hành nhất quán (`agent/rules/agentic-tools.md:15`).
  - Bắt buộc một bước/1 công cụ, luôn có preamble, duy trì reasoning_effort và giới hạn tìm context ≤2 lệnh cho tác vụ nhỏ (`agent/rules/agentic-tools.md:40`).
  - Quy tắc V4A cho `apply_patch`: mỗi lần chỉ sửa 1 file, ≥3 dòng ngữ cảnh, đường dẫn tương đối và tách hunk không liên quan (`agent/rules/agentic-tools.md:75`).

### [RULE] CODE EDITING RULES – BLEND-IN
- File: `agent/rules/code-editing-rule.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Áp dụng chu trình 7 bước từ preamble → scan → impact → thiết kế diff → `apply_patch` → verify → summary, dừng khi tìm được dòng cần sửa (`agent/rules/code-editing-rule.md:43`).
  - V4A: ≥3 dòng ngữ cảnh, không gom nhiều file, import luôn ở đầu và tuân thủ cấu trúc Next.js/Tailwind/shadcn mặc định (`agent/rules/code-editing-rule.md:34`).
  - Yêu cầu trả lời bằng tiếng Việt, lưu quyết định vào memory và giới hạn tool budget ≤2 cho tác vụ nhỏ (`agent/rules/code-editing-rule.md:27`).

### [RULE] CONTEXT GATHERING – EARLY STOP + TOOL BUDGET
- File: `agent/rules/context-gathering.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Khuyến khích thu thập ngữ cảnh tối thiểu, dừng ngay khi định danh được file/ký hiệu cần chỉnh và báo cáo nếu phải vượt quá 2 lần gọi công cụ (`agent/rules/context-gathering.md:52`).
  - Chế độ đọc kiến trúc: duyệt tuần tự từng module, không mở nhiều file cùng lúc, luôn có preamble và tóm tắt ngắn gọn (`agent/rules/context-gathering.md:39`).

### [RULE] CONTEXT UNDERSTANDING – BALANCED THOROUGHNESS
- File: `agent/rules/context-understanding.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Tập trung vào thông tin đủ để hành động, tránh đọc lặp; nếu chưa chắc chắn sau chỉnh sửa hãy thu thập thêm bằng chứng (`agent/rules/context-understanding.md:15`).
  - Ưu tiên tự tìm kiếm thay vì hỏi lại người dùng khi có thể giải quyết bằng công cụ (`agent/rules/context-understanding.md:20`).

### [RULE] CURSOR CODING STYLE – CLARITY + PROACTIVE
- File: `agent/rules/cursor-coding-style.md`
- Priority: normal | Activation: always_on | Trigger: always_on | Type: capability_prompt | Scope: project
- Highlights:
  - Viết mã rõ ràng, ưu tiên tên dễ hiểu, hạn chế one-liner; chủ động thực hiện thay đổi thay vì hỏi ý kiến trước (`agent/rules/cursor-coding-style.md:12`).
  - Giữ thông điệp người dùng gọn, song patch phải dễ review và đầy đủ thông tin (`agent/rules/cursor-coding-style.md:21`).

### [RULE] CAREFLOW – DOMAIN RULES (Healthcare scheduling)
- File: `agent/rules/domain-careflow.md`
- Highlights:
  - Quy định phân loại ưu tiên Red/Orange/Yellow/Green với thời hạn đặt lịch tương ứng và ngoại lệ khẩn cấp 911 (`agent/rules/domain-careflow.md:18`).
  - Yêu cầu kiểm tra hồ sơ, bảo hiểm, và xin consent trước khi đặt lịch, ưu tiên tự động đặt slot sớm nhất cho trường hợp Red/Orange (`agent/rules/domain-careflow.md:29`).

### [RULE] TAUBENCH RETAIL – MINIMAL REASONING INSTRUCTIONS
- File: `agent/rules/domain-retail-taubench.md`
- Highlights:
  - Bắt buộc xác minh danh tính khách bằng email hoặc tên + mã vùng trước khi hỗ trợ đơn hàng (`agent/rules/domain-retail-taubench.md:29`).
  - Các thao tác hủy/đổi trả cần xác nhận rõ hành động, danh sách sản phẩm và phương thức thanh toán hoàn tiền (`agent/rules/domain-retail-taubench.md:71`).

### [RULE] ENVIRONMENT PROFILE – Codex CLI Runtime
- File: `agent/rules/environment-profile.md`
- Highlights:
  - Mô tả sandbox `workspace-write`, mạng hạn chế và yêu cầu dùng `workdir` thay vì `cd` (`agent/rules/environment-profile.md:9`).
  - Giới hạn đọc ≤250 dòng mỗi lần và ưu tiên `rg` khi tìm kiếm (`agent/rules/environment-profile.md:15`).

### [RULE] 🎯 GOLDEN RULES
- File: `agent/rules/global-rules.md`
- Highlights:
  - Nhấn mạnh nguyên tắc Evidence-Only, không giả định sáng tạo và luôn trả lời tiếng Việt, trích dẫn nguồn (`agent/rules/global-rules.md:12`).
  - Định nghĩa vai trò nhà khoa học máy tính, yêu cầu đầu ra gồm mục tiêu, giả thuyết, đánh giá, độ phức tạp và kế hoạch tái lập (`agent/rules/global-rules.md:31`).

### [RULE] LANGUAGE RULES
- File: `agent/rules/language-rules.md`
- Highlights:
  - Mặc định hồi đáp bằng tiếng Việt và cung cấp chú thích ngắn cho thuật ngữ tiếng Anh khi cần (`agent/rules/language-rules.md:7`).

### [RULE] MARKDOWN FORMATTING – SEMANTIC USE ONLY
- File: `agent/rules/markdown-formatting.md`
- Highlights:
  - Chỉ dùng Markdown đúng ngữ nghĩa; tên file/thư mục/hàm đặt trong backtick, công thức dùng \( \) hoặc \[ \] (`agent/rules/markdown-formatting.md:7`).

### [RULE] Memory Tool Usage Guide
- File: `agent/rules/memory_tool_usage_guide.md`
- Highlights:
  - Luôn cân nhắc tìm kiếm memory khi có khả năng thiếu bối cảnh; chỉ lưu thông tin mới, tránh trùng lặp (`agent/rules/memory_tool_usage_guide.md:22`).
  - Hướng dẫn đặt tên project/session và sử dụng metadata cho truy vấn hiệu quả (`agent/rules/memory_tool_usage_guide.md:63`).

### [RULE] PERSISTENCE – DO NOT HAND BACK EARLY
- File: `agent/rules/persistence.md`
- Highlights:
  - Tiếp tục cho đến khi hoàn tất yêu cầu, không trả lại sớm khi còn nghi ngờ; tự quyết định giả định hợp lý và cập nhật sau nếu sai (`agent/rules/persistence.md:9`).

### [RULE] REASONING EFFORT – CONTROL THINKING DEPTH + TOOL CALLING
- File: `agent/rules/reasoning-effort.md`
- Highlights:
  - Mặc định `reasoning_effort = high` cho tác vụ phức tạp; điều chỉnh xuống `medium` khi luồng ổn định để giảm độ trễ (`agent/rules/reasoning-effort.md:9`).
  - Yêu cầu lập kế hoạch trước khi gọi công cụ và duy trì persistence, nêu rõ tiêu chí dừng (`agent/rules/reasoning-effort.md:31`).

### [RULE] RULE PRECEDENCE – Conflict Resolution
- File: `agent/rules/rule-precedence.md`
- Highlights:
  - Thứ tự ưu tiên: System > Developer > AGENTS > Domain; chỉ áp dụng domain rule khi không xung đột tầng cao hơn (`agent/rules/rule-precedence.md:12`).

### [RULE] SWE-BENCH – VERIFIED DEVELOPER INSTRUCTIONS
- File: `agent/rules/swe-bench.md`
- Highlights:
  - Luôn chỉnh sửa qua `apply_patch` với V4A; xác minh kỹ lưỡng vì có bài test ẩn (`agent/rules/swe-bench.md:7`).

### [RULE] TERMINAL-BENCH – PROMPT
- File: `agent/rules/terminal-bench.md`
- Highlights:
  - Cho phép sửa mã và chạy test trong workspace, nhắc nhở không thêm license header và kiểm tra `git status` sau khi hoàn tất (`agent/rules/terminal-bench.md:9`).

### [RULE] TOOL CALLING – GLOBAL SEQUENTIAL OVERRIDE
- File: `agent/rules/tool-calling-override.md`
- Highlights:
  - Cấm chạy song song; mỗi bước chỉ gọi một công cụ, kể cả tra cứu file (`agent/rules/tool-calling-override.md:12`).

### [RULE] TOOL PREAMBLES – PLAN + PROGRESS UPDATES
- File: `agent/rules/tool-preambles.md`
- Highlights:
  - Mọi lần dùng công cụ phải mở đầu bằng mục tiêu + kế hoạch, sau đó tường thuật tiến độ và kết thúc bằng tóm tắt (`agent/rules/tool-preambles.md:12`).

### [RULE] Working Principles and Guidelines
- File: `agent/rules/working-principles.md`
- Highlights:
  - 5 nguyên tắc: Think Big, Measure Twice, Quantity & Order, Get It Working First, Always Double-Check; nhấn mạnh kiểm tra trước-sau với mọi thao tác (`agent/rules/working-principles.md:12`).

## Workflows

### [WORKFLOW] Code Editing Playbook
- File: `agent/workflows/code-editing-playbook.md`
- Highlights:
  - Chuẩn hóa quy trình chỉnh sửa từ checklist năng lực tới xác thực, viện dẫn quy tắc V4A và giới hạn tool sequential (`agent/workflows/code-editing-playbook.md:35`).

### [WORKFLOW] Communication & Language Style
- File: `agent/workflows/communication-language-style.md`
- Highlights:
  - Đặt chuẩn giọng điệu, nhấn mạnh tiếng Việt thân thiện, súc tích và trích dẫn khi cần (`agent/workflows/communication-language-style.md:20`).

### [WORKFLOW] Context Scan
- File: `agent/workflows/context-scan.md`
- Highlights:
  - Quy định chuỗi hành động tìm kiếm ngắn gọn để định vị tệp/symbol, phù hợp với giới hạn 2 lần gọi công cụ (`agent/workflows/context-scan.md:18`).

### [WORKFLOW] Debug + Verification
- File: `agent/workflows/debug-verification.md`
- Highlights:
  - Đề xuất thêm log/tạm test có kiểm soát, xác định tiêu chí pass/fail và ghi nhận kết quả (`agent/workflows/debug-verification.md:28`).

### [WORKFLOW] Deep Reasoning
- File: `agent/workflows/deep-reasoning.md`
- Highlights:
  - Áp dụng phân tầng lập luận (strategic/structured/rigorous) và tiêu chí nâng cấp độ sâu suy nghĩ (`agent/workflows/deep-reasoning.md:21`).

### [WORKFLOW] Memory Discipline
- File: `agent/workflows/memory-discipline.md`
- Highlights:
  - Trình tự bắt buộc: kiểm tra memory → dùng → cập nhật sau tác vụ quan trọng, tránh lưu trùng (`agent/workflows/memory-discipline.md:24`).

### [WORKFLOW] Reproducibility Runbook
- File: `agent/workflows/reproducibility-runbook.md`
- Highlights:
  - Yêu cầu ghi nhận seed, version, môi trường và cung cấp hướng dẫn chạy lại (`agent/workflows/reproducibility-runbook.md:18`).

### [WORKFLOW] Rule Precedence & Escalation
- File: `agent/workflows/rule-precedence-escalation.md`
- Highlights:
  - Khi xung đột, xác minh tầng chỉ đạo, ghi nhận lý do và escalates nếu cần (`agent/workflows/rule-precedence-escalation.md:17`).

### [WORKFLOW] SWE-Bench Mode
- File: `agent/workflows/swe-bench-mode.md`
- Highlights:
  - Chế độ đặc biệt cho nhiệm vụ SWE-Bench: ưu tiên độ chính xác, kiểm thử kỹ và tận dụng log (`agent/workflows/swe-bench-mode.md:22`).

### [WORKFLOW] Tool Choreography
- File: `agent/workflows/tool-choreography.md`
- Highlights:
  - Điều phối công cụ theo chu kỳ plan→act→verify, bảo đảm tuần tự và thông báo tiến độ (`agent/workflows/tool-choreography.md:15`).

### [WORKFLOW] Activation Runbook
- File: `agent/workflows/activation-runbook.md`
- Highlights:
  - Chuẩn hoá quy trình kích hoạt: tái tạo manifest bằng `scripts/build_agents_manifest.py --rebuild-index` và chạy checklist khởi động (`agent/workflows/activation-runbook.md:12`).
  - Yêu cầu xác minh log trong `sessions/<YYYY>/<MM>/<DD>` để bảo đảm audit trail, cùng bước thông báo hoàn tất (`agent/workflows/activation-runbook.md:19`).

### [WORKFLOW] Working Principles Support Workflow
- File: `agent/workflows/working-principles.md`
- Highlights:
  - Hướng dẫn áp dụng 5 nguyên tắc vào tác vụ thực tế, nhấn mạnh kiểm đếm số lượng và thứ tự ưu tiên (`agent/workflows/working-principles.md:32`).
