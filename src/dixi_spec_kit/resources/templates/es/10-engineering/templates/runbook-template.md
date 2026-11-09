# Plantilla de runbook

## Propósito

Dar a la persona de guardia un procedimiento corto y probado para diagnosticar y resolver una
situación operativa conocida sin necesitar a quien lo escribió. Copia la estructura de abajo para
cada alerta o tarea.

## Plantilla

```markdown
# Runbook: <situación o nombre de la alerta>

Servicio: {{pending: componente afectado}}
Severidad: {{pending: escala de severidad y nivel}}
Responsable: {{pending: equipo o rol que mantiene este runbook}}
Última prueba: AAAA-MM-DD

## Cuándo usarlo

La alerta, síntoma o solicitud que activa este runbook.

## Impacto

Qué perciben los usuarios o sistemas mientras ocurre.

## Requisitos previos

- Accesos y permisos necesarios (nunca pegues credenciales aquí).
- Herramientas requeridas.

## Diagnóstico

1. Revisar ... (tablero, consulta de logs o comando, y cómo se ve lo "normal").
2. Confirmar ...

## Resolución

1. Paso, con el resultado esperado.
2. Paso, con el resultado esperado.

## Verificación

Cómo confirmar que el servicio volvió a estar sano.

## Reversión

Cómo deshacer los pasos de resolución si empeoran la situación.

## Escalamiento

A quién contactar, por qué canal y después de cuánto tiempo.

## Historial

| Fecha | Incidente o cambio | Notas |
|---|---|---|
```

## Notas

- Cada paso es una acción concreta con resultado esperado; evita "investigar".
- Prueba los runbooks periódicamente y después de cada incidente en que se usaron.

## Relacionados

- [Plantilla de postmortem](postmortem-template.md)
- [Estándar de código seguro](../secure-coding-standard.md)
- [Instrucciones del proyecto](../../AGENTS.md)
