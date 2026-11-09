# Cloud cost optimisation

## Purpose

Give a repeatable checklist to reduce infrastructure cost without hurting reliability or performance, and a way to record which savings were made and why.

Status: draft. {{pending: name the owner of cost optimisation}}

## Approach

1. Look at the largest cost lines first (see the [cost allocation model](cost-allocation-model.md)).
2. For each candidate, estimate the saving with assumptions and source, and the risk.
3. Make one change at a time, measure, and keep or roll back.
4. Record the result in the table below.

## Checklist

### Compute

- [ ] Rightsize: instances or containers sized from real usage, not guesses.
- [ ] Autoscaling with sensible minimums; non-production scales to zero or stops outside working hours.
- [ ] Commitment or reserved pricing only for stable, long-term baseline load. {{pending: decide commitment policy}}
- [ ] Interruptible capacity for fault-tolerant batch work.

### Storage

- [ ] Retention and lifecycle rules for logs, backups and objects.
- [ ] Infrequently accessed data moved to cheaper storage classes.
- [ ] Unattached volumes and old snapshots removed.

### Network

- [ ] Traffic between services stays in the same zone or region when possible.
- [ ] Paid network paths (gateways, cross-region transfer) reviewed for unnecessary traffic.
- [ ] Static content served through a cache or CDN.

### Databases

- [ ] Slow and frequent queries optimised before scaling up.
- [ ] Read replicas and capacity match actual load.
- [ ] Non-production databases are smaller or paused.

### Hygiene

- [ ] Every resource tagged with owner, environment and service.
- [ ] Orphaned resources reviewed every {{pending: frequency}}.

## Savings log

| Date | Change | Estimated saving (assumptions, source) | Measured saving | Risk | Decision |
|------|--------|----------------------------------------|-----------------|------|----------|
| {{pending: date}} | {{pending: change}} | {{pending: estimate}} | {{pending: measured}} | {{pending: risk}} | {{pending: keep / roll back}} |

## Do not

- Remove redundancy that protects a recovery objective just to save money, without an explicit decision.
- Let an AI agent delete or resize production resources; it may list candidates for a person to review.

## Related

- [Cost strategy](cost-strategy.md)
- [Cost allocation model](cost-allocation-model.md)
- [Budget alerts](budget-alerts.md)
- [Cost spike playbook](../15-operations/playbooks/cost-spike.md)
