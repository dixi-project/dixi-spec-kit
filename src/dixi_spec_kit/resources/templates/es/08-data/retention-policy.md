# Política de retención

## Propósito

Establecer cuánto tiempo se conserva cada categoría de datos, por qué y qué ocurre al terminar el plazo. Conservar datos más de lo necesario aumenta riesgo y coste; borrarlos demasiado pronto rompe necesidades legales, contractuales u operativas.

- Responsable: {{pending: persona o rol responsable de la retención}}
- Frecuencia de revisión: {{pending: cada cuánto se revisa esta política}}

## Principios

- Conservar datos solo mientras exista una finalidad documentada.
- Cada categoría tiene un plazo explícito y una acción de fin de vida explícita.
- Las retenciones legales prevalecen sobre el borrado y quedan registradas.
- Las copias de seguridad siguen las mismas reglas, con un desfase documentado.
- El borrado es verificable: hay evidencia de que se ejecutó.

## Calendario de retención

| Categoría de datos | Clasificación | Periodo activo | Periodo de archivo | Acción de fin de vida | Fundamento |
| --- | --- | --- | --- | --- | --- |
| Cuentas de usuario | Personal | Mientras la cuenta esté activa | {{pending: plazo}} | Borrar o anonimizar | {{pending: fundamento}} |
| Transacciones / pedidos | | {{pending: plazo}} | | | {{pending: requisito legal o fiscal}} |
| Logs de aplicación | Interno | {{pending: plazo}} | — | Borrar | Operación |
| Registros de auditoría | | {{pending: plazo}} | | | |
| Copias de seguridad | Mixta | {{pending: plazo}} | — | Expirar | Recuperación |
| Eventos analíticos | | | | Agregar y luego borrar | |

Los valores de clasificación provienen de la [clasificación de datos personales](pii-classification.md).

## Acciones de fin de vida

| Acción | Significado | Cuándo usarla |
| --- | --- | --- |
| Borrar | Eliminar el registro y sus copias | No queda finalidad |
| Anonimizar | Eliminar o transformar de forma irreversible los campos identificativos | Aún se necesitan estadísticas |
| Archivar | Mover a almacenamiento más barato y restringido | Necesidad legal, acceso raro |
| Agregar | Conservar solo totales o resúmenes | Tendencias, no individuos |

## Checklist de implementación

- [ ] Cada tabla o almacén con datos Personales tiene regla de retención y responsable.
- [ ] Un proceso programado aplica las reglas: {{pending: mecanismo y frecuencia de los procesos de purga}}
- [ ] Las purgas son idempotentes, se ejecutan por lotes y registran qué eliminaron (conteos, no contenido).
- [ ] Las solicitudes de supresión se propagan a réplicas, cachés, índices de búsqueda, exportaciones y copias de seguridad.
- [ ] Las retenciones legales pueden suspender el borrado de registros concretos y quedan registradas.
- [ ] Las pruebas cubren que los registros vencidos se eliminan o anonimizan de verdad.

## Excepciones

| Excepción | Alcance | Aprobada por | Vence |
| --- | --- | --- | --- |
| | | | |

## Relacionados

- [Clasificación de datos personales](pii-classification.md)
- [Proyecto](../00-master-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
