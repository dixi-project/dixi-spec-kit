# Catálogo de eventos de analítica

## Propósito

Mantener una sola lista de los eventos de producto que registra el proyecto, qué significa cada uno y qué datos lleva, para que las métricas sean confiables, se respete la privacidad y nadie invente un evento duplicado.

Estado: borrador. {{pending: elegir la herramienta o almacenamiento de analítica y la persona que aprueba eventos nuevos}}

## Convención de nombres

- Formato: `objeto_accion` en minúsculas con guion bajo, en pasado, por ejemplo `report_exported`.
- Un evento por acción relevante del usuario o resultado del sistema; evita eventos por cada clic.
- Las propiedades usan minúsculas con guion bajo y conjuntos de valores estables.
- Los nombres de eventos y las claves de propiedades no cambian de significado; un significado nuevo requiere un evento nuevo.
- Los nombres técnicos se mantienen en inglés para que no dependan del idioma de la interfaz.

{{pending: confirmar el formato de nombres si la herramienta elegida impone otro}}

## Reglas de privacidad

- No pongas datos personales (nombres, correos, texto libre, ubicación precisa) en las propiedades.
- Usa un identificador seudónimo; clasifica cada propiedad según la clasificación de datos personales.
- Respeta el consentimiento del usuario antes de enviar cualquier evento no esencial.
- Indica el periodo de retención de los eventos en bruto.

{{pending: decidir el modelo de consentimiento y el periodo de retención de los datos de analítica}}

## Propiedades estándar

Se envían con cada evento cuando están disponibles:

| Propiedad | Tipo | Ejemplo | Notas |
|-----------|------|---------|-------|
| `event_version` | entero | `1` | Aumenta cuando cambian las propiedades |
| `locale` | texto | `es-MX` | Idioma y región de la interfaz |
| `platform` | texto | `web` | {{pending: valores permitidos}} |
| `app_version` | texto | `1.4.0` | Versión del producto |

## Lista de eventos

| Evento | Disparador | Propiedades | Responsable | Funcionalidad | Estado |
|--------|------------|-------------|-------------|---------------|--------|
| `account_created` | El usuario termina el registro | `method` | {{pending}} | {{pending: ID de funcionalidad}} | Propuesto |
| `onboarding_completed` | Último paso de configuración | `steps_skipped` | {{pending}} | {{pending}} | Propuesto |
| `report_exported` | La exportación termina bien | `format` | {{pending}} | {{pending}} | Propuesto |

Valores de estado: Propuesto, Implementado, Obsoleto, Eliminado.

## Agregar un evento

1. Busca en este catálogo un evento existente que ya responda la pregunta.
2. Escribe la pregunta que responde el evento y la métrica que alimenta.
3. Clasifica cada propiedad respecto a datos personales.
4. Agrega la fila con estado Propuesto y consigue la aprobación.
5. Impleméntalo con una prueba que verifique el evento y sus propiedades.
6. Cambia el estado a Implementado cuando se publique.

## Controles de calidad

- Los eventos en el código que no estén en este catálogo son defectos.
- Los eventos del catálogo que no se envían durante todo un periodo de revisión se investigan.

## Relacionados

- [Ciclo de vida de funcionalidades](feature-lifecycle.md)
- [Marco de priorización](prioritization-framework.md)
- [Clasificación de datos personales](../08-data/pii-classification.md)
- [Política de retención](../08-data/retention-policy.md)
- [Especificación de ejemplo](../05-features/example/feature-spec.md)
