# Security test plan

## Purpose

Plan how the project checks its security requirements, so that security is tested alongside features instead of being assumed. This plan lists intended checks; it is not evidence that any check has been run.

Status: draft. {{pending: confirm security test scope with the person responsible for security}}

## Scope

| Asset or area | Threats considered | Owner |
|---------------|--------------------|-------|
| {{pending: asset, for example user accounts}} | {{pending: threats}} | {{pending: owner}} |
| {{pending: asset, for example personal data}} | {{pending: threats}} | {{pending: owner}} |

## Planned checks

| Check | What it looks for | When | Blocks merge |
|-------|-------------------|------|--------------|
| Dependency scan | Known vulnerable dependencies | {{pending: when}} | {{pending: yes/no and severity}} |
| Secret scan | Credentials committed to the repository | {{pending: when}} | {{pending: yes/no}} |
| Static analysis | Insecure code patterns | {{pending: when}} | {{pending: yes/no}} |
| Authentication and authorisation tests | Access without permission, privilege escalation | Every change to access rules | {{pending: yes/no}} |
| Input validation tests | Injection, malformed input, oversized payloads | Every change to inputs | {{pending: yes/no}} |
| Dynamic testing | Vulnerabilities in the running application | {{pending: when}} | {{pending: yes/no}} |

Tool choice is a project decision. {{pending: choose tools for each check}}

## Writing security tests

- Write negative tests first: the request without permission must fail.
- Test both the allowed and the denied path for every access rule.
- Never use real credentials or real personal data in tests; use generated data and `@example.com` addresses.

## Findings

- Record findings with severity, owner and due date. {{pending: severity scale and response times}}
- A finding is closed only when a test proves the fix.
- Accepted risks are recorded with the person who accepted them.

## Related

- [Quality strategy](quality-strategy.md)
- [Non-functional requirements](non-functional-requirements.md)
- [Risk-based review](risk-based-review.md)
- [Test plan](test-plan.md)
- [Project instructions](../AGENTS.md)
