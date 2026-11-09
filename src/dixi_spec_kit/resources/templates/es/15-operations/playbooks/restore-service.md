# Restaurar el servicio

## Propósito

Devolver un servicio degradado o no disponible a un estado funcional de forma rápida y segura, antes de investigar la causa raíz.

Estado: borrador. {{pending: nombrar al responsable de este playbook}}

## Cuándo aplica

- Una alerta o un reporte de usuario muestra que un servicio en producción está caído o degradado.
- Cualquier nivel de incidente; los [niveles de incidente](../incident-levels.md) deciden la rapidez y quién se suma.

## Roles

- **Líder del incidente**: decide y lleva la cronología.
- **Operador**: persona con acceso a producción que ejecuta las acciones.
- **Líder de comunicación**: mantiene los avisos internos y a clientes.

Un agente de IA puede ayudar a leer logs, resumir y proponer pasos; una persona ejecuta cada acción en producción.

## Pasos

1. **Declarar.** Abre el canal del incidente, fija el nivel, nombra al líder.
2. **Estabilizar.** Detén el daño: pausa el proceso que falla, reduce carga o activa una página de mantenimiento.
3. **Buscar el último cambio.** Revisa despliegues, configuración y feature flags recientes. {{pending: dónde está el registro de cambios}}
4. **Elegir la acción más segura**, en este orden de preferencia:
   - revertir el último despliegue o cambio de configuración;
   - apagar el feature flag involucrado;
   - reiniciar o escalar el componente afectado;
   - conmutar a un respaldo, si existe. {{pending: listar las opciones de conmutación disponibles}}
5. **Obtener aprobación** del líder del incidente para cualquier acción que cambie datos o no se pueda deshacer.
6. **Actuar y observar.** Ejecuta una acción a la vez y vigila las señales clave durante {{pending: minutos}} antes de la siguiente.
7. **Comunicar** cada {{pending: intervalo}} siguiendo el playbook de [comunicación de caída a clientes](comms-outage-customer.md).

## Criterios de cierre

- Señales clave de salud en su rango normal durante al menos {{pending: duración}}.
- Sin colas crecientes, errores acumulados ni inconsistencias de datos pendientes.
- Clientes avisados de que el servicio se restauró.
- Cronología registrada y postmortem agendado para SEV1 y SEV2.

## No hacer

- Borrar datos, rotar credenciales compartidas o cambiar varias cosas a la vez «para ver qué funciona».
- Cerrar el incidente porque la alerta dejó de sonar; confirma con señales reales.

## Relacionados

- [Niveles de incidente](../incident-levels.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Comunicación de caída a clientes](comms-outage-customer.md)
- [Plantilla de runbook](../../10-engineering/templates/runbook-template.md)
- [Plantilla de postmortem](../../10-engineering/templates/postmortem-template.md)
