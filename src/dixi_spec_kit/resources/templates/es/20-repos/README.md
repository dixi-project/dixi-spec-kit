# Repositorios

## Propósito

Describir cómo se reparte el código del proyecto en repositorios y cómo cada repositorio se mantiene enlazado a las specs que lo justifican. La regla general es un repositorio por pieza desplegable: algo que se construye, versiona y libera por sí mismo.

Estado: borrador. {{pending: decidir la organización de repositorios (uno por pieza desplegable, un monorepo o una mezcla)}}

## Inventario de repositorios

| Repositorio | Tipo | Responsable | Specs que implementa | Estado |
|-------------|------|-------------|----------------------|--------|
| {{pending: nombre}} | Servicio backend | {{pending: responsable}} | {{pending: IDs MODULE-/FEATURE-}} | Planeado |
| {{pending: nombre}} | App frontend | {{pending: responsable}} | {{pending: IDs}} | Planeado |

Según el perfil pueden aplicar otros tipos: worker en segundo plano, app móvil o servidor MCP. Añade una fila por cada uno que adoptes y sigue su guía de stack en esta carpeta.

## Un repositorio por pieza desplegable

- Un repositorio tiene un build, un número de versión y un pipeline de liberación.
- El código compartido va en una biblioteca versionada, no en copias entre repositorios.
- Dividir o fusionar repositorios es una decisión estructural: regístrala como ADR.
- Si eliges un monorepo, mantén una carpeta por pieza desplegable con las mismas reglas.

## Enlazar código con specs

1. Este repositorio de specs es la fuente de verdad; los repositorios de código no redefinen requisitos.
2. Cada repositorio de código tiene una sección en su README con los IDs de spec que implementa y un enlace de vuelta aquí.
3. Ramas, commits y pull requests mencionan el ID de spec que cambian, por ejemplo `FEATURE-001`.
4. Las pruebas nombran o etiquetan el criterio que cubren, para poder seguir el camino objetivo → feature → contrato → prueba.
5. Registra la ubicación en código de cada elemento en `.dixi/traceability.json` y en la matriz de trazabilidad.
6. Un cambio de comportamiento empieza con un cambio de spec, luego pruebas y luego código.

## Convenciones comunes

Todo repositorio de código debería incluir:

- `README.md` con propósito, cómo correrlo en local y las specs que implementa.
- `AGENTS.md` con reglas para agentes de IA, coherente con el [AGENTS.md](../AGENTS.md) raíz.
- Un único comando de verificación (por ejemplo `make verify`) que ejecute las comprobaciones reales.
- Un `.env.example` solo con nombres de variables; los secretos reales nunca entran al repositorio.
- Textos visibles al usuario en catálogos de traducción por idioma, nunca hardcodeados.

{{pending: listar las convenciones obligatorias para todo repositorio y quién las revisa}}

## Crear un repositorio nuevo

1. Confirma que la pieza desplegable está justificada por una spec de módulo o feature.
2. Elige la guía de stack que corresponda y resuelve sus decisiones `{{pending}}`.
3. Registra la elección de stack como ADR.
4. Añade el repositorio al inventario anterior y a los registros de trazabilidad.

## Relacionados

- [Servicio backend](backend-service.md)
- [App frontend](frontend-app.md)
- [Matriz de trazabilidad](../21-ai/sdd/traceability-matrix.md)
- [Índice de ADR](../09-architecture/adr/README.md)
- [Estándares de código](../10-engineering/coding-standards.md)
- [Proyecto](../00-master-spec.md)
