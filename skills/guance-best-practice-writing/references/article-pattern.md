# Guance Learn Article Patterns

Use this reference after classifying the source. It captures stable editorial patterns, not a mandatory table of contents.

The numbered lists below indicate suggested content order only. Write article headings without numeric, Chinese-numeral, or step-number prefixes unless the user explicitly requests heading numbering for the current article. Preserve heading hierarchy; use numbering within body lists only when it clarifies sequential actions.

## Contents

- Shared opening pattern
- Article archetypes
- Screenshot and evidence placement
- Compression rules
- Title and deck patterns

## Shared Opening Pattern

Strong Guance practice articles usually establish three things early:

1. **Scenario:** who has the problem and under what operating condition
2. **Method:** which Guance capability or integration path is used
3. **Outcome:** what the reader can observe, automate, govern, or troubleshoot afterward

Use a short deck beneath the title. Avoid opening with a menu path, a feature-definition dump, or broad digital-transformation language.

## Article Archetypes

### A. Product Configuration Or External Integration

Use for Webhook, notification-channel, cloud-event, third-party platform, or product-feature setup.

Suggested flow:

1. Background and operational value
2. Solution path
3. Preconditions
4. Grouped configuration steps
5. Concrete example
6. Effect and validation
7. Production considerations or troubleshooting
8. Summary

Keep screenshots beside the exact action or outcome they support.

### B. API Or Developer Practice

Use for OpenAPI, SDK, MCP, CLI, automation, or code-based integration.

Suggested flow:

1. Background and use cases
2. Capability or request-flow overview
3. Authentication, permissions, and prerequisites
4. Interface basics or data contract
5. One or two scenario examples
6. Production concerns: limits, retry, idempotency, security, observability
7. Validation and expected response
8. Summary

Do not turn the article into a full API reference. Link to canonical documentation for exhaustive fields.

### C. Monitoring Or Technology-Stack Practice

Use for databases, middleware, Kubernetes, cloud services, RUM, APM, logs, or infrastructure monitoring.

Suggested flow:

1. Technology and risk context
2. Guance collection or integration path
3. Preconditions and minimum configuration
4. Key signals and their diagnostic meaning
5. Scenario view or dashboard organization
6. Alert strategy grounded in verified fields and user baselines
7. Collection, visualization, and notification validation
8. Summary

Never invent thresholds. Use documented defaults, supplied values, measured baselines, or clearly labeled examples.

### D. Short Integration Tutorial

Use when the source is narrow and the expected read time is short.

Suggested flow:

1. Context
2. Preconditions
3. Third-party configuration
4. Guance configuration
5. Effect
6. Summary

Do not add separate “why this matters,” “solution overview,” or FAQ sections when one concise paragraph is enough.

## Screenshot And Evidence Placement

Each screenshot should prove one of:

- The value or state before implementation
- A configuration decision
- A successful test result
- The final operational effect

The adjacent prose must explain the action, important field, or success signal. “如下图所示” is insufficient.

For in-place edits, image anchors override the preferred outline. Reshape nearby text; do not move images to satisfy the template.

## Compression Rules

- Merge background and value when the article is short
- Merge solution path and prerequisites when both fit in one concise section
- Keep only the minimum runnable configuration
- Convert repeated screenshots into prose only when images are not required to remain
- Move exhaustive field catalogs to canonical documentation links
- Preserve one representative scenario deeply rather than several shallow examples

## Title And Deck Patterns

Useful title forms:

- `观测云 + 能力/对象 + 最佳实践`
- `使用观测云实现 + 具体结果`
- `技术栈接入观测云：从 + 起点 + 到 + 结果`
- `场景问题：基于观测云的 + 解决路径`

The deck should state the practice in one sentence:

> 本文以[场景]为例，介绍如何通过[方法]完成[关键动作]，并在[验证位置]确认[最终结果]。

Adapt the wording; do not mechanically reuse the sentence.

## Tone Check

Prefer concrete operational language:

- “配置完成后，可在事件中心按资源和事件类型查询结果。”
- “只有异常与恢复使用相同核心维度时，系统才能稳定关联状态。”

Avoid generic claims:

- “全面赋能企业数字化转型。”
- “显著提升效率并彻底解决告警问题。”
