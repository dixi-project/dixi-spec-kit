# B1 contract — Installable local core

## Purpose

Make concrete the first authorized block of TASK-001: help, version, `init --agent none`, `doctor` and `check`. It is a local `1.0.0.dev0` development build, not a public release. `upgrade` and adapters will be implemented in their own blocks.

## Interface

`dixi [--lang es|en] [--json] <command>`; default language `es`. JSON uses stable English keys: `status`, `code`, `messages` (each message has `key`, `message` and parameters), with the codes of the general contract. `--help` and `--version` work without a project. Global options are written before the subcommand.

- `init <directory> [--agent none]`: missing or empty destination, existing parent, no `..` or symlinks in the explicit path. Only `none` is distributed in B1. It does not run hooks, Git, Make or external tools. A failure leaves an identified partial state, without cleaning up unrelated files; nothing is overwritten on retry. Since v1.3.0, `.` (or `./`) means the current directory, resolved to its absolute path, with the same rules: it must be empty. An empty argument is rejected. An unsafe destination reports `unsafe_destination` (code 3), which tells the person how to choose a valid one.
- `doctor`: local diagnosis of the runtime, package resources and filesystem capabilities. It does not require an agent in `none` mode, nor credentials, network or a provider. If there is project metadata, it checks its format.
- `check`: from the project root, validates metadata, mandatory resources, local Markdown links and the explicit traceability graph. It does not run the Makefile or project code. Its success only certifies structure, not readiness to build or application quality.

First evaluated environment: macOS/POSIX with Python 3.15.2. Code intended for Python >=3.11; other versions/systems remain uncertified until their matrix is run. The core requires POSIX operations with directory descriptors and `O_NOFOLLOW` to avoid following symlinks; a system without them fails explicitly, without degrading that protection.

### Windows through WSL 2

Native Windows lacks those operations and exits with code 4. Under WSL 2 the code path is Linux, so Windows is supported through WSL 2 with the project on the Linux filesystem (under `~`); projects under `/mnt/c` or other mounted Windows drives are not supported ([ADR-107](../../09-architecture/adr/ADR-107-windows-support.md)).

Recorded run on 2026-11-11 (UTC), CI job `wsl.yml` on commit `062032f` ([run 42939778058](https://github.com/dixi-project/dixi-spec-kit/actions/runs/42939778058)): runner image `windows-2025-vs2026` (Windows Server 2025, 10.0.26100), Ubuntu 24.04.5 LTS in WSL 2 (`uname -r`: `6.18.54.1-microsoft-standard-WSL2`), Python 3.12.3, project in `$HOME/kit` on ext4.

- `make verify`: `Ran 191 tests`, `OK (skipped=2)` (`node` not installed; native-refusal test runs only on native Windows).
- The built wheel reports `dixi 1.5.0`; `dixi init demo --agent claude --controls`, `dixi check` and `dixi upgrade --dry-run` exit 0.
- With a committed `tests/test_ok.py`, `protect_tests.py` blocks an `Edit` and a `sed -i` of it and `guard_attestation.py` blocks `git commit -s`, each with exit 2, fed the same JSON Claude Code sends; the working tree stays unchanged.

The job fails unless the kernel reports WSL2 and the project is on ext4, so WSL 1 or a `/mnt` path cannot pass it.

### Adding DIXI to an existing folder

`dixi init <dir> --existing` (accepted on 2026-11-11, [ADR-108](../../09-architecture/adr/ADR-108-spec-kit-parity-and-beyond.md), [TASK-013](../../tasks/backlog/TASK-013-own-commands.md)) adds the baseline to a folder that already has files. Without the flag, a non-empty destination still exits 3 and the message points to `--existing`; if the folder does not exist yet, `--existing` behaves like a plain `init`.

- A folder that already holds `.dixi/project.json` is refused with exit 3 (`already_initialized`): use `dixi upgrade`.
- `.dixi-init.lock` is created exclusively first; if it exists, exit 3 and nothing is written.
- Each kit file is created with exclusive creation and without following links. A file that already exists with the same content is adopted; with other content, as a symlink, or under a symlinked folder, it is kept untouched and reported as a conflict.
- `.dixi/project.json` is written last and records every kit file with the **kit's** hash, including kept ones, so `dixi check` finds the required inventory and `dixi upgrade` never classifies a kept file as updatable.
- JSON adds `init: {created, adopted, conflicts}` with sorted paths; the human output lists the kept files.

## Generated files and metadata

Original resources of this product, stored in es/en JSON catalogs inside the package. No standard or proprietary template from the origin is copied. They include a README, vision, domain, module, feature, contract and draft test plan, a documentation-only usage guide, MODE, a structural-check Makefile and context/secret exclusions.

`.dixi/project.json`: `schema_version: 1`, `kit_version`, `language`, `agent: none`, `policy: portable`, `managed_files` as a map of relative path → SHA-256 of the originally generated file. It does not include its own hash. This record is untrusted data when read, not a cryptographic proof of provenance. Compatibility (v1.0.0): `check` and `doctor` accept projects whose `kit_version` has the same major version (`1.x.y`, with an optional `.devN` or `rcN` suffix); another major returns 4 and a malformed value, 1. `agent` accepts `none` or `claude`.

`.dixi/traceability.json`: `schema_version: 1`, `items` as a list of objects with `id`, `kind`, `path` and `parents`. Allowed types and parents: `goal` with no parents; `domain → goal`; `module → domain`; `feature → module`; `contract → feature|module`; `test → contract|feature`. Unique IDs; existing parents of the allowed type; relative paths inside the project. No application code is required for a valid structural draft.

The template includes an example documentation chain marked as a draft; a `test` item may be a test plan, never evidence of an executed test. The report always states that the verification was structural and that the application requires its own ladder. Pending fields remain marked in the documents; B1 does not evaluate their completeness or simulate user decisions. Only the items declared in the graph are checked, not their business coverage or the existence of executable tests.

## Boundaries and limits

Absolute paths in metadata, `..`, backslashes, control characters, Unicode surrogates, symlinks and special files are rejected. The components `.env*`, `.aws`, `.ssh`, `.git`, `.context`, `id_rsa`, `id_ed25519` and the extensions `.pem`/`.key` are denied, case-insensitively. This does not detect secrets stored under other names: they must not be registered in the inventory or graph either. Reads are limited to 1 MiB per file, 500 traceability items and 500 managed files; unexpected types and duplicate JSON keys are rejected.

The Markdown check recognizes simple inline links and single-line reference definitions, even if unused. It accepts destinations between `<...>` with spaces and optional titles. A maximum of 500 recognized destinations per document, labels of up to 999 characters and destination expressions of up to 4 096 characters; an excess of destinations returns `invalid_file`. Web links are not visited; local ones are normalized relative to the document and verified without leaving the root. Fragments and queries are not validated. It is a bounded analyzer, not a CommonMark parser: it does not interpret nesting, escapes or HTML, nor does it distinguish code examples from text. Forms outside that subset are not certified by `check`.

The metadata cannot omit mandatory core resources. Legitimate modifications of documents are not rejected merely because their hash changes: that baseline is kept for the future update comparison. A project with an unsupported schema or kit version returns 4; a missing project returns 2; inconsistent content returns 1; an unsafe/occupied destination returns 3; an I/O failure returns 5.

Initialization uses exclusive creation and directory descriptors, with an execution marker. It does not offer a multi-file transaction or isolation against an attacker with equivalent control of the process or system. The check is a read of the observed state; it does not certify transactional consistency under concurrent editing.

## Packaging and provenance

Setuptools 84.2.1, exclusively for build: verified on PyPI, author Python Packaging Authority, origin `pypa/setuptools`, file history since 2006-05-12. Wheel published 2026-10-20; SHA-256 `ca140b45d5325a9478f880e351484f62fef15f336462e449ca0c03c873d589c2`. No external runtime dependencies. The product license is still pending; MIT is not declared and nothing is published.

Wheel and sdist only incorporate code, new resources and the chosen packaging metadata. The verification inspects the inventory, installs in clean temporary environments without an index or dependencies, and tests the CLI, creation and `make verify` of the generated project. No inherited resource, `.context/`, workspace file or private history may ship.

## Related

- [General contract](command-contract.md)
- [B1 feature](../../05-features/local-core/feature-spec.md)
- [Threat model](../../13-security/local-core-threat-model.md)
- [Story](../../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Setuptools on PyPI](https://pypi.org/project/setuptools/84.2.1/)
- [Setuptools data files guide](https://setuptools.pypa.io/en/latest/userguide/datafiles.html)
