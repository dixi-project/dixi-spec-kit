# Plan de regresión

## Propósito

Asegurar que el comportamiento que ya funciona siga funcionando a medida que el proyecto cambia, definiendo qué pruebas lo protegen, cuándo corren y qué pasa cuando una falla.

Estado: borrador. {{pending: confirmar la suite de regresión y su calendario}}

## Suite de regresión

La suite de regresión es el conjunto de pruebas commiteadas y congeladas que protegen el comportamiento entregado.

| Suite | Contenido | Corre | Presupuesto de tiempo |
|-------|-----------|-------|-----------------------|
| Rápida | Pruebas unitarias y de integración | En cada cambio, dentro de `make verify` | {{pending: presupuesto}} |
| Completa | Suite rápida más pruebas de contrato y end-to-end | {{pending: por ejemplo en cada pull request}} | {{pending: presupuesto}} |
| Extendida | Pruebas de rendimiento, seguridad y larga duración | {{pending: calendario}} | {{pending: presupuesto}} |

## Añadir a la suite

- Cada defecto corregido recibe primero una prueba que lo reproduce (rojo) y después la corrección (verde).
- Cada funcionalidad aceptada añade sus pruebas a la suite.
- Nunca se quitan pruebas para acelerar la suite sin una decisión registrada; se mueven a un nivel más lento.

## Seleccionar pruebas para un cambio

{{pending: decidir si se corre siempre la suite completa o se seleccionan pruebas por áreas cambiadas, y cómo evitar omitir dependencias}}

## Fallos

1. Una prueba de regresión que falla bloquea la integración.
2. Averigua si el error está en el código, el entorno o la prueba.
3. Si la prueba es incorrecta, detente y pide una decisión humana; no edites una prueba congelada para que pase.
4. Las pruebas inestables se ponen en cuarentena con responsable y fecha límite, y se corrigen.

## Verificaciones de release

Antes de un release, registra:

- Resultados reales de la suite completa.
- Fallos conocidos y su riesgo aceptado, con la persona que lo aceptó.
- Verificaciones manuales de regresión realizadas, si las hubo.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Escalera de verificación](verification-ladder.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Revisión basada en riesgo](risk-based-review.md)
- [Plan de pruebas](test-plan.md)
