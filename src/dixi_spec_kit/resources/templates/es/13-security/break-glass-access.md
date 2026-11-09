# Acceso de emergencia (break-glass)

## Propósito

Definir la vía de acceso de emergencia que se usa cuando los controles de acceso normales impiden a una persona resolver un incidente crítico. El acceso de emergencia existe para ser raro, ruidoso y completamente auditado.

Estado: borrador. {{pending: nombrar al responsable del acceso de emergencia}}

## Cuándo puede usarse

- Hay un incidente crítico activo y el acceso normal no está disponible o es insuficiente.
- {{pending: listar otras situaciones permitidas}}

No debe usarse por comodidad, para mantenimiento rutinario ni para saltarse una revisión.

## Quién puede usarlo

| Persona o rol | Alcance del acceso | Segundo aprobador |
|---------------|--------------------|-------------------|
| {{pending: rol}} | {{pending: sistemas}} | {{pending: rol}} |

Mantén la lista corta; revísala al menos {{pending: frecuencia}}.

## Mecanismo

- Dónde se guardan las credenciales de emergencia y cómo se protegen: {{pending: definir, p. ej. almacén sellado que requiere a dos personas}}
- Segundo factor obligatorio: {{pending: sí / método}}
- El acceso está limitado en el tiempo: {{pending: duración máxima}}
- Las credenciales nunca se comparten con agentes de IA ni automatizaciones.

## Detección

Cada uso dispara una alerta inmediata a {{pending: destinatarios}}. Una alerta inesperada se trata como incidente de seguridad.

## Después del uso

1. Registra quién, cuándo, por qué, a qué se accedió y qué se cambió.
2. Rota las credenciales de emergencia.
3. Revisa el evento en el post-mortem del incidente.
4. Corrige, si es posible, el hueco que hizo necesario el acceso de emergencia.

## Ensayo

Prueba el procedimiento en un entorno no productivo con una cadencia fija para que funcione cuando haga falta. {{pending: definir la cadencia}}

## Relacionados

- [Respuesta a incidentes](incident-response.md)
- [Gestión de secretos](secret-management.md)
- [Controles de protección de datos](data-protection-controls.md)
- [Registro de riesgos](risk-register.md)
