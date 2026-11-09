# SLA matrix

## Purpose

Compare what each critical vendor promises with what the project promises its own customers, and expose gaps before they become an incident or a contract problem.

Status: draft. {{pending: name the owner of this matrix}}

## Vendor commitments

| Vendor | Service | Published availability | Support response | Credits or remedies | Status page | Last checked |
|--------|---------|------------------------|------------------|---------------------|-------------|--------------|
| {{pending: vendor}} | {{pending: service used}} | {{pending: value from the vendor's terms}} | {{pending: by severity}} | {{pending: summary}} | {{pending: link}} | {{pending: date}} |

Copy values from the vendor's current terms and note the date; do not estimate them.

## Our commitments

| Service | Availability target | Recovery time objective | Recovery point objective | Customer support response |
|---------|---------------------|-------------------------|--------------------------|---------------------------|
| {{pending: service}} | {{pending: target}} | {{pending: RTO}} | {{pending: RPO}} | {{pending: by priority}} |

## Gap analysis

A service that depends on several vendors in series cannot be more available than the product of their availabilities. Example only: two dependencies at 99.9% each give at most about 99.8% combined, before counting our own failures.

| Our service | Depends on | Combined vendor ceiling | Our target | Gap | Mitigation |
|-------------|------------|-------------------------|------------|-----|------------|
| {{pending: service}} | {{pending: vendors}} | {{pending: calculated}} | {{pending: target}} | {{pending: yes / no}} | {{pending: redundancy, caching, degraded mode, lower target}} |

## Rules

- Never promise customers a target higher than the combined vendor ceiling without a mitigation.
- Service credits rarely cover real losses; plan resilience, not compensation.
- Track real vendor incidents against their promise; repeated misses go to the vendor review.

## Review

Review every {{pending: frequency}}, at each vendor renewal and when a vendor changes its terms.

## Related

- [Vendor catalog](vendor-catalog.md)
- [Vendor risk assessment](vendor-risk-assessment.md)
- [Service catalog](../service-catalog.md)
- [Support model](../support-model.md)
