# Base de seguridad

## Propósito

Definir los controles de seguridad mínimos que toda parte del proyecto debe cumplir, sea cual sea el perfil, para que las brechas sean visibles y cada control tenga responsable. Las prácticas detalladas viven en `13-security/`.

Estado: borrador. {{pending: confirmar la base con la persona responsable de seguridad}}

## Cómo leer las tablas

- **Control**: lo que debe ser cierto.
- **Evidencia**: cómo comprobarlo sin fiarse de una afirmación.
- **Estado**: `pendiente`, `parcial` o `implantado`. Nada empieza como `implantado`.

## Identidad y acceso

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Cada persona y servicio tiene identidad propia; sin cuentas compartidas. | Lista de accesos | pendiente |
| Mínimo privilegio; los accesos se revisan periódicamente. | Registro de revisión | pendiente |
| Autenticación fuerte para el acceso administrativo. | Configuración | pendiente |

## Secretos

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Sin secretos en el repositorio, su historial, los logs ni el contexto de agentes. | Resultado del escaneo de secretos | pendiente |
| Los secretos viven en un almacén gestionado por entorno. | [Gestión de secretos](../13-security/secret-management.md) | pendiente |
| Los secretos tienen responsable y regla de rotación. | Inventario | pendiente |

## Código y dependencias

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Una persona revisa los cambios antes de integrarlos. | Historial de pull requests | pendiente |
| Las dependencias están fijadas y escaneadas. | [Escaneo de dependencias](../13-security/dependency-scanning.md) | pendiente |
| Las entradas se validan en los límites de confianza. | [Estándar de código seguro](../10-engineering/secure-coding-standard.md) | pendiente |

## Datos

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Los datos personales están clasificados y minimizados. | [Clasificación de PII](../08-data/pii-classification.md) | pendiente |
| Los datos se cifran en tránsito y en reposo. | Configuración | pendiente |
| Existen reglas de retención y borrado. | [Política de retención](../08-data/retention-policy.md) | pendiente |

## Agentes de IA

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Los agentes no pueden leer secretos, firmar, aprobar ni integrar. | [Endurecimiento de agentes de IA](../13-security/ai-agent-hardening.md) | pendiente |
| El contenido no confiable se trata como datos, no como instrucciones. | Checklist de revisión | pendiente |

## Detección y respuesta

| Control | Evidencia | Estado |
|---------|-----------|--------|
| Los eventos relevantes de seguridad se registran sin datos sensibles. | Muestras de logs | pendiente |
| Existe un proceso de incidentes con roles nombrados. | [Respuesta a incidentes](../13-security/incident-response.md) | pendiente |

## Marco de referencia

{{pending: elegir un marco o estándar de verificación de referencia, si lo hay, y el nivel objetivo}}

## Relacionados

- [Modelo de amenazas](../13-security/threat-model.md)
- [Estándares de ingeniería](engineering-standards.md)
- [Gobernanza de IA](ai-governance.md)
- [Principios](principles.md)
