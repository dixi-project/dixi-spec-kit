# Content guidelines

## Purpose

Define how the product speaks: voice, tone, terminology and formatting for interface text, help content and messages in every supported language, so that the product sounds like one product and translations stay consistent.

Status: draft. {{pending: name the person who approves interface text and the reviewer for each language}}

## Voice

Voice is constant; tone adapts to the situation.

| Trait | Means | Does not mean |
|-------|-------|---------------|
| {{pending: for example clear}} | Short sentences, common words | Oversimplifying or hiding details |
| {{pending: for example helpful}} | Tells the user what to do next | Lecturing |
| {{pending: for example respectful}} | Neutral, inclusive language | Jokes at the user's expense |

## Tone by situation

| Situation | Tone | Example |
|-----------|------|---------|
| Success | Brief, positive | "Changes saved." |
| Error the user can fix | Calm, specific, actionable | "Enter a date after today." |
| System failure | Honest, apologetic, with next step | "We couldn't load your reports. Try again in a few minutes." |
| Destructive action | Serious, explicit consequence | "Delete project? This removes all its files." |

## Writing rules

- Use the second person and active voice.
- Put the most important word first; buttons start with a verb ("Save changes", not "OK").
- Avoid jargon, internal names and abbreviations unknown to users.
- Use inclusive, gender-neutral wording where the language allows it.
- Never blame the user in error messages.

{{pending: decide the form of address in each language, for example formal or informal "you" in Spanish}}

## Internationalization

- All interface text lives in per-language catalogs; no hardcoded strings in components.
- Write source text that translates well: complete sentences, no string concatenation, placeholders with names (`{count} files`).
- Handle plurals and gender through the catalog's plural rules, not with code.
- Plan for text expansion of 30% or more; never fix widths around one language.
- Dates, numbers, currencies and units follow the user's locale.
- Each language is reviewed by a fluent person; machine translation alone is not enough for release.

## Terminology

Keep a glossary of product terms and their approved translation.

| Term (en) | Term (es) | Definition | Avoid |
|-----------|-----------|------------|-------|
| {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Formatting

- Sentence case for headings and buttons.
- {{pending: decide the style for lists, numbers and punctuation in each language}}

## Related

- [Design principles](design-principles.md)
- [Accessibility standard](accessibility-standard.md)
- [Information architecture](information-architecture.md)
- [Internationalization policy](../00-governance/policies/i18n-policy.md)
- [Glossary](../18-knowledge-base/glossary.md)
