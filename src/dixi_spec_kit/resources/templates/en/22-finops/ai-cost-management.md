# AI cost management

## Purpose

Keep the cost of language models and other AI services predictable: choose the right model for each task, measure usage per feature and stop runaway spending quickly.

Status: draft. {{pending: name the owner of AI costs}}

## Why it needs its own document

AI cost grows with usage and prompt size rather than with servers, can change in minutes because of a loop or an abusive user, and differs by orders of magnitude between models for the same task.

## Model tiers

| Tier | Use for | Relative cost | Model in use |
|------|---------|---------------|--------------|
| Small | Classification, extraction, routing, short answers | Low | {{pending: model}} |
| Medium | Most generation and summarisation tasks | Medium | {{pending: model}} |
| Large | Complex reasoning, long documents, high-stakes output | High | {{pending: model}} |

Start each feature on the smallest tier that passes its quality checks, and move up only with evidence. {{pending: define the quality checks per feature}}

## Cost levers

1. **Prompt caching** for long, repeated instructions or context, where the provider supports it.
2. **Routing** easy requests to a smaller model and hard ones to a larger model.
3. **Batch processing** for work that does not need an immediate answer, when cheaper batch pricing exists.
4. **Shorter context**: retrieve only relevant passages instead of whole documents.
5. **Output limits**: set a maximum output length per use case.
6. **Response caching** for identical, deterministic requests.

## Limits and budgets

| Scope | Limit | Action when reached |
|-------|-------|---------------------|
| Per user or tenant per day | {{pending: tokens or requests}} | {{pending: throttle / block / notify}} |
| Per feature per month | {{pending: amount}} | Alert to the feature owner |
| Whole project per month | {{pending: amount}} | See [budget alerts](budget-alerts.md) |

## Metrics

- Cost per feature, per request and per active user.
- Input and output tokens, cache hit rate, error and retry rate.
- Share of requests per model tier.

## Anti-patterns

- Retrying failed calls without a limit or backoff.
- Sending the whole conversation or document every time.
- Exposing a public endpoint that calls a paid model without authentication or rate limits.
- Choosing the largest model "to be safe" without measuring.

## Monthly review

Review the metrics with the [cost report template](templates/cost-report-template.md) and record model changes as decisions.

## Related

- [Cost strategy](cost-strategy.md)
- [Budget alerts](budget-alerts.md)
- [Cost spike playbook](../15-operations/playbooks/cost-spike.md)
- [Guardrails](../21-ai/agents/guardrails.md)
