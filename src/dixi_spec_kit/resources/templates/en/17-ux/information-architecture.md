# Information architecture

## Purpose

Describe how the product's content and functions are organized, labelled and found, so that users reach what they need quickly and the structure stays coherent as the product grows and is translated.

Status: draft. {{pending: validate the top-level structure with users before building navigation}}

## Content inventory

List the main content types and functions before deciding the structure.

| Item | Type | Audience | Owner | Languages | Notes |
|------|------|----------|-------|-----------|-------|
| {{pending: for example account settings}} | Function | Signed-in users | {{pending}} | es, en | — |
| {{pending: for example help articles}} | Content | Everyone | {{pending}} | es, en | — |

## Organization scheme

{{pending: choose how content is grouped, for example by task, by audience or by topic}}

- Group by the user's mental model, discovered through research, not by internal team structure.
- Keep the top level small (about five to seven sections).
- Avoid "Miscellaneous" or "Other" sections; they signal an unclear structure.

## Hierarchy

```text
/{lang}/
├── {{pending: section 1}}/
│   ├── {{pending: page}}
│   └── {{pending: page}}
├── {{pending: section 2}}/
└── help/
```

## URL and language rules

- Every public page lives under a language prefix, for example `/es/` and `/en/`.
- The root `/` redirects to the best match for the browser's language.
- Each language version has its own canonical URL and `hreflang` alternates to the others.
- Slugs may be translated; record the mapping so alternates stay linked.
- Changing a URL requires a permanent redirect from the old one.

{{pending: decide whether slugs are translated or kept identical across languages}}

## Labelling

- Labels use the words users use, confirmed through research such as card sorting or tree testing.
- The same item has the same label everywhere it appears.
- Labels are translated through the catalog and checked for length in every language.

## Search and findability

{{pending: decide whether the product needs search and which content it indexes}}

## Validation

| Method | Question it answers | Status |
|--------|---------------------|--------|
| Card sorting | How do users group the content? | {{pending}} |
| Tree testing | Can users find items in the proposed structure? | {{pending}} |

## Related

- [Navigation map](navigation-map.md)
- [Content guidelines](content-guidelines.md)
- [Design principles](design-principles.md)
- [SEO strategy](../25-growth/seo-strategy.md)
- [Discovery strategy](../24-research/discovery-strategy.md)
