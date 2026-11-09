# Estrategia de due diligence

> **Regla de evidencia.** La due diligence describe lo que prueban los artefactos. Los huecos se registran como huecos, nunca se rellenan con supuestos presentados como hechos, y cada afirmación remite a un artefacto del proyecto.

## Propósito

Definir cómo realiza el proyecto una due diligence (DD) técnica: quién la pide, qué entra en alcance, cómo se puntúan las áreas, cómo se reúne la evidencia y cómo el resultado se convierte en un plan de acción. El mismo método sirve para revisiones externas e internas.

Estado: borrador. {{pending: nombrar al responsable de la DD y quién puede compartir material de DD fuera del equipo}}

## Tipos de DD

| Tipo | Quién la pide | Pregunta habitual | Playbook |
|------|---------------|-------------------|----------|
| Comprador o inversor | Adquirente, inversor | ¿La tecnología es lo que se dice y cuánto cuesta corregirla? | [DD de comprador](playbooks/buyer-dd-playbook.md) |
| Cliente empresarial | Equipo de seguridad o compras del cliente | ¿Podemos confiar este producto con nuestros datos y operaciones? | [DD de cliente empresarial](playbooks/enterprise-customer-dd-playbook.md) |
| Auditoría interna | El propio proyecto | ¿Dónde somos débiles y qué corregimos primero? | [DD de auditoría interna](playbooks/internal-audit-dd-playbook.md) |
| Proveedor | El proyecto, evaluando a un proveedor | ¿Podemos depender de este proveedor? | [DD de proveedor](playbooks/vendor-dd-playbook.md) |

## Escala de madurez

Cada elemento de las listas se puntúa de 0 a 5:

| Puntuación | Significado |
|------------|-------------|
| 0 | Ausente o sin evidencia |
| 1 | Improvisado, depende de personas |
| 2 | Definido pero no aplicado de forma constante |
| 3 | Definido, aplicado y documentado |
| 4 | Medido y revisado |
| 5 | Mejorado de forma continua, verificado por terceros |

Puntuación de área: {{pending: decidir entre la media de los elementos y el elemento crítico más débil}}

## Proceso

1. **Alcance**: confirmar el tipo de DD, las áreas de la lista y el plazo.
2. **Barrido de evidencias**: reunir artefactos para cada área; anotar dónde vive cada uno.
3. **Puntuación**: puntuar cada elemento según su evidencia; anotar quién puntuó y cuándo.
4. **Análisis de brechas**: listar brechas por gravedad; marcar las señales de alarma de forma explícita.
5. **Resultado**: completar la [Plantilla de informe de DD](dd-report-template.md) y la [Lista final](checklist/11-final-report.md); convertir las brechas en tickets y riesgos.

## Áreas de la lista

[Infraestructura](checklist/01-infrastructure.md), [Arquitectura](checklist/02-architecture.md), [Código fuente](checklist/03-source-code.md), [Seguridad](checklist/04-security.md), [Gestión de datos](checklist/05-data-management.md), [Procesos](checklist/06-processes.md), [Equipo](checklist/07-team.md), [Finanzas](checklist/08-financial.md), [Proveedores y socios](checklist/09-vendors-partners.md), [Innovación](checklist/10-innovation.md).

## Confidencialidad

- Compartir material de DD solo bajo el acuerdo que rige la revisión: {{pending: p. ej. referencia del NDA}}
- Usar una sala de datos controlada; nunca enviar secretos, credenciales ni datos personales.
- Registrar qué se compartió, con quién y cuándo.

## Antipatrones

- Puntuar de memoria o por entrevistas sin artefacto.
- Ocultar brechas conocidas; aparecen después y cuestan más.
- Reescribir la historia: la evidencia conserva su fecha original.

Usa `/dixi.duediligence` (Claude Code) o `$dixi-duediligence` (Codex) para preparar una revisión con este método.

## Relacionados

- [Plantilla de informe de DD](dd-report-template.md)
- [Lista final](checklist/11-final-report.md)
- [Registro de riesgos](../13-security/risk-register.md)
- [Proyecto](../00-master-spec.md)
