# Page template

## Purpose

Specify one page of a site or application: its goal, content, behavior per language and how it is
checked. Useful for content sites and for the public pages of any product. Copy the structure
below for each page.

## Template

```markdown
# Page: <human name>

ID: {{pending: page or feature ID}}
Route: /<lang>/<path>
Languages: {{pending: supported locales, e.g. es, en}}
Owner: {{pending: person responsible for the content}}

## Goal

What the visitor must be able to understand or do on this page, and the metric
that tells it works (e.g. contact form submitted, document downloaded).

## Audience

Who arrives here and from where (search, campaign, internal link).

## Content

| Block | Content | Source of the text |
|---|---|---|
| Hero | | translation catalog key |
| ... | | |

## Behavior

- Interactions, forms and validations.
- Empty, loading and error states.

## SEO and internationalization

- Title and meta description per language.
- Canonical URL per language and `hreflang` alternates.
- Rendered on the server so crawlers see translated content.

## Accessibility

- Heading order, alternative texts, keyboard navigation, contrast.

## Checks

- [ ] Each acceptance point has an automated or manual check.
- [ ] Page renders in every supported language without hardcoded strings.
```

## Related

- [Feature template](feature-template.md)
- [Coding standards](../coding-standards.md)
- [Test plan](../../11-quality/test-plan.md)
