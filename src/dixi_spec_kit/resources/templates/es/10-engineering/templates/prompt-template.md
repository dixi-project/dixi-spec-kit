# Plantilla de prompt

## Propósito

Especificar un prompt que usa el producto (no el equipo de desarrollo) como un artefacto
versionado y comprobable: sus entradas, el contrato de salida esperado, la validación y los casos
de evaluación. Copia la estructura de abajo para cada prompt.

## Plantilla

````markdown
# Prompt: <nombre>

ID: {{pending: ID del prompt}}
Versión: 1.0.0
Responsable: {{pending: persona responsable}}
Usado por: FEATURE-NNN
Requisitos del modelo: {{pending: capacidades necesarias, sin atar la spec a un proveedor}}

## Propósito

La tarea que realiza el modelo y por qué un modelo es la herramienta adecuada.

## Entradas

| Variable | Origen | ¿Confiable? | Longitud máxima |
|---|---|---|---|
| `{{user_input}}` | usuario | no | |

## Prompt

```text
Instrucciones de sistema...
Contexto: {{context}}
Tarea: ...
Responde solo en el formato descrito abajo.
```

## Contrato de salida

La estructura que debe seguir la salida (p. ej. un JSON schema), con los valores permitidos.

## Validación

- La salida se parsea y valida contra el contrato antes de usarse.
- Salida inválida: un reintento y luego se recurre a ...
- La salida nunca concede permisos ni dispara acciones irreversibles por sí sola.

## Casos de evaluación

| Caso | Entrada | Salida o propiedad esperada |
|---|---|---|
| Normal | | |
| Borde | | |
| Intento de inyección | | instrucción ignorada |

## Límites

- Presupuesto de costo y latencia por llamada:
- Datos personales enviados al modelo: {{pending: datos permitidos}}
````

## Relacionados

- [Estándar de código seguro](../secure-coding-standard.md)
- [Plantilla de feature](feature-template.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
