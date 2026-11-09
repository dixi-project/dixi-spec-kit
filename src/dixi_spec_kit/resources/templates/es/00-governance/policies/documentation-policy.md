# Política de documentación

## Propósito

Definir cómo se escriben, nombran, enlazan y mantienen los documentos del proyecto, para que las specs sigan siendo legibles para las personas y útiles para los agentes, y `dixi check` pueda seguir la cadena de trazabilidad.

Estado: borrador. {{pending: confirmar las reglas de documentación con el equipo}}

## Idioma

- Idioma principal de la documentación: {{pending: idioma principal}}
- Documentos que también deben existir en otros idiomas: {{pending: lista}}
- Las traducciones mantienen las mismas secciones e IDs que el original.

## Formato

- Markdown, un tema por archivo, nombres de archivo en minúsculas y `kebab-case`.
- Todo documento empieza con `# Título`, sigue con `## Propósito` y termina con `## Relacionados`.
- Usa tablas y checklists para reglas; usa prosa para el razonamiento.
- Envuelve comandos, rutas e identificadores entre comillas invertidas.

## Estructura mínima

```markdown
# <Título>

## Propósito

<Por qué existe este documento, en una o dos frases.>

Estado: borrador | revisión | aprobado.

## <Secciones de contenido>

## Relacionados

- <enlace relativo a un documento relacionado>
```

## Decisiones abiertas

- Marca cada punto sin decidir como `{{pending: qué decidir}}`.
- No inventes valores para rellenar un hueco. Un hueco visible es mejor que una respuesta equivocada.
- Resuelve los marcadores pendientes antes de que un documento pase a `aprobado`.

## Enlaces

- Usa enlaces relativos a archivos locales; comprueba que resuelven.
- Enlaza en ambos sentidos entre specs padre e hijas (objetivo, dominio, módulo, funcionalidad, contrato, prueba).

## Trazabilidad

- Las specs mantienen IDs estables (por ejemplo `FEATURE-001`).
- Registra cada elemento trazable y sus padres en `.dixi/traceability.json`.
- Ejecuta `dixi check` antes de pedir revisión.

## Propiedad y revisión

| Tipo de documento | Responsable | Disparador de revisión |
|-------------------|-------------|------------------------|
| Gobernanza | {{pending: responsable}} | Cualquier cambio |
| Specs | Responsable de la funcionalidad | Antes de implementar |
| Runbooks | {{pending: responsable}} | Tras cada incidente |

## Relacionados

- [Convenciones de nombres](naming-conventions.md)
- [Política de i18n](i18n-policy.md)
- [Flujo documental](../../docs/guide.md)
- [Proyecto](../../00-master-spec.md)
