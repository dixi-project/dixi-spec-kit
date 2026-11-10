# Architecture Decision Records

## Purpose

Index of the Architecture Decision Records (ADRs) of this project. An ADR captures one structural decision, the context that forced it, the options considered and the consequences accepted. ADRs explain *why* the architecture looks the way it does, so future contributors and agents do not reopen settled questions or silently break them.

## When to write an ADR

Write one when a decision is hard to reverse or affects more than one module, for example:

- Choosing a persistence model, messaging style or deployment topology.
- Defining a trust boundary, an authentication scheme or a tenancy model.
- Adopting or dropping a framework, protocol or external integration.
- Accepting a known limitation or technical debt on purpose.

Small, local choices belong in the module or feature spec instead.

## How to write one

1. Copy the [ADR template](../../10-engineering/templates/adr-template.md) to `ADR-NNN-short-title.md` in this folder, using the next free number.
2. Describe the context and the forces at play, not only the chosen option.
3. List at least two options with their trade-offs.
4. State the decision and its consequences, including what becomes harder.
5. Link the specs, contracts and tests the decision affects.
6. Add a row to the index below.

## Status lifecycle

| Status | Meaning |
|---|---|
| Proposed | Drafted, under discussion. Not binding yet. |
| Accepted | Validated by a human owner. Binding for all contributors and agents. |
| Superseded | Replaced by a newer ADR. Keep the file and link the replacement. |

A structural decision stays **Proposed** until a human validates it. Agents may draft ADRs and propose changes, but must not mark an ADR as Accepted on their own. Never delete or rewrite an accepted ADR: supersede it with a new one.

## Index

| ID | Title | Status | Date |
|---|---|---|---|
| [ADR-001](ADR-001-i18n-logic-in-plain-modules.md) | i18n logic in plain ES modules, no i18n library | Accepted | 2026-11-10 |

## Owners

- Who validates ADRs: the example owner (fictitious).
- Review cadence: when `/dixi.plan` proposes one.

## Related

- [Master spec](../../00-master-spec.md)
- [Agent instructions](../../AGENTS.md)
- [ADR template](../../10-engineering/templates/adr-template.md)
- [System context](../system-context.md)
- [Guide](../../docs/guide.md)
