# Playbook de due diligence de comprador

> **Regla de evidencia.** Responde al comprador solo con lo que prueban los artefactos. Los huecos se declaran como huecos, nunca se cubren con supuestos presentados como hechos; cada respuesta remite a un artefacto del proyecto.

## Propósito

Preparar el proyecto para una revisión técnica de un posible adquirente o inversor: qué suelen mirar, cómo organizar la sala de datos, cómo responder preguntas y cómo gestionar los hallazgos con honestidad.

Estado: borrador. {{pending: nombrar al responsable interno y a la persona autorizada para compartir material}}

## Antes de la revisión

1. Confirmar el acuerdo de confidencialidad y las reglas de la sala de datos: {{pending: referencia del acuerdo}}
2. Hacer antes una [DD de auditoría interna](internal-audit-dd-playbook.md) para que las brechas conocidas no sorprendan.
3. Preparar un índice de evidencias por área de la lista; enlazar artefactos, no pegarlos.
4. Eliminar secretos, credenciales y datos personales de todo lo que se comparta.

## En qué suelen fijarse los compradores

| Foco | Lista | Evidencia habitual |
|------|-------|--------------------|
| ¿La tecnología funciona y escala? | [02](../checklist/02-architecture.md), [01](../checklist/01-infrastructure.md) | Diagramas, historial de SLO, pruebas de carga |
| ¿De quién es el código y la propiedad intelectual? | [03](../checklist/03-source-code.md) | Titularidad de repositorios, inventario de licencias, cesiones de PI |
| Seguridad e historial de incidentes | [04](../checklist/04-security.md) | Modelo de amenazas, métricas de vulnerabilidades, registros de incidentes |
| Exposición en datos y privacidad | [05](../checklist/05-data-management.md) | Inventario de datos, retención, registros de solicitudes de interesados |
| Riesgo de persona clave | [07](../checklist/07-team.md) | Mapa de personas clave, cobertura de documentación |
| Coste de operación y de escalar | [08](../checklist/08-financial.md) | Exportaciones de facturación, coste unitario |
| Dependencia de proveedores | [09](../checklist/09-vendors-partners.md) | Lista de proveedores, acuerdos, planes de salida |

## Durante la revisión

- Llevar un registro de preguntas: pregunta, respuesta, artefacto, quién respondió, fecha.
- Responder «aún no lo sabemos» antes que adivinar; añadir el elemento a la lista de brechas.
- Dar acceso a sistemas solo según lo acordado, en modo lectura y con caducidad.

## Registro de preguntas

| ID | Pregunta | Respuesta | Artefacto | Respondida por | Fecha |
|----|----------|-----------|-----------|----------------|-------|
| Q-01 | {{pending: pregunta}} | {{pending: respuesta}} | {{pending: enlace}} | {{pending: rol}} | {{pending: fecha}} |

## Después de la revisión

- Registrar los hallazgos en la [Plantilla de informe de DD](../dd-report-template.md) y acordar el plan de remediación.
- Revocar cualquier acceso concedido para la revisión.

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Playbook de DD de auditoría interna](internal-audit-dd-playbook.md)
- [Lista final](../checklist/11-final-report.md)
