# Playbook de migración de datos

## Propósito

Guiar el movimiento o la transformación de datos existentes: rellenos, traslados entre almacenes, importaciones desde sistemas heredados y reestructuraciones. Complementa la [estrategia de migraciones](migration-strategy.md), que cubre los cambios de esquema.

## Preparación

- [ ] Origen y destino identificados, con responsables.
- [ ] Volumen medido: filas, tamaño, crecimiento durante la ventana de migración.
- [ ] Calidad de datos perfilada: nulos, duplicados, valores inválidos, referencias huérfanas.
- [ ] Mapeo documentado campo a campo, con transformaciones y valores por defecto.
- [ ] Datos personales identificados según la [clasificación de datos personales](../pii-classification.md).
- [ ] Camino de reversión definido antes de empezar.
- [ ] Partes interesadas informadas de la ventana y del impacto esperado.

## Elección del patrón

| Patrón | Cuándo encaja | Riesgo principal |
| --- | --- | --- |
| Copia masiva única | Pocos datos, se acepta una ventana de mantenimiento | Indisponibilidad |
| Copia masiva más relleno de cambios | Datos medianos, se acepta una congelación breve | Cambios perdidos |
| Doble escritura más relleno | El origen sigue activo durante el traslado | Divergencia entre copias |
| Captura continua de cambios | Datos grandes o muy activos | Complejidad operativa |

Patrón elegido: {{pending: patrón y motivo}}

## Lotes e idempotencia

- Procesar por lotes según una clave estable; registrar la última clave procesada para reanudar.
- Limitar el ritmo para proteger el tráfico real: {{pending: tamaño de lote y pausa entre lotes}}
- Cada lote es idempotente: ejecutarlo dos veces da el mismo resultado (upsert, no insert).
- Los fallos de un lote se registran y se reintentan sin detener toda la ejecución.

## Observabilidad durante la ejecución

| Señal | Umbral que pausa la ejecución |
| --- | --- |
| Filas procesadas por minuto | |
| Tasa de errores | |
| Latencia de origen y destino | |
| Retraso de replicación | |

## Verificación

- [ ] Los conteos de filas coinciden entre origen y destino, por partición o tenant.
- [ ] Checksums o hashes coinciden en las columnas clave.
- [ ] Una muestra aleatoria se compara campo a campo.
- [ ] Los totales de negocio (por ejemplo sumas de importes) coinciden.
- [ ] La conciliación sigue en marcha hasta retirar el origen.

## Reversión

- Durante la ejecución: detener, mantener el origen como sistema de registro, descartar o marcar los datos parciales.
- Tras el cambio: {{pending: cómo volver atrás y cuánto tiempo se conserva el origen}}

## Plantilla de plan

| Elemento | Valor |
| --- | --- |
| Origen a destino | |
| Volumen | |
| Patrón | |
| Ventana y hora de cambio | |
| Pasos de verificación | |
| Pasos de reversión | |
| Responsable y aprobador | |

Las copias antiguas creadas para la migración siguen la [política de retención](../retention-policy.md).

## Relacionados

- [Estrategia de migraciones](migration-strategy.md)
- [Clasificación de datos personales](../pii-classification.md)
- [Política de retención](../retention-policy.md)
- [Arquitectura de datos](../data-architecture.md)
