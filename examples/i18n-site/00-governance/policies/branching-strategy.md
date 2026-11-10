# Branching strategy

## Purpose

Define how branches, commits, pull requests and merges work in this repository, so that the main branch is always releasable and every change reaches it through human review.

Status: draft. {{pending: confirm the branching model with the team}}

## Branches

| Branch | Purpose | Lifetime | Who merges into it |
|--------|---------|----------|--------------------|
| `main` | Always releasable history | Permanent | A person, through a reviewed pull request |
| `feat/<topic>` | New behaviour | Days | — |
| `fix/<topic>` | Bug fix | Hours to days | — |
| `docs/<topic>` | Documentation only | Hours to days | — |
| `release/<version>` | Release preparation, if used | Until release | {{pending: whether release branches are used}} |

- Nobody pushes directly to `main`, including agents.
- Branches are short-lived; rebase or merge `main` often to avoid drift.

## Commits

- Format: `[area] action: description`, for example `[05-features] add: password reset criteria`.
- One logical change per commit.
- The red test is committed alone, before the implementation (`... (red)`).
- Commits made with AI assistance are signed, when signing is required, by the person, never by the agent.

## Pull requests

- [ ] Links to the spec or task it implements.
- [ ] Describes what changed and how it was verified, with the real `make verify` result.
- [ ] States whether AI assisted and which parts.
- [ ] Is small enough to review in one sitting. {{pending: soft size limit}}
- [ ] Has at least {{pending: number}} human approval(s).

## Merge type

{{pending: choose squash, rebase or merge commits, and why}}

## Tags

- Releases are tagged from `main` following the [versioning policy](versioning-policy.md).

## Repository settings checklist

- [ ] `main` is protected against direct pushes and force pushes.
- [ ] Required checks must pass before merge.
- [ ] Required reviews are enforced.
- [ ] Stale approvals are dismissed when new commits arrive.

## Related

- [Testing policy](testing-policy.md)
- [Versioning policy](versioning-policy.md)
- [Engineering standards](../engineering-standards.md)
- [Project instructions](../../AGENTS.md)
