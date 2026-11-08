# language: es
Característica: Adaptador Claude Code
  @CC-01
  Escenario: Instalar los comandos en un proyecto nuevo
    Dado un destino ausente
    Cuando se ejecuta init con agent claude sin acceso a red
    Entonces existen CLAUDE.md y diez comandos dixi en .claude/commands
    Y no se instalan hooks, settings, permisos ni servidores MCP

  @CC-02
  Escenario: No sobrescribir comandos existentes
    Dado un destino con un archivo .claude/commands/dixi.plan.md propio
    Cuando se ejecuta init con agent claude
    Entonces la operación falla con código 3 y el archivo no cambia

  @CC-03
  Escenario: Comandos con límites explícitos
    Dado un proyecto inicializado con agent claude en español o inglés
    Cuando se inspecciona cada comando instalado
    Entonces declara entrada, límites comunes y solo operaciones dixi existentes

  @CC-04
  Escenario: Detectar un comando borrado
    Dado un proyecto con agent claude sin el comando dixi.build
    Cuando se ejecuta check
    Entonces falla con código 1 e identifica el archivo ausente

  @CC-05
  Escenario: Recursos del adaptador en la distribución
    Dado el wheel construido
    Cuando se listan sus archivos
    Entonces contiene los comandos es y en

  @CC-06
  Escenario: Ejemplo público verificable
    Dado el ejemplo examples/notes
    Cuando se ejecuta check y make verify
    Entonces ambos terminan con código 0
