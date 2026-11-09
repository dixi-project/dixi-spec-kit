# Plantilla de feature

## Propósito

Describir una feature con criterios de aceptación observables, trazada a su módulo y a las pruebas
que la demuestran. Copia la estructura de abajo en `05-features/<feature>/feature-spec.md`.

## Plantilla

```markdown
# FEATURE-NNN — <nombre de la feature>

Estado: borrador | lista | en curso | terminada
Padre: MODULE-NNN
Responsable: {{pending: persona responsable de esta feature}}

## Propósito

La necesidad de usuario o de negocio que resuelve, en dos o tres frases.

## Alcance

- Dentro del alcance: ...
- Fuera del alcance: ...

## Historias de usuario

- Como <rol>, quiero <capacidad>, para <beneficio>.

## Criterios de aceptación

Cada criterio es observable y comprobable.

1. Dado <contexto>, cuando <acción>, entonces <resultado observable>.
2. Dado ..., cuando ..., entonces ...

## Reglas de negocio

| ID | Regla | Fuente |
|---|---|---|
| BR-1 | | |

## Contratos y datos

- Contratos afectados: CONTRACT-NNN
- Datos creados, leídos o modificados: {{pending: entidades y campos}}

## Requisitos no funcionales

- Rendimiento: {{pending: tiempo de respuesta o capacidad objetivo}}
- Seguridad y privacidad: reglas de autorización, datos personales involucrados.
- Accesibilidad e idiomas: idiomas soportados, nivel de accesibilidad.

## Riesgos y preguntas abiertas

- ...

## Pruebas

| Criterio | ID de prueba | Tipo |
|---|---|---|
| 1 | TEST-NNN | unitaria / integración / aceptación |
```

## Notas

- Escribe las pruebas a partir de los criterios de aceptación antes de implementar.
- Registra la feature y su padre en `.dixi/traceability.json`.

## Relacionados

- [Feature de ejemplo](../../05-features/example/feature-spec.md)
- [Módulo de ejemplo](../../04-modules/example/module-spec.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
- [Plantilla de ADR](adr-template.md)
