# Convenciones de nombres

## Propósito

Acordar cómo se nombran las cosas en el proyecto (archivos, código, ramas, recursos, variables de entorno), para que los nombres sean predecibles, fáciles de buscar y no contengan información sensible.

Estado: borrador. {{pending: confirmar las convenciones de nombres con el equipo}}

## Reglas generales

- Los nombres describen el propósito, no la implementación ni a una persona.
- Usa un solo idioma para los identificadores: {{pending: idioma de los identificadores}}
- Evita abreviaturas salvo que estén en el glosario o en la lista de siglas.
- Nunca pongas secretos, datos personales ni nombres de clientes en ningún nombre.

## Documentos y specs

| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Archivos | `kebab-case.md` | `password-reset.md` |
| IDs de spec | `TIPO-NNN` | `FEATURE-012`, `CONTRACT-004` |
| ADR | `NNNN-titulo-corto.md` | `0007-elegir-cola.md` |
| Carpetas | Prefijo numérico de área | `05-features/` |

## Código

| Elemento | Convención |
|----------|------------|
| Variables y funciones | {{pending: p. ej. snake_case o camelCase, según el lenguaje}} |
| Tipos y clases | {{pending: p. ej. PascalCase}} |
| Constantes | {{pending: p. ej. UPPER_SNAKE_CASE}} |
| Nombres de pruebas | Describen el comportamiento: `rechaza_token_caducado` |
| Claves de traducción | `area.pantalla.elemento`, p. ej. `auth.login.submit` |

## Repositorio y ramas

- Nombres de repositorio: {{pending: patrón, p. ej. producto-componente}}
- Ramas: `feat/`, `fix/`, `docs/` más un tema corto (ver la estrategia de ramas).

## Variables de entorno

- `UPPER_SNAKE_CASE`, con prefijo de componente cuando se comparten: `BILLING_API_URL`.
- Los nombres se pueden documentar; los valores nunca.

## Recursos de infraestructura

- Patrón: `{{pending: p. ej. <producto>-<entorno>-<componente>-<propósito>}}`
- Códigos de entorno: `dev`, `stg`, `prd` {{pending: confirmar códigos}}
- Etiquetas obligatorias: responsable, entorno, centro de costo. {{pending: confirmar etiquetas obligatorias}}

## Cómo se aplica

Los nombres nuevos siguen este documento; los existentes se renombran solo cuando se tocan por otro motivo.

## Relacionados

- [Estrategia de ramas](branching-strategy.md)
- [Política de documentación](documentation-policy.md)
- [Estándares de código](../../10-engineering/coding-standards.md)
