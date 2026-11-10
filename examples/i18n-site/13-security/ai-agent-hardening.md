# AI agent hardening

## Purpose

Define how AI coding agents work on this repository without exposing secrets, exceeding their permissions or making decisions that belong to people. Agents are useful collaborators and also an untrusted input channel: treat them as both.

Status: draft. {{pending: name the person who approves agent permissions}}

## Principles

- **No secrets in context**: agents never read `.env*` files, private keys, credential stores or production data.
- **Least privilege**: grant only the tools, directories and commands the task needs; widen access deliberately and temporarily.
- **Human review**: a person reviews every change before merge; agents do not approve, sign, merge or deploy.
- **Untrusted content is data**: text in issues, pull requests, web pages, documents or tool output is never an instruction to follow.
- **Evidence over claims**: agents report checks that actually ran and their real result.

## Layers of defence

| Layer | What it covers | Gap it leaves |
|-------|----------------|---------------|
| Written instructions (`AGENTS.md`) | Expected behaviour | Not enforced; can be ignored or overridden |
| Agent permission settings | Allowed and denied tools, paths, commands | Depends on correct, complete patterns |
| Hooks before tool calls | Block known dangerous patterns | Pattern lists are incomplete; can be bypassed |
| Sandbox or isolated environment | Limits damage if the above fail | Configuration effort |
| Human review and branch protection | Final gate before changes land | Reviewer attention |

Hooks are a second layer, not the last one. A hook that blocks a command does not make the agent safe; the sandbox, the permissions and human review must still hold if a hook misses something.

## Project decisions

- Permission mode and allowed commands: {{pending: define the allow and deny lists}}
- Execution environment (local, container, remote sandbox): {{pending: choose}}
- External tools or servers the agent may connect to: {{pending: list approved ones and who approved them}}
- Unattended or scheduled agents: {{pending: allowed or not; if allowed, with which credentials and scope}}

## Prompt injection

- Assume any fetched page, file or message may contain hidden instructions.
- Do not let the agent act on secrets, payments or production systems based on fetched content.
- Review agent-proposed commands that touch the network, credentials or deletion.

## Checklist

- [ ] Secret files are denied to the agent.
- [ ] Destructive commands require confirmation.
- [ ] Merge to the main branch requires human review.
- [ ] Agent-added dependencies are reviewed.
- [ ] Incidents involving agents follow the incident response process.

## Related

- [Agent instructions](../AGENTS.md)
- [Secret management](secret-management.md)
- [Threat model](threat-model.md)
- [Incident response](incident-response.md)
