# Matriz de trazabilidad

## Propósito

Explicar cómo se enlazan los artefactos desde el objetivo de negocio hasta la prueba, dónde viven esos enlaces y cómo encontrar huecos. La fuente de verdad es `.dixi/traceability.json`; este documento explica cómo leerlo y mantenerlo.

## Cadena

```text
GOAL → DOMAIN → MODULE → FEATURE → CONTRACT → TEST
```

Cada elemento de `.dixi/traceability.json` tiene `id`, `kind`, `path` y una lista de `parents`. Un hijo debe referenciar a un padre existente del tipo anterior.

## Vista de ejemplo

| ID | Tipo | Ruta | Padres |
| --- | --- | --- | --- |
| GOAL-001 | goal | `01-business/vision.md` | — |
| DOMAIN-001 | domain | `03-domains/example/domain-spec.md` | GOAL-001 |
| MODULE-001 | module | `04-modules/example/module-spec.md` | DOMAIN-001 |
| FEATURE-001 | feature | `05-features/example/feature-spec.md` | MODULE-001 |
| CONTRACT-001 | contract | `07-contracts/example.md` | FEATURE-001 |
| TEST-001 | test | `11-quality/test-plan.md` | CONTRACT-001 |

Sustituye las filas de ejemplo a medida que se creen artefactos reales. Nunca reutilices un ID para otro artefacto.

## Mantenimiento

1. Registra cada spec nueva en `.dixi/traceability.json` en el mismo cambio que la crea.
2. Ejecuta `dixi check` para detectar archivos faltantes, padres desconocidos y enlaces rotos.
3. Al retirar un artefacto, márcalo como obsoleto en el documento antes de quitar la entrada.

## Huecos que buscar

- Objetivos sin dominio, o features sin contrato.
- Contratos sin entrada de prueba.
- Código o pruebas que no se pueden rastrear hasta ninguna feature.
- Specs cuyo padre quedó obsoleto.

## Decisiones del proyecto

- Esquema de IDs más allá de los predeterminados: {{pending: prefijos de ID y reglas de numeración}}
- Si se rastrean enlaces horizontales (dependencias entre módulos): {{pending: rastrear dependencias o no}}

## Relacionados

- [Metodología](methodology.md)
- [Reglas de validación](validation-rules.md)
- [Objetivo](../../01-business/vision.md)
- [Feature de ejemplo](../../05-features/example/feature-spec.md)
- [Contrato de ejemplo](../../07-contracts/example.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
