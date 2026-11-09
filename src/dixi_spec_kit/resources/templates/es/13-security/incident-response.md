# Respuesta a incidentes

## Propósito

Dar al equipo un camino corto y ensayado para detectar, contener, resolver y aprender de los incidentes de seguridad, de modo que las decisiones bajo presión sigan un plan y no la improvisación.

Estado: borrador. {{pending: nombrar a la persona líder de incidentes y a su suplente}}

## Qué cuenta como incidente

- Secreto o credencial filtrado o usado indebidamente.
- Acceso no autorizado a datos, cuentas o infraestructura.
- Vulnerabilidad explotada o dependencia maliciosa.
- Pérdida, corrupción o divulgación inesperada de datos.
- Un agente de IA o una automatización actuando fuera del alcance concedido.
- {{pending: añadir casos propios del proyecto}}

## Niveles de severidad

| Nivel | Ejemplo | Objetivo de respuesta |
|-------|---------|-----------------------|
| Crítico | Exposición activa de datos, producción comprometida | {{pending: tiempo para iniciar la respuesta}} |
| Alto | Fallo explotable, secreto de producción filtrado | {{pending: objetivo}} |
| Medio | Exposición limitada, sin evidencia de abuso | {{pending: objetivo}} |
| Bajo | Debilidad sin impacto inmediato | {{pending: objetivo}} |

## Contactos

| Rol | Contacto | Suplente |
|-----|----------|----------|
| Líder de incidentes | {{pending: nombre, security@example.com}} | {{pending: suplente}} |
| Responsable técnico | {{pending: contacto}} | {{pending: suplente}} |
| Comunicación / legal | {{pending: contacto}} | {{pending: suplente}} |

## Fases

1. **Detectar y reportar**: cualquiera puede abrir un incidente; registra la hora y lo observado.
2. **Clasificar**: asigna severidad y líder; abre un registro privado.
3. **Contener**: revoca credenciales, desactiva accesos afectados, aísla componentes. Conserva evidencia antes de destruir nada.
4. **Erradicar**: elimina la causa (parche, rotación, retirada de código malicioso).
5. **Recuperar**: restablece el servicio, verifica la integridad, vigila de cerca.
6. **Notificar**: decide si hay que informar a usuarios, socios o autoridades. {{pending: listar obligaciones de notificación aplicables y plazos}}
7. **Aprender**: haz una revisión sin culpables; convierte los hallazgos en specs, pruebas y actualizaciones del modelo de amenazas.

## Registro del incidente

Para cada incidente conserva: ID, fechas y horas, severidad, cronología, activos afectados, acciones tomadas, personas involucradas, causa raíz y tareas de seguimiento con responsable.

## Ensayo

Practica el plan con un ejercicio de mesa. {{pending: definir la frecuencia del ensayo}}

## Relacionados

- [Modelo de amenazas](threat-model.md)
- [Gestión de secretos](secret-management.md)
- [Endurecimiento de agentes de IA](ai-agent-hardening.md)
- [Proyecto](../00-master-spec.md)
