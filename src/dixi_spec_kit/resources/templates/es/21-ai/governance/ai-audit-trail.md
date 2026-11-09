# Rastro de auditoría de IA

## Propósito

Permitir responder, a posteriori, qué hizo una IA en un cambio o en una respuesta del producto, sin guardar secretos ni datos personales innecesarios.

## Principio

Registra lo suficiente para reconstruir quién decidió qué y con qué evidencia. No registres lo que no querrías que se filtrara.

## Ámbito 1 — IA que construye

Para responder «¿qué hizo la IA en este cambio?»:

1. **Descripción del pull request**: qué archivos o funciones se generaron con IA y dónde concentró la revisión el autor.
2. **Commits**: participación de IA marcada de forma consistente (por ejemplo, un trailer de coautoría); una persona sigue siendo responsable de cada commit.
3. **Pruebas**: el commit de pruebas en rojo precede a la implementación; las ediciones posteriores de pruebas se ven en el diff y necesitan un motivo humano.
4. **Revisiones**: los comentarios de agentes se etiquetan como tales; las aprobaciones humanas se refieren a la revisión final.
5. **Comprobaciones**: `dixi check` y las comprobaciones reales del proyecto, con su resultado observado.

Convención para marcar la participación de IA: {{pending: trailer, etiqueta o sección usada}}

## Ámbito 2 — IA dentro del producto

Para cada llamada al modelo, considera registrar:

| Campo | Por qué |
| --- | --- |
| ID de petición y marca de tiempo | Correlacionar con los logs de la aplicación |
| Identificador y versión del modelo | Explicar cambios de comportamiento |
| ID y versión de la plantilla de prompt | Reconstruir el prompt desde control de versiones |
| Parámetros (temperatura, límites) | Reproducir condiciones |
| Resultado (aceptado, rechazado, error) | Medir calidad |
| Hash con llave de la entrada, si hace falta | Verificar una reconstrucción sin guardar el texto |

No registres prompts en crudo que puedan contener datos personales salvo que exista una excepción aprobada.

## Nunca se registra

- Secretos, tokens ni credenciales.
- Datos personales en crudo sin base documentada ni retención.
- Documentos completos recuperados como contexto cuando basta un ID.

## Retención

- Rastro del desarrollo: vive con el historial del repositorio.
- Logs del producto: {{pending: periodo de retención y lugar de almacenamiento}}

## Relacionados

- [IA responsable](responsible-ai.md)
- [Guardarraíles](../agents/guardrails.md)
- [Humano en el circuito](../agents/human-in-the-loop.md)
