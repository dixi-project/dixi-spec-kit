# Known issues

## Purpose

List problems that are understood but not yet fixed, with their workaround, so support can answer quickly and nobody re-investigates the same issue.

Status: draft. {{pending: name who curates this list}}

## How to use

- Support checks this list before escalating a ticket.
- Engineering adds an entry as soon as an issue is confirmed and will not be fixed within {{pending: days}}.
- An entry is removed only when the fix is released and verified.

## Entry format

| ID | Summary | Affected | Workaround | Severity | Ticket | Since | Target fix |
|----|---------|----------|------------|----------|--------|-------|------------|
| KI-001 | {{pending: short description}} | {{pending: feature, platform, users}} | {{pending: steps users or support can take}} | {{pending: SEV3 / SEV4}} | {{pending: link}} | {{pending: date}} | {{pending: release or date}} |

## Writing a good entry

- Describe the symptom as a user sees it, not the internal cause.
- Give a workaround that support can share as is, or state clearly that there is none.
- Record which versions, browsers or plans are affected.
- Never paste personal data, tokens or customer names into an entry.

## Severity

Entries are normally SEV3 or SEV4. An issue that would be SEV2 or higher is an incident, not a known issue: follow [incident levels](incident-levels.md).

## Public or internal

{{pending: decide whether some entries are published to users, for example on a help page}}

Entries marked public must be reviewed by the communications role before publishing.

## Review

- Every {{pending: frequency}}, check each entry: still valid, workaround still works, fix date still realistic.
- An entry older than {{pending: months}} gets an explicit decision: fix, accept or close.

## Related

- [Support model](support-model.md)
- [Service catalog](service-catalog.md)
- [Incident levels](incident-levels.md)
