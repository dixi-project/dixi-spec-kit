# dixi extension

## Propósito

`dixi extension`: Añadir, listar o quitar extensiones locales de solo datos que añaden operaciones (ADR-109).

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi extension <command>
dixi extension add <folder>
dixi extension list
dixi extension remove <id>
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.

## Subcomandos

### `dixi extension add`

Instalar una carpeta de extensión (extension.json y operations/en|es/*.md) para el agente del proyecto.

**Argumentos**

- `folder` — Carpeta de la extensión en el disco local.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi extension list`

Listar las extensiones instaladas.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi extension remove`

Quitar una extensión: borra solo los archivos que instaló y que no has editado.

**Argumentos**

- `id` — Id de la extensión.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
