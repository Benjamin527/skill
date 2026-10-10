---
name: meegle-feedback-preview
description: Use when creating Feishu Project/Meegle customer feedback, deployment issue feedback, bug feedback, or any work item where the user provides screenshots or asks to submit feedback.
---

# Meegle Feedback Preview

Use this with the `meegle` skill. It captures the user's preferred workflow for creating feedback in `观测云产品使用管理`.

## Non-Negotiable Flow

1. Gather fields and attachments locally: customer, feedback type/template, title, description, app type, functional module, priority, receiving group (`承接小组`), high-priority reason when applicable, trace/link IDs, screenshots, videos, logs. Mark missing values as pending; do not assign a default priority or receiving group.
2. Resolve live metadata with `meegle` before drafting: project, work item type, enabled template option, customer work item ID, required roles, and field option IDs. Read the selected template's actual description and form requirements as described below. A template ID alone is not its body.
3. Upload screenshots as rich-text images with resource type `16`; use resource type `15` only for normal attachment files such as videos, logs, or archives.
4. Fill the selected template's sections with the user's evidence and inline rich-text screenshots. Include any separate rich-text fields required by that template; do not collapse them into `description`.
5. Prepare a complete preview before creating or updating the work item. Explicitly show feedback type, priority, receiving group, their confirmation status, all required fields, full body text, and image placement.
6. Obtain explicit approval of this concrete preview. Priority and receiving group must both have concrete, user-confirmed values before submission; follow the confirmation rules below. An incomplete preview is a draft, not a submission request.
7. After approval, create/update only the approved values and verify them by reading the item back, including template, priority, receiving group, roles, and rich-text images. If the template, priority, receiving group, or substantive content changes after approval, refresh the affected metadata/body and obtain approval of the revised preview before submission.

## Resolve the Selected Template

Use the `meegle` auth guard, then `project search`, `workitem meta-types`, `workitem meta-fields`, `workitem meta-roles`, and `workitem meta-create-fields`. Discover current flags with `meegle inspect` when needed. Read [references/template-discovery.md](references/template-discovery.md) for verified commands and CLI limitations.

- Distinguish the work item type (`反馈`) from the feedback type (`template`, such as `Studio 需求` or `部署问题`). Resolve the selected enabled option from live metadata; never reuse another type's template or a disabled option.
- Obtain the current selected template's headings, instructions, required/conditional sections, separate body fields, and defaults before producing the final preview. Prefer a supported template configuration API/CLI command when available. If CLI exposes only option IDs and general fields, inspect the current new-item form in the authenticated browser, selecting that feedback type without submitting it.
- Generic `meta-create-fields` output is not proof of template-specific requirements. A null description default does not prove the template is empty. Inspect the selected form's visibility and conditional rules, including high-priority reason fields.
- Existing work items may help locate a template or illustrate its structure, but their edited descriptions are not authoritative template definitions. Never copy another customer's content or treat a recent item's body as the current template.
- If the current template cannot be read, continue organizing the supplied facts, label the body as an unverified draft, and explain what is missing. Obtain the template from the user or regain access before submission; do not silently fall back to a fixed generic body.
- If the current form is verified to have no body template, write a case-specific description and identify that fact in the preview. Re-resolve the template and rebuild the draft whenever feedback type changes.

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

## Description Follows the Live Template

There is no universal description shape. Preserve the selected current template's headings, order, warnings, and required prompts; replace entry placeholders with supported facts. Place each screenshot in the section it supports. Do not force requirements, deployment issues, SDK bugs, and Studio bugs into the same two-section structure.

Keep observations, expected behavior, and unverified hypotheses distinct. Mark missing required facts as pending rather than inventing them. Include template-specific separate fields (for example, an expectation field) in the draft and preview when applicable.

Do not put initial evidence screenshots in `comment add`. Comments are only for later discussion, mentions, or follow-up notes after the work item exists.

## Preview Checklist

Before asking for approval, show:

- Work item type, selected feedback template label and ID, and the source used to verify its current body/form.
- Customer name and resolved customer ID.
- Title.
- Required role assignments such as `客户支持`.
- Priority and receiving group: exact labels, resolved field/option IDs, whether user-confirmed or awaiting confirmation, and any required high-priority reason.
- Other field values with labels and option IDs when useful; distinguish user values, proposed values, and permitted defaults.
- Full description and any separate body fields, preserving the selected template, including image placeholders or embedded Markdown lines.
- Files that will be uploaded and whether they are rich-text images or normal attachments.

If required information is missing, label the preview incomplete and collect it before submission. The documented customer-support role default is permitted; it does not authorize defaults for priority or receiving group. Never use `--ignore-required` to bypass template discovery, required facts, or confirmation of those two fields.
