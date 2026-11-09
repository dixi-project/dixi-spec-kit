# Reprocesar eventos

## Propósito

Reproducir de forma segura mensajes o eventos que fallaron, se perdieron o se procesaron con un bug, sin crear duplicados ni repetir efectos secundarios.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

## Cuándo aplica

- Se acumularon mensajes en una cola de mensajes fallidos (dead-letter).
- Un consumidor estuvo caído o procesó eventos con un bug durante un periodo conocido.
- Un sistema aguas abajo necesita reconstruir datos a partir del historial de eventos.

## Principios

- Corrige la causa antes de reprocesar; reprocesar sobre el mismo bug solo mueve el problema.
- Los consumidores deben ser idempotentes. {{pending: confirmar qué consumidores son idempotentes y cómo (ID de evento, versión, upsert)}}
- Reprocesar es una acción en producción: una persona la aprueba y la ejecuta; un agente de IA puede ayudar a analizar y preparar la selección.
- Prefiere lotes pequeños con pausas a un solo reproceso grande.

## Roles

- **Responsable del servicio**: decide qué reprocesar y aprueba.
- **Operador**: ejecuta el reproceso y vigila las señales.

## 1. Diagnosticar

1. Identifica la cola, el tópico o el stream afectado y el rango de tiempo.
2. Cuenta los eventos involucrados y revisa una muestra para entender el fallo.
3. Busca mensajes venenosos que siempre fallarán; apártalos.

## 2. Corregir la causa

Despliega la corrección, o confirma que la dependencia volvió, y verifica con un evento en un entorno seguro si es posible.

## 3. Reprocesar

1. Haz una copia o exporta los eventos a reprocesar, conservando sus IDs originales.
2. Ejecuta un piloto de {{pending: número}} eventos y revisa el resultado.
3. Reprocesa el resto en lotes de {{pending: tamaño}}, vigilando tasa de error, latencia y profundidad de la cola.
4. Detente ante el primer error inesperado y vuelve al paso 1.

## 4. Verificar

- Los conteos cuadran: reprocesados igual a seleccionados menos los mensajes venenosos apartados.
- Revisa por muestreo los resultados de negocio (registros creados, notificaciones enviadas una sola vez).
- La cola de fallidos está vacía o solo contiene elementos documentados.

## 5. Después

Registra el rango, los conteos, quién aprobó y el resultado. Añade una alerta o un test que habría detectado el fallo antes.

## Relacionados

- [Restaurar el servicio](restore-service.md)
- [Niveles de incidente](../incident-levels.md)
- [Catálogo de servicios](../service-catalog.md)
- [Plantilla de runbook](../../10-engineering/templates/runbook-template.md)
