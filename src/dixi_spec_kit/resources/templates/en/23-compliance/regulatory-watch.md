# Regulatory watch

> **Working aid, not legal advice.** This log helps notice and route regulatory changes. It does not interpret the law and no template certifies compliance; confirm the impact of each change with qualified counsel.

## Purpose

Detect changes in laws, regulations, standards and guidance that could affect the project, decide whether they matter and turn the ones that do into tracked work.

Status: draft. {{pending: name who runs the watch and how often}}

## Scope

- Jurisdictions where users, customers or data are located: {{pending: list jurisdictions}}
- Sectors the product serves: {{pending: list sectors}}
- Frameworks the project tracks: see the [Compliance overview](compliance-overview.md).

## Sources

| Source type | Example | Frequency | Owner |
|-------------|---------|-----------|-------|
| Official journals and regulators | Publications of the supervisory authority | {{pending: frequency}} | {{pending: owner}} |
| Standards bodies | New versions or transition deadlines of a standard | {{pending: frequency}} | {{pending: owner}} |
| Counsel or industry associations | Newsletters, alerts | {{pending: frequency}} | {{pending: owner}} |
| Customer requirements | New contract or questionnaire clauses | On each request | {{pending: owner}} |

## Triage

For each item decide:

1. **Relevant?** Does it touch our jurisdictions, sectors, data types or frameworks?
2. **Impact**: none, documentation only, process change, product change.
3. **Deadline**: effective date and any transition period, as published by the source.
4. **Action**: create a task, update a spec or a rule, or close with a reason.

## Watch log

| ID | Date seen | Change | Source (link) | Effective date | Relevance | Impact | Action / ticket | Owner | Status |
|----|-----------|--------|---------------|----------------|-----------|--------|-----------------|-------|--------|
| RW-01 | {{pending: date}} | {{pending: short description}} | {{pending: link}} | {{pending: date}} | {{pending: yes / no}} | {{pending: level}} | {{pending: ticket}} | {{pending: owner}} | open |

## Rules

- Record the source for every item; do not log hearsay as fact.
- Items with product impact become rules in [Compliance rules](../01-business/rules/compliance-rules.md) and risks in the [Risk register](../13-security/risk-register.md).
- Closed items stay in the log with their reason.

## Related

- [Compliance overview](compliance-overview.md)
- [GDPR readiness](gdpr/gdpr-readiness.md)
- [Risk register](../13-security/risk-register.md)
- [Project](../00-master-spec.md)
