# Instrucciones para Claude Code

@AGENTS.md

## Comandos DIXI Spec Kit

Este proyecto incluye comandos en `.claude/commands/`:

`/dixi.discover` → `/dixi.specify` → `/dixi.clarify` → `/dixi.plan` → `/dixi.tasks` → `/dixi.build` → `/dixi.verify` → `/dixi.review`, más `/dixi.analyze` y `/dixi.status` en cualquier momento.

En terminal: `dixi check`, `dixi doctor` y `dixi workflow list` (procedimientos de dominio, arquitectura, contrato y amenazas).

## Qué no hace este adaptador

No instala hooks, permisos ni servidores MCP. Las reglas de `AGENTS.md` y de cada comando son instrucciones, no controles automáticos: la protección efectiva es la revisión humana y la protección de rama del repositorio. El agente no firma, no aprueba, no integra y no despliega.
