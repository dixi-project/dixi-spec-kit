# Compliance overview

> **Working aid, not legal advice.** This template helps organise work and evidence. No template certifies compliance with any law or standard; only the competent authority or an accredited assessor can reach that conclusion. Have qualified counsel review every legal decision.

## Purpose

Keep one map of the regulations and frameworks the project may be subject to: why each one might apply, whether it does, who owns it and where its evidence lives. This file is the entry point to the `23-compliance/` area.

Status: draft. {{pending: name the compliance owner and the review cadence}}

## Applicability matrix

Record "no" with its reason as well: a documented non-applicability is evidence too.

| Regulation or framework | Typical trigger | Applies? | Owner | Evidence folder | Next review |
|-------------------------|-----------------|----------|-------|-----------------|-------------|
| Data protection law (e.g. GDPR) | Personal data of people in that jurisdiction | {{pending: yes / no / to assess}} | {{pending: owner}} | `23-compliance/gdpr/` | {{pending: date}} |
| SOC 2 | Business customers ask for an independent assurance report | {{pending: yes / no / to assess}} | {{pending: owner}} | `23-compliance/soc2/` (app and platform profiles) | {{pending: date}} |
| ISO/IEC 27001 | A market or customer requires a certified ISMS | {{pending: yes / no / to assess}} | {{pending: owner}} | `23-compliance/iso-27001/` (app and platform profiles) | {{pending: date}} |
| HIPAA | Health information handled for a covered entity | {{pending: yes / no / to assess}} | {{pending: owner}} | `23-compliance/hipaa/` (app and platform profiles) | {{pending: date}} |
| PCI DSS | Cardholder data stored, processed or transmitted | {{pending: yes / no / to assess}} | {{pending: owner}} | `23-compliance/pci-dss/` (app and platform profiles) | {{pending: date}} |
| Other local or sector rules | {{pending: list them}} | {{pending: yes / no / to assess}} | {{pending: owner}} | {{pending: folder}} | {{pending: date}} |

## Readiness levels

Describe status with these levels, never with "compliant" or "certified":

| Level | Meaning |
|-------|---------|
| 0 | Not assessed |
| 1 | Applicability decided and owner named |
| 2 | Gaps identified and recorded as risks |
| 3 | Controls designed and documented |
| 4 | Controls operating with evidence |
| 5 | Reviewed by an independent party (record who and when) |

## Shared building blocks

- Data inventory and classification: [PII classification](../08-data/pii-classification.md).
- Retention and deletion: [Retention policy](../08-data/retention-policy.md).
- Technical and organisational controls: [Data protection controls](../13-security/data-protection-controls.md).
- Gaps and accepted risks: [Risk register](../13-security/risk-register.md).
- Incidents and breach notification: [Incident response](../13-security/incident-response.md) and [Data breach playbook](../15-operations/playbooks/data-breach.md).
- Processors and contracts: [Sub-processors](gdpr/sub-processors.md) and [DPA template](dpa-template.md).
- Product rules derived from obligations: [Compliance rules](../01-business/rules/compliance-rules.md).

## Working rules

- Every statement in this area points to an artifact: spec, test, log, ticket or signed document.
- Unknowns stay as `{{pending: …}}`; do not fill them with assumptions.
- Use `/dixi.compliance` (Claude Code) or `$dixi-compliance` (Codex) to review gaps. `dixi check` validates structure only, not compliance.

## Related

- [Regulatory watch](regulatory-watch.md)
- [GDPR readiness](gdpr/gdpr-readiness.md)
- [DPA template](dpa-template.md)
- [Risk register](../13-security/risk-register.md)
- [Project](../00-master-spec.md)
