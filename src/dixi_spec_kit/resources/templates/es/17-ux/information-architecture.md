# Arquitectura de información

## Propósito

Describir cómo se organizan, nombran y encuentran el contenido y las funciones del producto, para que los usuarios lleguen rápido a lo que necesitan y la estructura siga siendo coherente a medida que el producto crece y se traduce.

Estado: borrador. {{pending: validar la estructura de primer nivel con usuarios antes de construir la navegación}}

## Inventario de contenido

Lista los principales tipos de contenido y funciones antes de decidir la estructura.

| Elemento | Tipo | Público | Responsable | Idiomas | Notas |
|----------|------|---------|-------------|---------|-------|
| {{pending: por ejemplo configuración de la cuenta}} | Función | Usuarios con sesión | {{pending}} | es, en | — |
| {{pending: por ejemplo artículos de ayuda}} | Contenido | Todos | {{pending}} | es, en | — |

## Esquema de organización

{{pending: elegir cómo se agrupa el contenido, por ejemplo por tarea, por público o por tema}}

- Agrupa según el modelo mental del usuario, descubierto con investigación, no según la estructura interna de los equipos.
- Mantén pequeño el primer nivel (entre cinco y siete secciones).
- Evita secciones «Varios» u «Otros»; indican una estructura poco clara.

## Jerarquía

```text
/{lang}/
├── {{pending: sección 1}}/
│   ├── {{pending: página}}
│   └── {{pending: página}}
├── {{pending: sección 2}}/
└── ayuda/
```

## Reglas de URL e idioma

- Toda página pública vive bajo un prefijo de idioma, por ejemplo `/es/` y `/en/`.
- La raíz `/` redirige a la mejor coincidencia con el idioma del navegador.
- Cada versión de idioma tiene su propia URL canónica y alternativas `hreflang` hacia las demás.
- Los slugs pueden traducirse; registra la correspondencia para que las alternativas sigan enlazadas.
- Cambiar una URL exige una redirección permanente desde la anterior.

{{pending: decidir si los slugs se traducen o se mantienen iguales en todos los idiomas}}

## Etiquetado

- Las etiquetas usan las palabras de los usuarios, confirmadas con investigación como ordenamiento de tarjetas o pruebas de árbol.
- El mismo elemento tiene la misma etiqueta en todos los lugares donde aparece.
- Las etiquetas se traducen mediante el catálogo y se revisa su longitud en cada idioma.

## Búsqueda y localización

{{pending: decidir si el producto necesita búsqueda y qué contenido indexa}}

## Validación

| Método | Pregunta que responde | Estado |
|--------|-----------------------|--------|
| Ordenamiento de tarjetas | ¿Cómo agrupan los usuarios el contenido? | {{pending}} |
| Prueba de árbol | ¿Encuentran los usuarios los elementos en la estructura propuesta? | {{pending}} |

## Relacionados

- [Mapa de navegación](navigation-map.md)
- [Guía de contenido](content-guidelines.md)
- [Principios de diseño](design-principles.md)
- [Estrategia SEO](../25-growth/seo-strategy.md)
- [Estrategia de descubrimiento](../24-research/discovery-strategy.md)
