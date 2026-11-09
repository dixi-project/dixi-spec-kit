# Workers y colas

## Propósito

Describir el procesamiento asíncrono del sistema: qué colas existen, quién publica y consume, cómo se manejan fallos y reintentos y cómo se despliegan y escalan los workers.

## Decisiones

- Tecnología de mensajería: {{pending: decidir y registrar en un ADR}}
- Garantía de entrega asumida: {{pending: «al menos una vez» es lo habitual}}
- Formato de mensaje y ubicación del esquema: {{pending: decidir}}

## Inventario de colas

| Cola | Publica | Consume | Mensaje | Orden | Reintentos | Cola de mensajes muertos | Responsable |
|---|---|---|---|---|---|---|---|
| {{pending: nombre de la cola}} | {{pending: componente}} | {{pending: worker}} | {{pending: evento o comando}} | {{pending: requerido o no}} | {{pending: número y espera}} | {{pending: nombre}} | {{pending: rol}} |

## Reglas para consumidores

- Los consumidores son idempotentes; usa un identificador de mensaje para descartar duplicados.
- Confirma un mensaje solo después de que su trabajo quede guardado.
- Reintenta errores transitorios con espera exponencial y un máximo; envía los errores permanentes a la cola de mensajes muertos.
- Propaga el contexto de traza desde las cabeceras del mensaje.
- Nunca pongas secretos ni datos personales innecesarios en el cuerpo de los mensajes.

## Mensajes muertos

- Alerta cuando la cola de mensajes muertos recibe mensajes: {{pending: umbral}}.
- Los mensajes se inspeccionan, se corrigen y se reprocesan con un procedimiento documentado, nunca se borran sin registro.
- Retención en la cola de mensajes muertos: {{pending: días}}.

## Despliegue y escalado

- Los workers usan despliegue rolling; al apagarse dejan de tomar mensajes nuevos y terminan el actual en {{pending: segundos}}.
- Durante una versión, workers viejos y nuevos consumen la nueva versión del mensaje.
- Señal de escalado: {{pending: tamaño de la acumulación, antigüedad del mensaje más viejo o CPU}}; límites: {{pending: mínimo y máximo de workers}}.

## Monitoreo

- Acumulación, antigüedad del mensaje más viejo, duración de procesamiento, fallos y mensajes muertos, según el catálogo de métricas.
- Salta una alerta cuando la acumulación crece durante {{pending: minutos}}.

## Relacionados

- [Tareas programadas](cron-jobs.md)
- [Arquitectura de eventos](../09-architecture/event-architecture.md)
- [Estándar de diseño de eventos](../10-engineering/event-design-standard.md)
- [Estrategia de trazas](../12-observability/tracing-strategy.md)
- [Runbooks](../12-observability/runbooks/README.md)
