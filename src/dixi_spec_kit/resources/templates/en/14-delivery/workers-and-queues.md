# Workers and Queues

## Purpose

Describe the asynchronous processing of the system: which queues exist, who publishes and consumes, how failures and retries are handled and how workers are deployed and scaled.

## Decisions

- Messaging technology: {{pending: decide and record in an ADR}}
- Delivery guarantee assumed: {{pending: at least once is the usual default}}
- Message format and schema location: {{pending: decide}}

## Queue inventory

| Queue | Publisher | Consumer | Message | Ordering | Retries | Dead letter queue | Owner |
|---|---|---|---|---|---|---|---|
| {{pending: queue name}} | {{pending: component}} | {{pending: worker}} | {{pending: event or command}} | {{pending: required or not}} | {{pending: number and backoff}} | {{pending: name}} | {{pending: role}} |

## Consumer rules

- Consumers are idempotent; use a message identifier to skip duplicates.
- Acknowledge a message only after its work is committed.
- Retry transient errors with exponential backoff and a maximum; send permanent errors to the dead letter queue.
- Propagate the trace context from message headers.
- Never put secrets or unnecessary personal data in message bodies.

## Dead letters

- Alert when a dead letter queue receives messages: {{pending: threshold}}.
- Messages are inspected, fixed and replayed with a documented procedure, never deleted without a record.
- Retention in the dead letter queue: {{pending: days}}.

## Deployment and scaling

- Workers use rolling deployment; on shutdown they stop taking new messages and finish the current one within {{pending: seconds}}.
- A new message version is consumed by both old and new workers during a release.
- Scaling signal: {{pending: backlog size, oldest message age or CPU}}; limits: {{pending: min and max workers}}.

## Monitoring

- Backlog, oldest message age, processing duration, failures and dead letters, from the metrics catalog.
- An alert fires when the backlog keeps growing for {{pending: minutes}}.

## Related

- [Scheduled jobs](cron-jobs.md)
- [Event architecture](../09-architecture/event-architecture.md)
- [Event design standard](../10-engineering/event-design-standard.md)
- [Tracing strategy](../12-observability/tracing-strategy.md)
- [Runbooks](../12-observability/runbooks/README.md)
