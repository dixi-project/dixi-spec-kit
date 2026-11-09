# Política de internacionalización

## Propósito

Asegurar que el producto se diseña para más de un idioma y región desde el inicio, para que añadir un idioma sea una tarea de traducción y no una reescritura, y para que cada idioma pueda encontrarse en los buscadores.

Estado: borrador. {{pending: confirmar idiomas y mercados soportados}}

## Idiomas soportados

| Idioma | Código | Estado | Responsable de traducciones |
|--------|--------|--------|-----------------------------|
| Inglés | `en` | Obligatorio | {{pending: responsable}} |
| Español | `es` | Obligatorio | {{pending: responsable}} |
| {{pending: p. ej. portugués}} | {{pending: código}} | Planificado | {{pending: responsable}} |

Idioma por defecto: {{pending: idioma por defecto}}

## Reglas

1. **Sin textos de usuario en el código.** Todos los textos viven en un catálogo por idioma, por ejemplo `locales/es.json`.
2. **Idioma en la URL.** Las páginas públicas usan un prefijo de idioma (`/es/`, `/en/`). El idioma nunca se cambia solo en el cliente.
3. **Redirección de la raíz.** `/` redirige al idioma que mejor coincide con la preferencia del visitante, con el idioma por defecto como respaldo.
4. **Enlaces alternativos.** Cada página pública declara `<link rel="alternate" hreflang="...">` para cada idioma y un `x-default`.
5. **URL canónica por idioma.** Cada página traducida es su propia URL indexable.
6. **Traducción en el servidor.** El contenido traducido se renderiza en el servidor o se pre-renderiza para que los rastreadores lo vean sin ejecutar scripts.
7. **Formatos según la configuración regional.** Fechas, números, monedas y unidades usan formato regional, nunca concatenación de cadenas.
8. **Expansión del texto.** Los diseños toleran textos entre un 30 y un 40 % más largos que en inglés.

## Reglas de catálogo

- Las claves son estables y semánticas: `checkout.summary.total`.
- Las claves que faltan hacen fallar las pruebas en desarrollo; nunca se muestran claves sin traducir al usuario.
- Plurales y género usan las reglas de plural del catálogo, no ramas de código.
- Quien traduce recibe contexto: una descripción o captura por clave.

## Contenido y documentación

- Los mensajes del producto y la documentación existen en cada idioma obligatorio.
- Una persona cualificada revisa los textos legales y de políticas por mercado.

## Checklist para una pantalla o página nueva

- [ ] Todos los textos vienen de los catálogos.
- [ ] La ruta tiene prefijo de idioma y enlaces alternativos.
- [ ] Fechas, números y monedas tienen formato regional.
- [ ] Diseño comprobado con el idioma más largo.
- [ ] Las pruebas cubren al menos dos idiomas.

## Relacionados

- [Convenciones de nombres](naming-conventions.md)
- [Política de documentación](documentation-policy.md)
- [Principios](../principles.md)
