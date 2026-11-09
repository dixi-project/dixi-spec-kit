# Política de dependencias

## Propósito

Controlar cómo entran y permanecen en el proyecto las bibliotecas, herramientas y runtimes de terceros, para que cada dependencia esté justificada, sea reproducible, tenga una licencia correcta y se mantenga al día.

Estado: borrador. {{pending: confirmar esta política con la persona responsable}}

## Añadir una dependencia

Antes de añadirla, responde en el pull request:

- [ ] ¿Qué problema resuelve y por qué no basta la biblioteca estándar o el código existente?
- [ ] ¿Está mantenida (releases recientes, mantenedores que responden)?
- [ ] ¿Su licencia está en la lista aprobada?
- [ ] ¿Tiene vulnerabilidades conocidas?
- [ ] ¿Cuántas dependencias transitivas trae?
- [ ] ¿Es de ejecución o solo de desarrollo?

Quién aprueba nuevas dependencias de ejecución: {{pending: quién aprueba}}

## Fijación y reproducibilidad

- Fija versiones exactas en un archivo de bloqueo; commitea ese archivo.
- Verifica la integridad con hashes cuando el ecosistema lo permita.
- Los builds deben poder reproducirse solo con el repositorio.
- No descargues código en tiempo de ejecución desde fuentes sin fijar.

## Actualizaciones

| Tipo | Frecuencia | Regla |
|------|------------|-------|
| Correcciones de seguridad | {{pending: p. ej. en N días según severidad}} | Prioridad sobre el trabajo de funcionalidades |
| Menores y parches | {{pending: cadencia}} | Agrupadas, con pruebas en verde |
| Mayores | Planificadas | Pull request propio, con notas de migración |

## Runtimes soportados

| Runtime | Versiones soportadas | Plan de fin de soporte |
|---------|----------------------|------------------------|
| {{pending: runtime}} | {{pending: versiones}} | {{pending: plan}} |

## Retirada

- Elimina las dependencias que ya no se usan.
- Sustituye las dependencias abandonadas antes de que bloqueen una corrección de seguridad.

## Relacionados

- [Licencias aprobadas](../../13-security/licensing/approved-licenses.md)
- [Política de licencias](../../13-security/licensing/licensing-policy.md)
- [Escaneo de dependencias](../../13-security/dependency-scanning.md)
- [Base de seguridad](../security-baseline.md)
