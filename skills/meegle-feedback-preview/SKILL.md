---
name: meegle-feedback-preview
description: Use when creating Feishu Project/Meegle customer feedback, deployment issue feedback, bug feedback, or any work item where the user provides screenshots or asks to submit feedback.
---

# Meegle Feedback Preview

Use this with the `meegle` skill. It captures the user's preferred workflow for creating feedback in `观测云产品使用管理`.

## Non-Negotiable Flow

1. Gather fields and attachments locally: customer, feedback type/template, title, description, app type, functional module, priority or high-priority reason, trace/link IDs, screenshots, videos, logs.
2. Resolve metadata with `meegle` before drafting: project, work item type, template option, customer work item ID, required roles, and field option IDs.
3. Upload screenshots as rich-text images with resource type `16`; use resource type `15` only for normal attachment files such as videos, logs, or archives.
4. Draft the full `description` field with inline rich-text screenshots.
5. Show the user a preview before creating or updating the work item. The preview must include title, customer, type, key field values, full description text, and where each image will appear.
6. Stop and wait for explicit approval. Do not submit on ambiguous replies. Proceed only after the user clearly agrees, such as "同意", "可以提交", "确认", or equivalent.
7. After approval, create/update the work item and verify by reading it back.

## Default Role Assignment

When creating a new feedback item and the user does not specify `客户支持`, default it to:

- Name: `王雨轩`
- User key: `7485747375298904065`
- Email: `wangyuxuan@guance.com`
- Role: `客户支持` / `role_customersuccess`

Show this default in the preview. If creation requires role owners, include it through `role_owners` in the create fields:

```json
{"field_key":"role_owners","field_value":"[{\"role\":\"role_customersuccess\",\"owners\":[\"7485747375298904065\"]}]"}
```

## Rich-Text Image Rule

Screenshots belong in the body field, not in comments.

Upload each screenshot with:

```bash
meegle attachment +upload "$IMAGE" \
  --resource-type 16 \
  --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" \
  --filename "$NAME" \
  --content-type "$MIME" \
  --format json
```

For an existing work item, use `--work-item-id "$WORK_ITEM_ID"` instead of `--work-item-type`.

Embed the returned values in the description:

```markdown
![](https://project.feishu.cn/goapi/v5/platform/file/stream/download/<file_token>)<!-- <file_token> -->
```

If the upload response includes `file_url`, prefer:

```markdown
![](<file_url>)<!-- <file_token> -->
```

## Description Shape

Preserve the feedback template structure when it exists. For common customer feedback, use this shape:

```markdown
<template warning text if present>

**1.操作步骤描述**

---
[具体操作步骤、客户环境、版本、链接、trace_id 或链路 ID]

现象 1：...
![](<file_url>)<!-- <file_token> -->

现象 2：...
![](<file_url>)<!-- <file_token> -->

**2. 实际结果与截图说明**

---
[实际异常、期望表现、影响范围、补充判断]
```

Do not put initial evidence screenshots in `comment add`. Comments are only for later discussion, mentions, or follow-up notes after the work item exists.

## Preview Checklist

Before asking for approval, show:

- Work item type and template, for example `反馈 / 部署问题`.
- Customer name and resolved customer ID.
- Title.
- Required role assignments such as `客户支持`.
- Field values with labels and option IDs when useful.
- Full description body, including image placeholders or embedded Markdown lines.
- Files that will be uploaded and whether they are rich-text images or normal attachments.

If required information is missing, call it out in the preview and explain the default you will use. Never silently use `--ignore-required` unless the user explicitly accepts that in the preview.
