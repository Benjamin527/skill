---
name: guance-best-practice-writing
description: Use when a Guance product, integration, observability, API, monitoring, or solution draft must be rewritten as a public best-practice article, especially from an internal SOP, Feishu document, screenshot-heavy tutorial, configuration note, or rough technical draft.
---

# Guance Best Practice Writing

## Overview

Create one public-facing Chinese article that feels native to `guance.com/learn`: concrete scenario, verified facts, reproducible implementation, observable outcome.

**Core principle:** evidence determines content; the scenario determines structure. Never invent technical facts to complete a template.

## Delivery Mode

| Input | Default delivery |
|-|-|
| Draft material | One title, a 50–100 Chinese-character deck, and one complete article |
| Existing Feishu/CMS document | Edit in place, preserve resources, then return a concise completion note and link |
| Explicit placement request | Add screenshot anchors as a separate publishing variant |

Do not return parallel versions, editor notes, or a change log unless requested.

## Heading Style

By default, write the article title and all section/subsection headings without numbering. Use descriptive heading text directly: `## 配置通知渠道`, not `## 1. 配置通知渠道`, `## 一、配置通知渠道`, `## 1.1 配置通知渠道`, or `## 步骤一：配置通知渠道`.

When rewriting a source, remove inherited heading numbers while preserving heading hierarchy and meaning. The reference flows describe content order, not numbered article headings. Ordered lists within the body may still number actual sequential actions; preserve meaningful numbers in names, versions, and technical content. Add heading numbering only when the user explicitly requests it for the current article.

## Hard Gates

### Evidence

Classify implementation claims as **verified in source**, **verified externally**, or **unverified**.

**REQUIRED SUB-SKILL:** Use `web-access` for online research or verification. Prefer current official `guance.com` and `docs.guance.com` sources.

Verify unstable or high-impact facts before publishing: menu paths, product names, fields, units, headers, API limits, permissions, status values, defaults, thresholds, and version behavior.

Never invent missing details, choose between conflicting examples because one “looks right,” present customer requirements as universal product behavior, or publish secrets and private identifiers. If a required fact cannot be verified, omit it, request the missing source, or label it as non-executable user-supplied context. Labeling does not make an unverified header, field, limit, permission, or threshold publishable as an executable practice.

### Media Preservation

Before editing an existing document, record every image/resource block ID or token, original order, neighboring text anchors, and the action or result it proves. When code placement must remain, include code block IDs and the global image/code order in the same ledger.

If media must remain unchanged:

- Do not overwrite the document
- Do not replace, upload, crop, resize, reorder, or move media
- Use precise block updates; do not delete or rebuild media parents or neighboring anchor blocks
- Rewrite text around media anchors rather than moving media to fit an outline
- After editing, verify the same resource count, tokens, image/code order, anchors, and meaning

Treat images, files, whiteboards, sheets, Base blocks, citations, and synced references as immutable unless the user explicitly requests a change.

### Reproducibility

Before drafting, identify the target reader, starting state, desired outcome, prerequisites, two to four decisive details, verification location, success signal, and likely failure signal.

## Workflow

### Diagnose And Route

Classify the source and separate public facts from internal notes, customer-specific requirements, duplication, and confidential data. Read [references/article-pattern.md](references/article-pattern.md) completely, then choose the closest article archetype. Do not force every article into “背景—价值—方案—步骤—FAQ—总结.” Explicit user formatting may retain requested heading names, but it never overrides evidence, safety, media, or reproducibility gates.

### Define The First Screen

Write a concrete title and deck that establish:

- The reader's scenario
- The Guance method or integration path
- The observable result

Avoid generic “使用方法,” broad digital-transformation language, and opening with a menu path.

### Rebuild The Practice

- Explain the solution path before detailed actions
- Group steps by purpose, not by every click
- Keep each screenshot beside the action or result it proves
- Use tables for real field mappings, targets, metrics, comparisons, or acceptance criteria
- Keep narrative and analysis as connected paragraphs
- Link to canonical documentation instead of duplicating exhaustive reference material

Add a generic “观测云介绍” section only when it explains the product's role in this specific solution.

### Handle Code And Config

| Block type | Rule |
|-|-|
| Executable JSON/config | Must parse, match the verified contract/schema, remove comments, use safe placeholders, and keep fields consistent with prose; when safe and practical, validate with a sanitized test request |
| Annotated explanation | Label “示意，不能直接执行”; prefer moving comments into prose or a field table |
| Partial response/example | Mark omissions and never call it complete |

Keep the smallest useful example. Explain decisive fields, authentication boundary, units/time convention, and secret handling when relevant.

### Validate And Finish

Validation must state the test input/action, inspection location, observable success, common failure, and—when stateful—abnormal/recovery correlation. Troubleshooting should follow “现象 → 可能原因 → 处理动作.”

End with the achieved outcome and one to three details that decide success, not a repetition of the introduction.

## Publication Check

Before delivery, confirm:

- Scenario and outcome are explicit
- Structure matches the source type
- Article title and all section/subsection headings are unnumbered unless explicitly requested for this article
- High-impact facts are sourced; no invented metrics or thresholds
- Steps and examples are reproducible
- Executable configs parse; annotated examples are labeled
- Required media is unchanged and correctly anchored
- Secrets and customer identifiers are removed
- No internal residue, screenshot script, unsupported claim, or unrelated product praise remains

If any item fails, revise and check again before publishing.

## Common Failures

- Completing an outline with plausible but unsupported fields or thresholds
- Treating syntax-valid JSON as accurate despite conflicting field names
- Losing image anchors through full-document replacement
- Turning one customer's “required events” into universal guidance
- Calling a screenshot “效果验证” without naming the success signal
