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

## Compatibility

Inventory requirements do not change: the three operations are optional, so projects from earlier versions keep passing `check` and see them as `new` in `dixi upgrade --dry-run`. `doctor` reports installed of available (30).

## Related

- [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md)
- [TASK-011](../../tasks/backlog/TASK-011-parity-commands.md)
- [Coming from Spec Kit](../../docs/coming-from-spec-kit.md)
