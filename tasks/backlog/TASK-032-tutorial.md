# TASK-032 — A step-by-step tutorial on the documentation site (v1.14.0)

## Purpose

The site documents every operation, every terminal command and what surrounds them, but all of it is reference: it answers "what does this command do?". A person who arrives without knowing DIXI has no page that answers "where do I start and in what order?", and has to reconstruct the path from the command guide, the reference and the README. This task adds a guided tutorial, one step per page, that takes one example feature from installing the kit to a verified build.

## Record

- Type: docs; priority P2; level 2. Created 2026-11-15. Product owner: Alfredo Castillejos.
- Decided by the owner on 2026-11-15: several steps, with a group of their own in the site menu, for v1.14.0.
- Existing material it builds on: the walkthrough in `docs/command-catalog.md`, the command reference in `docs/commands/` and the CLI reference in `docs/cli/`. The tutorial links to them instead of repeating them.
- The site publishes folders under `docs/` declared in `SECTIONS` of `scripts/build-site.py`, each under its own menu group, from `.md` (English) and `.es.md` (Spanish) pages.
- Out of scope: new CLI features, a video or screenshots, and tutorials for operations beyond the main path (domain, contracts, release and the rest stay in the reference).

## Story

As a person trying DIXI for the first time
I want a tutorial that walks me through one feature from installation to a verified build
so that I learn the order of the steps by doing them, without reading the whole reference first.

## Acceptance criteria

1. `docs/tutorial/` holds an introduction and one page per step, in order: install, create the project, specify, plan, tasks, build, verify. Every page exists in English (`.md`) and Spanish (`.es.md`) with the same links, the same commands and the same number of table rows.
2. The site shows the tutorial as a group of its own in the menu, before the command reference, in both languages, with the steps in order.
3. Each step says what you do, what you should see and what comes next, and links to the next step and to the reference page of every command it uses.
4. Every `dixi` terminal command and every `/dixi.<operation>` named in the tutorial exists: a test fails when one has no page in `docs/cli/` or `docs/commands/`.
5. The terminal commands in the tutorial's code blocks run: a test runs them in order in an empty folder and fails when one exits with an error.
6. The documentation index (`docs/documentation.md` and its Spanish version) and both READMEs link the tutorial.
7. The tutorial describes as available only what the support matrix lists as supported, and shows how to follow it with `--agent claude`, `--agent codex`, `--agent skills` or `--agent none`.

## Done when

1. Tests were committed red before the pages.
2. `make verify` passes and CI is green.
3. The owner followed the tutorial on the published site, in at least one language, and found each step from the menu.

## Related

- [Tasks](../TASKS.md)
- [Roadmap](../../ROADMAP.md)
- [TASK-030](TASK-030-complete-documentation.md)
- [Command guide](../../docs/command-catalog.md)
