# SOC 2 controls matrix

> **Working aid, not legal advice.** This matrix maps the project's own controls to broad SOC 2 themes. It does not reproduce the criteria text, it is not an audit, and no template certifies compliance.

## Purpose

List each control the project operates, the SOC 2 theme it supports, who owns it, how it is tested and where its evidence lives. The auditor's own mapping prevails; this is the team's working view.

Status: draft. {{pending: confirm the criteria in scope from the readiness plan}}

## How to use

- One row per control the project actually runs or plans to run; do not copy a generic list.
- Reference the criterion identifier only; read the official criteria from the issuing body.
- Status values: planned, designed, operating, gap.

## Matrix

| Control ID | Theme | Control (project's words) | Owner | Frequency | Test method | Evidence location | Status |
|------------|-------|---------------------------|-------|-----------|-------------|-------------------|--------|
| CTL-01 | Control environment | Security responsibilities assigned and acknowledged | {{pending: owner}} | Yearly | Inspect signed acknowledgements | {{pending: link}} | {{pending: status}} |
| CTL-02 | Risk assessment | Risks reviewed and scored on a schedule | {{pending: owner}} | {{pending: frequency}} | Inspect [Risk register](../../13-security/risk-register.md) history | {{pending: link}} | {{pending: status}} |
| CTL-03 | Logical access | Access granted by role and reviewed periodically | {{pending: owner}} | {{pending: frequency}} | Sample access reviews | [AuthN/AuthZ model](../../13-security/authn-authz-model.md) | {{pending: status}} |
| CTL-04 | Logical access | Access removed promptly at offboarding | {{pending: owner}} | Per event | Sample leavers against access logs | {{pending: link}} | {{pending: status}} |
| CTL-05 | Change management | Changes reviewed and tested before release | {{pending: owner}} | Per change | Sample merged changes and pipeline runs | [CI/CD overview](../../14-delivery/ci-cd-overview.md) | {{pending: status}} |
| CTL-06 | System operations | Vulnerabilities detected and fixed within targets | {{pending: owner}} | {{pending: frequency}} | Inspect scan results and tickets | [Vulnerability management](../../13-security/vulnerability-management.md) | {{pending: status}} |
| CTL-07 | System operations | Incidents handled and reviewed | {{pending: owner}} | Per incident | Inspect incident records | [Incident response](../../13-security/incident-response.md) | {{pending: status}} |
| CTL-08 | Monitoring | Alerts for security-relevant events | {{pending: owner}} | Continuous | Inspect alert configuration and samples | [Alerting rules](../../12-observability/alerting-rules.md) | {{pending: status}} |
| CTL-09 | Vendor management | Critical vendors assessed before use and reviewed | {{pending: owner}} | {{pending: frequency}} | Inspect assessments | [Vendor risk assessment](../../15-operations/vendor-management/vendor-risk-assessment.md) | {{pending: status}} |
| CTL-10 | Availability | Backups taken and restores tested | {{pending: owner}} | {{pending: frequency}} | Inspect restore test records | [Backup and recovery](../../14-delivery/backup-and-recovery.md) | {{pending: status}} |
| CTL-11 | Confidentiality | Data encrypted in transit and at rest | {{pending: owner}} | Continuous | Inspect configuration | [Data protection controls](../../13-security/data-protection-controls.md) | {{pending: status}} |
| {{pending: ID}} | {{pending: theme}} | {{pending: control}} | {{pending: owner}} | {{pending: frequency}} | {{pending: method}} | {{pending: link}} | {{pending: status}} |

## Gaps

Each row in status "gap" gets a ticket and, when material, a risk entry. {{pending: link the gap tickets}}

## Related

- [SOC 2 readiness](soc2-readiness.md)
- [System description](system-description.md)
- [ISO 27001 and SOC 2 overlap](../iso-soc2-overlap-mapping.md)
- [Risk register](../../13-security/risk-register.md)
