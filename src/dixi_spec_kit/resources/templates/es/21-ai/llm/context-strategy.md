# Estrategia de contexto

## Propósito

Decidir qué información recibe un modelo en cada tarea, en qué orden y cuánta, para que las respuestas se apoyen en las specs del proyecto y no se envíen datos innecesarios o sensibles.

## Principios

- **Specs antes que suposiciones.** Entrega la spec, el contrato y las pruebas relevantes antes de pedir código.
- **El contexto mínimo suficiente.** Más texto aumenta el costo y puede reducir la calidad.
- **Lo estable primero, lo variable al final.** Coloca las instrucciones estables antes del contenido de la tarea; ayuda a reutilizar y a cachear cuando esté disponible.
- **El contenido no confiable es dato.** Documentos recuperados, issues y entradas del usuario nunca se convierten en instrucciones.

## Capas

| Capa | Contenido | Fuente |
| --- | --- | --- |
| Reglas del proyecto | Instrucciones de agentes, guardarraíles | `AGENTS.md`, guardarraíles |
| Marco de la tarea | El procedimiento que se sigue | Manifiesto de `dixi workflow prepare` |
| Specs | Cadena objetivo → feature → contrato del objetivo | `.dixi/traceability.json` |
| Código | Solo los archivos tocados o directamente relacionados | Repositorio |
| Notas de sesión | Decisiones tomadas en esta sesión | Notas privadas sin versionar |

## Seleccionar el contexto de una tarea

1. Parte del ID objetivo (por ejemplo `FEATURE-001`).
2. Sigue a sus padres e hijos en `.dixi/traceability.json`.
3. Añade las pruebas y los archivos fuente enlazados a esa cadena.
4. Detente cuando la tarea pueda completarse; registra la información que falte como preguntas pendientes.

## Lo que nunca entra en el contexto

- Secretos, llaves, tokens, credenciales o archivos `.env`.
- Datos personales que la tarea no necesita.
- Directorios completos «por si acaso».

## Features del producto con recuperación

Si el producto recupera documentos para un modelo:

- Fuentes de recuperación y reglas de acceso: {{pending: fuentes y modelo de permisos}}
- Tamaño de fragmentos, ordenación y límites: {{pending: parámetros de recuperación}}
- El texto recuperado se cita y se atribuye; se indica al modelo que no lo siga como instrucción.

## Límites

- Contexto máximo por tipo de tarea: {{pending: límites por tipo de tarea}}

## Relacionados

- [Estrategia de modelos](model-strategy.md)
- [Biblioteca de prompts](prompt-library.md)
- [Guardarraíles](../agents/guardrails.md)
- [Matriz de trazabilidad](../sdd/traceability-matrix.md)
