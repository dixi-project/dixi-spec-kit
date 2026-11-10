# Documentary workflow

## Purpose

Work without depending on a specific agent or language.

1. Complete the goal, domain, and module; preserve their IDs.
2. Define a feature and observable criteria.
3. Document contracts and planned tests; validate structural decisions.
4. Register paths and parents in `.dixi/traceability.json`.
5. Choose a stack and connect its real tests to `make verify`.
6. Run checks and request human review before merging.

The CLI provides `init`, `doctor`, `check`, `workflow`, help, and version. With `--agent claude`, the `/dixi.*` commands live in `.claude/commands/`; with `--agent none` no agent commands are installed. Edit documents with your own tools. Hashes in `.dixi/project.json` preserve original files for future updates; do not alter them to simulate verification. Keep secrets outside the repository and private context untracked in `.context/`. Provider policies are explicit project decisions; no accounts or connections are configured.

## Related

- [Project](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)

## Shared procedures

Use `dixi --lang en workflow list` and `dixi --lang en workflow show discover`. Prepare context with `dixi --lang en workflow prepare discover --target GOAL-001 --request "Describe the need"`. `prepare` does not write specs or run an agent: it provides steps, gates and a source manifest with hashes. Complete the procedure with your tools, preserve IDs and record open questions. Never include secrets in the request.
