# 2. Crear el proyecto

## Propósito

Crear la base documental del proyecto e instalar las operaciones para tu agente, y comprobar después que todo está en su sitio.

## Qué haces

En una carpeta vacía, crea el proyecto con el adaptador de tu agente. Este tutorial usa Claude Code:

```bash
dixi init notes --agent claude
cd notes
dixi doctor
dixi check
dixi placeholders
```

Para que los documentos y los mensajes queden en español, escribe en su lugar `dixi --lang es init notes --agent claude`; los demás comandos responden en el idioma del proyecto. Con otro agente, cambia solo el primer comando:

| Agente | Comando |
|---|---|
| Codex CLI | `dixi init notes --agent codex` |
| OpenCode, u otro agente que lea Agent Skills | `dixi init notes --agent skills` |
| Cualquier agente o editor, sin operaciones instaladas | `dixi init notes --agent none` |

[`dixi init`](../cli/init.es.md) solo escribe en una carpeta nueva o vacía y nunca sobrescribe un archivo. [`dixi doctor`](../cli/doctor.es.md) comprueba tu entorno y las operaciones instaladas. [`dixi check`](../cli/check.es.md) comprueba la estructura, los enlaces y la cadena de trazabilidad objetivo → dominio → módulo → feature → contrato → prueba. [`dixi placeholders`](../cli/placeholders.es.md) lista los marcadores `{{pending: …}}` que aún esperan una decisión.

Después guarda la base en Git, para que cada cambio posterior se pueda revisar:

```bash
git init
git add .
git commit -m "DIXI baseline"
```

## Qué deberías ver

- `dixi init` dice `Documentary project created: notes` (con `--lang es`, `Proyecto documental creado: notes`).
- `dixi doctor` informa `Installed commands: 33 of 33` (`Comandos instalados: 33 de 33`) y el idioma del proyecto.
- `dixi check` termina con código de salida 0. Comprueba los documentos, no tu aplicación.
- `dixi placeholders` lista siete marcadores pendientes, uno por documento de ejemplo.

El proyecto ya contiene un ejemplo de cada eslabón de la cadena, con los IDs `GOAL-001`, `DOMAIN-001`, `MODULE-001`, `FEATURE-001`, `CONTRACT-001` y `TEST-001`. Tu feature colgará de `MODULE-001`.

## Siguiente

[3. Especificar la feature](03-specify.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de la CLI](../cli/index.es.md)
- [Matriz de soporte](../support-matrix.md)
