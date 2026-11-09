# Service catalog

## Purpose

Keep one list of the services the project runs, with their owner, criticality and dependencies, so that operations, support and incident response all speak about the same things.

Status: draft. {{pending: name the owner of the catalog}}

## Catalog

| Service | What it does | Owner | Criticality | Depends on | Runbook | Status |
|---------|--------------|-------|-------------|------------|---------|--------|
| {{pending: e.g. web app}} | {{pending: description}} | {{pending: team or role}} | {{pending: critical / high / normal}} | {{pending: services and vendors}} | {{pending: link}} | {{pending: active / deprecated}} |

Add one row per deployable unit or user-facing capability. {{pending: decide the granularity: deployable unit or business capability}}

## Criticality

| Level | Meaning | Incident floor |
|-------|---------|----------------|
| Critical | Users cannot do the main job without it | SEV2 or higher when broken |
| High | Important but has a workaround | SEV3 or higher |
| Normal | Internal or secondary | SEV4 or higher |

Keep the list of critical services aligned with the critical flows in [incident levels](incident-levels.md).

## Required per service

- A named owner (team or role, not a single person who might leave).
- Health signals and alerts that page the on-call rotation.
- A runbook for the most common failures.
- The vendors it depends on, listed in the [vendor catalog](vendor-management/vendor-catalog.md).
- Its targets, if any: availability, latency, recovery time. {{pending: set targets per critical service}}

## Lifecycle

- **New service**: added here before it reaches production.
- **Deprecated**: marked, with an end date and a migration path for users.
- **Retired**: removed after its data, alerts and access are cleaned up.

## Review

Review the catalog every {{pending: frequency}} and after every architecture change.

## Related

- [Support model](support-model.md)
- [Incident levels](incident-levels.md)
- [On-call rotation](team/on-call-rotation.md)
- [Vendor catalog](vendor-management/vendor-catalog.md)
- [Maintenance window policy](maintenance-window-policy.md)
