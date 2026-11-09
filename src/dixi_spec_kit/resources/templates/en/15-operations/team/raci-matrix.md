# RACI matrix

## Purpose

Make explicit who is Responsible, Accountable, Consulted and Informed for the main operational activities, so decisions do not stall and work is not done twice.

Status: draft. {{pending: name the owner of this matrix}}

## Legend

- **R** Responsible: does the work.
- **A** Accountable: makes the final decision; exactly one per activity.
- **C** Consulted: gives input before the decision.
- **I** Informed: told after the decision.

## Roles

{{pending: replace with the roles the project really has}}

| Short name | Role |
|------------|------|
| PO | Product owner |
| TL | Tech lead |
| ENG | Engineering team |
| OPS | Operations / on call |
| SEC | Security contact |
| SUP | Support |
| FIN | Finance contact |

## Matrix

| Activity | PO | TL | ENG | OPS | SEC | SUP | FIN |
|----------|----|----|-----|-----|-----|-----|-----|
| Production deployment | I | A | R | C | I | I | — |
| Incident response | I | C | R | A | C | I | — |
| Customer outage communication | A | C | — | C | — | R | — |
| Security incident | I | C | R | C | A | I | — |
| Vendor onboarding | A | C | — | C | C | — | C |
| Budget and cost review | A | R | C | C | — | — | C |
| Manual refunds | I | — | — | — | — | R | A |
| Maintenance windows | C | A | R | R | — | I | — |
| Access reviews | I | R | — | C | A | — | — |

These assignments are examples; adjust every cell. {{pending: confirm each row with the people named}}

## Rules

- One A per row. If two people feel accountable, the matrix is not finished.
- An AI agent is never A and never the only R for a production action.
- Update the matrix when someone joins, leaves or changes role.

## Related

- [On-call rotation](on-call-rotation.md)
- [Escalation matrix](../escalation-matrix.md)
- [Support model](../support-model.md)
- [Service catalog](../service-catalog.md)
