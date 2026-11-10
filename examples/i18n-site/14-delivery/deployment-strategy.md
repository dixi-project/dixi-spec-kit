# Deployment Strategy

## Purpose

Define how a new version replaces the running one with the least user impact, and how the team decides that a deployment is finished or must be reversed.

## Options

| Strategy | How it works | Good for | Cost |
|---|---|---|---|
| Recreate | Stop old, start new | Static sites, internal tools that tolerate a short gap | Downtime |
| Rolling | Replace instances gradually | Stateless services | Two versions run briefly |
| Blue/green | Run new version next to old, switch traffic at once | Fast rollback | Double capacity during switch |
| Canary | Send a small share of traffic to the new version, then increase | High-traffic services | Needs good per-version metrics |

Chosen strategy per component: {{pending: record in the table below and in an ADR}}

| Component | Strategy | Bake time | Rollback trigger |
|---|---|---|---|
| {{pending: web or site}} | {{pending: strategy}} | {{pending: minutes}} | {{pending: condition}} |
| {{pending: service}} | {{pending: strategy}} | {{pending: minutes}} | {{pending: condition}} |

## Before deploying

- [ ] `make verify` green on the exact commit being deployed
- [ ] Same artifact already verified in staging
- [ ] Database changes are backward compatible with the running version
- [ ] Release notes and rollback plan written
- [ ] Human approval recorded for production

## During and after

1. Deploy outside {{pending: blocked windows, e.g. peak hours}}.
2. Watch error rate and latency for the new version during the bake time.
3. If an alert fires or a smoke check fails, roll back first and investigate later.
4. Declare the deployment finished only when the bake time ends without alerts.

## Feature flags

- Use flags to separate deploying code from releasing a feature.
- Every flag has an owner and a removal date: {{pending: maximum flag lifetime}}.

## Related

- [Rollback strategy](rollback-strategy.md)
- [Environments](environments.md)
- [CI/CD overview](ci-cd-overview.md)
- [Alerting rules](../12-observability/alerting-rules.md)
- [Deployment architecture](../09-architecture/deployment-architecture.md)
