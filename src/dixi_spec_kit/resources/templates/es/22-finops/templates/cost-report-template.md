# Plantilla de reporte de costos

## Propósito

Dar a la revisión mensual de costos una estructura fija: qué se gastó, cómo se compara con el presupuesto y las estimaciones, por qué cambió y qué se hará.

Estado: borrador. {{pending: nombrar quién prepara y quién revisa el reporte}}

Copia este archivo para cada periodo, por ejemplo `cost-report-YYYY-MM.md`, y completa cada marcador. Indica la fuente de datos y su fecha; los datos de facturación pueden llegar con retraso.

## Periodo

- Periodo: {{pending: mes y año}}
- Preparado por / revisado por: {{pending: roles}}
- Fuente de datos y fecha de extracción: {{pending: fuente, fecha}}
- Moneda: {{pending: moneda}}

## Resumen

| Métrica | Este periodo | Periodo anterior | Presupuesto | Desviación |
|---------|--------------|------------------|-------------|------------|
| Costo total | {{pending: monto}} | {{pending: monto}} | {{pending: monto}} | {{pending: % y monto}} |
| Producción | {{pending: monto}} | {{pending: monto}} | {{pending: monto}} | {{pending: desviación}} |
| No producción | {{pending: monto}} | {{pending: monto}} | {{pending: monto}} | {{pending: desviación}} |
| Uso de IA | {{pending: monto}} | {{pending: monto}} | {{pending: monto}} | {{pending: desviación}} |

## Costos unitarios

| Unidad | Este periodo | Periodo anterior | Objetivo |
|--------|--------------|------------------|----------|
| Costo por usuario activo | {{pending: valor}} | {{pending: valor}} | {{pending: objetivo}} |
| {{pending: otra unidad}} | {{pending: valor}} | {{pending: valor}} | {{pending: objetivo}} |

## Principales líneas de costo

| Línea | Costo | Cambio | Responsable | Explicación |
|-------|-------|--------|-------------|-------------|
| {{pending: servicio o categoría}} | {{pending: monto}} | {{pending: %}} | {{pending: rol}} | {{pending: motivo}} |

## Estimaciones frente a costos reales

| Elemento | Estimación (supuestos) | Real | Diferencia | Aprendizaje |
|----------|------------------------|------|------------|-------------|
| {{pending: funcionalidad o cambio}} | {{pending: estimación}} | {{pending: real}} | {{pending: diferencia}} | {{pending: aprendizaje}} |

## Incidentes y anomalías

{{pending: picos de costo del periodo, con enlaces a sus registros del playbook}}

## Acciones

| Acción | Ahorro esperado (supuestos) | Responsable | Fecha límite |
|--------|-----------------------------|-------------|--------------|
| {{pending: acción}} | {{pending: estimación}} | {{pending: rol}} | {{pending: fecha}} |

## Relacionados

- [Estrategia de costos](../cost-strategy.md)
- [Alertas de presupuesto](../budget-alerts.md)
- [Gestión de costos de IA](../ai-cost-management.md)
- [Playbook de pico de costos](../../15-operations/playbooks/cost-spike.md)
