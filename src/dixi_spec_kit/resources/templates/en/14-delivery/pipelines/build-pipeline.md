# Build Pipeline

## Purpose

Describe the pipeline that turns a commit into a verified, immutable artifact. It runs on every pull request and on every merge to the main branch, and it never deploys to production.

## Triggers

- Pull request opened or updated: full checks, artifact discarded.
- Merge to main: full checks, artifact kept and tagged.
- Manual run: {{pending: allowed or not}}.

## Steps

| # | Step | Command or action | Fails the build when |
|---|---|---|---|
| 1 | Checkout | Fetch the exact commit | Commit cannot be fetched |
| 2 | Install | Install pinned dependencies from the lockfile | Lockfile out of date or hash mismatch |
| 3 | Verify (gate) | `make verify` | Any check fails |
| 4 | Unit and contract tests | {{pending: test command}} | Any test fails |
| 5 | Static analysis | {{pending: linters and type checks}} | New findings above {{pending: threshold}} |
| 6 | Dependency and secret scan | {{pending: scanners}} | Known vulnerability above {{pending: severity}} or secret found |
| 7 | Build artifact | {{pending: build command}} | Build error |
| 8 | Tag and store | Tag with the commit identifier and store in {{pending: registry}} | Upload fails |

Step 3 is mandatory: if `make verify` fails, no later step runs.

## Artifact rules

- Built once; the same artifact goes to staging and production.
- Contains its commit identifier and build date; no environment-specific values.
- Signed or checksummed: {{pending: method}}.
- Retained for {{pending: period}} to allow rollback.

## Performance

- Target duration: {{pending: minutes}}.
- Cache dependencies by lockfile hash; never cache build outputs between commits without a key.

## Security

- The build runs with read-only access to the repository and write access only to the artifact store.
- Pull requests from forks do not receive secrets.

## Related

- [Release pipeline](release-pipeline.md)
- [Migration pipeline](migration-pipeline.md)
- [CI/CD overview](../ci-cd-overview.md)
- [Dependency scanning](../../13-security/dependency-scanning.md)
- [Verification ladder](../../11-quality/verification-ladder.md)
