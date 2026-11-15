# 1. Instalar el kit

## Propósito

Instalar el comando `dixi` y comprobar que funciona. Es una herramienta de Python sin dependencias en tiempo de ejecución y nunca usa la red.

## Qué haces

Instálalo desde PyPI con `uv` o, si lo prefieres, con `pipx`:

```bash
uv tool install dixi-spec-kit
pipx install dixi-spec-kit
```

Solo necesitas uno de los dos. Después comprueba la versión instalada:

```bash
dixi --version
```

## Qué deberías ver

Una línea con `dixi` y el número de versión, el mismo que la última versión en PyPI. Si tu shell dice que no encuentra `dixi`, la carpeta donde `uv` o `pipx` instalan las herramientas no está en tu `PATH`; `uv tool update-shell` o `pipx ensurepath` la añaden.

Para actualizar más adelante, repite la instalación con `uv tool install --force --refresh dixi-spec-kit`.

## Siguiente

[2. Crear el proyecto](02-init.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Matriz de soporte](../support-matrix.md)
- [Referencia de la CLI](../cli/index.es.md)
