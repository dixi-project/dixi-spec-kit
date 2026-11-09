# Lista 08 — Finanzas (tecnología)

> **Regla de evidencia.** Puntúa solo lo que prueba un artefacto. Un artefacto ausente se anota como «sin evidencia» y vale 0; nunca se rellena con un supuesto presentado como hecho. No estimes cifras para rellenar huecos; tómalas de exportaciones de facturación o registros contables.

## Propósito

Evaluar la parte tecnológica de las finanzas: cuánto cuesta operar el producto, cómo escala ese coste con el uso, qué compromisos existen y si el gasto es visible y está controlado. Las finanzas corporativas quedan fuera salvo que el tipo de DD lo exija.

Estado: borrador. {{pending: decidir qué datos de coste pueden compartirse y con qué detalle}}

## Insumos

- [Estrategia de costes](../../22-finops/cost-strategy.md)
- [Alertas de presupuesto](../../22-finops/budget-alerts.md)
- [Gestión de costes de IA](../../22-finops/ai-cost-management.md), si hay funciones de IA
- [Plantilla de informe de costes](../../22-finops/templates/cost-report-template.md)
- [Reglas de precios](../../01-business/rules/pricing-rules.md) y [Objetivos estratégicos](../../01-business/strategic-goals.md)
- [Catálogo de proveedores](../../15-operations/vendor-management/vendor-catalog.md)

## Elementos

| ID | Pregunta | Evidencia (artefacto) | Puntuación 0–5 | Hallazgo |
|----|----------|-----------------------|----------------|----------|
| FIN-01 | ¿Se conoce el coste mensual de operación por entorno y componente principal? | {{pending: enlace a la exportación de facturación}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-02 | ¿Se conoce el coste unitario (por cliente, transacción o usuario activo)? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-03 | ¿El coste escala de forma predecible con el uso y está modelado? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-04 | ¿Hay presupuestos y alertas, y se actuó sobre alertas pasadas? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-05 | ¿Los compromisos a largo plazo y licencias están listados con fechas de renovación? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-06 | ¿Los costes por uso (p. ej. modelos de IA, mensajería) tienen límite o vigilancia? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-07 | ¿Hay un responsable de costes que revisa el gasto con calendario? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |
| FIN-08 | ¿El coste de la deuda técnica conocida o de la remediación está estimado con un método declarado? | {{pending: enlace}} | {{pending: puntuación}} | {{pending: hallazgo}} |

## Señales de alarma

- Nadie puede indicar el coste mensual actual a partir de registros.
- Gasto por uso sin límite y sin alerta.
- Servicios críticos pagados con cuentas o tarjetas personales.

## Resultado

- Puntuación del área: {{pending: puntuación y método}}
- Hallazgos trasladados al [Informe de DD](../dd-report-template.md).

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Lista 07 — Equipo](07-team.md)
- [Lista 09 — Proveedores y socios](09-vendors-partners.md)
- [Lista final](11-final-report.md)
