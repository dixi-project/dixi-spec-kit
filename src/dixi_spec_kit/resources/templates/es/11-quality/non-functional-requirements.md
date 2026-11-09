# Requisitos no funcionales

## Propósito

Registrar las cualidades que el sistema debe tener más allá de las funcionalidades, como rendimiento, disponibilidad, accesibilidad y privacidad, de forma que se puedan medir y probar.

Estado: borrador. {{pending: acordar los requisitos no funcionales con la persona dueña del producto}}

## Cómo redactar uno

Cada requisito tiene un ID, un objetivo medible, una forma de verificarlo y un responsable. Evita «rápido» o «seguro»; indica un número o una condición comprobable.

| ID | Cualidad | Requisito | Objetivo | Verificación | Responsable |
|----|----------|-----------|----------|--------------|-------------|
| NFR-001 | Rendimiento | Las páginas principales cargan rápido | {{pending: objetivo, ver presupuestos de web vitals}} | {{pending: cómo se mide}} | {{pending: responsable}} |
| NFR-002 | Disponibilidad | El servicio está accesible | {{pending: objetivo}} | {{pending: cómo se mide}} | {{pending: responsable}} |
| NFR-003 | Accesibilidad | La interfaz se puede usar con tecnologías de apoyo | {{pending: estándar y nivel}} | {{pending: cómo se comprueba}} | {{pending: responsable}} |
| NFR-004 | Internacionalización | El contenido está disponible en cada idioma soportado con su propia URL | {{pending: idiomas}} | {{pending: cómo se comprueba}} | {{pending: responsable}} |
| NFR-005 | Privacidad | Los datos personales se minimizan y protegen | {{pending: reglas}} | {{pending: cómo se comprueba}} | {{pending: responsable}} |
| NFR-006 | Mantenibilidad | El código supera la escalera de verificación | Todos los peldaños en verde | `make verify` | {{pending: responsable}} |

## Categorías a considerar

- Rendimiento y capacidad
- Disponibilidad y recuperación
- Seguridad y privacidad
- Accesibilidad
- Internacionalización y localización
- Observabilidad (logs, métricas, alertas)
- Compatibilidad (navegadores, dispositivos, versiones)
- Mantenibilidad y operabilidad

{{pending: quitar las categorías que no aplican y justificar por qué}}

## Reglas

- Los objetivos los deciden personas y se registran aquí. Los agentes pueden proponer objetivos, pero nunca bajar uno acordado para que una verificación pase.
- Un requisito sin método de verificación está incompleto.
- Enlaza cada requisito con las funcionalidades o contratos que restringe.

## Relacionados

- [Estrategia de calidad](quality-strategy.md)
- [Presupuestos de web vitals](performance-budgets/web-vitals-budgets.md)
- [Revisión basada en riesgo](risk-based-review.md)
- [Plan de pruebas](test-plan.md)
- [Proyecto](../00-master-spec.md)
