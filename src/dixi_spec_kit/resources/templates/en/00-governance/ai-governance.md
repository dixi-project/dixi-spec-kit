# AI governance

## Purpose

Set how AI assistants and agents may take part in this project: what they may do alone, what needs a person, what is never delegated, and how their work is traced. It applies to any model or tool the project chooses.

Status: draft. {{pending: confirm the AI governance rules with the responsible person}}

## Principles

1. **Human accountability.** A named person owns every change, whoever drafted it.
2. **Transparency.** AI-assisted work is identifiable in the pull request or commit.
3. **Progressive autonomy.** Autonomy grows with evidence, never by default.
4. **Quality first.** AI output passes the same tests and reviews as human work.
5. **Privacy by design.** Secrets and personal data never reach an agent's context.

## Autonomy levels

| Level | Name | The agent may | A person must |
|-------|------|---------------|---------------|
| 0 | Assist | Suggest text or code on request. | Write and commit. |
| 1 | Draft | Create specs, tests and code on a branch. | Review every change before merge. |
| 2 | Execute | Run read-only commands and the local test suite. | Approve any command with side effects. |
| 3 | Operate | {{pending: decide whether any level 3 action is allowed}} | Supervise and be able to stop it. |

Current maximum level: {{pending: maximum autonomy level for this project}}

## Never delegated to an agent

- Signing commits or attestations.
- Approving or merging pull requests.
- Deploying or promoting `MODE`.
- Reading secrets, keys or `.env*` files.
- Editing committed (frozen) tests to make code pass.

## Allowed per action

| Action | Allowed level | Notes |
|--------|---------------|-------|
| Draft a feature spec | 1 | Structural stories need human validation first. |
| Write a red test | 1 | Committed alone before the implementation. |
| Implement code | 1 | Only to make existing tests pass. |
| Run `dixi check` and `make verify` | 2 | Report the real result. |
| Change dependencies | {{pending: level}} | Follow the dependency policy. |

## Traceability

- Record which tool and model assisted, in the pull request description.
- Keep the prompts that shaped structural decisions next to the spec. {{pending: where prompts are kept}}

## Review cadence

{{pending: how often these rules are reviewed and by whom}}

## Related

- [AI usage policy](policies/ai-usage-policy.md)
- [Human in the loop](../21-ai/agents/human-in-the-loop.md)
- [Guardrails](../21-ai/agents/guardrails.md)
- [Project instructions](../AGENTS.md)
- [Principles](principles.md)
