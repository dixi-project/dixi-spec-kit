# Controles automáticos

## Propósito

Explicar qué instala `--controls`, qué bloquea cada control y qué no cubre ninguno. Sin controles, las reglas de DIXI son instrucciones que se le piden al agente. Con ellos, cinco scripts pequeños se ejecutan dentro del agente y lo detienen antes de que rompa una de esas reglas.

## Cómo activarlos

Los controles son opcionales y existen para los dos agentes que pueden ejecutar hooks:

```sh
dixi --lang es init mi-proyecto --agent claude --controls
dixi --lang es init mi-proyecto --agent codex --controls
```

En un proyecto que ya existe, `dixi upgrade --dry-run --controls` muestra lo que se añadiría y `dixi upgrade --apply --controls` lo añade. No están disponibles con `--agent skills` ni con `--agent none`: esos agentes no tienen hooks que DIXI pueda instalar, y `dixi init` rechaza la combinación en lugar de instalar algo que no se ejecutaría.

Qué se instala:

- Los cinco scripts, en `.dixi/hooks/`. Cada uno es Python de la biblioteca estándar, lee el evento del agente y responde permitir o bloquear, con el motivo.
- Para Claude Code, `.claude/settings.json` con solo una sección `hooks` que los llama. No se añaden permisos, herramientas ni servidores.
- Para Codex, `.codex/hooks.json`. Codex carga los hooks de un proyecto solo cuando confías en el proyecto, y ejecuta cada hook nuevo o modificado solo después de que lo apruebes con su comando `/hooks`.

## Qué bloquea cada control

| Control | Qué bloquea | Cuándo se ejecuta |
|---|---|---|
| `protect_tests.py` | Cambiar, mover o borrar una prueba que ya está commiteada, con las herramientas de edición o con un comando de shell. Las pruebas que aún no están commiteadas sí se pueden escribir: así es como las pruebas van primero. | Antes de cada edición y de cada comando de shell |
| `guard_secrets.py` | Leer archivos `.env*`, llaves privadas, `.aws/`, `.ssh/` y archivos de credenciales, directamente o con un comando de shell. Los archivos de ejemplo, como `.env.example`, se permiten. | Antes de cada lectura, búsqueda y comando de shell |
| `guard_attestation.py` | Firmar un commit, aprobar o integrar un pull request y marcar una casilla de atestación. El agente puede hacer commits sin firma; la persona firma. | Antes de cada comando de shell |
| `mode_gate.py` | Con `MODE` en `prod`: borrados recursivos fuera de carpetas temporales, push forzado, reset duro de una rama compartida, aplicar o destruir infraestructura, borrados en un clúster y `DROP` o `TRUNCATE` de SQL. Con `mvp` los permite. | Antes de cada comando de shell |
| `verify_on_stop.py` | Terminar el turno cuando cambiaron archivos y `make verify` falla. Tras una continuación forzada deja que el agente se detenga y te avisa, para que el agente nunca quede atrapado en un bucle. | Cuando el agente, o un subagente, está por detenerse |

Dos de ellos tienen un ajuste, que se lee del entorno con el que inicias el agente:

- `DIXI_ALLOW_TEST_EDITS=1` permite que el agente edite pruebas commiteadas durante esa sesión. Úsalo cuando hayas decidido que una prueba está mal; la decisión es tuya, no del agente.
- `DIXI_VERIFY_TIMEOUT` son los segundos que `verify_on_stop.py` espera a `make verify`; por defecto, 240.

## Cómo ver que están activos

1. `dixi doctor` informa si el proyecto se creó con controles.
2. Los archivos existen: `.dixi/hooks/` con los cinco scripts, y `.claude/settings.json` o `.codex/hooks.json`.
3. Pídele al agente algo que un control bloquea, por ejemplo cambiar una prueba commiteada. Se detiene con un mensaje que empieza por el nombre del control, como `DIXI protect_tests`, y el archivo no cambia.

En Codex, comprueba además que el proyecto es de confianza y que los hooks están aprobados; hasta entonces no se ejecutan.

## Qué no cubren los controles

Un control es una segunda capa, nunca la última.

- Un hook se puede evadir. `protect_tests.py` no ve un archivo escrito por un script que se ejecuta desde un archivo, ni uno al que se llega por una ruta construida en tiempo de ejecución o guardada en una variable de shell. En esos casos sigue valiendo la regla escrita en `AGENTS.md`.
- Revisan comandos, no intenciones: no juzgan si un cambio es correcto, completo o seguro.
- Actúan solo dentro del agente. Una persona, otra herramienta o un job de integración continua no se ven afectados.
- No sustituyen tu revisión ni la protección de la rama principal. La protección efectiva sigue siendo que una persona lea el cambio y que el repositorio lo exija.
- `mode_gate.py` lee `MODE`; nunca lo cambia. `dixi mode` muestra lo que falta antes de que una persona lo cambie.

## Relacionado

- [Índice de la documentación](documentation.es.md)
- [Subagentes](subagents.es.md)
- [Matriz de soporte (en inglés, con resumen en español)](support-matrix.md)
- [Referencia de la CLI](cli/index.es.md)
- [Contrato de controles (en inglés)](../07-contracts/commands/automated-controls-contract.md)
