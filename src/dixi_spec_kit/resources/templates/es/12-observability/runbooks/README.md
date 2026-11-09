# Runbooks

## Propósito

Explicar cómo escribir los runbooks a los que apuntan las alertas. Un runbook permite que una persona que no construyó el componente restablezca el servicio a las 3 a. m. siguiendo pasos, sin adivinar.

## Cuándo escribir uno

- Toda alerta con severidad `critical` o `warning` enlaza a un runbook.
- Toda operación manual recurrente (rotar una credencial, reprocesar una cola) tiene uno.
- Tras un incidente, crea o actualiza el runbook que habría ayudado.

## Cómo escribirlo

1. Copia la [plantilla de runbook](../../10-engineering/templates/runbook-template.md) en esta carpeta como `<sintoma>.md`, nombrado según lo que se observa, no según la causa sospechada.
2. Describe el síntoma y cómo lo detecta la alerta.
3. Lista las primeras comprobaciones en orden, de la más barata a la más costosa.
4. Da pasos de mitigación que reduzcan primero el impacto en las personas usuarias; la causa raíz viene después.
5. Indica cuándo escalar y a quién.
6. Explica cómo confirmar la recuperación.
7. Pruébalo: otra persona lo sigue en un entorno no productivo.

## Reglas de estilo

- Pasos cortos en imperativo; una acción por paso.
- Los comandos están listos para copiar y es seguro ejecutarlos dos veces; los pasos destructivos lo dicen en negrita y piden confirmación.
- Nunca incluyas secretos; indica dónde se guardan.
- Enlaza los tableros por su nombre en el mapa de tableros.

## Ejemplo (neutral)

> **Síntoma:** la acumulación de la cola crece durante más de 10 minutos.
>
> 1. Abre el tablero de trabajo asíncrono y comprueba si los consumidores están corriendo.
> 2. Si no hay consumidores, reinícialos con el procedimiento documentado.
> 3. Si corren pero fallan, revisa los últimos logs de error del consumidor y el conteo de mensajes muertos.
> 4. Si los fallos empezaron tras una versión, revierte esa versión.
> 5. Escala a la persona responsable del componente si la acumulación no baja 15 minutos después de mitigar.
> 6. Recuperación: acumulación en descenso y sin nuevos mensajes muertos.

Los números del ejemplo son ilustrativos; fija los umbrales reales en las reglas de alertas.

## Índice

| Runbook | Alerta | Responsable | Última prueba |
|---|---|---|---|
| {{pending: primer runbook}} | {{pending: nombre de la alerta}} | {{pending: rol}} | {{pending: fecha}} |

## Relacionados

- [Reglas de alertas](../alerting-rules.md)
- [Mapa de tableros](../dashboard-map.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
- [Plantilla de postmortem](../../10-engineering/templates/postmortem-template.md)
