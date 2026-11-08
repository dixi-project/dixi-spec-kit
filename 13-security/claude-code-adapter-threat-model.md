# Threat model STRIDE — Adaptador Claude Code B3

## Propósito

Identificar amenazas propias de instalar comandos de agente antes de implementarlos. Amplía el [modelo B1](local-core-threat-model.md); las amenazas de filesystem se heredan.

## Activos y límites de confianza

Activos: archivos del usuario, configuración de Claude Code, pruebas congeladas, historial Git y secretos locales. El texto que escribe la persona (`$ARGUMENTS`) y los documentos del proyecto son datos no confiables para el agente. La CLI no ejecuta el agente; el riesgo principal está en lo que los comandos instruyen.

## Amenazas y mitigaciones

| ID / STRIDE | Amenaza | Mitigación | Prueba |
|---|---|---|---|
| A01 / Elevation | Instalar permisos, hooks o MCP que amplíen lo que el agente puede hacer sin decisión de la persona. | Solo `CLAUDE.md` y `.claude/commands/dixi.*.md`; sin `allowed-tools`. | `test_installs_only_commands` |
| A02 / Tampering | Sobrescribir comandos o configuración `.claude/` existentes. | Destino vacío obligatorio y creación exclusiva (B1). | `test_existing_claude_dir_untouched` |
| A03 / Tampering | Un comando instruye modificar pruebas congeladas para pasar. | Límite común explícito en cada comando; revisión humana del PR. | `test_commands_declare_limits` |
| A04 / Repudiation | El agente firma, aprueba, integra o hace push en nombre de la persona. | Límite común; ningún comando contiene `git push` ni `--no-verify`. | `test_commands_declare_limits`, `test_commands_avoid_dangerous_operations` |
| A05 / Information disclosure | Inyección de instrucciones en specs o argumentos para leer secretos. | Instrucción de tratar entradas como datos; `dixi` deniega rutas sensibles. Riesgo residual: no hay enforcement en el agente. | `test_commands_declare_limits` |
| A06 / Spoofing | Metadata que declara un agente o inventario falso para pasar `check`. | Agente en lista cerrada e inventario completo exigido. | `test_unknown_agent_metadata`, `test_incomplete_adapter_inventory` |
| A07 / Information disclosure | Comandos que referencian recursos privados o ausentes. | Solo operaciones `dixi` existentes y procedimientos empaquetados. | `test_commands_reference_existing_operations` |

## Riesgo residual

Las instrucciones en Markdown dependen del modelo y no son controles. La protección efectiva contra cambios no revisados está en la protección de rama y la revisión humana del repositorio del proyecto, que el kit documenta pero no configura.

## Relacionados

- [Contrato B3](../07-contracts/commands/claude-code-adapter-contract.md)
- [Feature](../05-features/claude-code-adapter/feature-spec.md)
- [Modelo B1](local-core-threat-model.md)
