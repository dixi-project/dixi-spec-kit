# Pipeline de versión

## Propósito

Describir cómo un artefacto verificado se promueve a staging y después a producción. La promoción a producción siempre espera una aprobación humana; nada se despliega a producción de forma automática.

## Entrada

Un artefacto producido por el pipeline de build a partir de un commit de la rama principal, con `make verify` en verde.

## Etapas

| # | Etapa | Acción | Compuerta para continuar |
|---|---|---|---|
| 1 | Preparar | Reunir artefacto, notas de versión y plan de migración | El artefacto existe y coincide con el commit |
| 2 | Migrar staging | Ejecutar el pipeline de migraciones contra staging | Las migraciones terminan bien |
| 3 | Desplegar staging | Desplegar el artefacto | Despliegue sano |
| 4 | Verificar staging | Comprobación de versión, pruebas de humo, resultado de `make verify` adjunto | Todo pasa |
| 5 | Aprobación | Una persona revisa la evidencia y aprueba | **Aprobación humana explícita registrada** |
| 6 | Migrar producción | Ejecutar el pipeline de migraciones contra producción | Las migraciones terminan bien |
| 7 | Desplegar producción | Desplegar con la estrategia elegida | Despliegue sano |
| 8 | Observación | Vigilar errores y latencia de la versión nueva | Sin alertas durante el tiempo de observación |
| 9 | Cierre | Marcar la versión como terminada, conservar el artefacto anterior | n/a |

Si falla cualquier compuerta, el pipeline se detiene; después de la etapa 7, un fallo activa el procedimiento de reversión.

## Aprobación

- Personas aprobadoras: {{pending: roles}}; quien escribió el cambio no puede ser la única persona que aprueba.
- Evidencia que se muestra: commit, notas de versión, resultado de `make verify`, comprobaciones de staging.
- La aprobación caduca tras {{pending: horas}}; después hace falta una nueva.
- Los agentes pueden preparar la versión (por ejemplo con `/dixi.release`), pero nunca aprobarla.

## Notas de versión

- Se generan a partir de los pull requests fusionados y las revisa una persona.
- Incluyen: cambios visibles para personas usuarias, migraciones, flags, riesgos conocidos y notas de reversión.
- Esquema de versiones: {{pending: versionado semántico, por fecha u otro}}.

## Ventanas bloqueadas

{{pending: periodos en que no se permiten versiones a producción y quién puede conceder excepciones}}

## Relacionados

- [Pipeline de build](build-pipeline.md)
- [Pipeline de migraciones](migration-pipeline.md)
- [Estrategia de despliegue](../deployment-strategy.md)
- [Estrategia de reversión](../rollback-strategy.md)
- [Verificación continua](../continuous-verification.md)
