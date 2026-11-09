# Controles de protección de datos

## Propósito

Listar los datos personales y sensibles que maneja el proyecto y los controles técnicos y organizativos que los protegen durante todo su ciclo de vida: recogida, uso, almacenamiento, compartición y eliminación.

Estado: borrador. {{pending: nombrar al responsable de protección de datos}}

## Obligaciones aplicables

Qué leyes, contratos o políticas internas aplican depende de los usuarios y mercados atendidos. {{pending: listar obligaciones aplicables; esta plantilla no declara conformidad con ninguna}}

## Inventario de datos

| Categoría | Ejemplos | Clasificación | Finalidad | Base legal o justificación | Conservación |
|-----------|----------|---------------|-----------|----------------------------|--------------|
| {{pending: p. ej. datos de contacto}} | {{pending: nombre, correo}} | {{pending: pública / interna / confidencial / restringida}} | {{pending: finalidad}} | {{pending: base}} | {{pending: plazo}} |

## Controles

| Control | Descripción | Estado |
|---------|-------------|--------|
| Minimización | Recoger solo lo que la finalidad necesita | {{pending: planificado / implantado}} |
| Cifrado en tránsito | Todo el tráfico externo e interno cifrado | {{pending: estado}} |
| Cifrado en reposo | Almacenes y copias de seguridad cifrados | {{pending: estado}} |
| Control de acceso | Mínimo privilegio, revisado periódicamente | {{pending: estado}} |
| Higiene de logs | Sin datos personales ni secretos en los logs | {{pending: estado}} |
| Seudonimización | Los entornos no productivos usan datos sintéticos o enmascarados | {{pending: estado}} |
| Eliminación | Datos borrados al fin de la conservación o ante una solicitud válida | {{pending: estado}} |
| Copias de seguridad | Restauración probada, mismas protecciones que los datos principales | {{pending: estado}} |

«Implantado» significa implementado y verificado por una prueba o revisión registrada en otro lugar, no solo escrito aquí.

## Solicitudes de los titulares

Cómo se reciben, verifican y completan las solicitudes de acceso, rectificación, portabilidad y supresión. {{pending: definir el proceso y el plazo de respuesta}}

## Terceros y transferencias

| Destinatario | Datos compartidos | Finalidad | Garantías |
|--------------|-------------------|-----------|-----------|
| {{pending: categoría de encargado}} | {{pending: datos}} | {{pending: finalidad}} | {{pending: acuerdo, ubicación}} |

## Gestión de brechas

Las brechas de datos personales siguen el proceso de respuesta a incidentes, incluidos los plazos de notificación que apliquen.

## Relacionados

- [Modelo de amenazas](threat-model.md)
- [Respuesta a incidentes](incident-response.md)
- [Registro de riesgos](risk-register.md)
- [Gestión de secretos](secret-management.md)
