# Referencia de la CLI

## Propósito

Cada comando de terminal de `dixi` con sus argumentos, opciones y códigos de salida, para poder automatizarlo con seguridad. Las operaciones que se ejecutan dentro de un agente están en la referencia de comandos.

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi [--lang {es,en}] [--json] <command>
```

## Opciones globales

Escríbelas antes del comando, por ejemplo `dixi --lang es --json check`.

- `--help`, `-h` — Mostrar esta ayuda.
- `--version` — Mostrar la versión instalada.
- `--lang {es,en}` — Idioma de mensajes y nuevos documentos.
- `--json` — Emitir resultados estructurados JSON.

## Comandos

- [`dixi init`](init.es.md) — Crear una base documental en un destino nuevo o vacío.
- [`dixi doctor`](doctor.es.md) — Diagnosticar requisitos locales sin red ni credenciales.
- [`dixi check`](check.es.md) — Comprobar estructura y trazabilidad sin ejecutar código.
- [`dixi workflow`](workflow.es.md) — Consultar procedimientos y preparar su contexto sin ejecutar un agente.
- [`dixi upgrade`](upgrade.es.md) — Previsualizar (--dry-run) o aplicar (--apply) lo que esta versión del kit cambia en el proyecto.
- [`dixi extension`](extension.es.md) — Añadir, listar o quitar extensiones locales de solo datos que añaden operaciones (ADR-109).
- [`dixi preset`](preset.es.md) — Añadir, listar o quitar presets locales de solo datos que sustituyen textos del kit (ADR-109).
- [`dixi placeholders`](placeholders.es.md) — Lista los marcadores {{pending: …}} que quedan en los documentos del proyecto.
- [`dixi pr-size`](pr-size.es.md) — Mide la rama actual contra una base: líneas cambiadas, sin documentación, lockfiles, archivos generados ni pruebas.

## Códigos de salida

| Código | Significado |
|---|---|
| 0 | Completado. |
| 1 | Contenido inválido: el proyecto no pasa una comprobación. |
| 2 | Uso incorrecto o proyecto ausente. |
| 3 | Destino ocupado o inseguro. |
| 4 | Versión o plataforma no soportada. |
| 5 | Fallo de entrada o salida. |

## Relacionado

- [Referencia de comandos (operaciones dentro del agente)](../commands/index.es.md)
- [README](../../README.es.md)
