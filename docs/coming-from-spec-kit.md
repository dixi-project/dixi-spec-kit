# Coming from Spec Kit

## Purpose

Get a person who knows GitHub Spec Kit productive in DIXI Spec Kit: the same steps under DIXI's names, where each document lives, and what changes in day-to-day work. Facts about Spec Kit refer to v1.4.0, read on 2026-11-11 ([comparison](spec-kit-comparison.md)).

## Install and start

```sh
uv tool install dixi-spec-kit          # or: pipx install dixi-spec-kit
dixi init my-project --agent claude    # or --agent codex, or --agent none
cd my-project
dixi doctor && dixi check
```

Add `--profile site|app|platform` for fuller templates and `--controls` to have the agent's hooks enforce the rules.

## Command map

| Spec Kit | DIXI | What changes |
|---|---|---|
| `/speckit.constitution` | `/dixi.constitution` | Writes `00-governance/principles.md` with a version and change log; removing or redefining a principle needs an ADR. |
| `/speckit.specify` | `/dixi.discover` then `/dixi.specify` | `discover` frames the goal; `specify` writes the feature under a module and domain. |
| `/speckit.clarify` | `/dixi.clarify` | Answers stay in the spec; earlier answers are preserved. |
| `/speckit.plan` | `/dixi.plan` | Pulls in `/dixi.domain`, `/dixi.architecture`, `/dixi.contract` and `/dixi.threat-model` when risk requires. |
| `/speckit.checklist` | `/dixi.checklist` | `05-features/<slug>/checklists/<domain>.md`; `/dixi.build` stops while items are open. |
| `/speckit.tasks` | `/dixi.tasks` | `05-features/<slug>/tasks.md` with `T-NNN`, risk levels and links to criteria. |
| `/speckit.analyze` | `/dixi.analyze` | Plus `dixi check` for the mechanical rules. |
| `/speckit.implement` | `/dixi.build` | One task at a time: failing tests first, committed, then code; `make verify` must be green. |
| `/speckit.github.taskstoissues` | `/dixi.issues` | Creates issues with `gh` after you confirm a preview; records them in `05-features/<slug>/issues.md`. |
| `/speckit.converge` | `/dixi.converge` | Appends `## Convergence` tasks typed `missing`, `partial`, `contradicts` or `unrequested`. |
| — | `/dixi.verify`, `/dixi.review` | Report checks run, failed and not run; prepare a human review. DIXI never approves or merges. |
| — | `/dixi.status`, `/dixi.handoff` | Next step and a resumable handoff between sessions. |

## Where things live

| Spec Kit | DIXI |
|---|---|
| `.specify/memory/constitution.md` | `00-governance/principles.md` |
| `specs/NNN-name/spec.md` | `05-features/<slug>/feature-spec.md`, under `04-modules/<module>/` and `03-domains/<domain>/` |
| `specs/NNN-name/plan.md`, `research.md` | Plan next to the feature; decisions as ADRs in `09-architecture/adr/` |
| `specs/NNN-name/data-model.md` | `08-data/` (with `/dixi.data`) |
| `specs/NNN-name/contracts/` | `07-contracts/` |
| `specs/NNN-name/tasks.md` | `05-features/<slug>/tasks.md` |
| `specs/NNN-name/checklists/` | `05-features/<slug>/checklists/` |
| — | `.dixi/traceability.json`: the goal → domain → module → feature → contract → test chain that `dixi check` verifies |

## Moving an existing Spec Kit project

1. In a new branch of the repository, run `dixi init . --existing`: it adds DIXI next to the existing files, never overwrites any of them and lists the ones it kept (for example your own `README.md`).
2. Copy the constitution's principles into `00-governance/principles.md` with `/dixi.constitution`, keeping their meaning and giving them IDs.
3. For each `specs/NNN-name/`, run `/dixi.specify` with the existing spec as input and place the feature under its module; move contracts and data models to `07-contracts/` and `08-data/`.
4. Run `dixi check` and `/dixi.analyze`, then `/dixi.converge` per feature to see what the code already covers.

Nothing is converted automatically: a person reviews each step. `/dixi.onboard` drafts modules and features from an existing codebase for you to validate, as a starting point for those steps.

## Related

- [Comparison](spec-kit-comparison.md)
- [Workflow quickstart](workflow-quickstart.md)
- [Support matrix](support-matrix.md)
