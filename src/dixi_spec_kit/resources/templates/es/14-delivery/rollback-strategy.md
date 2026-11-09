# Estrategia de reversión

## Propósito

Hacer que volver a la última versión buena sea una acción rutinaria y ensayada, no una improvisación. Revertir es la primera respuesta por defecto ante una versión defectuosa.

## Reglas

- Cada versión conserva disponible el artefacto anterior durante {{pending: periodo o número de versiones}}.
- Revertir no requiere un build nuevo; vuelve a desplegar el artefacto anterior.
- Los cambios de base de datos siguen el patrón expandir y contraer para que la versión anterior siga funcionando tras una migración.
- Cualquier persona de la rotación de guardia puede revertir sin otra aprobación; volver a avanzar requiere la aprobación normal.

## Cuándo revertir

- Salta una alerta ligada a la versión durante el tiempo de observación.
- Falla una prueba de humo tras el despliegue.
- Las personas usuarias reportan una regresión en el flujo principal y la causa no es evidente en {{pending: minutos}}.

## Cómo revertir

| Componente | Mecanismo | Tiempo esperado | Verificado el |
|---|---|---|---|
| {{pending: web o sitio}} | {{pending: cambiar a la versión anterior}} | {{pending: minutos}} | {{pending: fecha del último ensayo}} |
| {{pending: servicio}} | {{pending: redesplegar el artefacto anterior}} | {{pending: minutos}} | {{pending: fecha}} |
| Configuración | Revertir el cambio de configuración en control de versiones | {{pending: minutos}} | {{pending: fecha}} |

## Cuando revertir no basta

- Cambios de datos irreversibles: restaurar desde un respaldo o aplicar un cambio correctivo; documéntalo en las notas de versión antes de desplegar.
- Mensajes ya enviados a terceros: planifica acciones compensatorias.
- En esos casos, despliega detrás de una feature flag para poder apagar la funcionalidad.

## Después de revertir

1. Confirma la recuperación con las mismas señales que dispararon la reversión.
2. Abre un registro de incidente y, si hubo personas usuarias afectadas, un postmortem.
3. Bloquea volver a publicar la versión defectuosa hasta que una corrección pase `make verify` y staging.

## Ensayo

Ensaya una reversión en staging {{pending: frecuencia}} y registra aquí el resultado.

## Relacionados

- [Estrategia de despliegue](deployment-strategy.md)
- [Visión general de CI/CD](ci-cd-overview.md)
- [Respuesta a incidentes](../13-security/incident-response.md)
- [Plantilla de postmortem](../10-engineering/templates/postmortem-template.md)
- [Reglas de alertas](../12-observability/alerting-rules.md)
