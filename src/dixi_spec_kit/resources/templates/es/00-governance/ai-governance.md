# Gobernanza de IA

## Propósito

Establecer cómo pueden participar los asistentes y agentes de IA en el proyecto: qué pueden hacer solos, qué requiere a una persona, qué nunca se delega y cómo se traza su trabajo. Aplica a cualquier modelo o herramienta que elija el proyecto.

Estado: borrador. {{pending: confirmar las reglas de gobernanza de IA con la persona responsable}}

## Principios

1. **Responsabilidad humana.** Una persona nombrada es dueña de cada cambio, lo haya redactado quien lo haya redactado.
2. **Transparencia.** El trabajo asistido por IA se identifica en el pull request o el commit.
3. **Autonomía progresiva.** La autonomía crece con evidencia, nunca por defecto.
4. **Calidad primero.** La salida de la IA pasa las mismas pruebas y revisiones que el trabajo humano.
5. **Privacidad desde el diseño.** Los secretos y datos personales nunca llegan al contexto de un agente.

## Niveles de autonomía

| Nivel | Nombre | El agente puede | Una persona debe |
|-------|--------|-----------------|------------------|
| 0 | Asistir | Sugerir texto o código a petición. | Escribir y commitear. |
| 1 | Redactar | Crear specs, pruebas y código en una rama. | Revisar cada cambio antes de integrarlo. |
| 2 | Ejecutar | Correr comandos de solo lectura y la suite local de pruebas. | Aprobar cualquier comando con efectos. |
| 3 | Operar | {{pending: decidir si se permite alguna acción de nivel 3}} | Supervisar y poder detenerlo. |

Nivel máximo actual: {{pending: nivel máximo de autonomía de este proyecto}}

## Nunca se delega a un agente

- Firmar commits o atestaciones.
- Aprobar o integrar pull requests.
- Desplegar o promover `MODE`.
- Leer secretos, llaves o archivos `.env*`.
- Editar pruebas commiteadas (congeladas) para que el código pase.

## Permitido por acción

| Acción | Nivel permitido | Notas |
|--------|-----------------|-------|
| Redactar una spec de funcionalidad | 1 | Las historias estructurales requieren validación humana previa. |
| Escribir una prueba en rojo | 1 | Se commitea sola antes de la implementación. |
| Implementar código | 1 | Solo para hacer pasar pruebas existentes. |
| Ejecutar `dixi check` y `make verify` | 2 | Reportar el resultado real. |
| Cambiar dependencias | {{pending: nivel}} | Seguir la política de dependencias. |

## Trazabilidad

- Registra qué herramienta y modelo asistieron, en la descripción del pull request.
- Guarda junto a la spec los prompts que dieron forma a decisiones estructurales. {{pending: dónde se guardan los prompts}}

## Cadencia de revisión

{{pending: cada cuánto se revisan estas reglas y quién lo hace}}

## Relacionados

- [Política de uso de IA](policies/ai-usage-policy.md)
- [Humano en el ciclo](../21-ai/agents/human-in-the-loop.md)
- [Salvaguardas](../21-ai/agents/guardrails.md)
- [Instrucciones del proyecto](../AGENTS.md)
- [Principios](principles.md)
