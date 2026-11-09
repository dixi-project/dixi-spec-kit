# Observability standard

## Purpose

Define the minimum logs, metrics, traces and alerts every service in this project must produce, so that failures are detected by the system before users report them and can be diagnosed without guesswork.

Status: draft. {{pending: confirm the observability owner}}

## Minimum rules

- [ ] Logs are structured, with timestamp, level, service, environment and correlation ID.
- [ ] No secrets or personal data in logs, metrics or trace attributes.
- [ ] Every request carries a correlation ID across services.
- [ ] Each service exposes a health check.
- [ ] Each user-facing journey has at least one service level indicator.
- [ ] Every alert has an owner and a runbook.

## Signals

| Signal | Minimum content | Retention |
|--------|-----------------|-----------|
| Logs | Errors, security events, key business events | {{pending: retention}} |
| Metrics | Request rate, error rate, latency, saturation | {{pending: retention}} |
| Traces | Cross-service requests, external calls | {{pending: retention}} |
| Audit events | Who did what, when, on which resource | {{pending: retention}} |

## Service levels

| Journey | Indicator | Objective | Window |
|---------|-----------|-----------|--------|
| {{pending: e.g. sign in}} | {{pending: success rate}} | {{pending: target}} | {{pending: window}} |

## Alerts

- Alert on symptoms users feel (errors, latency), not only on causes.
- Every alert must be actionable; remove alerts nobody acts on.
- Severity maps to the incident levels in the [incident policy](policies/incident-policy.md).
- Each alert links to a runbook based on the [runbook template](../10-engineering/templates/runbook-template.md).

## Logging levels

| Level | Use |
|-------|-----|
| ERROR | A request or job failed and needs attention. |
| WARN | Unexpected but handled; may need follow-up. |
| INFO | Key lifecycle and business events. |
| DEBUG | Diagnostic detail; off in production by default. |

## Tooling

{{pending: choose how signals are collected, stored and visualized}}

## Related

- [Logging standard](../10-engineering/logging-standard.md)
- [Environment strategy](environment-strategy.md)
- [Release management standard](release-management-standard.md)
- [Security baseline](security-baseline.md)
