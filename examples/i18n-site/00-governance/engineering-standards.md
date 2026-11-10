# Engineering standards

## Purpose

Give a single entry point to the engineering standards of this project: which rules apply, where each one is written down and how it is enforced. This document is an index and a minimum bar, not a replacement for the detailed standards.

Status: draft. {{pending: confirm the standards that apply to this project}}

## Minimum bar for every change

- [ ] A spec or task explains why the change exists.
- [ ] Tests were written first and committed before the implementation.
- [ ] `make verify` was run and its real result is reported.
- [ ] No secrets, credentials or personal data were added to the repository.
- [ ] User-facing text lives in translation catalogs, not in code.
- [ ] Public interfaces changed only through their contract.
- [ ] A person reviewed and merged the change.

## Standards index

| Topic | Where it lives | Enforced by |
|-------|----------------|-------------|
| Coding style | [Coding standards](../10-engineering/coding-standards.md) | {{pending: formatter or linter}} |
| Secure coding | [Secure coding standard](../10-engineering/secure-coding-standard.md) | Review, {{pending: static analysis}} |
| Testing | [Testing policy](policies/testing-policy.md) | `make verify`, review |
| Branches and commits | [Branching strategy](policies/branching-strategy.md) | Repository settings |
| Naming | [Naming conventions](policies/naming-conventions.md) | Review |
| Documentation | [Documentation policy](policies/documentation-policy.md) | `dixi check` |
| Dependencies | [Dependency policy](policies/dependency-policy.md) | {{pending: dependency scanner}} |
| Versioning | [Versioning policy](policies/versioning-policy.md) | Release review |
| Internationalization | [i18n policy](policies/i18n-policy.md) | Review, tests |
| Use of AI | [AI usage policy](policies/ai-usage-policy.md) | Review |

## Enforcement levels

| Level | Meaning |
|-------|---------|
| Automated | A check fails the build when the rule is broken. |
| Review | A reviewer checks the rule; the checklist records it. |
| Advisory | Recommended; deviations are noted but do not block. |

Mark each rule with its level. A rule that is "automated" only on paper is advisory. {{pending: which rules must become automated first}}

## Exceptions

- An exception names the rule, the reason, the owner and an expiry date.
- Exceptions are recorded in {{pending: where exceptions are recorded}}.
- Expired exceptions are reviewed, not silently extended.

## Related

- [Principles](principles.md)
- [Security baseline](security-baseline.md)
- [TDD guide](../11-quality/tdd-guide.md)
- [Project instructions](../AGENTS.md)
