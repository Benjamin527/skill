---
name: meegle-feedback-preview
description: Use when creating Feishu Project/Meegle customer feedback, deployment issue feedback, bug feedback, or any work item where the user provides screenshots or asks to submit feedback.
---

# Meegle Feedback Preview

Use this with the `meegle` skill. It captures the user's preferred workflow for creating feedback in `观测云产品使用管理`.

## Non-Negotiable Flow

1. Gather fields and attachments locally: customer, feedback type/template, title, description, app type, functional module, priority, receiving group (`承接小组`), high-priority reason when applicable, trace/link IDs, screenshots, videos, logs. Mark missing values as pending; do not assign a default priority or receiving group.
2. Resolve live metadata with `meegle` before drafting: project, work item type, enabled template option, customer work item ID, required roles, and field option IDs. Reuse the user-provided or saved local template body as described below; use CLI metadata to validate writable fields and option IDs. A template ID alone is not its body.
3. Upload screenshots as rich-text images with resource type `16`; use resource type `15` only for normal attachment files such as videos, logs, or archives.
4. Fill the selected template's sections with the user's evidence and inline rich-text screenshots. Include any separate rich-text fields required by that template; do not collapse them into `description`.
5. Prepare a complete preview before creating or updating the work item. Explicitly show feedback type, priority, receiving group, their confirmation status, all required fields, full body text, and image placement.
6. Obtain explicit approval of this concrete preview. Priority and receiving group must both have concrete, user-confirmed values before submission; follow the confirmation rules below. An incomplete preview is a draft, not a submission request.
7. After approval, create/update only the approved values and verify them by reading the item back, including template, priority, receiving group, roles, and rich-text images. If the template, priority, receiving group, or substantive content changes after approval, refresh the affected metadata/body and obtain approval of the revised preview before submission.

## Reuse the Selected Template

Read [references/template-discovery.md](references/template-discovery.md) for saved template sections and verified CLI commands. Use the `meegle` auth guard and CLI metadata for the project, work item type, enabled template option, customer ID, required roles, writable fields, and option IDs; reuse metadata already verified in this task.

- Template body precedence: the user's supplied or approved template for this request, then the saved matching local template. Reuse its headings and prompts directly; no browser verification or template rediscovery is needed for routine submission.
- Distinguish the work item type (`反馈`) from the feedback type (`template`, such as `Studio Bug`). Do not reuse a different feedback type's body or a disabled option.
- CLI metadata validates fields and options; it need not return the template body. A null description default or missing template-specific metadata does not invalidate a supplied or saved template and is not a reason to open a browser or block an otherwise complete submission.
- Do not open a browser to inspect templates, verify forms, upload attachments, or submit feedback. Use supported CLI/API commands; browser work requires a separate explicit user request.
- If no matching body is supplied or saved, use a supported template API/CLI if available, or ask only for the missing template content while preserving the prepared facts. Do not borrow another customer's description or invent a template.
- If the server explicitly rejects a field or requirement, report the exact missing item and retain the draft. For a timeout or unknown outcome, query for the item before any retry; do not fall back to the browser or create duplicates.
- When the feedback type changes, use the corresponding supplied/saved template and refresh only the affected field metadata and preview.

## Priority and Receiving Group Confirmation

`优先级` and `承接小组` require user confirmation even if the UI preselects values, the API does not mark them required, or a similar past feedback used them.

- Fetch their current field keys, enabled options, and help text. `承接小组` is its own routing field, not `功能模块`, `客户支持`, or a role owner. Use current group guidance to recommend a group; a recommendation remains pending until accepted.
- If either value is missing, show available choices or a clearly labelled recommendation with its reason, and ask the user to choose/confirm. Do not invent P2, select `其他`/a fallback group automatically, or omit the field to rely on a server default.
- User-specified values earlier in this request count as confirmed; preserve them and show them in the preview without asking the same question again. Values merely visible in a screenshot or copied from an existing item are not confirmation.
- One explicit approval can confirm both values and submission when the complete preview clearly states the exact priority and group and explicitly asks to confirm both. For example: `本次拟提交：优先级 P2，承接小组 平台能力组；请确认这两项及以上完整内容是否可以提交。` This is a confirmation pattern, not a default choice.
- A reply such as `确认` or `可以提交` does not resolve a blank value, multiple alternatives, or an unmentioned group. If either is unresolved, ask only for the missing choice and retain the completed draft.
- For P0/P1, follow current template guidance and collect any required reason, impact, and urgency. Do not infer high priority solely from emphatic wording.

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

Embed the returned values in the relevant template body field (`description` or the appropriate separate rich-text field):

```markdown
![](https://project.feishu.cn/goapi/v5/platform/file/stream/download/<file_token>)<!-- <file_token> -->
```

If the upload response includes `file_url`, prefer:

```markdown
![](<file_url>)<!-- <file_token> -->
```

## Description Follows the Reused Template

There is no universal description shape. Preserve the selected supplied or saved template's headings, order, warnings, and required prompts; replace entry placeholders with supported facts. Place each screenshot in the section it supports. Do not force requirements, deployment issues, SDK bugs, and Studio bugs into the same two-section structure.

Keep observations, expected behavior, and unverified hypotheses distinct. Mark missing required facts as pending rather than inventing them. Include template-specific separate fields (for example, an expectation field) in the draft and preview when applicable.

Do not put initial evidence screenshots in `comment add`. Comments are only for later discussion, mentions, or follow-up notes after the work item exists.

## Preview Checklist

Before asking for approval, show:

- Work item type, selected feedback template label and ID, and the source of the reused body (user-provided or local reference).
- Customer name and resolved customer ID.
- Title.
- Required role assignments such as `客户支持`.
- Priority and receiving group: exact labels, resolved field/option IDs, whether user-confirmed or awaiting confirmation, and any required high-priority reason.
- Other field values with labels and option IDs when useful; distinguish user values, proposed values, and permitted defaults.
- Full description and any separate body fields, preserving the selected template, including image placeholders or embedded Markdown lines.
- Files that will be uploaded and whether they are rich-text images or normal attachments.

If required information is missing, label the preview incomplete and collect it before submission. The documented customer-support role default is permitted; it does not authorize defaults for priority or receiving group. Never use `--ignore-required` to bypass required facts, or confirmation of those two fields.
