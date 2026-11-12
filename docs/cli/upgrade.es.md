# dixi upgrade

## Propósito

`dixi upgrade`: Previsualizar (--dry-run) o aplicar (--apply) lo que esta versión del kit cambia en el proyecto.

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi upgrade [--dry-run] [--apply] [--profile {minimal,site,app,platform}] [--regulated] [--controls]
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.
- `--dry-run` — Solo calcula el plan; no escribe ningún archivo.
- `--apply` — Escribe solo archivos del kit actualizables y nuevos; nunca tus ediciones, archivos borrados ni obsoletos.
- `--profile {minimal,site,app,platform}` — Perfil de contenido: minimal (por defecto, la base actual), site, app o platform.
- `--regulated` — Añade plantillas de cumplimiento, due diligence y seguridad reforzada (requiere site, app o platform).
- `--controls` — Instala hooks opcionales para el agente que hacen cumplir pruebas congeladas, no leer secretos, no firmar ni integrar, seguridad en modo producción y verificación antes de terminar (requiere --agent claude o codex).

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
