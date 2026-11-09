# Contratos de interfaz de agentes

## Propósito

Describir las interfaces de los agentes de IA que participan en el proyecto: qué puede hacer cada
agente, qué recibe, qué devuelve, qué herramientas puede usar y qué acciones requieren a una persona.
Una interfaz de agente es un contrato como cualquier otro; escribirla hace que el comportamiento del
agente sea revisable, comprobable y sustituible, sin importar el modelo o proveedor que haya detrás.

## Estructura

```text
07-contracts/agent-interfaces/
  <nombre-agente>.interface.md     Contrato legible por personas
  <nombre-agente>.interface.json   Versión opcional legible por máquinas
```

Diseña el agente con la [plantilla de especificación de agente](../../10-engineering/templates/agent-spec-template.md);
esta carpeta solo contiene la interfaz de la que dependen otros componentes.

## Qué debe definir cada interfaz de agente

- Nombre, versión, responsable y los IDs de funcionalidad a los que sirve.
- Capacidades: cada tarea que realiza el agente, con formatos de entrada y salida.
- Nivel de autonomía por capacidad: solo sugerir, actuar con aprobación, o actuar e informar.
- Herramientas que puede invocar y el alcance de cada una (solo lectura, escritura, efecto externo).
- Contexto que recibe y datos que nunca debe recibir (secretos, datos personales innecesarios).
- Validación de la salida: comprobación de esquema, límites y qué ocurre ante una salida inválida.
- Puntos de control humano: acciones que siempre necesitan la aprobación de una persona.
- Auditoría: qué se registra en cada ejecución para poder revisar las decisiones después.

## Forma de ejemplo

```json
{
  "agent": "spec-drafter",
  "version": "0.1.0",
  "capabilities": [
    {"name": "draft_feature_spec", "input": {"goal_id": "string"}, "output": "markdown",
     "autonomy": "suggest"}
  ],
  "tools": ["read_specs"],
  "human_approval_required": ["write_to_main_branch"]
}
```

## Índice de agentes

| Agente | Capacidades | Autonomía | Responsable | Estado |
|---|---|---|---|---|
| {{pending: nombre del agente}} | {{pending: capacidades}} | {{pending: nivel de autonomía}} | {{pending: rol}} | {{pending: estado}} |

## Relacionados

- [Plantilla de especificación de agente](../../10-engineering/templates/agent-spec-template.md)
- [Arquitectura de agentes](../../21-ai/agents/agent-architecture.md)
- [Persona en el circuito](../../21-ai/agents/human-in-the-loop.md)
- [Contratos MCP](../mcp/README.md)
