# DIXI Spec Kit

[English](README.md) · **Español**

## Propósito

DIXI Spec Kit es una herramienta de [Dixi Project](https://github.com/dixi-project) para desarrollar software guiado por especificaciones (SDD) con trazabilidad y verificación: de la idea a specs enlazadas, pruebas primero, código verificado y revisión humana. Incluye una CLI (`dixi`) y comandos para Claude Code.

- **Trazabilidad explícita:** objetivo → dominio → módulo → feature → contrato → prueba, con IDs que `dixi check` comprueba.
- **Pruebas primero y congeladas:** los comandos instruyen escribir pruebas en rojo antes del código y no tocarlas para hacerlo pasar.
- **Control humano:** el agente no firma, no aprueba, no integra y no despliega.
- **Sin dependencias ni red:** la CLI usa solo la biblioteca estándar de Python, no consume IA y no pide credenciales. El lenguaje de tu proyecto lo eliges tú.

## Instalación

Requisitos: Python 3.11 o superior, macOS o Linux. Windows no está soportado en v1.0.0.

```sh
uv tool install git+https://github.com/dixi-project/dixi-spec-kit@v1.0.0
# o
pipx install git+https://github.com/dixi-project/dixi-spec-kit@v1.0.0
```

El paquete aún no está publicado en PyPI. También puedes descargar el wheel de la [release v1.0.0](https://github.com/dixi-project/dixi-spec-kit/releases/tag/v1.0.0) e instalarlo con `pipx install dixi_spec_kit-1.0.0-py3-none-any.whl`.

## Inicio rápido

```sh
dixi --lang es init mi-proyecto --agent claude   # o --agent none para usarlo sin agente
cd mi-proyecto
dixi doctor
dixi check
make verify
```

Abre Claude Code en `mi-proyecto` y recorre:

```text
/dixi.discover <tu idea>
/dixi.specify <funcionalidad>
/dixi.clarify <ID de la spec>
/dixi.plan <FEATURE-ID>
/dixi.tasks <FEATURE-ID>
/dixi.build <T-ID>
/dixi.verify
/dixi.review main
```

`/dixi.analyze` revisa coherencia e impacto de un cambio; `/dixi.status` indica el siguiente paso. Diseña con `/dixi.domain`, `/dixi.architecture`, `/dixi.contract` y `/dixi.threat-model`; propone cambios con `/dixi.change`; deja un traspaso con `/dixi.handoff`. Operaciones especializadas: `/dixi.data`, `/dixi.quality`, `/dixi.ai`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance` y `/dixi.duediligence` solo escriben documentos; nunca ejecutan migraciones, despliegan, cambian `MODE` ni declaran certificaciones. Sin `--lang es`, documentos y mensajes salen en inglés; dentro de un proyecto, los mensajes siguen su idioma.

## Comandos de terminal

| Comando | Qué hace |
|---|---|
| `dixi init <dir> [--agent none\|claude\|codex]` | Crea la base documental en un directorio nuevo o vacío; nunca sobrescribe. |
| `dixi doctor` | Diagnostica el entorno y el proyecto sin red ni credenciales. |
| `dixi check` | Comprueba estructura, enlaces y trazabilidad. No ejecuta código. |
| `dixi workflow list\|show\|prepare` | Consulta y prepara los procedimientos de descubrimiento, especificación, dominio, arquitectura, contrato, amenazas y plan. |
| `dixi upgrade --dry-run` | Previsualiza qué cambiaría la versión instalada del kit: archivos sin cambios, actualizables, en conflicto, nuevos, ausentes y obsoletos. No escribe nada. |
| `dixi --help`, `dixi --version` | Ayuda y versión. Opciones globales: `--lang es\|en`, `--json`. |

Códigos de salida: 0 completado, 1 contenido inválido, 2 uso incorrecto o proyecto ausente, 3 destino ocupado o inseguro, 4 versión o plataforma no soportada, 5 fallo de entrada/salida.

## Ejemplo

[`examples/notes`](examples/notes) es una biblioteca y CLI de notas construida con este recorrido, con una evolución y su análisis de impacto. `make verify` ejecuta `dixi check` y 12 pruebas reales.

## Qué incluye y qué no

Lo que ofrece cada integración y sus límites están en la [matriz de soporte](docs/support-matrix.md). En resumen: el adaptador de Claude Code instala comandos e instrucciones, **no hooks ni permisos**; las reglas son instrucciones para el agente, y la protección efectiva es tu revisión y la protección de rama. El adaptador de Codex (`--agent codex`, skills que se invocan como `$dixi-specify`, `$dixi-plan`, …) instala las mismas operaciones como Agent Skills, con la invocación implícita desactivada. Aplicar actualizaciones automáticamente aún no está disponible ([plan](ROADMAP.md)). Windows no está soportado.

## Contribuir

Cualquiera puede usar, clonar y hacer fork. Los cambios se proponen con un PR desde tu fork; solo los mantenedores integran en `main`, con revisión y checks en verde. Consulta [CONTRIBUTING.md](CONTRIBUTING.md). Las vulnerabilidades se reportan de forma privada según [SECURITY.md](SECURITY.md).

## Licencia

[MIT](LICENSE) © 2026 Dixi Project. Los proyectos que generes con `dixi init` son tuyos.
