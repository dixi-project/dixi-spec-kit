# Guía de adopción de SDD

## Propósito

Ayudar a un equipo a empezar con el desarrollo guiado por especificaciones, en un proyecto nuevo o en uno existente, sin documentarlo todo por adelantado.

## Proyecto nuevo

Orden recomendado:

1. Completa `00-master-spec.md` con el problema, el alcance y las restricciones conocidas.
2. Escribe el objetivo de negocio en `01-business/vision.md`.
3. Describe un dominio y un módulo, conservando los IDs de ejemplo o renombrándolos de forma coherente.
4. Especifica la primera feature con criterios observables.
5. Escribe su contrato y las pruebas previstas; valida con una persona las decisiones estructurales.
6. Elige el stack y conecta las pruebas reales a `make verify`.

## Proyecto existente

Documenta sobre la marcha en lugar de detener el desarrollo:

1. Empieza por la spec maestra y las instrucciones del proyecto describiendo lo que existe hoy.
2. Especifica solo las features que estás cambiando.
3. Añade primero contratos para las interfaces más usadas.
4. Registra de forma retroactiva las decisiones pasadas importantes cuando se cuestionen.
5. Usa la matriz de trazabilidad para decidir qué huecos importan después.

Evita: specs vacías creadas solo para completar la estructura, duplicar documentación que ya vive en otro sitio y congelar el trabajo hasta tenerlo todo escrito.

## Niveles mínimos

| Nivel | Contenido | Uso típico |
| --- | --- | --- |
| Navegable | Spec maestra, objetivo, instrucciones del proyecto | Prototipos, exploración |
| Gobernable | Además dominios, módulos y decisiones clave | Código compartido |
| Trazable | Además contratos y pruebas enlazados para cada feature | Producción y trabajo regulado |

Nivel objetivo de este proyecto: {{pending: navegable, gobernable o trazable}}

## Con agentes

- Pide al agente que prepare el contexto con `dixi workflow prepare` antes de redactar.
- Revisa cada borrador; los agentes rellenan huecos con supuestos, que deben convertirse en marcas pendientes explícitas.
- Mantén los puntos de control humanos descritos en los documentos de guardarraíles y de humano en el circuito.

## Relacionados

- [Metodología](methodology.md)
- [Matriz de trazabilidad](traceability-matrix.md)
- [Guardarraíles](../agents/guardrails.md)
- [Humano en el circuito](../agents/human-in-the-loop.md)
- [Guía del proyecto](../../docs/guide.md)
