# DIXI Spec Kit

**English** · [Español](README.es.md)

## Purpose

DIXI Spec Kit is a [Dixi Project](https://github.com/dixi-project) tool for specification-driven development (SDD) with traceability and verification: from an idea to linked specs, tests first, verified code and human review. It ships a CLI (`dixi`) and commands for Claude Code.

- **Explicit traceability:** goal → domain → module → feature → contract → test, with IDs checked by `dixi check`.
- **Tests first, then frozen:** commands instruct writing failing tests before code and never editing them to make code pass.
- **Human control:** the agent does not sign, approve, merge or deploy.
- **No dependencies, no network:** the CLI uses only the Python standard library, consumes no AI and asks for no credentials. You choose your project's language.

## Installation

Requirements: Python 3.11 or later, macOS or Linux. Windows is not supported.

```sh
uv tool install git+https://github.com/dixi-project/dixi-spec-kit@v1.3.0
# or
pipx install git+https://github.com/dixi-project/dixi-spec-kit@v1.3.0
```

The package is not on PyPI yet. You can also download the wheel from the [v1.3.0 release](https://github.com/dixi-project/dixi-spec-kit/releases/tag/v1.3.0) and install it with `pipx install dixi_spec_kit-1.3.0-py3-none-any.whl`.

## Quickstart

```sh
dixi init my-project --agent claude   # or --agent none to use it without an agent
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

`/dixi.analyze` checks consistency and the impact of a change; `/dixi.status` suggests the next step. Design with `/dixi.domain`, `/dixi.architecture`, `/dixi.contract` and `/dixi.threat-model`; propose changes with `/dixi.change`; leave a resumable handoff with `/dixi.handoff`. Specialized operations: `/dixi.data`, `/dixi.quality`, `/dixi.ai`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance` and `/dixi.duediligence` write documents only; they never run migrations, deploy, change `MODE` or claim certifications. Documents and messages are in English by default; use `dixi --lang es init …` for Spanish. Inside a project, messages follow the project's language.

## Profiles

`dixi init` installs a minimal documentary baseline by default. Choose a profile to also get standards, guides and blanks for governance, business, data, architecture, engineering, quality, security, observability, delivery, operations, product, UX, AI, FinOps, research, growth and customer success:

| Profile | For | Adds |
|---|---|---|
| `minimal` (default) | Trying the method or adding documents by hand | Nothing: the 16-file baseline |
| `site` | Landing page or content site without its own backend | 77 templates |
| `app` | A few deployable parts: web, admin, API, one database | 190 templates |
| `platform` | Several services, events, apps or teams | 241 templates |
| `--regulated` | Payments, health, sensitive data or enterprise customers | Compliance (GDPR, SOC 2, ISO 27001, HIPAA, PCI DSS), due diligence and stricter security templates on top of `site`, `app` or `platform` (94, 226 or 273 in total) |

```sh
dixi init my-app --agent claude --profile app
```

Templates are guidance with `{{pending: …}}` blanks, not decisions: delete the ones that do not apply (`dixi check` does not require them). The exact list per profile is in the [profiles contract](07-contracts/commands/profiles-contract.md). `dixi upgrade --dry-run --profile <name>` shows what another profile would add.

## Terminal commands

| Command | What it does |
|---|---|
| `dixi init <dir> [--agent none\|claude\|codex] [--profile …] [--regulated]` | Creates the documentary baseline, plus the profile's templates, in a new or empty directory (`.` for the current one); never overwrites. |
| `dixi doctor` | Diagnoses environment and project without network or credentials. |
| `dixi check` | Checks structure, links and traceability. Runs no code. |
| `dixi workflow list\|show\|prepare` | Lists and prepares the discover, specify, clarify, domain, architecture, contract, threat-model and plan procedures. |
| `dixi upgrade --dry-run [--profile …]` | Previews what the installed kit version would change: unchanged, updatable, conflicting, new, missing and obsolete files. Writes nothing. |
| `dixi --help`, `dixi --version` | Help and version. Global options: `--lang es\|en`, `--json`. |

Exit codes: 0 success, 1 invalid content, 2 usage error or missing project, 3 occupied or unsafe destination, 4 unsupported version or platform, 5 I/O failure.

## Example

[`examples/notes`](examples/notes) is a notes library and CLI built with this flow, including an evolution with its impact analysis. `make verify` runs `dixi check` and 12 real tests.

## What is and is not included

See the [support matrix](docs/support-matrix.md). In short: the Claude Code adapter installs commands and instructions, **not hooks or permissions**; rules are instructions for the agent, and effective protection comes from your review and branch protection. The Codex adapter (`--agent codex`, skills invoked as `$dixi-specify`, `$dixi-plan`, …) installs the same operations as Agent Skills, with implicit invocation disabled. Applying upgrades automatically is not available yet ([roadmap](ROADMAP.md)). Windows is not supported.

## Contributing

Anyone can use, clone and fork. Propose changes with a pull request from your fork; only maintainers merge into `main`, after review and green checks. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [code of conduct](CODE_OF_CONDUCT.md); for help, see [SUPPORT.md](SUPPORT.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © 2026 Dixi Project. Projects you generate with `dixi init` are yours.
