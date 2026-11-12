# dixi init

## Propósito

`dixi init`: Crear una base documental en un destino nuevo o vacío.

Generada por `scripts/build-cli-reference.py` a partir del analizador de argumentos y del catálogo de mensajes; no la edites a mano.

## Uso

```text
dixi init <directory> [--agent {none,claude,codex,skills}] [--profile {minimal,site,app,platform}] [--regulated] [--controls] [--existing]
```

Las opciones globales `--lang` y `--json` van antes del comando; consulta la [referencia de la CLI](index.es.md).

## Argumentos

- `directory` — Directorio destino; su padre debe existir.

## Opciones

- `--help`, `-h` — Mostrar esta ayuda.
- `--agent {none,claude,codex,skills}` — Integración distribuida: none (sin agente), claude (comandos para Claude Code), codex (skills para Codex) o skills (Agent Skills para otros agentes compatibles).
- `--profile {minimal,site,app,platform}` — Perfil de contenido: minimal (por defecto, la base actual), site, app o platform.
- `--regulated` — Añade plantillas de cumplimiento, due diligence y seguridad reforzada (requiere site, app o platform).
- `--controls` — Instala hooks opcionales para el agente que hacen cumplir pruebas congeladas, no leer secretos, no firmar ni integrar, seguridad en modo producción y verificación antes de terminar (requiere --agent claude o codex).
- `--existing` — Añadir DIXI a una carpeta que ya tiene archivos: crea solo lo que falta y nunca sobrescribe.

## Relacionado

- [Referencia de la CLI](index.es.md)
- [README](../../README.es.md)
