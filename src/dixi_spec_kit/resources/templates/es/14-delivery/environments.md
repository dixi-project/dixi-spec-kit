# Entornos

## Propósito

Listar los entornos que usa el proyecto, para qué sirve cada uno, qué datos contiene y cómo pasa un cambio de uno a otro. Pocos entornos fieles valen más que muchos que se desvían.

## Catálogo de entornos

| Entorno | Propósito | Datos | Acceso | Despliega | Vida |
|---|---|---|---|---|---|
| local | Desarrollo y retroalimentación rápida | Fixtures sintéticos | Desarrollador/a | Desarrollador/a | Efímero |
| preview | {{pending: por pull request, opcional}} | Sintéticos | Equipo | Automático en el pull request | Se borra al hacer merge |
| staging | Validación previa a la versión, lo más parecido a producción que sea práctico | {{pending: sintéticos o anonimizados}} | Equipo | {{pending: automático tras merge o manual}} | Permanente |
| production | Personas usuarias reales | Reales | {{pending: roles restringidos}} | Tras aprobación humana | Permanente |

## Reglas de paridad

- Mismo artefacto, mismas claves de configuración, distintos valores por entorno.
- Las diferencias de staging respecto a producción se listan aquí con su motivo: {{pending: listar diferencias conocidas}}.
- Los datos de producción nunca van a entornos no productivos salvo que se anonimicen de forma irreversible y la decisión quede registrada.

## Configuración

| Ajuste | local | staging | production |
|---|---|---|---|
| Nivel de log | debug | info | info |
| Integraciones externas | Stubs | {{pending: sandbox o stubs}} | Reales |
| Correo saliente | Capturado en local | {{pending: capturado o lista permitida}} | Real |
| Feature flags | Todas activas | {{pending: por flag}} | {{pending: por flag}} |

Las direcciones de correo de prueba usan el dominio `@example.com`.

## Acceso y aislamiento

- Las credenciales son distintas por entorno; una credencial de staging nunca funciona en producción.
- Quién tiene acceso de escritura a producción: {{pending: roles}}
- Cómo se revisa el acceso: {{pending: frecuencia y responsable}}

## Promoción

Un cambio llega a producción solo después de pasar por staging con el mismo identificador de commit y una aprobación humana explícita.

## Relacionados

- [Visión general de CI/CD](ci-cd-overview.md)
- [Estrategia de despliegue](deployment-strategy.md)
- [Arquitectura de despliegue](../09-architecture/deployment-architecture.md)
- [Gestión de secretos](../13-security/secret-management.md)
