# Desarrollo y prueba local / Local development

## Propósito

Construir, instalar y probar DIXI Spec Kit desde este repositorio. La CLI no necesita agente ni proveedor; Python es su runtime, no una elección del lenguaje del proyecto. Licencia MIT; el paquete aún no está en PyPI.

## Requisitos y build

Entorno comprobado: macOS, Python 3.15.2, pip y Make. El paquete declara Python >=3.11; las demás versiones todavía no se han probado. Se requieren operaciones POSIX con descriptores de directorio y `O_NOFOLLOW`. Windows no está soportado en B1. La primera instalación de Setuptools requiere red; el build y las instalaciones de los artefactos locales funcionan sin consultar un índice.

Desde la raíz del repositorio:

```sh
python3 -m venv .venv
.venv/bin/python -m pip --isolated install --index-url https://pypi.org/simple --only-binary=:all: --no-deps --require-hashes -r requirements-build.txt
make verify
```

`make verify` construye wheel y sdist, comprueba sintaxis/catálogos y ejecuta todas las pruebas. Las pruebas de distribución reconstruyen el wheel desde sdist e instalan ambos en entornos temporales limpios con `--no-index --no-deps`; después prueban los comandos y el Makefile generado. `make package` solo construye los artefactos. `make test` ejecuta únicamente los casos de `test_local_core.py`; no sustituye la verificación completa.

Setuptools 84.2.1 es la única dependencia externa de build; está fijada por hash en `requirements-build.txt`. Procedencia y comprobación en el [contrato B1](../07-contracts/commands/local-core-contract.md). El runtime usa biblioteca estándar.

## Instalar y probar

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

El destino debe estar ausente o vacío y su padre debe existir. Si ya usaste `demo-sdd`, elige otro nombre: `init` rechaza la repetición y conserva archivos. Un fallo de escritura puede dejar archivos parciales y `.dixi-init.lock`; inspecciona el directorio, conserva lo útil y usa un destino nuevo. No hay recuperación automática ni borrado al reintentar.

Para documentos en inglés, usa `dixi --lang en init .context/demo-en --agent none` desde la raíz. Las opciones globales (`--lang`, `--json`) preceden al subcomando. `doctor` también funciona fuera de un proyecto; `check` requiere estar en su raíz. Sin instalar, puedes consultar ayuda con `PYTHONPATH=src python3 -m dixi_spec_kit --help` desde este repositorio.

## Interpretar resultados

| Código | Significado |
|---|---|
| 0 | Operación completada dentro de su alcance. |
| 1 | Contenido, enlaces o rutas del proyecto inválidos. |
| 2 | Uso incorrecto o proyecto ausente. |
| 3 | Destino ocupado/inseguro; inicialización rechazada. |
| 4 | Versión de esquema/kit o plataforma no soportada. |
| 5 | Fallo de entrada/salida o recursos del paquete. |

`check` verifica archivos inventariados y declarados en `.dixi/traceability.json`, no escanea todo el árbol. Comprueba padres/IDs y un subconjunto de enlaces Markdown inline y por referencia. Tiene límites de 1 MiB por archivo y 500 archivos/elementos/destinos según el [contrato](../07-contracts/commands/local-core-contract.md). No es un parser CommonMark completo, no visita webs ni valida anchors, completitud de specs o cobertura de negocio. El hash del inventario conserva el contenido inicial; editar una spec no debe fallar solo por cambiar ese hash.

El mismo paquete ya incluye `dixi workflow list/show/prepare`: consulta procedimientos y prepara contexto para un objetivo explícito. Sigue el [recorrido es/en de B2a](workflow-quickstart.md). Las recetas están disponibles sin instalar un agente; preparar no equivale a ejecutarlas.

Los documentos son borradores. El elemento `test` inicial es un plan, no una prueba ejecutable. El `make verify` generado llama a `dixi check`; cada proyecto debe conectar sus propias pruebas antes de afirmar calidad de aplicación. Las instrucciones de `AGENTS.md` son reglas documentales: B1 no instala hooks ni automatiza revisión humana, promoción o despliegue. `dixi init --agent claude` instala además los diez comandos `/dixi.*` para Claude Code; `upgrade` y Codex llegan en v1.1.

## English quickstart

Purpose: build and exercise the local B1 development package without an agent. Tested on macOS with Python 3.15.2 and Make; Python >=3.11 is the declared floor, not a tested compatibility matrix. POSIX directory descriptors and `O_NOFOLLOW` are required. Windows is unsupported in B1.

Run the build commands above from the repository root. Setuptools is a verified, hash-pinned build dependency; the CLI has no third-party runtime dependencies. `make verify` builds wheel/sdist, checks source and catalogs, runs the suite, rebuilds from sdist, and installs both wheels into clean temporary environments without an index. License: MIT.

After installing the local wheel and activating `.venv` as shown above:

```sh
dixi --lang en --help
dixi --lang en init .context/demo-en --agent none
cd .context/demo-en
dixi --lang en doctor
dixi --lang en --json check
make verify
```

The parent directory must exist and the destination must be new or empty. Repeating initialization refuses to overwrite files. Interrupted writes may leave partial files and a lock marker; inspect and preserve useful content, then use a new destination. Global options precede the command.

Exit codes: 0 success, 1 invalid project content, 2 usage/missing project, 3 destination conflict, 4 unsupported version/platform, 5 I/O or package resource failure. Checks inspect declared files and graph references only, use a limited Markdown link syntax, and do not execute application code or access the network. Draft specs and test plans remain drafts even when checks pass. Connect application tests to the generated Makefile before claiming application verification. `--agent claude` installs ten `/dixi.*` Claude Code commands; upgrade and Codex are planned for v1.1.

## Relacionados / Related

- [Evidencia B1 / Verification](b1-verification.md)
- [Contrato / Contract](../07-contracts/commands/local-core-contract.md)
- [Amenazas / Threat model](../13-security/local-core-threat-model.md)
- [Plan / Roadmap](../ROADMAP.md)
