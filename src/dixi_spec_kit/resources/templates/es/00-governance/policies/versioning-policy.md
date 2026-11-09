# Política de versiones

## Propósito

Definir cómo se versionan el proyecto, sus contratos públicos y sus documentos, para que los consumidores sepan qué cambió y si una actualización puede romperles algo.

Estado: borrador. {{pending: confirmar el esquema de versiones}}

## Versión del producto

- Esquema: {{pending: p. ej. versionado semántico MAYOR.MENOR.PARCHE, o versionado por calendario}}
- Con versionado semántico:
  - **MAYOR** para cambios incompatibles en el comportamiento o los contratos públicos.
  - **MENOR** para funcionalidades compatibles hacia atrás.
  - **PARCHE** para correcciones compatibles hacia atrás.
- Las versiones preliminares usan un sufijo, por ejemplo `1.4.0-rc.1`.

## Contratos

| Tipo de contrato | Cómo se expresa la versión | Regla ante cambio incompatible |
|------------------|----------------------------|--------------------------------|
| APIs HTTP | {{pending: ruta, cabecera o tipo de medio}} | Nueva versión mayor; la anterior se declara obsoleta, no se retira de golpe |
| Eventos | Campo de versión en el esquema | Nueva versión del evento; los consumidores migran |
| Archivos y exportaciones | Versión en la cabecera o el nombre | Documentado en las notas del release |

## Versión del kit

- La versión de DIXI Spec Kit usada para crear el proyecto se registra en `.dixi/project.json`.
- Actualizar el kit es un cambio revisado, como cualquier otro.

## Registro de cambios

- Cada release tiene notas: añadido, cambiado, obsoleto, eliminado, corregido, seguridad.
- Los cambios incompatibles incluyen una nota de migración.
- {{pending: dónde vive el registro de cambios}}

## Obsolescencia

- Anuncia las obsolescencias con al menos {{pending: plazo de aviso}} antes de retirar.
- Mantén probado el comportamiento obsoleto hasta que se retire.

## Quién decide

- Los cambios de versión se proponen en el pull request del release y los confirma {{pending: rol}}.

## Relacionados

- [Estrategia de ramas](branching-strategy.md)
- [Política de documentación](documentation-policy.md)
- [Contrato de ejemplo](../../07-contracts/example.md)
