# Plantilla de ADR

## Propósito

Registrar una decisión de arquitectura para que cualquiera entienda después qué se decidió, por
qué, qué alternativas se descartaron y cuánto cuesta. Copia la estructura de abajo en un archivo nuevo.

## Cómo usarla

- Una decisión por ADR. Numéralos en secuencia y nunca reutilices un número.
  {{pending: carpeta de ADRs y esquema de numeración}}
- Una **decisión estructural** (stack, modelo de datos, límites entre módulos, modelo de seguridad,
  proveedores externos) queda **Proposed** hasta que una persona responsable la valida. Un agente
  puede redactar un ADR, pero nunca pasarlo a Accepted.
- Un ADR aceptado no se edita para cambiar su decisión: se escribe un ADR nuevo que lo reemplaza.

## Plantilla

```markdown
# ADR-NNN — <título corto de la decisión>

Estado: Proposed | Accepted | Superseded por ADR-NNN | Rejected
Fecha: AAAA-MM-DD
Decisores: {{pending: personas que validan esta decisión}}
IDs relacionados: {{pending: IDs de objetivo, feature o contrato afectados}}

## Contexto

Qué problema o fuerza exige decidir ahora. Hechos, restricciones y supuestos,
sin proponer todavía la respuesta.

## Decisión

Qué haremos, en una o dos frases firmes, seguidas de los detalles necesarios
para aplicarla.

## Alternativas consideradas

| Opción | A favor | En contra | Por qué no se eligió |
|---|---|---|---|
| A | | | |
| B | | | |

## Consecuencias

- Positivas: qué se vuelve más fácil.
- Negativas: qué se vuelve más difícil, costos, riesgos y deuda aceptada.
- Seguimiento: tareas, pruebas o ADRs que esta decisión requiere.

## Validación

- [ ] Revisado por los decisores.
- [ ] Specs y pruebas afectadas actualizadas.
```

## Valores de estado

| Estado | Significado |
|---|---|
| Proposed | Redactado, en discusión; aún no obliga |
| Accepted | Validado por los decisores; obliga |
| Superseded | Reemplazado por un ADR más nuevo, que se enlaza |
| Rejected | Discutido y no adoptado; se conserva como historia |

## Relacionados

- [Estándares de código](../coding-standards.md)
- [Proyecto](../../00-master-spec.md)
- [Instrucciones del proyecto](../../AGENTS.md)
