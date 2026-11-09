# Gobierno de datos

## Propósito

Definir quién es dueño de cada tipo de dato del proyecto, cómo se clasifica, quién puede acceder, cuánto tiempo se conserva y cómo se protege su calidad, para que las decisiones sobre datos sean explícitas y auditables.

Estado: borrador. {{pending: nombrar a la persona responsable del gobierno de datos}}

## Dueños de datos

| Conjunto de datos | Dueño | Custodio | Sistemas que lo contienen |
|-------------------|-------|----------|---------------------------|
| {{pending: p. ej. cuentas de clientes}} | {{pending: dueño}} | {{pending: custodio}} | {{pending: sistemas}} |

- El **dueño** decide propósito, acceso y retención.
- El **custodio** mantiene al día las definiciones, las reglas de calidad y la entrada del catálogo.

## Clasificación

| Nivel | Ejemplos | Tratamiento mínimo |
|-------|----------|--------------------|
| Público | Contenido publicado | Sin restricción. |
| Interno | Métricas operativas | Solo acceso autenticado. |
| Confidencial | Datos personales, contratos | Mínimo privilegio, cifrado, registro de accesos. |
| Restringido | Credenciales, datos personales sensibles | Acceso nominal, controles más fuertes, nunca en logs ni en contexto de agentes. |

Reglas detalladas para datos personales: [Clasificación de PII](../08-data/pii-classification.md).

## Catálogo y linaje

- Cada conjunto de datos tiene una entrada de catálogo: definición, dueño, clasificación, origen y consumidores.
- Los cambios de forma de un conjunto de datos pasan por un contrato y un plan de migración.
- {{pending: dónde vive el catálogo de datos}}

## Calidad

| Dimensión | Regla de ejemplo | Verificación |
|-----------|------------------|--------------|
| Completitud | Los campos obligatorios están presentes | {{pending: verificación}} |
| Validez | Los valores cumplen el formato permitido | {{pending: verificación}} |
| Unicidad | Sin claves de negocio duplicadas | {{pending: verificación}} |
| Oportunidad | Los datos se refrescan dentro de la ventana acordada | {{pending: verificación}} |

## Retención y borrado

- Cada conjunto de datos tiene un periodo de retención y un método de borrado: [Política de retención](../08-data/retention-policy.md).
- Las solicitudes de borrado de titulares se atienden en {{pending: plazo de respuesta}}.

## Acceso

- El acceso se concede por rol, se revisa {{pending: frecuencia de revisión}} y se retira al cambiar de rol.
- Los datos de producción no se copian a desarrollo; usa datos sintéticos o enmascarados.

## Datos e IA

- No se envían datos confidenciales ni restringidos a un modelo de IA sin una decisión explícita y registrada.
- Los datos usados para evaluar o ajustar modelos se clasifican como cualquier otro conjunto de datos.

## Relacionados

- [Base de seguridad](security-baseline.md)
- [Gobernanza de IA](ai-governance.md)
- [Principios](principles.md)
- [Controles de protección de datos](../13-security/data-protection-controls.md)
