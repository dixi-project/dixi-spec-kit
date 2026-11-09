# Plan de continuidad del negocio

## Propósito

Describir cómo la organización sigue prestando sus servicios críticos cuando personas, lugares, sistemas o proveedores no están disponibles. La recuperación ante desastres restablece la tecnología; la continuidad mantiene el negocio funcionando mientras tanto.

## Alcance

- Servicios críticos cubiertos: {{pending: lista de servicios de negocio}}
- Fuera de alcance: {{pending: lista}}
- Responsable del plan: {{pending: rol}}

## Análisis de impacto en el negocio

| Servicio de negocio | Caída máxima tolerable | Depende de | Alternativa manual | Responsable |
|---|---|---|---|---|
| {{pending: servicio}} | {{pending: duración}} | {{pending: sistemas, personas, proveedores}} | {{pending: alternativa}} | {{pending: rol}} |
| {{pending: servicio}} | {{pending: duración}} | {{pending: dependencias}} | {{pending: alternativa}} | {{pending: rol}} |

Las metas técnicas de recuperación de cada servicio se registran en la matriz RTO/RPO.

## Escenarios de interrupción

| Escenario | Respuesta |
|---|---|
| Personas clave no disponibles | Runbooks documentados, al menos dos personas formadas por tarea crítica: {{pending: lista}} |
| Oficina o lugar de trabajo no disponible | {{pending: acuerdos de trabajo remoto}} |
| Sistema crítico no disponible | Seguir el runbook de recuperación ante desastres; aplicar alternativas manuales |
| Proveedor crítico no disponible | {{pending: proveedor alternativo o servicio degradado}} |

## Roles y contactos

| Rol | Titular | Suplente |
|---|---|---|
| Líder de continuidad | {{pending: rol}} | {{pending: rol}} |
| Recuperación técnica | {{pending: rol}} | {{pending: rol}} |
| Comunicación | {{pending: rol}} | {{pending: rol}} |

Guarda los datos de contacto personales en un lugar protegido fuera de este repositorio: {{pending: dónde}}.

## Activación

1. Cualquier líder puede activar el plan cuando un escenario anterior supera su caída tolerable.
2. Notifica a los roles y abre un registro de continuidad.
3. Ejecuta las alternativas y la recuperación técnica en paralelo.
4. Desactiva el plan cuando los servicios vuelvan a niveles normales; haz una revisión.

## Pruebas y mantenimiento

- Ejercita el plan {{pending: frecuencia}}; registra solo los ejercicios realizados de verdad.
- Revísalo tras cualquier cambio importante de servicios, proveedores o equipo.

## Relacionados

- [Runbook de recuperación ante desastres](dr-runbook.md)
- [Estrategia de recuperación ante desastres](dr-strategy.md)
- [Matriz RTO y RPO](rto-rpo-matrix.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Registro de riesgos](../../13-security/risk-register.md)
