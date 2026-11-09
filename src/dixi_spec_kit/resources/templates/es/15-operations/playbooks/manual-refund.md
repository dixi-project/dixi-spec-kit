# Reembolso manual

## Propósito

Devolver dinero a un cliente fuera del flujo automático de forma controlada y trazable, con las aprobaciones correctas y sin reembolsos duplicados.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

## Cuándo aplica

- Un cargo no pudo revertirse automáticamente.
- Un incidente provocó cargos erróneos a uno o muchos clientes.
- Un acuerdo de soporte o una decisión de cortesía concede un reembolso.

## Reglas

- Los reembolsos vuelven al medio de pago original salvo que la política diga otra cosa. {{pending: definir excepciones}}
- Cada reembolso tiene un código de motivo y un enlace al ticket o incidente.
- Límites de aprobación: {{pending: monto}} líder de soporte; por encima, contacto de finanzas.
- Quien solicita un reembolso no es quien lo aprueba.
- Un agente de IA puede preparar la lista y la evidencia; una persona aprueba y ejecuta.

## Reembolso individual

1. Revisa el cargo original, lo ya reembolsado y el estado de la cuenta del cliente.
2. Confirma el motivo y el monto con el responsable del ticket.
3. Obtén la aprobación según los límites anteriores.
4. Emite el reembolso en la herramienta de pagos. {{pending: nombrar el rol de la herramienta, no el proveedor}}
5. Registra el ID del reembolso, monto, motivo y quién aprobó.
6. Avisa al cliente con el plazo esperado de llegada.

## Reembolso por lote (tras un incidente)

1. Construye la lista de cargos afectados desde logs o la base de datos con una consulta revisada y de solo lectura.
2. Pide a una segunda persona que revise la lista: totales, duplicados, elementos ya reembolsados.
3. Haz un piloto de {{pending: número}} reembolsos y verifícalos.
4. Ejecuta el resto en lotes pequeños, deteniéndote ante el primer error inesperado.
5. Concilia: total reembolsado igual a total aprobado.

## Criterios de cierre

- Todos los reembolsos aprobados emitidos y conciliados.
- Clientes avisados.
- Contabilidad informada del total y del motivo. {{pending: cómo se informa a contabilidad}}

## Relacionados

- [Modelo de soporte](../support-model.md)
- [Niveles de incidente](../incident-levels.md)
- [Comunicación de caída a clientes](comms-outage-customer.md)
- [Matriz RACI](../team/raci-matrix.md)
