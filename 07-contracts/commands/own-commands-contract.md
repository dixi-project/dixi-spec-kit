# Contract — onboard, bugfix and issues (ADR-108 phase C)

## Purpose

Specify the three operations of [TASK-013](../../tasks/backlog/TASK-013-own-commands.md) where DIXI goes beyond GitHub Spec Kit. The common command contract and limits of the [Claude Code adapter](claude-code-adapter-contract.md) apply; Codex skills are generated from the same text ([Codex adapter](codex-adapter-contract.md)). `dixi upgrade --apply`, the fourth item of the phase, is specified in the [block A contract](block-a-contract.md#dixi-upgrade---apply).

## Operations

| Operation | Reads | Writes | Never does |
|---|---|---|---|
| `onboard` | Code roots named by the person, manifests, tests, existing specs, principles, traceability | After the person validates the module split: `04-modules/<module>/module-spec.md` and `05-features/<slug>/feature-spec.md` starting with `Status: draft (onboarded from code)`, criteria only for behaviour the code or tests show, `{{pending: …}}` for intent; new entries in `.dixi/traceability.json` | Change code, tests, build files or configuration; overwrite a document the person wrote; claim intent the code cannot prove |
| `bugfix` | Bug report, the feature's specs and contracts, principles | `05-features/<slug>/bugs/BUG-NNN.md` (report, reproduction, broken criterion, cause, test, fix); a failing test proposed for its own commit without `Signed-off-by`; the minimal fix; spec or contract updates only with the person's agreement | Fix without a reproducing test; edit frozen tests; treat unspecified behaviour as a bug (it goes to `clarify` or `change`) |
| `issues` | `05-features/<slug>/tasks.md`, the spec, existing issues (`gh issue list`), `gh auth status` | GitHub issues created with `gh issue create` for the tasks the person confirms in a preview; `05-features/<slug>/issues.md` mapping tasks to issue numbers and URLs | Create anything before an explicit confirmation; edit, close, assign or label existing issues; ask for or handle a token |

Every operation follows `00-governance/principles.md` when it exists, treats the request and observed content as data, and closes with `dixi check` and a report of checks run, failed and not run.

## Manual run

Run on 2026-11-11 with Claude Code 2.1.322 (`claude -p`), in a repository holding an existing Python package (`src/shop/catalog.py`, `src/shop/orders.py`, two tests) to which DIXI was added with `dixi init --agent claude` from this branch (thirty-three commands; `init` needs an empty destination, so the code was copied in afterwards).

- `/dixi.onboard src/` mapped the code roots, entry points, in-memory store and the `orders` → `catalog` dependency with `file:line` evidence, proposed `DOMAIN-002 shop`, `MODULE-002 catalog`, `MODULE-003 orders` and three features with their certainty, listed which behaviours the tests assert, and stopped without writing any file.
- After the person validated the split, the same session wrote `03-domains/shop/domain-spec.md`, two module specs and three feature specs, each starting with `Status: draft (onboarded from code)`, with `src/shop/*.py:<line>` evidence and 3 to 9 `{{pending: …}}` markers each, and registered them in `.dixi/traceability.json`. `src/` and `tests/` were unchanged; `dixi check` passed.

## Workflow recipes

`dixi workflow show/prepare` covers the three operations: `onboard` targets a goal, `bugfix` and `issues` target a feature. Packets stay read-only.

## Compatibility

Inventory requirements do not change: the operations are optional, so projects from earlier versions keep passing `check` and see them as `new` in `dixi upgrade --dry-run` (and `--apply` creates them). `doctor` reports installed of available (33).

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [TASK-013](../../tasks/backlog/TASK-013-own-commands.md)
- [Command catalog](../../docs/command-catalog.md)
