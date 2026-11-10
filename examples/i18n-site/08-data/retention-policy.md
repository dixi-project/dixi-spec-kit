# Retention Policy

## Purpose

State how long each category of data is kept, why, and what happens when the period ends. Keeping data longer than needed increases risk and cost; deleting it too early breaks legal, contractual or operational needs.

- Owner: {{pending: person or role accountable for retention}}
- Review cadence: {{pending: how often this policy is reviewed}}

## Principles

- Keep data only while there is a documented purpose for it.
- Every category has an explicit period and an explicit end-of-life action.
- Legal holds override deletion and are recorded.
- Backups follow the same rules, with a documented lag.
- Deletion is verifiable: there is evidence that it ran.

## Retention schedule

| Data category | Classification | Active period | Archive period | End-of-life action | Basis |
| --- | --- | --- | --- | --- | --- |
| User accounts | Personal | While the account is active | {{pending: period}} | Delete or anonymise | {{pending: basis}} |
| Transactions / orders | | {{pending: period}} | | | {{pending: legal or tax requirement}} |
| Application logs | Internal | {{pending: period}} | — | Delete | Operations |
| Audit records | | {{pending: period}} | | | |
| Backups | Mixed | {{pending: period}} | — | Expire | Recovery |
| Analytics events | | | | Aggregate, then delete | |

Classification values come from the [PII classification](pii-classification.md).

## End-of-life actions

| Action | Meaning | When to use |
| --- | --- | --- |
| Delete | Remove the record and its copies | No remaining purpose |
| Anonymise | Remove or irreversibly transform identifying fields | Statistics still needed |
| Archive | Move to cheaper, restricted storage | Legal need, rare access |
| Aggregate | Keep only totals or summaries | Trends, not individuals |

## Implementation checklist

- [ ] Each table or store with Personal data has a retention rule and an owner.
- [ ] A scheduled job applies the rules: {{pending: mechanism and frequency for purge jobs}}
- [ ] Purge jobs are idempotent, run in batches and record what they removed (counts, not content).
- [ ] Erasure requests propagate to replicas, caches, search indexes, exports and backups.
- [ ] Legal holds can suspend deletion for specific records and are logged.
- [ ] Tests cover that expired records are actually removed or anonymised.

## Exceptions

| Exception | Scope | Approved by | Expires |
| --- | --- | --- | --- |
| | | | |

## Related

- [PII classification](pii-classification.md)
- [Master spec](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)
