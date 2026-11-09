# Agent capability matrix

## Purpose

Record what each agent role is allowed to do, so that permissions are granted on purpose and reviewed when they change. Anything not listed is denied by default.

## Capabilities by role

Legend: **Y** allowed, **C** allowed with human confirmation, **N** not allowed.

| Capability | Specifier | Contract writer | Test writer | Builder | Reviewer |
| --- | --- | --- | --- | --- | --- |
| Read specs and code | Y | Y | Y | Y | Y |
| Write spec files | Y | Y | N | N | N |
| Write test files | N | N | Y | N | N |
| Write source code | N | N | N | Y | N |
| Run tests and `dixi check` | Y | Y | Y | Y | Y |
| Install dependencies | N | N | N | C | N |
| Run shell commands that change state | N | N | C | C | N |
| Network access | {{pending: Y / C / N}} | {{pending: define}} | {{pending: define}} | {{pending: define}} | {{pending: define}} |
| Create branches and commits | N | N | C | C | N |
| Push, open pull requests | {{pending: Y / C / N}} | N | N | C | N |
| Approve, merge, deploy | N | N | N | N | N |
| Read secrets or credentials | N | N | N | N | N |

Adjust the columns to the roles defined in the agent architecture.

## External tools

| Tool or server | Purpose | Roles allowed | Read or write |
| --- | --- | --- | --- |
| {{pending: tool name}} | {{pending: purpose}} | {{pending: roles}} | {{pending: read / write}} |

## Rules

- Grant capabilities per task, not per convenience.
- Write access to tests and to code should not belong to the same unattended step.
- Changes to this matrix are structural: record the reason and the approver.

## Review

- Review cadence: {{pending: when this matrix is reviewed}}

## Related

- [Agent architecture](agent-architecture.md)
- [Guardrails](guardrails.md)
- [Human in the loop](human-in-the-loop.md)
- [Quality gates](../governance/quality-gates.md)
