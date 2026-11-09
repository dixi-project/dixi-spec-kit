# Data protection controls

## Purpose

List the personal and sensitive data the project handles and the technical and organizational controls that protect it through its lifecycle: collection, use, storage, sharing and deletion.

Status: draft. {{pending: name the owner of data protection}}

## Applicable obligations

Which laws, contracts or internal policies apply depends on the users and markets served. {{pending: list applicable obligations; this template does not declare compliance with any}}

## Data inventory

| Data category | Examples | Classification | Purpose | Legal basis or justification | Retention |
|---------------|----------|----------------|---------|------------------------------|-----------|
| {{pending: e.g. contact data}} | {{pending: name, email}} | {{pending: public / internal / confidential / restricted}} | {{pending: purpose}} | {{pending: basis}} | {{pending: period}} |

## Controls

| Control | Description | Status |
|---------|-------------|--------|
| Minimization | Collect only what the purpose needs | {{pending: planned / in place}} |
| Encryption in transit | All external and internal traffic encrypted | {{pending: status}} |
| Encryption at rest | Stores and backups encrypted | {{pending: status}} |
| Access control | Least privilege, reviewed periodically | {{pending: status}} |
| Logging hygiene | No personal data or secrets in logs | {{pending: status}} |
| Pseudonymization | Non-production environments use synthetic or masked data | {{pending: status}} |
| Deletion | Data removed at end of retention or on valid request | {{pending: status}} |
| Backups | Tested restore, same protections as primary data | {{pending: status}} |

"In place" means implemented and verified by a test or review recorded elsewhere, not only written here.

## Data subject requests

How access, correction, export and deletion requests are received, verified and completed. {{pending: define process and response time}}

## Third parties and transfers

| Recipient | Data shared | Purpose | Safeguards |
|-----------|-------------|---------|------------|
| {{pending: processor category}} | {{pending: data}} | {{pending: purpose}} | {{pending: agreement, location}} |

## Breach handling

Personal data breaches follow the incident response process, including any notification deadlines.

## Related

- [Threat model](threat-model.md)
- [Incident response](incident-response.md)
- [Risk register](risk-register.md)
- [Secret management](secret-management.md)
