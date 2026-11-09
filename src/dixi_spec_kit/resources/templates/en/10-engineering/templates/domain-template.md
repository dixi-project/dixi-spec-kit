# Domain template

## Purpose

Describe one business domain: its language, core concepts, rules and boundaries, before splitting
it into modules. Copy the structure below into `03-domains/<domain>/domain-spec.md`.

## Template

```markdown
# DOMAIN-NNN — <domain name>

Status: draft | validated
Parent: GOAL-NNN
Domain expert: {{pending: person who validates the business language}}

## Purpose

The part of the business this domain covers and the goal it serves.

## Ubiquitous language

| Term | Definition | Not to be confused with |
|---|---|---|

## Core concepts

| Concept | Type (entity, value object, aggregate) | Identity | Lifecycle states |
|---|---|---|---|

## Business rules and invariants

| ID | Rule | Always true? |
|---|---|---|
| INV-1 | | yes |

## Domain events

| Event | When it happens | Data |
|---|---|---|

## Boundaries

- Inside this domain: ...
- Outside (owned by other domains): ...
- Relationships with other domains: {{pending: upstream, downstream, shared concepts}}

## Modules

- MODULE-NNN — ...

## Open questions

- ...
```

## Notes

- Use the business vocabulary; a developer and a domain expert should read it the same way.
- Invariants become tests in the modules that implement them.

## Related

- [Example domain](../../03-domains/example/domain-spec.md)
- [Module template](module-template.md)
- [Flow template](flow-template.md)
