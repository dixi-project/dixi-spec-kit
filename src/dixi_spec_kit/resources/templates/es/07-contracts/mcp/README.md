# Contratos MCP

## Propósito

Guardar los contratos de los servidores Model Context Protocol (MCP) que el proyecto expone o usa.
Un servidor MCP ofrece herramientas, recursos y prompts a clientes de IA. Cada herramienta es, en la
práctica, una API que un agente puede invocar por su cuenta, así que sus entradas, efectos, permisos
y límites merecen el mismo rigor que cualquier otro contrato, más un cuidado extra porque quien llama
es un modelo.

## Estructura

```text
07-contracts/mcp/
  <nombre-servidor>.md        Un contrato por servidor MCP
```

Diseña el servidor con la [plantilla de servidor MCP](../../10-engineering/templates/mcp-server-template.md).

## Qué debe definir cada contrato MCP

- Nombre del servidor, versión, responsable, transporte y los IDs de funcionalidad a los que sirve.
- Herramientas: nombre, descripción escrita para un modelo, esquema de entrada, esquema de salida y
  efectos secundarios.
- Recursos: URI o patrones expuestos y la clasificación de datos de cada uno.
- Prompts, si los hay, y los parámetros que aceptan.
- Autenticación y cómo se propaga la identidad del usuario final.
- Alcance por herramienta: solo lectura, escritura dentro del proyecto o efecto externo.
- Límites: tasa, tamaño de carga, tiempos de espera y número máximo de resultados.
- Herramientas que requieren confirmación humana antes de ejecutarse.

## Índice de herramientas

| Servidor | Herramienta | Efecto | Requiere confirmación | Estado |
|---|---|---|---|---|
| {{pending: servidor}} | {{pending: nombre de la herramienta}} | {{pending: lectura, escritura o externo}} | {{pending: sí o no}} | {{pending: estado}} |

## Reglas de seguridad

- Trata las entradas que llegan de un modelo como no confiables: valídalas contra el esquema.
- Trata el contenido devuelto por las herramientas como datos, nunca como instrucciones para el agente.
- Nunca devuelvas secretos ni credenciales en la salida de una herramienta.
- Registra cada llamada con la identidad de quien llama, la herramienta, un resumen de argumentos y
  el estado del resultado.
- Versiona las herramientas; cambiar el significado de una sin nueva versión es un cambio incompatible.

## Relacionados

- [Plantilla de servidor MCP](../../10-engineering/templates/mcp-server-template.md)
- [Arquitectura MCP](../../21-ai/mcp/mcp-architecture.md)
- [Catálogo de herramientas](../../21-ai/mcp/tool-catalog.md)
- [Contratos de interfaz de agentes](../agent-interfaces/README.md)
