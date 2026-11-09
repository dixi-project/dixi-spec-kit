# PII Classification

## Purpose

Define how the project classifies personal and sensitive data, so that every field, table, file and event has a known sensitivity level and a matching set of handling rules. Specs, contracts and tests refer to these levels instead of restating rules.

- Owner: {{pending: person or role accountable for data classification}}
- Applicable law and obligations: {{pending: privacy laws and contractual obligations that apply in each target market}}

## Classification levels

| Level | Meaning | Examples | Handling summary |
| --- | --- | --- | --- |
| Public | Safe to publish | Product name, published prices | No restrictions |
| Internal | Not secret, not for publication | Internal identifiers, feature flags | Authenticated access only |
| Personal (PII) | Identifies or relates to a person | Name, e-mail, phone, IP address | Least privilege, masked in logs |
| Sensitive | Harm if exposed | Government IDs, health, financial, precise location | Encrypted at field level, access audited |
| Secret | Credentials and keys | Passwords, tokens, signing keys | Never stored in plain text, never logged |

Adjust the levels to the project: {{pending: confirm or rename the classification levels}}

## Data inventory

Register every element that holds data at level Personal or above.

| Element | Location (table, file, event) | Level | Purpose of processing | Legal basis | Retention rule |
| --- | --- | --- | --- | --- | --- |
| `user.email` | {{pending: location}} | Personal | Account login and notices | {{pending: basis}} | See [retention policy](retention-policy.md) |
| | | | | | |

## Handling rules per level

- [ ] Personal and above are never written to application logs in clear text; mask or hash them.
- [ ] Sensitive data is encrypted at rest at field or column level, not only at disk level.
- [ ] Access to Sensitive data is restricted by role and every read is auditable.
- [ ] Test fixtures and seeds use synthetic data; production data is never copied to lower environments without anonymisation.
- [ ] Exports, reports and analytics datasets state the highest level they contain.
- [ ] Data shared with third parties is listed with the level and the agreement that covers it.
- [ ] Secrets live in a secret store, not in the repository or in configuration files.

## Data subject requests

| Request | Supported | Process and response time |
| --- | --- | --- |
| Access / export | {{pending: yes or no}} | |
| Rectification | | |
| Erasure | | |
| Objection / restriction | | |

## How to use this document

1. When a feature spec introduces a new field, classify it here before implementation.
2. Contracts mark fields at level Personal or above (see the [contract example](../07-contracts/example.md)).
3. `dixi check` and `/dixi.data` (Claude Code) or `$dixi-data` (Codex) help review that new data has a classification.
4. The [test plan](../11-quality/test-plan.md) includes cases for masking and access control.

## Related

- [Retention policy](retention-policy.md)
- [Master spec](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)
- [Contract example](../07-contracts/example.md)
