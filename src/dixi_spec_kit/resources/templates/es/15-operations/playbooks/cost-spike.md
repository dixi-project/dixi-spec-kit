# Pico de costos

## Propósito

Investigar y contener un aumento inesperado del costo de infraestructura, almacenamiento, red o uso de IA antes de que se convierta en una factura grande.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

## Cuándo aplica

- Salta una alerta de presupuesto (ver [alertas de presupuesto](../../22-finops/budget-alerts.md)).
- El gasto diario de un servicio o cuenta crece más de {{pending: porcentaje}} sobre su promedio reciente.
- Alguien nota una línea inusual en la factura.

## Roles

- **Responsable de costos** del servicio afectado: lidera la investigación.
- **Operador**: persona con acceso que aplica la contención.
- **Contacto de finanzas**: se le informa cuando el exceso proyectado supera {{pending: monto o porcentaje}}.

## Pasos

1. **Confirmar** que el pico es real: compara con el mismo día de la semana anterior y descarta retrasos de facturación o cargos únicos.
2. **Ubicar**: desglosa el costo por servicio, entorno, etiqueta y tipo de uso.
3. **Clasificar la causa**, familias típicas:
   - cómputo: bucle de autoescalado, recursos de prueba olvidados, instancias sobredimensionadas;
   - red: tráfico por una ruta de pago, transferencia de datos entre regiones, una integración demasiado habladora;
   - almacenamiento: logs o respaldos sin retención, objetos que crecen sin reglas de ciclo de vida;
   - base de datos: consultas desbocadas, réplicas de más, crecimiento automático del almacenamiento;
   - uso de IA: un bucle que llama a un modelo, un modelo más grande de lo necesario, prompts sin caché, abuso de un endpoint público.
4. **Contener** con la acción menos disruptiva: bajar un límite, pausar un proceso, añadir una cuota o límite de tasa, borrar recursos de prueba claramente huérfanos. Los cambios en producción siguen la aprobación normal; un agente de IA nunca los aplica solo.
5. **Estimar** el impacto: gasto extra proyectado, con supuestos y fuente de datos.
6. **Corregir** la causa raíz y añadir una protección para que no se repita en silencio (alerta, cuota, regla de retención, test).

## Criterios de cierre

- Gasto diario de vuelta en el rango esperado durante {{pending: días}}.
- Causa raíz escrita, con la estimación y su fuente.
- Una protección preventiva está activa o registrada en el backlog.

## Relacionados

- [Alertas de presupuesto](../../22-finops/budget-alerts.md)
- [Gestión de costos de IA](../../22-finops/ai-cost-management.md)
- [Estrategia de costos](../../22-finops/cost-strategy.md)
- [Matriz de escalamiento](../escalation-matrix.md)
