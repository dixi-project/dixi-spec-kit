# Vendor due diligence playbook

> **Evidence rule.** Assess a vendor from the evidence it supplies, not from its marketing. Missing evidence is recorded as a gap, never replaced with assumptions presented as facts; every conclusion points to an artifact.

## Purpose

Decide whether the project can depend on a supplier, with a depth proportional to the risk: what data it would receive, how critical it is, and what would happen if it failed or left.

Status: draft. {{pending: decide who approves critical vendors}}

## Tiering

| Tier | Criteria | Depth of review |
|------|----------|-----------------|
| Critical | Receives sensitive or personal data, or its outage stops the product | Full review, agreement checked by counsel, exit plan |
| Important | Supports a core process but has a workaround | Questionnaire and evidence review |
| Low | No data, easily replaced | Basic record in the vendor catalogue |

Tier of this vendor: {{pending: tier and reason}}

## Review areas

| Area | What to ask for | Evidence received | Assessment |
|------|-----------------|-------------------|------------|
| Security | Independent reports or certificates with scope and date, security overview | {{pending: link}} | {{pending: finding}} |
| Data protection | Data locations, sub-processors, DPA | {{pending: link}} | {{pending: finding}} |
| Availability | Service levels, status history, continuity plan | {{pending: link}} | {{pending: finding}} |
| Incident handling | Notification commitment and contact | {{pending: link}} | {{pending: finding}} |
| Financial and business continuity | Signals of stability relevant to the dependence | {{pending: link}} | {{pending: finding}} |
| Exit | Data export, notice periods, substitution options | {{pending: link}} | {{pending: finding}} |
| Licensing | Terms compatible with the project's use | {{pending: link}} | {{pending: finding}} |

## Steps

1. Record the need and the data the vendor would receive.
2. Assign the tier and request evidence accordingly.
3. Complete the [Vendor risk assessment](../../15-operations/vendor-management/vendor-risk-assessment.md).
4. If personal data is involved, add it to [Sub-processors](../../23-compliance/gdpr/sub-processors.md) and check the [DPA template](../../23-compliance/dpa-template.md) topics.
5. Decide: approve, approve with conditions, or reject; record the reason.
6. Add the vendor to the [Vendor catalogue](../../15-operations/vendor-management/vendor-catalog.md) with a review date.

## Decision

- Outcome: {{pending: approve / approve with conditions / reject}}
- Conditions and owner: {{pending: conditions}}
- Next review: {{pending: date}}

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 09 — Vendors and partners](../checklist/09-vendors-partners.md)
- [Vendor risk assessment](../../15-operations/vendor-management/vendor-risk-assessment.md)
