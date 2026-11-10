# Restore service

## Purpose

Bring a degraded or unavailable service back to a working state quickly and safely, before investigating the root cause.

Status: draft. {{pending: name the owner of this playbook}}

## When it applies

- An alert or a user report shows that a service in production is down or degraded.
- Any incident level; the [incident levels](../incident-levels.md) decide how fast and who joins.

## Roles

- **Incident lead**: decides and keeps the timeline.
- **Operator**: a person with production access who runs the actions.
- **Communications lead**: keeps internal and customer updates flowing.

An AI agent may help read logs, summarise and propose steps; a person runs every production action.

## Steps

1. **Declare.** Open the incident channel, set the level, name the lead.
2. **Stabilise.** Stop the bleeding: pause the failing job, shed load or switch on a maintenance page.
3. **Find the last change.** Check recent deployments, configuration and feature flags. {{pending: where the change log lives}}
4. **Choose the safest action**, in this order of preference:
   - roll back the last deployment or configuration change;
   - turn off the feature flag involved;
   - restart or scale the affected component;
   - fail over to a standby, if one exists. {{pending: list available failover options}}
5. **Get approval** from the incident lead for any action that changes data or cannot be undone.
6. **Act and observe.** Run one action at a time and watch the key signals for {{pending: minutes}} before the next.
7. **Communicate** every {{pending: interval}} following the [customer outage communication](comms-outage-customer.md) playbook.

## Close criteria

- Key health signals back to their normal range for at least {{pending: duration}}.
- No growing queue, error backlog or data inconsistency left behind.
- Customers told that service is restored.
- Timeline recorded and a postmortem scheduled for SEV1 and SEV2.

## Do not

- Delete data, rotate shared credentials or change several things at once to "see what works".
- Close the incident because the alert stopped; confirm with real signals.

## Related

- [Incident levels](../incident-levels.md)
- [Escalation matrix](../escalation-matrix.md)
- [Customer outage communication](comms-outage-customer.md)
- [Runbook template](../../10-engineering/templates/runbook-template.md)
- [Postmortem template](../../10-engineering/templates/postmortem-template.md)
