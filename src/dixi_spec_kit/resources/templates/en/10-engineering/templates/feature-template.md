# Feature template

## Purpose

Describe one feature with observable acceptance criteria, traced to its module and to the tests
that prove it. Copy the structure below into `05-features/<feature>/feature-spec.md`.

## Template

```markdown
# FEATURE-NNN — <feature name>

Status: draft | ready | in progress | done
Parent: MODULE-NNN
Owner: {{pending: person responsible for this feature}}

## Purpose

The user or business need this feature solves, in two or three sentences.

## Scope

- In scope: ...
- Out of scope: ...

## User stories

- As a <role>, I want <capability>, so that <benefit>.

## Acceptance criteria

Each criterion is observable and testable.

1. Given <context>, when <action>, then <observable result>.
2. Given ..., when ..., then ...

## Business rules

| ID | Rule | Source |
|---|---|---|
| BR-1 | | |

## Contracts and data

- Contracts touched: CONTRACT-NNN
- Data created, read or changed: {{pending: entities and fields}}

## Non-functional requirements

- Performance: {{pending: target response time or throughput}}
- Security and privacy: authorization rules, personal data involved.
- Accessibility and languages: supported locales, accessibility level.

## Risks and open questions

- ...

## Tests

| Criterion | Test ID | Type |
|---|---|---|
| 1 | TEST-NNN | unit / integration / acceptance |
```

## Notes

- Write the tests from the acceptance criteria before the implementation.
- Register the feature and its parent in `.dixi/traceability.json`.

## Related

- [Example feature](../../05-features/example/feature-spec.md)
- [Example module](../../04-modules/example/module-spec.md)
- [Test plan](../../11-quality/test-plan.md)
- [ADR template](adr-template.md)
