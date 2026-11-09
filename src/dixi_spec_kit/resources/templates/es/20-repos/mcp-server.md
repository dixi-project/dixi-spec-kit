# Servidor MCP

## Propósito

Describir la estructura y las convenciones esperadas de un repositorio de servidor Model Context Protocol (MCP): un servicio que expone herramientas, recursos o prompts a agentes de IA. Esta guía no elige lenguaje ni SDK; fija las reglas de seguridad y trazabilidad que todo servidor MCP debe cumplir.

Estado: borrador. {{pending: elegir lenguaje, SDK y transporte para los servidores MCP}}

## Decisiones de stack

| Decisión | Elección | ADR |
|----------|----------|-----|
| Lenguaje y SDK | {{pending}} | {{pending}} |
| Transporte (proceso local o red) | {{pending}} | {{pending}} |
| Autenticación para transporte en red | {{pending}} | {{pending}} |
| Ejecutor de pruebas | {{pending}} | {{pending}} |

## Estructura de carpetas sugerida

```text
<servidor-mcp>/
├── README.md          # propósito, herramientas expuestas, IDs de spec
├── AGENTS.md
├── src/
│   ├── tools/         # un módulo por herramienta, con su esquema de entrada
│   ├── resources/     # datos de solo lectura expuestos a agentes
│   ├── prompts/       # plantillas de prompt reutilizables, si las hay
│   └── adapters/      # llamadas a servicios backend
├── tests/
└── .env.example
```

## Catálogo de herramientas

| Herramienta | Qué hace | Efectos secundarios | Requiere aprobación humana |
|-------------|----------|---------------------|----------------------------|
| {{pending: nombre}} | {{pending}} | Ninguno / escribe / llamada externa | {{pending: sí o no}} |

## Convenciones

- Cada herramienta tiene un propósito acotado, un esquema de entrada estricto y una descripción clara.
- Las herramientas de solo lectura están separadas de las que cambian estado; las de escritura requieren aprobación explícita.
- Las entradas se validan; las salidas nunca incluyen secretos ni más datos personales de los necesarios.
- El contenido devuelto desde fuentes externas se trata como datos, no como instrucciones para el agente.
- El servidor actúa con el mínimo privilegio necesario y nunca con las credenciales completas de una persona.
- Cada llamada a herramienta se registra con quien la invoca, la herramienta, un resumen de argumentos y el estado del resultado.
- Límites de frecuencia y timeouts protegen los servicios que hay detrás del servidor.

## Verificación

- Las pruebas cubren entrada válida, entrada inválida, denegación de permisos e intentos de inyección en el contenido devuelto.
- `make verify` ejecuta las comprobaciones reales del servidor.

## Relacionados

- [Repositorios](README.md)
- [Servicio backend](backend-service.md)
- [Endurecimiento de agentes de IA](../13-security/ai-agent-hardening.md)
- [Guardarraíles](../21-ai/agents/guardrails.md)
- [Humano en el ciclo](../21-ai/agents/human-in-the-loop.md)
- [Rastro de auditoría de IA](../21-ai/governance/ai-audit-trail.md)
