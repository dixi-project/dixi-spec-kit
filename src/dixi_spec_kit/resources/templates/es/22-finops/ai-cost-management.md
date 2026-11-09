# Gestión de costos de IA

## Propósito

Mantener predecible el costo de los modelos de lenguaje y otros servicios de IA: elegir el modelo adecuado para cada tarea, medir el uso por funcionalidad y frenar rápido el gasto desbocado.

Estado: borrador. {{pending: nombrar al responsable de los costos de IA}}

## Por qué tiene su propio documento

El costo de IA crece con el uso y el tamaño de los prompts más que con los servidores, puede cambiar en minutos por un bucle o un usuario abusivo, y varía en órdenes de magnitud entre modelos para la misma tarea.

## Niveles de modelo

| Nivel | Se usa para | Costo relativo | Modelo en uso |
|-------|-------------|----------------|---------------|
| Pequeño | Clasificación, extracción, enrutamiento, respuestas cortas | Bajo | {{pending: modelo}} |
| Mediano | La mayoría de tareas de generación y resumen | Medio | {{pending: modelo}} |
| Grande | Razonamiento complejo, documentos largos, salidas de alto impacto | Alto | {{pending: modelo}} |

Empieza cada funcionalidad en el nivel más pequeño que pase sus controles de calidad, y sube solo con evidencia. {{pending: definir los controles de calidad por funcionalidad}}

## Palancas de costo

1. **Caché de prompts** para instrucciones o contexto largos y repetidos, cuando el proveedor lo soporte.
2. **Enrutamiento** de solicitudes fáciles a un modelo pequeño y difíciles a uno grande.
3. **Procesamiento por lotes** para trabajo que no necesita respuesta inmediata, cuando exista un precio por lotes más barato.
4. **Contexto más corto**: recupera solo los fragmentos relevantes en lugar de documentos completos.
5. **Límites de salida**: fija una longitud máxima de salida por caso de uso.
6. **Caché de respuestas** para solicitudes idénticas y deterministas.

## Límites y presupuestos

| Alcance | Límite | Acción al alcanzarlo |
|---------|--------|----------------------|
| Por usuario o tenant por día | {{pending: tokens o solicitudes}} | {{pending: limitar / bloquear / avisar}} |
| Por funcionalidad por mes | {{pending: monto}} | Alerta al responsable de la funcionalidad |
| Proyecto completo por mes | {{pending: monto}} | Ver [alertas de presupuesto](budget-alerts.md) |

## Métricas

- Costo por funcionalidad, por solicitud y por usuario activo.
- Tokens de entrada y salida, tasa de aciertos de caché, tasa de errores y reintentos.
- Porcentaje de solicitudes por nivel de modelo.

## Antipatrones

- Reintentar llamadas fallidas sin límite ni espera progresiva.
- Enviar toda la conversación o el documento completo cada vez.
- Exponer un endpoint público que llama a un modelo de pago sin autenticación ni límites de tasa.
- Elegir el modelo más grande «por si acaso» sin medir.

## Revisión mensual

Revisa las métricas con la [plantilla de reporte de costos](templates/cost-report-template.md) y registra los cambios de modelo como decisiones.

## Relacionados

- [Estrategia de costos](cost-strategy.md)
- [Alertas de presupuesto](budget-alerts.md)
- [Playbook de pico de costos](../15-operations/playbooks/cost-spike.md)
- [Guardarraíles](../21-ai/agents/guardrails.md)
