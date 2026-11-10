# Documentation policy

## Purpose

Define how project documents are written, named, linked and kept up to date, so that specs stay readable for people and usable by agents, and `dixi check` can follow the traceability chain.

Status: draft. {{pending: confirm the documentation rules with the team}}

## Language

- Primary documentation language: {{pending: primary language}}
- Documents that must also exist in other languages: {{pending: list}}
- Translations keep the same sections and IDs as the original.

## Format

- Markdown, one topic per file, lowercase `kebab-case` file names.
- Every document starts with `# Title`, then `## Purpose`, and ends with `## Related`.
- Use tables and checklists for rules; use prose for reasoning.
- Wrap commands, paths and identifiers in backticks.

## Minimum structure

```markdown
# <Title>

## Purpose

<Why this document exists, in one or two sentences.>

Status: draft | review | approved.

## <Content sections>

## Related

- <relative link to a related document>
```

## Open decisions

- Mark every undecided item as `{{pending: what to decide}}`.
- Do not invent values to fill a gap. A visible gap is better than a wrong answer.
- Resolve pending markers before a document moves to `approved`.

## Links

- Use relative links to local files; check they resolve.
- Link both ways between parent and child specs (goal, domain, module, feature, contract, test).

## Traceability

- Specs keep stable IDs (for example `FEATURE-001`).
- Register each traceable item and its parents in `.dixi/traceability.json`.
- Run `dixi check` before requesting review.

## Ownership and review

| Document type | Owner | Review trigger |
|---------------|-------|----------------|
| Governance | {{pending: owner}} | Any change |
| Specs | Feature owner | Before implementation |
| Runbooks | {{pending: owner}} | After each incident |

## Related

- [Naming conventions](naming-conventions.md)
- [i18n policy](i18n-policy.md)
- [Documentary workflow](../../docs/guide.md)
- [Project](../../00-master-spec.md)
