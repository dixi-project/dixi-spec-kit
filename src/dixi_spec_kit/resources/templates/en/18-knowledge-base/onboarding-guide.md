# Onboarding guide

## Purpose

Help a new person (or a newly configured agent) become productive in this project safely: what is non-negotiable, what to set up, how daily work flows and when to stop and ask.

Status: draft. {{pending: name the onboarding buddy or contact}}

## Non-negotiables

- Specs lead; tests come first; committed tests are frozen.
- A person reviews and merges every change. Agents never sign, approve, merge or deploy.
- No secrets in the repository, prompts or logs.
- User-facing text lives in translation catalogs.

## Prerequisites

- [ ] Repository access with your own identity.
- [ ] The DIXI Spec Kit CLI installed (`dixi --version`).
- [ ] {{pending: language runtime and tools for this project}}
- [ ] Access to the team channel: {{pending: channel}}

## Setup

1. Clone the repository and create a branch: `feat/<topic>`.
2. Run `dixi doctor` and `dixi check`.
3. Run `make verify` and note the result.
4. Read [AGENTS.md](../AGENTS.md) and the [documentary workflow](../docs/guide.md).

## Reading path (first day)

| Order | Document | Why |
|-------|----------|-----|
| 1 | [Project](../00-master-spec.md) | Scope and decisions |
| 2 | [Business goal](../01-business/vision.md) | Why the project exists |
| 3 | [Principles](../00-governance/principles.md) | How trade-offs are made |
| 4 | [Testing policy](../00-governance/policies/testing-policy.md) | Rules for tests |
| 5 | [Glossary](glossary.md) | Shared vocabulary |

## Daily flow

1. Pick a task linked to a feature spec.
2. Read the spec and its criteria; ask about anything unclear.
3. Write and commit a red test.
4. Implement until green; refactor.
5. Run `make verify`; open a pull request with the real result.

## When to stop and ask

- The spec is ambiguous or contradicts a test.
- A change touches security, personal data, payments or permissions.
- You would need to edit a committed test.
- A tool asks for a secret or wider access.

## First task

{{pending: a small, well-specified first task for newcomers}}

## Related

- [FAQ](faq.md)
- [Glossary](glossary.md)
- [Decision log](decision-log.md)
- [Engineering standards](../00-governance/engineering-standards.md)
