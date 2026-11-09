# Troubleshooting index

## Purpose

Point from a symptom to its most likely cause and the document or runbook that fixes it, so that common problems are solved in minutes and the same investigation is not repeated.

Status: draft. {{pending: fill with the problems actually seen in this project}}

## How to use it

- Search for the symptom as you saw it (error text, failing check).
- Follow the link; if the fix is missing or wrong, update the entry.
- Add an entry after any problem that took more than {{pending: time}} to solve.

## Local environment and agents

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `dixi check` reports a broken link | A file was moved or renamed | Update the relative link and `.dixi/traceability.json` |
| `dixi check` reports an unknown ID | Item not registered | Add it with its parents to `.dixi/traceability.json` |
| An agent refuses to read a file | File looks like a secret | Expected; provide a non-secret example instead |
| `make verify` passes but the app is broken | Real tests not connected | Connect the test suite to `make verify` |

## Pull request checks

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| A test changed after commit | Frozen test edited | Revert; follow the [testing policy](../00-governance/policies/testing-policy.md) |
| Missing translation key | String added in code | Move it to the language catalogs |
| {{pending: symptom}} | {{pending: cause}} | {{pending: fix}} |

## Delivery and runtime

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Works in staging, fails in production | Configuration drift | Compare with the [environment strategy](../00-governance/environment-strategy.md) |
| Alert without runbook | Alert added without owner | Write a runbook from the [template](../10-engineering/templates/runbook-template.md) |
| {{pending: symptom}} | {{pending: cause}} | {{pending: fix}} |

## Security

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Secret found in history | Committed by mistake | Rotate first, then clean; see [secret management](../13-security/secret-management.md) |

## Related

- [FAQ](faq.md)
- [Incident policy](../00-governance/policies/incident-policy.md)
- [Observability standard](../00-governance/observability-standard.md)
