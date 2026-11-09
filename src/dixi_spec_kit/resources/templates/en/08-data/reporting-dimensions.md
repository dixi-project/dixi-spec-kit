# Reporting Dimensions

## Purpose

Define the dimensions and measures used in reports, dashboards and analytics, so that every report slices data the same way and every metric has one agreed definition.

- Owner: {{pending: person or role accountable for metric definitions}}
- Business goals these metrics serve: see the [vision](../01-business/vision.md).

## Dimensions

| Dimension | Description | Source | Granularity | Slowly changing handling |
| --- | --- | --- | --- | --- |
| Date | Calendar date in the reporting time zone | System clock, UTC converted | Day | Not applicable |
| Tenant / customer | Owning organisation | [Master data](master-data.md) | Record | {{pending: keep history or overwrite}} |
| Product / offering | | Master data | | |
| Channel | Where the action happened (web, mobile, API) | Events | | |
| Locale | Language and country of the user | User profile | | |
| {{pending: domain-specific dimension}} | | | | |

## Measures

| Measure | Definition (formula) | Unit | Aggregation | Filters always applied |
| --- | --- | --- | --- | --- |
| Active users | Distinct users with at least one qualifying action in the period | Count | Distinct count | Exclude internal and test accounts |
| {{pending: key business metric}} | | | | |

Write each definition so two people would compute the same number.

## Rules

- [ ] Dimension values come from the [canonical data model](canonical-data-model.md) or master data, not free text.
- [ ] The reporting time zone is fixed: {{pending: reporting time zone}}
- [ ] Currency conversion uses a documented rate source and date.
- [ ] Test, internal and deleted records are excluded consistently.
- [ ] Reports never expose Personal data beyond what the [PII classification](pii-classification.md) allows; prefer aggregates.
- [ ] Small groups are suppressed or merged when they could identify individuals.

## Report catalogue

| Report | Audience | Dimensions | Measures | Refresh | Owner |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Change process

- Changing a metric definition creates a new version; old reports state which version they use.
- Deprecated dimensions stay available for a period: {{pending: deprecation period}}

## Related

- [Master data](master-data.md)
- [Canonical data model](canonical-data-model.md)
- [PII classification](pii-classification.md)
- [Vision](../01-business/vision.md)
