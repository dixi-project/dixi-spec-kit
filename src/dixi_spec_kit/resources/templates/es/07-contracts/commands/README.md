# Contratos de comandos

## Propósito

Guardar los contratos de los comandos que un módulo envía a otro para pedir una acción («emitir
factura»). A diferencia de un evento, un comando tiene exactamente un destinatario previsto y puede
rechazarse. El contrato define qué se pide, quién puede pedirlo, qué valida quien lo atiende y cómo
conoce el resultado quien lo envía.

## Comandos frente a eventos

| Aspecto | Comando | Evento |
|---|---|---|
| Significado | Una petición para hacer algo | Un hecho que ya ocurrió |
| Tiempo verbal | Imperativo: `IssueInvoice` | Pasado: `InvoiceIssued` |
| Destinatarios | Exactamente uno | Ninguno o varios |
| Puede rechazarse | Sí | No, ya ocurrió |

## Estructura

```text
07-contracts/commands/
  <dominio>.<accion>.v<N>.json    Un contrato por comando y versión mayor
```

## Qué debe definir cada contrato de comando

- Nombre, versión, módulo que lo atiende, emisores permitidos y los IDs de funcionalidad que lo necesitan.
- Contenido con campos obligatorios y opcionales, reutilizando esquemas compartidos.
- Reglas de validación y las reglas de negocio (`BR-NNN`) que aplica quien lo atiende.
- Clave de idempotencia, para que un comando reintentado no se ejecute dos veces.
- Resultados: aceptado, rechazado con códigos de motivo o fallido; y cómo se informa al emisor
  (respuesta síncrona, evento de resultado o consulta de estado).
- Autorización: qué identidad y contexto de tenencia deben acompañar al comando.
- Tiempo de espera que asume el emisor y el comportamiento después.

## Índice de comandos

| Comando | Versión | Destinatario | Emisores | Canal de resultado | Estado |
|---|---|---|---|---|---|
| {{pending: nombre del comando}} | {{pending: versión}} | {{pending: módulo}} | {{pending: módulos}} | {{pending: respuesta o evento}} | {{pending: estado}} |

## Versionado

- Mismas reglas que los eventos: los cambios aditivos mantienen la versión y los incompatibles crean una nueva.
- El destinatario acepta la versión anterior durante {{pending: duración}} tras publicar una nueva.

## Relacionados

- [Contratos de eventos](../events/README.md)
- [Estándar de diseño de eventos](../../10-engineering/event-design-standard.md)
- [Esquemas](../schemas/README.md)
- [Reglas de negocio](../../01-business/rules/business-rules.md)
