# Incident levels

## Purpose

Give everyone the same scale to classify an incident, so that the response, the people involved and the communication match the real impact.

Status: draft. {{pending: name the owner of the incident scale}}

## The scale

| Level | Meaning | Example signals | First response | Customer update |
|-------|---------|-----------------|----------------|-----------------|
| SEV1 | Critical service down or data at risk for most users | Main flow unavailable, suspected data loss or leak | {{pending: e.g. 15 minutes, any hour}} | {{pending: e.g. within 30 minutes}} |
| SEV2 | Major degradation or a critical flow broken for part of the users | Error rate far above normal, one region or segment down | {{pending: e.g. 30 minutes}} | {{pending: e.g. within 1 hour}} |
| SEV3 | Minor degradation with a workaround | Slow pages, a secondary feature failing | {{pending: e.g. next business hours}} | {{pending: only if asked}} |
| SEV4 | Cosmetic or internal issue, no user impact | Typo, noisy alert, internal tool glitch | Backlog | None |

The times above are placeholders; set them with the people who will be on call.

## Critical services and flows

A failure in one of these is never below SEV2:

- {{pending: list critical flows, e.g. sign-in, checkout, data export}}

## Classifying

1. Classify with the information you have; do not wait for certainty.
2. When in doubt between two levels, choose the higher one.
3. Any suspected exposure of personal data starts at SEV1 until ruled out.
4. Record the level, the time and who declared it in the incident channel.

## Raising and lowering

- Anyone in the response can raise the level at any time.
- Only the incident lead lowers it, and writes down why.
- A level change triggers the matching row of the [escalation matrix](escalation-matrix.md).

## Mitigate first, keep the chain

Restoring service comes before finding the root cause, but mitigation does not skip approvals: follow the [restore service](playbooks/restore-service.md) playbook and never let an AI agent operate production on its own.

## After the incident

SEV1 and SEV2 always get a blameless postmortem using the [postmortem template](../10-engineering/templates/postmortem-template.md). {{pending: decide whether SEV3 also requires a postmortem}}

## Related

- [Escalation matrix](escalation-matrix.md)
- [Restore service](playbooks/restore-service.md)
- [Customer outage communication](playbooks/comms-outage-customer.md)
- [Incident response](../13-security/incident-response.md)
- [Project](../00-master-spec.md)
