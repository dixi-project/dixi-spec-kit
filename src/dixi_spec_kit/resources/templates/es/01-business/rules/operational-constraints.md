# Restricciones operativas

## Propósito

Registrar los límites del mundo real bajo los que debe funcionar el producto: horarios, capacidad,
ubicaciones, conectividad, personal y dependencias. Estas restricciones condicionan los requisitos no
funcionales y las decisiones de arquitectura, y suelen descubrirse demasiado tarde si nadie las
anota.

## Catálogo de restricciones

| ID | Restricción | Categoría | Impacto en el producto | Fuente | Responsable |
|---|---|---|---|---|---|
| OC-001 | {{pending: restricción}} | {{pending: categoría}} | {{pending: impacto}} | {{pending: fuente}} | {{pending: rol}} |
| OC-002 | {{pending: restricción}} | {{pending: categoría}} | {{pending: impacto}} | {{pending: fuente}} | {{pending: rol}} |

## Categorías a revisar

- Tiempo: horario comercial, zonas horarias, temporadas pico, ventanas de mantenimiento.
- Volumen: usuarios esperados, transacciones por periodo, ritmo de crecimiento, tamaño de datos.
- Geografía: países, idiomas, monedas, festivos y formatos locales.
- Conectividad: uso sin conexión o con poco ancho de banda, tipos de dispositivo, condiciones de campo.
- Personas: horario de soporte, disponibilidad de guardias, formación necesaria.
- Dependencias: disponibilidad de socios, ventanas de procesos por lotes, pasos manuales que aún no
  se pueden automatizar.

## Horario de operación y soporte

- Horario de operación: {{pending: p. ej. 24x7 u horario comercial en una zona horaria}}
- Cobertura de soporte: {{pending: horario y canales}}
- Ventanas de mantenimiento aceptables: {{pending: cuándo se permite una parada planificada}}

## Supuestos de capacidad

| Métrica | Esperado hoy | Esperado en 12 meses | Factor de pico |
|---|---|---|---|
| {{pending: p. ej. usuarios activos}} | {{pending: valor}} | {{pending: valor}} | {{pending: multiplicador}} |

Marca cada cifra como medida o estimada; revisa las estimaciones cuando haya datos reales.

## Consecuencias

- Requisitos derivados de estas restricciones: {{pending: enlaces a requisitos no funcionales}}
- Restricciones que el equipo no puede cumplir hoy: {{pending: brechas y mitigación}}

## Relacionados

- [Reglas de negocio](business-rules.md)
- [Requisitos no funcionales](../../11-quality/non-functional-requirements.md)
- [Arquitectura de despliegue](../../09-architecture/deployment-architecture.md)
