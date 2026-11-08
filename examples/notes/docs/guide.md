# Uso documental

## Propósito

Trabajar sin depender de un agente o lenguaje específico.

1. Completa visión, dominio y módulo; conserva sus IDs.
2. Define una feature y sus criterios observables.
3. Documenta contrato y pruebas previstas; valida decisiones estructurales.
4. Registra rutas y padres en `.dixi/traceability.json`.
5. Elige stack y conecta sus pruebas reales a `make verify`.
6. Ejecuta verificaciones y solicita revisión humana antes de integrar.

La CLI ofrece `init`, `doctor`, `check`, `workflow`, ayuda y versión. Con `--agent claude`, los comandos `/dixi.*` están en `.claude/commands/`; con `--agent none` no se instalan comandos de agente. Puedes editar los documentos con tus herramientas. El hash en `.dixi/project.json` conserva la versión original para futuras actualizaciones; no lo cambies para simular verificación. Secretos fuera del repositorio; contexto privado en `.context/`, sin versionar. Las políticas de proveedores se deciden explícitamente; no hay cuentas ni conexiones configuradas.

## Relacionados

- [Proyecto](../00-master-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)

## Procedimientos compartidos

Consulta `dixi workflow list` y `dixi workflow show discover`. Para preparar contexto usa `dixi workflow prepare discover --target GOAL-001 --request "Describe la necesidad"`. `prepare` no escribe specs ni ejecuta un agente: entrega pasos, gates y un manifiesto de fuentes con hashes. Completa el procedimiento con tus herramientas, conserva los IDs y registra qué sigue pendiente. Nunca incluyas secretos en la solicitud.
