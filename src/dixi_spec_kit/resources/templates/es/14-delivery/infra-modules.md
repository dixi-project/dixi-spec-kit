# Módulos de infraestructura

## Propósito

Explicar cómo se declara la infraestructura como código: qué herramienta, cómo se organizan los módulos y cómo se revisan y aplican los cambios. Este documento contiene reglas y decisiones; el código de infraestructura vive donde el proyecto decida, no en esta área.

## Decisiones

- Herramienta de infraestructura como código: {{pending: elegir con una matriz de selección y registrar en un ADR}}
- Ubicación en el repositorio: {{pending: ruta}}
- Almacenamiento del estado: {{pending: dónde, cómo se bloquea y quién puede leerlo}}

## Criterios de selección

| Criterio | Peso | Opción A | Opción B |
|---|---|---|---|
| Familiaridad del equipo | {{pending: peso}} | {{pending: puntuación}} | {{pending: puntuación}} |
| Soporte para el alojamiento elegido | {{pending: peso}} | {{pending: puntuación}} | {{pending: puntuación}} |
| Plan o vista previa antes de aplicar | {{pending: peso}} | {{pending: puntuación}} | {{pending: puntuación}} |
| Licencia y mantenimiento a largo plazo | {{pending: peso}} | {{pending: puntuación}} | {{pending: puntuación}} |

## Estructura de módulos

- Un módulo por bloque reutilizable (red, base de datos, servicio, sitio estático).
- Una composición por entorno que conecta los módulos con los valores del entorno.
- Los módulos reciben entradas y exponen salidas; sin valores globales ocultos.
- Las versiones de la herramienta y de los módulos están fijadas.

## Nombres y etiquetas

Cada recurso lleva: proyecto, entorno, componente, responsable. Patrón: {{pending: convención de nombres}}.

## Reglas de seguridad

- Los recursos que guardan datos están protegidos contra destrucción accidental.
- Sin secretos en el código ni en archivos de estado sin cifrar.
- Mínimo privilegio: el rol que aplica cambios en un entorno no puede tocar otro entorno.
- Nunca se aplican cambios a producción desde una máquina personal.

## Flujo de cambio

1. Abre un pull request con el cambio de infraestructura.
2. CI ejecuta `make verify`, formato, análisis estático y produce un plan o vista previa.
3. Quien revisa lee el plan, no solo el código.
4. Tras el merge, el plan se aplica a staging y luego a producción tras aprobación humana.

## Deriva

- Detecta diferencias entre el código y la realidad {{pending: frecuencia}}.
- Corrige la deriva mediante código, nunca editando recursos a mano.

## Relacionados

- [Entornos](environments.md)
- [Visión general de CI/CD](ci-cd-overview.md)
- [Arquitectura de despliegue](../09-architecture/deployment-architecture.md)
- [Gestión de secretos](../13-security/secret-management.md)
