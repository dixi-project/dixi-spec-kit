# Checklist 04 — Security

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess how the project identifies threats, controls access, protects secrets and data, finds and fixes vulnerabilities, and responds to incidents.

Status: draft. {{pending: confirm whether penetration test results may be shared in this review}}

## Inputs

- [Threat model](../../13-security/threat-model.md) and [Risk register](../../13-security/risk-register.md)
- [AuthN/AuthZ model](../../13-security/authn-authz-model.md) and [Break-glass access](../../13-security/break-glass-access.md)
- [Secret management](../../13-security/secret-management.md)
- [Data protection controls](../../13-security/data-protection-controls.md)
- [Vulnerability management](../../13-security/vulnerability-management.md) and [Security test plan](../../11-quality/security-test-plan.md)
- [Incident response](../../13-security/incident-response.md)
- [LLM application security](../../13-security/llm-application-security.md), when AI features exist

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| SEC-01 | Is there a current threat model for the main flows? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-02 | Is authentication strong, with multi-factor for staff and admins? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-03 | Is authorisation enforced server-side and tested, including tenant isolation if any? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-04 | Are data encrypted in transit and at rest, with managed keys? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-05 | Are secrets kept out of code and rotated? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-06 | Are vulnerabilities found by scans and tests, and fixed within defined targets? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-07 | Is input validated and output encoded at trust boundaries? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-08 | Are security events logged, retained and alerted on? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-09 | Is there a tested incident response process with records of past incidents? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SEC-10 | Are privileged and emergency accesses controlled and reviewed? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- Known critical vulnerabilities open with no plan.
- Shared admin accounts or no multi-factor for production access.
- A past breach that was not investigated or disclosed as required.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 03 — Source code](03-source-code.md)
- [Checklist 05 — Data management](05-data-management.md)
- [Final checklist](11-final-report.md)
