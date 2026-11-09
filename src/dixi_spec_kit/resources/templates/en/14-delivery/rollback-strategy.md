# Rollback Strategy

## Purpose

Make returning to the last known good version a routine, rehearsed action instead of an improvisation. Rolling back is the default first response to a bad release.

## Rules

- Every release keeps the previous artifact available for {{pending: period or number of versions}}.
- Rolling back does not require a new build; it redeploys the previous artifact.
- Database changes follow expand and contract so the previous version still works after a migration.
- Anyone on the on-call rotation may roll back without further approval; rolling forward again requires the normal approval.

## When to roll back

- An alert tied to the release fires during the bake time.
- A smoke check fails after deployment.
- Users report a regression in the main flow and the cause is not obvious within {{pending: minutes}}.

## How to roll back

| Component | Mechanism | Expected time | Verified on |
|---|---|---|---|
| {{pending: web or site}} | {{pending: switch to previous version}} | {{pending: minutes}} | {{pending: date of last rehearsal}} |
| {{pending: service}} | {{pending: redeploy previous artifact}} | {{pending: minutes}} | {{pending: date}} |
| Configuration | Revert the configuration change in version control | {{pending: minutes}} | {{pending: date}} |

## When rollback is not enough

- Irreversible data changes: restore from backup or apply a corrective change; document it in the release notes before deploying.
- Messages already sent to third parties: plan compensating actions.
- In those cases, deploy behind a feature flag so the feature can be switched off instead.

## After a rollback

1. Confirm recovery with the same signals that triggered it.
2. Open an incident record and, if users were affected, a postmortem.
3. Block re-release of the faulty version until a fix passes `make verify` and staging.

## Rehearsal

Rehearse a rollback in staging {{pending: frequency}} and record the result here.

## Related

- [Deployment strategy](deployment-strategy.md)
- [CI/CD overview](ci-cd-overview.md)
- [Incident response](../13-security/incident-response.md)
- [Postmortem template](../10-engineering/templates/postmortem-template.md)
- [Alerting rules](../12-observability/alerting-rules.md)
