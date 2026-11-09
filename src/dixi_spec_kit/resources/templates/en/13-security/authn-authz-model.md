# Authentication and authorization model

## Purpose

Describe how users and services prove who they are (authentication) and what each one is allowed to do (authorization), so every feature applies the same rules and every access decision can be tested.

Status: draft. {{pending: name the owner of the access model}}

## Identities

| Identity type | Example | How it authenticates |
|---------------|---------|----------------------|
| End user | Customer account | {{pending: e.g. password plus second factor, single sign-on, magic link}} |
| Administrator | Back-office operator | {{pending: method; second factor required?}} |
| Service | Background job, other system | {{pending: e.g. short-lived token, mutual TLS}} |
| AI agent or automation | Scheduled task | {{pending: method and scope}} |

## Authentication rules

- Identity provider or mechanism: {{pending: choose}}
- Password and second-factor policy: {{pending: define}}
- Session lifetime, idle timeout and revocation: {{pending: define}}
- Account recovery that cannot be abused for takeover: {{pending: define}}
- Rate limiting and lockout on login and recovery endpoints.

## Authorization model

Approach: {{pending: role-based, attribute-based, relationship-based or a mix}}

| Role | Can | Cannot |
|------|-----|--------|
| {{pending: role}} | {{pending: actions}} | {{pending: actions}} |

## Rules every feature follows

- Deny by default; grant explicitly.
- Check authorization on the server for every request, never only in the user interface.
- Check ownership of the specific resource, not only the role (prevents access to another user's records by changing an ID).
- Tenant isolation, if multi-tenant: {{pending: define how tenant boundaries are enforced}}
- Privileged actions are logged with who, what and when.

## Verification

Each rule above maps to tests in the test plan: a permitted case, a denied case and an ownership case per protected resource. {{pending: list the test IDs}}

## Related

- [Threat model](threat-model.md)
- [Secret management](secret-management.md)
- [Data protection controls](data-protection-controls.md)
- [Test plan](../11-quality/test-plan.md)
