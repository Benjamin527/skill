---
name: summarize-customer-issue
description: Use when the user asks for a one-sentence summary, concise cause-and-effect recap, customer issue synopsis, support-ticket conclusion, or chat-ready technical incident update.
---

# Summarize Customer Issue

## Core rule

Produce exactly one concise Chinese sentence that starts with the customer's reported problem and then states the verified cause and resolution.

## Workflow

1. Extract the customer-visible symptom or question. Preserve important field names, thresholds, counts, error codes, and contrasts.
2. Extract the confirmed root cause. If it is only suspected, retain uncertainty with “初步判断” or “可能”。
3. Extract the proposed or completed resolution. Distinguish “需/建议” from “已通过”。
4. Return only this pattern, without a heading or explanation:

   `客户反馈【问题现象】，经排查【根因】，需/已通过【处理方案】。`

Never begin with the root cause when a customer symptom is available. Do not invent missing facts. If cause or resolution is absent, omit that clause rather than guessing.

## Example

Input context: `latency <= 10000` returns no data, while `latency <= 5000` returns two records; `latency` was ingested as a string; convert it to integer `latency_ms` in Pipeline.

Output: `客户反馈 latency ≤ 10000 查不到数据而 latency ≤ 5000 反而有值，经排查是 latency 以字符串存储导致范围条件按字典序比较，需通过 Pipeline 将其转换为整数 latency_ms 后再查询。`

## Common mistakes

- Mentioning only cause and fix while omitting the customer's original problem.
- Dropping the exact contrast, threshold, count, or error that makes the issue understandable.
- Turning one sentence into bullets, a multi-sentence explanation, or a new technical investigation.
