# Contract — constitution, checklist and converge (ADR-108 phase A)

## Purpose

Specify the three operations of [TASK-011](../../tasks/backlog/TASK-011-parity-commands.md) that close the gap with GitHub Spec Kit. The common command contract and limits of the [Claude Code adapter](claude-code-adapter-contract.md) apply; Codex skills are derived from the same text ([Codex adapter](codex-adapter-contract.md)).

## Operations

| Operation | Reads | Writes | Never does |
|---|---|---|---|
| `constitution` | `00-governance/principles.md`, `00-master-spec.md`, `01-business/vision.md`, ADRs citing a principle | `00-governance/principles.md` with `Version: X.Y.Z`, last-amended date and change log; a proposed ADR when a principle is removed or redefined | Edit code, specs, tasks or tests; reuse a retired principle ID; invent principles |
| `checklist` | Feature spec, plan, contracts, test plan, parent module and domain, principles | `05-features/<slug>/checklists/<domain>.md` with unchecked `CHK-NNN` items, each classified and traced to a spec section or principle, or marked as a gap | Tick, untick, reword or delete items; answer the questions; change the spec |
| `converge` | Feature spec and criteria, contracts, plan, `tasks.md`, tests, principles, code in the authorized roots, real `make verify` result | A dated `## Convergence` section appended to `05-features/<slug>/tasks.md`: one `T-NNN` task per gap with type (`missing`, `partial`, `contradicts`, `unrequested`), source, evidence, first test and risk | Edit specs, contracts, code, existing tasks or tests; claim a check ran when it did not |

Versioning of the constitution: MAJOR for a removed or incompatibly redefined principle, MINOR for an added or materially extended one, PATCH for wording that keeps the meaning.

## Effects on other operations

- Every operation, in both languages and both adapters, follows `00-governance/principles.md` when it exists and reports conflicts instead of resolving them silently.
- `build` lists open items (`- [ ]`) of the feature's checklists and stops until the person closes them or decides to continue.
- When `converge` finds no gap, `tasks.md` stays byte for byte unchanged and the answer says the feature has converged, with evidence.

## Workflow recipes

`dixi workflow show/prepare` covers the three operations: `constitution` targets a goal (`GOAL-001`), `checklist` and `converge` target a feature. Packets stay read-only, as for the other recipes.

## Manual run

Run on 2026-11-11 with Claude Code 2.1.322 (`claude -p`, project commands loaded), in a project created with `dixi init parity-demo --agent claude` from the wheel built on this branch (thirty commands installed). Each step was committed in the sample project to record what it wrote.

- `/dixi.constitution add a principle: every user-facing text is available in English and Spanish` created `00-governance/principles.md` with `Version: 0.1.0`, `Last amended: 2026-11-11`, principle `P-01`, `{{pending: …}}` for the undecided architecture and engineering principles and precedence, the change rules and a change log; it listed the affected documents without editing them and suggested `/dixi.analyze`. No other file changed.
- `/dixi.checklist example i18n` wrote `05-features/example/checklists/i18n.md`: 22 unchecked `CHK-001`…`CHK-022` items (0 ticked), classified, traced to the spec and to `P-01`, gaps marked and each pointed to the operation that closes it. No spec changed.
- `/dixi.converge example` on the draft feature (no criteria, plan, tasks or code) stopped without writing and said that "not evaluable" is not "converged".
- After adding three acceptance criteria, a plan with `src/` as authorized root, a `tasks.md` with `T-001` and code meeting only AC-1, `/dixi.converge example` appended `## Convergence 2026-11-11` with `T-002` (`missing`, AC-2 and `P-01`, highest severity), `T-003` (`missing`, AC-3) and `T-004` (`unrequested`, English returned for any language), each with source, file-and-line evidence, the test to write first and a risk level. Only `tasks.md` changed.
- `/dixi.build T-002`, without edit permissions, stopped at step 1 listing the 22 open checklist items; it wrote nothing.

## Compatibility

Inventory requirements do not change: the three operations are optional, so projects from earlier versions keep passing `check` and see them as `new` in `dixi upgrade --dry-run`. `doctor` reports installed of available (30).

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [TASK-011](../../tasks/backlog/TASK-011-parity-commands.md)
- [Coming from Spec Kit](../../docs/coming-from-spec-kit.md)
