# Plantilla de dominio

## Propósito

Describir un dominio de negocio: su lenguaje, conceptos centrales, reglas y límites, antes de
dividirlo en módulos. Copia la estructura de abajo en `03-domains/<dominio>/domain-spec.md`.

## Plantilla

```markdown
# DOMAIN-NNN — <nombre del dominio>

Estado: borrador | validado
Padre: GOAL-NNN
Experto del dominio: {{pending: persona que valida el lenguaje de negocio}}

## Propósito

La parte del negocio que cubre este dominio y el objetivo al que sirve.

## Lenguaje ubicuo

| Término | Definición | No confundir con |
|---|---|---|

## Conceptos centrales

| Concepto | Tipo (entidad, objeto de valor, agregado) | Identidad | Estados del ciclo de vida |
|---|---|---|---|

## Reglas de negocio e invariantes

| ID | Regla | ¿Siempre se cumple? |
|---|---|---|
| INV-1 | | sí |

## Eventos de dominio

| Evento | Cuándo ocurre | Datos |
|---|---|---|

## Límites

- Dentro de este dominio: ...
- Fuera (pertenece a otros dominios): ...
- Relación con otros dominios: {{pending: proveedor, consumidor, conceptos compartidos}}

## Módulos

- MODULE-NNN — ...

## Preguntas abiertas

- ...
```

## Notas

- Usa el vocabulario del negocio; una persona desarrolladora y una experta del dominio deben leerlo igual.
- Las invariantes se convierten en pruebas en los módulos que las implementan.

## Relacionados

- [Dominio de ejemplo](../../03-domains/example/domain-spec.md)
- [Plantilla de módulo](module-template.md)
- [Plantilla de flujo](flow-template.md)
