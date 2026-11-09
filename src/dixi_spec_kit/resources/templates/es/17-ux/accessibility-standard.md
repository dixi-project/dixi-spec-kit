# Estándar de accesibilidad

## Propósito

Fijar el nivel de accesibilidad al que se compromete el proyecto y las revisiones que demuestran que cada funcionalidad lo cumple, para que las personas con discapacidad puedan percibir, operar y entender el producto en cada idioma soportado.

Estado: borrador. {{pending: confirmar el nivel de conformidad objetivo, por ejemplo WCAG 2.2 nivel AA}}

Este documento es un estándar de trabajo, no una declaración de conformidad. Solo puede afirmarse conformidad después de auditorías reales.

## Objetivo

| Elemento | Decisión |
|----------|----------|
| Guía y nivel | {{pending: versión de la guía y nivel}} |
| Alcance | {{pending: todas las páginas públicas y pantallas autenticadas, o un subconjunto}} |
| Tecnologías de apoyo soportadas | {{pending: lectores de pantalla, control por voz, magnificadores con los que probar}} |
| Navegadores y dispositivos soportados | {{pending: lista}} |

## Requisitos que cumple cada pantalla

### Perceptible

- Texto alternativo para imágenes con significado; las decorativas se ocultan a la tecnología de apoyo.
- Contraste de color de al menos 4.5:1 para texto normal y 3:1 para texto grande y componentes de interfaz.
- La información nunca se transmite solo con color.
- El contenido se reacomoda a 320 píxeles CSS de ancho y con zoom al 200 % sin pérdida.
- Subtítulos para video y transcripciones para audio.

### Operable

- Toda acción funciona solo con teclado, con indicador de foco visible y orden de foco lógico.
- Sin trampas de teclado; enlace para saltar al contenido principal.
- Áreas táctiles lo bastante grandes para tocarlas con comodidad.
- El movimiento y el contenido automático pueden pausarse; se respeta la preferencia de movimiento reducido.
- Los límites de tiempo pueden ampliarse o desactivarse.

### Comprensible

- El atributo `lang` está definido para la página y para cualquier pasaje en otro idioma.
- Los campos de formulario tienen etiquetas visibles; los errores explican qué falló y cómo corregirlo.
- La navegación y los nombres son consistentes entre páginas e idiomas.

### Robusto

- HTML semántico primero; ARIA solo cuando ningún elemento nativo sirve, y bien usado.
- Los mensajes de estado se anuncian a la tecnología de apoyo sin mover el foco.

## Verificación

| Revisión | Cuándo | Evidencia |
|----------|--------|-----------|
| Escaneo automático | Cada cambio, en el pipeline | {{pending: ubicación del reporte}} |
| Recorrido con teclado | Cada pantalla nueva | Notas en la especificación |
| Pasada con lector de pantalla | Antes de publicar una funcionalidad | Notas por idioma soportado |
| Auditoría por una persona calificada | {{pending: frecuencia}} | Informe de auditoría |

Las herramientas automáticas detectan solo una parte de los problemas; las revisiones manuales son obligatorias.

## Defectos

- Un defecto de accesibilidad que bloquea una tarea tiene la misma severidad que un defecto funcional que bloquea una tarea.
- {{pending: decidir dónde se recibe la retroalimentación de accesibilidad de los usuarios y en cuánto tiempo se responde}}

## Relacionados

- [Principios de diseño](design-principles.md)
- [Guía de contenido](content-guidelines.md)
- [Mapa de navegación](navigation-map.md)
- [Estrategia de aceptación](../11-quality/acceptance-strategy.md)
- [Requisitos no funcionales](../11-quality/non-functional-requirements.md)
- [Política de internacionalización](../00-governance/policies/i18n-policy.md)
