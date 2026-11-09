# Estrategia de modelos

## Propósito

Dar criterios para elegir modelos de lenguaje para el desarrollo y para el producto, y registrar la política de proveedores del proyecto. Este documento no recomienda proveedor ni modelo; son decisiones del proyecto.

## Política de proveedores

- Proveedores aprobados para herramientas de desarrollo: {{pending: política de proveedores para el desarrollo}}
- Proveedores aprobados para features del producto: {{pending: política de proveedores para el producto}}
- Datos que pueden salir del perímetro del proyecto: {{pending: clases de datos y regiones permitidas}}
- Requisitos contractuales (uso de datos para entrenamiento, retención, lugar de tratamiento): {{pending: requisitos}}

## Criterios de selección

| Criterio | Preguntas a responder |
| --- | --- |
| Ajuste a la tarea | ¿La tarea necesita razonamiento, extracción, clasificación, generación o código? |
| Calidad | ¿Cumple el umbral de evaluación de esta tarea? |
| Latencia | ¿Qué tiempo de respuesta tolera el flujo del usuario? |
| Costo | ¿Cuál es el costo esperado por petición y por mes? |
| Tamaño de contexto | ¿Cuánta entrada debe caber en una llamada? |
| Manejo de datos | ¿Dónde se tratan y guardan los datos, y por cuánto tiempo? |
| Disponibilidad | ¿Hay alternativa si el modelo no está disponible o se retira? |
| Portabilidad | ¿Qué tan difícil es cambiar si cambian los términos? |

## Niveles

Ajusta el tamaño del modelo a la tarea en lugar de usar el más grande en todo:

| Nivel | Tareas típicas | Modelo elegido |
| --- | --- | --- |
| Ligero | Clasificación, enrutamiento, extracción corta | {{pending: definir}} |
| Estándar | Redacción, resúmenes, la mayoría de tareas de código | {{pending: definir}} |
| Pesado | Razonamiento complejo, revisión de arquitectura | {{pending: definir}} |

## Fijación y cambio

- Fija el identificador y la versión exactos del modelo en configuración, no repartidos por el código.
- Cambiar de modelo es un cambio revisable que vuelve a ejecutar las evaluaciones definidas en las puertas de calidad.
- Ten un plan alternativo cuando un modelo quede obsoleto.

## Presupuesto

- Presupuesto mensual y umbral de alerta: {{pending: monto y responsable}}

## Relacionados

- [Estrategia de contexto](context-strategy.md)
- [Biblioteca de prompts](prompt-library.md)
- [Puertas de calidad](../governance/quality-gates.md)
- [IA responsable](../governance/responsible-ai.md)
