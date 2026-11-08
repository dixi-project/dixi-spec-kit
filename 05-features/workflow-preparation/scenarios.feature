# language: es
Característica: Preparar procedimientos sin imponer agente
  @WP-01
  Escenario: Consultar procedimientos sin proyecto
    Dado un directorio sin proyecto ni agente
    Cuando se consulta el catálogo y una receta en español o inglés
    Entonces se muestran entradas, pasos, salidas, gates y comprobaciones

  @WP-02 @WP-03
  Escenario: Preparar un objetivo explícito
    Dado un proyecto B1 y un ID compatible
    Cuando se prepara una operación con una solicitud
    Entonces el manifiesto contiene el objetivo y sus ancestros con hashes actuales
    Y no contiene cuerpos de documentos ni ramas ajenas

  @WP-02 @WP-03
  Escenario: Rechazar entradas inseguras
    Dado un objetivo inexistente o una fuente insegura
    Cuando se intenta preparar la operación
    Entonces se informa un error y no se entrega un paquete parcial

  @WP-04
  Escenario: Repetir sin efectos externos
    Dado un proyecto sin cambios
    Cuando se prepara dos veces la misma solicitud
    Entonces los paquetes son idénticos y el proyecto no cambia
    Y no se ejecuta código ni se afirma que el diseño está aprobado

  @WP-05
  Escenario: Usar la distribución instalada
    Dado un wheel original y otro reconstruido desde sdist
    Cuando se instala cada uno y se prepara un objetivo
    Entonces ambos incluyen el catálogo y recetas completas
