# Guía de pruebas de contrato

## Propósito

Explicar cómo comprueba este proyecto que productores y consumidores de una interfaz (APIs HTTP, eventos, mensajes) siguen de acuerdo, para que un lado no pueda romper al otro sin que se note.

Estado: borrador. {{pending: decidir el enfoque de pruebas de contrato para cada interfaz}}

## Cuándo ayudan las pruebas de contrato

- Varios servicios o equipos dependen de la misma interfaz.
- Productor y consumidor se publican de forma independiente.
- Los mensajes viajan por una cola o bus de eventos donde los fallos aparecen tarde.

## Enfoques

| Enfoque | Cómo funciona | Encaja cuando |
|---------|---------------|---------------|
| Guiado por el consumidor | Los consumidores publican expectativas; el productor las verifica | Pocos consumidores conocidos |
| Basado en esquema | Ambos lados validan contra un esquema compartido y versionado | Muchos consumidores o desconocidos |
| Instantánea del productor | El productor registra respuestas; los cambios se revisan | Interfaces simples de un solo equipo |

{{pending: elegir un enfoque por interfaz y registrar por qué}}

## Reglas

- El contrato escrito en `07-contracts/` es la fuente de verdad; las pruebas comprueban el código contra él.
- Los cambios de contrato siguen primero la especificación: se actualiza el contrato, se revisa y luego se escribe la prueba que falla.
- Los cambios incompatibles requieren una nueva versión o un plan de migración acordado con los consumidores.
- Las pruebas de contrato quedan congeladas como cualquier otra prueba.

## Qué probar

- Campos obligatorios, tipos y formatos.
- Respuestas de error y su forma.
- Que los campos opcionales sean realmente opcionales.
- Que se toleren campos desconocidos si el contrato lo indica.
- Cabeceras, claves y supuestos de orden de los eventos.

## En la escalera de verificación

Las pruebas de contrato corren después de las de integración y antes de las end-to-end. {{pending: dónde corre la verificación de contratos, en local o en CI}}

## Relacionados

- [Contrato](../07-contracts/example.md)
- [Escalera de verificación](verification-ladder.md)
- [Pirámide de pruebas](test-pyramid.md)
- [Presupuestos de latencia de API](performance-budgets/api-latency-budgets.md)
- [Plan de regresión](regression-plan.md)
