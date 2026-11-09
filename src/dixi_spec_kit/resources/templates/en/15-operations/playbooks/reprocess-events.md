# Reprocess events

## Purpose

Safely replay messages or events that failed, were lost or were processed with a bug, without creating duplicates or side effects twice.

Status: draft. {{pending: name the owner of this playbook}}

## When it applies

- Messages piled up in a dead-letter queue.
- A consumer was down or processed events with a bug for a known period.
- A downstream system needs data rebuilt from the event history.

## Principles

- Fix the cause before replaying; replaying into the same bug only moves the problem.
- Consumers must be idempotent. {{pending: confirm which consumers are idempotent and how (event ID, version, upsert)}}
- Replay is a production action: a person approves and runs it; an AI agent may help analyse and prepare the selection.
- Prefer small batches with a pause over one large replay.

## Roles

- **Service owner**: decides what to replay and approves.
- **Operator**: runs the replay and watches signals.

## 1. Diagnose

1. Identify the affected queue, topic or stream and the time range.
2. Count the events involved and sample a few to understand the failure.
3. Check for poison messages that will always fail; set them aside.

## 2. Fix the cause

Deploy the fix, or confirm the dependency is back, and verify with one event in a safe environment if possible.

## 3. Replay

1. Snapshot or export the events to replay, keeping their original IDs.
2. Run a pilot of {{pending: number}} events and check the outcome.
3. Replay the rest in batches of {{pending: size}}, watching error rate, latency and queue depth.
4. Stop at the first unexpected error and go back to step 1.

## 4. Verify

- Counts match: replayed equals selected minus set-aside poison messages.
- Spot-check business results (records created, notifications sent once).
- The dead-letter queue is empty or contains only documented items.

## 5. Afterwards

Record the range, counts, approver and outcome. Add an alert or test that would have caught the failure earlier.

## Related

- [Restore service](restore-service.md)
- [Incident levels](../incident-levels.md)
- [Service catalog](../service-catalog.md)
- [Runbook template](../../10-engineering/templates/runbook-template.md)
