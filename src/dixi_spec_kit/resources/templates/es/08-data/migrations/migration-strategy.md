# Estrategia de migraciones

## Propósito

Fijar las reglas para cambiar esquemas de base de datos con seguridad: cómo se escriben, revisan, aplican y revierten las migraciones. Los cambios de esquema son cambios de código y siguen la misma disciplina.

- Herramienta de migraciones: {{pending: herramienta de migraciones y dónde viven los archivos de migración}}
- Quién puede aplicar migraciones en producción: {{pending: rol o paso del pipeline}}

## Principios

- Las migraciones están versionadas, ordenadas y guardadas en el repositorio.
- Una migración nunca se edita después de aplicarse en un entorno compartido; se escribe una nueva.
- Los cambios de esquema y de aplicación se pueden desplegar de forma independiente.
- Se prefieren pasos pequeños y reversibles a un cambio grande.
- Los pasos destructivos (drop, cambios de tipo que reducen) van al final, tras un periodo de verificación.

## Expandir y contraer

1. **Expandir**: añadir la estructura nueva (columna, tabla, índice) sin quitar la antigua.
2. **Migrar**: escribir en ambas, rellenar los datos existentes y después cambiar las lecturas.
3. **Contraer**: eliminar la estructura antigua cuando nada la use.

Cada fase es un despliegue separado.

## Decisiones por tipo de cambio

| Cambio | Enfoque seguro | Reversible |
| --- | --- | --- |
| Añadir columna nulable | Una sola migración | Sí |
| Añadir columna obligatoria | Añadir nulable, rellenar y después añadir la restricción | Sí, hasta contraer |
| Renombrar columna | Expandir y contraer, nunca en el sitio | Sí, hasta contraer |
| Eliminar columna | Dejar de usarla, esperar una versión y después eliminar | No |
| Cambiar tipo de columna | Columna nueva, relleno, cambio, eliminar la antigua | En parte |
| Índice en tabla grande | Creación no bloqueante si el motor lo permite | Sí |
| Añadir restricción | Añadir sin validar y después validar | Sí |

## Flujo de trabajo

- [ ] Describir el cambio y sus fases en la spec de feature o de módulo.
- [ ] Escribir la migración y su reversión.
- [ ] Ejecutarla sobre una copia con volumen realista y registrar la duración.
- [ ] Revisar: bloqueos, duración, compatibilidad hacia atrás, pérdida de datos.
- [ ] Aplicar en entornos inferiores y después en producción, mediante el pipeline.
- [ ] Verificar con consultas definidas de antemano.

## Reversión

{{pending: enfoque de reversión, por ejemplo migraciones down, solo correcciones hacia adelante o restauración desde copia}}

## Registro de la migración

| Campo | Valor |
| --- | --- |
| Objetivo | |
| Fases | |
| Duración y bloqueos esperados | |
| Plan de reversión | |
| Consultas de verificación | |
| Responsable | |

Para movimientos de datos (no solo de esquema), usa el [playbook de migración de datos](data-migration-playbook.md).

## Relacionados

- [Playbook de migración de datos](data-migration-playbook.md)
- [Arquitectura de datos](../data-architecture.md)
- [Modelo de datos canónico](../canonical-data-model.md)
- [Plan de pruebas](../../11-quality/test-plan.md)
