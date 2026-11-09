# Servicio backend

## Propósito

Describir la estructura y las convenciones esperadas de un repositorio de servicio backend: la pieza que expone una API, contiene las reglas de negocio y persiste datos. Esta guía no crea código ni elige lenguaje; define lo que todo repositorio backend debe contener para seguir alineado con las specs.

Estado: borrador. {{pending: elegir lenguaje, framework y runtime para los servicios backend}}

## Decisiones de stack

| Decisión | Elección | ADR |
|----------|----------|-----|
| Lenguaje y runtime | {{pending}} | {{pending}} |
| Framework web | {{pending}} | {{pending}} |
| Persistencia y herramienta de migraciones | {{pending}} | {{pending}} |
| Ejecutor de pruebas | {{pending}} | {{pending}} |
| Formato de descripción de la API | {{pending}} | {{pending}} |

## Estructura de carpetas sugerida

```text
<servicio>/
├── README.md          # propósito, ejecución local, IDs de spec implementados
├── AGENTS.md          # reglas para agentes en este repositorio
├── src/
│   ├── api/           # capa de transporte: rutas, mapeo de request/response
│   ├── domain/        # reglas de negocio, sin imports de framework ni de E/S
│   ├── application/   # casos de uso que orquestan dominio y adaptadores
│   └── adapters/      # base de datos, colas, servicios externos
├── migrations/        # cambios de esquema versionados
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/      # comprobaciones contra los contratos publicados
├── locales/           # mensajes visibles al usuario por idioma
└── .env.example       # solo nombres de variables
```

Adapta los nombres al stack elegido, pero conserva la separación entre transporte, dominio y adaptadores.

## Convenciones

- La API sigue los contratos de `07-contracts/`; el cambio de contrato va primero.
- Los errores usan una forma documentada con un código estable y una clave de mensaje traducible.
- Cada petición lleva un ID de correlación que llega a los logs.
- La configuración viene del entorno; los secretos vienen del almacén de secretos elegido.
- Los mensajes devueltos al usuario se resuelven por idioma, usando el locale de la petición.
- Existen endpoints de salud y disponibilidad, baratos de llamar.
- Las migraciones solo avanzan y se revisan como código.

## Verificación

- `make verify` (o su equivalente) ejecuta linting y pruebas unitarias, de integración y de contrato.
- Todo comportamiento nuevo empieza con una prueba fallida enlazada a un ID de spec.

{{pending: definir la cobertura mínima y qué comprobaciones bloquean un merge}}

## Relacionados

- [Repositorios](README.md)
- [App frontend](frontend-app.md)
- [Estándares de código](../10-engineering/coding-standards.md)
- [Estándar de código seguro](../10-engineering/secure-coding-standard.md)
- [Gestión de secretos](../13-security/secret-management.md)
- [Contrato de ejemplo](../07-contracts/example.md)
