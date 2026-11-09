# BDD guide

## Purpose

Describe how this project uses behaviour-driven development to turn acceptance criteria into shared, executable examples that people outside engineering can read.

Status: draft. {{pending: decide whether BDD scenarios are executable or documentation only}}

## When to use BDD

- Behaviour that business people need to read and confirm.
- Rules with several cases that are easier to understand as examples.
- Critical journeys that also deserve acceptance tests.

Skip BDD for pure technical details; a unit test is cheaper and clearer.

## Scenario shape

```
Scenario: <observable behaviour>
  Given <initial context>
  When <action>
  Then <observable outcome>
```

- One behaviour per scenario.
- Use the domain's language, not UI details ("the order is confirmed", not "click the green button").
- Use example tables for rule variations instead of copying scenarios.
- Reference the criterion ID from the feature spec in each scenario.

## Workflow

1. Product, engineering and quality discuss examples before building.
2. Scenarios are written and reviewed with the person responsible for the feature.
3. Scenarios are committed red, following the [TDD guide](tdd-guide.md).
4. Step implementations call the system through its real interface or a stable boundary.
5. Committed scenarios are frozen like any other test.

## Tooling

{{pending: choose a scenario runner for the stack, or decide to keep scenarios as reviewed documentation}}

## Anti-patterns

- Scenarios that describe clicks instead of behaviour.
- Long scenarios with many *When* steps.
- Step definitions full of logic that nobody tests.
- Rewriting scenarios after delivery to match what was built.

## Related

- [Acceptance strategy](acceptance-strategy.md)
- [TDD guide](tdd-guide.md)
- [Test pyramid](test-pyramid.md)
- [Regression plan](regression-plan.md)
- [Feature](../05-features/example/feature-spec.md)
