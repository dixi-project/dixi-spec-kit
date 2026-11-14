# TASK-030 — Guides for what surrounds the commands, and a documentation index (v1.12.0)

## Purpose

Every operation and every terminal command has a reference page since v1.10.0, but what surrounds them does not: the subagents are one sentence in the README, the automatic controls and the format of extensions and presets are described only in internal contracts, and no page says where to start. A person feels that documentation is missing even where it exists, because nothing lists it.

## Record

- Type: docs; priority P1; level 2. Created 2026-11-13. Product owner: Alfredo Castillejos.
- Audit of 2026-11-13: 33 operations with a page in `docs/commands/` and 10 terminal commands with a page in `docs/cli/`, both in English and Spanish. Without a user guide: the four subagents in `resources/claude/*/agents/`, the five hooks in `resources/hooks/`, extensions and presets (format only in `07-contracts/commands/extensions-contract.md` and `presets-contract.md`). `docs/workflow-quickstart.md` exists in English only. The README links the references in one sentence inside a long paragraph.
- Out of scope: the commands of the private EIS-IA ecosystem, which are not part of this repository.

## Story

As a person adopting DIXI
I want one place that lists all the documentation, and a guide for each thing the kit installs
so that I do not have to read the packaged files or the internal contracts to use it.

## Acceptance criteria

1. Documentation index: `docs/documentation.md` (first written here as `docs/index.md`; renamed during the work because `index` is the home page of the site), with a Spanish version, lists every user document by what the person wants to do (start, choose a command, look up a command or an option, extend the kit, migrate, contribute). Both READMEs link it in a section of its own near the top, and the documentation site shows it.
2. Subagents: a page that says what each of the four subagents is for, what it may and may not do, and how to invoke it, generated from the packaged agent files so that it cannot drift; a test fails when a subagent has no entry or the page is out of date.
3. Automatic controls: a guide to `--controls` that says, for each of the five hooks, what it blocks, when it runs, for which agents, and how to see that it is active; with what the controls do not cover. A test fails when a packaged hook is not in the guide.
4. Extensions and presets: a guide to writing one from an empty folder (the files, the fields of the manifest, the limits) with a minimal example that a test installs with `dixi extension add` and `dixi preset add`.
5. Recipes: a Spanish version of `docs/workflow-quickstart.md`.
6. Every new page exists in English and Spanish and is published on the site in both trees; the test that lists the pages with a Spanish version is extended by adding to it, not by loosening it.
7. No page describes as available something that the support matrix does not list as supported.

## Done when

1. Tests were committed red before the implementation.
2. `make verify` passes and CI is green.
3. The owner opened the index and found each of the five things above from it.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
- [TASK-016](TASK-016-command-reference.md)
- [TASK-020](TASK-020-spanish-site.md)
