# Metodología SDD

## Propósito

Describir cómo este proyecto aplica el desarrollo guiado por especificaciones (SDD): todo cambio parte de una especificación escrita y enlazada, se demuestra con pruebas escritas primero y termina con revisión humana. Este archivo explica el método; las decisiones propias del proyecto quedan marcadas como pendientes hasta que una persona responsable las tome.

## Principios

1. **Primero la spec.** No hay código sin una spec que diga el comportamiento esperado y sus criterios de aceptación.
2. **Specs enlazadas.** Cada spec nombra a su padre: objetivo → dominio → módulo → feature → contrato → prueba. Los enlaces se registran en `.dixi/traceability.json`.
3. **Primero las pruebas.** Las pruebas derivadas del contrato se escriben y se ven fallar antes de implementar. Las pruebas congeladas nunca se editan para que el código pase.
4. **Documentación viva.** Si cambia el comportamiento, la spec cambia en el mismo pull request.
5. **Responsabilidad humana.** Los agentes redactan, comprueban y proponen; una persona valida las decisiones estructurales, firma, aprueba e integra.

## El ciclo

| Paso | Entrada | Salida | Quién decide |
| --- | --- | --- | --- |
| Descubrir | Una necesidad o idea | Objetivo y alcance en `01-business/vision.md` | Persona responsable |
| Especificar | Objetivo aprobado | Specs de dominio, módulo y feature | Persona, asistida por un agente |
| Contrato | Spec de feature | Contrato con entradas, salidas y errores | La persona valida |
| Probar | Contrato | Pruebas en rojo que codifican los criterios | El agente redacta, la persona revisa |
| Construir | Pruebas en rojo | Código que las hace pasar | Agente o persona |
| Verificar | Código y pruebas | `dixi check` más las comprobaciones reales del proyecto | Automático, reportado con honestidad |
| Revisar | Pull request | Aprobación e integración | Solo una persona |

## Trabajo con agentes

- Usa `dixi workflow list` para ver los procedimientos compartidos y `dixi workflow prepare <nombre>` para reunir contexto antes de pedirle algo a un agente.
- En las integraciones con agentes, los mismos procedimientos aparecen como comandos `/dixi.*` o skills `$dixi-*`; para la guía de IA usa `/dixi.ai` o `$dixi-ai`.
- La revisión de un agente es un insumo para quien revisa, nunca un sustituto.

## Decisiones del proyecto

- Profundidad de spec exigida antes de construir: {{pending: profundidad mínima, estándar o completa según el nivel de riesgo}}
- Quién valida las decisiones estructurales: {{pending: nombrar el rol o la persona}}
- Qué cambios pueden omitir la spec de feature (por ejemplo, erratas): {{pending: listar las excepciones permitidas}}

## Relacionados

- [Ciclo de vida de specs](spec-lifecycle.md)
- [Matriz de trazabilidad](traceability-matrix.md)
- [Reglas de validación](validation-rules.md)
- [Guía de adopción](adoption-guide.md)
- [Guía del proyecto](../../docs/guide.md)
- [Spec maestra](../../00-master-spec.md)
