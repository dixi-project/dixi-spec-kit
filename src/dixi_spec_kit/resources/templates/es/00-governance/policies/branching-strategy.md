# Estrategia de ramas

## Propósito

Definir cómo funcionan las ramas, los commits, los pull requests y las integraciones en este repositorio, para que la rama principal siempre se pueda publicar y todo cambio llegue a ella tras una revisión humana.

Estado: borrador. {{pending: confirmar el modelo de ramas con el equipo}}

## Ramas

| Rama | Propósito | Duración | Quién integra en ella |
|------|-----------|----------|-----------------------|
| `main` | Historial siempre publicable | Permanente | Una persona, mediante un pull request revisado |
| `feat/<tema>` | Comportamiento nuevo | Días | — |
| `fix/<tema>` | Corrección de un error | Horas o días | — |
| `docs/<tema>` | Solo documentación | Horas o días | — |
| `release/<versión>` | Preparación de release, si se usa | Hasta el release | {{pending: si se usan ramas de release}} |

- Nadie hace push directo a `main`, tampoco los agentes.
- Las ramas son de vida corta; haz rebase o merge de `main` a menudo para evitar divergencias.

## Commits

- Formato: `[área] acción: descripción`, por ejemplo `[05-features] add: criterios de restablecer contraseña`.
- Un cambio lógico por commit.
- La prueba en rojo se commitea sola, antes de la implementación (`... (red)`).
- Los commits hechos con ayuda de IA los firma, cuando se exige firma, la persona, nunca el agente.

## Pull requests

- [ ] Enlaza a la spec o tarea que implementa.
- [ ] Describe qué cambió y cómo se verificó, con el resultado real de `make verify`.
- [ ] Indica si hubo asistencia de IA y en qué partes.
- [ ] Es lo bastante pequeño para revisarlo de una vez. {{pending: límite orientativo de tamaño}}
- [ ] Tiene al menos {{pending: número}} aprobación(es) humana(s).

## Tipo de integración

{{pending: elegir squash, rebase o merge commits, y por qué}}

## Etiquetas

- Los releases se etiquetan desde `main` según la [política de versiones](versioning-policy.md).

## Checklist de configuración del repositorio

- [ ] `main` está protegida contra pushes directos y forzados.
- [ ] Las verificaciones obligatorias deben pasar antes de integrar.
- [ ] Las revisiones obligatorias están activadas.
- [ ] Las aprobaciones se descartan cuando llegan commits nuevos.

## Relacionados

- [Política de pruebas](testing-policy.md)
- [Política de versiones](versioning-policy.md)
- [Estándares de ingeniería](../engineering-standards.md)
- [Instrucciones del proyecto](../../AGENTS.md)
