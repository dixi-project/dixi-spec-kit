# Scheduled Jobs

## Purpose

List every scheduled job, when it runs, what it does and what happens when it fails. Jobs that run silently and fail silently are a common source of incidents.

## Rules

- Schedules are declared in versioned configuration, never only on a server.
- Times are in UTC; record the local business time next to it if it matters.
- Every job is idempotent: running it twice produces the same result.
- Only one instance runs at a time unless the job is designed for parallelism (use a lock).
- Every job emits duration and failure metrics and logs with its name.
- A job that has not succeeded within its expected interval raises an alert.

## Job inventory

| Job | Schedule (UTC) | What it does | Max duration | Idempotent | On failure | Owner |
|---|---|---|---|---|---|---|
| {{pending: e.g. cleanup-expired-sessions}} | {{pending: cron expression}} | {{pending: description}} | {{pending: minutes}} | Yes | {{pending: retry, alert}} | {{pending: role}} |
| {{pending: e.g. nightly-report}} | {{pending: cron expression}} | {{pending: description}} | {{pending: minutes}} | {{pending: yes or no}} | {{pending: action}} | {{pending: role}} |

## Failure handling

- Retries: {{pending: number and backoff}}.
- After retries: alert to {{pending: channel}} and record the failure.
- Missed runs (system down at the scheduled time): {{pending: run on recovery or skip}}.

## Deployment

- Jobs use the same artifact and configuration as the service they belong to.
- During a deployment, running jobs finish or stop safely: {{pending: behaviour}}.
- A new job is tested in staging before it is enabled in production.

## Monitoring

| Signal | Source |
|---|---|
| Duration per run | `job.run.duration` in the metrics catalog |
| Failures per run | `job.run.failures` in the metrics catalog |
| Last success time | {{pending: metric or log query}} |

## Related

- [Workers and queues](workers-and-queues.md)
- [Metrics catalog](../12-observability/metrics-catalog.md)
- [Alerting rules](../12-observability/alerting-rules.md)
- [Tracing strategy](../12-observability/tracing-strategy.md)
