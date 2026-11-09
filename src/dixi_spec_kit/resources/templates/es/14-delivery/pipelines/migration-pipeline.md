# Pipeline de migraciones

## Propósito

Describir cómo se aplican las migraciones de esquema y de datos de forma segura, en orden y con camino de vuelta. Las migraciones corren como parte de una versión, nunca a mano contra producción.

## Reglas

- Las migraciones son archivos versionados en el repositorio, aplicados en orden y registrados en la base de datos.
- Cada migración es compatible con la versión que está corriendo (expandir, migrar, contraer).
- Los pasos destructivos (borrar columna, borrar tabla) van en una versión posterior, cuando ningún código use ya la estructura vieja.
- Los rellenos de datos grandes corren por lotes y se pueden pausar y reanudar.
- Ninguna migración contiene secretos ni datos personales reales.

## Pasos

| # | Paso | Acción | Compuerta |
|---|---|---|---|
| 1 | Verificar | `make verify` y pruebas de migración sobre una base de datos nueva | Todo pasa |
| 2 | Ensayo | Aplicar sobre una copia con un volumen realista de datos sintéticos | Termina en {{pending: minutos}} |
| 3 | Punto de respaldo | Confirmar que existe un respaldo o snapshot reciente | Respaldo de menos de {{pending: horas}} |
| 4 | Staging | Aplicar en staging | Termina bien; aplicación sana |
| 5 | Aprobación | Incluida en la aprobación de la versión a producción | **Aprobación humana registrada** |
| 6 | Producción | Aplicar en producción con un tiempo límite de bloqueo de {{pending: segundos}} | Termina bien; aplicación sana |

## Bloqueos y horarios

- Fija un tiempo límite de bloqueo para que una migración falle rápido en lugar de bloquear el tráfico.
- Crea índices sin bloquear escrituras cuando la base de datos lo permita.
- Las migraciones largas corren en {{pending: ventana de poco tráfico}}.

## Reversión

- Cada migración indica si se puede revertir y cómo.
- Las migraciones irreversibles requieren un plan de restauración escrito antes de la aprobación.
- Prefiere revertir la aplicación manteniendo el esquema expandido antes que revertir una migración.

## Decisiones

- Herramienta de migraciones: {{pending: decidir y registrar en un ADR}}
- Quién puede ejecutar una migración manual en una emergencia: {{pending: roles y proceso de acceso de emergencia}}

## Relacionados

- [Estrategia de migraciones](../../08-data/migrations/migration-strategy.md)
- [Guía de migración de datos](../../08-data/migrations/data-migration-playbook.md)
- [Pipeline de versión](release-pipeline.md)
- [Respaldo y recuperación](../backup-and-recovery.md)
