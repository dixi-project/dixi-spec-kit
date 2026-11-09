# Estándares de ingeniería

## Propósito

Ofrecer un único punto de entrada a los estándares de ingeniería del proyecto: qué reglas aplican, dónde está escrita cada una y cómo se hace cumplir. Este documento es un índice y un mínimo exigible, no un sustituto de los estándares detallados.

Estado: borrador. {{pending: confirmar los estándares que aplican a este proyecto}}

## Mínimo para cada cambio

- [ ] Una spec o tarea explica por qué existe el cambio.
- [ ] Las pruebas se escribieron primero y se commitearon antes de la implementación.
- [ ] Se ejecutó `make verify` y se reporta su resultado real.
- [ ] No se añadieron secretos, credenciales ni datos personales al repositorio.
- [ ] Los textos visibles para el usuario viven en catálogos de traducción, no en el código.
- [ ] Las interfaces públicas cambiaron solo a través de su contrato.
- [ ] Una persona revisó e integró el cambio.

## Índice de estándares

| Tema | Dónde vive | Cómo se hace cumplir |
|------|------------|----------------------|
| Estilo de código | [Estándares de código](../10-engineering/coding-standards.md) | {{pending: formateador o linter}} |
| Código seguro | [Estándar de código seguro](../10-engineering/secure-coding-standard.md) | Revisión, {{pending: análisis estático}} |
| Pruebas | [Política de pruebas](policies/testing-policy.md) | `make verify`, revisión |
| Ramas y commits | [Estrategia de ramas](policies/branching-strategy.md) | Configuración del repositorio |
| Nombres | [Convenciones de nombres](policies/naming-conventions.md) | Revisión |
| Documentación | [Política de documentación](policies/documentation-policy.md) | `dixi check` |
| Dependencias | [Política de dependencias](policies/dependency-policy.md) | {{pending: escáner de dependencias}} |
| Versiones | [Política de versiones](policies/versioning-policy.md) | Revisión de release |
| Internacionalización | [Política de i18n](policies/i18n-policy.md) | Revisión, pruebas |
| Uso de IA | [Política de uso de IA](policies/ai-usage-policy.md) | Revisión |

## Niveles de cumplimiento

| Nivel | Significado |
|-------|-------------|
| Automático | Una verificación rompe el build cuando se incumple la regla. |
| Revisión | Quien revisa comprueba la regla; la checklist lo registra. |
| Recomendación | Se aconseja; las desviaciones se anotan pero no bloquean. |

Marca cada regla con su nivel. Una regla «automática» solo en el papel es una recomendación. {{pending: qué reglas deben automatizarse primero}}

## Excepciones

- Una excepción indica la regla, el motivo, la persona dueña y una fecha de caducidad.
- Las excepciones se registran en {{pending: dónde se registran las excepciones}}.
- Las excepciones caducadas se revisan; no se prorrogan en silencio.

## Relacionados

- [Principios](principles.md)
- [Base de seguridad](security-baseline.md)
- [Guía de TDD](../11-quality/tdd-guide.md)
- [Instrucciones del proyecto](../AGENTS.md)
