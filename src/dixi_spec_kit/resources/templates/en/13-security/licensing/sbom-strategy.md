# SBOM strategy

## Purpose

Define how the project produces and keeps a software bill of materials (SBOM): a machine-readable list of every component in each release, used to answer quickly "are we affected?" when a new vulnerability or license issue appears.

Status: draft. {{pending: name the owner of the SBOM process}}

## Scope

- Artifacts covered: {{pending: e.g. application packages, container images, libraries}}
- Depth: direct and transitive dependencies, base images and bundled binaries.
- Excluded and why: {{pending: list}}

## Format

- SBOM format: {{pending: choose an open standard format}}
- Component identifiers: package URLs and SPDX license identifiers where available.
- Each SBOM records the artifact name, version, build date and source revision.

## Generation

| Moment | Artifact | Output location |
|--------|----------|-----------------|
| Every release build | {{pending: artifact}} | {{pending: where it is stored}} |
| On demand | Current main branch | Build output |

Generator tool: {{pending: choose; this kit does not require a specific one}}

Generate the SBOM from the built artifact or the lockfile used for the build, not from a hand-written list.

## Integrity and storage

- Store SBOMs next to the release they describe and keep them for {{pending: retention period}}.
- {{pending: decide whether SBOMs are signed or checksummed}}

## Use

- Feed SBOMs to vulnerability and license checks.
- When a new advisory appears, search stored SBOMs to find affected releases.
- {{pending: decide whether SBOMs are shared with customers and how}}

## Related

- [Licensing policy](licensing-policy.md)
- [Approved licenses](approved-licenses.md)
- [Dependency scanning](../dependency-scanning.md)
- [Vulnerability management](../vulnerability-management.md)
