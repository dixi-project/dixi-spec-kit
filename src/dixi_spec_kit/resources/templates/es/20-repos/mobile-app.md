# App móvil

## Propósito

Describir la estructura y las convenciones esperadas de un repositorio de app móvil. Esta guía no elige entre enfoque nativo o multiplataforma; fija lo que cualquier repositorio móvil debe contener para seguir alineado con las specs.

Estado: borrador. {{pending: elegir nativo o multiplataforma, el lenguaje y las versiones mínimas de sistema operativo}}

## Decisiones de stack

| Decisión | Elección | ADR |
|----------|----------|-----|
| Enfoque (nativo o multiplataforma) | {{pending}} | {{pending}} |
| Lenguaje y toolkit de UI | {{pending}} | {{pending}} |
| Versiones mínimas de sistema operativo | {{pending}} | {{pending}} |
| Almacenamiento offline | {{pending}} | {{pending}} |
| Herramientas de pruebas (unitarias y de UI) | {{pending}} | {{pending}} |

## Estructura de carpetas sugerida

```text
<app-movil>/
├── README.md
├── AGENTS.md
├── src/
│   ├── features/      # pantallas agrupadas por spec de feature
│   ├── components/    # UI reutilizable, sin texto hardcodeado
│   ├── services/      # clientes de API construidos desde contratos
│   ├── storage/       # persistencia local y sincronización
│   └── i18n/
├── locales/
│   ├── en.json
│   └── es.json
├── assets/
└── tests/
```

## Convenciones

- Todo texto visible viene de catálogos por idioma; la app sigue el idioma del dispositivo y permite cambiarlo manualmente.
- La app tolera versiones antiguas de la API mientras sigan en uso versiones antiguas de la app.
- Los datos sensibles se guardan solo en el almacenamiento seguro de la plataforma, nunca en archivos planos.
- El comportamiento offline se define por feature: qué funciona, qué se encola y qué se bloquea.
- Los permisos se piden en contexto, con una explicación y solo cuando hacen falta.
- Los deep links se corresponden con las mismas rutas con prefijo de idioma de la app web, si existe.

## Liberaciones

| Elemento | Valor |
|----------|-------|
| Cadencia de liberación | {{pending}} |
| Porcentaje de despliegue escalonado | {{pending}} |
| Política de actualización forzada | {{pending}} |
| Objetivo de sesiones sin fallos | {{pending}} |

## Verificación

- `make verify` ejecuta pruebas unitarias y comprobaciones estáticas; las pruebas de UI corren en {{pending: dispositivos o emuladores}}.
- La accesibilidad se revisa con lectores de pantalla y tamaños de texto grandes.

## Relacionados

- [Repositorios](README.md)
- [App frontend](frontend-app.md)
- [Servicio backend](backend-service.md)
- [Estándar de accesibilidad](../17-ux/accessibility-standard.md)
- [Política de i18n](../00-governance/policies/i18n-policy.md)
