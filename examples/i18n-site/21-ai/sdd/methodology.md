# SDD methodology

## Purpose

Describe how this project applies spec-driven development (SDD): every change starts from a written, linked specification, is proven by tests written first, and ends with human review. This file explains the method; project-specific choices stay marked as pending until a responsible person decides them.

## Principles

1. **Spec first.** No code without a spec that states the expected behaviour and its acceptance criteria.
2. **Linked specs.** Each spec names its parent: goal → domain → module → feature → contract → test. Links are registered in `.dixi/traceability.json`.
3. **Tests first.** Tests derived from the contract are written and seen failing before the implementation. Frozen tests are never edited to make code pass.
4. **Living documentation.** When behaviour changes, the spec changes in the same pull request.
5. **Human accountability.** Agents draft, check and propose; a person validates structural decisions, signs, approves and merges.

## The cycle

| Step | Input | Output | Who decides |
| --- | --- | --- | --- |
| Discover | A need or idea | Goal and scope in `01-business/vision.md` | Responsible person |
| Specify | Approved goal | Domain, module and feature specs | Person, assisted by an agent |
| Contract | Feature spec | Contract with inputs, outputs and errors | Person validates |
| Test | Contract | Failing tests that encode the criteria | Agent drafts, person reviews |
| Build | Failing tests | Code that makes them pass | Agent or person |
| Verify | Code and tests | `dixi check` plus the project's real checks | Automated, reported honestly |
| Review | Pull request | Approval and merge | Person only |

## Working with agents

- Use `dixi workflow list` to see shared procedures and `dixi workflow prepare <name>` to gather context before asking an agent to act.
- In agent integrations the same procedures appear as `/dixi.*` commands or `$dixi-*` skills; for AI-specific guidance use `/dixi.ai` or `$dixi-ai`.
- An agent's review is input for the human reviewer, never a substitute for it.

## Project decisions

- Depth of specs required before building: {{pending: minimal, standard or full spec depth per risk level}}
- Who validates structural decisions: {{pending: name the role or person}}
- Which changes may skip a feature spec (for example typo fixes): {{pending: list allowed exceptions}}

## Related

- [Spec lifecycle](spec-lifecycle.md)
- [Traceability matrix](traceability-matrix.md)
- [Validation rules](validation-rules.md)
- [Adoption guide](adoption-guide.md)
- [Project guide](../../docs/guide.md)
- [Master spec](../../00-master-spec.md)
