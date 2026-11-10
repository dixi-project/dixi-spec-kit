# Versioning policy

## Purpose

Define how the project, its public contracts and its documents are versioned, so that consumers know what changed and whether an update can break them.

Status: draft. {{pending: confirm the versioning scheme}}

## Product version

- Scheme: {{pending: e.g. semantic versioning MAJOR.MINOR.PATCH, or calendar versioning}}
- With semantic versioning:
  - **MAJOR** for incompatible changes to public behaviour or contracts.
  - **MINOR** for backward-compatible features.
  - **PATCH** for backward-compatible fixes.
- Pre-releases use a suffix, for example `1.4.0-rc.1`.

## Contracts

| Contract type | How the version is expressed | Breaking change rule |
|---------------|------------------------------|----------------------|
| HTTP APIs | {{pending: path, header or media type}} | New major version; old one deprecated, not removed at once |
| Events | Version field in the schema | New event version; consumers migrate |
| Files and exports | Version in the header or name | Documented in release notes |

## Kit version

- The DIXI Spec Kit version used to create the project is recorded in `.dixi/project.json`.
- Updating the kit is a reviewed change, like any other.

## Changelog

- Every release has notes: added, changed, deprecated, removed, fixed, security.
- Breaking changes include a migration note.
- {{pending: where the changelog lives}}

## Deprecation

- Announce deprecations at least {{pending: notice period}} before removal.
- Keep deprecated behaviour tested until it is removed.

## Who decides

- Version bumps are proposed in the release pull request and confirmed by {{pending: role}}.

## Related

- [Branching strategy](branching-strategy.md)
- [Documentation policy](documentation-policy.md)
- [Contract example](../../07-contracts/example.md)
