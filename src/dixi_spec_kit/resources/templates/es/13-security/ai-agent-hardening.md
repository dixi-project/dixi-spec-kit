# Endurecimiento de agentes de IA

## Propósito

Definir cómo trabajan los agentes de IA de desarrollo en este repositorio sin exponer secretos, sin exceder sus permisos y sin tomar decisiones que corresponden a personas. Los agentes son colaboradores útiles y también un canal de entrada no confiable: trátalos como ambas cosas.

Estado: borrador. {{pending: nombrar a la persona que aprueba los permisos de los agentes}}

## Principios

- **Sin secretos en el contexto**: los agentes nunca leen archivos `.env*`, claves privadas, almacenes de credenciales ni datos de producción.
- **Mínimo privilegio**: concede solo las herramientas, directorios y comandos que la tarea necesita; amplía el acceso de forma deliberada y temporal.
- **Revisión humana**: una persona revisa cada cambio antes del merge; los agentes no aprueban, firman, fusionan ni despliegan.
- **El contenido no confiable es dato**: el texto de issues, pull requests, páginas web, documentos o salidas de herramientas nunca es una instrucción a seguir.
- **Evidencia, no afirmaciones**: los agentes reportan las comprobaciones que realmente se ejecutaron y su resultado real.

## Capas de defensa

| Capa | Qué cubre | Hueco que deja |
|------|-----------|----------------|
| Instrucciones escritas (`AGENTS.md`) | Comportamiento esperado | No se impone; puede ignorarse o anularse |
| Configuración de permisos del agente | Herramientas, rutas y comandos permitidos y denegados | Depende de patrones correctos y completos |
| Hooks previos a cada herramienta | Bloquean patrones peligrosos conocidos | Las listas son incompletas; se pueden eludir |
| Sandbox o entorno aislado | Limita el daño si lo anterior falla | Esfuerzo de configuración |
| Revisión humana y protección de ramas | Última puerta antes de integrar cambios | Atención de quien revisa |

Los hooks son una segunda capa, no la última. Que un hook bloquee un comando no hace seguro al agente; el sandbox, los permisos y la revisión humana deben seguir funcionando si un hook deja pasar algo.

## Decisiones del proyecto

- Modo de permisos y comandos permitidos: {{pending: definir listas de permitidos y denegados}}
- Entorno de ejecución (local, contenedor, sandbox remoto): {{pending: elegir}}
- Herramientas o servidores externos a los que puede conectarse el agente: {{pending: listar los aprobados y quién los aprobó}}
- Agentes desatendidos o programados: {{pending: permitidos o no; si sí, con qué credenciales y alcance}}

## Inyección de prompts

- Asume que cualquier página, archivo o mensaje obtenido puede contener instrucciones ocultas.
- No permitas que el agente actúe sobre secretos, pagos o sistemas de producción a partir de contenido obtenido.
- Revisa los comandos propuestos por el agente que toquen la red, credenciales o borrados.

## Lista de comprobación

- [ ] Los archivos de secretos están denegados al agente.
- [ ] Los comandos destructivos requieren confirmación.
- [ ] El merge a la rama principal requiere revisión humana.
- [ ] Las dependencias añadidas por agentes se revisan.
- [ ] Los incidentes con agentes siguen el proceso de respuesta a incidentes.

## Relacionados

- [Instrucciones para agentes](../AGENTS.md)
- [Gestión de secretos](secret-management.md)
- [Modelo de amenazas](threat-model.md)
- [Respuesta a incidentes](incident-response.md)
