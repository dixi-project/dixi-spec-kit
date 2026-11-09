# Disaster Recovery Runbook

## Purpose

Give the step-by-step procedure to follow once a disaster has been declared. It assumes the person running it is under pressure: steps are short, ordered and safe to repeat.

## Before you start

- Disaster declared by: {{pending: role with decision rights}}
- Incident channel and record opened: {{pending: where}}
- Roles assigned: incident lead, operator, communications, scribe.
- Emergency access, if needed, follows the break-glass procedure and is logged.

## Procedure

1. **Assess.** Confirm scope: which capabilities and tiers are affected. Check the RTO/RPO matrix.
2. **Contain.** Stop the damage: block compromised credentials, pause jobs and workers that could write bad data.
3. **Decide.** Choose recovery path (restore in place, fail over to another location, degraded mode) and record who decided and when.
4. **Prepare target.** Recreate infrastructure from versioned code in the recovery location: {{pending: command or pipeline reference}}.
5. **Restore data.** Restore the latest valid backup or point in time before the failure; record the restore point.
6. **Restore secrets and configuration.** From the secondary location: {{pending: where}}.
7. **Deploy.** Deploy the last known good artifact through the release pipeline; human approval still applies.
8. **Verify.** `make verify` result for the artifact, version check, smoke checks and data integrity checks.
9. **Switch traffic.** Point users to the recovered system: {{pending: mechanism}}.
10. **Monitor.** Watch errors, latency and backlog for {{pending: duration}}.

## Communication

| Audience | Channel | When | Owner |
|---|---|---|---|
| Internal team | {{pending: channel}} | At declaration and every {{pending: minutes}} | Communications |
| Users | {{pending: status page or channel}} | {{pending: when}} | Communications |
| Regulators or customers under contract | {{pending: channel}} | {{pending: deadline}} | {{pending: role}} |

## Return to normal

- Fail back to the primary location only when stable, with a planned window and approval.
- Reconcile data written during the disaster.
- Write a postmortem and update this runbook with what was missing.

## Related

- [Disaster recovery strategy](dr-strategy.md)
- [RTO and RPO matrix](rto-rpo-matrix.md)
- [Backup and recovery](../backup-and-recovery.md)
- [Break-glass access](../../13-security/break-glass-access.md)
- [Incident response](../../13-security/incident-response.md)
