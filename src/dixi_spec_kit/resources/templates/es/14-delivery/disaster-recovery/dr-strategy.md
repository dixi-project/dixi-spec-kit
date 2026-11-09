# Estrategia de recuperación ante desastres

## Propósito

Decidir cómo se recupera el sistema tras perder un componente, una ubicación o un servicio de un proveedor por completo, y cuánto tiempo fuera de servicio y pérdida de datos acepta el negocio. Los fallos del día a día se resuelven con reversiones y runbooks; este documento cubre los eventos raros y graves.

## Escenarios

| Escenario | Ejemplo | Probabilidad | Impacto | Cubierto por |
|---|---|---|---|---|
| Corrupción o borrado de datos | Migración defectuosa, error humano | {{pending: valoración}} | {{pending: valoración}} | Restauración a un punto en el tiempo |
| Pérdida de la ubicación principal | Caída regional del alojamiento | {{pending: valoración}} | {{pending: valoración}} | {{pending: estrategia}} |
| Credenciales comprometidas | Un atacante borra recursos | {{pending: valoración}} | {{pending: valoración}} | Respaldos aislados, respuesta a incidentes |
| Pérdida de un tercero crítico | Servicio de pagos o de identidad caído | {{pending: valoración}} | {{pending: valoración}} | {{pending: alternativa o modo degradado}} |

## Estrategias de recuperación

| Estrategia | Descripción | Costo típico | Tiempo de recuperación típico |
|---|---|---|---|
| Respaldo y restauración | Reconstruir desde código y restaurar datos | Bajo | Horas |
| Pilot light | Copia mínima de datos y servicios clave lista en otro lugar | Medio | Decenas de minutos a horas |
| Warm standby | Copia completa reducida corriendo en otro lugar | Alto | Minutos |
| Activo/activo | Capacidad completa en más de una ubicación | El más alto | Cercano a cero |

Los tiempos de recuperación anteriores son órdenes de magnitud aproximados, no compromisos.

Estrategia elegida: {{pending: por nivel, alineada con la matriz RTO/RPO y registrada en un ADR}}

## Requisitos previos

- La infraestructura se puede recrear desde código versionado.
- Los respaldos se guardan fuera de la ubicación principal y fuera del alcance de las credenciales de producción.
- Los secretos y llaves necesarios para recuperar están disponibles desde una segunda ubicación.
- La lista de contactos y los derechos de decisión están escritos: {{pending: quién declara un desastre}}.

## Ejercicios

| Ejercicio | Frecuencia | Última ejecución | Resultado |
|---|---|---|---|
| Simulacro de mesa | {{pending: frecuencia}} | {{pending: fecha}} | {{pending: resultado}} |
| Prueba de restauración | {{pending: frecuencia}} | {{pending: fecha}} | {{pending: resultado}} |

Registra solo ejercicios realizados de verdad.

## Relacionados

- [Matriz RTO y RPO](rto-rpo-matrix.md)
- [Estrategia de reversión](../rollback-strategy.md)
- [Entornos](../environments.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Proyecto](../../00-master-spec.md)
