# B1 evidence — DIXI Spec Kit local core

## Purpose

Record the technical result of the first authorized block of TASK-001 and its limits. Date: 2026-11-06. Local version `1.0.0.dev0`; launch target `v1.0.0`. This report does not constitute human PR approval nor enable publication.

## Observed result

`make verify` finished with exit code 0: **43 tests, all passing**, in an 8.434-second suite. Observed environment: macOS 27.2, arm64, Python 3.15.2; build environment `.venv` with Setuptools 84.2.1. Python syntax, es/en catalog/resource parity and whitespace differences with Git were checked.

| Set | Cases | Evidence |
|---|---:|---|
| CLI contract | 33 | Help/version, es/en, no-agent creation, errors, file preservation, metadata, links, graph, symlinks/FIFO, absence of execution and blocked sockets. |
| Distribution | 2 | Wheel/sdist inventory; rebuild from sdist, clean installs without index/dependencies, installed CLI and Makefile of the generated project. |
| Additional security | 7 | Invalid Unicode, uppercase sensitive names, 501 links, incomplete Markdown, valid/broken references and write interruption. |
| Markdown targets | 1 | Empty target, fragment and paths with spaces in inline/reference links. |

The distribution tests use two temporary environments: one installs the original wheel and the other the one rebuilt from sdist. In both, version, `init`, `check`, `doctor` and the generated `make verify` work. The rebuild uses the local build environment; this does not accredit bit-for-bit reproducible builds nor the whole Python matrix.

After updating the guides, the local links of 24 new/modified Markdown documents were checked, along with full preservation of the inherited rules of `AGENTS.md`. The syntax/catalogs/whitespace check was repeated. The wheel was installed in `.venv` with `--no-index --no-deps`; `.venv/bin/dixi --version` confirmed `1.0.0.dev0`.

## Tests before implementation

| Local commit | Change and observed red |
|---|---|
| `e768a2a` | 33 CLI cases initially failed against the stub; includes the two distribution contracts. |
| `d80ee0c` | Adds seven security cases before fixing references, Unicode/sensitive paths and excess links. There were eleven failures counting subcases. |
| `a5143b5` | Adds the empty/spaced targets case; it detected an `IndexError` before it was fixed. |

The three commits contain only new tests, with no signature or `Signed-off-by` from a person. No frozen test was modified to reach green. Implementation and documentation remain in the working tree for review; no push, merge or release was performed by this block. The responsible person must complete the required provenance and review before merging.

Private logs: `.context/b1-red.log`, `.context/b1-safety-red.log`, `.context/b1-links-red.log` and `.context/b1-verify.log`. They are not distributed.

## Artifacts of this run

Historical record of the B1 build of 2026-11-06. The local files in `dist/` were superseded by the B2a increment; see its [current hashes](b2-verification.md).

| File in `dist/` | Bytes | SHA-256 |
|---|---:|---|
| `dixi_spec_kit-1.0.0.dev0-py3-none-any.whl` | 14 663 | `d0c7e932b4d2b200a9c349e88fab1b9d53a011108a3e29d5ea248c47718851ab` |
| `dixi_spec_kit-1.0.0.dev0.tar.gz` | 11 663 | `5170f32706f21fe62ad76bb6ec05fa33d07968315df9aa2bff7cc5ac7d3a0a99` |

The hashes identify this local build; a new build may differ because of timestamps. `scripts/build-local.py` copies an explicit list to a temporary staging area and `MANIFEST.in` restricts the sdist. The artifacts contain new B1 code and resources, packaging metadata and a local-use README; they exclude inherited rules, context, history, working configuration and the repository's tests. The publication license remains pending.

## Scope and pending items

- Only `init --agent none`, `doctor`, `check`, help/version. No agent commands, upgrade or stack profiles implemented.
- Python >=3.11 is a declared requirement; only 3.15.2/macOS was tested. Other versions and Linux have no evidence yet. Windows lacks the support required in B1. The wheel's `py3-none-any` tag does not certify operating systems.
- `check` accredits structure over declared files and graph. It does not accredit complete content, business coverage, executed tests or production readiness. The Markdown parser is limited; details in the contract.
- The inventory records original hashes for a future upgrade; it does not authenticate provenance. There is no multi-file transaction nor snapshot against concurrent editing.
- Tests are not modified from the CLI. The rules for agents are documentary; B1 does not install hooks, CI, human review or provider controls.
- Gitleaks, semgrep, coverage, mutation testing and agent evaluations were not run. The inventory and distribution tests do not replace the content/history scan required before publishing.
- TASK-001 remains open: B2–B5, rights/license, operational mechanisms, support matrix, public documentation, contribution controls and launch remain pending.

## Related

- [Local es/en guide](local-development.md)
- [Feature and acceptance](../05-features/local-core/feature-spec.md)
- [B1 contract](../07-contracts/commands/local-core-contract.md)
- [Threats](../13-security/local-core-threat-model.md)
- [Story](../tasks/backlog/TASK-001-lanzamiento-v1.md)
- [Publication gate](publication-readiness.md)
