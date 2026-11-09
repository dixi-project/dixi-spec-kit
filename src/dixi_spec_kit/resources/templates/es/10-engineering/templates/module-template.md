# Plantilla de módulo

## Propósito

Describir un módulo: su responsabilidad, los datos que le pertenecen, las interfaces que expone y
sus dependencias. Un módulo es una unidad de código con límites claros dentro de un dominio. Copia
la estructura de abajo en `04-modules/<modulo>/module-spec.md`.

## Plantilla

```markdown
# MODULE-NNN — <nombre del módulo>

Estado: borrador | activo | deprecado
Padre: DOMAIN-NNN
Responsable: {{pending: equipo o persona responsable}}

## Propósito

De qué se encarga este módulo y, explícitamente, de qué no.

## Responsabilidades

- ...

## Datos propios

| Entidad | Campos clave | Notas (datos personales, retención) |
|---|---|---|

Solo este módulo escribe sus datos; los demás los leen por sus interfaces.

## Interfaces públicas

| Tipo (API, evento, función) | Nombre | Contrato |
|---|---|---|
| API | | CONTRACT-NNN |
| Evento publicado | | |
| Evento consumido | | |

## Dependencias

| Depende de | Por qué | Comportamiento ante fallo |
|---|---|---|

## Reglas de negocio

| ID | Regla |
|---|---|

## Requisitos no funcionales

- Objetivos de disponibilidad y latencia: {{pending: objetivos}}
- Seguridad: modelo de autorización, datos sensibles.

## Features

- FEATURE-NNN — ...

## Ubicación del código

{{pending: ruta del módulo en el repositorio}}
```

## Relacionados

- [Módulo de ejemplo](../../04-modules/example/module-spec.md)
- [Plantilla de dominio](domain-template.md)
- [Plantilla de feature](feature-template.md)
- [Estándar de estructura de paquetes](../package-structure-standard.md)
