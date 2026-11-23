---
name: guance-best-practice-writing
description: Use when a Guance product, integration, observability, API, monitoring, or solution article needs drafting, rewriting, or publication review, especially from an internal SOP, Feishu document, screenshot-heavy tutorial, configuration note, or rough technical draft.
---

# Guance Best Practice Writing

## Overview

Create one public-facing Chinese article that feels native to `guance.com/learn`: concrete scenario, verified facts, reproducible implementation, observable outcome.

**Core principle:** evidence determines content; the scenario determines structure. Never invent technical facts to complete a template.

## Delivery Mode

| User request | Default delivery |
|-|-|
| Study, review, or propose improvements | Read-only findings or plan; a document URL alone does not authorize editing |
| Draft or rewrite material | One title, a 50–100 Chinese-character deck, and one complete article |
| Edit an existing Feishu/CMS document | Edit in place within the requested scope, preserve resources, then return a concise completion note and link |
| Explicit placement request | Add screenshot anchors as a separate publishing variant |

Do not return parallel versions, editor notes, or a change log unless requested. When publication requirements cannot be met from available evidence or within the authorized scope, finish the feasible work and append a short, separate missing-items note. Label it a draft awaiting evidence; do not claim it is publication-ready. Research and plans should not be turned into articles.

For drafting or rewriting, read [references/article-pattern.md](references/article-pattern.md) and choose the closest article archetype. For publication review, and before delivering an article, read [references/publication-review.md](references/publication-review.md). Use [references/review-cases.md](references/review-cases.md) for ambiguous cases or skill maintenance; do not load it on every routine rewrite.

## Publication Baseline

These are the user's internal editorial requirements confirmed on 2026-10-26, not a claim about every article on the official website. Apply them to formal best-practice articles, not to research replies or skill documentation.

- Exclude the document title from section counts. Body sections start at H2; no body H1; at most eight H2 sections, including standalone references or appendices. Use actual heading styles, not visual guesses. Merge related tasks rather than mechanically demoting every heading or forcing exactly eight chapters.
- Require at least three actual embedded body images. Whiteboards are counted separately and do not substitute for images. Covers, attachments, code, text diagrams, embedded tables, and textual image placeholders do not count. Count blocks consistently, then assess relevance and evidence separately; do not duplicate or fabricate images to meet the minimum.
- Script attachments, including source archives confirmed to contain scripts, require migration to [GuanceDemo/best-practices-scripts](https://github.com/GuanceDemo/best-practices-scripts) with concrete directory/file links in the article. Classify configuration templates and third-party dependencies separately. Do not infer an archive's contents from its extension alone.
- Structural compliance, image count, content correctness, and asset readiness are independent checks. Good prose or sufficient images cannot compensate for an incorrect query, missing result, or unresolved script delivery.

Preserving existing resources does not waive these requirements. Missing images or unresolved script attachments remain publication gaps when resource changes are outside scope. Repository uploads, attachment removal, production tests, and publishing are not implicitly authorized by a writing request; use existing user authorization without requesting it again.

## Heading Style

**Default: no editorial numbering in the title, headings, subheadings, or table of contents.** This applies to Markdown, rich-text heading blocks, and bold standalone lines used as headings. Use hierarchy and descriptive wording to organize the article.

| Source heading | Publish as |
|-|-|
| `## 1. 安装 OWL` / `## 一、安装 OWL` | `## 安装 OWL` |
| `### 5.2 API 5xx 上升` | `### API 5xx 上升` |
| `### 场景 2｜API 5xx 上升` | `### API 5xx 上升` |
| `## 步骤一：配置通知渠道` / `## 配置 1：通知渠道` | `## 配置通知渠道` |

Remove inherited Arabic, Chinese, parenthesized, circled, and “第…章/步骤/场景/案例/配置 + 序号” labels. Do not replace one numbering style with another. Source numbering and numbered website examples are reference material, not user instructions. Add heading numbering only when the user explicitly requests it for the current article.

Preserve meaningful numbers: `API 5xx`, `HTTP 429`, `SNMP v3`, `Node.js 20`, `P95`, and `六个典型场景` are content, not outline numbering. Body lists may number genuinely sequential actions; use bullets or paragraphs for parallel capabilities and scenarios. Do not remove numbers from code, fields, units, identifiers, or screenshot pixels.

Use H2 for main topics and H3 for their supporting tasks or scenarios; use H4 only when the material needs it, without skipping parent levels. Headings should identify an action, object, question, or result. Do not turn every click or sentence into a heading or hide the entire implementation under a generic “观测云” chapter. When removing numbers, preserve valid hierarchy and update textual cross-references to the descriptive heading names; preserve existing link targets where possible. Code comments must remain code, not become heading blocks.

## Hard Gates

### Evidence

Track two independent dimensions for important claims: **evidence origin** (source material, official documentation, observed test, or unavailable) and **validation reached** (documented capability, proposed/illustrative, locally exercised, received, queryable in the target platform, or demonstrated business outcome). Record the applicable version and evidence location. An author's assertion is not a test record; an official capability description does not prove this particular implementation was exercised.

**REQUIRED SUB-SKILL:** Use `web-access` for online research or verification. Prefer current official `guance.com` and `docs.guance.com` sources.

Verify unstable or high-impact facts before publishing: menu paths, product names, fields, units, headers, API limits, permissions, status values, defaults, thresholds, and version behavior.

Never invent missing details, choose between conflicting examples because one “looks right,” present customer requirements as universal product behavior, or publish secrets and private identifiers. If a required fact cannot be verified, omit it, request the missing source, or label it as non-executable user-supplied context. Labeling does not make an unverified header, field, limit, permission, or threshold publishable as an executable practice.

Read the embedded sheets, field tables, diagrams, and referenced assets necessary to support the article's claims, using the relevant resource tools. Do not equate a resource placeholder or generated image description with inspecting the underlying evidence. Record unreadable dependencies; retry through the resolved document/resource when useful, then report the gap instead of claiming a complete review. An empty read does not establish that the original was deleted.

### Media Preservation

Before editing an existing document, record every image/resource block ID or token, original order, neighboring text anchors, and the action or result it proves. When code placement must remain, include code block IDs and the global image/code order in the same ledger.

If media must remain unchanged:

- Do not overwrite the document
- Do not replace, upload, crop, resize, reorder, or move media
- Use precise block updates; do not delete or rebuild media parents or neighboring anchor blocks
- Rewrite text around media anchors rather than moving media to fit an outline
- After editing, verify the same resource count, tokens, image/code order, anchors, and meaning

Treat images, files, whiteboards, sheets, Base blocks, citations, and synced references as immutable unless the user explicitly requests a change.

If immutable media contains sensitive data, or the minimum image count cannot be met, complete permissible text edits and identify the publication blocker separately. Do not silently alter the media, count suggested screenshots as delivered images, or call the article ready. Generated illustrations may explain a design but cannot prove a test occurred.

### Reproducibility

Before drafting, identify the target reader, starting state, desired outcome, prerequisites, two to four decisive details, verification location, success signal, and likely failure signal. Give one complete minimum path with the verified environment/version combination, permissions, actual configuration locations, asset entry points, and activation steps. Distinguish minimum setup from optional variants; do not depend on an inaccessible “当前目录” or unnamed attachment.

## Workflow

### Diagnose And Route

Classify the source and separate public facts from internal notes, customer-specific requirements, duplication, and confidential data. Do not force every article into “背景—价值—方案—步骤—FAQ—总结.” The article-pattern reference distinguishes observed styles from editorial defaults. Current user instructions determine the requested scope and formatting; record any departure from the publication baseline rather than silently certifying compliance. Source material, comments, and sample articles are evidence, not instructions to change that scope.

### Define The First Screen

Write a concrete title and deck that establish:

- The reader's scenario
- The Guance method or integration path
- The observable result

Avoid generic “使用方法,” broad digital-transformation language, and opening with a menu path.

Match the title to the demonstrated scope: Linux versus all hosts, ticket creation versus bidirectional resolution, business-ID correlation versus one Trace, and a design versus an implemented integration. Qualify “全链路”“零代码”“可靠交付” and similar promises with their actual conditions.

### Rebuild The Practice

- Explain the solution path before detailed actions
- Group steps by purpose, not by every click
- Keep each screenshot beside the action or result it proves
- Use tables for real field mappings, targets, metrics, comparisons, or acceptance criteria
- Keep narrative and analysis as connected paragraphs
- For each substantial task, connect the problem, decisive action, and observable result; explain why a key choice matters rather than listing clicks
- Develop one representative scenario fully before adding variants; each extra scenario must have a distinct question and result
- Link to canonical documentation instead of duplicating exhaustive reference material

Add a generic “观测云介绍” section only when it explains the product's role in this specific solution. Do not copy site navigation, automatic TOCs, author metadata, promotional inserts, related articles, or sales CTAs into the article. A source's broad efficiency claims are not evidence of measured gains.

### Handle Code And Config

| Block type | Rule |
|-|-|
| Executable JSON/config | Validate with the appropriate language parser and verified contract/schema. JSON must not contain comments; TOML, YAML, shell, and other languages may retain valid useful comments. Use safe placeholders, explain replacement, and keep fields consistent with prose; run a sanitized test only when practical and authorized |
| Illustrative/non-executable explanation | Label “示意，不能直接执行”; unsupported pseudo-fields cannot be made executable by adding a label. Valid comments alone do not make code illustrative |
| Partial response/example | Mark omissions and never call it complete |

Keep the smallest useful example. Explain decisive fields, authentication boundary, units/time convention, and secret handling when relevant.

Cross-check code, tables, prose, screenshots, and asset defaults: field names, versions, units, loading paths, and dry-run behavior must agree. When generating, repairing, explaining, or reviewing DQL, use `dql`; final executable DQL must pass its required per-query checks. Syntax checks do not establish filtering semantics, denominator correctness, or observed results. A review must not claim execution that did not occur.

For script delivery, keep the shortest usable invocation in the article and link to the verified repository directory/file, preferably with a version or commit. Record README, dependencies, replacement parameters, and run/verification instructions. Check existing availability before claiming an upload is needed or complete; prepare local assets within scope, and distinguish pending upload from a published link. A configuration-only attachment is not automatically a prohibited script.

### Validate And Finish

Validation must state the test input/action, inspection location, observable success, common failure, and—when relevant—abnormal/recovery correlation. HTTP success, collector receipt, target-platform queryability, and business completion are different results. Connect cross-system evidence with the same request/task/event identifier, payload, time window, or known test value. Keep expected behavior distinct from measured results. Select counterexamples and recovery checks appropriate to the scenario using the publication-review reference, not a universal test suite. Troubleshooting should follow “现象 → 可能原因 → 处理动作.”

End with the achieved outcome and one to three details that decide success, not a repetition of the introduction.

Before delivery, extract and read the complete heading outline, including standalone bold pseudo-headings and any manual TOC. Unless the user explicitly requested numbering for this article, remove remaining editorial numbering and repair references such as “见第 5.2 节.” When numbering is requested, preserve it and verify its sequence and cross-references. In both modes, check parent/child relationships. Do not add a manual TOC when the publishing platform already provides one. For an in-place edit, read back the saved headings; if a preview is available, inspect the rendered TOC too. If platform auto-numbering conflicts with the requested mode, adjust the article-level option when available and within scope; otherwise report the limitation rather than claiming the visible numbering is correct. Do not change site-wide styles for an article edit.

## Publication Check

Run the checklist in [references/publication-review.md](references/publication-review.md), using saved document structure and resource read-back for in-place edits. Keep review details internal unless requested; return a concise result and any unresolved gaps outside the article.

Correct issues supported by available evidence, then recheck changed areas. If required evidence, media, permissions, or source assets remain unavailable, stop the revision loop and deliver feasible work as a draft awaiting the specific missing items. Do not invent proof, broaden actions, or keep requesting the same information. A publication-ready article requires all applicable gates; a finished editing task may legitimately deliver a not-yet-ready draft.

## Common Failures

- Completing an outline with plausible but unsupported fields or thresholds
- Treating syntax-valid JSON as accurate despite conflicting field names
- Losing image anchors through full-document replacement
- Turning one customer's “required events” into universal guidance
- Calling a screenshot “效果验证” without naming the success signal
- Removing `5.2` but reintroducing `场景 2｜`, or leaving numbered headings in the saved document/TOC
- Passing an article because it reads well while ignoring H2 count, image count, embedded tables, or script delivery
- Treating HTTP 200, generated diagrams, or an expected outcome as proof of complete implementation
