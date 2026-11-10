# Validation rules

## Purpose

List the checks a specification must pass, separating what a tool verifies from what a person must judge. `dixi check` covers structure only; it does not prove that behaviour is correct.

## Types of validation

| Type | Examples | How |
| --- | --- | --- |
| Structural | Title, Purpose and Related sections, resolvable links, valid JSON | Automated (`dixi check`) |
| Traceability | Every item has a valid parent; IDs are unique | Automated |
| Completeness | Required sections filled; no blocking pending markers | Checklist plus review |
| Semantic | Consistent with parent, unambiguous criteria, glossary terms | Human review |

## Checklists by spec kind

### Domain

- [ ] One-sentence purpose and boundary (what is in, what is out).
- [ ] Main entities and domain events named.
- [ ] Glossary of terms.

### Module

- [ ] Parent domain referenced.
- [ ] Responsibilities and explicit non-responsibilities.
- [ ] Public interfaces and dependencies.

### Feature

- [ ] User story or need statement.
- [ ] Observable acceptance criteria (for example Given / When / Then).
- [ ] Edge cases and error behaviour.

### Contract

- [ ] Inputs, outputs and error cases with types.
- [ ] Compatibility rule for future changes.
- [ ] Linked test entry.

## Severity

- **Blocking**: missing parent, broken link, ambiguous acceptance criteria.
- **Warning**: missing glossary entry, unclear non-responsibilities.

{{pending: which warnings become blocking for this project}}

## Who validates

- Agents may run the automated checks and point out gaps; they report results as observed.
- A person decides semantic validity and approves. {{pending: reviewer role per spec kind}}

## Related

- [Spec lifecycle](spec-lifecycle.md)
- [Traceability matrix](traceability-matrix.md)
- [Methodology](methodology.md)
- [Project instructions](../../AGENTS.md)
