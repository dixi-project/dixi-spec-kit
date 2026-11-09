# Reglas de validación

## Propósito

Enumerar las comprobaciones que debe superar una especificación, separando lo que verifica una herramienta de lo que debe juzgar una persona. `dixi check` cubre solo la estructura; no demuestra que el comportamiento sea correcto.

## Tipos de validación

| Tipo | Ejemplos | Cómo |
| --- | --- | --- |
| Estructural | Título, secciones de propósito y relacionados, enlaces que resuelven, JSON válido | Automática (`dixi check`) |
| Trazabilidad | Cada elemento tiene un padre válido; IDs únicos | Automática |
| Completitud | Secciones obligatorias llenas; sin marcas pendientes bloqueantes | Lista de comprobación y revisión |
| Semántica | Coherente con el padre, criterios sin ambigüedad, términos del glosario | Revisión humana |

## Listas por tipo de spec

### Dominio

- [ ] Propósito en una oración y frontera (qué entra y qué no).
- [ ] Entidades principales y eventos de dominio nombrados.
- [ ] Glosario de términos.

### Módulo

- [ ] Dominio padre referenciado.
- [ ] Responsabilidades y no responsabilidades explícitas.
- [ ] Interfaces públicas y dependencias.

### Feature

- [ ] Historia de usuario o enunciado de la necesidad.
- [ ] Criterios de aceptación observables (por ejemplo Dado / Cuando / Entonces).
- [ ] Casos límite y comportamiento ante errores.

### Contrato

- [ ] Entradas, salidas y casos de error con tipos.
- [ ] Regla de compatibilidad para cambios futuros.
- [ ] Entrada de prueba enlazada.

## Severidad

- **Bloqueante**: padre faltante, enlace roto, criterios de aceptación ambiguos.
- **Advertencia**: término sin entrada en el glosario, no responsabilidades poco claras.

{{pending: qué advertencias pasan a ser bloqueantes en este proyecto}}

## Quién valida

- Los agentes pueden ejecutar las comprobaciones automáticas y señalar huecos; reportan los resultados tal como los observan.
- Una persona decide la validez semántica y aprueba. {{pending: rol revisor por tipo de spec}}

## Relacionados

- [Ciclo de vida de specs](spec-lifecycle.md)
- [Matriz de trazabilidad](traceability-matrix.md)
- [Metodología](methodology.md)
- [Instrucciones del proyecto](../../AGENTS.md)
