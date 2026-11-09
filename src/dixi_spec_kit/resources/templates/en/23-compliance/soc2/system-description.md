# System description (SOC 2)

> **Working aid, not legal advice.** This outline gathers the facts usually needed for the system description that accompanies a SOC 2 report. Management owns the final description and the auditor evaluates it; no template certifies compliance.

## Purpose

Describe the system in scope accurately and completely: what service it provides, which components and people support it, how data flows, and which commitments and controls apply. Every statement must match how the system actually works.

Status: draft. {{pending: name the author and the approver of the system description}}

## 1. Services provided

- Service and main users: {{pending: describe}}
- Principal service commitments to customers (e.g. availability, confidentiality): {{pending: list, linked to contracts or SLAs}}
- System requirements derived from those commitments: {{pending: list}}

## 2. Components of the system

| Component | Description | Source artifact |
|-----------|-------------|-----------------|
| Infrastructure | Environments, networks, hosting regions | [Deployment architecture](../../09-architecture/deployment-architecture.md) |
| Software | Applications, services, databases | [System context](../../09-architecture/system-context.md) |
| People | Roles that operate, develop and support the system | [RACI matrix](../../15-operations/team/raci-matrix.md) |
| Procedures | Change, access, incident, backup procedures | {{pending: links}} |
| Data | Data types, classification, retention | [PII classification](../../08-data/pii-classification.md) |

## 3. Boundaries

- In scope: {{pending: systems, locations, teams}}
- Out of scope, with reason: {{pending: list}}
- Subservice organisations and how they are treated (carved out or included): {{pending: list categories}}

## 4. Data flows

Describe how customer data enters, is processed, stored and leaves the system. {{pending: link a diagram in 09-architecture}}

## 5. Controls summary

Reference the [Controls matrix](soc2-controls-matrix.md); do not duplicate it here.

## 6. Complementary controls

- Controls expected from customers (complementary user entity controls): {{pending: list, e.g. managing their own user accounts}}
- Controls expected from subservice organisations: {{pending: list}}

## 7. Significant changes during the period

| Date | Change | Impact on controls |
|------|--------|--------------------|
| {{pending: date}} | {{pending: change}} | {{pending: impact}} |

## Related

- [SOC 2 readiness](soc2-readiness.md)
- [SOC 2 controls matrix](soc2-controls-matrix.md)
- [System context](../../09-architecture/system-context.md)
- [Compliance overview](../compliance-overview.md)
