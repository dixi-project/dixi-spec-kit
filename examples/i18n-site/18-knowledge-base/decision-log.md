# Decision log

## Purpose

Record the project's decisions that are not big enough for an ADR but must not be lost (scope cuts, conventions, accepted risks, exceptions), and say where each kind of decision lives.

Status: draft. {{pending: name who keeps this log up to date}}

## Where each decision lives

| Kind of decision | Where it is recorded |
|------------------|----------------------|
| Architecture, hard to reverse | ADR in [09-architecture/adr](../09-architecture/adr/README.md) |
| Scope and priorities | [Project](../00-master-spec.md) |
| Feature behaviour | The feature spec |
| Interface | The contract |
| Small, reversible, cross-cutting | This log |
| Exceptions to a policy | This log, with expiry date |

## Rules

- One row per decision; never rewrite a past row. Supersede it with a new one.
- Every decision has a date, an owner and the alternatives considered.
- Agents may propose entries; a person confirms them.
- If a decision turns out to be hard to reverse, promote it to an ADR.

## Log

| ID | Date | Decision | Alternatives | Owner | Status | Supersedes |
|----|------|----------|--------------|-------|--------|------------|
| DEC-001 | {{pending: date}} | {{pending: decision}} | {{pending: alternatives}} | {{pending: owner}} | proposed | — |

Status values: `proposed`, `accepted`, `superseded`, `expired`.

## Review

{{pending: how often the log is reviewed, and who checks expired exceptions}}

## Related

- [ADR template](../10-engineering/templates/adr-template.md)
- [FAQ](faq.md)
- [Principles](../00-governance/principles.md)
