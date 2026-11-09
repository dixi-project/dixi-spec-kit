# Support model

## Purpose

Describe how users get help, who answers, how requests move between support tiers and what response times the project commits to.

Status: draft. {{pending: name the owner of the support model}}

## Channels

| Channel | Audience | Hours | Owner |
|---------|----------|-------|-------|
| {{pending: e.g. help centre}} | All users | Always available | {{pending: role}} |
| {{pending: e.g. support@example.com}} | All users | {{pending: hours and time zone}} | {{pending: role}} |
| {{pending: e.g. dedicated chat}} | {{pending: paid plans only?}} | {{pending: hours}} | {{pending: role}} |

## Tiers

| Tier | Handles | Escalates when |
|------|---------|----------------|
| Tier 0 | Self-service: help articles, status page, in-product guidance | The answer is not documented |
| Tier 1 | Account questions, how-to, known issues | A bug or data problem is suspected |
| Tier 2 | Reproduction, logs, configuration, workarounds | A code or infrastructure change is needed |
| Tier 3 | Engineering fix | — |

A suspected outage skips the tiers and goes straight to the [incident levels](incident-levels.md).

## Response targets

| Priority | Definition | First response | Resolution target |
|----------|------------|----------------|-------------------|
| P1 | User cannot work at all | {{pending: target}} | {{pending: target}} |
| P2 | Important feature broken, workaround exists | {{pending: target}} | {{pending: target}} |
| P3 | Question or minor issue | {{pending: target}} | {{pending: target}} |

Do not publish these targets as a contractual commitment until they have been measured for a while.

## Use of AI in support

{{pending: decide whether an AI assistant drafts or sends replies, and which topics always need a person}}

- AI-drafted replies that touch billing, data deletion or security are always reviewed by a person.
- The assistant only reads what the ticket needs; it never gets broad access to user data.

## Feedback loop

- Repeated questions become help articles.
- Repeated bugs go to [known issues](known-issues.md) and to the backlog.
- A monthly summary of ticket volume and themes goes to the product owner.

## Related

- [Service catalog](service-catalog.md)
- [Known issues](known-issues.md)
- [Incident levels](incident-levels.md)
- [Escalation matrix](escalation-matrix.md)
