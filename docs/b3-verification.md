# B3 and v1.0.0 evidence

## Purpose

Record the technical verification of the Claude Code adapter (TASK-003) and of version 1.0.0, and their limits. Date: 2026-11-08. Environment: macOS, Python 3.15.2, Claude Code 2.1.319, Setuptools 84.2.1 pinned by hash.

## Tests first

| Block | Red commit | Prior result |
|---|---|---|
| Claude Code adapter | `[11-quality] test: acceptance in red for Claude Code adapter B3` | 18 expected failures; the `--agent none` regression passes |
| Public exporter | `[11-quality] test: acceptance in red for public release export` | 3 expected failures |
| 1.x compatibility | `[11-quality] test: accept same-major kit versions in red` | 8 expected failures |

Two frozen tests were changed with explicit authorization from the responsible person, each in its own commit: the quoting of the interpreter in the example's shim (paths with spaces) and the expected version (`1.0.0.dev0` → `1.0.0`).

## Results

- `make verify` in the repository: syntax, es/en parity of catalogs and resources, license and **93 tests** green, including clean installation from the wheel and from the rebuilt sdist.
- Exported public tree (`scripts/export-release.py`, 145 files): `make verify` green with 89 tests (the exporter and its test are not distributed). Installation from source in a new environment, followed by `dixi --version` → `dixi 1.0.0`, `init --agent claude`, `doctor` and `check` with exit code 0.
- `examples/notes`: `dixi check` and 12 application tests green.
- Gitleaks 8.30.1: no findings in the public tree or in the 64 commits of the local history.
- Relative links in the public tree's Markdown files: no broken links.
- Name `dixi-spec-kit` free on PyPI on 2026-11-08 (HTTP 404). Another project called `dixi` exists on PyPI; there is no package conflict, but the `dixi` executable could clash if someone installs both.

| Artifact | Bytes | SHA-256 |
|---|---|---|
| `dixi_spec_kit-1.0.0-py3-none-any.whl` | 53 422 | `51e5a3424c6e1067b6bf2ba27e28d26228438390e46a44ae487c7a6c4f233a5e` |
| `dixi_spec_kit-1.0.0.tar.gz` | 33 545 | `ad736aa7096f977cf77af465e85afc757b790ca331dd5813455088be8ad35acf` |

The hashes identify this local build; bit-for-bit reproduction is not promised. The release must attach the artifacts built by the person from the published commit.

## Walkthrough in the agent

The example was produced by following the steps of each command in a Claude Code 2.1.319 session, including the evolution with impact analysis and red tests before code ([walkthrough](../examples/notes/docs/walkthrough.md)). It is **not** an independent evaluation: a person still needs to invoke the ten installed `/dixi.*` commands in a new session and confirm that they behave according to the [contract](../07-contracts/commands/claude-code-adapter-contract.md).

## Publication

- New public repository `dixi-project/dixi-spec-kit`, with only `main` (`f317065`, signed by the person). CI green on `ubuntu-latest` and `macos-latest` with Python 3.11 and 3.13.
- `main-protegida` ruleset active and private vulnerability reporting enabled.
- Release v1.0.0 with artifacts built from `f317065` (89 tests green): wheel `46947a0fd4c2175fda70b8adae65ae86af67c4ea160349ae103bcce72d3ca6ff`, sdist `46c6a217190968cb4feddc53e8ba6928b3cc67a83790839dd885bd019e37eec2`.
- External installation verified in clean environments: `pip install git+…@v1.0.0`, `uv tool install git+…@v1.0.0` and the wheel downloaded from the release (with `init --agent claude`, `check` and `make verify` of the generated project).

## Pending

- Manual evaluation of the commands in a new Claude Code session.

## Related

- [Support matrix](support-matrix.md)
- [Publication gate](publication-readiness.md)
- [TASK-003](../tasks/backlog/TASK-003-adaptador-claude-code.md)
