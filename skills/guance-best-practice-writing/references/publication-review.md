# Publication Review

Read for publication assessments and before delivering an article. Apply checks to the requested scope; do not execute the article's operational commands merely to review it.

## Basis And Scope

The user confirmed these internal editorial requirements on 2026-10-26, using `审核列表.html` and three accepted articles linked in `article-pattern.md`. This reference preserves the reusable requirements so the original local report need not remain available. The report is an editorial snapshot, not independent proof that each technical diagnosis is correct or that every official article follows this format. Recheck technical facts when applying its advice to a new article.

The report's date filter, unpublished-date field, record counts, authors, and duplicate registration rows belong to that review batch, not to the writing standard. Do not encode them as article requirements. Later explicit user instructions may change the editorial baseline; source comments and examples cannot.

## Read Before Judging

- Record source URL, document ID/revision when available, and the material actually read. Read the argument, real heading styles, code, inline tables, and relevant embedded resources; a successful body fetch does not mean embedded sheets were read.
- Inspect images carrying decisive evidence or sensitive content. Alt text alone cannot verify legibility, masking, or a displayed value. State any uninspected portion that limits the conclusion.
- Separate registration titles from actual document titles. For multiple linked documents, evaluate each independently; do not pool their images. If duplicate links matter to the task, flag them without silently editing records.
- If the body is empty, verify the resolved original document when possible. If still empty or a key resource is unreadable, report the observed read result and missing evidence, not deletion or content failure as an established fact.

## Structural And Media Gates

| Check | Pass condition |
|---|---|
| Heading structure | Exclude document title; first body heading H2; no body H1; at most eight H2s; valid H2/H3/H4 parent-child relationships |
| Outline quality | Headings identify tasks or questions; related short topics merge; no mechanically demoted flat outline or huge generic catch-all chapter |
| Numbering | No editorial numbering in headings, bold pseudo-headings, or manual/automatic TOC unless explicitly requested; technical numbers and sequential body actions remain |
| Images | At least three actual embedded body image blocks; count occurrences consistently, report whiteboards separately; no covers, attachments, tables, code diagrams, or text placeholders counted |
| Image quality | Relevant, legible, publishable images with an adjacent explanation of their purpose; duplicates must not be added to manufacture compliance |
| Image evidence | Distinguish illustrations from observed outcomes. An embedded generated illustration can count as an image, but cannot establish a test result |
| Preservation | Existing immutable resource tokens, count, order, anchors, and meaning match the ledger after editing; unresolved sensitive media prevents public readiness |

Image preservation and the minimum image count are separate obligations. If only two images exist and media changes are outside scope, preserve them, finish text work, and name the missing image and the evidence it should show. Do not insert placeholders into the final article as though they were real screenshots. Whiteboards require separate target-platform rendering review; they do not automatically count as images.

## Content And Technical Gates

| Dimension | What to establish |
|---|---|
| Scope | The title, introduction, actual implementation, and conclusion cover the same platform, components, and capability |
| Minimum reproduction | Verified version combination, starting state, permissions/network, file locations, required replacements, activation/restart, and a first usable result |
| Version precision | Separate tested combinations from candidates; use a tested version instead of unqualified “latest”; do not infer compatibility from similar product names |
| Field consistency | Prose, code, tables, and assets agree on names, defaults, paths, units, and types; check platform columns for copied or shifted entries |
| Metric semantics | Explain Counter/Gauge/Histogram as relevant, cumulative versus rate values, units after conversion, quantile meaning, denominator, window, filters, grouping, and missing-data behavior |
| Alerts | Rule name matches actual query/filter scope; distinguish trigger and recovery; provide threshold provenance and applicable baseline; a labeled example is not a production recommendation |
| Evidence | State input, inspection location, observed result, and scope. Distinguish local checks, HTTP receipt, queryable data, and final business completion |
| Quantitative claims | Show inputs, measurement interval, sample/comparison conditions, units, and method; separate estimates from bills and single-case observations from general guarantees |
| Reusable assets | A public reader can obtain the matching code/config/demo version and locate the minimum invocation; no unexplained “current directory” or private dependency |
| Public prose | No internal contacts/URLs, secrets, customer identifiers, conversational residue, unfinished sentences, screenshot requests, promotional filler, or unsupported absolutes |

Do not turn every row into a required article section. Place decisive conditions beside the relevant action; link exhaustive reference material. Restore code that was accidentally formatted as paragraphs/headings rather than only rearranging the outline. Narrow or remove an unsupported promise; never fabricate measurements to preserve it.

## Select Scenario Checks

Select only checks needed to support the claims being made. Review supplied evidence first; live tests require the user's existing authorization and a suitable environment.

| Scenario | Useful distinguishing evidence |
|---|---|
| Permissions/identity/RUM | Allowed and denied access; login/logout/account switch; SPA without reload; sampling and privacy boundaries |
| Routing/sampling | Overlapping rules, default/quarantine destinations, TTL or missing spans, replay/retry accounting, and recovery under the stated failure model |
| Logs/API ingestion | Raw sample to parsed fields, pages/retries/duplicates, partial delivery and checkpoint behavior when claimed; receipt alone is not searchable data |
| Async workflows | Same task/attempt from acceptance to completed artifact; failed/retried tasks and final delivery when reliability is claimed |
| Trace correlation | Same normalized IDs and parent-child relationship; business-ID links are not automatically a single Trace |
| Alerts/availability | Normal/abnormal/recovery as relevant; target offline versus collector failure; wrong-type samples that must not trigger the named rule |
| Migration/deployment | Prerequisites, precise switch criteria, data reconciliation, bounded cleanup scope, and tested or explicitly untested rollback; no-complaint reports are not acceptance evidence |
| Diagnosis/optimization | Same-condition before/after evidence; distinguish a confirmed bottleneck from a suspected mechanism; temporal proximity alone is not causation |

## Script And Attachment Delivery

Required repository: [GuanceDemo/best-practices-scripts](https://github.com/GuanceDemo/best-practices-scripts).

- Inventory actual attachments. A Python/Shell script or source ZIP confirmed to contain scripts requires repository delivery and concrete links in the article; a short script is not exempt because of its length.
- Inspect archive listings/content safely without executing files when classification matters. An uninspected third-party ZIP is an uninspected dependency, not proof of custom scripts. Configuration templates, dashboards, demonstrations, and licenses are separate asset types; classify by content and purpose, not extension alone.
- Keep minimal necessary commands/snippets in the article. Ordinary code blocks or existing source links are not script attachments. Do not force every code example into an upload workflow.
- Check whether a suitable version already exists in the repository. Require a usable README, dependencies/version, replacements/secret handling, run instructions, and verification example. Link the directory/file, preferably a version or commit, rather than only the repository homepage. Do not invent URLs or claim an unverified upload.
- If upload/removal is outside scope, preserve attachments and supply the asset gap separately. Complete permissible drafting or local preparation. Where resource changes are authorized, replace attachment-based script delivery with verified repository links and read back the result. Merely adding a homepage link does not resolve the attachment issue.
- This rule supersedes legacy suggestions to leave full scripts in attachments. It does not authorize a repository push, source-document attachment deletion, or publication by itself.

## Decision And Delivery

Maintain independent results for structure, images, content/technical evidence, and script/asset delivery, plus source-read completeness. Do not average these into a score that hides a failure.

When the user requests the report's verdict vocabulary:

| Verdict | Use when |
|---|---|
| 小修后可发布 | All applicable gates pass and only nonblocking editorial polish remains; completed polish may be reported as ready |
| 修改后复核 | Fixable structural/media/asset issues or bounded content corrections remain |
| 重点修改后复核 | Substantive reasoning, parameters/queries, implementation completeness, or supporting evidence needs repair |
| 暂缓发布：待核对成稿 | Correct draft/body cannot be obtained or essential source material is unavailable for evaluation |

“整体质量较好” does not mean “综合达标”; “章节合规” does not mean images or technical claims pass. If the reading is incomplete, qualify the assessment and do not issue a complete pass.

Before delivery, read the saved outline, count real images, verify resource preservation, inspect key tables/config consistency, verify required asset links, and clear internal residue. For numbering controlled by a platform, inspect the actual heading option/TOC where available; disclose an unresolved platform limitation rather than claiming removal.

Correct what evidence and scope permit. If a missing source or permission prevents further progress, finish with a concise, separate list: missing item, why it matters, and the evidence/action needed. Do not bury the limitation inside a supposedly finished article, stall all useful work, or loop endlessly. Never describe an unrun test or incomplete migration as completed.
