# Playbook de due diligence de auditoría interna

> **Regla de evidencia.** Una auditoría interna solo sirve si es honesta. Puntúa desde artefactos, registra los huecos como huecos y nunca presentes un supuesto como hecho; cada hallazgo remite a un artefacto del proyecto.

## Propósito

Aplicar el método de due diligence al propio proyecto, con calendario, para encontrar debilidades antes que un tercero y medir el progreso entre revisiones.

Estado: borrador. {{pending: fijar la cadencia de auditoría y nombrar a quien la lidera}}

## Principios

- Quien audita no debe puntuar las áreas de las que es responsable; rota o empareja revisores.
- Usa la misma escala y listas que las revisiones externas para que los resultados sean comparables.
- Los hallazgos se siguen como cualquier otro trabajo, con responsables y fechas.

## Plan

| Campo | Valor |
|-------|-------|
| Ciclo | {{pending: p. ej. trimestral o antes de cada versión mayor}} |
| Áreas de este ciclo | {{pending: todas o un subconjunto rotatorio}} |
| Revisores por área | {{pending: roles}} |
| Periodo de la evidencia | {{pending: desde – hasta}} |
| Tiempo máximo | {{pending: duración}} |

## Pasos

1. Elegir las áreas de las [listas](../dd-strategy.md) y asignar revisores.
2. Reunir evidencia; marcar los elementos sin artefacto como «sin evidencia».
3. Puntuar y acordar las puntuaciones en una breve sesión de calibración.
4. Comparar con el ciclo anterior; explicar cada puntuación que haya bajado.
5. Completar la [Plantilla de informe de DD](../dd-report-template.md) y la [Lista final](../checklist/11-final-report.md).
6. Crear tickets para las brechas y añadir las relevantes al [Registro de riesgos](../../13-security/risk-register.md).

## Tendencia

| Área | Puntuación anterior | Puntuación actual | Cambio explicado por |
|------|---------------------|-------------------|----------------------|
| {{pending: área}} | {{pending: puntuación}} | {{pending: puntuación}} | {{pending: artefacto o hallazgo}} |

## Uso del resultado

- Llevar las brechas principales a la planificación: {{pending: decidir cuánta capacidad se reserva para remediación}}
- Reutilizar la evidencia vigente cuando llegue una revisión externa.
- Usar `/dixi.duediligence` (Claude Code) o `$dixi-duediligence` (Codex) para preparar el ciclo.

## Relacionados

- [Estrategia de DD](../dd-strategy.md)
- [Playbook de DD de comprador](buyer-dd-playbook.md)
- [Playbook de DD de cliente empresarial](enterprise-customer-dd-playbook.md)
- [Lista final](../checklist/11-final-report.md)
