# Contratos externos

## Propósito

Documentar los contratos con sistemas que el proyecto no controla: API de terceros, webhooks de
socios, intercambios de archivos y fuentes de datos públicas. Los contratos externos cambian al ritmo
de otros, así que registra con exactitud de qué depende el proyecto, cómo se aísla y qué ocurre
cuando el otro lado falla o cambia.

## Estructura

```text
07-contracts/external/
  <socio-o-sistema>.md          Un archivo por sistema externo
  <socio-o-sistema>/            Opcional: copias de esquemas o muestras, sin secretos
```

Empieza cada archivo con la [plantilla de integración externa](../../10-engineering/templates/external-integration-template.md).
Usa nombres genéricos hasta que se elija el proveedor en un ADR.

## Qué debe registrar cada contrato externo

- La capacidad necesaria y los IDs de funcionalidad que dependen de ella.
- El subconjunto de la interfaz externa que realmente se usa (operaciones, campos, eventos).
- Método de autenticación y dónde viven las credenciales (nunca las credenciales en sí).
- Límites: tasa de peticiones, cuotas, tamaños de carga, compromisos de disponibilidad.
- Tiempos de espera, reintentos, cortacircuitos y el comportamiento degradado para los usuarios.
- Datos compartidos con el tercero, señalando los personales y los acuerdos aplicables.
- Cómo se aísla la integración (un adaptador o capa anticorrupción) para poder sustituirla.
- Cómo se prueba sin llamar al sistema real (dobles, muestras grabadas, entorno de pruebas).

## Índice de integraciones

| Sistema | Capacidad | Dirección | Criticidad | Responsable del adaptador | Estado |
|---|---|---|---|---|---|
| {{pending: nombre genérico del sistema}} | {{pending: capacidad}} | {{pending: entrante, saliente o ambas}} | {{pending: criticidad}} | {{pending: rol}} | {{pending: estado}} |

## Seguimiento de cambios

- Cómo se entera el equipo de cambios en el lado externo: {{pending: registro de cambios, avisos, contacto}}
- Quién revisa los avisos de retirada: {{pending: rol}}

## Relacionados

- [Plantilla de integración externa](../../10-engineering/templates/external-integration-template.md)
- [Arquitectura de integración](../../09-architecture/integration-architecture.md)
- [Socios externos](../../01-business/actors/external-partners.md)
- [Esquemas](../schemas/README.md)
