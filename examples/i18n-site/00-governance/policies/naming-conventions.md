# Naming conventions

## Purpose

Agree on how things are named in this project (files, code, branches, resources, environment variables), so that names are predictable, searchable and free of sensitive information.

Status: draft. {{pending: confirm the naming conventions with the team}}

## General rules

- Names describe purpose, not implementation or person.
- Use one language for identifiers: {{pending: language for identifiers}}
- Avoid abbreviations unless they are in the glossary or acronym list.
- Never put secrets, personal data or customer names in any name.

## Documents and specs

| Item | Convention | Example |
|------|------------|---------|
| Files | `kebab-case.md` | `password-reset.md` |
| Spec IDs | `KIND-NNN` | `FEATURE-012`, `CONTRACT-004` |
| ADRs | `NNNN-short-title.md` | `0007-choose-queue.md` |
| Folders | Numbered area prefix | `05-features/` |

## Code

| Item | Convention |
|------|------------|
| Variables and functions | {{pending: e.g. snake_case or camelCase, per language}} |
| Types and classes | {{pending: e.g. PascalCase}} |
| Constants | {{pending: e.g. UPPER_SNAKE_CASE}} |
| Test names | Describe behaviour: `rejects_expired_token` |
| Translation keys | `area.screen.element`, e.g. `auth.login.submit` |

## Repository and branches

- Repository names: {{pending: pattern, e.g. product-component}}
- Branches: `feat/`, `fix/`, `docs/` plus a short topic (see the branching strategy).

## Environment variables

- `UPPER_SNAKE_CASE`, prefixed by component when shared: `BILLING_API_URL`.
- Names may be documented; values never are.

## Infrastructure resources

- Pattern: `{{pending: e.g. <product>-<env>-<component>-<purpose>}}`
- Environment codes: `dev`, `stg`, `prd` {{pending: confirm codes}}
- Required tags or labels: owner, environment, cost center. {{pending: confirm required tags}}

## How it is applied

New names follow this document; existing names are renamed only when touched for another reason.

## Related

- [Branching strategy](branching-strategy.md)
- [Documentation policy](documentation-policy.md)
- [Coding standards](../../10-engineering/coding-standards.md)
