# Recorrido del ejemplo

## Propósito

Registrar cómo se construyó este ejemplo con DIXI Spec Kit y Claude Code, paso a paso, para que puedas repetirlo. La persona responsable es ficticia.

El ejemplo se produjo siguiendo los pasos de cada comando en una sesión de Claude Code 2.1.319. Si lo repites, la redacción generada variará; lo que debe mantenerse es la estructura, la trazabilidad y `make verify` en verde.

## Pasos

| Paso | Comando | Resultado en este repositorio |
|---|---|---|
| 1 | `dixi init notes --agent claude` | Base documental, `CLAUDE.md` y diez comandos `/dixi.*`. |
| 2 | `/dixi.discover Una biblioteca y CLI para guardar notas locales con etiquetas` | `00-master-spec.md` y `01-business/vision.md` (GOAL-001). |
| 3 | `/dixi.specify Capturar, listar y buscar notas` | Dominio, módulo y FEATURE-001 con criterios verificables. |
| 4 | `/dixi.plan FEATURE-001` | CONTRACT-001, plan de pruebas TEST-001 y ADR-001 (aceptado por la persona). |
| 5 | `/dixi.tasks FEATURE-001` | `05-features/example/tasks.md` (T-001 a T-003). |
| 6 | `/dixi.build T-001` … `T-003` | `tests/test_notes.py` en rojo primero; después `notes/` hasta verde. |
| 7 | `/dixi.verify` | `make verify`: `dixi check` y 7 pruebas en verde. |
| 8 | `/dixi.analyze normalizar etiquetas y filtrar por etiqueta` | [Informe de impacto](../05-features/tags/impact.md): contrato v2, datos antiguos y prueba congelada intacta. |
| 9 | `/dixi.specify` + `/dixi.tasks` | FEATURE-002 y T-004 a T-006. |
| 10 | `/dixi.build T-004` … `T-006` | `tests/test_tags.py` en rojo (5 fallos); después verde sin tocar `tests/test_notes.py`. |
| 11 | `/dixi.verify` y `/dixi.review` | `make verify` con 12 pruebas en verde; [revisión preparada](review-feature-002.md) para una persona. |

## Repetirlo

```sh
cd examples/notes
make verify
python3 -m notes --file /tmp/mis-notas.json add "Leer sobre DDD" --tag Libros
python3 -m notes --file /tmp/mis-notas.json list --tag libros
```

Requiere `dixi` instalado y Python 3.11 o superior.

## Relacionados

- [Proyecto](../00-master-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
