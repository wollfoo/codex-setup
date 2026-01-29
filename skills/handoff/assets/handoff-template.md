---
type: handoff
created: {{DATE}} {{TIME}}
session_id: {{SESSION_ID}}
goal: {{GOAL}}
---

# Handoff: {{TASK_NAME}}

## Context Summary

### 🎯 Goal
{{MAIN_GOAL}}

### 📊 Progress
- **Phase**: {{CURRENT_PHASE}} (planning/implementation/testing/review)
- **Completion**: {{PERCENT}}%

---

## Work Status

### ✅ Completed
- [x] {{COMPLETED_TASK_1}}
- [x] {{COMPLETED_TASK_2}}

### 🔄 In Progress
- [ ] {{IN_PROGRESS_TASK}} ({{PERCENT}}%)

### ⏳ Pending
- [ ] {{PENDING_TASK_1}}
- [ ] {{PENDING_TASK_2}}

---

## 📁 Modified Files

| File | Status | Description |
|------|--------|-------------|
| `{{FILE_PATH_1}}` | modified | {{DESCRIPTION_1}} |
| `{{FILE_PATH_2}}` | created | {{DESCRIPTION_2}} |

---

## 💡 Key Decisions

1. **{{DECISION_1}}**
   - Lý do: {{REASON_1}}
   - Impact: {{IMPACT_1}}

2. **{{DECISION_2}}**
   - Lý do: {{REASON_2}}
   - Impact: {{IMPACT_2}}

---

## ⚠️ Blockers / Issues

| Issue | Status | Notes |
|-------|--------|-------|
| {{ISSUE_1}} | {{STATUS}} | {{NOTES}} |

---

## 🔧 Environment / Dependencies

- **Runtime**: {{RUNTIME}}
- **Key Dependencies**: {{DEPENDENCIES}}
- **Services**: {{SERVICES}}

---

## Resume Prompt

```
Tiếp tục task: **{{TASK_NAME}}**

### Context
{{CONTEXT_SUMMARY_2_3_SENTENCES}}

### Files cần xem
@{{FILE_1}} @{{FILE_2}} @{{FILE_3}}

### Current state
{{CURRENT_STATE}}

### Next action
{{NEXT_ACTION}}

### Reference
`.handoff/checkpoints/{{THIS_FILENAME}}`
```

---

## Session Notes

{{ADDITIONAL_NOTES}}
