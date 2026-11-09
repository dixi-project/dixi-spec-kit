# Guía de pruebas de mutación

## Propósito

Explicar cómo las pruebas de mutación miden si las pruebas detectan realmente código incorrecto, introduciendo pequeños cambios (mutantes) y comprobando que alguna prueba falla con cada uno.

Estado: borrador. {{pending: decidir dónde y con qué frecuencia corren las pruebas de mutación}}

## Cómo funciona

1. Una herramienta cambia ligeramente el código, por ejemplo `>` por `>=` o `+` por `-`.
2. La suite de pruebas corre contra cada mutante.
3. Si alguna prueba falla, el mutante queda **eliminado** (bien). Si todas pasan, **sobrevivió**: ninguna prueba vigila ese comportamiento.

La puntuación de mutación es la proporción de mutantes eliminados.

## Cuándo usarlas

- Lógica crítica: dinero, permisos, reglas con límites.
- Código mayormente generado o muy refactorizado, para comprobar que las pruebas tienen sentido.
- Sobre los archivos cambiados en un pull request, y sobre todo el código de forma programada.

## Trabajar con supervivientes

- Lee cada mutante superviviente: señala una prueba ausente o débil.
- Añade una prueba que lo elimine, escrita a partir de la especificación, no del mutante.
- Algunos mutantes son equivalentes (el comportamiento no cambia); márcalos con un motivo.
- Nunca debilites el conjunto de mutaciones ni excluyas archivos solo para subir la puntuación.

## Objetivos

| Alcance | Puntuación mínima | Corre |
|---------|-------------------|-------|
| Código cambiado en un pull request | {{pending: objetivo}} | {{pending: cuándo}} |
| Módulos críticos | {{pending: objetivo}} | {{pending: cuándo}} |
| Todo el código | {{pending: objetivo o «solo seguimiento»}} | {{pending: calendario}} |

Solo como ejemplo: algunos equipos empiezan siguiendo la puntuación sin bloquear y fijan un mínimo cuando se estabiliza.

## Costo

Las pruebas de mutación son lentas. Limítalas al código cambiado o crítico en los pull requests y ejecuta el análisis completo de forma programada.

## Herramientas

{{pending: elegir una herramienta de pruebas de mutación para el stack}}

## Relacionados

- [Guía de pruebas basadas en propiedades](property-based-testing-guide.md)
- [Guía de TDD](tdd-guide.md)
- [Escalera de verificación](verification-ladder.md)
- [Métricas de ingeniería](engineering-metrics.md)
