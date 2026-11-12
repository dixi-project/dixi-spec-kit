# DIXI Spec Kit command guide

## Purpose

Show the method as a map: where to start, which command to use at each moment and what comes next. Every command has its own page in the [command reference](commands/index.md); this guide tells you which one to open.

The commands below run inside your agent. They are written here as Claude Code writes them (`/dixi.specify`); in Codex the same operation is `$dixi-specify` and in an Agent Skills compatible agent it is the `dixi-specify` skill. Commands that start with `dixi ` and no slash, like `dixi check`, run in the terminal.

## Journey

One feature travels this path, from an idea to a version a person decides to publish:

```text
discover → specify → clarify → plan → tasks → build → verify → review → release
```

1. **Define.** `/dixi.discover` turns the idea into vision, actors, scope and open questions. `/dixi.specify` writes one feature with criteria that can be checked from outside. `/dixi.clarify` asks you what is still ambiguous and records your answers.
2. **Plan.** `/dixi.plan` writes the technical plan for the feature and `/dixi.tasks` splits it into small, ordered tasks.
3. **Build.** `/dixi.build` implements one task at a time: failing tests first, then the least code that makes them pass, then `make verify`.
4. **Check.** `/dixi.verify` gathers the real evidence for each criterion and `/dixi.review` prepares the review for a person. Neither approves anything.
5. **Publish.** `/dixi.release` prepares the evidence, the changelog and the rollback plan. You decide, tag and publish.

At any point `/dixi.status` tells you where the project stands and names the next step. A small change does not need the whole path: start at the step that matches what you already have.

The other operations sit around that path. Use them when the feature needs them, not by default.

### Design

Before or during the plan, when a feature touches more than one part of the system: `/dixi.domain` delimits a domain and its language, `/dixi.architecture` compares alternatives and writes the decision records, `/dixi.contract` specifies an interface and its consumers, and `/dixi.threat-model` links each threat to a mitigation and a test.

### Quality

`/dixi.checklist` tests the requirements of a feature before you build it. `/dixi.analyze` looks for gaps and contradictions between specs and for the impact of a change, without writing. `/dixi.converge` compares the code with its specs and adds the missing work as tasks. `/dixi.risk-review` prepares a report on the risk of a pull request or branch.

### Continuity

`/dixi.status` and `/dixi.handoff` let a session stop and another one continue. `/dixi.change` turns a requested change into a proposal with its impact before anything is edited. `/dixi.bugfix` takes a bug from report to fix with the failing test committed first. `/dixi.issues` publishes the open tasks of a feature as GitHub issues after you confirm a preview.

### Setup and adoption

`/dixi.constitution` writes the project's principles, which every other operation reads. `/dixi.interview` fills the `{{pending: …}}` blanks of the templates one question at a time. `/dixi.onboard` reads an existing codebase and drafts its domains, modules and features for you to validate.

### Specialized

These write documents only: they never run migrations, deploy, change `MODE` or claim a certification. `/dixi.data` specifies the data model and its migrations, `/dixi.quality` the test strategy, `/dixi.ai` an AI capability and its evaluation, `/dixi.operate` the operation of a service, `/dixi.finops` the costs, `/dixi.compliance` the obligations of a regulation, `/dixi.duediligence` a report for an investor, customer or audit, and `/dixi.promote` checks whether the project is ready to change `MODE` from `mvp` to `prod`.

## Which command when

| Command | Use it when | It leaves |
|---|---|---|
| [`/dixi.discover`](commands/discover.md) | You have an idea or a need and nothing written yet. | Vision, actors, scope and open questions in `01-business/`. |
| [`/dixi.specify`](commands/specify.md) | You know what one feature must do and want it written down. | `05-features/<slug>/feature-spec.md` with a story and numbered criteria. |
| [`/dixi.clarify`](commands/clarify.md) | A spec has doubts, gaps or two possible readings. | Your answers recorded in the spec, apart from the assumptions. |
| [`/dixi.plan`](commands/plan.md) | The feature is clear and you need to decide how to build it. | The technical plan: contracts affected, decisions to take, risks and how to verify. |
| [`/dixi.tasks`](commands/tasks.md) | The plan is agreed and the work must be split. | `05-features/<slug>/tasks.md` with small, ordered tasks linked to their specs. |
| [`/dixi.build`](commands/build.md) | One task is ready to be implemented. | Failing tests, then code that makes them pass, and `make verify` green. |
| [`/dixi.verify`](commands/verify.md) | The tasks are done and you want proof for each criterion. | A report of evidence per criterion; it changes no file. |
| [`/dixi.review`](commands/review.md) | The change is ready for a person to review. | A review prepared by risk against a base branch; it approves nothing. |
| [`/dixi.release`](commands/release.md) | You are about to publish a version. | `docs/releases/<version>.md` with evidence, changelog and rollback plan, for you to decide. |
| [`/dixi.domain`](commands/domain.md) | A goal needs its business language and boundaries fixed before splitting it. | `03-domains/<slug>/domain-spec.md` and its modules, linked to business goals. |
| [`/dixi.architecture`](commands/architecture.md) | A decision has alternatives with different consequences. | Decision records in `09-architecture/adr/`, as drafts for you to accept. |
| [`/dixi.contract`](commands/contract.md) | Two parts, or you and a consumer, must agree on an interface. | `07-contracts/<slug>.md` with inputs, outputs, errors and consumers. |
| [`/dixi.threat-model`](commands/threat-model.md) | The feature handles data, permissions or an exposed surface. | `13-security/<slug>-threat-model.md` with a mitigation and a test per threat. |
| [`/dixi.checklist`](commands/checklist.md) | You want to test the requirements before building on them. | A checklist in `05-features/<slug>/checklists/` that a person ticks. |
| [`/dixi.analyze`](commands/analyze.md) | You suspect gaps or contradictions, or need the impact of a change. | A report of findings; it writes nothing. |
| [`/dixi.converge`](commands/converge.md) | Code and specs may have drifted apart. | One traced task per gap, added to the feature's `tasks.md`. |
| [`/dixi.risk-review`](commands/risk-review.md) | A pull request or branch needs a risk report before a person reviews it. | A risk report by area; it approves nothing. |
| [`/dixi.status`](commands/status.md) | You open the project and do not know what comes next. | A summary and one justified next step; it changes no file. |
| [`/dixi.handoff`](commands/handoff.md) | You stop and someone, or a later session, must continue. | `.context/handoff.md` with the current state. |
| [`/dixi.change`](commands/change.md) | Someone asks to change something that is already specified. | `05-features/<slug>/changes/CHANGE-NNN.md` with the impact, before any edit. |
| [`/dixi.bugfix`](commands/bugfix.md) | Something that worked is broken, or never matched its spec. | A failing test committed first, the fix and `05-features/<slug>/bugs/BUG-NNN.md`. |
| [`/dixi.issues`](commands/issues.md) | The team tracks work in GitHub and the tasks live in the repository. | GitHub issues for the open tasks, created with `gh` after you confirm a preview. |
| [`/dixi.constitution`](commands/constitution.md) | The project needs its principles written, or one of them changes. | `00-governance/principles.md`, versioned. |
| [`/dixi.interview`](commands/interview.md) | The templates still have `{{pending: …}}` blanks. | The blanks filled with your answers, one question at a time. |
| [`/dixi.onboard`](commands/onboard.md) | You add DIXI to a codebase that already exists. | Draft domains, modules and features with `file:line` evidence, for you to validate. |
| [`/dixi.data`](commands/data.md) | A feature stores or moves data, above all personal data. | `08-data/<slug>.md` with model, classification, retention and migration plan. |
| [`/dixi.quality`](commands/quality.md) | You need to decide how a scope is verified. | `11-quality/strategy.md` and a criterion-to-test matrix. |
| [`/dixi.ai`](commands/ai.md) | A feature uses a model or an agent. | `21-ai/<slug>.md` with use case, evaluation, data and costs. |
| [`/dixi.operate`](commands/operate.md) | A service is about to run for real users. | `15-operations/<service>.md` with objectives, observability and runbooks. |
| [`/dixi.finops`](commands/finops.md) | You need a cost estimate with its assumptions. | `22-finops/<slug>.md` with sources and budgets. |
| [`/dixi.compliance`](commands/compliance.md) | A framework or regulation applies to the project. | `23-compliance/<framework>.md` mapping obligations to evidence. |
| [`/dixi.duediligence`](commands/duediligence.md) | An investor, customer or auditor asks for a report. | `28-due-diligence/<type>.md` built from existing artifacts, with its gaps. |
| [`/dixi.promote`](commands/promote.md) | You consider moving the project from `mvp` to `prod`. | `docs/promotion/<date>-prod.md` with the missing evidence, for you to decide. |

## Walkthrough

A small example from an empty folder to a first version: a command-line tool that keeps short notes with tags. The repository has a finished version of it in [`examples/notes`](../examples/notes).

**1. Create the project.** In the terminal:

```sh
uv tool install dixi-spec-kit
dixi init notes --agent claude
cd notes
dixi doctor
dixi check
```

`dixi init` creates the documentary baseline and installs the commands for the agent. `dixi doctor` checks the environment and `dixi check` checks structure, links and traceability.

**2. Define.** Open the agent in `notes` and describe the idea:

```text
/dixi.discover a command-line tool to keep short notes with tags
/dixi.specify add a note with tags
/dixi.clarify FEATURE-001
```

Discovery asks about users, scope and limits and writes what you answer. The specification gives the feature an ID, here `FEATURE-001`, and numbered criteria such as "a note without text is rejected". Clarification asks what the spec leaves open, for example whether tags are case sensitive; answer, and it records the answer.

**3. Plan.**

```text
/dixi.plan FEATURE-001
/dixi.tasks FEATURE-001
```

Read the plan before going on: it is the moment to change the approach cheaply. The tasks get IDs such as `T-001`, each linked to the criteria it covers.

**4. Build, one task at a time.**

```text
/dixi.build T-001
```

The agent writes the tests first and shows them failing, then writes the code. It finishes with `make verify`. You review and commit; the agent does not sign, push or merge. Repeat for `T-002` and the rest.

**5. Check.**

```text
/dixi.verify FEATURE-001
/dixi.review main
```

Verification maps every criterion to the test that covers it and says which ones have no evidence. The review groups the change by risk for the person who reviews it. Open the pull request and let a person approve it.

**6. Publish.**

```text
/dixi.release 0.1.0
```

You get the evidence, a changelog entry and a rollback plan in `docs/releases/0.1.0.md`. Tagging and publishing are yours.

When a later request changes the behavior, start with `/dixi.change`: it shows what the change touches before any spec or code is edited.

## Related

- [Command reference](commands/index.md)
- [Workflow quickstart](workflow-quickstart.md)
- [Support matrix](support-matrix.md)
- [Coming from GitHub Spec Kit](coming-from-spec-kit.md)
- [Working catalog used to design v1 (history)](history/command-catalog.md)
- [README](../README.md)
