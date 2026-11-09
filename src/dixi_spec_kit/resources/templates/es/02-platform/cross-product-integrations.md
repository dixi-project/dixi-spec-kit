# Integraciones entre productos

## Propósito

Documentar cada integración entre productos de la plataforma: qué la desencadena, qué contrato usa,
quién es responsable de cada lado y cómo se gestionan los fallos. Las integraciones son el punto
donde productos independientes se acoplan; hacerlas explícitas mantiene ese acoplamiento deliberado
y comprobable.

## Catálogo de integraciones

| ID | Productor | Consumidor | Estilo | Disparador | Contrato | Responsable |
|---|---|---|---|---|---|---|
| INT-001 | {{pending: producto}} | {{pending: producto}} | {{pending: API síncrona, evento, comando o archivo}} | {{pending: disparador de negocio}} | {{pending: ruta en 07-contracts}} | {{pending: rol}} |
| INT-002 | {{pending: producto}} | {{pending: producto}} | {{pending: estilo}} | {{pending: disparador}} | {{pending: contrato}} | {{pending: rol}} |

## Elegir un estilo

| Estilo | Úsalo cuando | Cuidado con |
|---|---|---|
| API síncrona | Quien llama necesita respuesta inmediata | Fallos en cascada, presupuestos de latencia |
| Evento | Otros reaccionan a un hecho; el productor no espera | Orden, duplicados, consistencia eventual |
| Comando | Un consumidor concreto debe ejecutar una acción | Reintentos e idempotencia |
| Archivo o lote | Grandes volúmenes con un calendario | Fallos parciales, reprocesamiento |

## Detalle por integración (copiar por integración)

### INT-001 — {{pending: nombre}}

- Motivo de negocio: {{pending: por qué los productos necesitan comunicarse}}
- Datos intercambiados: {{pending: entidades y campos, señalando los datos personales}}
- Consistencia esperada: {{pending: inmediata o eventual, y retraso aceptable}}
- Comportamiento ante fallos: {{pending: reintento, cola de mensajes fallidos, compensación, mensaje al usuario}}
- Idempotencia: {{pending: clave usada para detectar duplicados}}
- Propagación de la tenencia: {{pending: cómo viajan tenencia e identidad con el mensaje}}
- Pruebas de contrato: {{pending: dónde viven y quién las ejecuta}}

## Reglas

- Ningún producto lee directamente el almacenamiento de otro.
- Toda integración tiene un contrato y una prueba de contrato en el lado consumidor.
- Cambiar un contrato sigue su política de versionado y se notifica a todos los consumidores.

## Relacionados

- [Mapa de productos](product-map.md)
- [Mapa de servicios compartidos](shared-services-map.md)
- [Contratos de eventos](../07-contracts/events/README.md)
- [Contratos de comandos](../07-contracts/commands/README.md)
- [Guía de pruebas de contrato](../11-quality/contract-testing-guide.md)
