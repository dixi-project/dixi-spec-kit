# Checklist 03 — Source code

> **Evidence rule.** Score only what an artifact proves. A missing artifact is recorded as "no evidence" and scored 0; it is never filled with an assumption presented as fact.

## Purpose

Assess the quality, ownership, testability and legal cleanliness of the source code: who can change it, how changes are checked, and whether third-party code is used under acceptable licences.

Status: draft. {{pending: list the repositories in scope}}

## Inputs

- [Repositories](../../20-repos/README.md)
- [Coding standards](../../10-engineering/coding-standards.md) and [Secure coding standard](../../10-engineering/secure-coding-standard.md)
- [Quality strategy](../../11-quality/quality-strategy.md) and [Test pyramid](../../11-quality/test-pyramid.md)
- [CI/CD overview](../../14-delivery/ci-cd-overview.md)
- [Dependency scanning](../../13-security/dependency-scanning.md)
- [Licensing policy](../../13-security/licensing/licensing-policy.md) and [Approved licences](../../13-security/licensing/approved-licenses.md)
- [Engineering metrics](../../11-quality/engineering-metrics.md)

## Items

| ID | Question | Evidence (artifact) | Score 0–5 | Finding |
|----|----------|---------------------|-----------|---------|
| SRC-01 | Is all code in version control, with the organisation owning the repositories? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-02 | Does every change go through review and automated checks before merging? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-03 | Are there automated tests at several levels, run on every change? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-04 | Is test coverage of critical paths measured and reported? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-05 | Are coding standards enforced by linters or formatters? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-06 | Are dependencies pinned, scanned and updated on a schedule? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-07 | Are third-party licences inventoried and compatible with the business model? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-08 | Is the history free of committed secrets, or were leaks rotated? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-09 | Can a new engineer build and run the project from the documentation? | {{pending: link}} | {{pending: score}} | {{pending: finding}} |
| SRC-10 | Do contributors' agreements or employment terms assign IP to the organisation? | {{pending: link, confirmed by counsel}} | {{pending: score}} | {{pending: finding}} |

## Red flags

- Code in personal accounts or without clear ownership.
- Copyleft code in a distributed product without a decision.
- Secrets in the history that were never rotated.

## Output

- Area score: {{pending: score and method}}
- Findings carried to the [DD report](../dd-report-template.md).

## Related

- [DD strategy](../dd-strategy.md)
- [Checklist 02 — Architecture](02-architecture.md)
- [Checklist 04 — Security](04-security.md)
- [Final checklist](11-final-report.md)
