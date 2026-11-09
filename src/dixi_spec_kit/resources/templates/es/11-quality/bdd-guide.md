# Guía de BDD

## Propósito

Describir cómo este proyecto usa el desarrollo guiado por comportamiento para convertir criterios de aceptación en ejemplos compartidos y ejecutables que personas ajenas a ingeniería puedan leer.

Estado: borrador. {{pending: decidir si los escenarios BDD son ejecutables o solo documentación}}

## Cuándo usar BDD

- Comportamiento que las personas de negocio necesitan leer y confirmar.
- Reglas con varios casos que se entienden mejor como ejemplos.
- Recorridos críticos que también merecen pruebas de aceptación.

Omite BDD para detalles puramente técnicos; una prueba unitaria es más barata y clara.

## Forma del escenario

```
Escenario: <comportamiento observable>
  Dado <contexto inicial>
  Cuando <acción>
  Entonces <resultado observable>
```

- Un comportamiento por escenario.
- Usa el lenguaje del dominio, no detalles de interfaz («el pedido queda confirmado», no «pulsa el botón verde»).
- Usa tablas de ejemplos para variaciones de una regla en lugar de copiar escenarios.
- Referencia en cada escenario el ID del criterio de la especificación.

## Flujo

1. Producto, ingeniería y calidad discuten ejemplos antes de construir.
2. Los escenarios se redactan y revisan con la persona responsable de la funcionalidad.
3. Los escenarios se commitean en rojo, siguiendo la [guía de TDD](tdd-guide.md).
4. Los pasos llaman al sistema a través de su interfaz real o de una frontera estable.
5. Los escenarios commiteados quedan congelados como cualquier otra prueba.

## Herramientas

{{pending: elegir un ejecutor de escenarios para el stack, o decidir mantenerlos como documentación revisada}}

## Antipatrones

- Escenarios que describen clics en lugar de comportamiento.
- Escenarios largos con muchos pasos *Cuando*.
- Definiciones de pasos llenas de lógica que nadie prueba.
- Reescribir escenarios tras la entrega para que coincidan con lo construido.

## Relacionados

- [Estrategia de aceptación](acceptance-strategy.md)
- [Guía de TDD](tdd-guide.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Plan de regresión](regression-plan.md)
- [Funcionalidad](../05-features/example/feature-spec.md)
