# Optimización de costos de nube

## Propósito

Dar una lista de verificación repetible para reducir el costo de infraestructura sin dañar la fiabilidad ni el rendimiento, y una forma de registrar qué ahorros se hicieron y por qué.

Estado: borrador. {{pending: nombrar al responsable de la optimización de costos}}

## Enfoque

1. Mira primero las líneas de costo más grandes (ver el [modelo de asignación de costos](cost-allocation-model.md)).
2. Para cada candidato, estima el ahorro con supuestos y fuente, y el riesgo.
3. Haz un cambio a la vez, mide, y consérvalo o revierte.
4. Registra el resultado en la tabla de abajo.

## Lista de verificación

### Cómputo

- [ ] Dimensionamiento: instancias o contenedores ajustados al uso real, no a suposiciones.
- [ ] Autoescalado con mínimos sensatos; no producción escala a cero o se apaga fuera del horario laboral.
- [ ] Precios por compromiso o reserva solo para carga base estable y de largo plazo. {{pending: decidir la política de compromisos}}
- [ ] Capacidad interrumpible para trabajo por lotes tolerante a fallos.

### Almacenamiento

- [ ] Reglas de retención y ciclo de vida para logs, respaldos y objetos.
- [ ] Datos de acceso poco frecuente movidos a clases de almacenamiento más baratas.
- [ ] Volúmenes sin asociar y snapshots antiguos eliminados.

### Red

- [ ] El tráfico entre servicios se queda en la misma zona o región cuando es posible.
- [ ] Rutas de red de pago (gateways, transferencia entre regiones) revisadas para evitar tráfico innecesario.
- [ ] Contenido estático servido a través de una caché o CDN.

### Bases de datos

- [ ] Consultas lentas y frecuentes optimizadas antes de escalar.
- [ ] Réplicas de lectura y capacidad acordes a la carga real.
- [ ] Bases de datos de no producción más pequeñas o pausadas.

### Higiene

- [ ] Cada recurso etiquetado con responsable, entorno y servicio.
- [ ] Recursos huérfanos revisados cada {{pending: frecuencia}}.

## Registro de ahorros

| Fecha | Cambio | Ahorro estimado (supuestos, fuente) | Ahorro medido | Riesgo | Decisión |
|-------|--------|-------------------------------------|---------------|--------|----------|
| {{pending: fecha}} | {{pending: cambio}} | {{pending: estimación}} | {{pending: medido}} | {{pending: riesgo}} | {{pending: conservar / revertir}} |

## No hacer

- Quitar redundancia que protege un objetivo de recuperación solo para ahorrar, sin una decisión explícita.
- Dejar que un agente de IA borre o redimensione recursos de producción; puede listar candidatos para que una persona los revise.

## Relacionados

- [Estrategia de costos](cost-strategy.md)
- [Modelo de asignación de costos](cost-allocation-model.md)
- [Alertas de presupuesto](budget-alerts.md)
- [Playbook de pico de costos](../15-operations/playbooks/cost-spike.md)
