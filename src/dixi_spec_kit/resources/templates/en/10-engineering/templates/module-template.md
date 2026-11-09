# Module template

## Purpose

Describe one module: its responsibility, the data it owns, the interfaces it exposes and its
dependencies. A module is a unit of code with clear boundaries inside a domain. Copy the structure
below into `04-modules/<module>/module-spec.md`.

## Template

```markdown
# MODULE-NNN — <module name>

Status: draft | active | deprecated
Parent: DOMAIN-NNN
Owner: {{pending: team or person responsible}}

## Purpose

What this module is responsible for, and what it explicitly is not.

## Responsibilities

- ...

## Owned data

| Entity | Key fields | Notes (personal data, retention) |
|---|---|---|

Only this module writes its data; others read it through its interfaces.

## Public interfaces

| Type (API, event, function) | Name | Contract |
|---|---|---|
| API | | CONTRACT-NNN |
| Event published | | |
| Event consumed | | |

## Dependencies

| Depends on | Why | Failure behavior |
|---|---|---|

## Business rules

| ID | Rule |
|---|---|

## Non-functional requirements

- Availability and latency targets: {{pending: targets}}
- Security: authorization model, sensitive data.

## Features

- FEATURE-NNN — ...

## Code location

{{pending: path of the module in the repository}}
```

## Related

- [Example module](../../04-modules/example/module-spec.md)
- [Domain template](domain-template.md)
- [Feature template](feature-template.md)
- [Package structure standard](../package-structure-standard.md)
