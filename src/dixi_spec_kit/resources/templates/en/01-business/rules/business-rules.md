# Business rules

## Purpose

Collect the rules that govern how the business operates, written so that a person can validate
them and a test can check them. A business rule is a constraint, calculation or decision that holds
regardless of the screen or system that applies it. Keeping rules here, with IDs, avoids burying
them in code where nobody can review them.

## How to write a rule

- One rule per row, with a stable ID (`BR-NNN`).
- Use the ubiquitous language and an unambiguous form: "When X, then Y", "X must never Y".
- State the source (policy, contract, regulation, decision) and the owner who can change it.
- Link each rule to the features and tests that enforce it.
- Prefer concrete values ("within 30 days") over vague ones ("soon").

## Rule types

| Type | Example shape |
|---|---|
| Constraint | An order cannot be confirmed without at least one item. |
| Derivation | The total equals the sum of items minus discounts. |
| Decision | If the amount exceeds a threshold, a second approval is required. |
| Timing | A reservation expires after a defined period without payment. |

## Rule catalog

| ID | Rule | Type | Domain | Source | Owner | Enforced by |
|---|---|---|---|---|---|---|
| BR-001 | {{pending: rule statement}} | {{pending: type}} | {{pending: domain}} | {{pending: source}} | {{pending: role}} | {{pending: FEATURE or test ID}} |
| BR-002 | {{pending: rule statement}} | {{pending: type}} | {{pending: domain}} | {{pending: source}} | {{pending: role}} | {{pending: FEATURE or test ID}} |

## Examples per rule

Write at least one positive and one negative example for each rule; they become acceptance tests.

| Rule | Given | When | Then |
|---|---|---|---|
| {{pending: BR ID}} | {{pending: context}} | {{pending: action}} | {{pending: expected outcome}} |

## Change control

- Who approves rule changes: {{pending: role}}
- How changes are communicated to affected teams: {{pending: channel}}

## Related

- [Operational constraints](operational-constraints.md)
- [Pricing rules](pricing-rules.md)
- [Ubiquitous language](../domains/ubiquitous-language.md)
- [Feature example](../../05-features/example/feature-spec.md)
