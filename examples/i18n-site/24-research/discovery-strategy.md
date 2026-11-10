# Discovery strategy

## Purpose

Explain how the project learns about its users and their problems before committing to build, so that specs rest on evidence rather than assumptions, and so that every supported market and language is considered from the start.

Status: draft. {{pending: name the person responsible for discovery and the time reserved for it}}

## Questions to answer

Discovery is driven by questions, not by methods. Start from the riskiest assumptions.

| Assumption | Risk if wrong | Question | How we will learn |
|------------|---------------|----------|-------------------|
| {{pending: for example users struggle to compare offers}} | {{pending: high, medium, low}} | {{pending}} | {{pending: interviews, analytics, prototype test}} |
| {{pending}} | {{pending}} | {{pending}} | {{pending}} |

Assumption types to cover:

- **Value**: will people want this?
- **Usability**: can people use it?
- **Feasibility**: can we build and run it?
- **Viability**: does it work for the business, legally and financially?

## Methods

Choose the lightest method that answers the question.

| Method | Good for | Effort |
|--------|----------|--------|
| Desk research | Context, existing evidence | Low |
| Interviews | Motivations, current behaviour, pain points | Medium |
| Surveys | Size of a known problem | Medium |
| Analytics review | What users actually do | Low to medium |
| Prototype or usability test | Whether a solution works | Medium |

## Participants

- Recruit from the real target audience, including each language and market served.
- Include people who use assistive technologies.
- {{pending: decide how participants are recruited and whether they are compensated}}
- Obtain informed consent and store only the personal data needed.

## Cadence

{{pending: choose a rhythm, for example a few user conversations every week or a discovery phase per roadmap item}}

## From findings to specs

1. Record each study and its findings in the research notes, with date and evidence.
2. Turn findings into problem statements and update personas.
3. Use `/dixi.discover` (or the equivalent workflow) to prepare the discovery context for a goal.
4. Link the evidence from the business goal and feature specs it supports.

## Ethics

- Never record or share participant data without consent.
- Anonymize quotes before sharing them outside the research team.
- Do not present a single conversation as a validated finding.

## Related

- [Persona template](persona-template.md)
- [Business goal](../01-business/vision.md)
- [Value proposition](../01-business/value-proposition.md)
- [Personas](../01-business/actors/personas.md)
- [Guide](../docs/guide.md)
