# SEO strategy

## Purpose

Define how public pages become discoverable in search engines in every supported language. International SEO is part of the architecture: language-prefixed URLs, `hreflang`, canonical URLs per language and server-rendered content are requirements, not later improvements.

Status: draft. {{pending: confirm the indexable languages and the priority markets}}

## Technical SEO

- Every public page lives under a language prefix: `/en/...`, `/es/...`.
- The root `/` redirects to the browser language, with a default; the redirect is not cached for everyone.
- Each page declares a canonical URL for its own language, never pointing to another language.
- Each page lists `<link rel="alternate" hreflang="xx">` for every language version and `x-default`; alternates are reciprocal.
- Content is rendered on the server or pre-rendered; crawlers must not need to run scripts to see text.
- A sitemap per language (or one with alternates) lists only canonical, indexable URLs.
- Robots rules block private areas, never public assets needed to render pages.
- Pages meet the performance budgets and are usable on mobile.

## On-page SEO

| Element | Rule |
|---------|------|
| Title | Unique per page and language, describes the content |
| Meta description | Unique, written for people, translated per language |
| Headings | One `h1`, logical hierarchy |
| URL slug | Readable, translated per language when useful |
| Images | Descriptive alternative text per language |
| Structured data | {{pending: decide which schema types apply}} |
| Internal links | Each page links to related pages in the same language |

## Content SEO

- Keyword and intent research is done per language and market, not translated from one language.
- Each topic has one primary page to avoid pages competing with each other.
- Outdated pages are updated, merged with redirects or removed on purpose.

## Metrics

| Metric | Per language | Target |
|--------|--------------|--------|
| Indexed pages vs. published pages | Yes | {{pending}} |
| Organic visits | Yes | {{pending}} |
| Organic conversions | Yes | {{pending}} |
| Pages with technical errors | Yes | {{pending}} |

## Periodic audit

{{pending: define the audit frequency and owner}}

Check broken links, missing or wrong `hreflang`, canonical mistakes, duplicate titles, untranslated text and performance regressions.

## Related

- [Growth strategy](growth-strategy.md)
- [Landing pages catalog](landing-pages-catalog.md)
- [Content strategy](content-strategy.md)
- [i18n policy](../00-governance/policies/i18n-policy.md)
- [Web vitals budgets](../11-quality/performance-budgets/web-vitals-budgets.md)
- [Information architecture](../17-ux/information-architecture.md)
