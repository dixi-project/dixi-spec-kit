# Estrategia de observabilidad

## Propósito

Explicar cómo sabrá el equipo qué hace el sistema en producción: qué señales se recogen, cómo se correlacionan y quién las mira. Este documento fija las reglas; los catálogos de esta área guardan el detalle.

## Señales

| Señal | Responde | Detalle en |
|---|---|---|
| Métricas | ¿Está sano? ¿Cuánto, qué tan rápido? | [Catálogo de métricas](metrics-catalog.md) |
| Logs | ¿Qué pasó en este evento concreto? | [Mapa de logs](logging-map.md) |
| Trazas | ¿Dónde se fue el tiempo entre componentes? | Estrategia de trazas (perfil platform) |
| Chequeos de salud | ¿Está arriba ahora mismo? | [Reglas de alertas](alerting-rules.md) |

## Decisiones

- Estándar de instrumentación: {{pending: preferir un estándar abierto y neutral; registrar en un ADR}}
- Backend de telemetría: {{pending: decidir y registrar en un ADR}}
- Retención por señal: {{pending: días para métricas, logs y trazas}}
- Política de muestreo: {{pending: qué proporción de trazas se guarda y cuáles siempre}}
- Presupuesto de telemetría: {{pending: límite mensual y quién lo vigila}}

## Atributos obligatorios

Toda señal lleva los mismos atributos de identificación para poder unirlas:

- `service.name`: el componente que la emite.
- `service.version`: el identificador del commit del build desplegado.
- `deployment.environment`: local, staging o production.
- Un identificador de correlación o de traza propagado entre llamadas y colas.

## Endpoints que expone cada servicio

- Un endpoint de salud que responde rápido y no depende de dependencias lentas.
- Un endpoint de versión que devuelve el mismo identificador de commit que `service.version`.

## Reglas

- Sin secretos, tokens ni datos personales en ninguna señal; enmascara antes de emitir.
- Instrumenta primero el flujo principal de negocio y después el resto.
- Tableros y alertas se versionan junto al código cuando la herramienta lo permite.
- Cada servicio nuevo completa la lista siguiente antes de llegar a producción.

## Lista para un servicio nuevo

- [ ] Atributos obligatorios presentes en métricas, logs y trazas
- [ ] Endpoints de salud y versión expuestos
- [ ] Logs estructurados con identificador de correlación
- [ ] Métricas de tasa, errores y duración en sus puntos de entrada
- [ ] Al menos un indicador en [SLIs, SLOs y SLAs](slis-slos-slas.md)
- [ ] Alertas con runbook, según las [reglas de alertas](alerting-rules.md)
- [ ] Una entrada en el [mapa de tableros](dashboard-map.md)

## Relacionados

- [Runbooks](runbooks/README.md)
- [Estándar de logging](../10-engineering/logging-standard.md)
- [Requisitos no funcionales](../11-quality/non-functional-requirements.md)
- [Verificación continua](../14-delivery/continuous-verification.md)
- [Proyecto](../00-master-spec.md)
