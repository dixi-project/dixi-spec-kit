# Matriz de capacidades de agentes

## Propósito

Registrar qué puede hacer cada rol de agente, para que los permisos se concedan a propósito y se revisen cuando cambien. Todo lo que no esté listado queda denegado por defecto.

## Capacidades por rol

Leyenda: **S** permitido, **C** permitido con confirmación humana, **N** no permitido.

| Capacidad | Especificador | Redactor de contratos | Redactor de pruebas | Constructor | Revisor |
| --- | --- | --- | --- | --- | --- |
| Leer specs y código | S | S | S | S | S |
| Escribir archivos de spec | S | S | N | N | N |
| Escribir archivos de prueba | N | N | S | N | N |
| Escribir código fuente | N | N | N | S | N |
| Ejecutar pruebas y `dixi check` | S | S | S | S | S |
| Instalar dependencias | N | N | N | C | N |
| Ejecutar comandos que cambian estado | N | N | C | C | N |
| Acceso a red | {{pending: S / C / N}} | {{pending: definir}} | {{pending: definir}} | {{pending: definir}} | {{pending: definir}} |
| Crear ramas y commits | N | N | C | C | N |
| Hacer push, abrir pull requests | {{pending: S / C / N}} | N | N | C | N |
| Aprobar, integrar, desplegar | N | N | N | N | N |
| Leer secretos o credenciales | N | N | N | N | N |

Ajusta las columnas a los roles definidos en la arquitectura de agentes.

## Herramientas externas

| Herramienta o servidor | Propósito | Roles permitidos | Lectura o escritura |
| --- | --- | --- | --- |
| {{pending: nombre de la herramienta}} | {{pending: propósito}} | {{pending: roles}} | {{pending: lectura / escritura}} |

## Reglas

- Concede capacidades por tarea, no por comodidad.
- La escritura de pruebas y la de código no deberían pertenecer al mismo paso desatendido.
- Los cambios en esta matriz son estructurales: registra el motivo y quién aprobó.

## Revisión

- Cadencia de revisión: {{pending: cuándo se revisa esta matriz}}

## Relacionados

- [Arquitectura de agentes](agent-architecture.md)
- [Guardarraíles](guardrails.md)
- [Humano en el circuito](human-in-the-loop.md)
- [Puertas de calidad](../governance/quality-gates.md)
