# Disaster Recovery Strategy

## Purpose

Decide how the system recovers from losing a whole component, location or provider service, and how much downtime and data loss the business accepts. Day-to-day failures are handled by rollback and runbooks; this document covers the rare, severe events.

## Scenarios

| Scenario | Example | Likelihood | Impact | Covered by |
|---|---|---|---|---|
| Data corruption or deletion | Faulty migration, human error | {{pending: rating}} | {{pending: rating}} | Point-in-time restore |
| Loss of the primary location | Regional outage of the hosting | {{pending: rating}} | {{pending: rating}} | {{pending: strategy}} |
| Compromised credentials | Attacker deletes resources | {{pending: rating}} | {{pending: rating}} | Isolated backups, incident response |
| Loss of a critical third party | Payment or identity service down | {{pending: rating}} | {{pending: rating}} | {{pending: fallback or degraded mode}} |

## Recovery strategies

| Strategy | Description | Typical cost | Typical recovery time |
|---|---|---|---|
| Backup and restore | Rebuild from code and restore data | Low | Hours |
| Pilot light | Minimal copy of core data and services kept ready elsewhere | Medium | Tens of minutes to hours |
| Warm standby | Scaled-down full copy running elsewhere | High | Minutes |
| Active/active | Full capacity in more than one location | Highest | Near zero |

The recovery times above are rough orders of magnitude, not commitments.

Chosen strategy: {{pending: per tier, aligned with the RTO/RPO matrix and recorded in an ADR}}

## Prerequisites

- Infrastructure can be recreated from versioned code.
- Backups are stored outside the primary location and outside production credentials.
- Secrets and keys needed to recover are available from a second location.
- Contact list and decision rights are written down: {{pending: who declares a disaster}}.

## Exercises

| Exercise | Frequency | Last run | Result |
|---|---|---|---|
| Tabletop walkthrough | {{pending: frequency}} | {{pending: date}} | {{pending: result}} |
| Restore test | {{pending: frequency}} | {{pending: date}} | {{pending: result}} |

Record only exercises actually performed.

## Related

- [RTO and RPO matrix](rto-rpo-matrix.md)
- [Rollback strategy](../rollback-strategy.md)
- [Environments](../environments.md)
- [Incident response](../../13-security/incident-response.md)
- [Project](../../00-master-spec.md)
