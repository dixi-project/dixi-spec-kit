# Estándar de código seguro

## Propósito

Dar a quien escribe o revisa código, persona o agente, una página con las reglas que no pueden
fallar. Aplican a todo cambio, sin importar el stack ni el perfil.

Responsable de este estándar: {{pending: rol responsable de la revisión de seguridad}}

## Reglas

1. **Autorizar en la consulta.** Todo acceso por identificador filtra por dueño y tenant, para que
   nadie lea el registro de otra persona cambiando un ID (IDOR / autorización rota a nivel de objeto).
2. **Validar la entrada externa con un esquema en el borde.** Rechazar campos desconocidos y exigir
   tipos, longitudes y rangos. Todo lo que cruza un límite de confianza es entrada externa.
3. **Solo consultas parametrizadas**, o un constructor de consultas que parametrice. Nunca armar
   consultas, comandos de shell o rutas de archivo concatenando entrada.
4. **Codificar la salida según su contexto** (cuerpo HTML, atributo, URL, script). No inyectar datos
   externos sin procesar en la página ni evaluarlos como código.
5. **Secretos fuera del código y del repositorio.** Se leen en ejecución desde un almacén de
   secretos; se rotan si alguna vez llegan a un log, un commit o un ticket.
6. **Verificar dependencias antes de instalarlas.** Revisar procedencia, mantenimiento y
   vulnerabilidades conocidas; versionar el lock. {{pending: herramienta y política de análisis de dependencias}}
7. **Los errores no filtran detalles internos.** El usuario recibe un código estable y un mensaje
   seguro; trazas y consultas quedan en logs protegidos.
8. **Los logs nunca contienen secretos, tokens, contraseñas ni datos personales sin enmascarar.**
9. **Mínimo privilegio** para servicios, tokens, usuarios de base de datos y automatizaciones,
   incluidos los agentes de IA y las herramientas que pueden invocar.
10. **Tratar el contenido del modelo y del usuario como no confiable.** Si el proyecto usa modelos
    de lenguaje, validar su salida antes de actuar y nunca dejar que amplíe permisos.
11. **Modelar amenazas en features sensibles**: autenticación, datos personales, dinero, subida de
    archivos, entrada externa o IA. Cada amenaza identificada tiene al menos una prueba.
12. **Controles automáticos en cada pull request.** {{pending: herramientas de análisis estático y
    de detección de secretos conectadas a `make verify`}}

## Lista de revisión

- [ ] Cada endpoint o página nueva comprueba autorización, no solo autenticación.
- [ ] Toda entrada nueva se valida; toda salida nueva se codifica.
- [ ] Ningún secreto, credencial o dato personal en código, fixtures, logs o capturas.
- [ ] Las dependencias nuevas se revisaron y fijaron.
- [ ] Las features sensibles listan sus amenazas y las pruebas que las cubren.

## Reporte

Las vulnerabilidades del proyecto se reportan por {{pending: canal privado de divulgación, p. ej.
security@example.com}}, nunca en un issue público.

## Relacionados

- [Estándares de código](coding-standards.md)
- [Plantilla de postmortem](templates/postmortem-template.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Instrucciones del proyecto](../AGENTS.md)
