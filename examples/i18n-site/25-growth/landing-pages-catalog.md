# Landing pages catalog

## Purpose

Keep one inventory of the project's landing pages: what each one is for, which languages it exists in, which conversion it pursues and who maintains it. A landing page that is not in this catalog has no owner and should not be published.

Status: draft. {{pending: list the first landing pages and their owners}}

## Mandatory rules

- Every landing page exists under a language prefix, with the same structure in each language.
- Each version has its own canonical URL and reciprocal `hreflang` alternates, including `x-default`.
- Content is server-rendered or pre-rendered and comes from translation catalogs.
- Each page has one primary call to action and one tracked conversion event.
- Pages meet the accessibility standard and the performance budgets.

## Catalog

| ID | Purpose | Audience | Languages | URL pattern | Conversion event | Owner | Status |
|----|---------|----------|-----------|-------------|------------------|-------|--------|
| LP-001 | Home | All visitors | ES, EN | `/{lang}/` | {{pending}} | {{pending}} | {{pending}} |
| LP-002 | {{pending: product or feature}} | {{pending}} | ES, EN | `/{lang}/{{pending}}` | {{pending}} | {{pending}} | {{pending}} |
| LP-003 | {{pending: campaign}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

Status values: draft, live, testing, retired. Retired pages redirect to the closest live page in the same language.

## Recommended anatomy

1. Headline that states the outcome for the visitor.
2. Short supporting text and a primary call to action.
3. Evidence: how it works, examples, honest limits.
4. Answers to the most common objections.
5. Repeated call to action and links to related pages in the same language.

## Tracking

- Record the conversion rate per language and per channel, not only overall.
- Campaign parameters are kept consistent across pages.

## Maintenance

{{pending: define how often the catalog is reviewed and who approves new pages}}

During each review, check: broken links, outdated claims, untranslated text, missing alternates and pages without traffic or purpose.

## Related

- [SEO strategy](seo-strategy.md)
- [Conversion funnel](conversion-funnel.md)
- [Content strategy](content-strategy.md)
- [Page template](../10-engineering/templates/page-template.md)
- [Accessibility standard](../17-ux/accessibility-standard.md)
- [i18n policy](../00-governance/policies/i18n-policy.md)
