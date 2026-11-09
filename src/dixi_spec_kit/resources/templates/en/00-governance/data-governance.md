# Data governance

## Purpose

Define who owns each kind of data in this project, how it is classified, who may access it, how long it is kept and how its quality is protected, so that data decisions are explicit and auditable.

Status: draft. {{pending: name the data governance owner}}

## Data owners

| Data set | Owner | Steward | Systems that hold it |
|----------|-------|---------|----------------------|
| {{pending: e.g. customer accounts}} | {{pending: owner}} | {{pending: steward}} | {{pending: systems}} |

- The **owner** decides purpose, access and retention.
- The **steward** keeps definitions, quality rules and the catalog entry up to date.

## Classification

| Level | Examples | Minimum handling |
|-------|----------|------------------|
| Public | Published content | No restriction. |
| Internal | Operational metrics | Authenticated access only. |
| Confidential | Personal data, contracts | Least privilege, encryption, access log. |
| Restricted | Credentials, sensitive personal data | Named access, strongest controls, never in logs or agent context. |

Detailed rules for personal data: [PII classification](../08-data/pii-classification.md).

## Catalog and lineage

- Each data set has a catalog entry: definition, owner, classification, source and consumers.
- Changes to a data set's shape go through a contract and a migration plan.
- {{pending: where the data catalog lives}}

## Quality

| Dimension | Example rule | Check |
|-----------|--------------|-------|
| Completeness | Required fields are present | {{pending: check}} |
| Validity | Values match the allowed format | {{pending: check}} |
| Uniqueness | No duplicate business keys | {{pending: check}} |
| Timeliness | Data is refreshed within the agreed window | {{pending: check}} |

## Retention and deletion

- Every data set has a retention period and a deletion method: [Retention policy](../08-data/retention-policy.md).
- Deletion requests from data subjects are handled within {{pending: response time}}.

## Access

- Access is granted per role, reviewed {{pending: review frequency}} and revoked on role change.
- Production data is not copied to development; use synthetic or masked data.

## Data and AI

- No confidential or restricted data is sent to an AI model without an explicit, recorded decision.
- Data used to evaluate or tune models is classified like any other data set.

## Related

- [Security baseline](security-baseline.md)
- [AI governance](ai-governance.md)
- [Principles](principles.md)
- [Data protection controls](../13-security/data-protection-controls.md)
