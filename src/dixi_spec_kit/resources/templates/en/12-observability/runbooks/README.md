# Runbooks

## Purpose

Explain how to write the runbooks that alerts point to. A runbook lets a person who did not build the component restore service at 3 a.m. by following steps, without guessing.

## When to write one

- Every alert with severity `critical` or `warning` links to a runbook.
- Every recurring manual operation (rotating a credential, replaying a queue) has one.
- After an incident, create or update the runbook that would have helped.

## How to write one

1. Copy the [runbook template](../../10-engineering/templates/runbook-template.md) into this folder as `<symptom>.md`, named after what is observed, not after the suspected cause.
2. State the symptom and how the alert detects it.
3. List the first checks in order, from cheapest to most expensive.
4. Give mitigation steps that reduce user impact first; root cause comes later.
5. Say when to escalate and to whom.
6. Note how to confirm recovery.
7. Test it: someone else follows it in a non-production environment.

## Style rules

- Short imperative steps; one action per step.
- Commands are copy-paste ready and safe to run twice; destructive steps say so in bold and require confirmation.
- Never include secrets; refer to where they are stored.
- Link dashboards by name from the dashboard map.

## Example (neutral)

> **Symptom:** the queue backlog keeps growing for more than 10 minutes.
>
> 1. Open the async work dashboard and check whether consumers are running.
> 2. If no consumers are running, restart them using the documented procedure.
> 3. If consumers run but fail, check the latest error logs for the consumer and the dead letter count.
> 4. If failures started after a release, roll back that release.
> 5. Escalate to the component owner if the backlog is not shrinking 15 minutes after mitigation.
> 6. Recovery: backlog trending down and no new dead letters.

The numbers in the example are illustrative; set real thresholds in the alerting rules.

## Index

| Runbook | Alert | Owner | Last tested |
|---|---|---|---|
| {{pending: first runbook}} | {{pending: alert name}} | {{pending: role}} | {{pending: date}} |

## Related

- [Alerting rules](../alerting-rules.md)
- [Dashboard map](../dashboard-map.md)
- [Incident response](../../13-security/incident-response.md)
- [Postmortem template](../../10-engineering/templates/postmortem-template.md)
