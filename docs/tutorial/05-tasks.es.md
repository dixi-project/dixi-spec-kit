# 5. Dividirla en tareas

## Propósito

Dividir el plan en tareas pequeñas, ordenadas por sus dependencias, cada una enlazada a los criterios de aceptación que cubre.

## Qué haces

Ejecuta [`/dixi.tasks`](../commands/tasks.es.md) con el ID de tu feature:

```text
/dixi.tasks FEATURE-002
```

Con Codex, `$dixi-tasks FEATURE-002`; con un agente de Agent Skills, `@dixi-tasks FEATURE-002`.

## Qué deberías ver

Un archivo `05-features/<slug>/tasks.md` con una lista como esta:

| ID | Tarea | Cubre | Nivel |
|---|---|---|---|
| `T-001` | Guardar una nota con el texto recortado y sus etiquetas | Criterios 1–2 | 1 |
| `T-002` | Listar las notas en orden de creación | Criterio 3 | 1 |

Cada tarea tiene un ID, los criterios que cubre, sus dependencias y un nivel de riesgo de 0 (una corrección) a 3 (estructural). Una tarea de nivel 3 necesita tu validación antes de construirse, y el agente señala como bloqueo cualquier ADR que siga en «Proposed».

Si los requisitos aún tienen preguntas abiertas, [`/dixi.checklist`](../commands/checklist.es.md) las escribe como elementos que marcas; el build se detiene mientras quede alguno abierto.

## Siguiente

[6. Construir una tarea](06-build.es.md).

## Relacionado

- [Tutorial](index.es.md)
- [Referencia de comandos](../commands/index.es.md)
