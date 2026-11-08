# ADR-103 — Public verification CI on GitHub Actions, without credentials

## Purpose

Decide where the checks for pull requests to the public repository run, including those coming from forks, without exposing Dixi infrastructure or credentials.

## Status

Accepted on 2026-11-08 by the responsible person. First green run in the public repository (Ubuntu and macOS, Python 3.11 and 3.13); the checks are required in the `main` ruleset.

## Context

The inherited EIS-IA rule runs checks on CodeBuild runners in Dixi's account and deploys through CodePipeline (ADR-006 of the origin). A public repository receives PRs from forks: running them on the organization's runners would expose internal infrastructure to third-party code. DIXI Spec Kit deploys nothing: its release is a tag and some artifacts published by a person.

## Decision

1. Public checks run on GitHub-hosted runners (`ubuntu-latest` and `macos-latest`), with `permissions: contents: read`, no secrets, no OIDC and no AWS access.
2. The event is `pull_request` (never `pull_request_target`) and `push` to `main`. Actions are pinned by SHA.
3. The `verify` job installs only hash-pinned Setuptools and runs `make verify` on Python 3.11 and 3.13.
4. The `dco` job requires `Signed-off-by` on every commit in the PR (ADR-010 of the origin).
5. There is no automatic deployment. The v1.0.0 release is created by a person from a green commit.

## Consequences

A narrowly scoped exception for this public repository: it does not change the rules of the origin or of private Dixi projects. CI minutes are covered by GitHub for public repositories. If publishing to PyPI from CI happens in the future, it will require another ADR (for example, trusted publishing with manual approval).

## Related

- [ADR-100](ADR-100-distribucion-publica-v1.md)
- [Repository settings](../../docs/repository-settings.md)
- [Workflow](../../.github/workflows/verify.yml)
