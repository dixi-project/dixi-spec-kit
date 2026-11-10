# Alerting Rules

## Purpose

Define which conditions page a person, which only open a ticket and which are just shown on a dashboard. An alert exists to trigger a human action; if nobody needs to act, it is not an alert.

## Principles

- Alert on symptoms users feel (errors, latency, unavailability), not on every internal cause.
- Every alert that pages must link to a runbook with the first steps to take.
- Every alert has an owner, a severity and a review date.
- An alert that fires and is ignored twice is either fixed, retuned or deleted.
- Alerts never include secrets or personal data in their message.

## Severity levels

| Severity | Meaning | Response | Channel |
|---|---|---|---|
| critical | Users cannot complete the main flow | {{pending: response time, e.g. 15 minutes}} | {{pending: paging channel}} |
| warning | Degradation or risk of breach soon | {{pending: within business hours}} | {{pending: team channel}} |
| info | Useful context, no action required | None | Dashboard only |

## Alert inventory

| Alert | Condition | Window | Severity | Owner | Runbook |
|---|---|---|---|---|---|
| Site or service unavailable | Health check fails from outside | {{pending: e.g. 3 consecutive checks}} | critical | {{pending: role}} | {{pending: link}} |
| Error rate high | Server errors above {{pending: threshold}} | {{pending: window}} | critical | {{pending: role}} | {{pending: link}} |
| Latency degraded | p95 above {{pending: budget}} | {{pending: window}} | warning | {{pending: role}} | {{pending: link}} |
| Certificate expiring | Less than {{pending: days}} to expiry | Daily | warning | {{pending: role}} | {{pending: link}} |
| Deployment failed | Release did not complete or was rolled back | Per event | warning | {{pending: role}} | [Rollback](../14-delivery/rollback-strategy.md) |

When service level objectives exist, prefer alerts on error budget burn rate (a fast window and a slow window) over fixed thresholds.

## Routing and escalation

- Primary responder: {{pending: role or rotation}}
- Escalation after no acknowledgement: {{pending: time and next role}}
- Quiet hours policy: {{pending: which severities page out of hours}}
- Notification tool: {{pending: decide and record in an ADR}}

## Lifecycle

1. Propose the alert with its condition, severity and runbook.
2. Test it in a non-production environment by forcing the condition.
3. Review the inventory {{pending: frequency}} and remove noisy or unused alerts.
4. After an incident, check whether an alert fired early enough; adjust if not.

## Related

- [Incident response](../13-security/incident-response.md)
- [Runbook template](../10-engineering/templates/runbook-template.md)
- [Postmortem template](../10-engineering/templates/postmortem-template.md)
- [Rollback strategy](../14-delivery/rollback-strategy.md)
- [Test plan](../11-quality/test-plan.md)
