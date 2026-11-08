# Política de seguridad / Security policy

## Propósito

Explicar cómo reportar vulnerabilidades de DIXI Spec Kit de forma responsable.

## Versiones soportadas

| Versión | Soporte |
|---|---|
| 1.0.x | Sí |
| < 1.0 | No |

## Reportar una vulnerabilidad

No abras una issue pública. Usa **Report a vulnerability** en la pestaña *Security* del repositorio (GitHub private vulnerability reporting). Incluye versión, sistema, pasos para reproducir e impacto. Responderemos en un plazo objetivo de 5 días hábiles y coordinaremos la divulgación tras publicar la corrección.

Dentro del alcance: la CLI `dixi` (rutas, symlinks, sobrescrituras, lectura fuera del proyecto, recursos empaquetados) y los comandos instalados del adaptador. Fuera del alcance: el comportamiento del modelo de IA que ejecuta los comandos y los proyectos generados por terceros.

## English

Do not open a public issue. Use **Report a vulnerability** in the repository's *Security* tab (GitHub private vulnerability reporting) with version, OS, reproduction steps and impact. Target first response: 5 business days; disclosure is coordinated after a fix ships. In scope: the `dixi` CLI and the installed adapter commands. Out of scope: the AI model's behavior and third-party generated projects.
