# Guía de pruebas basadas en propiedades

## Propósito

Explicar cómo usar pruebas basadas en propiedades, que comprueban reglas que deben cumplirse para muchas entradas generadas, para encontrar casos límite que los ejemplos elegidos a mano no cubren.

Estado: borrador. {{pending: decidir dónde se esperan pruebas basadas en propiedades}}

## Cuándo usarlas

- Funciones puras con reglas claras: parseo, serialización, cálculos, dinero, fechas.
- Código con espacios de entrada grandes donde los ejemplos cubren solo una fracción.
- Invariantes que nunca deben romperse (un saldo nunca es negativo, un ordenamiento conserva todos los elementos).

Complementan, no sustituyen, a las pruebas basadas en ejemplos.

## Encontrar propiedades

| Patrón | Propiedad de ejemplo |
|--------|----------------------|
| Ida y vuelta | Decodificar un valor codificado devuelve el original |
| Invariante | Ordenar conserva el mismo número de elementos |
| Idempotencia | Aplicar una normalización dos veces equivale a aplicarla una |
| Oráculo | La versión optimizada coincide con una versión de referencia simple |
| Conmutatividad | El orden de operaciones independientes no cambia el resultado |
| Límites | Un descuento calculado nunca supera el subtotal |

## Pautas

- Escribe la propiedad a partir de la especificación antes que el código, como cualquier prueba (rojo primero).
- Restringe los generadores a valores válidos del dominio; prueba la entrada inválida por separado.
- Cuando aparezca un fallo, conserva el contraejemplo reducido como prueba de ejemplo normal.
- Fija la semilla aleatoria o regístrala para que los fallos sean reproducibles.
- Mantén un número razonable de ejecuciones en local. {{pending: número de ejemplos en local y en CI}}

## Herramientas

{{pending: elegir una biblioteca de pruebas basadas en propiedades para el stack}}

## Trampas

- Propiedades que repiten la implementación no demuestran nada.
- Generadores demasiado filtrados que rara vez producen entradas útiles.
- Ignorar un fallo como «aleatorio»; todo fallo es un contraejemplo real.

## Relacionados

- [Guía de TDD](tdd-guide.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Guía de pruebas de mutación](mutation-testing-guide.md)
- [Escalera de verificación](verification-ladder.md)
