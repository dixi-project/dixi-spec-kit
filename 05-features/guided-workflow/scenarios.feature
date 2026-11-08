# language: es
Característica: Recorrido guiado con trazabilidad y evidencia
  Como persona que desarrolla con Dixi
  Quiero comandos que mantengan conectados mis artefactos
  Para construir y evolucionar funcionalidades sin perder contexto ni controles

  @WF-01 @S01
  Escenario: Descubrir y especificar con información incompleta
    Dado un proyecto inicializado y una idea sin reglas de retención definidas
    Cuando la persona recorre discover y specify
    Entonces quedan visión, historia y criterios enlazados
    Y la retención aparece como pregunta pendiente y no como decisión confirmada

  @WF-02 @S02
  Escenario: Reutilizar diseño al preparar el plan
    Dado un dominio, un ADR propuesto y un contrato creados por comandos directos
    Cuando la persona ejecuta plan sobre la feature que los referencia
    Entonces el plan utiliza los mismos identificadores y documentos
    Y no crea copias contradictorias ni declara aceptado el ADR

  @WF-02 @S03
  Escenario: Incorporar amenazas al plan
    Dado una feature con entrada externa y un límite de confianza documentado
    Cuando se ejecuta threat-model y se prepara su plan
    Entonces cada amenaza aplicable referencia una mitigación y una prueba prevista
    Y ninguna prueba prevista aparece como ejecutada

  @WF-03 @S04
  Escenario: Detectar criterios sin tareas y dependencias circulares
    Dado un plan con un criterio sin tarea y dos tareas que dependen entre sí
    Cuando se ejecuta tasks sobre ese plan
    Entonces se informan el criterio descubierto y el ciclo
    Y el conjunto no se declara listo para construir

  @WF-04 @S05
  Escenario: Respetar la validación estructural
    Dado una historia de nivel 3 y su ADR pendientes de validación humana
    Cuando se solicita build para esa historia
    Entonces se informa el gate pendiente
    Y no se escribe implementación ni se registra una aprobación humana

  @WF-04 @S06
  Escenario: Construir con pruebas primero
    Dado una tarea validada con criterio verificable y los gates resueltos
    Cuando se ejecuta build
    Entonces una prueba nueva falla por el comportamiento pendiente
    Y el rojo se registra en un commit de pruebas antes de implementar
    Y el resultado final incluye la evidencia real de verificación

  @WF-04 @S07
  Escenario: Preservar una prueba congelada
    Dado una prueba commiteada que contradice la nueva solicitud
    Cuando build detecta que requeriría cambiar esa prueba
    Entonces conserva la prueba sin cambios
    Y pide resolver la contradicción a la persona

  @WF-05 @S08
  Escenario: Analizar specs contradictorias
    Dado una regla de negocio y un contrato con comportamientos incompatibles
    Cuando se ejecuta analyze
    Entonces el informe identifica ambos artefactos y la contradicción
    Y no modifica las fuentes para resolverla silenciosamente

  @WF-05 @S09
  Escenario: Informar verificación incompleta
    Dado un proyecto sin make verify y con una prueba obligatoria no ejecutada
    Cuando se ejecuta verify
    Entonces el resultado es partial y enumera lo que falta
    Y no declara verificación completa ni inventa resultados

  @WF-05 @S10
  Escenario: Revisar con evidencia de otra revisión
    Dado un diff con base explícita y evidencia anterior a un cambio del contrato
    Cuando se ejecuta review
    Entonces el informe marca la evidencia afectada como desactualizada
    Y no aprueba ni integra el cambio

  @WF-06 @S11
  Escenario: Retomar una escritura interrumpida
    Dado una ejecución interrumpida después de crear una historia
    Y una edición local posterior de esa historia
    Cuando se retoma la operación con el mismo objetivo
    Entonces se reutiliza el identificador de la historia
    Y se conserva la edición local o se informa un conflicto sin sobrescribirla

  @WF-06 @S12
  Escenario: Consultar estado sin modificar archivos
    Dado un proyecto con trabajo parcial y sin acceso a GitHub
    Cuando se ejecuta status
    Entonces se muestra el avance real y el siguiente paso
    Y los archivos del proyecto permanecen idénticos

  @WF-06 @S13
  Escenario: Impedir un handoff privado en una ruta versionada
    Dado que .context está incluido en el índice de Git
    Cuando se ejecuta handoff
    Entonces se bloquea la escritura del contexto privado
    Y no se hace push ni se alteran tareas para declararlas terminadas

  @WF-07 @S14
  Escenario: Proponer una evolución compatible
    Dado el ejemplo de notas verificado y una solicitud de filtro opcional
    Cuando se ejecuta change para esa funcionalidad
    Entonces se identifican specs, contrato, tareas y pruebas afectados
    Y se produce una propuesta enlazada sin aplicar el cambio automáticamente

  @WF-07 @S15
  Escenario: Proponer un cambio incompatible
    Dado una fixture que representa un contrato publicado y una solicitud incompatible
    Cuando se ejecuta change
    Entonces se identifica el gate de compatibilidad y la decisión requerida
    Y el contrato publicado y las pruebas congeladas quedan sin modificar

  @WF-08 @S16
  Escenario: Ejecutar el recorrido desde recursos instalados
    Dado el paquete instalado en un entorno limpio con el agente soportado
    Cuando una persona completa el ejemplo de notas y prepara su revisión
    Entonces todos los comandos encuentran sus recursos dentro de la distribución
    Y la evidencia identifica el entorno y los controles ejecutados
    Y la ayuda solo anuncia los comandos incluidos y verificados

  @WF-09 @S17
  Escenario: Elegir una integración sin imponer su formato al núcleo
    Dado recursos del núcleo y dos adaptadores incluidos en la distribución
    Cuando se inicializan proyectos equivalentes eligiendo un adaptador distinto en cada uno
    Entonces los artefactos canónicos conservan el mismo formato e identificadores
    Y solo los recursos de integración y su configuración reflejan la elección
    Y no se instala ni autentica el ejecutable de otro agente

  @WF-09 @S18
  Escenario: Usar el método sin integración de agente
    Dado una instalación de la CLI sin agentes instalados
    Cuando se inicializa un proyecto sin seleccionar integración
    Entonces se entregan núcleo, plantillas y guías de las operaciones
    Y doctor no exige un agente y check puede validar la estructura
    Y no se presenta build como automatización disponible sin integración

  @WF-10 @S19
  Escenario: Verificar ejemplos en lenguajes distintos al runtime del instalador
    Dado dos ejemplos equivalentes en lenguajes distintos y al menos uno diferente al runtime de la CLI
    Cuando se ejecuta el recorrido de cada ejemplo con cada adaptador que se pretende anunciar
    Entonces sus perfiles conectan las comprobaciones del stack con make verify
    Y las evidencias identifican lenguaje, sistema y versión de cada integración evaluada
    Y el kit no exige convertir el código del usuario al lenguaje del instalador

  @WF-10 @S20
  Escenario: Detectar un control obligatorio no disponible en una integración
    Dado un adaptador sin un mecanismo requerido de protección de pruebas
    Y ningún mecanismo equivalente documentado y verificado
    Cuando se consulta doctor y se solicita build
    Entonces doctor informa la limitación y build bloquea la operación dependiente
    Y unas instrucciones en Markdown no se presentan como un hook implementado
