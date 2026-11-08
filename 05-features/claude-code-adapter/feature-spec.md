# Feature — Adaptador Claude Code B3

## Propósito

Instalar en un proyecto nuevo los diez comandos `/dixi.*` para que una persona recorra el método dentro de Claude Code, con trazabilidad y gates humanos. Concreta [TASK-003](../../tasks/backlog/TASK-003-adaptador-claude-code.md).

## Historia y criterios

Como persona que usa Claude Code quiero instalar los comandos de DIXI Spec Kit en mi proyecto para recorrer descubrimiento, especificación, plan, tareas, construcción, verificación y revisión sin perder trazabilidad ni control humano.

- CC-01: `init --agent claude` crea la base B1, `CLAUDE.md` y exactamente diez comandos en `.claude/commands/`, sin hooks, settings, MCP ni permisos; sin red. La ayuda de `init` anuncia `claude`.
- CC-02: un destino ocupado (incluido un `.claude/` previo) se rechaza sin cambios.
- CC-03: cada comando tiene frontmatter con `description` y `argument-hint`, usa `$ARGUMENTS`, declara los límites comunes (pruebas congeladas; no firmar, aprobar ni integrar) y solo invoca operaciones `dixi` y procedimientos existentes. No contiene `git push`, `--no-verify` ni rutas absolutas.
- CC-04: `doctor` informa la integración y el número de comandos; `check` falla si falta un comando instalado o si la metadata declara un agente desconocido o un inventario incompleto.
- CC-05: los recursos del adaptador viajan en wheel/sdist y tienen paridad es/en.
- CC-06: el ejemplo público `examples/notes` pasa `dixi check` y su `make verify` ejecuta pruebas reales de aplicación.

## Verificación

`tests/test_claude_adapter.py` cubre CC-01 a CC-06 de forma determinista. El recorrido del ejemplo dentro de Claude Code se registra en [la evidencia B3](../../docs/b3-verification.md); no exige igualdad literal del texto generado.

## Relacionados

- [Módulo padre](../../04-modules/command-workflow/module-spec.md)
- [Contrato B3](../../07-contracts/commands/claude-code-adapter-contract.md)
- [Escenarios](scenarios.feature)
- [Aceptación](acceptance.yaml)
- [Amenazas](../../13-security/claude-code-adapter-threat-model.md)
