# Extensiones y presets

## Propósito

Mostrar cómo escribir una extensión o un preset desde una carpeta vacía e instalarlo. Una extensión añade operaciones propias junto a las del kit; un preset sustituye el texto de operaciones o plantillas del kit por la versión de tu equipo. Los dos son carpetas locales que solo contienen datos: DIXI copia texto, nunca ejecuta nada de ellas y no usa la red.

## Cuál necesitas

| Quieres | Usa | Instala |
|---|---|---|
| Añadir una operación que el kit no tiene | Una extensión | Un comando nuevo llamado `dixi-<id>-<operation>` |
| Cambiar cómo se lee una operación o una plantilla del kit | Un preset | Tu texto en lugar del texto del kit, en el mismo archivo |

Una extensión necesita un proyecto creado con un agente: con `--agent none` no hay archivos de comandos que añadir, y `dixi extension add` se rechaza. Un preset se acepta en cualquier proyecto; con `--agent none` no hay archivos de operaciones que sustituir, así que solo pueden aplicarse sus plantillas.

## Escribir una extensión

Una carpeta con un manifiesto y un texto por operación e idioma. El repositorio tiene esta en [`examples/extension-minimal`](../examples/extension-minimal):

```text
extension-minimal/
├── extension.json
└── operations/
    ├── en/deploy-check.md
    └── es/deploy-check.md
```

`extension.json`:

```json
{"id": "acme", "version": "1.0.0", "operations": ["deploy-check"]}
```

- `id` nombra la extensión; `operations` lista los archivos de `operations/<idioma>/`, sin `.md`. Los nombres usan minúsculas, dígitos y guiones. `id` no puede ser `dixi`.
- Cada operación necesita su texto en inglés y en español; el proyecto recibe el de su idioma.
- Cada texto empieza con dos líneas de encabezado, `description` y `argument-hint`, las dos entre comillas, como las operaciones del kit. En el cuerpo, `$ARGUMENTS` es lo que la persona escribe después del comando.
- No puede haber nada más en la carpeta: otro archivo, un enlace o un idioma que falte rechazan la extensión entera y no se escribe nada.
- Límites: de 1 a 50 operaciones, 64 KiB por texto y `dixi-<id>-<operation>` de 64 caracteres como máximo.

Instálala desde la raíz del proyecto:

```sh
dixi extension add ../examples/extension-minimal
dixi extension list
```

La operación queda disponible como `dixi-acme-deploy-check`: `/dixi-acme-deploy-check` en Claude Code, `$dixi-acme-deploy-check` en Codex y la skill `dixi-acme-deploy-check` en un agente compatible con Agent Skills. El prefijo hace que una extensión nunca pueda tomar el nombre de una operación del kit. Si ya existe un archivo con ese nombre, no se escribe nada.

Para quitarla:

```sh
dixi extension remove acme
```

Borra solo los archivos que instaló y que no editaste; los editados se conservan y se listan.

## Escribir un preset

Una carpeta con un manifiesto y los textos que sustituye. El repositorio tiene este en [`examples/preset-minimal`](../examples/preset-minimal), que le da al traspaso los encabezados propios del equipo:

```text
preset-minimal/
├── preset.json
└── operations/
    ├── en/handoff.md
    └── es/handoff.md
```

`preset.json`:

```json
{"id": "team", "version": "1.0.0", "priority": 50}
```

- `priority` es un número de 0 a 100. Cuando dos presets sustituyen el mismo archivo, gana el más alto.
- `operations/<idioma>/<operación>.md` sustituye una operación del kit; el nombre debe ser el de una operación del kit. `templates/<idioma>/<ruta>` sustituye una plantilla del kit con la misma ruta.
- Inglés y español deben sustituir los mismos archivos.
- Límites: de 1 a 300 archivos, 64 KiB por texto de operación y 256 KiB por plantilla.

Instálalo desde la raíz del proyecto:

```sh
dixi preset add ../examples/preset-minimal
dixi preset list
```

Un archivo se sustituye solo cuando se cumple todo esto:

1. Es un archivo del kit instalado en este proyecto.
2. No lo has editado: conserva el texto del kit, o el de un preset de menor prioridad.
3. No hay un archivo para él en `.dixi/overrides/`. Esa carpeta guarda las versiones propias del proyecto y siempre gana a cualquier preset.

Los archivos que no lo cumplen se conservan y se listan, así que un preset nunca sobrescribe tu trabajo. `dixi upgrade` tampoco sobrescribe un archivo que un preset sustituyó.

Para quitarlo:

```sh
dixi preset remove team
```

Devuelve el texto del kit a los archivos que aún tienen el texto del preset y conserva los que editaste después.

## Qué no hace ninguno de los dos

- No ejecutan código, no añaden hooks ni cambian `--controls`. Una carpeta que contenga algo distinto de los archivos de arriba se rechaza.
- No cambian los límites de las operaciones: escribe en tus textos los mismos límites que llevan las operaciones del kit, porque nada los añade por ti.
- DIXI no los publica ni los descarga. Comparte la carpeta como compartes cualquier otro archivo de tu equipo.

## Relacionado

- [Índice de la documentación](documentation.es.md)
- [Referencia de comandos](commands/index.es.md)
- [Referencia de la CLI: `dixi extension`](cli/extension.es.md)
- [Referencia de la CLI: `dixi preset`](cli/preset.es.md)
- [Contrato de extensiones (en inglés)](../07-contracts/commands/extensions-contract.md)
- [Contrato de presets (en inglés)](../07-contracts/commands/presets-contract.md)
