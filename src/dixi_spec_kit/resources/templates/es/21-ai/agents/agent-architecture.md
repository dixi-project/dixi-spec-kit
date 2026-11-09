# Arquitectura de agentes

## Propósito

Describir qué agentes de IA participan en este proyecto, de qué es responsable cada uno, cómo se pasan el trabajo entre ellos y a las personas, y dónde se ejecutan. Es neutral respecto al proveedor: importan más los roles y los límites que la herramienta.

## Roles

| Rol | Responsabilidad | Salidas típicas | No debe |
| --- | --- | --- | --- |
| Especificador | Convertir una necesidad en borradores de objetivo, dominio, módulo y feature | Borradores con marcas pendientes | Aprobar sus propias specs |
| Redactor de contratos | Derivar contratos de features aprobadas | Borradores de contrato | Cambiar en silencio contratos aprobados |
| Redactor de pruebas | Escribir pruebas en rojo a partir de contratos | Archivos de prueba | Editar pruebas congeladas |
| Constructor | Implementar hasta que pasen las pruebas | Cambios de código | Debilitar pruebas o comprobaciones |
| Revisor | Leer diffs contra las specs y reportar riesgos | Comentarios de revisión | Aprobar o integrar |

Los roles pueden ser modos de un mismo agente o agentes distintos: {{pending: un agente con modos o agentes separados}}

## Flujo

```text
necesidad → especificador → [la persona valida] → redactor de contratos → redactor de pruebas
          → constructor → revisor → [la persona revisa, aprueba e integra]
```

Cada flecha pasa artefactos del repositorio, no estado oculto. Usa `dixi workflow prepare <nombre>` para dar a cada paso el mismo manifiesto de contexto.

## Modos de ejecución

| Modo | ¿Hay una persona al teclado? | Acciones permitidas |
| --- | --- | --- |
| Interactivo | Sí | Leer y escribir en la copia de trabajo; los comandos piden confirmación |
| Desatendido | No | {{pending: acciones permitidas, por ejemplo comentarios de revisión de solo lectura}} |

Los agentes desatendidos deben procesar contenido no confiable sin secretos y producir comentarios o artefactos, nunca despliegues.

## Contexto y permisos

- Cada rol recibe solo los archivos que necesita (ver la estrategia de contexto).
- Cada rol tiene el conjunto mínimo de herramientas para su tarea (ver la matriz de capacidades).

## Decisiones del proyecto

- Integraciones de agentes en uso: {{pending: ninguna, o las integraciones elegidas}}
- Dónde se ejecutan los agentes desatendidos: {{pending: entorno y aislamiento}}

## Relacionados

- [Matriz de capacidades](capability-matrix.md)
- [Guardarraíles](guardrails.md)
- [Humano en el circuito](human-in-the-loop.md)
- [Estrategia de contexto](../llm/context-strategy.md)
- [Metodología](../sdd/methodology.md)
