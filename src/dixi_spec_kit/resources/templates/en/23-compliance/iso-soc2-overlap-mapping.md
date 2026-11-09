# ISO/IEC 27001 and SOC 2 overlap

> **Working aid, not legal advice.** This table helps reuse one control and one piece of evidence for both frameworks. Overlaps are approximate, the assessor's mapping prevails, and no template certifies compliance.

## Purpose

Avoid running two parallel programmes. Each project control is implemented once, mapped to the ISO/IEC 27001 reference controls and to the SOC 2 themes it supports, and evidenced once.

Status: draft. {{pending: decide which framework is the primary programme and which reuses its evidence}}

## Key differences in general terms

| Aspect | ISO/IEC 27001 | SOC 2 |
|--------|---------------|-------|
| Outcome | Certificate of a management system | Auditor's report on controls |
| Focus | The ISMS: risk process, policy, review, improvement | Controls relevant to the criteria in scope |
| Scope choice | Organisation-defined ISMS scope | System and criteria chosen for the report |
| Recurring cycle | Surveillance audits and recertification | New report per period |

## Shared control map

| Project control | ISO/IEC 27001 ref. ID | SOC 2 theme | Shared evidence | Owner | Gaps specific to one framework |
|-----------------|-----------------------|-------------|-----------------|-------|--------------------------------|
| Risk assessment and treatment | {{pending: ID}} | Risk assessment | [Risk register](../13-security/risk-register.md) | {{pending: owner}} | {{pending: gap}} |
| Access control and reviews | {{pending: ID}} | Logical access | [AuthN/AuthZ model](../13-security/authn-authz-model.md) | {{pending: owner}} | {{pending: gap}} |
| Change management | {{pending: ID}} | Change management | [CI/CD overview](../14-delivery/ci-cd-overview.md) | {{pending: owner}} | {{pending: gap}} |
| Vulnerability management | {{pending: ID}} | System operations | [Vulnerability management](../13-security/vulnerability-management.md) | {{pending: owner}} | {{pending: gap}} |
| Incident management | {{pending: ID}} | System operations | [Incident response](../13-security/incident-response.md) | {{pending: owner}} | {{pending: gap}} |
| Supplier management | {{pending: ID}} | Vendor management | [Vendor risk assessment](../15-operations/vendor-management/vendor-risk-assessment.md) | {{pending: owner}} | {{pending: gap}} |
| Backup and continuity | {{pending: ID}} | Availability | [DR strategy](../14-delivery/disaster-recovery/dr-strategy.md) | {{pending: owner}} | {{pending: gap}} |
| Data protection | {{pending: ID}} | Confidentiality, privacy | [Data protection controls](../13-security/data-protection-controls.md) | {{pending: owner}} | {{pending: gap}} |
| Management review and internal audit | {{pending: ID}} | Monitoring activities | {{pending: link}} | {{pending: owner}} | Mostly ISO-specific |

## Working rules

- Keep one evidence repository with tags for both frameworks.
- When an auditor requests a different format, derive it from the same source; do not create a second truth.
- Record framework-specific gaps in the readiness file of that framework.

## Related

- [SOC 2 controls matrix](soc2/soc2-controls-matrix.md)
- [ISO 27001 controls mapping](iso-27001/controls-mapping.md)
- [SOC 2 readiness](soc2/soc2-readiness.md)
- [ISO 27001 readiness](iso-27001/iso-27001-readiness.md)
- [Compliance overview](compliance-overview.md)
