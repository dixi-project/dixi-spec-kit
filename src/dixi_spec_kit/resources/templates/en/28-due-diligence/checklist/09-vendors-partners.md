# Checklist 09 — Vendors and partners

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess the project's dependence on third parties: which suppliers and partners are critical, how they were assessed, what agreements cover them, and what happens if one fails or leaves.

Status: draft. {{pending: decide the criticality criteria for vendors}}

## Inputs

- [Vendor catalogue](../../15-operations/vendor-management/vendor-catalog.md)
- [Vendor risk assessment](../../15-operations/vendor-management/vendor-risk-assessment.md)
- [Sub-processors](../../23-compliance/gdpr/sub-processors.md) and [DPA template](../../23-compliance/dpa-template.md)
- [External partners](../../01-business/actors/external-partners.md)
- [External contracts](../../07-contracts/external/README.md)
- [Licensing policy](../../13-security/licensing/licensing-policy.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| VEN-01 | Is there a complete list of vendors with owner and criticality? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-02 | Were critical vendors assessed for security and continuity before use? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-03 | Do agreements cover data protection, service levels and exit? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-04 | Is there an exit or substitution plan for each critical vendor? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-05 | Are vendors that receive personal data listed as sub-processors? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-06 | Are vendor incidents and status monitored? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-07 | Are partner integrations documented with contracts and error handling? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| VEN-08 | Are contracts assignable if the organisation changes ownership? | {{pending: link, confirmed by counsel}} | {{pending: score}} | {{pending: finding}} |

## Concentration map

| Capability | Vendor category | Alternatives identified? | Switching effort |
|------------|-----------------|--------------------------|------------------|
| {{pending: capability}} | {{pending: category}} | {{pending: yes / no}} | {{pending: low / medium / high, with reason}} |

## Red flags

- A critical service with no agreement or with terms nobody has read.
- Personal data sent to a vendor that is not in the sub-processor list.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Vendor DD playbook](../playbooks/vendor-dd-playbook.md)
- [Checklist 10 — Innovation](10-innovation.md)
- [Final checklist](11-final-report.md)
