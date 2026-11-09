# Rotación de claves

## Propósito

Definir cómo se rotan las claves criptográficas, claves de firma, certificados y credenciales de larga duración, tanto de forma programada como en emergencias, sin interrupciones y sin dejar material antiguo activo.

Estado: borrador. {{pending: nombrar al responsable de la rotación de claves}}

## Inventario

| Clave o credencial | Uso | Responsable | Periodo de rotación | Método | Última rotación |
|--------------------|-----|-------------|---------------------|--------|-----------------|
| {{pending: p. ej. clave de cifrado de datos}} | {{pending: uso}} | {{pending: responsable}} | {{pending: periodo}} | {{pending: automático / manual}} | {{pending: fecha}} |

Registra solo nombres y metadatos, nunca el material de la clave.

## Principios

- Prefiere credenciales de vida corta emitidas automáticamente frente a las de larga duración.
- Prefiere la rotación automática; la manual necesita un runbook escrito y un recordatorio en el calendario.
- Debe poder rotarse en cualquier momento, no solo según el calendario; practícalo.
- Cada clave tiene un único propósito.

## Procedimiento de rotación (sin interrupción)

1. Crea la nueva clave o credencial junto a la actual.
2. Despliega consumidores que acepten la antigua y la nueva.
3. Cambia los productores a la nueva clave.
4. Confirma que ningún tráfico usa ya la clave antigua (logs o métricas).
5. Revoca o desactiva la clave antigua; conserva acceso solo de descifrado si hay datos almacenados que dependen de ella.
6. Registra la fecha de rotación y quién la realizó.

## Rotación de emergencia

Se activa ante sospecha de filtración o compromiso. Omite los periodos de espera, revoca primero, acepta una interrupción breve si es necesario y después sigue la respuesta a incidentes. {{pending: definir quién puede activar una rotación de emergencia}}

## Datos cifrados con claves antiguas

{{pending: decidir si los datos almacenados se vuelven a cifrar tras la rotación o mantienen las claves antiguas en modo solo descifrado}}

## Verificación

- Se ejecuta un simulacro de rotación al menos {{pending: frecuencia}} en un entorno no productivo.
- Se generan alertas cuando una credencial supera su periodo de rotación.

## Relacionados

- [Gestión de secretos](secret-management.md)
- [Respuesta a incidentes](incident-response.md)
- [Acceso de emergencia](break-glass-access.md)
- [Modelo de amenazas](threat-model.md)
