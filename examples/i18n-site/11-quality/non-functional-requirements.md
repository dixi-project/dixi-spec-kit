# Non-functional requirements

## Purpose

Record the qualities the system must have beyond features, such as performance, availability, accessibility and privacy, in a form that can be measured and tested.

Status: draft. {{pending: agree on the non-functional requirements with the product owner}}

## How to write one

Each requirement has an ID, a measurable target, a way to verify it and an owner. Avoid "fast" or "secure"; state a number or a checkable condition.

| ID | Quality | Requirement | Target | Verification | Owner |
|----|---------|-------------|--------|--------------|-------|
| NFR-001 | Performance | Main pages load quickly | {{pending: target, see web vitals budgets}} | {{pending: how measured}} | {{pending: owner}} |
| NFR-002 | Availability | Service is reachable | {{pending: target}} | {{pending: how measured}} | {{pending: owner}} |
| NFR-003 | Accessibility | Interface is usable with assistive technology | {{pending: standard and level}} | {{pending: how checked}} | {{pending: owner}} |
| NFR-004 | Internationalisation | Content is available in each supported language with its own URL | {{pending: languages}} | {{pending: how checked}} | {{pending: owner}} |
| NFR-005 | Privacy | Personal data is minimised and protected | {{pending: rules}} | {{pending: how checked}} | {{pending: owner}} |
| NFR-006 | Maintainability | Code passes the verification ladder | All rungs green | `make verify` | {{pending: owner}} |

## Categories to consider

- Performance and capacity
- Availability and recovery
- Security and privacy
- Accessibility
- Internationalisation and localisation
- Observability (logs, metrics, alerts)
- Compatibility (browsers, devices, versions)
- Maintainability and operability

{{pending: remove the categories that do not apply and justify why}}

## Rules

- Targets are decided by people and recorded here. Agents may propose targets but never lower an agreed one to make a check pass.
- A requirement without a verification method is incomplete.
- Link each requirement to the features or contracts it constrains.

## Related

- [Quality strategy](quality-strategy.md)
- [Web vitals budgets](performance-budgets/web-vitals-budgets.md)
- [Risk-based review](risk-based-review.md)
- [Test plan](test-plan.md)
- [Project](../00-master-spec.md)
