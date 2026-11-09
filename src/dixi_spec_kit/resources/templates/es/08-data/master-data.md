# Datos maestros

## Propósito

Identificar los datos maestros y de referencia compartidos entre módulos (catálogos, organizaciones, ubicaciones, monedas, categorías), nombrar la fuente única de cada uno y definir cómo se gobiernan y distribuyen sus cambios.

- Custodio de datos: {{pending: persona o rol responsable de la calidad de los datos maestros}}

## Inventario de datos maestros y de referencia

| Conjunto | Tipo (maestro o referencia) | Sistema de registro | Responsable | Consumidores | Frecuencia de actualización |
| --- | --- | --- | --- | --- | --- |
| Países | Referencia | Lista estándar (ISO 3166-1) | | | Rara |
| Monedas | Referencia | Lista estándar (ISO 4217) | | | Rara |
| Idiomas | Referencia | Etiquetas estándar (BCP 47) | | | Rara |
| {{pending: conjunto maestro principal, por ejemplo productos u organizaciones}} | Maestro | | | | |

## Reglas de gobierno

- [ ] Cada conjunto tiene un único sistema de registro; las demás copias son réplicas de solo lectura.
- [ ] Los identificadores son estables y nunca se reutilizan, incluso tras desactivarse.
- [ ] Los registros se desactivan, no se borran, cuando otros datos los referencian.
- [ ] Existen etiquetas traducidas para cada idioma soportado.
- [ ] Los cambios pasan por: {{pending: flujo de aprobación de cambios en datos maestros}}

## Distribución

| Mecanismo | Cuándo encaja | Se usa para |
| --- | --- | --- |
| API de lectura del dueño | Bajo volumen, necesita datos frescos | |
| Eventos de cambio | Los consumidores mantienen copia local | |
| Instantánea periódica | Analítica, conjuntos grandes | |

Los consumidores deben tolerar valores desconocidos o nuevos sin fallar.

## Calidad de datos

| Regla | Conjunto | Comprobación | Frecuencia | Acción si falla |
| --- | --- | --- | --- | --- |
| Sin duplicados por clave natural | | | | |
| Atributos obligatorios presentes | | | | |
| Las referencias se resuelven | | | | |

## Detección y fusión de duplicados

{{pending: cómo se detectan y fusionan duplicados y quién aprueba las fusiones}}

- Las fusiones conservan un mapeo de los identificadores antiguos al superviviente.
- Las fusiones se auditan según el [estándar de campos de auditoría](audit-fields-standard.md).

## Relacionados

- [Modelo de datos canónico](canonical-data-model.md)
- [Dimensiones de reporte](reporting-dimensions.md)
- [Arquitectura de datos](data-architecture.md)
- [Estándar de campos de auditoría](audit-fields-standard.md)
