# Modelo de amenazas

## Propósito

Identificar qué debe proteger el proyecto, quién podría atacarlo y cómo, y vincular cada mitigación con una verificación trazable hasta el plan de pruebas. Es un documento vivo: actualízalo cuando una funcionalidad cambie un límite de confianza, añada un flujo de datos o maneje datos sensibles nuevos.

Estado: borrador. {{pending: nombrar a la persona responsable de mantener y revisar este modelo}}

## Alcance

- Sistema o funcionalidades cubiertas: {{pending: listar funcionalidades y componentes incluidos}}
- Fuera de alcance y por qué: {{pending: listar exclusiones}}
- Fecha de la última revisión: {{pending: fecha}}

## Activos

| ID | Activo | Por qué importa | Sensibilidad |
|----|--------|-----------------|--------------|
| AS-01 | {{pending: p. ej. cuentas de usuario}} | {{pending: impacto si se compromete}} | {{pending: baja / media / alta}} |

## Actores y límites de confianza

| Actor | Nivel de confianza | Puntos de entrada |
|-------|--------------------|-------------------|
| Visitante anónimo | No confiable | {{pending: páginas públicas, formularios, APIs}} |
| Usuario autenticado | Parcialmente confiable | {{pending: puntos de entrada}} |
| Operador o administrador | Confiable, auditado | {{pending: puntos de entrada}} |
| Agente de IA de desarrollo | No confiable por defecto | Repositorio, terminal, herramientas concedidas |

Dibuja o describe el flujo de datos: qué componente habla con cuál, por qué canal y dónde los datos cruzan un límite de confianza. {{pending: añadir la descripción o el diagrama de flujo de datos}}

## Método: STRIDE por flujo de datos

Para cada flujo que cruza un límite, haz las seis preguntas:

- **Suplantación (Spoofing)**: ¿alguien puede hacerse pasar por otro usuario o servicio?
- **Manipulación (Tampering)**: ¿se pueden alterar datos en tránsito o en reposo?
- **Repudio (Repudiation)**: ¿se puede negar una acción por falta de registros?
- **Divulgación de información**: ¿pueden llegar datos a quien no debe verlos?
- **Denegación de servicio**: ¿se puede agotar o bloquear el flujo?
- **Elevación de privilegios**: ¿alguien puede obtener derechos que no le corresponden?

## Amenazas, mitigaciones y verificación

| ID | Flujo / activo | STRIDE | Amenaza | Mitigación | Verificación (prueba o control) | Estado |
|----|----------------|--------|---------|------------|---------------------------------|--------|
| TH-01 | {{pending: flujo}} | S | {{pending: amenaza}} | {{pending: control}} | {{pending: ID de prueba en el plan}} | abierta |

Toda mitigación necesita una verificación. Una mitigación sin prueba o control planificado es un hueco conocido, no un control. Escribir aquí un ID de prueba no significa que se haya ejecutado.

## Riesgos aceptados

Las amenazas que no se mitigarán ahora deben aceptarse de forma explícita, con responsable y fecha de revisión. {{pending: listar riesgos aceptados o indicar «ninguno»}}

## Cómo trabajarlo

- Prepara el contexto con `dixi workflow prepare threat-model`, o usa `/dixi.threat-model` (Claude Code) o `$dixi-threat-model` (Codex) si la integración está instalada.
- Ejecuta `dixi check` tras editar para mantener la estructura y las referencias coherentes.
- Una persona revisa y aprueba el resultado; un agente puede redactar, no aprobar.

## Relacionados

- [Proyecto](../00-master-spec.md)
- [Plan de pruebas](../11-quality/test-plan.md)
- [Gestión de secretos](secret-management.md)
- [Respuesta a incidentes](incident-response.md)
- [Endurecimiento de agentes de IA](ai-agent-hardening.md)
