# Help center structure

## Purpose

Define how the help center is organised, how articles are written and localised, and how it is kept accurate. A good help center lets people solve problems on their own, in their language, and is findable from search engines and from inside the product.

Status: draft. {{pending: decide whether the help center is part of the main site or separate, and who owns it}}

## URL structure

- Articles live under a language prefix: `/en/help/...`, `/es/help/...`.
- Each article has a canonical URL for its language and reciprocal `hreflang` alternates, including `x-default`.
- Articles are server-rendered or pre-rendered so search engines index translated text.
- Slugs are readable and stable; renamed articles redirect to the new URL in the same language.

## Taxonomy

| Level | Example |
|-------|---------|
| Category | Getting started, Account, Billing, Features, Troubleshooting |
| Section | {{pending: group within a category}} |
| Article | One task or one question |

{{pending: define the first categories based on the most common questions}}

## Article structure

1. Title that matches how people phrase the question.
2. One-sentence summary of what the article solves.
3. Prerequisites, if any.
4. Numbered steps, one action each.
5. Troubleshooting for common failures.
6. Related articles in the same language.
7. How to contact support if the problem persists.

## Writing rules

- Plain language, short sentences, consistent terms from the glossary.
- Screenshots and media have alternative text and are updated when the interface changes.
- No personal data, secrets or real customer details in examples.

## Localisation

- Each article exists in every supported language, or is clearly marked as unavailable in that language.
- Translations are reviewed by a fluent person; terms follow the glossary per language.
- When the source article changes, its translations are flagged as outdated until reviewed.

## In-product links

- Screens link to the article that explains them, in the user's language.
- Error messages may link to a troubleshooting article.

## Maintenance

| Task | Frequency | Owner |
|------|-----------|-------|
| Review top articles for accuracy | {{pending}} | {{pending}} |
| Review searches with no results | {{pending}} | {{pending}} |
| Update after each release | Every release | {{pending}} |

## Related

- [Support tiers](support-tiers.md)
- [Customer success strategy](success-strategy.md)
- [Content guidelines](../17-ux/content-guidelines.md)
- [Glossary](../18-knowledge-base/glossary.md)
- [FAQ](../18-knowledge-base/faq.md)
- [i18n policy](../00-governance/policies/i18n-policy.md)
