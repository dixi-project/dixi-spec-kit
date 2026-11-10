# Escalation matrix

## Purpose

Make clear who is called, in which order and how fast, for each incident level, so nobody has to improvise contacts during an outage.

Status: draft. {{pending: name the owner who keeps this matrix current}}

## Roles

| Role | Responsibility during an incident |
|------|-----------------------------------|
| First responder | Acknowledges the alert, classifies, starts mitigation |
| Incident lead | Coordinates, decides, owns the timeline |
| Communications lead | Writes internal and customer updates |
| Technical expert | Deep knowledge of the affected component |
| Executive contact | Business decisions, legal and public statements |

One person may hold several roles in a small team; write down who holds which.

## Matrix by level

| Level | Step 1 | Step 2 (if no ack) | Step 3 | Notify |
|-------|--------|--------------------|--------|--------|
| SEV1 | First responder, immediately | Incident lead after {{pending: minutes}} | Executive contact after {{pending: minutes}} | Communications lead at once |
| SEV2 | First responder | Incident lead after {{pending: minutes}} | Technical expert as needed | Communications lead if customers notice |
| SEV3 | First responder in business hours | Team lead next day | — | — |
| SEV4 | Backlog triage | — | — | — |

## Contacts

| Role | Primary | Backup | Channel |
|------|---------|--------|---------|
| {{pending: role}} | {{pending: person or rotation}} | {{pending: backup}} | {{pending: paging tool, phone, chat}} |

Use role addresses such as `oncall@example.com`, not personal ones, and keep personal phone numbers out of the repository.

## Rules

- Escalating early is never a mistake; staying silent is.
- If a step does not acknowledge in time, go to the next one without waiting.
- External parties (vendors, authorities, customers) are contacted only by the role named here.
- A suspected security or privacy incident also follows [incident response](../13-security/incident-response.md).

## Review

Test the matrix with a paging drill every {{pending: frequency}} and after every team change.

## Related

- [Incident levels](incident-levels.md)
- [Restore service](playbooks/restore-service.md)
- [Customer outage communication](playbooks/comms-outage-customer.md)
- [Incident response](../13-security/incident-response.md)
