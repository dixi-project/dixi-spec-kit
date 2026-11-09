# Matriz de SLA

## Propósito

Comparar lo que promete cada proveedor crítico con lo que el proyecto promete a sus propios clientes, y exponer las brechas antes de que se conviertan en un incidente o un problema contractual.

Estado: borrador. {{pending: nombrar al responsable de esta matriz}}

## Compromisos de proveedores

| Proveedor | Servicio | Disponibilidad publicada | Respuesta de soporte | Créditos o compensaciones | Página de estado | Última revisión |
|-----------|----------|--------------------------|----------------------|---------------------------|------------------|-----------------|
| {{pending: proveedor}} | {{pending: servicio usado}} | {{pending: valor de los términos del proveedor}} | {{pending: por severidad}} | {{pending: resumen}} | {{pending: enlace}} | {{pending: fecha}} |

Copia los valores de los términos vigentes del proveedor y anota la fecha; no los estimes.

## Nuestros compromisos

| Servicio | Objetivo de disponibilidad | Objetivo de tiempo de recuperación | Objetivo de punto de recuperación | Respuesta de soporte a clientes |
|----------|----------------------------|------------------------------------|-----------------------------------|---------------------------------|
| {{pending: servicio}} | {{pending: objetivo}} | {{pending: RTO}} | {{pending: RPO}} | {{pending: por prioridad}} |

## Análisis de brechas

Un servicio que depende de varios proveedores en serie no puede estar más disponible que el producto de sus disponibilidades. Solo como ejemplo: dos dependencias al 99,9 % cada una dan como máximo cerca del 99,8 % combinado, antes de contar nuestros propios fallos.

| Nuestro servicio | Depende de | Techo combinado de proveedores | Nuestro objetivo | Brecha | Mitigación |
|------------------|------------|--------------------------------|------------------|--------|------------|
| {{pending: servicio}} | {{pending: proveedores}} | {{pending: calculado}} | {{pending: objetivo}} | {{pending: sí / no}} | {{pending: redundancia, caché, modo degradado, objetivo menor}} |

## Reglas

- Nunca prometas a los clientes un objetivo mayor que el techo combinado de proveedores sin una mitigación.
- Los créditos de servicio rara vez cubren las pérdidas reales; planifica resiliencia, no compensaciones.
- Registra los incidentes reales del proveedor frente a su promesa; los incumplimientos repetidos van a la revisión del proveedor.

## Revisión

Revisa cada {{pending: frecuencia}}, en cada renovación de proveedor y cuando un proveedor cambie sus términos.

## Relacionados

- [Catálogo de proveedores](vendor-catalog.md)
- [Evaluación de riesgo de proveedores](vendor-risk-assessment.md)
- [Catálogo de servicios](../service-catalog.md)
- [Modelo de soporte](../support-model.md)
