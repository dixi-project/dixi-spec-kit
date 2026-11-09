# Arquitectura de resiliencia

## Propósito

Describir cómo el sistema sigue funcionando, se degrada de forma controlada o se recupera cuando fallan partes de él. Fija los objetivos de disponibilidad y recuperación y los patrones usados para alcanzarlos. Los objetivos son metas de diseño, no resultados medidos.

## Objetivos

| Objetivo | Meta | Notas |
|---|---|---|
| Disponibilidad | {{pending: p. ej. porcentaje mensual}} | Acordada con la persona responsable de negocio |
| Tiempo objetivo de recuperación (RTO) | {{pending: duración}} | Tiempo máximo para restaurar el servicio |
| Punto objetivo de recuperación (RPO) | {{pending: duración}} | Pérdida de datos máxima aceptable |

## Modos de fallo

| Fallo | Impacto | Detección | Respuesta |
|---|---|---|---|
| Caída de una instancia de aplicación | {{pending: impacto}} | Health check | Reiniciar y enrutar a instancias sanas |
| Almacén de datos no disponible | {{pending: impacto}} | {{pending: señal}} | {{pending: conmutación o modo solo lectura}} |
| Dependencia externa lenta | {{pending: impacto}} | Alerta de latencia | Timeout, circuit breaker, alternativa |
| Despliegue defectuoso | {{pending: impacto}} | Alerta de tasa de errores | Reversión |

## Patrones

- **Timeouts** en toda llamada remota: {{pending: valores por defecto}}.
- **Reintentos** con backoff exponencial y jitter, solo para operaciones idempotentes.
- **Circuit breakers** alrededor de dependencias inestables: {{pending: cuáles}}.
- **Bulkheads**: aislar recursos para que una funcionalidad que falla no agote al resto.
- **Degradación controlada**: {{pending: qué funcionalidades pueden desactivarse}}.
- **Idempotencia** en operaciones que pueden repetirse por reintentos o por las personas usuarias.

## Copias de seguridad y restauración

- Qué se respalda: {{pending: almacenes de datos, archivos, configuración}}
- Frecuencia y retención: {{pending: calendario}}
- Procedimiento de restauración: {{pending: enlace o pasos}}
- Simulacros de restauración: {{pending: cadencia prevista}}

## Observabilidad para la resiliencia

- Endpoints de salud: {{pending: liveness y readiness}}
- Alertas clave: {{pending: tasa de errores, saturación, profundidad de colas}}
- Guardia o escalado: {{pending: quién responde}}

## Relacionados

- [Arquitectura de despliegue](deployment-architecture.md)
- [Arquitectura de integración](integration-architecture.md)
- [Arquitectura de rendimiento](performance-architecture.md)
- [Decisiones de arquitectura](adr/README.md)
- [Plan de pruebas](../11-quality/test-plan.md)
