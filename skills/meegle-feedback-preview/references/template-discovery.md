# Reuse feedback templates and resolve Meegle fields

Reuse the matching template below or the user-provided template. Use these read-only CLI queries to resolve field metadata that has not already been verified in the current task; do not repeat template discovery. Resolve the project and work item type first; values below are local query variables, not permanent IDs.

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

## Saved template bodies

Reuse these saved sections directly for their matching feedback type. The user confirmed local-template reuse on 2026-10-14; routine submissions do not require reading a live browser form. User-provided or approved content for the current request takes precedence.

| Feedback type | Saved sections |
| --- | --- |
| Studio 需求 | 需求背景；具体使用场景；核心目的；已提供建议及客户反馈。另有独立的“期望说明（new）”字段。 |
| Studio Bug | 操作步骤描述；实际结果与截图说明；说明会议录像和查询问题 trace_id 的可用情况。 |

### Studio Bug body

```markdown
## 操作步骤描述

填写环境、版本、操作步骤或原始查询，以及复现所需条件。

## 实际结果与截图说明

填写预期与实际结果、已验证的对照结果，并在对应说明下嵌入截图。
记录已提供的查询请求 trace_id、录像或日志；尚未提供时如实说明获取限制和后续排查方式，不捏造根因或修复结果。
```

For other feedback types, use the user's matching template when supplied. Earlier notes such as “DataKit 需求：场景描述等” or free-form deployment examples are incomplete; do not treat them as complete saved templates.

## Missing information and submission errors

A CLI response with general fields only, or a null description default, is not a missing template when a matching local/user template exists. Continue with that body and validate known required fields and user-confirmed priority/group through CLI metadata.

If no matching saved/user template exists, retrieve it through a supported API/CLI or ask for its contents. Do not open the browser. Existing work items may provide a reference only when needed; never copy another customer's facts.

If the API rejects a submission, retain the draft and report the concrete error or missing requirement. If its outcome is unknown, query before retrying. Do not automatically switch to browser submission. Browser actions require a separate explicit user request.
