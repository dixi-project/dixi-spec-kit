# Arquitectura de memoria

## Propósito

Definir qué recuerdan los agentes y las features con IA entre pasos y sesiones, dónde vive esa memoria, quién puede leerla y cuándo se borra. El repositorio sigue siendo la fuente de verdad; la memoria nunca sustituye a las specs.

## Capas

| Capa | Contenido | Duración | Ubicación |
| --- | --- | --- | --- |
| De trabajo | Contexto de la tarea actual | Una petición o sesión | En el proceso del agente |
| Notas de sesión | Decisiones y preguntas abiertas de una sesión | Días | Carpeta privada sin versionar (por ejemplo `.context/`) |
| Conocimiento del proyecto | Specs, contratos, decisiones, pruebas | Vida del proyecto | Repositorio, versionado |
| Índice derivado | Índice de búsqueda o grafo construido desde el repositorio | Se reconstruye al cambiar | {{pending: si se usa un índice y dónde}} |
| Memoria del producto | Estado por usuario que usan las features con IA | {{pending: retención}} | {{pending: almacenamiento}} |

## Reglas

- Si la información puede vivir en la documentación del repositorio, ponla ahí y no en la memoria del agente.
- La memoria nunca es lugar para secretos ni credenciales.
- Un índice derivado es desechable: puede reconstruirse desde el repositorio en cualquier momento.
- Las notas de sesión son privadas y no se versionan; lleva las decisiones a las specs antes de cerrar la sesión.

## Memoria del producto

Si una feature del producto recuerda información del usuario:

- Qué se guarda y para qué: {{pending: datos guardados y finalidad}}
- Visibilidad y borrado: el usuario puede ver y borrar lo que se recuerda.
- Aislamiento: la memoria de un usuario nunca se recupera para otro; una prueba lo demuestra.
- La retención y las solicitudes de borrado siguen la política de datos del proyecto.

## Acceso

| Capa | Lectores | Escritores |
| --- | --- | --- |
| Notas de sesión | La persona y sus agentes | Los mismos |
| Conocimiento del proyecto | Todos con acceso al repositorio | Mediante pull requests revisados |
| Memoria del producto | {{pending: servicios y roles}} | {{pending: servicios y roles}} |

## Exposición mediante herramientas

Si la memoria se expone a los agentes como recursos MCP, registra cada recurso en el catálogo de herramientas con su sensibilidad.

## Relacionados

- [Arquitectura MCP](../mcp/mcp-architecture.md)
- [Catálogo de herramientas](../mcp/tool-catalog.md)
- [Estrategia de contexto](../llm/context-strategy.md)
- [IA responsable](../governance/responsible-ai.md)
