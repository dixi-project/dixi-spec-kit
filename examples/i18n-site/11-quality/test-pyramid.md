# Test pyramid

## Purpose

Define the intended balance between test types so that the suite stays fast, reliable and focused. Many small, fast tests at the base; few slow, broad tests at the top.

Status: draft. {{pending: agree on the target distribution for this project}}

## Shape

```
          /\        end-to-end: few, critical journeys only
         /  \
        /----\      contract / integration: component boundaries
       /      \
      /--------\    unit: many, fast, isolated
```

## Layers

| Layer | What it proves | Speed | Target share |
|-------|----------------|-------|--------------|
| Unit | One unit behaves as specified, including edge cases | Milliseconds | {{pending: share, for example most tests}} |
| Integration | Components work together with real wiring | Seconds | {{pending: share}} |
| Contract | Producer and consumer agree on an interface | Seconds | {{pending: share or "not applicable"}} |
| End-to-end | A critical user journey works through the real interface | Seconds to minutes | {{pending: share, kept small}} |

## Guidelines

- Push each check to the lowest layer that can catch the defect.
- Use end-to-end tests for journeys whose failure would block users, not for every branch.
- Avoid the "ice cream cone": many slow UI tests and few unit tests make the suite fragile and slow.
- A flaky test is a defect. Quarantine it with a recorded reason and owner, and fix it; do not delete or weaken it silently.
- Coverage is a signal, not a goal. {{pending: decide whether a coverage floor exists and where it applies}}

## Critical journeys

List the journeys that deserve end-to-end coverage.

| Journey | Feature | Why critical |
|---------|---------|--------------|
| {{pending: journey}} | [Feature](../05-features/example/feature-spec.md) | {{pending: reason}} |

## Related

- [Verification ladder](verification-ladder.md)
- [TDD guide](tdd-guide.md)
- [Acceptance strategy](acceptance-strategy.md)
- [Test plan](test-plan.md)
