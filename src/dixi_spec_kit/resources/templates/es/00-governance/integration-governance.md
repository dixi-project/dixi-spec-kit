# Gobierno de integraciones

## Propósito

Fijar las reglas para toda integración entre los servicios de la plataforma y con sistemas externos, para que cada integración tenga responsable, contrato, revisión de seguridad y un comportamiento conocido ante fallos.

Estado: borrador. {{pending: nombrar a la persona responsable del gobierno de integraciones}}

## Reglas

1. Toda integración tiene un contrato escrito antes de construirse.
2. Los contratos se versionan; los cambios incompatibles siguen un periodo de obsolescencia.
3. Cada integración tiene una persona responsable en cada lado.
4. Las credenciales son por integración y por entorno, con mínimo privilegio.
5. Cada llamada tiene tiempo límite, política de reintentos y un comportamiento definido cuando el otro lado no responde.
6. Los datos externos se validan en el límite y se tratan como no confiables.
7. Las integraciones son observables: tasa, errores, latencia e IDs de correlación.

## Registro de integraciones

| ID | Consumidor | Proveedor | Estilo | Contrato | Responsable | Criticidad |
|----|------------|-----------|--------|----------|-------------|------------|
| INT-001 | {{pending: consumidor}} | {{pending: proveedor}} | {{pending: API síncrona / evento / archivo}} | [Contrato](../07-contracts/example.md) | {{pending: responsable}} | {{pending: nivel}} |

## Elegir un estilo

| Necesidad | Preferir |
|-----------|----------|
| Se requiere respuesta inmediata | Petición síncrona |
| Reacción desacoplada a un hecho | Evento |
| Transferencia de lotes grandes | Archivo o transferencia masiva |

{{pending: estilo de integración por defecto de la plataforma}}

## Checklist de aprobación de una integración nueva

- [ ] Contrato escrito y revisado.
- [ ] Clasificación de datos de los campos intercambiados conocida.
- [ ] Modelo de amenazas actualizado.
- [ ] Comportamiento ante fallo y alternativa definidos.
- [ ] Pruebas de contrato planificadas en ambos lados.
- [ ] Responsable y contacto de soporte registrados.

## Obsolescencia

- Anuncia con al menos {{pending: plazo de aviso}} antes de retirar una versión.
- Identifica a los consumidores de cada versión antes de retirarla.

## Relacionados

- [Arquitectura de integración](../09-architecture/integration-architecture.md)
- [Guía de pruebas de contrato](../11-quality/contract-testing-guide.md)
- [Estándar de diseño de API](../10-engineering/api-design-standard.md)
- [Estándar de diseño de eventos](../10-engineering/event-design-standard.md)
- [Estándar de observabilidad](observability-standard.md)
