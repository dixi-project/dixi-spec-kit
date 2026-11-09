# Business Continuity Plan

## Purpose

Describe how the organisation keeps delivering its critical services when people, places, systems or suppliers are unavailable. Disaster recovery restores technology; continuity keeps the business working while that happens.

## Scope

- Critical services covered: {{pending: list of business services}}
- Out of scope: {{pending: list}}
- Plan owner: {{pending: role}}

## Business impact analysis

| Business service | Maximum tolerable outage | Depends on | Manual workaround | Owner |
|---|---|---|---|---|
| {{pending: service}} | {{pending: duration}} | {{pending: systems, people, suppliers}} | {{pending: workaround}} | {{pending: role}} |
| {{pending: service}} | {{pending: duration}} | {{pending: dependencies}} | {{pending: workaround}} | {{pending: role}} |

Technical recovery targets for each service are recorded in the RTO/RPO matrix.

## Disruption scenarios

| Scenario | Response |
|---|---|
| Key people unavailable | Documented runbooks, at least two people trained per critical task: {{pending: list}} |
| Office or workplace unavailable | {{pending: remote work arrangements}} |
| Critical system unavailable | Follow the disaster recovery runbook; apply manual workarounds |
| Critical supplier unavailable | {{pending: alternative supplier or degraded service}} |

## Roles and contacts

| Role | Primary | Backup |
|---|---|---|
| Continuity lead | {{pending: role}} | {{pending: role}} |
| Technical recovery | {{pending: role}} | {{pending: role}} |
| Communications | {{pending: role}} | {{pending: role}} |

Keep personal contact details in a protected location outside this repository: {{pending: where}}.

## Activation

1. Any lead may activate the plan when a scenario above exceeds its tolerable outage.
2. Notify roles and open a continuity record.
3. Run workarounds and technical recovery in parallel.
4. Deactivate when services are back within normal levels; hold a review.

## Testing and maintenance

- Exercise the plan {{pending: frequency}}; record only exercises actually held.
- Review after any significant change in services, suppliers or team.

## Related

- [Disaster recovery runbook](dr-runbook.md)
- [Disaster recovery strategy](dr-strategy.md)
- [RTO and RPO matrix](rto-rpo-matrix.md)
- [Incident response](../../13-security/incident-response.md)
- [Risk register](../../13-security/risk-register.md)
