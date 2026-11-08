# Threat model — Procedure preparation B2a

## Purpose

Extend the B1 analysis to requests, context selection and shared recipes, before implementing TASK-002. No agents executed and no files written.

## Threats and coverage

| Threat / STRIDE | Control | Planned evidence |
|---|---|---|
| Spoofing a target or type | Exact ID, per-operation types, validated graph | Missing/incompatible targets, invalid parents and duplicates. |
| Altering or fabricating evidence | Hash of current bytes, prepared status, no implicit approval | Identical repetition and hash change on edit. |
| Reading out of scope / disclosure | B1 confined root; ancestor selection; no bodies and no links followed; only known fields of the target | Symlinks/FIFO, traversal, sensitive names, unrelated branch not read and `test_target_excludes_unknown_fields`. |
| Exhausting memory or blocking reads | 1 MiB/file, 64 sources, 2 MiB total, request 4 096 characters | Cases for each limit and special files. |
| Executing malicious text / elevation | Request as data, no subprocess/network; recipes with guards | Shell request not executed, sockets blocked, snapshot unchanged. |
| Hiding missing controls / repudiation | Explicit status and scope; common and specific gates | Complete recipes, prepared status and no project bodies. |
| Losing resources in distribution | Allowlist and loading from importlib.resources | Walkthrough in wheel and in a wheel rebuilt from sdist. |

## Residual risk

The manifest is neither a snapshot nor a signature; a consumer must revalidate hashes. The CLI does not interpret whether a project instruction is safe nor does it impose guards on an external agent. It does not detect secrets with arbitrary names: secret files must not be registered as specs. A prepared package does not certify completeness, consent or design quality. Injection/gate evaluations for each adapter remain pending before it is announced.

## Related

- [Contract](../07-contracts/commands/workflow-preparation-contract.md)
- [B1 threats](local-core-threat-model.md)
- [Feature](../05-features/workflow-preparation/feature-spec.md)
