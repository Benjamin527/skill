# Guance Learn Article Patterns

Use this reference after classifying the source. These are editorial choices and content paths, not a mandatory table of contents. All example headings are unnumbered; arrows describe reading order, not section numbers.

The publication baseline in `SKILL.md` applies to every formal article archetype below: no body H1, at most eight H2 sections, and at least three embedded body images. Short form does not waive the media requirement, and eight is a ceiling, not a template. Detailed checks live in [publication-review.md](publication-review.md).

## User-Accepted Article Sample

Read on 2026-10-26. These three articles were accepted by the user and classified as “小修后可发布” in the supplied review. Their strengths are examples of writing and evidence organization, not independently reverified product contracts. No need to reread them on every task.

| Article / snapshot | Reusable pattern | Retain the review's small corrections |
|-|-|-|
| [RocketMQ 5.3 可观测最佳实践](https://guanceyun.feishu.cn/wiki/H9xywjnihiaN3nktQ4KcVwMFnYK), revision 24; 3 H2 / 16 images | A concentrated environment/version table; separate Broker and client paths; metric types, units, diagnostic meaning, and alert purpose | Avoid concentrating nearly the entire implementation under “观测云”; provide a minimum path and actual template entry point; many screenshots do not imply every screenshot is necessary |
| [Graphite 对接观测云最佳实践](https://guanceyun.feishu.cn/wiki/YCc5wWSP7iZnYekCNK2cXWYSnrc), revision 33; 8 H2 / 3 images | One known sample value links sending, field/tag mapping, query, and display; a symptom-based troubleshooting table | Explain what each screenshot proves, state the verified DataKit version, and compress generic introduction; normalize numbered headings to the user's default |
| [用统一目录事件时间轴关联故障与变更](https://guanceyun.feishu.cn/wiki/KQcAwMUwsiF4W1kWGOpcwiUanDf), revision 228; 5 H2 / 8 images | Show the outcome before configuration; distinguish entity relationships, matching dimensions, and contextual fields; connect payloads to entity/time/title | Tie each image to its test and time, distinguish expected from observed results, preserve “temporal correlation is not causation,” and check automatic heading numbering |

These different outlines support scenario-led structure. Do not copy their numbering, historical version values, screenshot thresholds, or remaining flaws as universal rules.

## Official Article Sample

Reviewed on 2026-10-13, starting from the [best-practices collection](https://www.guance.com/learn/tagselected?slug=best-practices). This is a focused sample across integration, collection, troubleshooting, and AI-assisted operation, not a statistical claim about the whole site. Observations concern writing and structure; technical configurations still require verification against current documentation.

| Official article | Useful editorial pattern | Adaptation boundary |
|-|-|-|
| [DataKit SNMP 设备指标采集配置最佳实践](https://www.guance.com/learn/articles/datakit-snmp) | Explains the collection path and data shapes before showing a device example; headings name concrete objects | Keep only concepts needed to make configuration decisions; do not inherit internal notes or repeat every configuration variant |
| [基于观测云的 JMeter 压测报告与 APM 关联实践](https://www.guance.com/learn/articles/guance-jmeter-apm) | Starts with a specific analysis gap; explains correlation identifiers; compares measured results and states sample limits | Keep measurement scope and units explicit; normalize mixed heading levels and remove implementation heading numbers |
| [观测云 Agent 让告警先到，分析随后](https://www.guance.com/learn/articles/guance-agent-alert) | Explains the timing tradeoff, separates delivery from analysis, and validates the sequence across system locations | Its Chinese and Arabic heading numbering is not this skill's default; observed timings are example results, not service guarantees |
| [技术实战：观测云告警到飞书群并精准@相关人](https://www.guance.com/learn/articles/guance-feishu) | Presents a message-conversion path, explains the decisive mapping, then gives a minimal test and symptom-led troubleshooting | Rename numbered configuration sections by their purpose; do not treat an article's API fields or identity terminology as a verified contract |
| [OpenTelemetry Node.js 接入观测云最佳实践](https://www.guance.com/learn/articles/opentelemetry-nodejs) | Separates the standard telemetry path from an extension, with prerequisites and a quick success check | Keep optional extensions distinct; remove subsection numbers and reverify versions and defaults |
| [IPMI 实战：服务器硬件监控与异常告警](https://www.guance.com/learn/articles/ipmi) | Connects a hardware blind spot to collection, signal meaning, dashboards, and alerts | Compress generic product introduction; do not mix platform-specific commands or import thresholds without verification |
| [用自然语言驱动观测云：OWL 从查询诊断到资源创建](https://www.guance.com/learn/articles/guance-owl) | Starts with a first useful task, then expands into diagnostic and creation scenarios with reviewable outputs | Remove “场景 + 序号” from subheadings; distinguish queries from resource changes and keep each scenario's input and acceptance criteria explicit |

The sample contains unnumbered, numbered, and mixed outlines. **Unnumbered headings are the user's editorial default, not a claim that every official article already follows it.** Learn the problem-to-action-to-evidence progression, not inconsistent numbering or page furniture. Ignore automatic TOCs, inline sales banners, author metadata, and related-content modules when identifying article structure.

## Shared Opening Pattern

Establish the reader's operating problem, the Guance method or integration path, and the observable result early. A short deck can summarize these; the opening paragraph should add the concrete difficulty or scope instead of repeating the deck.

Avoid opening with a menu path, a feature-definition dump, or broad digital-transformation language. Describe the starting state before promising an outcome. Separate a demonstrated result from an expected benefit.

## Article Archetypes

Choose the closest path, then merge or omit sections according to the source. Section names below are descriptive examples, not required headings.

### Product Configuration Or External Integration

For Webhook, notification channels, cloud events, and third-party platforms:

`场景与目标 → 接入链路 → 开始前的准备 → 按系统或目的配置 → 验证消息与状态 → 必要的排查说明`

Explain what each component receives and produces before configuration. Group actions by the outcome they enable. Keep a field table only when it explains a real mapping or choice. Put critical constraints beside the relevant action rather than hiding them in a final FAQ.

### API Or Developer Practice

For OpenAPI, SDK, MCP, CLI, automation, and code-based integration:

`要解决的问题 → 调用或数据路径 → 环境与权限 → 最小可用示例 → 检查响应与最终结果 → 扩展与边界`

Explain the decisive fields, units, and authentication boundary. Distinguish one complete working path from optional extensions. Add retry, idempotency, or rate-limit details only when relevant and verified. Link to canonical documentation for exhaustive fields.

### Monitoring Or Technology-Stack Practice

For databases, middleware, Kubernetes, cloud services, RUM, APM, logs, and infrastructure:

`观测盲区 → 采集路径 → 最小接入配置 → 信号与诊断含义 → 场景视图或告警 → 检查采集和通知结果`

Connect each important signal to a question the operator needs to answer. A useful metric table explains the metric, unit, and diagnostic meaning. A dashboard screenshot should explain what the reader should notice. Never invent thresholds: use verified defaults, supplied values, measured baselines, or clearly labeled illustrative values.

### Short Integration Tutorial

For a narrow setup with few decisions:

`问题与目标 → 必要准备 → 两端配置 → 验证结果`

One short opening paragraph may cover background and value. Do not add a separate solution overview, FAQ, generic product introduction, or summary just to fill a template.

### AI Or CLI Scenario Practice

For natural-language operation, diagnostic assistants, or several related tasks:

`适用任务 → 接入准备 → 第一个可复核结果 → 不同场景的任务表达与验收 → 权限和使用边界`

Name scenarios by the actual problem, such as `API 5xx 上升：关联链路与日志`, without “场景 2” or section numbers. Each scenario needs a distinct question, usable input, scope, and a way to judge the output. Develop one representative path fully; expand only when the source supports materially different uses. Keep query tasks and resource-writing tasks distinguishable, and state the permissions or review boundary relevant to the actual workflow.

## Heading And Paragraph Craft

A readable outline lets the reader find an action or answer without needing section numbers. Use H2 for main topics, H3 for subordinate tasks, and H4 only when useful. Repair source heading-level mistakes according to the actual parent/child relationship.

For a crowded outline, merge background with goals, environment with permissions, and installation with activation when they serve one task. Put variations, troubleshooting, or reference details under the appropriate parent when useful. Preserve navigation between meaningful tasks; do not simply demote all excess H2s beneath an unrelated section.

For example, a monitoring setup can use this outline without becoming a numbered tutorial:

```markdown
## 将设备指标接入观测云
### 验证设备返回的数据
### 配置 DataKit 采集器
## 用关键指标识别设备异常
## 验证采集与告警结果
```

Do not copy this outline into unrelated topics. A heading such as `配置通知渠道` is clearer than `步骤三`, while `API 5xx 上升` must keep its meaningful digits. Replace textual references like “回到第 3 步” with the relevant action or heading name when that number no longer exists.

Within a substantial section, connect the reason for the action, its decisive detail, and the result to inspect. Use connected paragraphs for explanation, bullets for parallel items, numbered body lists for dependent actions, and tables for comparisons or mappings. Do not turn the whole article into a checklist or use numbered lists as substitute section headings.

## Screenshot And Evidence Placement

Each screenshot should prove a starting state, a configuration choice, a successful test, or the final operational effect. Adjacent prose must explain the action, important field, or success signal; “如下图所示” alone is insufficient.

For in-place edits, image anchors override the preferred outline. Reshape nearby text; do not move images to satisfy a template. Heading cleanup does not authorize deleting or altering screenshots, code, resources, or meaningful figure references.

For a claim of successful integration, name the action performed and where its result is visible. When multiple systems participate, describe how their identifiers, states, or times establish that they refer to the same test. Do not generalize one screenshot's timing or measured value into a guaranteed performance claim.

## Compression And Ending

Merge background and value when short. Keep only the concepts and configuration needed for the reader's decision. Link to reference documentation instead of reproducing catalogs. Convert repeated screenshots to prose only when the user allows media changes.

End once the result and decisive implementation details are clear. A brief practical next step is useful when supported; a repeated introduction, generic praise, or sales CTA is not required.

## Title And Deck

Useful title forms include `使用观测云实现 + 具体结果`, `技术栈接入观测云 + 最佳实践`, or `具体问题：基于观测云的解决路径`. Choose the form that accurately describes the scope; do not promise an end-to-end solution when the source demonstrates only one segment.

The deck should briefly state the scenario, method, and result in natural Chinese. Avoid mechanically starting every article with the same “本文以……为例” formula. Use concrete actions such as “查询”“关联”“验证”; replace unsupported claims like “显著提升效率” with the demonstrated change in workflow.
