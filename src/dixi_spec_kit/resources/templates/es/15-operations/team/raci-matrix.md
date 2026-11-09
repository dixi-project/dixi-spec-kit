# Matriz RACI

## Propósito

Hacer explícito quién es Responsable, quién Aprueba (rinde cuentas), a quién se Consulta y a quién se Informa en las principales actividades operativas, para que las decisiones no se atasquen ni el trabajo se haga dos veces.

Estado: borrador. {{pending: nombrar al responsable de esta matriz}}

## Leyenda

- **R** Responsable: hace el trabajo.
- **A** Aprobador: toma la decisión final; exactamente uno por actividad.
- **C** Consultado: aporta antes de la decisión.
- **I** Informado: se le avisa después de la decisión.

## Roles

{{pending: sustituir por los roles que realmente tiene el proyecto}}

| Abreviatura | Rol |
|-------------|-----|
| PO | Dueño del producto |
| TL | Líder técnico |
| ENG | Equipo de ingeniería |
| OPS | Operaciones / guardia |
| SEC | Contacto de seguridad |
| SUP | Soporte |
| FIN | Contacto de finanzas |

## Matriz

| Actividad | PO | TL | ENG | OPS | SEC | SUP | FIN |
|-----------|----|----|-----|-----|-----|-----|-----|
| Despliegue a producción | I | A | R | C | I | I | — |
| Respuesta a incidentes | I | C | R | A | C | I | — |
| Comunicación de caída a clientes | A | C | — | C | — | R | — |
| Incidente de seguridad | I | C | R | C | A | I | — |
| Alta de proveedores | A | C | — | C | C | — | C |
| Revisión de presupuesto y costos | A | R | C | C | — | — | C |
| Reembolsos manuales | I | — | — | — | — | R | A |
| Ventanas de mantenimiento | C | A | R | R | — | I | — |
| Revisiones de acceso | I | R | — | C | A | — | — |

Estas asignaciones son ejemplos; ajusta cada celda. {{pending: confirmar cada fila con las personas indicadas}}

## Reglas

- Una sola A por fila. Si dos personas se sienten aprobadoras, la matriz no está terminada.
- Un agente de IA nunca es A ni el único R de una acción en producción.
- Actualiza la matriz cuando alguien entra, sale o cambia de rol.

## Relacionados

- [Rotación de guardia](on-call-rotation.md)
- [Matriz de escalamiento](../escalation-matrix.md)
- [Modelo de soporte](../support-model.md)
- [Catálogo de servicios](../service-catalog.md)
