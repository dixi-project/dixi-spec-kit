# Módulo — Flujo de trabajo por comandos

## Propósito

Conectar comandos, artefactos y verificaciones para implementar el dominio de desarrollo guiado por especificaciones. B1 implementa CLI, filesystem seguro, recursos y validación estructural en `src/dixi_spec_kit/`. B2a añade recetas compartidas y preparación de contexto en `workflows.py`; ejecución mediante adaptadores y operaciones posteriores siguen pendientes.

## Responsabilidades

| Parte | Responsabilidad | Límite |
|---|---|---|
| CLI local | Instalar recursos, diagnosticar, validar estructura y planificar actualización. | Sin inferencia ni llamadas a IA/AWS. |
| Recursos y contratos | Compartir plantillas, reglas, identificadores y comportamiento por operación. | No duplicar reglas distintas por cada entrada del agente. |
| Adaptadores elegibles | Exponer las mismas operaciones del núcleo en cada herramienta, cargar contexto y declarar capacidades/controles. | No seleccionar un agente implícitamente ni asumir compatibilidad sin evaluar cada adaptador. |
| Perfiles de stack | Conectar herramientas y comprobaciones del lenguaje/framework elegido a `make verify`. | Python como runtime del kit no impone Python al proyecto. |
| Conjuntos de políticas | Declarar garantías y mecanismos según las decisiones del proyecto. | Dirección portable/Dixi aceptada; mecanismos operativos pendientes según ADR-101. |
| Validación y evidencia | Comprobaciones deterministas y registro de resultados ligados al estado revisado. | No sustituir evaluación semántica ni aprobación humana. |

`plan` reutiliza las capacidades de dominio, arquitectura, contratos y amenazas; las entradas directas trabajan sobre los mismos artefactos. `analyze`, `verify` y `review` distinguen coherencia, ejecución de controles y preparación de revisión. La CLI no ejecuta texto generado por el agente.

El modo sin integración conserva plantillas, guías y validadores locales. Los adaptadores no poseen las specs y no cambian sus IDs. Una integración sin el control necesario no puede anunciar una protección equivalente; debe declarar la limitación y respetar el gate.

## Contratos y riesgos

Consume [command-contract.md](../../07-contracts/commands/command-contract.md) por bloques. La feature de flujo guiado cubre la coordinación; [local-core](../../05-features/local-core/feature-spec.md) concreta B1 con [contrato](../../07-contracts/commands/local-core-contract.md), [threat model](../../13-security/local-core-threat-model.md) y pruebas de CLI/distribución. Actualización e integraciones tendrán su cobertura antes de implementar sus bloques.

Riesgos principales: escritura fuera de raíz, pérdida de cambios locales, instrucciones maliciosas en documentos, evidencia falsa/desactualizada y bypass de gates. Se exige threat model propio del kit y pruebas por amenaza antes de construir. El comando `threat-model` del producto no sustituye esa obligación durante su desarrollo.

## Relacionados

- [Dominio padre](../../03-domains/spec-driven-delivery/domain-spec.md)
- [Feature](../../05-features/guided-workflow/feature-spec.md)
- [Preparación B2a](../../05-features/workflow-preparation/feature-spec.md)
- [Contrato B2a](../../07-contracts/commands/workflow-preparation-contract.md)
- [Contrato](../../07-contracts/commands/command-contract.md)
- [ADR-100](../../09-architecture/adr/ADR-100-distribucion-publica-v1.md)
- [ADR-101](../../09-architecture/adr/ADR-101-nucleo-sdd-portable-e-integraciones.md)
