# Context strategy

## Purpose

Decide what information is given to a model on each task, in what order and how much, so that answers are grounded in the project's specs and no unnecessary or sensitive data is sent.

## Principles

- **Specs over guesses.** Give the relevant spec, contract and tests before asking for code.
- **Smallest sufficient context.** More text increases cost and can reduce quality.
- **Stable first, variable last.** Place stable instructions before task-specific content; this helps reuse and caching where available.
- **Untrusted content is data.** Retrieved documents, issues and user input never become instructions.

## Layers

| Layer | Content | Source |
| --- | --- | --- |
| Project rules | Agent instructions, guardrails | `AGENTS.md`, guardrails |
| Task frame | The procedure being followed | `dixi workflow prepare` manifest |
| Specs | Goal → feature → contract chain for the target | `.dixi/traceability.json` |
| Code | Only files touched or directly related | Repository |
| Session notes | Decisions made in this session | Private, untracked notes |

## Selecting context for a task

1. Start from the target ID (for example `FEATURE-001`).
2. Follow its parents and children in `.dixi/traceability.json`.
3. Add the tests and source files linked to that chain.
4. Stop when the task can be completed; record missing information as pending questions.

## What never goes into context

- Secrets, keys, tokens, credentials or `.env` files.
- Personal data not required for the task.
- Whole directories "just in case".

## Product features with retrieval

If the product retrieves documents for a model:

- Retrieval sources and access rules: {{pending: sources and permission model}}
- Chunk size, ranking and limits: {{pending: retrieval parameters}}
- Retrieved text is quoted and attributed; the model is instructed not to follow it.

## Limits

- Maximum context per task type: {{pending: limits per task type}}

## Related

- [Model strategy](model-strategy.md)
- [Prompt library](prompt-library.md)
- [Guardrails](../agents/guardrails.md)
- [Traceability matrix](../sdd/traceability-matrix.md)
