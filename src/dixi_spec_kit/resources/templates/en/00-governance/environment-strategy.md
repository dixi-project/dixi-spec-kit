# Environment strategy

## Purpose

Define which environments this project uses, what each one is for, how changes move between them and which rules keep them isolated from each other.

Status: draft. {{pending: confirm the list of environments}}

## Environments

| Environment | Purpose | Data | Who deploys | Who has access |
|-------------|---------|------|-------------|----------------|
| Local | Development and tests on a laptop | Synthetic | Developer | Developer |
| Development | Integration of merged work | Synthetic | Automated pipeline | Team |
| Staging | Production-like validation | Masked or synthetic | Automated pipeline | Team, reviewers |
| Production | Real users | Real | {{pending: who or what deploys}} | {{pending: named roles}} |

{{pending: add or remove environments, for example preview environments per pull request}}

## Rules

- Each environment has its own secrets, identities and data. Nothing is shared with production.
- Real personal data never leaves production.
- Configuration differs between environments only through configuration, not code branches.
- The same build artifact is promoted from one environment to the next.
- Agents never deploy to any shared environment.

## Promotion path

1. Merge to the main branch after review.
2. Deploy to development automatically; run smoke tests.
3. Promote to staging; run acceptance and regression checks.
4. Promote to production after the release owner's go decision.

Gate between staging and production: {{pending: required checks and approver}}

## Parity

| Aspect | Must match production | May differ |
|--------|-----------------------|------------|
| Runtime and versions | Yes | |
| Infrastructure shape | Yes | |
| Scale and size | | Yes |
| Data volume | | Yes |

## Cost and lifecycle

- Non-production environments are sized for their purpose and can be stopped when idle. {{pending: idle policy}}
- Temporary environments are deleted when their branch is closed.

## Related

- [Release management standard](release-management-standard.md)
- [Security baseline](security-baseline.md)
- [Deployment architecture](../09-architecture/deployment-architecture.md)
- [Secret management](../13-security/secret-management.md)
