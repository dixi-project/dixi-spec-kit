# AI audit trail

## Purpose

Make it possible to answer, after the fact, what an AI did in a change or in a product response, without storing secrets or unnecessary personal data.

## Principle

Record enough to reconstruct who decided what and with which evidence. Do not record what you would not want to leak.

## Scope 1 — AI that builds

Answering "what did the AI do in this change?":

1. **Pull request description**: which files or functions were generated with AI and where the author focused the review.
2. **Commits**: AI participation marked consistently (for example a co-author trailer); a person remains responsible for each commit.
3. **Tests**: the failing-test commit precedes the implementation; later edits to tests are visible in the diff and need a human reason.
4. **Reviews**: agent comments are labelled as such; human approvals reference the final revision.
5. **Checks**: `dixi check` and the project's real checks, with their observed result.

Convention for marking AI participation: {{pending: trailer, label or section used}}

## Scope 2 — AI inside the product

For each model call, consider logging:

| Field | Why |
| --- | --- |
| Request ID and timestamp | Correlate with application logs |
| Model identifier and version | Explain behaviour changes |
| Prompt template ID and version | Reconstruct the prompt from version control |
| Parameters (temperature, limits) | Reproduce conditions |
| Outcome (accepted, rejected, error) | Measure quality |
| Keyed hash of the input, if needed | Verify a reconstruction without storing raw text |

Do not log raw prompts that may contain personal data unless an approved exception exists.

## Never record

- Secrets, tokens or credentials.
- Raw personal data without a documented basis and retention.
- Full documents retrieved for context when an ID is enough.

## Retention

- Development trail: lives with the repository history.
- Product logs: {{pending: retention period and storage location}}

## Related

- [Responsible AI](responsible-ai.md)
- [Guardrails](../agents/guardrails.md)
- [Human in the loop](../agents/human-in-the-loop.md)
