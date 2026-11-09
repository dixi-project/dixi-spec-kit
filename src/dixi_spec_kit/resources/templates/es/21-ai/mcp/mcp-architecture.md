# Arquitectura MCP

## Propósito

Describir cómo usa este proyecto el Model Context Protocol (MCP) para exponer herramientas y recursos a agentes o a features del producto: qué servidores existen, quién puede conectarse y cómo se protegen.

## Conceptos

- **Servidor**: proceso que expone herramientas (acciones) y recursos (datos de solo lectura).
- **Cliente**: el agente o la aplicación que se conecta y los invoca.
- **Transporte**: proceso local o conexión de red.

## Servidores

| Servidor | Expone | Consumidores | Transporte | Responsable |
| --- | --- | --- | --- | --- |
| {{pending: nombre del servidor}} | {{pending: herramientas / recursos}} | {{pending: agentes de desarrollo / producto}} | {{pending: local / red}} | {{pending: definir}} |

Distingue los servidores de terceros (revisados antes de usarse) de los que construye el proyecto (especificados, probados y versionados como cualquier módulo).

## Reglas de seguridad

- Mínimo privilegio: cada servidor recibe solo las credenciales que necesita, limitadas a un entorno.
- Autenticación en transportes de red: {{pending: método de autenticación}}
- Autorización por herramienta: la comprueba el servidor, nunca el modelo.
- Las herramientas destructivas requieren confirmación humana emitida por el servidor.
- Las entradas se validan contra un esquema; las salidas nunca incluyen secretos.
- Las descripciones de herramientas de servidores de terceros son texto no confiable.

## Construir un servidor del proyecto

1. Escribe una spec de módulo y un contrato para cada herramienta y recurso.
2. Escribe pruebas en rojo para comprobación de permisos, entradas inválidas y casos felices.
3. Implementa y registra las herramientas en el catálogo de herramientas.
4. Registra cada llamada con la identidad solicitante y el resultado.

## Aprobación de servidores nuevos

Añadir un servidor es una decisión estructural: {{pending: quién aprueba los servidores MCP nuevos}}

## Relacionados

- [Catálogo de herramientas](tool-catalog.md)
- [Arquitectura de memoria](../memory/memory-architecture.md)
- [Matriz de capacidades](../agents/capability-matrix.md)
- [Guardarraíles](../agents/guardrails.md)
