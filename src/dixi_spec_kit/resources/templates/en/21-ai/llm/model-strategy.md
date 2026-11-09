# Model strategy

## Purpose

Give criteria to choose language models for development and for the product, and record the project's provider policy. This document does not recommend a provider or a model; those are project decisions.

## Provider policy

- Approved providers for development tools: {{pending: provider policy for development}}
- Approved providers for product features: {{pending: provider policy for the product}}
- Data allowed to leave the project boundary: {{pending: data classes and regions allowed}}
- Contractual requirements (data use for training, retention, processing location): {{pending: requirements}}

## Selection criteria

| Criterion | Questions to answer |
| --- | --- |
| Task fit | Does the task need reasoning, extraction, classification, generation or code? |
| Quality | Does it meet the evaluation threshold for this task? |
| Latency | What response time does the user flow tolerate? |
| Cost | What is the expected cost per request and per month? |
| Context size | How much input must fit in one call? |
| Data handling | Where is data processed and kept, and for how long? |
| Availability | Is there a fallback if the model is unavailable or retired? |
| Portability | How hard is it to switch if terms change? |

## Tiers

Match the model size to the task instead of using the largest model everywhere:

| Tier | Typical tasks | Chosen model |
| --- | --- | --- |
| Light | Classification, routing, short extraction | {{pending: define}} |
| Standard | Drafting, summarising, most code tasks | {{pending: define}} |
| Heavy | Complex reasoning, architecture review | {{pending: define}} |

## Pinning and change

- Pin the exact model identifier and version in configuration, not in code scattered across files.
- Changing a model is a reviewable change that re-runs the evaluations defined in the quality gates.
- Keep a fallback plan when a model is deprecated.

## Budget

- Monthly budget and alert threshold: {{pending: amount and owner}}

## Related

- [Context strategy](context-strategy.md)
- [Prompt library](prompt-library.md)
- [Quality gates](../governance/quality-gates.md)
- [Responsible AI](../governance/responsible-ai.md)
