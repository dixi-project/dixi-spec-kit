# Security baseline

## Purpose

Define the minimum security controls every part of this project must meet, regardless of profile, so that gaps are visible and each control has an owner. Detailed practices live in `13-security/`.

Status: draft. {{pending: confirm the baseline with the security owner}}

## How to read the table

- **Control**: what must be true.
- **Evidence**: how a reviewer can check it without trusting a claim.
- **Status**: `pending`, `partial` or `in place`. Nothing starts as `in place`.

## Identity and access

| Control | Evidence | Status |
|---------|----------|--------|
| Every person and service has its own identity; no shared accounts. | Access list | pending |
| Least privilege; access is reviewed periodically. | Review record | pending |
| Strong authentication for administrative access. | Configuration | pending |

## Secrets

| Control | Evidence | Status |
|---------|----------|--------|
| No secrets in the repository, its history, logs or agent context. | Secret scan result | pending |
| Secrets live in a managed store per environment. | [Secret management](../13-security/secret-management.md) | pending |
| Secrets have owners and a rotation rule. | Inventory | pending |

## Code and dependencies

| Control | Evidence | Status |
|---------|----------|--------|
| Changes are reviewed by a person before merge. | Pull request history | pending |
| Dependencies are pinned and scanned. | [Dependency scanning](../13-security/dependency-scanning.md) | pending |
| Inputs are validated at trust boundaries. | [Secure coding standard](../10-engineering/secure-coding-standard.md) | pending |

## Data

| Control | Evidence | Status |
|---------|----------|--------|
| Personal data is classified and minimized. | [PII classification](../08-data/pii-classification.md) | pending |
| Data is encrypted in transit and at rest. | Configuration | pending |
| Retention and deletion rules exist. | [Retention policy](../08-data/retention-policy.md) | pending |

## AI agents

| Control | Evidence | Status |
|---------|----------|--------|
| Agents cannot read secrets, sign, approve or merge. | [AI agent hardening](../13-security/ai-agent-hardening.md) | pending |
| Untrusted content is treated as data, not instructions. | Review checklist | pending |

## Detection and response

| Control | Evidence | Status |
|---------|----------|--------|
| Security-relevant events are logged without sensitive data. | Log samples | pending |
| An incident process with named roles exists. | [Incident response](../13-security/incident-response.md) | pending |

## Reference framework

{{pending: choose a reference framework or verification standard, if any, and the level targeted}}

## Related

- [Threat model](../13-security/threat-model.md)
- [Engineering standards](engineering-standards.md)
- [AI governance](ai-governance.md)
- [Principles](principles.md)
