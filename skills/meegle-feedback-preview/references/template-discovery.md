# Discover feedback templates with Meegle

Use these read-only queries before drafting. Resolve the project and work item type first; values below are local query variables, not permanent IDs.

```bash
meegle auth status --format json
meegle project search --project-key '观测云产品使用管理' --format json
meegle workitem meta-types --project-key "$PROJECT_KEY" --format json
meegle workitem meta-fields --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" --field-keys template --format json
meegle workitem meta-fields --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" --field-query '优先级' --format json
meegle workitem meta-fields --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" --field-query '承接小组' --format json
meegle workitem meta-roles --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" --page-num 1 --format json
meegle workitem meta-create-fields --project-key "$PROJECT_KEY" \
  --work-item-type "$WORK_ITEM_TYPE" --format json
```

Check pagination when listing metadata. Discover other relevant fields through `meta-fields` rather than guessing keys. Read the general `meegle` skill for command schemas and field serialization.

## Verified CLI behavior (2026-10-10)

In `观测云产品使用管理`, the active work item type named `反馈` resolved to `67e4df4a0029e0f8957669f4` (`customer_feedback`); other feedback/history types also exist. Re-resolve names and IDs in each task.

- `template` is the feedback-type selector, with separate options for Studio Bug, Studio 需求, DataKit Bug/需求, 部署问题, RUM SDK Bug/需求, and others. Disabled options are also returned and must be filtered out.
- `priority` exposes P0–P3. `承接小组` resolved to `field_8f323e`, a separate select field with routing guidance in `field_desc` and group options in `option`.
- `meegle inspect workitem.meta-create-fields` required both project and work item type; it exposed no template selector parameter. Its result contained a null description default and did not include the receiving-group field, even though the user's new-item form marked that field required. Thus this response cannot describe all template-specific form rules.
- `meegle inspect` exposed no dedicated template-body command at verification time. Recheck the installed CLI if capabilities change; do not invent a template argument or treat option IDs as work item IDs.

## Body verification and fallback

When a supported API/CLI command cannot return the selected template's body, open the authenticated project's new-feedback form and select the exact feedback type. Read its body prompts, other text fields, visible required fields, warnings, and conditional fields. Do not submit a work item just to discover a template.

If the form is inaccessible or incomplete, explain that the template body remains unverified and obtain its contents from the user. Continue organizing facts, but do not replace the missing template with a static local shape.

Existing items can be queried using `workitem query` with a verified `template` label, then read with `workitem get`. They are examples only: the author may have removed, changed, or failed to fill template sections.

For illustration, read-only checks on 2026-10-10 found these different structures in existing items, **not authoritative current template definitions**:

| Feedback type | Observed structure |
| --- | --- |
| Studio 需求 | 需求背景；具体使用场景；核心目的；已提供建议及客户反馈。另有独立的“期望说明（new）”字段。 |
| Studio Bug | 操作步骤描述；实际结果与截图说明；附有会议录像和查询问题 trace_id 的提示。 |
| DataKit 需求 | 场景描述等需求内容。 |
| 部署问题 | Sample items had rewritten free-form bodies; they do not establish the current deployment template. |

Do not use this table as a template catalog or copy these headings instead of reading the selected current form.
