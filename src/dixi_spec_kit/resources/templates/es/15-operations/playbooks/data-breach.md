# Brecha de datos

## Propósito

Responder a una exposición confirmada o sospechada de datos personales o confidenciales: contenerla, preservar la evidencia, evaluar a quién afecta y cumplir a tiempo las obligaciones de notificación.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

Este playbook es una guía operativa, no es asesoría legal. Las obligaciones de notificación dependen de las leyes y contratos aplicables.

## Cuándo aplica

- Alguien sin autorización accedió, copió, cambió o borró datos.
- Se publicaron datos o se enviaron al destinatario equivocado.
- Se filtró una credencial con acceso a datos personales.

Toda sospecha de brecha empieza en SEV1 hasta descartarla (ver [niveles de incidente](../incident-levels.md)).

## Roles

- **Líder del incidente**: coordina y lleva la cronología.
- **Contacto de seguridad**: lidera la contención y la evidencia.
- **Contacto de privacidad o legal**: decide las notificaciones. {{pending: nombrar este rol}}
- **Líder de comunicación**: prepara los mensajes; no publica nada sin aprobación.

Un agente de IA puede ayudar a buscar en logs y resumir hallazgos; nunca borra evidencia, rota credenciales ni contacta a nadie.

## Pasos

1. **Declarar** y abrir un canal de incidente restringido; limita quién entra.
2. **Contener**: revoca credenciales filtradas, cierra la vía expuesta, bloquea al actor. Prefiere acciones que no destruyan evidencia.
3. **Preservar la evidencia**: exporta logs, snapshots y registros de acceso relevantes a una ubicación protegida; registra quién los manejó.
4. **Evaluar el alcance**: qué datos, qué categorías (ver [clasificación de PII](../../08-data/pii-classification.md)), cuántas personas, qué periodo, si los datos estaban cifrados.
5. **Decidir la notificación** con el contacto de privacidad o legal: autoridades, personas afectadas, clientes con contrato. Plazo: {{pending: listar plazos legales y contractuales}}.
6. **Notificar** con el playbook de [comunicación de brecha a clientes](comms-breach-customer.md).
7. **Recuperar**: corrige la causa raíz, verifica que no haya más accesos, restablece la operación normal.

## Registro cronológico

Registra cada acción con hora, persona y evidencia. El plazo de notificación suele empezar cuando se conoce la brecha, no cuando se entiende por completo.

## Criterios de cierre

- Exposición detenida y verificada.
- Decisión de notificación documentada y notificaciones enviadas cuando corresponda.
- Postmortem completado y riesgos añadidos al [registro de riesgos](../../13-security/risk-register.md).

## Relacionados

- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Comunicación de brecha a clientes](comms-breach-customer.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Controles de protección de datos](../../13-security/data-protection-controls.md)
