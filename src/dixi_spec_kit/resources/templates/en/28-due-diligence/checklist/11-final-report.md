# Checklist 11 — Final consolidation

> **Evidence rule.** The consolidation adds no new claims: it only brings together scores and findings already backed by artifacts in checklists 01–10. Unscored items stay "no evidence".

## Purpose

Check that the review is complete and consistent before the [DD report](../dd-report-template.md) is issued: every area scored, every finding sourced, red flags explicit, remediation owned, and confidentiality respected.

Status: draft. {{pending: name who signs off the consolidation}}

## Completeness

| Area | Checklist | Scored? | Evidence linked for every item? | Red flags recorded? |
|------|-----------|---------|---------------------------------|---------------------|
| Infrastructure | [01](01-infrastructure.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Architecture | [02](02-architecture.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Source code | [03](03-source-code.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Security | [04](04-security.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Data management | [05](05-data-management.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Processes | [06](06-processes.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Team | [07](07-team.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Financial | [08](08-financial.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Vendors and partners | [09](09-vendors-partners.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |
| Innovation | [10](10-innovation.md) | {{pending: yes / no}} | {{pending: yes / no}} | {{pending: yes / none}} |

## Consistency checks

- [ ] Scores follow the scale and aggregation method in the [DD strategy](../dd-strategy.md).
- [ ] Each finding has severity, evidence link and recommendation.
- [ ] Contradictions between areas are resolved or stated (e.g. security score vs. open critical vulnerabilities).
- [ ] Limitations (areas not reviewed, access denied) are listed.
- [ ] No secrets, credentials or personal data appear in the material.
- [ ] Material shared externally matches the confidentiality agreement.

## Remediation hand-off

- [ ] Every high or critical finding has an owner, a date and a ticket.
- [ ] Material findings are added to the [Risk register](../../13-security/risk-register.md).
- [ ] A follow-up review date is set: {{pending: date}}

## Sign-off

| Role | Name or role | Date | Decision |
|------|--------------|------|----------|
| DD owner | {{pending: role}} | {{pending: date}} | {{pending: approved / changes requested}} |
| Technical reviewer | {{pending: role}} | {{pending: date}} | {{pending: approved / changes requested}} |

## Related

- [DD report template](../dd-report-template.md)
- [DD strategy](../dd-strategy.md)
- [Risk register](../../13-security/risk-register.md)
