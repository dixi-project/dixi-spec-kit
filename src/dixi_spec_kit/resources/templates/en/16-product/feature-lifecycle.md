# Feature lifecycle

## Purpose

Describe the stages a feature goes through from idea to retirement, what must be true to move from one stage to the next and who decides. This keeps specs, code, tests and documentation in step.

Status: draft. {{pending: confirm the stages and the approver for each gate}}

## Stages

| Stage | Entry criteria | Exit criteria | Artifacts |
|-------|----------------|---------------|-----------|
| Idea | Problem noted with some evidence | Accepted into the roadmap | Roadmap item |
| Discovery | Roadmap item in "Next" or "Now" | Problem and outcome validated | Research notes, `/dixi.discover` output |
| Specified | Validated problem | Spec reviewed, acceptance criteria agreed | Feature spec (`/dixi.specify`) |
| Building | Approved spec and tests written first | Tests green, review approved | Code, tests, traceability entries |
| Released | Merged and deployed | Adoption measured against the outcome | Release notes, analytics events |
| Retired | Decision to remove | Code, docs and translations removed | Decision record, migration notes |

## Gates

Each gate needs a human decision. Agents may prepare the evidence but never approve a gate.

- **Discovery → Specified**: the outcome is measurable and the target users are named.
- **Specified → Building**: acceptance criteria are observable; structural decisions are recorded.
- **Building → Released**: `make verify` passes, accessibility and translation checks are done for every supported language.
- **Released → Retired**: users affected are informed and data handling is decided.

{{pending: name who approves each gate}}

## Release exposure

{{pending: decide whether features can ship behind flags, to a percentage of users or only to everyone at once}}

When flags are used:

- Every flag has an owner and a removal date.
- A flag that has been fully on for longer than the agreed period is removed.

## Measuring success

Each released feature declares in its spec:

- The outcome from the roadmap it serves.
- The events that show it is being used (see the [analytics events catalog](analytics-events-catalog.md)).
- The review date when the result will be compared with the expectation.

## Retirement checklist

- Usage data reviewed and decision recorded.
- Users notified in every supported language.
- Code, tests, translation keys and docs removed together.
- Traceability entries updated with `dixi check` passing.

## Related

- [Roadmap](roadmap.md)
- [Prioritization framework](prioritization-framework.md)
- [Release notes](release-notes.md)
- [Example feature spec](../05-features/example/feature-spec.md)
- [Test plan](../11-quality/test-plan.md)
- [Guide](../docs/guide.md)
