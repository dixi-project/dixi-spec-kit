# On-call rotation

## Purpose

Define who responds to alerts outside and inside business hours, how shifts work and how the rotation stays fair and sustainable.

Status: draft. {{pending: name the owner of the rotation}}

## Coverage

| Item | Decision |
|------|----------|
| Hours covered | {{pending: e.g. business hours only, or 24/7}} |
| Shift length | {{pending: e.g. one week}} |
| Handover time | {{pending: day and hour, time zone}} |
| Primary and secondary | {{pending: yes / primary only}} |
| Paging tool | {{pending: tool category, not vendor}} |
| Acknowledge target | {{pending: minutes}} |

With fewer than {{pending: number}} people, 24/7 coverage is not sustainable; prefer business hours plus best effort and say so in the support model.

## Who is on call

- Engineers who have completed onboarding, shadowed at least one shift and can access the runbooks.
- {{pending: decide whether leads and managers take shifts}}

## During the shift

- Keep the phone reachable and be able to start working within the acknowledge target.
- Acknowledge every page, classify it with [incident levels](../incident-levels.md) and escalate using the [escalation matrix](../escalation-matrix.md).
- Write a short log of every page: time, cause, action, follow-up.

## Handover

1. Review the shift log together.
2. Hand over open incidents and anything that may page again.
3. Confirm the next person's paging setup works.

## Fairness and health

- Compensation or time off after shifts: {{pending: define according to local rules}}
- Nobody does two shifts in a row unless they volunteer.
- A shift with a night page gives the right to start late the next day.
- Noisy alerts that page without action are fixed or removed within {{pending: days}}.

## Metrics

- Pages per shift, out-of-hours pages, time to acknowledge.
- Review them every {{pending: frequency}} with the team.

## Related

- [RACI matrix](raci-matrix.md)
- [Escalation matrix](../escalation-matrix.md)
- [Incident levels](../incident-levels.md)
- [Restore service](../playbooks/restore-service.md)
