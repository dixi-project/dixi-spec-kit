# Backup and Recovery

## Purpose

Record what data is backed up, how often, where copies live and how a restore is performed and tested. A backup that has never been restored is an assumption, not a backup.

## Inventory

| Data store | Contents | Method | Frequency | Retention | Copy location | Encrypted | Owner |
|---|---|---|---|---|---|---|---|
| Primary database | {{pending: description}} | {{pending: snapshot, continuous log or dump}} | {{pending: frequency}} | {{pending: days}} | {{pending: separate location or account}} | {{pending: yes or no}} | {{pending: role}} |
| Object storage | {{pending: user files, exports}} | {{pending: versioning or replication}} | {{pending: frequency}} | {{pending: days}} | {{pending: location}} | {{pending: yes or no}} | {{pending: role}} |
| Configuration | Versioned in the repository | Version control | Every change | Full history | Remote repository | n/a | {{pending: role}} |

## Rules

- At least one copy lives outside the primary location and outside the reach of production credentials.
- Backups are encrypted; the keys are managed separately from the data.
- Deleting or shortening retention of backups requires two people.
- Retention respects the data retention policy, including deletion requests.

## Restore procedure

1. Declare the restore and record who approved it.
2. Choose the restore point and confirm the expected data loss with the owner.
3. Restore into an isolated environment first and verify integrity.
4. Switch the application to the restored data or copy the needed records back.
5. Record the time taken and any data lost.

## Restore testing

| Data store | Last test | Result | Time to restore | Next test |
|---|---|---|---|---|
| {{pending: store}} | {{pending: date}} | {{pending: result}} | {{pending: duration}} | {{pending: date}} |

Test frequency: {{pending: e.g. quarterly}}. Record real results only; never mark a test as passed without running it.

## Related

- [Data retention policy](../08-data/retention-policy.md)
- [Data architecture](../08-data/data-architecture.md)
- [Secret management](../13-security/secret-management.md)
- [Rollback strategy](rollback-strategy.md)
