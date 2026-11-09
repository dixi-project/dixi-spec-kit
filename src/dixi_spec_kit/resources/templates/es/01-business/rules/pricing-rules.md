# Reglas de precios

## Propósito

Describir cómo se calculan precios, planes, descuentos, impuestos y límites, para que la lógica de
facturación pueda especificarse y probarse sin adivinar. Los precios cambian a menudo y tienen
impacto económico y legal directo: mantén cada regla explícita, versionada y con una persona
responsable que pueda aprobar cambios.

## Modelo de precios

- Modelo: {{pending: gratuito, pago único, suscripción, por uso, por tramos o híbrido}}
- Moneda o monedas: {{pending: monedas y quién asume el riesgo de tipo de cambio}}
- Periodo de facturación: {{pending: mensual, anual, por transacción}}
- Impuestos: {{pending: si los precios incluyen impuestos y quién determina el tipo aplicable}}

## Planes

| Plan | Precio | Límites incluidos | Funcionalidades | Quién puede contratarlo |
|---|---|---|---|---|
| {{pending: plan}} | {{pending: precio}} | {{pending: límites}} | {{pending: funcionalidades}} | {{pending: segmento}} |

## Reglas

| ID | Regla | Ejemplo | Responsable |
|---|---|---|---|
| PR-001 | {{pending: p. ej. cómo funciona el prorrateo al mejorar de plan}} | {{pending: ejemplo resuelto con cifras}} | {{pending: rol}} |
| PR-002 | {{pending: p. ej. qué ocurre al superar un límite}} | {{pending: ejemplo resuelto}} | {{pending: rol}} |
| PR-003 | {{pending: p. ej. cómo se combinan los descuentos}} | {{pending: ejemplo resuelto}} | {{pending: rol}} |

## Convenciones de cálculo

- Redondeo: {{pending: modo de redondeo y en qué paso se aplica}}
- Precisión: guarda importes como enteros en la unidad mínima o como decimales exactos, nunca como
  coma flotante.
- Fechas de efecto: un cambio de precio aplica desde {{pending: cuándo}} y no altera facturas pasadas.
- Precios heredados: {{pending: si los clientes actuales conservan precios antiguos y durante cuánto}}

## Casos límite a especificar

- Pruebas gratuitas, reembolsos, cancelaciones a mitad de periodo y pagos fallidos.
- Cuentas gratuitas o internas y cómo se excluyen de los informes de ingresos.
- Cambios de plan entre monedas o regiones fiscales.

## Control de cambios

- Quién aprueba cambios de precios: {{pending: rol}}
- Plazo de aviso a clientes: {{pending: duración y canal}}

## Relacionados

- [Reglas de negocio](business-rules.md)
- [Propuesta de valor](../value-proposition.md)
- [Objetivos estratégicos](../strategic-goals.md)
