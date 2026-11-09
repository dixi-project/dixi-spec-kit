# Pricing rules

## Purpose

Describe how prices, plans, discounts, taxes and limits are calculated, so that billing logic can be
specified and tested without guessing. Pricing changes often and has direct financial and legal
impact: keep every rule explicit, versioned and owned by a person who can approve changes.

## Pricing model

- Model: {{pending: free, one-time, subscription, usage-based, tiered or hybrid}}
- Currency or currencies: {{pending: currencies and who bears exchange rate risk}}
- Billing period: {{pending: monthly, annual, per transaction}}
- Taxes: {{pending: whether prices include taxes and who determines the applicable rate}}

## Plans

| Plan | Price | Included limits | Features | Who can buy it |
|---|---|---|---|---|
| {{pending: plan}} | {{pending: price}} | {{pending: limits}} | {{pending: features}} | {{pending: segment}} |

## Rules

| ID | Rule | Example | Owner |
|---|---|---|---|
| PR-001 | {{pending: e.g. how proration works on upgrade}} | {{pending: worked example with numbers}} | {{pending: role}} |
| PR-002 | {{pending: e.g. what happens when a limit is exceeded}} | {{pending: worked example}} | {{pending: role}} |
| PR-003 | {{pending: e.g. how discounts combine}} | {{pending: worked example}} | {{pending: role}} |

## Calculation conventions

- Rounding: {{pending: rounding mode and at which step it applies}}
- Precision: store amounts as integers in the smallest unit or as exact decimals, never as floats.
- Effective dates: a price change applies from {{pending: when}} and does not alter past invoices.
- Grandfathering: {{pending: whether existing customers keep old prices and for how long}}

## Edge cases to specify

- Trials, refunds, cancellations mid-period and failed payments.
- Free or internal accounts and how they are excluded from revenue reports.
- Plan changes across currencies or tax regions.

## Change control

- Who approves pricing changes: {{pending: role}}
- Notice period for customers: {{pending: duration and channel}}

## Related

- [Business rules](business-rules.md)
- [Value proposition](../value-proposition.md)
- [Strategic goals](../strategic-goals.md)
