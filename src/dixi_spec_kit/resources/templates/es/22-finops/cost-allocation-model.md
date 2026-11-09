# Modelo de asignación de costos

## Propósito

Atribuir cada costo a un producto, servicio, entorno y, cuando corresponda, a un tenant, para conocer los costos unitarios y basar en datos las decisiones de precio y optimización.

Estado: borrador. {{pending: nombrar al responsable del modelo de asignación}}

## Esquema de etiquetas

Todo recurso que admita etiquetas debe llevar estas claves:

| Clave | Valor de ejemplo | Obligatoria |
|-------|------------------|-------------|
| `project` | {{pending: nombre corto del proyecto}} | Sí |
| `environment` | `prod`, `staging`, `dev` | Sí |
| `service` | {{pending: nombre del servicio según el catálogo de servicios}} | Sí |
| `owner` | {{pending: equipo o rol}} | Sí |
| `tenant` | {{pending: ID del tenant, cuando es dedicado}} | Cuando aplique |
| `cost-center` | {{pending: código de finanzas}} | {{pending: sí / no}} |

Usa claves en minúsculas y valores de una lista fija. Los recursos sin etiquetar se reportan cada {{pending: frecuencia}} y se corrigen o eliminan.

## Separación de cuentas y entornos

{{pending: decidir si los entornos viven en cuentas o proyectos separados, o solo separados por etiquetas}}

Las cuentas separadas por entorno simplifican la asignación y el control de acceso; las etiquetas solas son más fáciles al empezar, pero dejan más huecos.

## Costos compartidos

Algunos costos no se pueden etiquetar (planes de soporte, red compartida, observabilidad). Asígnalos con una regla documentada:

| Costo compartido | Regla de asignación |
|------------------|---------------------|
| {{pending: p. ej. clúster compartido}} | {{pending: p. ej. por CPU solicitada por servicio}} |
| {{pending: p. ej. monitoreo}} | {{pending: p. ej. a partes iguales por servicio}} |

## Costos unitarios

| Unidad | Fórmula | Objetivo |
|--------|---------|----------|
| Costo por usuario activo | Costo de producción / usuarios activos mensuales | {{pending: objetivo}} |
| Costo por tenant | Costo dedicado + parte del costo compartido | {{pending: objetivo}} |
| Costo por funcionalidad | Costo de sus servicios y uso de IA | {{pending: objetivo}} |

## Showback y chargeback

- **Showback**: cada equipo o tenant ve su costo; no se mueve dinero. Primer paso recomendado.
- **Chargeback**: el costo se factura internamente o al cliente. {{pending: decidir si y cuándo pasar a chargeback}}

## Reportes

Los resultados mensuales de asignación alimentan el reporte de costos. Guarda en el repositorio las consultas o scripts que los producen para que las cifras se puedan reproducir.

## Relacionados

- [Estrategia de costos](cost-strategy.md)
- [Optimización de costos de nube](cloud-cost-optimization.md)
- [Plantilla de reporte de costos](templates/cost-report-template.md)
- [Alta de tenants](../15-operations/playbooks/tenant-onboarding.md)
- [Catálogo de servicios](../15-operations/service-catalog.md)
