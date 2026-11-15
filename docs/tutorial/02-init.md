# 2. Create the project

## Purpose

Create the documentary baseline of the project and install the operations for your agent, then check that everything is in place.

## What you do

In an empty folder, create the project with the adapter of your agent. This tutorial uses Claude Code:

```bash
dixi init notes --agent claude
cd notes
dixi doctor
dixi check
dixi placeholders
```

With another agent, change only the first command:

| Agent | Command |
|---|---|
| Codex CLI | `dixi init notes --agent codex` |
| OpenCode, or another agent that reads Agent Skills | `dixi init notes --agent skills` |
| Any agent or editor, without installed operations | `dixi init notes --agent none` |

[`dixi init`](../cli/init.md) writes only into a new or empty folder and never overwrites a file. [`dixi doctor`](../cli/doctor.md) checks your environment and the installed operations. [`dixi check`](../cli/check.md) checks structure, links and the traceability chain goal → domain → module → feature → contract → test. [`dixi placeholders`](../cli/placeholders.md) lists the `{{pending: …}}` markers that still need a decision.

Then record the baseline in Git, so that every later change can be reviewed:

```bash
git init
git add .
git commit -m "DIXI baseline"
```

## What you should see

- `dixi init` says `Documentary project created: notes`.
- `dixi doctor` reports `Installed commands: 33 of 33` and the project language.
- `dixi check` ends with exit code 0. It checks the documents, not your application.
- `dixi placeholders` lists seven pending markers, one per example document.

The project already contains one example of each link of the chain, with the IDs `GOAL-001`, `DOMAIN-001`, `MODULE-001`, `FEATURE-001`, `CONTRACT-001` and `TEST-001`. Your own feature will hang from `MODULE-001`.

## Next

[3. Specify the feature](03-specify.md).

## Related

- [Tutorial](index.md)
- [CLI reference](../cli/index.md)
- [Support matrix](../support-matrix.md)
