# Local development and testing

## Purpose

Build, install and test DIXI Spec Kit from this repository. The CLI needs no agent or provider; Python is its runtime, not a choice of the project's language. MIT license; released versions are on [PyPI](https://pypi.org/project/dixi-spec-kit/) ([publishing](pypi-publishing.md)).

## Requirements and build

Tested environment: macOS, Python 3.15.2, pip and Make. The package declares Python >=3.11; the other versions have not been tested yet. POSIX operations with directory descriptors and `O_NOFOLLOW` are required. Native Windows is not supported; use WSL 2 ([below](#windows-wsl-2)). The first installation of Setuptools requires network access; the build and the installations of the local artifacts work without querying an index.

From the repository root:

```sh
python3 -m venv .venv
.venv/bin/python -m pip --isolated install --index-url https://pypi.org/simple --only-binary=:all: --no-deps --require-hashes -r requirements-build.txt
make verify
```

`make verify` builds wheel and sdist, checks syntax/catalogs and runs all tests. The distribution tests rebuild the wheel from sdist and install both in clean temporary environments with `--no-index --no-deps`; then they test the commands and the generated Makefile. `make package` only builds the artifacts. `make test` runs only the cases in `test_local_core.py`; it does not replace the full verification.

## Windows (WSL 2)

Native Windows exits with code 4. Use WSL 2 with an Ubuntu LTS distribution and keep the project on the Linux filesystem:

```powershell
wsl --install -d Ubuntu-24.04
```

Inside Ubuntu:

```sh
sudo apt update && sudo apt install -y python3-venv make git
cd ~                         # not /mnt/c/...
git clone https://github.com/dixi-project/dixi-spec-kit.git && cd dixi-spec-kit
```

Then follow the build steps above. Projects under `/mnt/c` (or any mounted Windows drive) are not supported: Windows processes can create junctions there, and its translation layer does not have the ext4 link semantics `dixi` relies on. Evidence: the `wsl.yml` CI job ([contract](../07-contracts/commands/local-core-contract.md#windows-through-wsl-2)).

Setuptools 84.2.1 is the only external build dependency; it is pinned by hash in `requirements-build.txt`. Provenance and verification are in the [B1 contract](../07-contracts/commands/local-core-contract.md). The runtime uses the standard library.

## Install and test

```sh
.venv/bin/python -m pip --isolated install --no-index --no-deps --force-reinstall dist/dixi_spec_kit-*-py3-none-any.whl
source .venv/bin/activate
dixi --version
dixi --help
mkdir -p .context
dixi init .context/demo-sdd --agent none
cd .context/demo-sdd
dixi doctor
dixi --json check
make verify
```

The destination must be absent or empty and its parent must exist. If you have already used `demo-sdd`, choose another name: `init` refuses the repetition and keeps the files. A write failure may leave partial files and `.dixi-init.lock`; inspect the directory, keep what is useful and use a new destination. There is no automatic recovery or deletion on retry.

For documents in English, use `dixi --lang en init .context/demo-en --agent none` from the root. Global options (`--lang`, `--json`) precede the subcommand. `doctor` also works outside a project; `check` requires being at its root. Without installing, you can view the help with `PYTHONPATH=src python3 -m dixi_spec_kit --help` from this repository.

## Interpreting results

| Code | Meaning |
|---|---|
| 0 | Operation completed within its scope. |
| 1 | Invalid project content, links or paths. |
| 2 | Incorrect usage or missing project. |
| 3 | Occupied/unsafe destination; initialization refused. |
| 4 | Unsupported schema/kit version or platform. |
| 5 | Input/output failure or package resource failure. |

`check` verifies files inventoried and declared in `.dixi/traceability.json`; it does not scan the whole tree. It checks parents/IDs and a subset of inline and reference Markdown links. It has limits of 1 MiB per file and 500 files/items/targets according to the [contract](../07-contracts/commands/local-core-contract.md). It is not a full CommonMark parser, does not visit websites and does not validate anchors, spec completeness or business coverage. The inventory hash preserves the initial content; editing a spec must not fail merely because that hash changes.

The same package already includes `dixi workflow list/show/prepare`: it looks up procedures and prepares context for an explicit target. Follow the [B2a es/en walkthrough](workflow-quickstart.md). The recipes are available without installing an agent; preparing is not the same as executing them.

The documents are drafts. The initial `test` element is a plan, not an executable test. The generated `make verify` calls `dixi check`; each project must connect its own tests before claiming application quality. The instructions in `AGENTS.md` are documentary rules: B1 does not install hooks or automate human review, promotion or deployment. `dixi init --agent claude` additionally installs the ten `/dixi.*` commands for Claude Code; `upgrade` and Codex arrive in v1.1.

## Handoff from an isolated agent session

The maintainers' handoff between sessions lives in `.context/` of this repository's main checkout. Git ignores that folder, so it is in no branch and in no worktree: an agent session that works in an isolated worktree cannot write there, and what it writes inside its own worktree disappears with it.

Such a session hands off like this:

1. It writes the complete handoff to a file outside the repository, in a folder of its own.
2. Before finishing, it gives the maintainer the exact command to copy it, and says that the file is lost if the session is deleted first:

   ```sh
   cp <folder of the session>/HANDOFF.md .context/HANDOFF.md
   ```

3. The maintainer runs the command from the main checkout. The next session reads `.context/HANDOFF.md` at the start.

The handoff is private working state. It is never committed, and it is not pasted into pull requests, issues or task records.

## Related

- [B1 evidence](b1-verification.md)
- [Contract](../07-contracts/commands/local-core-contract.md)
- [Threat model](../13-security/local-core-threat-model.md)
- [Roadmap](../ROADMAP.md)

## Resumen en español

Propósito: construir y probar el paquete local de desarrollo B1 sin agente. Probado en macOS con Python 3.15.2 y Make; Python >=3.11 es el mínimo declarado, no una matriz de compatibilidad probada. Se requieren descriptores de directorio POSIX y `O_NOFOLLOW`. Windows nativo no está soportado; usa WSL 2 con el proyecto bajo `~` (no en `/mnt/c`).

Ejecuta los comandos de build anteriores desde la raíz del repositorio. Setuptools es una dependencia de build verificada y fijada por hash; la CLI no tiene dependencias de ejecución de terceros. `make verify` construye wheel/sdist, comprueba código y catálogos, ejecuta la suite, reconstruye desde sdist e instala ambos wheels en entornos temporales limpios sin índice. Licencia: MIT.

Tras instalar el wheel local y activar `.venv`, `dixi init <destino> --agent none`, `dixi doctor`, `dixi --json check` y `make verify` crean y comprueban un proyecto documental; usa `--lang es` o `--lang en` (antes del subcomando) para elegir el idioma. El directorio padre debe existir y el destino debe ser nuevo o estar vacío; repetir la inicialización no sobrescribe archivos. Una escritura interrumpida puede dejar archivos parciales y un marcador de bloqueo: inspecciona, conserva lo útil y usa un destino nuevo.

Códigos de salida: 0 éxito, 1 contenido de proyecto inválido, 2 uso/proyecto ausente, 3 conflicto de destino, 4 versión/plataforma no soportada, 5 fallo de E/S o de recursos del paquete. Las comprobaciones inspeccionan solo archivos declarados y referencias del grafo, con una sintaxis limitada de enlaces Markdown, sin ejecutar código de aplicación ni acceder a la red. Las specs y planes de prueba en borrador siguen siendo borradores aunque pasen las comprobaciones. `--agent claude` instala diez comandos `/dixi.*` de Claude Code; upgrade y Codex están previstos para v1.1.
