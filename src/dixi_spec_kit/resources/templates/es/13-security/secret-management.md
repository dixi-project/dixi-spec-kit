# Gestión de secretos

## Propósito

Definir cómo el proyecto guarda, distribuye, usa y retira secretos (contraseñas, claves de API, tokens, certificados, claves de firma) para que ninguno viva en el repositorio, en los logs ni en el contexto de un agente de IA.

Estado: borrador. {{pending: nombrar al responsable de la gestión de secretos}}

## Principios

- Los secretos nunca entran al control de versiones, ni en el historial, ni en ejemplos, ni en pruebas.
- Cada entorno tiene sus propios secretos; los de producción nunca se reutilizan en desarrollo.
- Cada secreto tiene responsable, propósito y el alcance más estrecho posible.
- Las aplicaciones leen los secretos en tiempo de ejecución desde un almacén gestionado o el entorno, nunca desde el código.
- Personas y agentes acceden solo a los secretos que su tarea necesita.

## Inventario

Mantén una lista de *nombres* de secretos, nunca de valores.

| Nombre | Propósito | Entornos | Responsable | Almacenamiento | Rotación |
|--------|-----------|----------|-------------|----------------|----------|
| {{pending: p. ej. DATABASE_PASSWORD}} | {{pending: propósito}} | {{pending: dev / staging / prod}} | {{pending: responsable}} | {{pending: almacén}} | {{pending: frecuencia}} |

## Decisión de almacenamiento

- Dónde viven los secretos en cada entorno: {{pending: elegir un almacén o mecanismo por entorno}}
- Quién puede leerlos y quién escribirlos: {{pending: definir roles de acceso}}
- Cómo se audita el acceso: {{pending: definir el registro de auditoría}}

## Desarrollo local

- Usa un archivo `.env` local ignorado por el control de versiones; versiona solo un `.env.example` con valores de relleno como `CHANGE_ME`.
- No pegues secretos en issues, pull requests, herramientas de chat ni prompts de IA.
- Los agentes de IA no deben leer archivos `.env*`, archivos de claves ni almacenes de credenciales.

## Detección y prevención

- Escanea los commits en busca de secretos antes de hacer push: {{pending: elegir un escáner de secretos en pre-commit o CI}}
- Escanea el historial completo al menos una vez al adoptar esta política.
- Enmascara los secretos en logs y mensajes de error.

## Si se filtra un secreto

1. Trátalo como comprometido, aunque la exposición haya sido breve o el repositorio sea privado.
2. Revócalo o rótalo primero; limpiar el historial viene después.
3. Revisa los registros de acceso en busca de abuso durante la ventana de exposición.
4. Registra el evento siguiendo el proceso de respuesta a incidentes.

## Relacionados

- [Modelo de amenazas](threat-model.md)
- [Respuesta a incidentes](incident-response.md)
- [Endurecimiento de agentes de IA](ai-agent-hardening.md)
- [Instrucciones para agentes](../AGENTS.md)
