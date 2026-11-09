# Flows

## Purpose

Describe the business flows that cross several steps, actors or modules: what starts them, the
happy path, the alternatives, the errors and the events they emit. A feature spec explains one
capability; a flow explains how features and modules cooperate end to end. Flows are where missing
contracts, unclear ownership and unhandled errors become visible before any code is written.

## When to write a flow

- The process involves more than one module, domain or external system.
- Several actors take turns (for example, a customer submits and an operator approves).
- Failures in the middle need compensation or a clear message to the user.
- The process has timing rules: expirations, reminders, retries or schedules.

Simple, single-module interactions are documented in the feature spec instead.

## How to describe a flow

1. Copy the [flow template](../10-engineering/templates/flow-template.md) to
   `06-flows/<flow-name>-flow.md`, using lowercase words separated by hyphens.
2. Give it a stable ID (`FLOW-NNN`) and link the features it covers.
3. Write the happy path as numbered steps with one actor per step.
4. Add a sequence diagram; keep it consistent with the numbered steps.
5. List alternative flows and error handling for every step that can fail.
6. Name each event, command or API call and link its contract in `07-contracts/`.
7. Ask a person to validate the flow before building the features it involves.

## Flow index

| ID | Flow | Trigger | Actors | Features | Owner | Status |
|---|---|---|---|---|---|---|
| FLOW-001 | {{pending: flow name}} | {{pending: what starts it}} | {{pending: actors}} | {{pending: FEATURE IDs}} | {{pending: role}} | {{pending: draft or validated}} |

## Quality checklist

- Every step names its actor and the system that records the result.
- Every external call states its timeout and retry policy.
- Every error has an observable behavior and, if relevant, an error code.
- Every emitted event has a contract and at least one known consumer.
- Acceptance tests cover the happy path and at least one alternative flow.

## Related

- [Flow template](../10-engineering/templates/flow-template.md)
- [Feature example](../05-features/example/feature-spec.md)
- [Contract example](../07-contracts/example.md)
- [API contracts](../07-contracts/api/README.md)
