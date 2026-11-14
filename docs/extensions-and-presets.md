# Extensions and presets

## Purpose

Show how to write an extension or a preset from an empty folder and install it. An extension adds operations of your own next to the kit's; a preset replaces the text of kit operations or templates with your team's version. Both are local folders that hold only data: DIXI copies text, it never runs anything from them and it uses no network.

## Which one you need

| You want to | Use | It installs |
|---|---|---|
| Add an operation the kit does not have | An extension | A new command named `dixi-<id>-<operation>` |
| Change how a kit operation or template reads | A preset | Your text in place of the kit's, in the same file |

An extension needs a project created with an agent: with `--agent none` there are no command files to add, and `dixi extension add` is refused. A preset is accepted in any project; with `--agent none` there are no operation files to replace, so only its templates can apply.

## Writing an extension

A folder with a manifest and one text per operation and language. The repository has this one in [`examples/extension-minimal`](../examples/extension-minimal):

```text
extension-minimal/
├── extension.json
└── operations/
    ├── en/deploy-check.md
    └── es/deploy-check.md
```

`extension.json`:

```json
{"id": "acme", "version": "1.0.0", "operations": ["deploy-check"]}
```

- `id` names the extension; `operations` lists the files in `operations/<language>/`, without `.md`. Names use lowercase letters, digits and hyphens. `id` cannot be `dixi`.
- Every operation needs its text in English and in Spanish; the project gets the one in its language.
- Each text starts with two lines of front matter, `description` and `argument-hint`, both quoted, like the kit operations. In the body, `$ARGUMENTS` is what the person writes after the command.
- Nothing else may be in the folder: another file, a link or a missing language refuses the whole extension and writes nothing.
- Limits: 1 to 50 operations, 64 KiB per text, and `dixi-<id>-<operation>` of at most 64 characters.

Install it from the project root:

```sh
dixi extension add ../examples/extension-minimal
dixi extension list
```

The operation is now available as `dixi-acme-deploy-check`: `/dixi-acme-deploy-check` in Claude Code, `$dixi-acme-deploy-check` in Codex and the `dixi-acme-deploy-check` skill in an Agent Skills compatible agent. The prefix means that an extension can never take the name of a kit operation. If a file with that name already exists, nothing is written.

To take it out:

```sh
dixi extension remove acme
```

It deletes only the files it installed and that you did not edit; edited ones are kept and listed.

## Writing a preset

A folder with a manifest and the texts it replaces. The repository has this one in [`examples/preset-minimal`](../examples/preset-minimal), which gives the handoff the team's own headings:

```text
preset-minimal/
├── preset.json
└── operations/
    ├── en/handoff.md
    └── es/handoff.md
```

`preset.json`:

```json
{"id": "team", "version": "1.0.0", "priority": 50}
```

- `priority` is a number from 0 to 100. When two presets replace the same file, the higher one wins.
- `operations/<language>/<operation>.md` replaces a kit operation; the name must be one of the kit's operations. `templates/<language>/<path>` replaces a kit template with the same path.
- English and Spanish must replace the same files.
- Limits: 1 to 300 files, 64 KiB per operation text and 256 KiB per template.

Install it from the project root:

```sh
dixi preset add ../examples/preset-minimal
dixi preset list
```

A file is replaced only when all of this is true:

1. It is a kit file installed in this project.
2. You have not edited it: it still has the kit's text, or the text of a preset with lower priority.
3. There is no file for it in `.dixi/overrides/`. That folder holds the project's own versions and always wins over any preset.

Files that do not meet this are kept and listed, so a preset never overwrites your work. `dixi upgrade` does not overwrite a file that a preset replaced either.

To take it out:

```sh
dixi preset remove team
```

It puts the kit's text back in the files that still have the preset's text and keeps the ones you edited afterwards.

## What neither of them does

- They do not run code, add hooks or change `--controls`. A folder that holds anything but the files above is refused.
- They do not change the limits of the operations: write the same limits in your texts that the kit operations carry, because nothing adds them for you.
- They are not published or downloaded by DIXI. Share the folder as you share any other file of your team.

## Related

- [Documentation index](documentation.md)
- [Command reference](commands/index.md)
- [CLI reference: `dixi extension`](cli/extension.md)
- [CLI reference: `dixi preset`](cli/preset.md)
- [Extensions contract](../07-contracts/commands/extensions-contract.md)
- [Presets contract](../07-contracts/commands/presets-contract.md)
