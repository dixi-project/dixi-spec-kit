# Maturity model

## Purpose

Give the platform a shared scale to assess how mature each area is, decide which gaps to close next and avoid claiming a level the evidence does not support.

Status: draft. {{pending: confirm the target level per area}}

## Levels

| Level | Name | Typical traits |
|-------|------|----------------|
| 1 | Exploratory | Works on one machine; few tests; manual steps. |
| 2 | Prototype | Specs for main features; tests for core paths; manual release. |
| 3 | Production-ready | Tests first; automated pipeline; monitoring and alerts; runbooks. |
| 4 | Industry-grade | Measured service levels; tested recovery; security reviews; audited changes. |
| 5 | Mission-critical | Redundancy across failure domains; regular recovery drills; formal change control. |

The project's declared stage is stored in `MODE`; promoting it is a human decision.

## Signals per level

| Area | Level 3 evidence | Level 4 evidence |
|------|------------------|------------------|
| Specs | Every merged feature traces to a spec | Traceability checked on every change |
| Testing | Red tests committed first; `make verify` in pipeline | Risk-based thresholds enforced; mutation or property tests on critical code |
| Security | Baseline controls in place | Threat models reviewed; periodic external review |
| Operations | Alerts with runbooks | Service level objectives tracked; recovery tested |
| Delivery | Automated deploy to staging | Progressive rollout with automatic rollback |
| AI | Agents limited to drafting | Agent actions audited and reviewed |

## What a level does not mean

- A level is not a certification.
- A high level in one area does not compensate for a low level in another.
- A level is claimed only with evidence a reviewer can check.

## Assessment

| Area | Current level | Target level | Evidence | Next step | Owner |
|------|---------------|--------------|----------|-----------|-------|
| {{pending: area}} | {{pending: level}} | {{pending: level}} | {{pending: evidence}} | {{pending: step}} | {{pending: owner}} |

Assessment cadence: {{pending: e.g. quarterly}}

## Related

- [Principles](../00-governance/principles.md)
- [Engineering standards](../00-governance/engineering-standards.md)
- [Verification ladder](../11-quality/verification-ladder.md)
- [Decision log](decision-log.md)
