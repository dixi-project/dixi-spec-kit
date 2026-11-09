# Maintenance window policy

## Purpose

Define when planned work that may affect users can happen, how it is approved and how users are told in advance.

Status: draft. {{pending: name the owner of this policy}}

## Windows

| Type | When | Notice to users | Approval |
|------|------|-----------------|----------|
| Standard | {{pending: day, hours and time zone of lowest traffic}} | {{pending: e.g. 5 business days}} | Service owner |
| Extended | {{pending: e.g. once per quarter, weekend}} | {{pending: e.g. 2 weeks}} | Service owner and product owner |
| Emergency | Any time | As soon as possible | Incident lead |

Choose the standard window from real traffic data, not habit. {{pending: confirm the lowest-traffic period from metrics}}

## What needs a window

- Changes that cause downtime or a read-only period.
- Database migrations that lock tables or take longer than {{pending: minutes}}.
- Infrastructure changes without a tested rollback.

Changes deployed with zero downtime and a tested rollback do not need a window.

## Before the window

1. Write the plan: steps, expected duration, rollback point, owner.
2. Get the approval listed above.
3. Notify users through the status page and the channels in the [support model](support-model.md).
4. Confirm the on-call person knows about the work.
5. Freeze unrelated deployments during the window.

## During the window

- Follow the plan; any deviation is decided by the owner and written down.
- If the work runs over by {{pending: minutes}}, roll back unless the owner decides otherwise.
- Keep an internal channel updated every {{pending: interval}}.

## After the window

- Confirm health signals are normal.
- Close the status page notice.
- Record the outcome and anything to improve.

## Blackout periods

{{pending: list periods with no planned maintenance, e.g. product launches, peak sales days}}

## Related

- [Service catalog](service-catalog.md)
- [Support model](support-model.md)
- [Internal outage communication](playbooks/comms-outage-internal.md)
- [Customer outage communication](playbooks/comms-outage-customer.md)
