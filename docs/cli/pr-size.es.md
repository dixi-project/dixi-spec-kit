# dixi pr-size

## Propósito

`dixi pr-size`: Mide la rama actual contra una base: líneas cambiadas, sin documentación, lockfiles, archivos generados ni pruebas.

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi pr-size [--base <base>] [--max <limit>]
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.
- `--base <base>` — Rama o commit base (por defecto: main).
- `--max <limit>` — Máximo de líneas contadas (por defecto: 1500).

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
