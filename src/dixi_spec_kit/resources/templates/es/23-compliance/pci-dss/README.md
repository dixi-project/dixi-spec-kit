# PCI DSS

> **Ayuda de trabajo; no es asesoría legal.** Esta página ayuda a decidir cómo afecta al proyecto el estándar de seguridad de datos de la industria de tarjetas de pago (PCI DSS) y cómo mantener ese impacto pequeño. La validación se hace por los medios que exigen las marcas de tarjetas y el adquirente; ninguna plantilla certifica conformidad.

## Propósito

Registrar si el proyecto almacena, procesa o transmite datos de titulares de tarjetas, qué partes del sistema quedan en alcance y la vía de validación acordada con el socio de pagos. El objetivo habitual es reducir el alcance para que los datos de tarjeta nunca toquen los sistemas del proyecto.

Estado: borrador. {{pending: decidir el enfoque de integración de pagos y registrarlo como ADR}}

## Preguntas de alcance

| Pregunta | Respuesta | Fuente |
|----------|-----------|--------|
| ¿Algún sistema del proyecto recibe números de tarjeta completos, aunque sea de paso? | {{pending: respuesta}} | [Arquitectura de integración](../../09-architecture/integration-architecture.md) |
| ¿La captura de la tarjeta la hace una página alojada, un campo embebido o una redirección del socio de pagos? | {{pending: respuesta}} | {{pending: enlace}} |
| ¿Qué sistemas podrían afectar a la seguridad de la página de pago (scripts, CDN, redirecciones)? | {{pending: lista}} | {{pending: enlace}} |
| ¿Qué validación exige el adquirente o el socio de pagos? | {{pending: respuesta, según el socio}} | {{pending: enlace}} |

## Opciones para reducir el alcance

| Opción | Efecto en el alcance | Contrapartidas |
|--------|----------------------|----------------|
| Redirección a una página de pago alojada | Huella mínima para el proyecto | Menos control sobre la experiencia de pago |
| Campos embebidos servidos por el socio de pagos | Huella pequeña; la integridad de la página sigue importando | Hay que gestionar la integridad de los scripts |
| Los datos de tarjeta pasan por servidores del proyecto | Huella grande; aplican la mayoría de requisitos | Esfuerzo alto; evitar salvo necesidad |

## Si está en alcance: áreas a preparar

Descritas en términos generales; consulta la versión vigente del estándar en su editor oficial.

- Segmentación de red que aísle el entorno de datos de titulares.
- Configuración segura y control de cambios en los sistemas en alcance.
- Protección de los datos de tarjeta almacenados y transmitidos; tokenización cuando sea posible.
- Gestión de vulnerabilidades y pruebas periódicas: [Gestión de vulnerabilidades](../../13-security/vulnerability-management.md).
- Control de acceso fuerte y cuentas únicas: [Modelo de AuthN/AuthZ](../../13-security/authn-authz-model.md).
- Logging y monitorización del acceso a datos de tarjeta.
- Integridad de los scripts de la página de pago.
- Políticas, formación y respuesta a incidentes: [Respuesta a incidentes](../../13-security/incident-response.md).

## Salvaguardas

- Nunca registrar en logs números de tarjeta ni códigos de seguridad; añadir un test que busque patrones de tarjeta en los logs. {{pending: decidir dónde vive este test}}
- Usar números de tarjeta de prueba del socio de pagos solo en entornos que no sean producción.

## Relacionados

- [Panorama de cumplimiento](../compliance-overview.md)
- [Evaluación de riesgo de proveedores](../../15-operations/vendor-management/vendor-risk-assessment.md)
- [Modelo de amenazas](../../13-security/threat-model.md)
- [Registro de riesgos](../../13-security/risk-register.md)
