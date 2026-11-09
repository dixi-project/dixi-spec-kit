# App frontend

## Propósito

Describir la estructura y las convenciones esperadas de un repositorio de frontend web. La app debe ser internacional desde el inicio: rutas con prefijo de idioma, contenido renderizado en servidor y señales SEO correctas por idioma. Esta guía no elige framework.

Estado: borrador. {{pending: elegir el framework frontend y la estrategia de renderizado}}

## Decisiones de stack

| Decisión | Elección | ADR |
|----------|----------|-----|
| Framework | {{pending}} | {{pending}} |
| Renderizado (en servidor, pre-render o híbrido) | {{pending}} | {{pending}} |
| Enfoque de estilos | {{pending}} | {{pending}} |
| Herramientas de pruebas unitarias y end-to-end | {{pending}} | {{pending}} |
| Idiomas soportados | ES, EN, {{pending: otros}} | {{pending}} |

## Estructura de carpetas sugerida

```text
<app>/
├── README.md
├── AGENTS.md
├── src/
│   ├── routes/[lang]/   # toda página pública vive bajo un prefijo de idioma
│   ├── components/      # piezas de presentación, sin texto hardcodeado
│   ├── features/        # pantallas agrupadas por spec de feature
│   ├── services/        # clientes de API generados o escritos desde contratos
│   └── i18n/            # detección de locale y utilidades
├── locales/
│   ├── en.json
│   └── es.json
├── public/
└── tests/
    ├── unit/
    └── e2e/
```

## Reglas de internacionalización

- Las URLs públicas llevan el idioma: `/es/...`, `/en/...`. Nunca cambiar de idioma solo en el cliente.
- La raíz `/` redirige al idioma que mejor coincida con el del navegador, con uno por defecto.
- Cada página emite una URL canónica de su propio idioma y alternativas `hreflang` para todos los idiomas, más `x-default`.
- El contenido se renderiza en servidor o se pre-renderiza, para que los crawlers vean el texto traducido sin ejecutar scripts.
- Todas las cadenas visibles vienen de los catálogos JSON; una clave faltante hace fallar el build o las pruebas.
- Fechas, números y monedas se formatean según el locale.

## Convenciones

- Las páginas siguen la plantilla de página y el estándar de accesibilidad.
- Los presupuestos de rendimiento se comprueban en las páginas clave.
- Sin secretos en el código cliente; solo la configuración pública llega al navegador.

{{pending: definir qué páginas son públicas e indexables y cuáles requieren sesión}}

## Relacionados

- [Repositorios](README.md)
- [Servicio backend](backend-service.md)
- [Política de i18n](../00-governance/policies/i18n-policy.md)
- [Plantilla de página](../10-engineering/templates/page-template.md)
- [Estándar de accesibilidad](../17-ux/accessibility-standard.md)
- [Presupuestos de web vitals](../11-quality/performance-budgets/web-vitals-budgets.md)
