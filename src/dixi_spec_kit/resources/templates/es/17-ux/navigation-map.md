# Mapa de navegación

## Propósito

Registrar cada pantalla o página, cómo se mueven los usuarios entre ellas y qué elementos de navegación las conectan, para que ninguna pantalla quede huérfana, cada camino tenga regreso y los enlaces sean correctos en cada idioma.

Estado: borrador. {{pending: confirmar la lista de pantallas de la primera versión}}

## Navegación global

| Elemento | Contenido | Visible para | Notas |
|----------|-----------|--------------|-------|
| Menú principal | {{pending: secciones de primer nivel}} | {{pending: todos o usuarios con sesión}} | Mismo orden en cada idioma |
| Selector de idioma | Idiomas soportados, cada uno con su propio nombre | Todos | Enlaza a la misma página en el otro idioma, no al inicio |
| Pie de página | {{pending: legal, ayuda, contacto}} | Todos | — |
| Menú de cuenta | {{pending}} | Usuarios con sesión | — |

## Inventario de pantallas

| ID | Pantalla | Patrón de ruta | Entradas | Salidas | Sesión | Plantilla |
|----|----------|----------------|----------|---------|--------|-----------|
| SCR-001 | Inicio | `/{lang}/` | Redirección de la raíz, logotipo | Menú principal | No | {{pending}} |
| SCR-002 | {{pending}} | `/{lang}/{{pending}}` | {{pending}} | {{pending}} | {{pending}} | {{pending}} |
| SCR-404 | No encontrada | cualquier ruta desconocida | Enlaces rotos | Inicio, búsqueda | No | Error |

## Flujos clave

Describe los recorridos principales como pasos ordenados.

```text
Flujo: {{pending: por ejemplo registro}}
SCR-001 Inicio → SCR-00x Registro → SCR-00y Confirmar correo → SCR-00z Bienvenida
```

- Cada flujo indica su inicio, su final exitoso y qué pasa ante una falla o cancelación.
- Cada paso puede alcanzarse y abandonarse solo con teclado.
- Volver atrás conserva los datos del usuario cuando es razonable.

## Reglas

- Cada pantalla tiene al menos una entrada y una salida; las pantallas huérfanas son defectos.
- Las migas de pan o un título visible indican al usuario dónde está.
- Los enlaces profundos funcionan: abrir una URL directa muestra la pantalla correcta en el idioma correcto, o pide iniciar sesión y luego regresa al usuario.
- Las redirecciones después de iniciar sesión conservan el prefijo de idioma.

{{pending: decidir el comportamiento cuando una página existe en un idioma pero no en otro}}

## Mantenimiento

- Actualiza este mapa en el mismo cambio que agrega, renombra o elimina una pantalla.
- Mantén estables los ID de pantalla; referéncialos desde especificaciones y pruebas.

## Relacionados

- [Arquitectura de información](information-architecture.md)
- [Estándar de accesibilidad](accessibility-standard.md)
- [Principios de diseño](design-principles.md)
- [Plantilla de página](../10-engineering/templates/page-template.md)
- [Especificación de ejemplo](../05-features/example/feature-spec.md)
