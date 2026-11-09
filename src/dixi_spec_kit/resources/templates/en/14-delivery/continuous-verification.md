# Continuous Verification

## Purpose

Keep checking a release after it leaves CI: confirm that what runs is what was approved, that it behaves in the real environment and that it stays within objectives. Passing tests before deployment is necessary but not sufficient.

## Checks after each deployment

| Check | What it proves | Where | Blocks promotion |
|---|---|---|---|
| Version check | The running version endpoint returns the approved commit identifier | staging, production | Yes |
| Smoke checks | Health, sign-in of a synthetic user and the main flow in read-only mode | staging, production | Yes |
| Error and latency watch | No regression for the new version during the bake time | staging, production | Yes |
| Dynamic security scan | No new findings above {{pending: severity}} on the deployed system | staging | {{pending: yes or report only}} |
| SLO burn | Error budget is not burning fast | production | Triggers rollback |

## Smoke checks

- Few and critical; they finish in under {{pending: minutes}}.
- Use synthetic users and data; in production they never create data a real user can see.
- Credentials for synthetic users live in the secret store, never in the repository.
- They are a separate step that does not rebuild or reinstall the application.

## Bake time

- Minimum bake time in production: {{pending: minutes}}.
- During the bake time the previous version is still available and rollback is quick.
- The deployment ends only when the bake time closes without alerts.

## Synthetic monitoring

- Run the main journey from outside every {{pending: interval}} in production.
- Alert on {{pending: number}} consecutive failures, following the alerting rules.

## Evidence

Each production deployment records: commit identifier, `make verify` result, smoke check result, approver and time. Location: {{pending: where the record is kept}}.

## Rehearsal

Practise a forced failure in staging {{pending: frequency}} to confirm that checks block promotion and rollback works.

## Related

- [Deployment strategy](deployment-strategy.md)
- [Rollback strategy](rollback-strategy.md)
- [SLIs, SLOs and SLAs](../12-observability/slis-slos-slas.md)
- [Alerting rules](../12-observability/alerting-rules.md)
- [Security test plan](../11-quality/security-test-plan.md)
