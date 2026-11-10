# Dependency scanning

## Purpose

Describe how the project detects known vulnerabilities, risky licenses and suspicious packages in its third-party dependencies, and what happens when a finding appears.

Status: draft. {{pending: name the owner of dependency hygiene}}

## Scope

- Package ecosystems in use: {{pending: list the package managers and lockfiles}}
- Container images or base images, if any: {{pending: list}}
- Build and CI tooling dependencies: {{pending: list}}

## Baseline rules

- Commit lockfiles and install from them so builds are reproducible.
- Pin versions; prefer hash pinning where the ecosystem supports it.
- Add a new dependency only with a stated reason; prefer the standard library or an existing dependency.
- Check that a package name is the intended one before installing it (typosquatting, look-alike names).
- AI agents propose dependencies; a human approves them.

## When scans run

| Moment | What is scanned | Blocks merge? |
|--------|-----------------|---------------|
| Pull request | Changed dependencies | {{pending: yes / no, and from which severity}} |
| Scheduled | Full dependency tree | No, opens a finding |
| Before release | Full tree and images | {{pending: decide}} |

Scanning tool or service: {{pending: choose one or more scanners; none is required by this kit}}

## Handling findings

1. Confirm the vulnerable code path is reachable, or assume it is when unsure.
2. Upgrade, replace or remove the dependency.
3. If no fix exists, record a temporary exception with an owner, a justification and an expiry date.
4. Add or update a test when the fix changes behaviour.

## Exceptions

| Package | Finding | Reason | Owner | Expires |
|---------|---------|--------|-------|---------|
| {{pending: package}} | {{pending: identifier}} | {{pending: reason}} | {{pending: owner}} | {{pending: date}} |

## Related

- [Licensing policy](licensing/licensing-policy.md)
- [Threat model](threat-model.md)
- [Incident response](incident-response.md)
- [Test plan](../11-quality/test-plan.md)
