# Incident policy

## Purpose

Define what counts as an incident in this project, who does what when one happens, how it is communicated and how the team learns from it. Step-by-step response lives in runbooks and the security incident response plan.

Status: draft. {{pending: confirm this policy with the responsible person}}

## Principles

- Restore service first; investigate root cause after.
- Blameless: describe systems and decisions, not people's faults.
- One incident commander at a time.
- Every incident leaves a record, however small.

## Severity levels

| Level | Definition | Response target | Notify |
|-------|------------|-----------------|--------|
| SEV1 | Service down or data exposed for many users | {{pending: target}} | {{pending: who}} |
| SEV2 | Major feature degraded, workaround exists | {{pending: target}} | {{pending: who}} |
| SEV3 | Minor impact, few users | {{pending: target}} | {{pending: who}} |

## Roles

| Role | Responsibility |
|------|----------------|
| Incident commander | Coordinates, decides, keeps the timeline. |
| Operations lead | Investigates and applies fixes. |
| Communications lead | Updates users and stakeholders. |
| Scribe | Records actions and decisions with timestamps. |

Agents may help gather data and draft updates; a person makes every decision and change.

## Lifecycle

1. **Detect** through alerts or reports.
2. **Declare** with a severity and a commander.
3. **Mitigate** to stop the impact.
4. **Resolve** and confirm with monitoring.
5. **Review** with a postmortem.

## Access during an incident

- Elevated access is granted temporarily, logged and revoked afterwards. {{pending: break-glass procedure}}

## Communication

- Incident channel: {{pending: channel}}
- Status updates every {{pending: interval}} for SEV1 and SEV2.
- Legal or regulatory notifications: {{pending: who decides and within what time}}

## Postmortem

- Required for SEV1 and SEV2, within {{pending: days}}.
- Use the [postmortem template](../../10-engineering/templates/postmortem-template.md).
- Action items have owners and due dates.

## Related

- [Incident response](../../13-security/incident-response.md)
- [Runbook template](../../10-engineering/templates/runbook-template.md)
- [Observability standard](../observability-standard.md)
