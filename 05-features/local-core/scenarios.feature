# language: es
Característica: Núcleo local sin dependencia de agente
  @LC-01
  Escenario: Consultar capacidades reales
    Dado un directorio sin proyecto ni agente
    Cuando se consulta ayuda y versión
    Entonces solo se anuncian operaciones disponibles y una versión de desarrollo

  @LC-02 @LC-04
  Escenario: Crear y comprobar un proyecto documental
    Dado un destino ausente y recursos locales es/en
    Cuando se ejecuta init con agent none y luego check y doctor
    Entonces la estructura es válida y el baseline identifica los archivos generados
    Y no se requiere agente ni se afirma verificación de código de aplicación

  @LC-03
  Escenario: Preservar un destino ocupado
    Dado un destino con archivos del usuario o un enlace simbólico
    Cuando se intenta inicializarlo
    Entonces se informa conflicto y el contenido permanece idéntico

  @LC-04 @LC-05
  Escenario: Comprobar datos no confiables sin ejecutar instrucciones
    Dado metadata alterada y enlaces a rutas inseguras
    Cuando se ejecuta check
    Entonces se informan errores sin leer fuera de la raíz ni ejecutar código del proyecto

  @LC-06
  Escenario: Instalar artefactos locales limpios
    Dado wheel y sdist construidos con inventario explícito
    Cuando se instalan sin índice en entornos temporales
    Entonces la CLI genera un proyecto verificable
    Y no hay recursos privados ni dependencias externas de ejecución en los artefactos
