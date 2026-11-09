# Resilience Architecture

## Purpose

Describe how the system keeps working, degrades gracefully or recovers when parts of it fail. It sets availability and recovery targets and the patterns used to meet them. Targets here are design goals, not measured results.

## Targets

| Objective | Target | Notes |
|---|---|---|
| Availability | {{pending: e.g. monthly percentage}} | Agreed with the business owner |
| Recovery time objective (RTO) | {{pending: duration}} | Max time to restore service |
| Recovery point objective (RPO) | {{pending: duration}} | Max acceptable data loss |

## Failure modes

| Failure | Impact | Detection | Response |
|---|---|---|---|
| Application instance crashes | {{pending: impact}} | Health check | Restart and route to healthy instances |
| Datastore unavailable | {{pending: impact}} | {{pending: signal}} | {{pending: failover or read-only mode}} |
| External dependency slow | {{pending: impact}} | Latency alert | Timeout, circuit breaker, fallback |
| Bad deployment | {{pending: impact}} | Error-rate alert | Rollback |

## Patterns

- **Timeouts** on every remote call: {{pending: default values}}.
- **Retries** with exponential backoff and jitter, only for idempotent operations.
- **Circuit breakers** around unstable dependencies: {{pending: which ones}}.
- **Bulkheads**: isolate resources so one failing feature does not exhaust the rest.
- **Graceful degradation**: {{pending: which features can be switched off}}.
- **Idempotency** for operations that may be repeated by retries or users.

## Backup and restore

- What is backed up: {{pending: datastores, files, configuration}}
- Frequency and retention: {{pending: schedule}}
- Restore procedure: {{pending: link or steps}}
- Restore drills: {{pending: planned cadence}}

## Observability for resilience

- Health endpoints: {{pending: liveness and readiness}}
- Key alerts: {{pending: error rate, saturation, queue depth}}
- On-call or escalation: {{pending: who responds}}

## Related

- [Deployment architecture](deployment-architecture.md)
- [Integration architecture](integration-architecture.md)
- [Performance architecture](performance-architecture.md)
- [Architecture decisions](adr/README.md)
- [Test plan](../11-quality/test-plan.md)
