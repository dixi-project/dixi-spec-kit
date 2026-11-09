# Guía de contenido

## Propósito

Definir cómo habla el producto: voz, tono, terminología y formato para textos de interfaz, contenido de ayuda y mensajes en cada idioma soportado, para que el producto suene como uno solo y las traducciones se mantengan consistentes.

Estado: borrador. {{pending: nombrar a la persona que aprueba los textos de interfaz y al revisor de cada idioma}}

## Voz

La voz es constante; el tono se adapta a la situación.

| Rasgo | Significa | No significa |
|-------|-----------|--------------|
| {{pending: por ejemplo claro}} | Frases cortas, palabras comunes | Simplificar de más u ocultar detalles |
| {{pending: por ejemplo útil}} | Dice al usuario qué hacer después | Sermonear |
| {{pending: por ejemplo respetuoso}} | Lenguaje neutral e inclusivo | Bromas a costa del usuario |

## Tono según la situación

| Situación | Tono | Ejemplo |
|-----------|------|---------|
| Éxito | Breve, positivo | «Cambios guardados.» |
| Error que el usuario puede corregir | Tranquilo, concreto, accionable | «Escribe una fecha posterior a hoy.» |
| Falla del sistema | Honesto, con disculpa y siguiente paso | «No pudimos cargar tus reportes. Inténtalo de nuevo en unos minutos.» |
| Acción destructiva | Serio, con la consecuencia explícita | «¿Eliminar el proyecto? Se borrarán todos sus archivos.» |

## Reglas de redacción

- Usa la segunda persona y la voz activa.
- Pon primero la palabra más importante; los botones empiezan con un verbo («Guardar cambios», no «Aceptar»).
- Evita jerga, nombres internos y abreviaturas que el usuario no conoce.
- Usa lenguaje inclusivo y neutral en género cuando el idioma lo permita.
- Nunca culpes al usuario en los mensajes de error.

{{pending: decidir la forma de tratamiento en cada idioma, por ejemplo tú o usted en español}}

## Internacionalización

- Todo texto de interfaz vive en catálogos por idioma; nada de textos fijos en los componentes.
- Escribe textos fuente fáciles de traducir: frases completas, sin concatenar cadenas, con marcadores con nombre (`{count} archivos`).
- Resuelve plurales y género con las reglas de plural del catálogo, no con código.
- Prevé una expansión del texto de 30 % o más; nunca fijes anchos pensando en un solo idioma.
- Fechas, números, monedas y unidades siguen la configuración regional del usuario.
- Cada idioma lo revisa una persona con dominio del idioma; la traducción automática sola no basta para publicar.

## Terminología

Mantén un glosario de términos del producto y su traducción aprobada.

| Término (en) | Término (es) | Definición | Evitar |
|--------------|--------------|------------|--------|
| {{pending}} | {{pending}} | {{pending}} | {{pending}} |

## Formato

- Solo mayúscula inicial en títulos y botones.
- {{pending: decidir el estilo de listas, números y puntuación en cada idioma}}

## Relacionados

- [Principios de diseño](design-principles.md)
- [Estándar de accesibilidad](accessibility-standard.md)
- [Arquitectura de información](information-architecture.md)
- [Política de internacionalización](../00-governance/policies/i18n-policy.md)
- [Glosario](../18-knowledge-base/glossary.md)
