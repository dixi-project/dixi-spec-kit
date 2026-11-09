# Dimensiones de reporte

## Propósito

Definir las dimensiones y medidas usadas en informes, paneles y analítica, para que todo informe segmente los datos igual y cada métrica tenga una única definición acordada.

- Responsable: {{pending: persona o rol responsable de las definiciones de métricas}}
- Objetivos de negocio a los que sirven estas métricas: ver el [objetivo de negocio](../01-business/vision.md).

## Dimensiones

| Dimensión | Descripción | Fuente | Granularidad | Tratamiento de cambios lentos |
| --- | --- | --- | --- | --- |
| Fecha | Fecha de calendario en la zona horaria de reporte | Reloj del sistema, convertido desde UTC | Día | No aplica |
| Tenant / cliente | Organización propietaria | [Datos maestros](master-data.md) | Registro | {{pending: conservar historial o sobrescribir}} |
| Producto / oferta | | Datos maestros | | |
| Canal | Dónde ocurrió la acción (web, móvil, API) | Eventos | | |
| Locale | Idioma y país del usuario | Perfil de usuario | | |
| {{pending: dimensión propia del dominio}} | | | | |

## Medidas

| Medida | Definición (fórmula) | Unidad | Agregación | Filtros siempre aplicados |
| --- | --- | --- | --- | --- |
| Usuarios activos | Usuarios distintos con al menos una acción válida en el periodo | Conteo | Conteo distinto | Excluir cuentas internas y de prueba |
| {{pending: métrica de negocio clave}} | | | | |

Redacta cada definición de modo que dos personas calculen el mismo número.

## Reglas

- [ ] Los valores de dimensión provienen del [modelo de datos canónico](canonical-data-model.md) o de los datos maestros, no de texto libre.
- [ ] La zona horaria de reporte es fija: {{pending: zona horaria de reporte}}
- [ ] La conversión de moneda usa una fuente de tipos de cambio y una fecha documentadas.
- [ ] Los registros de prueba, internos y borrados se excluyen de forma consistente.
- [ ] Los informes nunca exponen datos Personales más allá de lo que permite la [clasificación de datos personales](pii-classification.md); se prefieren agregados.
- [ ] Los grupos pequeños se suprimen o agrupan cuando podrían identificar a personas.

## Catálogo de informes

| Informe | Audiencia | Dimensiones | Medidas | Actualización | Responsable |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Proceso de cambio

- Cambiar la definición de una métrica crea una versión nueva; los informes antiguos indican qué versión usan.
- Las dimensiones deprecadas siguen disponibles durante un periodo: {{pending: periodo de deprecación}}

## Relacionados

- [Datos maestros](master-data.md)
- [Modelo de datos canónico](canonical-data-model.md)
- [Clasificación de datos personales](pii-classification.md)
- [Objetivo de negocio](../01-business/vision.md)
