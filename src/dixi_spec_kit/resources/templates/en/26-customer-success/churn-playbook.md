# Churn playbook

## Purpose

Define how the project detects customers at risk of leaving, which actions respond to each warning signal, and how cancellations are handled respectfully. The goal is to fix the reasons people leave, not to make leaving hard.

Status: draft. {{pending: define what counts as churn for this product and the target churn rate}}

## Types of churn

| Type | Definition |
|------|------------|
| Voluntary | The customer decides to cancel or stop using the product |
| Involuntary | Access ends for other reasons, such as a failed payment |
| Contraction | The customer stays but reduces use or plan |

## Metrics

| Metric | Definition | Target |
|--------|------------|--------|
| Customer churn rate | Customers lost in a period / customers at start | {{pending}} |
| Revenue churn rate, if applicable | Revenue lost in a period / revenue at start | {{pending}} |
| Recovery rate | At-risk customers who return to healthy | {{pending}} |

Measure by segment, market and language.

## Warning signals

- Sharp drop in active use or no activity for {{pending: days}}.
- Key feature never adopted after onboarding.
- Repeated or unresolved support requests.
- Low satisfaction feedback.
- Failed payment or downgrade request.
- Champion contact leaves the customer organisation, for larger accounts.

## Playbooks by trigger

| Trigger | Action | Channel | Owner | Timing |
|---------|--------|---------|-------|--------|
| Inactivity | Helpful message with the next useful step | {{pending}} | {{pending}} | {{pending}} |
| Low satisfaction | Personal follow-up to understand the problem | {{pending}} | {{pending}} | {{pending}} |
| Failed payment | Clear notices and a simple way to update payment | {{pending}} | {{pending}} | {{pending}} |
| Cancellation request | Ask for the reason; offer relevant options once | {{pending}} | {{pending}} | Immediate |

## Cancellation rules

- Cancelling is as easy as signing up and never requires calling or waiting.
- Offers to stay (pause, smaller plan, help) are shown once and can be declined in one step.
- The customer can export their data before leaving, as defined by the retention policy.
- Messages are sent in the customer's language.

## Learning from churn

1. Record the reason for every cancellation using a fixed list plus free text.
2. Review reasons {{pending: frequency}} and link recurring ones to product or support work.
3. Track whether the changes reduce churn for that reason.

## Related

- [Customer success strategy](success-strategy.md)
- [Support tiers](support-tiers.md)
- [Help center structure](help-center-structure.md)
- [Retention policy](../08-data/retention-policy.md)
- [Growth strategy](../25-growth/growth-strategy.md)
