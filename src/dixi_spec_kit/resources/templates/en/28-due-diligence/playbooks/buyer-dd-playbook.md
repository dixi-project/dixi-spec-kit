# Buyer due diligence playbook

> **Evidence rule.** Answer the buyer only with what artifacts prove. Gaps are disclosed as gaps, never covered with assumptions presented as facts; every answer points to an artifact of the project.

## Purpose

Prepare the project for a technical review by a prospective acquirer or investor: what they usually look at, how to organise the data room, how to answer questions, and how to handle findings honestly.

Status: draft. {{pending: name the internal lead and the person authorised to share material}}

## Before the review

1. Confirm the confidentiality agreement and the data room rules: {{pending: agreement reference}}
2. Run an [internal audit DD](internal-audit-dd-playbook.md) first, so known gaps are not a surprise.
3. Prepare an evidence index by checklist area; link artifacts, do not paste them.
4. Remove secrets, credentials and personal data from everything to be shared.

## What buyers usually focus on

| Focus | Checklist | Typical evidence |
|-------|-----------|------------------|
| Does the technology work and scale? | [02](../checklist/02-architecture.md), [01](../checklist/01-infrastructure.md) | Diagrams, SLO history, load tests |
| Who owns the code and IP? | [03](../checklist/03-source-code.md) | Repository ownership, licence inventory, IP assignments |
| Security and incident history | [04](../checklist/04-security.md) | Threat model, vulnerability metrics, incident records |
| Data and privacy exposure | [05](../checklist/05-data-management.md) | Data inventory, retention, subject request records |
| Key-person risk | [07](../checklist/07-team.md) | Key-person map, documentation coverage |
| Run cost and scaling cost | [08](../checklist/08-financial.md) | Billing exports, unit cost |
| Dependence on vendors | [09](../checklist/09-vendors-partners.md) | Vendor list, agreements, exit plans |

## During the review

- Keep a question log: question, answer, artifact, who answered, date.
- Answer "we do not know yet" rather than guessing; add the item to the gap list.
- Give access to systems only as agreed, read-only and time-limited.

## Question log

| ID | Question | Answer | Artifact | Answered by | Date |
|----|----------|--------|----------|-------------|------|
| Q-01 | {{pending: question}} | {{pending: answer}} | {{pending: link}} | {{pending: role}} | {{pending: date}} |

## After the review

- Record findings in the [DD report template](../dd-report-template.md) and agree the remediation plan.
- Revoke any access granted for the review.

## Related

- [DD strategy](../dd-strategy.md)
- [Internal audit DD playbook](internal-audit-dd-playbook.md)
- [Final checklist](../checklist/11-final-report.md)
