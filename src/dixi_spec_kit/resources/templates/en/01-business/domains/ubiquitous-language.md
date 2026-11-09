# Ubiquitous language

## Purpose

Keep one shared vocabulary between business people, specs, code and tests. When a term means the
same thing everywhere, specs are easier to review and agents make fewer wrong assumptions. If two
domains use the same word with different meanings, record both and name the domain that owns each.

## Rules

- One term, one meaning per domain. Synonyms are listed, not used interchangeably.
- Code identifiers, API fields and event names reuse these terms (translated only in the UI).
- New terms enter this page before they appear in a contract.
- Ambiguous words ("user", "account", "order") always carry a qualifier or a domain.
- Keep the canonical term in English if the code is in English, and add the translation.

## Glossary

| Term | Definition | Owning domain | Synonyms to avoid | Translation (es) | Example |
|---|---|---|---|---|---|
| {{pending: term}} | {{pending: definition in one sentence}} | {{pending: domain}} | {{pending: synonyms}} | {{pending: translation}} | {{pending: usage example}} |
| {{pending: term}} | {{pending: definition}} | {{pending: domain}} | {{pending: synonyms}} | {{pending: translation}} | {{pending: usage example}} |

## Terms with different meanings per domain

| Term | Domain A meaning | Domain B meaning | How to disambiguate |
|---|---|---|---|
| {{pending: term}} | {{pending: meaning}} | {{pending: meaning}} | {{pending: qualifier or rename}} |

## States and lifecycles

Entities with states should list them here using the same names as in the code:

| Entity | States | Allowed transitions |
|---|---|---|
| {{pending: entity}} | {{pending: e.g. draft, active, closed}} | {{pending: e.g. draft to active}} |

## Maintenance

- Owner of the glossary: {{pending: role}}
- `/dixi.domain` can propose terms while drafting a domain; a person confirms them here.

## Related

- [Domain map](domain-map.md)
- [Business capabilities](business-capabilities.md)
- [Domain example](../../03-domains/example/domain-spec.md)
- [Domain template](../../10-engineering/templates/domain-template.md)
