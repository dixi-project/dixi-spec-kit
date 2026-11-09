# Humano en el circuito

## Propósito

Indicar dónde debe decidir una persona, y por qué ahí y no en todas partes. Pedir confirmación en cada paso acostumbra a aceptar sin leer; los puntos de control humanos van donde un error es caro o irreversible.

## Dónde decide una persona

- **Qué se construye**: aprobar specs, contratos y las pruebas que los codifican.
- **Qué pasa a ser compartido o irreversible**: integrar, publicar, migrar datos, borrar.
- **Cuándo se relaja una regla**: excepciones a los guardarraíles o cambios de modo del proyecto.
- **Decisiones estructurales**: arquitectura, modelo de datos, dependencias externas, proveedores.

## En el desarrollo

| Momento | El agente puede | La persona debe |
| --- | --- | --- |
| Spec redactada | Redactar y comprobar la estructura | Validar las decisiones estructurales |
| Pruebas escritas | Redactar pruebas en rojo | Revisar que codifican los criterios |
| Código listo | Ejecutar comprobaciones y reportar resultados | Leer el diff y entenderlo |
| Pull request | Comentar y resumir | Aprobar e integrar |
| Publicación | Preparar notas | Decidir y ejecutar |

La revisión de un agente es un insumo útil; nunca es la aprobación.

## En el producto

Si un modelo puede disparar acciones para los usuarios:

1. La confirmación la emite el servidor, no el modelo, y queda ligada a la acción y los parámetros exactos.
2. Si los parámetros cambian después de confirmar, la confirmación deja de valer.
3. Cada confirmación se registra (quién, cuándo, qué acción) sin datos personales innecesarios.
4. Una prueba demuestra que se rechaza una acción sin confirmación válida.

Acciones que requieren confirmación: {{pending: listar las acciones del producto que necesitan confirmación humana}}

## Antipatrones

- Aprobar muchos cambios de agentes en minutos sin leerlos.
- Aceptar todo con «sí a todo»; si hay demasiadas preguntas, ajusta los permisos.
- Aprobar código que nadie del equipo sabe explicar.
- Que el autor apruebe su propio cambio.

## Decisiones del proyecto

- Número mínimo de revisores humanos: {{pending: número y rol}}

## Relacionados

- [Guardarraíles](guardrails.md)
- [Rastro de auditoría de IA](../governance/ai-audit-trail.md)
- [Metodología](../sdd/methodology.md)
- [Instrucciones del proyecto](../../AGENTS.md)
