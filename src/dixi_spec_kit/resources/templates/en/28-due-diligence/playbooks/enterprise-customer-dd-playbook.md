# Enterprise customer due diligence playbook

> **Evidence rule.** Answer questionnaires only with what artifacts prove. Never tick "yes" for a control that is planned but not operating; gaps are stated as gaps, and every answer points to an artifact of the project.

## Purpose

Respond consistently and truthfully when a business customer's security, privacy or procurement team assesses the product, usually through a questionnaire, a document request or a call.

Status: draft. {{pending: name who owns customer security reviews and who approves answers}}

## Intake

| Field | Value |
|-------|-------|
| Customer (internal reference only) | {{pending: reference}} |
| Format | {{pending: questionnaire / document request / call}} |
| Deadline | {{pending: date}} |
| Confidentiality terms | {{pending: agreement reference}} |
| Sales owner and technical owner | {{pending: roles}} |

## Answer library

Keep reusable, approved answers so each review starts from the last one. Each answer has a source artifact and a review date.

| Topic | Approved answer | Source artifact | Last reviewed |
|-------|-----------------|-----------------|---------------|
| Encryption | {{pending: answer}} | [Data protection controls](../../13-security/data-protection-controls.md) | {{pending: date}} |
| Access control | {{pending: answer}} | [AuthN/AuthZ model](../../13-security/authn-authz-model.md) | {{pending: date}} |
| Incident response | {{pending: answer}} | [Incident response](../../13-security/incident-response.md) | {{pending: date}} |
| Sub-processors | {{pending: answer}} | [Sub-processors](../../23-compliance/gdpr/sub-processors.md) | {{pending: date}} |
| Business continuity | {{pending: answer}} | [DR strategy](../../14-delivery/disaster-recovery/dr-strategy.md) | {{pending: date}} |
| Vulnerability management | {{pending: answer}} | [Vulnerability management](../../13-security/vulnerability-management.md) | {{pending: date}} |
| Certifications and reports | Only what exists, with date and scope | [Compliance overview](../../23-compliance/compliance-overview.md) | {{pending: date}} |

## Steps

1. Log the request and confirm the deadline.
2. Fill from the answer library; mark new questions.
3. Route new questions to the owner of the related area; answer from artifacts.
4. Review answers for accuracy; flag any "partial" or "planned" honestly with a date.
5. Send through the agreed channel; keep a copy of what was sent.
6. Add new approved answers to the library and gaps to the backlog.

## Typical documents requested

- Security overview, data flow diagram, list of sub-processors, DPA, incident response summary, penetration test summary (if one exists and sharing is allowed). {{pending: decide which of these the project can provide}}

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 04 — Security](../checklist/04-security.md)
- [DPA template](../../23-compliance/dpa-template.md)
- [Compliance overview](../../23-compliance/compliance-overview.md)
