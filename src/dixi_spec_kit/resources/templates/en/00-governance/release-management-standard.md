# Release management standard

## Purpose

Define how a change becomes a release: what a release contains, who decides it goes out, which checks must pass and how it is communicated and reversed if needed.

Status: draft. {{pending: confirm the release process with the responsible person}}

## Release types

| Type | Content | Cadence | Approval |
|------|---------|---------|----------|
| Regular | Features and fixes merged since the last release | {{pending: cadence}} | {{pending: approver}} |
| Patch | Urgent fixes only | As needed | {{pending: approver}} |
| Major | Breaking changes, with migration notes | Planned | {{pending: approver}} |

## Readiness checklist

- [ ] Every included change was reviewed and merged by a person.
- [ ] `make verify` and the project's real test suite passed on the release commit.
- [ ] Version number follows the [versioning policy](policies/versioning-policy.md).
- [ ] Release notes list user-visible changes, breaking changes and migrations.
- [ ] Data migrations have a tested rollback or a forward-fix plan.
- [ ] Monitoring and alerts for the changed areas are in place.
- [ ] A rollback path is known and has an owner.

## Roles

| Role | Responsibility |
|------|----------------|
| Release owner | Coordinates, decides go or no-go. |
| Reviewer | Confirms the checklist with evidence. |
| On-call | Watches the release and can trigger rollback. |

Agents may prepare release notes and run checks; they never approve or deploy.

## Rollout

- Promote through environments in order: [Environment strategy](environment-strategy.md).
- {{pending: rollout technique, for example all at once, canary or feature flags}}
- Freeze windows: {{pending: periods when releases are not allowed}}

## After the release

- Watch key indicators for {{pending: observation window}}.
- Record the outcome and any incident in the decision log.
- If a rollback happens, write a postmortem.

## Related

- [Versioning policy](policies/versioning-policy.md)
- [Environment strategy](environment-strategy.md)
- [Observability standard](observability-standard.md)
- [Incident policy](policies/incident-policy.md)
- [Deployment architecture](../09-architecture/deployment-architecture.md)
