# Spec lifecycle

## Purpose

Define the states a specification moves through, what must be true to advance, and how drift between spec and code is detected. States describe documents; they never claim that tests or reviews were executed unless evidence exists.

## States

| State | Meaning | Who may move it forward |
| --- | --- | --- |
| Draft | Being written; may contain `{{pending: ...}}` markers | Author |
| Review | Complete enough to be read and challenged | Author requests, reviewer reads |
| Approved | Accepted as the reference for tests and code | A responsible person |
| Implemented | Code and passing tests exist and match the spec | Person, with evidence |
| Deprecated | Kept for history; replaced or retired | A responsible person |

## Exit criteria

### Draft → Review

- [ ] Starts with a title and a Purpose section.
- [ ] Names its parent spec and keeps its ID.
- [ ] Local links resolve (`dixi check` reports broken structure).

### Review → Approved

- [ ] No pending markers in fields that block tests (criteria, inputs, errors).
- [ ] Consistent with its parent; terms match the domain glossary.
- [ ] Registered in `.dixi/traceability.json`.
- [ ] Reviewed by a person; an agent review alone is not enough.

### Approved → Implemented

- [ ] Tests derived from the contract exist and were seen failing first.
- [ ] The project's real checks pass, and the result is reported as observed.
- [ ] No known drift between spec and behaviour.

## Versioning

- Specs live in version control; the pull request history is the change log.
- A breaking change to an approved contract creates a new version or a new contract ID: {{pending: versioning convention for contracts}}

## Drift

Drift means the code no longer does what the spec says. Signals: tests that were edited without a spec change, behaviour found in code but not in any spec, or specs that mention removed features. When drift is found, update the spec or the code in the same change and record why.

- How often specs are reviewed for drift: {{pending: review cadence}}

## Related

- [Methodology](methodology.md)
- [Validation rules](validation-rules.md)
- [Traceability matrix](traceability-matrix.md)
- [Test plan](../../11-quality/test-plan.md)
