# Estrategia de costos

## Propósito

Fijar los principios de gasto en infraestructura, proveedores y uso de IA, para que el costo sea una entrada de diseño desde el inicio y cada costo importante tenga responsable.

Estado: borrador. {{pending: nombrar al responsable de la estrategia de costos}}

## Principios

1. **El costo es un requisito.** Cada spec de funcionalidad indica su costo de operación esperado cuando no es trivial.
2. **Cada costo tiene responsable.** Una línea de la factura sin responsable se investiga y se asigna o se elimina.
3. **Estimar antes de construir.** Las estimaciones listan sus supuestos y su fuente (página de precios del proveedor, facturas anteriores, prueba de carga) y una fecha.
4. **Medir después de publicar.** Compara la estimación con el costo real tras {{pending: semanas}} y registra la diferencia.
5. **Optimizar donde importa.** Dedica esfuerzo primero a las líneas más grandes; ahorros pequeños que añaden complejidad no compensan.
6. **Costo unitario antes que costo total.** Mide el costo por usuario, por solicitud o por tenant, para distinguir crecimiento de desperdicio.

## Presupuesto

| Alcance | Presupuesto mensual | Responsable | Umbrales de alerta |
|---------|---------------------|-------------|--------------------|
| Proyecto completo | {{pending: monto y moneda}} | {{pending: rol}} | Ver [alertas de presupuesto](budget-alerts.md) |
| Producción | {{pending: monto}} | {{pending: rol}} | {{pending: umbrales}} |
| No producción | {{pending: monto}} | {{pending: rol}} | {{pending: umbrales}} |
| Uso de IA | {{pending: monto}} | {{pending: rol}} | Ver [gestión de costos de IA](ai-cost-management.md) |

Ningún monto de este documento es una recomendación; cada uno es una decisión del proyecto.

## Formato de estimación

| Elemento | Supuesto | Precio unitario (fuente, fecha) | Cantidad | Estimación mensual |
|----------|----------|---------------------------------|----------|--------------------|
| {{pending: p. ej. cómputo para la API}} | {{pending: p. ej. 2 instancias, siempre encendidas}} | {{pending: precio, fuente, fecha}} | {{pending: cantidad}} | {{pending: resultado}} |

## Decisiones que necesitan nota de costo

- Elegir o cambiar un proveedor o un modelo de hosting.
- Añadir un entorno, una región o un recurso siempre encendido.
- Añadir o cambiar un modelo de IA, o una funcionalidad que lo llame en cada acción del usuario.
- Aumentar la retención de logs, respaldos o datos de analítica.

## Ritmo de revisión

- Revisión mensual de costos con la [plantilla de reporte de costos](templates/cost-report-template.md).
- Revisión trimestral de esta estrategia y del presupuesto. {{pending: confirmar participantes}}

Puedes usar `/dixi.finops` (Claude Code) o `$dixi-finops` (Codex) para preparar la revisión; una persona aprueba las decisiones.

## Relacionados

- [Alertas de presupuesto](budget-alerts.md)
- [Gestión de costos de IA](ai-cost-management.md)
- [Plantilla de reporte de costos](templates/cost-report-template.md)
- [Playbook de pico de costos](../15-operations/playbooks/cost-spike.md)
- [Proyecto](../00-master-spec.md)
