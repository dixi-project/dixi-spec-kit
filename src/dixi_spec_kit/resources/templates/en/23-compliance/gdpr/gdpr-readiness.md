# GDPR readiness

> **Working aid, not legal advice.** This checklist organises the work and evidence usually expected under the EU General Data Protection Regulation. It does not interpret the regulation and no template certifies compliance; confirm conclusions with qualified counsel.

## Purpose

Show, area by area, what the project has in place for personal data protection, what is missing and where the evidence is. Gaps become risks or tasks, not assumptions.

Status: draft. {{pending: decide whether the regulation applies and record the reason in the compliance overview}}

## Roles

- Is the project a controller, a processor or both, and for which processing? {{pending: decide per processing activity}}
- Is a data protection officer or a local representative required? {{pending: decide with counsel}}

## Readiness checklist

Readiness uses the levels in the [Compliance overview](../compliance-overview.md).

| Area | What is expected (in general terms) | Level | Evidence | Gap / ticket |
|------|-------------------------------------|-------|----------|--------------|
| Records of processing | Inventory of processing activities, purposes, data and recipients | {{pending: 0-5}} | [PII classification](../../08-data/pii-classification.md) | {{pending: gap}} |
| Lawful basis | A documented basis for each purpose | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Transparency | Privacy notice that matches real processing | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Consent | Where used: freely given, recorded, withdrawable | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Data subject rights | Process for access, rectification, erasure, portability, objection | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Minimisation and retention | Only needed data, kept only as long as needed | {{pending: 0-5}} | [Retention policy](../../08-data/retention-policy.md) | {{pending: gap}} |
| Privacy by design | Privacy reviewed in specs before building | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Impact assessments | Done for high-risk processing | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Security of processing | Measures appropriate to the risk | {{pending: 0-5}} | [Data protection controls](../../13-security/data-protection-controls.md) | {{pending: gap}} |
| Processors | Contracts and a current list | {{pending: 0-5}} | [Sub-processors](sub-processors.md) | {{pending: gap}} |
| International transfers | Mechanism identified for each transfer | {{pending: 0-5}} | {{pending: link}} | {{pending: gap}} |
| Breach handling | Detection, assessment, notification within the legal deadline | {{pending: 0-5}} | [Data breach playbook](../../15-operations/playbooks/data-breach.md) | {{pending: gap}} |

## Product questions to answer in specs

- Which features collect personal data, and is each field needed?
- Can a user export and delete their data without manual work?
- Are logs, analytics and backups covered by retention and erasure?
- Do AI features send personal data to third parties? {{pending: answer per feature}}

## Related

- [Compliance overview](../compliance-overview.md)
- [Sub-processors](sub-processors.md)
- [DPA template](../dpa-template.md)
- [Risk register](../../13-security/risk-register.md)
