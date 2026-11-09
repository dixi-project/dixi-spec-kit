# Navigation map

## Purpose

Record every screen or page, how users move between them and which navigation elements connect them, so that no screen is orphaned, every path has a way back and links stay correct in every language.

Status: draft. {{pending: confirm the list of screens for the first release}}

## Global navigation

| Element | Contents | Visible to | Notes |
|---------|----------|------------|-------|
| Primary menu | {{pending: top-level sections}} | {{pending: everyone or signed-in users}} | Same order in every language |
| Language switcher | Supported languages, each in its own name | Everyone | Links to the same page in the other language, not to the home page |
| Footer | {{pending: legal, help, contact}} | Everyone | — |
| Account menu | {{pending}} | Signed-in users | — |

## Screen inventory

| ID | Screen | Path pattern | Entry points | Exits | Auth | Template |
|----|--------|--------------|--------------|-------|------|----------|
| SCR-001 | Home | `/{lang}/` | Root redirect, logo | Primary menu | No | {{pending}} |
| SCR-002 | {{pending}} | `/{lang}/{{pending}}` | {{pending}} | {{pending}} | {{pending}} | {{pending}} |
| SCR-404 | Not found | any unknown path | Broken links | Home, search | No | Error |

## Key flows

Describe the main user journeys as ordered steps.

```text
Flow: {{pending: for example sign up}}
SCR-001 Home → SCR-00x Sign up → SCR-00y Confirm e-mail → SCR-00z Welcome
```

- Each flow states its start, its success end and what happens on failure or cancel.
- Each step can be reached and left with a keyboard alone.
- Back navigation keeps the user's data where reasonable.

## Rules

- Every screen has at least one entry point and one exit; orphan screens are defects.
- Breadcrumbs or a visible title tell users where they are.
- Deep links work: opening a URL directly shows the right screen in the right language, or asks the user to sign in and then returns them.
- Redirects after sign-in keep the language prefix.

{{pending: decide the behaviour when a page exists in one language but not in another}}

## Maintenance

- Update this map in the same change that adds, renames or removes a screen.
- Keep screen IDs stable; reference them from feature specs and tests.

## Related

- [Information architecture](information-architecture.md)
- [Accessibility standard](accessibility-standard.md)
- [Design principles](design-principles.md)
- [Page template](../10-engineering/templates/page-template.md)
- [Example feature spec](../05-features/example/feature-spec.md)
