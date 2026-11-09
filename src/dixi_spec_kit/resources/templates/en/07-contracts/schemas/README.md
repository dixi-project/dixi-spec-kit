# Schemas

## Purpose

Store the shared data schemas that several contracts reuse: entities, value objects, error formats
and common envelopes. Defining a type once and referencing it from APIs, events and files avoids
the slow drift that happens when each contract redefines "customer" or "money" in its own way.

## Layout

```text
07-contracts/schemas/
  <entity>.schema.json     One schema per shared type (for example, JSON Schema)
  common/                  Reusable pieces: money, address, pagination, error
```

- Schema format: {{pending: JSON Schema, protocol buffers or another format, recorded in an ADR}}
- File naming: lowercase words separated by hyphens, one type per file.

## What every schema must define

- A stable `$id` or name and a version.
- Field names from the ubiquitous language, with type, format and whether each is required.
- Constraints: lengths, ranges, patterns, allowed values.
- Fields that contain personal data, flagged so that logging and retention rules apply.
- At least one valid and one invalid example, used by tests.

## Schema index

| Schema | Owning domain | Used by contracts | Version | Contains PII |
|---|---|---|---|---|
| {{pending: schema}} | {{pending: domain}} | {{pending: contract IDs}} | {{pending: version}} | {{pending: yes or no}} |

## Compatibility rules

- Adding an optional field is compatible; removing or renaming a field is breaking.
- Changing a type or tightening a constraint is breaking.
- Consumers must ignore unknown fields so that producers can add data safely.
- Breaking changes get a new version; the old one stays until every consumer has migrated.

## Conventions

- Dates and times: {{pending: e.g. ISO 8601 in UTC}}
- Money: amount in the smallest unit plus currency code, never floating point.
- Identifiers: {{pending: format, e.g. opaque strings}}

## Related

- [API contracts](../api/README.md)
- [External contracts](../external/README.md)
- [Canonical data model](../../08-data/canonical-data-model.md)
- [PII classification](../../08-data/pii-classification.md)
