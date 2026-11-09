# Data breach

## Purpose

Respond to a confirmed or suspected exposure of personal or confidential data: contain it, preserve evidence, assess who is affected and meet any notification duties on time.

Status: draft. {{pending: name the owner of this playbook}}

This playbook is operational guidance, not legal advice. Notification duties depend on the applicable laws and contracts.

## When it applies

- Data accessed, copied, changed or deleted by someone without authorisation.
- Data published or sent to the wrong recipient.
- A credential with access to personal data leaked.

Every suspected breach starts at SEV1 until ruled out (see [incident levels](../incident-levels.md)).

## Roles

- **Incident lead**: coordinates and keeps the timeline.
- **Security contact**: leads containment and evidence.
- **Privacy or legal contact**: decides on notifications. {{pending: name this role}}
- **Communications lead**: prepares messages; publishes nothing without approval.

An AI agent may help search logs and summarise findings; it never deletes evidence, rotates credentials or contacts anyone.

## Steps

1. **Declare** and open a restricted incident channel; limit who joins.
2. **Contain**: revoke leaked credentials, close the exposed path, block the actor. Prefer actions that do not destroy evidence.
3. **Preserve evidence**: export relevant logs, snapshots and access records to a protected location; record who handled them.
4. **Assess scope**: what data, which categories (see [PII classification](../../08-data/pii-classification.md)), how many people, which period, whether data was encrypted.
5. **Decide on notification** with the privacy or legal contact: authorities, affected people, customers under contract. Deadline: {{pending: list legal and contractual deadlines}}.
6. **Notify** using the [customer breach communication](comms-breach-customer.md) playbook.
7. **Recover**: fix the root cause, verify no further access, restore normal operation.

## Timeline log

Record every action with time, person and evidence. The clock for notification deadlines usually starts when the breach becomes known, not when it is fully understood.

## Close criteria

- Exposure stopped and verified.
- Notification decision documented, and notifications sent where required.
- Postmortem completed and risks added to the [risk register](../../13-security/risk-register.md).

## Related

- [Incident response](../../13-security/incident-response.md)
- [Customer breach communication](comms-breach-customer.md)
- [Escalation matrix](../escalation-matrix.md)
- [Data protection controls](../../13-security/data-protection-controls.md)
