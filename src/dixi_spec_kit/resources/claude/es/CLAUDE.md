# Instrucciones para Claude Code

@AGENTS.md

## Comandos DIXI Spec Kit

Este proyecto incluye comandos en `.claude/commands/`:

`/dixi.discover` → `/dixi.specify` → `/dixi.clarify` → `/dixi.plan` → `/dixi.tasks` → `/dixi.build` → `/dixi.verify` → `/dixi.review`, más `/dixi.analyze` y `/dixi.status` en cualquier momento.

Principios y calidad: `/dixi.constitution` (principios versionados en `00-governance/principles.md`, que lee cada comando), `/dixi.checklist` (checklists de calidad de requisitos; `/dixi.build` se detiene con ítems abiertos) y `/dixi.converge` (compara el código con las specs y añade tareas de convergencia).

Proyectos existentes y trabajo en equipo: `/dixi.onboard` (borradores de módulos y features a partir del código; primero validas la división), `/dixi.bugfix` (prueba en rojo commiteada antes del arreglo, registro trazado del bug) y `/dixi.issues` (tareas a issues de GitHub con `gh`, tras confirmar una vista previa).

Diseño: `/dixi.domain`, `/dixi.architecture`, `/dixi.contract`, `/dixi.threat-model`. Continuidad y cambio: `/dixi.handoff` (escribe `.context/handoff.md`, ignorado por Git) y `/dixi.change`.

Especializados: `/dixi.data`, `/dixi.quality`, `/dixi.ai`, `/dixi.release`, `/dixi.promote`, `/dixi.operate`, `/dixi.finops`, `/dixi.compliance`, `/dixi.duediligence`. Solo escriben documentos; nunca ejecutan migraciones, despliegan, cambian `MODE` ni declaran certificaciones.

Guía y revisión: `/dixi.interview` rellena los huecos `{{pending: …}}` con una pregunta a la vez; `/dixi.risk-review` prepara una revisión por riesgo para una persona. Subagentes en `.claude/agents/`: `dixi-architect`, `dixi-tester`, `dixi-developer`, `dixi-reviewer`.

En terminal: `dixi check`, `dixi doctor`, `dixi workflow list`, `dixi placeholders`, `dixi pr-size` `dixi upgrade --dry-run` (previsualiza qué cambiaría una versión nueva del kit, sin escribir) y `dixi upgrade --apply` (escribe solo los archivos del kit que no has editado).

## Qué no hace este adaptador

No instala permisos ni servidores MCP, ni hooks salvo que el proyecto se cree con `--controls` (entonces `.claude/settings.json` ejecuta los scripts de `.dixi/hooks/`: una segunda capa, no la última). Sin ellos, las reglas de `AGENTS.md` y de cada comando son instrucciones, no controles automáticos: la protección efectiva es la revisión humana y la protección de rama del repositorio. El agente no firma, no aprueba, no integra y no despliega.
