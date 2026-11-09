# Business capabilities

## Purpose

Describe what the business must be able to do, independently of how it is implemented today.
Capabilities are stable over time (processes and systems change, the need remains), so they are a
good basis for drawing domain and module boundaries and for prioritizing investment.

## How to identify capabilities

1. Start from the strategic goals and value proposition: what must the organization do to deliver?
2. Name each capability with a noun phrase ("Customer onboarding", "Invoice management").
3. Group them in levels: level 1 is broad, level 2 breaks it into concrete abilities.
4. Do not name teams, tools or screens; those are implementations.
5. Mark how each capability differentiates the product: core, supporting or generic.

## Capability map

| ID | Level 1 | Level 2 | Type | Goal served | Domain |
|---|---|---|---|---|---|
| CAP-001 | {{pending: capability}} | {{pending: sub-capability}} | {{pending: core, supporting or generic}} | {{pending: GOAL ID}} | {{pending: domain}} |
| CAP-002 | {{pending: capability}} | {{pending: sub-capability}} | {{pending: type}} | {{pending: GOAL ID}} | {{pending: domain}} |

Core capabilities deserve custom design and the strongest tests. Generic ones are candidates for
reuse or for an external service (that choice is recorded as an ADR).

## Maturity and gaps

| Capability | Current state | Target state | Gap |
|---|---|---|---|
| {{pending: CAP ID}} | {{pending: manual, partial or automated}} | {{pending: target}} | {{pending: what is missing}} |

## Prioritization

- Capabilities in scope for the current period: {{pending: CAP IDs}}
- Deferred capabilities and reason: {{pending: CAP IDs and reason}}

## Related

- [Strategic goals](../strategic-goals.md)
- [Domain map](domain-map.md)
- [Ubiquitous language](ubiquitous-language.md)
- [Business goal](../vision.md)
