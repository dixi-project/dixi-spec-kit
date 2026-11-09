# Estándar de observabilidad

## Propósito

Definir los logs, métricas, trazas y alertas mínimos que cada servicio del proyecto debe producir, para que el sistema detecte los fallos antes de que los reporten los usuarios y se puedan diagnosticar sin adivinar.

Estado: borrador. {{pending: confirmar la persona responsable de observabilidad}}

## Reglas mínimas

- [ ] Los logs son estructurados, con marca de tiempo, nivel, servicio, entorno e ID de correlación.
- [ ] Sin secretos ni datos personales en logs, métricas ni atributos de trazas.
- [ ] Cada petición lleva un ID de correlación entre servicios.
- [ ] Cada servicio expone una verificación de salud.
- [ ] Cada recorrido de usuario tiene al menos un indicador de nivel de servicio.
- [ ] Cada alerta tiene responsable y runbook.

## Señales

| Señal | Contenido mínimo | Retención |
|-------|------------------|-----------|
| Logs | Errores, eventos de seguridad, eventos clave de negocio | {{pending: retención}} |
| Métricas | Tasa de peticiones, tasa de errores, latencia, saturación | {{pending: retención}} |
| Trazas | Peticiones entre servicios, llamadas externas | {{pending: retención}} |
| Eventos de auditoría | Quién hizo qué, cuándo y sobre qué recurso | {{pending: retención}} |

## Niveles de servicio

| Recorrido | Indicador | Objetivo | Ventana |
|-----------|-----------|----------|---------|
| {{pending: p. ej. iniciar sesión}} | {{pending: tasa de éxito}} | {{pending: meta}} | {{pending: ventana}} |

## Alertas

- Alerta por los síntomas que nota el usuario (errores, latencia), no solo por las causas.
- Toda alerta debe ser accionable; elimina las alertas que nadie atiende.
- La severidad corresponde a los niveles de la [política de incidentes](policies/incident-policy.md).
- Cada alerta enlaza a un runbook basado en la [plantilla de runbook](../10-engineering/templates/runbook-template.md).

## Niveles de log

| Nivel | Uso |
|-------|-----|
| ERROR | Una petición o tarea falló y requiere atención. |
| WARN | Inesperado pero gestionado; puede requerir seguimiento. |
| INFO | Eventos clave de ciclo de vida y de negocio. |
| DEBUG | Detalle de diagnóstico; desactivado en producción por defecto. |

## Herramientas

{{pending: elegir cómo se recogen, almacenan y visualizan las señales}}

## Relacionados

- [Estándar de logging](../10-engineering/logging-standard.md)
- [Estrategia de entornos](environment-strategy.md)
- [Estándar de gestión de releases](release-management-standard.md)
- [Base de seguridad](security-baseline.md)
