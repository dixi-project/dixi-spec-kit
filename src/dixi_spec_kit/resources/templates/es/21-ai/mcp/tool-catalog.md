# Catálogo de herramientas

## Propósito

Listar cada herramienta y recurso que los agentes o las features del producto pueden invocar mediante MCP o integraciones similares, con su riesgo y los controles que la rodean. Una herramienta que no esté en este catálogo no debe habilitarse.

## Niveles de riesgo

| Nivel | Descripción | Control requerido |
| --- | --- | --- |
| Lectura | Devuelve datos, sin efectos | Comprobación de acceso por llamante |
| Escritura | Cambia estado, reversible | Comprobación de acceso, log de auditoría |
| Destructiva | Efecto irreversible o externo | Comprobación de acceso, log de auditoría, confirmación humana |

## Catálogo

| Herramienta | Servidor | Descripción | Entradas | Riesgo | Roles permitidos | Pruebas |
| --- | --- | --- | --- | --- | --- | --- |
| {{pending: nombre de la herramienta}} | {{pending: definir}} | {{pending: definir}} | {{pending: referencia al esquema}} | {{pending: lectura / escritura / destructiva}} | {{pending: definir}} | {{pending: referencia a la prueba}} |

## Recursos

| Recurso | Servidor | Contenido | Sensibilidad | Roles permitidos |
| --- | --- | --- | --- | --- |
| {{pending: nombre del recurso}} | {{pending: definir}} | {{pending: definir}} | {{pending: público / interno / confidencial}} | {{pending: definir}} |

## Lista de alta

- [ ] Existe un contrato con esquema de entrada y salida.
- [ ] Nivel de riesgo asignado y controles correspondientes implementados.
- [ ] Las pruebas cubren la denegación de permisos y las entradas inválidas.
- [ ] Los roles permitidos se reflejan en la matriz de capacidades.
- [ ] Herramientas de terceros revisadas, con versión fijada.

## Retirar una herramienta

Deshabilítala primero en el servidor y luego quítala de este catálogo y de la matriz de capacidades en el mismo cambio.

## Relacionados

- [Arquitectura MCP](mcp-architecture.md)
- [Matriz de capacidades](../agents/capability-matrix.md)
- [Humano en el circuito](../agents/human-in-the-loop.md)
- [Rastro de auditoría de IA](../governance/ai-audit-trail.md)
