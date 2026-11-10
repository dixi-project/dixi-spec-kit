# Example walkthrough

## Purpose

Record how this example was built with DIXI Spec Kit, step by step, so that you can repeat it. The responsible person and the studio are fictitious.

The documents were written by following each `/dixi.*` command's steps with Claude Code. If you repeat it, the wording will vary; what must hold is the structure, the traceability and `make verify` green.

## Steps

| Step | Command | Result in this repository |
|---|---|---|
| 1 | `dixi init i18n-site --agent claude --profile site` | Documentation base, `CLAUDE.md`, the `/dixi.*` commands, four subagents and the 77 optional `site` templates. |
| 2 | `/dixi.discover A Next.js site in English and Spanish, indexable per language` | `00-master-spec.md` and `01-business/vision.md` (GOAL-001). |
| 3 | `/dixi.specify Language-prefixed pages with SEO alternates` | Domain, module and FEATURE-001 with five verifiable criteria; `00-governance/policies/i18n-policy.md` completed. |
| 4 | `/dixi.plan FEATURE-001` | CONTRACT-001, test plan TEST-001 and [ADR-001](../09-architecture/adr/ADR-001-i18n-logic-in-plain-modules.md) (accepted by the person). |
| 5 | `/dixi.tasks FEATURE-001` | `05-features/example/tasks.md` (T-001 to T-003). |
| 6 | `/dixi.build T-001` … `T-003` | `tests/*.test.mjs` red first; then `lib/`, `locales/` and the Next.js skeleton until green. |
| 7 | `/dixi.verify` | `make verify`: `dixi check` and 18 `node --test` tests green. |
| 8 | `dixi upgrade --dry-run` (kit 1.4.0) | Empty plan: every managed file is unchanged for this kit version. |

## Managed files edited by hand

`init` records a SHA-256 for each file it writes in `.dixi/project.json`. As in `examples/notes`, those hashes stay as generated: `upgrade --dry-run` compares them with the files a newer kit ships, so local edits are reported as conflicts instead of being overwritten. The edited managed files are `README.md`, `00-master-spec.md`, the GOAL, DOMAIN, MODULE, FEATURE, CONTRACT and TEST-001 documents, `Makefile` (adds `node --test`), `.gitignore` (adds `node_modules/`, `.next/` and `next-env.d.ts`), `00-governance/policies/i18n-policy.md` and `09-architecture/adr/README.md`. The other profile templates keep their `{{pending: …}}` blanks; `dixi placeholders` lists them.

## Repeat it

```sh
cd examples/i18n-site
make verify                 # dixi check + node --test, if node is installed
npm test                    # only the node tests
```

Requires `dixi` installed; the application tests need Node.js 20.10 or later and no packages. To run the illustrative Next.js skeleton, install `next`, `react` and `react-dom` yourself; they are not part of the example.

## Related

- [Project](../00-master-spec.md)
- [Test plan](../11-quality/test-plan.md)
