# Ciclo de vida de funcionalidades

## Propósito

Describir las etapas que recorre una funcionalidad desde la idea hasta su retiro, qué debe cumplirse para pasar de una etapa a otra y quién decide. Así se mantienen alineadas las especificaciones, el código, las pruebas y la documentación.

Estado: borrador. {{pending: confirmar las etapas y quién aprueba cada compuerta}}

## Etapas

| Etapa | Criterio de entrada | Criterio de salida | Artefactos |
|-------|---------------------|--------------------|------------|
| Idea | Problema anotado con algo de evidencia | Aceptada en la hoja de ruta | Elemento de la hoja de ruta |
| Descubrimiento | Elemento en «Después» o «Ahora» | Problema y resultado validados | Notas de investigación, salida de `/dixi.discover` |
| Especificada | Problema validado | Especificación revisada, criterios de aceptación acordados | Especificación (`/dixi.specify`) |
| En construcción | Especificación aprobada y pruebas escritas primero | Pruebas en verde, revisión aprobada | Código, pruebas, entradas de trazabilidad |
| Publicada | Integrada y desplegada | Adopción medida contra el resultado | Notas de versión, eventos de analítica |
| Retirada | Decisión de eliminarla | Código, documentación y traducciones eliminados | Registro de decisión, notas de migración |

## Compuertas

Cada compuerta necesita una decisión humana. Los agentes pueden preparar la evidencia, pero nunca aprueban una compuerta.

- **Descubrimiento → Especificada**: el resultado es medible y los usuarios objetivo están nombrados.
- **Especificada → En construcción**: los criterios de aceptación son observables; las decisiones estructurales están registradas.
- **En construcción → Publicada**: `make verify` pasa; las revisiones de accesibilidad y traducción están hechas para cada idioma soportado.
- **Publicada → Retirada**: los usuarios afectados están informados y el manejo de datos está decidido.

{{pending: nombrar quién aprueba cada compuerta}}

## Exposición del lanzamiento

{{pending: decidir si las funcionalidades pueden salir detrás de banderas, a un porcentaje de usuarios o solo a todos a la vez}}

Cuando se usan banderas:

- Cada bandera tiene responsable y fecha de eliminación.
- Una bandera activa al 100 % por más tiempo del acordado se elimina.

## Medición del éxito

Cada funcionalidad publicada declara en su especificación:

- El resultado de la hoja de ruta al que sirve.
- Los eventos que muestran que se usa (ver el [catálogo de eventos de analítica](analytics-events-catalog.md)).
- La fecha de revisión en la que se comparará el resultado con lo esperado.

## Lista para el retiro

- Datos de uso revisados y decisión registrada.
- Usuarios notificados en cada idioma soportado.
- Código, pruebas, claves de traducción y documentación eliminados juntos.
- Entradas de trazabilidad actualizadas y `dixi check` en verde.

## Relacionados

- [Hoja de ruta](roadmap.md)
- [Marco de priorización](prioritization-framework.md)
- [Notas de versión](release-notes.md)
- [Especificación de ejemplo](../05-features/example/feature-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Guía](../docs/guide.md)
