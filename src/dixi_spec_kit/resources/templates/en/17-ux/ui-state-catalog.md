# UI state catalog

## Purpose

List the states every screen and component must handle beyond the happy path (empty, loading, error, partial, offline and others), so that specs describe them, designs include them and tests cover them in every supported language.

Status: draft. {{pending: confirm which states are mandatory for every screen and which only when relevant}}

## Standard states

| State | When it happens | What the user sees | Accessibility note |
|-------|-----------------|--------------------|--------------------|
| Empty (first use) | No data yet | Explanation and the first action to take | Message is real text, not only an illustration |
| Empty (no results) | Filter or search returns nothing | What was searched and how to broaden it | Result count announced |
| Loading | Data is being fetched | Skeleton or progress indicator after a short delay | Busy state announced; no focus loss |
| Partial | Some data loaded, some failed | Available data plus a notice for the missing part | Notice reachable by keyboard |
| Error (recoverable) | Request failed, retry possible | What happened and a retry action | Error announced; focus moved to the message when it blocks the task |
| Error (fatal) | Cannot continue | Apology, next step, way back | Page title reflects the error |
| Offline | No connection | Notice and what still works | Announced once, not on every change |
| Success | Action completed | Brief confirmation | Status message, not a modal unless required |
| Permission denied | User lacks access | Why and how to request access | — |
| Validation | Input is invalid | Message next to the field and a summary | Field linked to its message |

## Per-screen matrix

Fill one row per screen from the navigation map.

| Screen ID | Empty | Loading | Partial | Error | Offline | Success | Permission | Spec |
|-----------|-------|---------|---------|-------|---------|---------|------------|------|
| {{pending: SCR-001}} | {{pending: yes, n/a}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Rules

- Every state's text comes from the translation catalog and is reviewed in every language.
- Loading indicators appear only after a short delay to avoid flicker. {{pending: set the delay}}
- Errors never show stack traces, internal codes alone or raw server messages.
- Each state has at least one test: unit or component level for rendering, end-to-end for key flows.
- Long-running actions show progress and can be cancelled when possible.

## Defining a new state

1. Check this catalog for an existing state that fits.
2. Describe trigger, content and accessibility behaviour.
3. Add it here and to the affected feature specs before designing it.

## Related

- [Design tokens](design-tokens.md)
- [Navigation map](navigation-map.md)
- [Content guidelines](content-guidelines.md)
- [Accessibility standard](accessibility-standard.md)
- [Test pyramid](../11-quality/test-pyramid.md)
