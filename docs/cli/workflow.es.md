# dixi workflow

## Propósito

`dixi workflow`: Consultar procedimientos y preparar su contexto sin ejecutar un agente.

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi workflow <command>
dixi workflow list
dixi workflow show <operation>
dixi workflow prepare <operation> --target <target> --request <request>
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.

## Subcomandos

### `dixi workflow list`

Listar los procedimientos compartidos disponibles.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi workflow show`

Mostrar entradas, pasos, salidas y gates de un procedimiento.

**Argumentos**

- `operation` — Procedimiento compartido. Una de las operaciones que lista `dixi workflow list`.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.

### `dixi workflow prepare`

Preparar instrucciones y manifiesto del objetivo; sin escribir ni ejecutar IA.

**Argumentos**

- `operation` — Procedimiento compartido. Una de las operaciones que lista `dixi workflow list`.

**Opciones**

- `--help`, `-h` — Mostrar esta ayuda.
- `--target <target>` — ID exacto de un objetivo compatible en el grafo. Obligatoria.
- `--request <request>` — Solicitud explícita; hasta 4 096 caracteres, sin secretos. Obligatoria.

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
