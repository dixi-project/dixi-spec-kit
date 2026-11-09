# Release notes

## Purpose

Tell users and internal teams what changed in each release, in plain language and in every supported language, so nobody has to read commits to know what is new, fixed or removed.

Status: draft. {{pending: decide where release notes are published and who approves them}}

## Audiences

| Audience | What they need | Channel |
|----------|----------------|---------|
| End users | What they can do now, what changed for them | {{pending: in-product, website, e-mail}} |
| Support and sales | What to tell customers, known issues | {{pending: internal channel}} |
| Integrators | Contract changes, deprecations, migration steps | {{pending: changelog file, developer portal}} |

## Writing rules

- Lead with the benefit to the user, not with the internal change.
- One entry per user-visible change; group trivial fixes.
- Mark breaking changes and deprecations clearly and say what the user must do.
- Write the source text once, then translate it through the normal translation catalog process; never publish one language only without saying so.
- Do not mention internal ticket numbers, people or vendors.
- Version numbers follow the project versioning policy.

## Entry template

Copy this block for each release.

```markdown
## <version> — <YYYY-MM-DD>

### New
- <what users can now do and why it matters>

### Improved
- <change to existing behaviour>

### Fixed
- <problem users experienced, now solved>

### Deprecated or removed
- <what is going away, when, and what to use instead>

### Known issues
- <problem, workaround, expected fix>
```

## Example entry

```markdown
## 1.4.0 — 2026-01-15

### New
- You can export your reports as a spreadsheet.

### Fixed
- Dates now show in the format of the language you selected.
```

## Review checklist

- Every entry maps to a merged change and, where relevant, to a feature spec.
- All supported languages are present and reviewed by a fluent reader.
- Breaking changes include migration steps.
- {{pending: add any legal or contractual notice that must appear in every release}}

## Related

- [Feature lifecycle](feature-lifecycle.md)
- [Roadmap](roadmap.md)
- [Versioning policy](../00-governance/policies/versioning-policy.md)
- [Content guidelines](../17-ux/content-guidelines.md)
- [Internationalization policy](../00-governance/policies/i18n-policy.md)
