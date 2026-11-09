# Alertas de presupuesto

## Propósito

Detectar pronto el exceso de gasto con alertas sobre el costo real y el proyectado, y asegurar que cada alerta llega a alguien que puede actuar.

Estado: borrador. {{pending: nombrar al responsable de las alertas de presupuesto}}

## Tipos de alerta

| Tipo | Salta cuando | Por qué |
|------|--------------|---------|
| Umbral real | El gasto acumulado del mes supera un porcentaje del presupuesto | Detecta excesos sostenidos |
| Umbral proyectado | El gasto proyectado a fin de mes supera el presupuesto | Avisa antes de gastar el dinero |
| Anomalía | El gasto diario salta muy por encima de su patrón reciente | Detecta picos súbitos, bucles, abuso |
| Cuota de uso | Un recurso medido (tokens de IA, llamadas a API, almacenamiento) supera un límite | Detecta costos que la facturación reporta tarde |

## Umbrales

| Alcance | Presupuesto | Alertas reales | Alerta proyectada | Destinatarios |
|---------|-------------|----------------|-------------------|---------------|
| Proyecto completo | {{pending: monto}} | {{pending: p. ej. 50 %, 80 %, 100 %}} | {{pending: p. ej. 100 %}} | {{pending: roles, p. ej. finops@example.com}} |
| Producción | {{pending: monto}} | {{pending: umbrales}} | {{pending: umbral}} | {{pending: roles}} |
| No producción | {{pending: monto}} | {{pending: umbrales}} | {{pending: umbral}} | {{pending: roles}} |
| Uso de IA | {{pending: monto}} | {{pending: umbrales}} | {{pending: umbral}} | {{pending: roles}} |

Los porcentajes son ejemplos. Elige valores que dejen tiempo para reaccionar.

## Enrutamiento

- Los umbrales informativos van a un canal de costos o a correo.
- El 100 % real, la proyección por encima del presupuesto y las anomalías avisan además directamente al responsable de costos.
- Una anomalía por encima de {{pending: monto o porcentaje}} abre el [playbook de pico de costos](../15-operations/playbooks/cost-spike.md).

## Límites duros

{{pending: decidir dónde se limita el gasto automáticamente (cuotas, límites de tasa) y dónde solo se usan alertas}}

Los límites duros protegen contra costos desbocados, pero pueden causar caídas. Úsalos en no producción, experimentos y endpoints públicos que llaman a APIs de pago; prefiere alertas en rutas de producción de las que dependen los usuarios.

## Higiene

- Cada alerta tiene responsable y una acción documentada.
- Prueba la ruta de alerta una vez bajando un umbral en un entorno de pruebas.
- Elimina las alertas que nadie atiende; sustitúyelas por otras útiles.
- Los datos de facturación suelen llegar con horas de retraso; las cuotas de uso cubren ese hueco.

## Relacionados

- [Estrategia de costos](cost-strategy.md)
- [Gestión de costos de IA](ai-cost-management.md)
- [Playbook de pico de costos](../15-operations/playbooks/cost-spike.md)
- [Plantilla de reporte de costos](templates/cost-report-template.md)
