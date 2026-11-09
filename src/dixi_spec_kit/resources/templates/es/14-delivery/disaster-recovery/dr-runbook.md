# Runbook de recuperación ante desastres

## Propósito

Dar el procedimiento paso a paso a seguir una vez declarado un desastre. Supone que quien lo ejecuta está bajo presión: los pasos son cortos, ordenados y seguros de repetir.

## Antes de empezar

- Desastre declarado por: {{pending: rol con derechos de decisión}}
- Canal y registro del incidente abiertos: {{pending: dónde}}
- Roles asignados: líder del incidente, operador/a, comunicación, registro.
- El acceso de emergencia, si hace falta, sigue el procedimiento de acceso de emergencia y queda registrado.

## Procedimiento

1. **Evaluar.** Confirma el alcance: qué capacidades y niveles están afectados. Consulta la matriz RTO/RPO.
2. **Contener.** Detén el daño: bloquea credenciales comprometidas, pausa tareas y workers que puedan escribir datos erróneos.
3. **Decidir.** Elige el camino de recuperación (restaurar en el sitio, conmutar a otra ubicación, modo degradado) y registra quién decidió y cuándo.
4. **Preparar el destino.** Recrea la infraestructura desde código versionado en la ubicación de recuperación: {{pending: referencia al comando o pipeline}}.
5. **Restaurar datos.** Restaura el último respaldo válido o el punto en el tiempo previo al fallo; registra el punto de restauración.
6. **Restaurar secretos y configuración.** Desde la ubicación secundaria: {{pending: dónde}}.
7. **Desplegar.** Despliega el último artefacto bueno conocido mediante el pipeline de versión; la aprobación humana sigue aplicando.
8. **Verificar.** Resultado de `make verify` del artefacto, comprobación de versión, pruebas de humo y comprobaciones de integridad de datos.
9. **Cambiar el tráfico.** Dirige a las personas usuarias al sistema recuperado: {{pending: mecanismo}}.
10. **Monitorear.** Vigila errores, latencia y acumulación durante {{pending: duración}}.

## Comunicación

| Audiencia | Canal | Cuándo | Responsable |
|---|---|---|---|
| Equipo interno | {{pending: canal}} | Al declarar y cada {{pending: minutos}} | Comunicación |
| Personas usuarias | {{pending: página de estado o canal}} | {{pending: cuándo}} | Comunicación |
| Reguladores o clientes con contrato | {{pending: canal}} | {{pending: plazo}} | {{pending: rol}} |

## Vuelta a la normalidad

- Vuelve a la ubicación principal solo cuando esté estable, con una ventana planificada y aprobación.
- Concilia los datos escritos durante el desastre.
- Escribe un postmortem y actualiza este runbook con lo que faltó.

## Relacionados

- [Estrategia de recuperación ante desastres](dr-strategy.md)
- [Matriz RTO y RPO](rto-rpo-matrix.md)
- [Respaldo y recuperación](../backup-and-recovery.md)
- [Acceso de emergencia](../../13-security/break-glass-access.md)
- [Respuesta a incidentes](../../13-security/incident-response.md)
