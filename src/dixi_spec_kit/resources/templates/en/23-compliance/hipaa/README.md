# HIPAA

> **Working aid, not legal advice.** This page helps decide whether the US Health Insurance Portability and Accountability Act may apply and what to prepare if it does. It does not interpret the law and no template certifies compliance; applicability must be confirmed by qualified counsel.

## Purpose

Record whether the project handles protected health information (PHI) and in which role, and, if it does, track the safeguards, agreements and evidence the team must put in place. Until applicability is decided, this folder holds only this page.

Status: draft. {{pending: decide whether HIPAA applies and record the reason in the compliance overview}}

## Applicability questions

| Question | Answer | Source |
|----------|--------|--------|
| Does the product create, receive, store or transmit health information about identifiable individuals? | {{pending: answer}} | [PII classification](../../08-data/pii-classification.md) |
| Is the project a covered entity, or does it act on behalf of one (business associate)? | {{pending: answer, confirmed by counsel}} | {{pending: link}} |
| Do customers ask for a business associate agreement? | {{pending: answer}} | {{pending: link}} |
| Do sub-processors receive that information? | {{pending: answer}} | [Sub-processors](../gdpr/sub-processors.md) |

If every answer is "no", record the decision and stop here.

## If it applies: areas to prepare

Described in general terms; read the official rules for exact requirements.

| Area | What the project prepares | Evidence | Gap / ticket |
|------|---------------------------|----------|--------------|
| Risk analysis | A documented assessment of risks to health information | [Risk register](../../13-security/risk-register.md) | {{pending: gap}} |
| Administrative safeguards | Security responsibility, workforce training, access management, contingency plan | {{pending: link}} | {{pending: gap}} |
| Physical safeguards | Facility and device controls, usually partly inherited from hosting | {{pending: link}} | {{pending: gap}} |
| Technical safeguards | Access control, audit logging, integrity, transmission security | [Data protection controls](../../13-security/data-protection-controls.md) | {{pending: gap}} |
| Agreements | Business associate agreements with customers and downstream processors | {{pending: link}} | {{pending: gap}} |
| Breach notification | Assessment and notification process and deadlines confirmed by counsel | [Data breach playbook](../../15-operations/playbooks/data-breach.md) | {{pending: gap}} |
| Minimum necessary | Access and disclosure limited to what each purpose needs | {{pending: link}} | {{pending: gap}} |

## Product guardrails to consider

- Keep health information out of logs, analytics and error reports.
- Restrict which environments may contain real health information.
- Confirm that AI features never send health information to providers without an agreement. {{pending: decide per feature}}

## Related

- [Compliance overview](../compliance-overview.md)
- [Regulatory watch](../regulatory-watch.md)
- [Data protection controls](../../13-security/data-protection-controls.md)
- [Risk register](../../13-security/risk-register.md)
