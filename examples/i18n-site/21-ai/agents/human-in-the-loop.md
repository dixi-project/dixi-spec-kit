# Human in the loop

## Purpose

State where a person must decide, and why there and not everywhere. Asking for confirmation on every step trains people to click through; human gates belong where a mistake is expensive or irreversible.

## Where a person decides

- **What gets built**: approving specs, contracts and the tests that encode them.
- **What becomes shared or irreversible**: merging, releasing, migrating data, deleting.
- **When a rule is relaxed**: exceptions to guardrails or changes of project mode.
- **Structural decisions**: architecture, data model, external dependencies, providers.

## In development

| Moment | Agent may | Person must |
| --- | --- | --- |
| Spec drafted | Draft and check structure | Validate structural choices |
| Tests written | Draft failing tests | Review that they encode the criteria |
| Code ready | Run checks and report results | Read the diff and understand it |
| Pull request | Comment and summarise | Approve and merge |
| Release | Prepare notes | Decide and execute |

An agent's review is a useful input; it is never the approval.

## In the product

If a model can trigger actions for users:

1. The confirmation is issued by the server, not by the model, and is bound to the exact action and parameters.
2. If parameters change after confirmation, the confirmation is invalid.
3. Each confirmation is recorded (who, when, which action) without unnecessary personal data.
4. A test proves that an action without valid confirmation is rejected.

Actions that require confirmation: {{pending: list product actions that need human confirmation}}

## Anti-patterns

- Approving many agent changes in minutes without reading them.
- Accepting every prompt "yes to all"; if there are too many prompts, adjust permissions instead.
- Approving code nobody on the team can explain.
- An author approving their own change.

## Project decisions

- Minimum number of human reviewers: {{pending: number and role}}

## Related

- [Guardrails](guardrails.md)
- [AI audit trail](../governance/ai-audit-trail.md)
- [Methodology](../sdd/methodology.md)
- [Project instructions](../../AGENTS.md)
