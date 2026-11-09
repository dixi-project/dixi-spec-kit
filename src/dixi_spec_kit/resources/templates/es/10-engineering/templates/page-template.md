# Plantilla de página

## Propósito

Especificar una página de un sitio o aplicación: su objetivo, contenido, comportamiento por idioma
y cómo se comprueba. Sirve para sitios de contenido y para las páginas públicas de cualquier
producto. Copia la estructura de abajo para cada página.

## Plantilla

```markdown
# Página: <nombre legible>

ID: {{pending: ID de la página o feature}}
Ruta: /<idioma>/<ruta>
Idiomas: {{pending: idiomas soportados, p. ej. es, en}}
Responsable: {{pending: persona responsable del contenido}}

## Objetivo

Qué debe poder entender o hacer quien visita la página, y la métrica que indica
que funciona (p. ej. formulario de contacto enviado, documento descargado).

## Audiencia

Quién llega aquí y desde dónde (búsqueda, campaña, enlace interno).

## Contenido

| Bloque | Contenido | Origen del texto |
|---|---|---|
| Hero | | clave del catálogo de traducción |
| ... | | |

## Comportamiento

- Interacciones, formularios y validaciones.
- Estados vacío, cargando y error.

## SEO e internacionalización

- Título y meta descripción por idioma.
- URL canónica por idioma y alternativas `hreflang`.
- Renderizada en el servidor para que los buscadores vean el contenido traducido.

## Accesibilidad

- Orden de encabezados, textos alternativos, navegación por teclado, contraste.

## Comprobaciones

- [ ] Cada punto de aceptación tiene una comprobación automática o manual.
- [ ] La página se muestra en cada idioma soportado sin textos escritos en el código.
```

## Relacionados

- [Plantilla de feature](feature-template.md)
- [Estándares de código](../coding-standards.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
