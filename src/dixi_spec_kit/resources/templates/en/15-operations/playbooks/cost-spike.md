# Cost spike

## Purpose

Investigate and contain an unexpected rise in infrastructure, storage, network or AI usage cost before it becomes a large bill.

Status: draft. {{pending: name the owner of this playbook}}

## When it applies

- A budget alert fires (see [budget alerts](../../22-finops/budget-alerts.md)).
- Daily spend for a service or account grows more than {{pending: percent}} over its recent average.
- Someone notices an unusual line in the bill.

## Roles

- **Cost owner** of the affected service: leads the investigation.
- **Operator**: a person with access who applies containment.
- **Finance contact**: informed when the projected overrun exceeds {{pending: amount or percent}}.

## Steps

1. **Confirm** the spike is real: compare with the same day last week and rule out billing delays or one-off charges.
2. **Locate** it: break the cost down by service, environment, tag and usage type.
3. **Classify the cause**, typical families:
   - compute: autoscaling loop, forgotten test resources, oversized instances;
   - network: traffic routed through a paid path, data transfer between regions, a chatty integration;
   - storage: logs or backups without retention, objects growing without lifecycle rules;
   - database: runaway queries, extra replicas, storage auto-growth;
   - AI usage: a loop calling a model, larger model than needed, prompts without caching, abuse of a public endpoint.
4. **Contain** with the least disruptive action: lower a limit, pause a job, add a quota or rate limit, delete clearly orphaned test resources. Changes to production follow the normal approval; an AI agent never applies them alone.
5. **Estimate** the impact: projected extra spend, with assumptions and the data source.
6. **Fix** the root cause and add a guard so it cannot repeat silently (alert, quota, retention rule, test).

## Close criteria

- Daily spend back to the expected range for {{pending: days}}.
- Root cause written down with the estimate and its source.
- A preventive guard is in place or tracked in the backlog.

## Related

- [Budget alerts](../../22-finops/budget-alerts.md)
- [AI cost management](../../22-finops/ai-cost-management.md)
- [Cost strategy](../../22-finops/cost-strategy.md)
- [Escalation matrix](../escalation-matrix.md)
