# Flujos

## Propósito

Describir los flujos de negocio que atraviesan varios pasos, actores o módulos: qué los inicia, el
camino feliz, las alternativas, los errores y los eventos que emiten. Una especificación de
funcionalidad explica una capacidad; un flujo explica cómo cooperan funcionalidades y módulos de
principio a fin. En los flujos se hacen visibles los contratos que faltan, las responsabilidades
difusas y los errores sin gestionar antes de escribir código.

## Cuándo escribir un flujo

- El proceso implica más de un módulo, dominio o sistema externo.
- Varios actores se turnan (por ejemplo, un cliente envía y un operador aprueba).
- Los fallos a mitad de camino necesitan compensación o un mensaje claro para el usuario.
- El proceso tiene reglas temporales: caducidades, recordatorios, reintentos o calendarios.

Las interacciones simples de un solo módulo se documentan en la especificación de la funcionalidad.

## Cómo describir un flujo

1. Copia la [plantilla de flujo](../10-engineering/templates/flow-template.md) a
   `06-flows/<nombre-del-flujo>-flow.md`, con palabras en minúsculas separadas por guiones.
2. Dale un ID estable (`FLOW-NNN`) y enlaza las funcionalidades que cubre.
3. Escribe el camino feliz como pasos numerados con un actor por paso.
4. Añade un diagrama de secuencia coherente con los pasos numerados.
5. Enumera los flujos alternativos y la gestión de errores de cada paso que pueda fallar.
6. Nombra cada evento, comando o llamada a API y enlaza su contrato en `07-contracts/`.
7. Pide a una persona que valide el flujo antes de construir las funcionalidades implicadas.

## Índice de flujos

| ID | Flujo | Disparador | Actores | Funcionalidades | Responsable | Estado |
|---|---|---|---|---|---|---|
| FLOW-001 | {{pending: nombre del flujo}} | {{pending: qué lo inicia}} | {{pending: actores}} | {{pending: IDs de FEATURE}} | {{pending: rol}} | {{pending: borrador o validado}} |

## Lista de calidad

- Cada paso nombra a su actor y al sistema que registra el resultado.
- Cada llamada externa indica su política de tiempo de espera y reintentos.
- Cada error tiene un comportamiento observable y, si procede, un código de error.
- Cada evento emitido tiene contrato y al menos un consumidor conocido.
- Las pruebas de aceptación cubren el camino feliz y al menos un flujo alternativo.

## Relacionados

- [Plantilla de flujo](../10-engineering/templates/flow-template.md)
- [Ejemplo de funcionalidad](../05-features/example/feature-spec.md)
- [Ejemplo de contrato](../07-contracts/example.md)
- [Contratos de API](../07-contracts/api/README.md)
