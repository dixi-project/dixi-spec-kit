# Plantilla de servidor MCP

## Propósito

Especificar un servidor de Model Context Protocol (MCP) que expone herramientas, recursos o
prompts de la plataforma a agentes de IA: qué hace cada uno, quién puede invocarlo y cómo se
asegura y prueba. Copia la estructura de abajo para cada servidor.

## Plantilla

```markdown
# Servidor MCP: <nombre del servidor>

ID: {{pending: ID del servidor}}
Versión: 0.1.0
Responsable: {{pending: equipo responsable}}
Transporte: {{pending: proceso local o remoto sobre HTTP}}

## Propósito

Qué capacidad de la plataforma expone este servidor y qué agentes lo usan.

## Herramientas

### Herramienta: <nombre_herramienta>

- Descripción (escrita para el modelo, precisa y corta):
- Esquema de entrada: (JSON schema con tipos, límites y campos obligatorios)
- Salida: (estructura, y cómo se ve un error)
- Efectos secundarios: ninguno | escribe ... | irreversible ...
- Autorización: qué identidades pueden invocarla
- Requiere confirmación humana: sí | no

## Recursos

### Recurso: <plantilla de URI>

- Contenido y formato:
- Reglas de acceso:

## Prompts (opcional)

- Nombre, argumentos y propósito.

## Seguridad

- Autenticación del cliente: {{pending: mecanismo}}
- Mínimo privilegio: cada herramienta tiene solo los permisos que necesita.
- Entradas validadas; las salidas nunca incluyen secretos.
- Los agentes tratan como no confiable el contenido que reciben.
- Límites de uso y registro de auditoría de cada llamada.

## Dependencias

| Sistema | Usado por | Comportamiento ante fallo |
|---|---|---|

## Pruebas

- Pruebas unitarias por herramienta, incluidas entrada inválida y permiso denegado.
- Prueba de contrato de los esquemas que se listan a los clientes.

## Operación

- Despliegue, configuración y ubicación del runbook.
```

## Relacionados

- [Plantilla de especificación de agente](agent-spec-template.md)
- [Plantilla de integración externa](external-integration-template.md)
- [Estándar de código seguro](../secure-coding-standard.md)
