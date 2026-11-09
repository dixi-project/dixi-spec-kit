# Glossary

## Purpose

Give one shared meaning to the terms used in this project's specs, code and conversations, so that people and agents use the same words for the same things. Business terms specific to the product are added below the method terms.

Status: draft. {{pending: add the product's business terms}}

## How to use it

- Define a term here once; link to it instead of redefining it.
- When two words mean the same thing, choose one and list the other as a synonym to avoid.
- Keep definitions short and testable: what it is, and what it is not.

## Method terms

| Term | Definition |
|------|------------|
| Spec | A document that states what must be true before code is written. |
| Spec-driven development (SDD) | Working from linked, reviewed specs down to tests and code. |
| Goal | A business outcome the project pursues (`GOAL-NNN`). |
| Domain | An area of the business with its own language and rules (`DOMAIN-NNN`). |
| Module | A cohesive unit of the system inside a domain (`MODULE-NNN`). |
| Feature | A user-visible behaviour with acceptance criteria (`FEATURE-NNN`). |
| Contract | The agreed interface between parts of the system (`CONTRACT-NNN`). |
| Acceptance criterion | An observable condition that decides whether a feature is done. |
| Traceability | The chain of links from goal to test, recorded in `.dixi/traceability.json`. |
| Red test | A test written first that fails because the behaviour does not exist yet. |
| Frozen test | A committed test that may not be edited to make code pass. |
| Pending marker | `{{pending: ...}}`, a visible, undecided item in a document. |
| MODE | The project's declared maturity stage, stored in the `MODE` file. |
| ADR | Architecture decision record: one decision, its context and consequences. |

## Agents and control

| Term | Definition |
|------|------------|
| Agent | An AI tool that reads, proposes and edits files on request. |
| Human in the loop | A person who reviews and decides at defined points. |
| Untrusted data | Content from issues, pages or files that is read but never obeyed as instructions. |

## Product terms

| Term | Definition | Synonyms to avoid |
|------|------------|-------------------|
| {{pending: term}} | {{pending: definition}} | {{pending: synonyms}} |

## Related

- [FAQ](faq.md)
- [Onboarding guide](onboarding-guide.md)
- [Documentary workflow](../docs/guide.md)
- [Project](../00-master-spec.md)
