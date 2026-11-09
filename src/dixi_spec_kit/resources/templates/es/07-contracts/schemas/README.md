# Esquemas

## Propósito

Guardar los esquemas de datos compartidos que reutilizan varios contratos: entidades, objetos de
valor, formatos de error y envoltorios comunes. Definir un tipo una sola vez y referenciarlo desde
API, eventos y archivos evita la deriva lenta que ocurre cuando cada contrato redefine «cliente» o
«importe» a su manera.

## Estructura

```text
07-contracts/schemas/
  <entidad>.schema.json    Un esquema por tipo compartido (por ejemplo, JSON Schema)
  common/                  Piezas reutilizables: importe, dirección, paginación, error
```

- Formato de esquema: {{pending: JSON Schema, protocol buffers u otro formato, registrado en un ADR}}
- Nombres de archivo: palabras en minúsculas separadas por guiones, un tipo por archivo.

## Qué debe definir cada esquema

- Un `$id` o nombre estable y una versión.
- Nombres de campo del lenguaje ubicuo, con tipo, formato y si cada uno es obligatorio.
- Restricciones: longitudes, rangos, patrones, valores permitidos.
- Campos con datos personales, señalados para que apliquen las reglas de registro y conservación.
- Al menos un ejemplo válido y uno inválido, que usan las pruebas.

## Índice de esquemas

| Esquema | Dominio propietario | Usado por contratos | Versión | Contiene datos personales |
|---|---|---|---|---|
| {{pending: esquema}} | {{pending: dominio}} | {{pending: IDs de contrato}} | {{pending: versión}} | {{pending: sí o no}} |

## Reglas de compatibilidad

- Añadir un campo opcional es compatible; eliminar o renombrar un campo es incompatible.
- Cambiar un tipo o endurecer una restricción es incompatible.
- Los consumidores deben ignorar campos desconocidos para que los productores añadan datos con seguridad.
- Los cambios incompatibles reciben versión nueva; la anterior se mantiene hasta que todos migren.

## Convenciones

- Fechas y horas: {{pending: p. ej. ISO 8601 en UTC}}
- Importes: cantidad en la unidad mínima más el código de moneda, nunca coma flotante.
- Identificadores: {{pending: formato, p. ej. cadenas opacas}}

## Relacionados

- [Contratos de API](../api/README.md)
- [Contratos externos](../external/README.md)
- [Modelo de datos canónico](../../08-data/canonical-data-model.md)
- [Clasificación de datos personales](../../08-data/pii-classification.md)
