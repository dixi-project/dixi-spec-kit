# DIXI Spec Kit

[Español](README.md) · **English**

## Purpose

DIXI Spec Kit is a [Dixi Project](https://github.com/dixi-project) tool for specification-driven development (SDD) with traceability and verification: from an idea to linked specs, tests first, verified code and human review. It ships a CLI (`dixi`) and commands for Claude Code.

- **Explicit traceability:** goal → domain → module → feature → contract → test, with IDs checked by `dixi check`.
- **Tests first, then frozen:** commands instruct writing failing tests before code and never editing them to make code pass.
- **Human control:** the agent does not sign, approve, merge or deploy.
- **No dependencies, no network:** the CLI uses only the Python standard library, consumes no AI and asks for no credentials. You choose your project's language.

## Installation

Requirements: Python 3.11 or later, macOS or Linux. Windows is not supported in v1.0.0.

```sh
uv tool install git+https://github.com/dixi-project/dixi-spec-kit@v1.0.0
# or
pipx install git+https://github.com/dixi-project/dixi-spec-kit@v1.0.0
```

The package is not on PyPI yet. You can also download the wheel from the [v1.0.0 release](https://github.com/dixi-project/dixi-spec-kit/releases/tag/v1.0.0) and install it with `pipx install dixi_spec_kit-1.0.0-py3-none-any.whl`.

## Quickstart

```sh
dixi --lang en init my-project --agent claude   # or --agent none to use it without an agent
cd my-project
dixi doctor
dixi check
make verify
```

Open Claude Code in `my-project` and walk through:

```text
/dixi.discover <your idea>
/dixi.specify <feature>
/dixi.clarify <spec ID>
/dixi.plan <FEATURE-ID>
/dixi.tasks <FEATURE-ID>
/dixi.build <T-ID>
/dixi.verify
/dixi.review main
```

`/dixi.analyze` checks consistency and the impact of a change; `/dixi.status` suggests the next step. Without `--lang en`, documents and messages are in Spanish.

## Terminal commands

| Command | What it does |
|---|---|
| `dixi init <dir> [--agent none\|claude]` | Creates the documentary baseline in a new or empty directory; never overwrites. |
| `dixi doctor` | Diagnoses environment and project without network or credentials. |
| `dixi check` | Checks structure, links and traceability. Runs no code. |
| `dixi workflow list\|show\|prepare` | Lists and prepares the discover, specify, clarify, domain, architecture, contract, threat-model and plan procedures. |
| `dixi --help`, `dixi --version` | Help and version. Global options: `--lang es\|en`, `--json`. |

Exit codes: 0 success, 1 invalid content, 2 usage error or missing project, 3 occupied or unsafe destination, 4 unsupported version or platform, 5 I/O failure.

## Example

[`examples/notes`](examples/notes) is a notes library and CLI built with this flow, including an evolution with its impact analysis. `make verify` runs `dixi check` and 12 real tests. The example documents are in Spanish.

## What is and is not included

See the [support matrix](docs/support-matrix.md). In short: the Claude Code adapter installs commands and instructions, **not hooks or permissions**; rules are instructions for the agent, and effective protection comes from your review and branch protection. `dixi upgrade`, Codex, Windows and a second example language are planned for v1.1 ([roadmap](ROADMAP.md)).

## Contributing

Anyone can use, clone and fork. Propose changes with a pull request from your fork; only maintainers merge into `main`, after review and green checks. See [CONTRIBUTING.md](CONTRIBUTING.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © 2026 Dixi Project. Projects you generate with `dixi init` are yours.
