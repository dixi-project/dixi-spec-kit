# Matriz RTO y RPO

## Propósito

Registrar, por capacidad de negocio, cuánto tiempo puede estar no disponible (RTO) y cuántos datos recientes se pueden perder (RPO) tras un desastre. Estas metas determinan el costo de la estrategia de recuperación, así que las fija el negocio, no solo ingeniería.

## Definiciones

- **RTO** (objetivo de tiempo de recuperación): tiempo máximo aceptable desde el inicio de la caída hasta el servicio restablecido.
- **RPO** (objetivo de punto de recuperación): ventana máxima aceptable de pérdida de datos, medida hacia atrás desde el momento del fallo.
- **Nivel**: grupo de capacidades que comparten las mismas metas.

## Niveles

| Nivel | Significado | RTO | RPO |
|---|---|---|---|
| 1 | Flujo principal; el negocio se detiene sin él | {{pending: meta}} | {{pending: meta}} |
| 2 | Importante; existen alternativas durante un tiempo | {{pending: meta}} | {{pending: meta}} |
| 3 | Puede esperar a que vuelva la operación normal | {{pending: meta}} | {{pending: meta}} |

Solo como ejemplo, no como recomendación: un nivel 1 con RTO de 4 horas y RPO de 15 minutos suele requerir respaldos continuos y una restauración ensayada.

## Matriz

| Capacidad | Nivel | RTO | RPO | Almacenes de datos | Estrategia de recuperación | Responsable | Última validación |
|---|---|---|---|---|---|---|---|
| {{pending: p. ej. inicio de sesión}} | {{pending: nivel}} | {{pending: meta}} | {{pending: meta}} | {{pending: almacenes}} | {{pending: estrategia}} | {{pending: rol}} | {{pending: fecha}} |
| {{pending: p. ej. pago}} | {{pending: nivel}} | {{pending: meta}} | {{pending: meta}} | {{pending: almacenes}} | {{pending: estrategia}} | {{pending: rol}} | {{pending: fecha}} |
| {{pending: p. ej. reportes}} | {{pending: nivel}} | {{pending: meta}} | {{pending: meta}} | {{pending: almacenes}} | {{pending: estrategia}} | {{pending: rol}} | {{pending: fecha}} |

## Comprobaciones de consistencia

- La frecuencia de respaldo de cada almacén es al menos tan alta como el RPO más exigente que depende de él.
- El tiempo de restauración medido en pruebas está por debajo del RTO; si no, la brecha se registra como riesgo.
- Los compromisos externos (SLAs, contratos) no prometen más de lo que permiten estas metas.

## Revisión

Revisa con las personas responsables del negocio {{pending: frecuencia}} y tras cualquier cambio de arquitectura o de contratos.

## Relacionados

- [Estrategia de recuperación ante desastres](dr-strategy.md)
- [Estrategia de reversión](../rollback-strategy.md)
- [Objetivo](../../01-business/vision.md)
