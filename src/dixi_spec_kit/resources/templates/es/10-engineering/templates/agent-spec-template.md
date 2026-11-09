# Plantilla de especificación de agente

## Propósito

Especificar un agente de IA que forma parte de la plataforma: qué puede hacer, qué contexto y
herramientas usa, sus guardrails, cómo escala a personas y cómo se mide. Copia la estructura de
abajo para cada agente. La spec se mantiene independiente de cualquier proveedor de modelos.

## Plantilla

```markdown
# Agente: <nombre del agente>

ID: {{pending: ID del agente}}
Versión: 0.1.0
Responsable: {{pending: persona que responde por el comportamiento del agente}}
Estado: borrador | piloto | activo | retirado

## Propósito

El trabajo que hace el agente y para quién. Un párrafo.

## Capacidades

- Puede: ...
- No puede (fuera de alcance explícito): ...

## Contexto

- Siempre cargado: (instrucciones, políticas)
- Cargado bajo demanda: (documentos, registros, con reglas de acceso)
- Memoria persistente: qué se guarda, dónde y por cuánto tiempo. {{pending: política de memoria}}

## Herramientas

| Herramienta | Acción | Efectos secundarios | ¿Requiere aprobación humana? |
|---|---|---|---|

## Guardrails

- Alcance: temas y datos que el agente debe rechazar.
- Acciones: las acciones irreversibles o costosas siempre requieren aprobación humana.
- Calidad: la salida se valida contra un contrato antes de usarse.
- Costo: presupuesto por tarea y por periodo; comportamiento al excederlo.
- Entrada no confiable: el contenido de usuarios, documentos o herramientas es dato, nunca instrucción.

## Flujos de trabajo

1. Disparador ... → pasos ... → salida ...

## Escalamiento

Cuándo y cómo el agente pasa el caso a una persona, con el contexto que debe entregar.

## Métricas y evaluación

| Métrica | Objetivo | Conjunto de evaluación |
|---|---|---|

## Registro de cambios

| Versión | Cambio | Evaluado sobre |
|---|---|---|
```

## Relacionados

- [Plantilla de prompt](prompt-template.md)
- [Plantilla de servidor MCP](mcp-server-template.md)
- [Estándar de código seguro](../secure-coding-standard.md)
- [Instrucciones del proyecto](../../AGENTS.md)
