# Modelo de datos canónico

## Propósito

Definir las entidades de negocio compartidas, su significado y su representación canónica, para que módulos, contratos e informes usen los mismos nombres y la misma semántica. El modelo canónico es el vocabulario; cada módulo puede almacenar los datos a su manera, pero traduce a este modelo en sus fronteras.

- Responsable: {{pending: persona o rol responsable del modelo canónico}}

## Entidades

| Entidad | Definición (una frase) | Módulo dueño | Identificador | Estados del ciclo de vida |
| --- | --- | --- | --- | --- |
| {{pending: entidad principal}} | | | | |
| | | | | |

Las definiciones usan el lenguaje de negocio de las specs de dominio, no términos técnicos.

## Convenciones de atributos

| Aspecto | Convención |
| --- | --- |
| Identificadores | {{pending: formato, por ejemplo UUID, ULID o cadena con prefijo}} |
| Fechas y horas | ISO 8601, UTC |
| Dinero | Importe en unidades menores más código de moneda ISO 4217 |
| Idioma y locale | Etiquetas BCP 47, por ejemplo `es`, `en`, `pt-BR` |
| País | ISO 3166-1 alfa-2 |
| Enumeraciones | Mayúsculas con guion bajo; los valores desconocidos se rechazan |
| Texto traducible | Guardado por locale, nunca en un único idioma fijo |
| Booleanos | Nombres en positivo (`is_active`, no `is_not_disabled`) |

## Plantilla de detalle por entidad

Copia este bloque para cada entidad.

### {{pending: nombre de la entidad}}

| Atributo | Tipo | Obligatorio | Clasificación | Descripción |
| --- | --- | --- | --- | --- |
| `id` | | Sí | Interno | |
| | | | | |

- Invariantes: {{pending: reglas que siempre deben cumplirse}}
- Relaciones: ver la [vista general del ERD](models/erd-overview.md).
- Campos de auditoría: siguen el [estándar de campos de auditoría](audit-fields-standard.md).
- Campos personales: clasificados en la [clasificación de datos personales](pii-classification.md).

## Correspondencia con contratos

| Entidad | Contrato | Diferencias de representación |
| --- | --- | --- |
| | [Ejemplo de contrato](../07-contracts/example.md) | |

## Reglas de cambio

- [ ] Añadir un atributo opcional es compatible hacia atrás.
- [ ] Renombrar o eliminar un atributo exige un periodo de deprecación y un plan de migración.
- [ ] Cambiar el significado de un atributo se trata como un atributo nuevo.
- [ ] Cada cambio actualiza contratos y pruebas en el mismo conjunto de cambios.

## Relacionados

- [Arquitectura de datos](data-architecture.md)
- [Vista general del ERD](models/erd-overview.md)
- [Estándar de campos de auditoría](audit-fields-standard.md)
- [Clasificación de datos personales](pii-classification.md)
- [Ejemplo de contrato](../07-contracts/example.md)
- [Ejemplo de dominio](../03-domains/example/domain-spec.md)
