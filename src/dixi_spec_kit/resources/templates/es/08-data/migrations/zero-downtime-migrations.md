# Migraciones sin indisponibilidad

## Propósito

Describir cómo cambiar esquemas y datos mientras el sistema sigue atendiendo tráfico. Aplica cuando no se aceptan ventanas de mantenimiento y se apoya en la [estrategia de migraciones](migration-strategy.md).

- Objetivo de disponibilidad que lo exige: {{pending: objetivo de disponibilidad y degradación aceptable durante migraciones}}

## Regla de compatibilidad

En todo momento, las versiones de la aplicación en ejecución (antigua y nueva, durante un despliegue gradual) deben funcionar con el esquema actual. Por tanto:

- Los cambios de esquema son compatibles con la versión anterior de la aplicación.
- Los cambios de aplicación son compatibles con el esquema anterior y con el siguiente.

## Matriz de cambios

| Cambio | Riesgo de bloqueo | Técnica sin indisponibilidad |
| --- | --- | --- |
| Añadir columna con valor por defecto | Reescritura de tabla en algunos motores | Añadir nulable, default para filas nuevas, relleno por lotes |
| Añadir restricción obligatoria | Recorrido completo con bloqueo | Añadir check sin validar, rellenar, validar aparte |
| Añadir clave foránea | Bloqueo en ambas tablas | Añadir sin validar, validar después |
| Crear índice | Escrituras bloqueadas | Creación de índice no bloqueante si existe |
| Renombrar columna o tabla | Rompe la versión antigua | Expandir y contraer con doble escritura |
| Dividir o unir tablas | Rompe a los lectores | Estructura nueva, doble escritura, lecturas en sombra, cambio, retiro |

## Técnicas a nivel de aplicación

- **Feature flags**: cambiar lecturas y escrituras a la estructura nueva sin desplegar, y volver atrás rápido.
- **Doble escritura**: escribir en la estructura antigua y en la nueva; decidir cuál manda y cómo se detecta la divergencia.
- **Lecturas en sombra**: leer de ambas, servir el resultado antiguo, comparar y registrar diferencias hasta llegar a cero.
- **Captura de cambios**: transmitir cambios del origen al destino cuando la doble escritura en código no es práctica.

## Despliegue multi-tenant

| Enfoque | Descripción | Decisión |
| --- | --- | --- |
| Por tenant | Migrar tenants en oleadas, empezando por los internos o de bajo riesgo | {{pending: elegir enfoque}} |
| Todos a la vez | Un cambio para todos, solo para cambios pequeños y seguros | |

## Antipatrones

- Renombrar en el sitio en un único despliegue.
- Transacciones largas que mantienen bloqueos durante un relleno.
- Eliminar la estructura antigua en la misma versión que deja de usarla.
- Rellenos sin limitación de ritmo durante el tráfico pico.

## Checklist por cambio de esquema

- [ ] Se conoce el comportamiento de bloqueo de cada sentencia en el motor elegido.
- [ ] Hay timeouts de sentencia y de bloqueo configurados para la sesión de migración.
- [ ] Ambas versiones de la aplicación se probaron contra el esquema nuevo.
- [ ] El relleno es por lotes, idempotente y reanudable (ver el [playbook de migración de datos](data-migration-playbook.md)).
- [ ] Están definidas las métricas a vigilar y los criterios para abortar.
- [ ] La fase de contracción está programada y tiene responsable.

## Relacionados

- [Estrategia de migraciones](migration-strategy.md)
- [Playbook de migración de datos](data-migration-playbook.md)
- [Arquitectura de datos](../data-architecture.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
