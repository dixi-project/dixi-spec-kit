# Arquitectura de datos

## Propósito

Describir dónde viven los datos del proyecto, cómo se mueven y quién es dueño de cada parte. Es el mapa al que se refieren el modelo canónico, el ERD y los documentos de migración.

- Responsable: {{pending: persona o rol responsable de la arquitectura de datos}}

## Almacenes de datos

| Almacén | Tipo (relacional, documental, clave-valor, búsqueda, objetos, cola) | Finalidad | Módulo dueño | Clasificación máxima |
| --- | --- | --- | --- | --- |
| {{pending: almacén principal}} | | Sistema de registro | | |
| | | Caché | | |
| | | Índice de búsqueda | | |
| | | Archivos y medios | | |

Elige el tipo de almacén por patrón de acceso, no por costumbre. Registra la elección en una decisión de arquitectura.

## Reglas de propiedad

- [ ] Cada entidad tiene exactamente un módulo dueño que la escribe.
- [ ] Los demás módulos leen mediante contratos (API, eventos), no accediendo directamente a tablas.
- [ ] Los almacenes derivados (cachés, índices, informes) pueden reconstruirse desde el sistema de registro.
- [ ] Los joins entre módulos en la base de datos se evitan o se aprueban explícitamente.

## Flujos de datos

| Flujo | Origen | Destino | Mecanismo (llamada síncrona, evento, lote, CDC) | Frecuencia | Consistencia |
| --- | --- | --- | --- | --- | --- |
| | | | | | {{pending: fuerte o eventual}} |

## Multi-tenancy

{{pending: modelo de tenancy, por ejemplo single tenant, esquema compartido con columna de tenant, esquema por tenant o base de datos por tenant}}

- El aislamiento se aplica en: {{pending: capa de aplicación, políticas de base de datos o ambas}}
- Toda consulta sobre datos de tenant filtra por tenant; las pruebas cubren el acceso cruzado entre tenants.

## Consistencia y transacciones

- Las transacciones quedan dentro de un único módulo dueño.
- Los flujos entre módulos usan eventos o sagas con acciones compensatorias.
- Las claves de idempotencia protegen las operaciones que pueden reintentarse.

## Copias de seguridad y recuperación

| Almacén | Frecuencia de copia | Objetivo de punto de recuperación | Objetivo de tiempo de recuperación | Restauración probada |
| --- | --- | --- | --- | --- |
| | {{pending: frecuencia}} | | | {{pending: fecha del último ejercicio de restauración}} |

## Tamaño y crecimiento

| Almacén | Tamaño actual | Crecimiento esperado | Plan de particionado o archivo |
| --- | --- | --- | --- |
| | | | |

## Relacionados

- [Modelo de datos canónico](canonical-data-model.md)
- [Vista general del ERD](models/erd-overview.md)
- [Estrategia de migraciones](migrations/migration-strategy.md)
- [Clasificación de datos personales](pii-classification.md)
- [Política de retención](retention-policy.md)
- [Estándar de campos de auditoría](audit-fields-standard.md)
