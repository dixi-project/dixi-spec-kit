# Dependency policy

## Purpose

Control how third-party libraries, tools and runtimes enter and stay in this project, so that each dependency is justified, reproducible, licensed correctly and kept up to date.

Status: draft. {{pending: confirm this policy with the responsible person}}

## Adding a dependency

Before adding one, answer in the pull request:

- [ ] What problem does it solve, and why not the standard library or existing code?
- [ ] Is it maintained (recent releases, responsive maintainers)?
- [ ] Is its licence on the approved list?
- [ ] Does it have known vulnerabilities?
- [ ] How many transitive dependencies does it bring?
- [ ] Is it a runtime or a development-only dependency?

Approver for new runtime dependencies: {{pending: approver}}

## Pinning and reproducibility

- Pin exact versions in a lock file; commit the lock file.
- Verify integrity with hashes when the ecosystem supports it.
- Builds must be reproducible from the repository alone.
- Do not fetch code at runtime from unpinned sources.

## Updates

| Type | Frequency | Rule |
|------|-----------|------|
| Security fixes | {{pending: e.g. within N days by severity}} | Prioritized over feature work |
| Minor and patch | {{pending: cadence}} | Batched, with tests green |
| Major | Planned | Own pull request, with migration notes |

## Supported runtimes

| Runtime | Supported versions | End of support plan |
|---------|--------------------|---------------------|
| {{pending: runtime}} | {{pending: versions}} | {{pending: plan}} |

## Removal

- Remove dependencies that are no longer used.
- Replace abandoned dependencies before they block a security fix.

## Related

- [Approved licences](../../13-security/licensing/approved-licenses.md)
- [Licensing policy](../../13-security/licensing/licensing-policy.md)
- [Dependency scanning](../../13-security/dependency-scanning.md)
- [Security baseline](../security-baseline.md)
