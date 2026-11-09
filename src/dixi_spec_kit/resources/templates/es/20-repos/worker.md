# Worker

## Propósito

Describir la estructura y las convenciones esperadas de un repositorio de worker en segundo plano: un proceso que consume mensajes o tareas programadas y trabaja fuera del camino de la petición. Esta guía no elige lenguaje ni tecnología de mensajería.

Estado: borrador. {{pending: elegir lenguaje, runtime y tecnología de mensajería o programación para los workers}}

## Decisiones de stack

| Decisión | Elección | ADR |
|----------|----------|-----|
| Lenguaje y runtime | {{pending}} | {{pending}} |
| Broker de mensajes o cola | {{pending}} | {{pending}} |
| Programador de tareas periódicas | {{pending}} | {{pending}} |
| Ejecutor de pruebas | {{pending}} | {{pending}} |

## Estructura de carpetas sugerida

```text
<worker>/
├── README.md          # propósito, eventos consumidos y producidos, IDs de spec
├── AGENTS.md
├── src/
│   ├── consumers/     # un handler por tipo de mensaje
│   ├── jobs/          # tareas programadas
│   ├── domain/        # reglas de negocio sin código de transporte
│   └── adapters/      # broker, almacenamiento, servicios externos
├── tests/
│   ├── unit/
│   └── integration/
└── .env.example
```

## Convenciones

- Cada handler es idempotente: procesar el mismo mensaje dos veces tiene el mismo efecto que una.
- Los mensajes siguen los contratos de eventos; un cambio de esquema se versiona y es retrocompatible.
- Los reintentos usan backoff y un límite; los mensajes que siguen fallando van a un destino dead-letter.
- Cada mensaje lleva un ID de correlación que llega a los logs y a los mensajes producidos.
- Las tareas largas informan su progreso y pueden detenerse de forma segura.
- Los límites de concurrencia son explícitos y están documentados.

## Operación

| Elemento | Valor |
|----------|-------|
| Mensajes consumidos | {{pending}} |
| Mensajes producidos | {{pending}} |
| Reintentos máximos | {{pending}} |
| Responsable de la cola dead-letter | {{pending}} |
| Alerta por profundidad de cola | {{pending}} |

## Verificación

- Las pruebas cubren el camino feliz, duplicados, mensajes mal formados y el agotamiento de reintentos.
- `make verify` ejecuta las comprobaciones reales del worker.

## Relacionados

- [Repositorios](README.md)
- [Servicio backend](backend-service.md)
- [Reglas de alertas](../12-observability/alerting-rules.md)
- [Estándares de código](../10-engineering/coding-standards.md)
- [Playbook de restauración del servicio](../15-operations/playbooks/restore-service.md)
