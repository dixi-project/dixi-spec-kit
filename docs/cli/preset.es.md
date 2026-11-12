# dixi preset

## Propósito

`dixi preset`: Añadir, listar o quitar presets locales de solo datos que sustituyen textos del kit (ADR-109).

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi preset <command>
dixi preset add <folder>
dixi preset list
dixi preset remove <id>
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.

## Subcomandos

### `dixi preset add`

Aplicar una carpeta de preset (preset.json, operations/en|es, templates/en|es) a los archivos del kit sin editar.

**Argumentos**

- `folder` — Carpeta del preset en el disco local.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi preset list`

Listar los presets instalados.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi preset remove`

Quitar un preset: restaura el texto del kit solo donde el texto del preset no cambió.

**Argumentos**

- `id` — Id del preset.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
