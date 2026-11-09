# RTO and RPO Matrix

## Purpose

Record, per business capability, how long it may be unavailable (RTO) and how much recent data may be lost (RPO) after a disaster. These targets drive the cost of the recovery strategy, so the business sets them, not engineering alone.

## Definitions

- **RTO** (recovery time objective): maximum acceptable time from the start of the outage to restored service.
- **RPO** (recovery point objective): maximum acceptable window of data loss, measured back from the moment of failure.
- **Tier**: a group of capabilities that share the same targets.

## Tiers

| Tier | Meaning | RTO | RPO |
|---|---|---|---|
| 1 | Core flow; the business stops without it | {{pending: target}} | {{pending: target}} |
| 2 | Important; workarounds exist for a while | {{pending: target}} | {{pending: target}} |
| 3 | Can wait until normal operations resume | {{pending: target}} | {{pending: target}} |

Example only, not a recommendation: a tier 1 with RTO of 4 hours and RPO of 15 minutes usually requires continuous backups and a rehearsed restore.

## Matrix

| Capability | Tier | RTO | RPO | Data stores involved | Recovery strategy | Owner | Last validated |
|---|---|---|---|---|---|---|---|
| {{pending: e.g. sign-in}} | {{pending: tier}} | {{pending: target}} | {{pending: target}} | {{pending: stores}} | {{pending: strategy}} | {{pending: role}} | {{pending: date}} |
| {{pending: e.g. checkout}} | {{pending: tier}} | {{pending: target}} | {{pending: target}} | {{pending: stores}} | {{pending: strategy}} | {{pending: role}} | {{pending: date}} |
| {{pending: e.g. reporting}} | {{pending: tier}} | {{pending: target}} | {{pending: target}} | {{pending: stores}} | {{pending: strategy}} | {{pending: role}} | {{pending: date}} |

## Consistency checks

- Backup frequency for each data store is at least as frequent as the smallest RPO that depends on it.
- The measured restore time in tests is below the RTO; if not, the gap is recorded as a risk.
- External commitments (SLAs, contracts) do not promise faster recovery or less data loss than these targets allow.

## Review

Review with business owners {{pending: frequency}} and after any change to architecture or contracts.

## Related

- [Disaster recovery strategy](dr-strategy.md)
- [Rollback strategy](../rollback-strategy.md)
- [Goal](../../01-business/vision.md)
