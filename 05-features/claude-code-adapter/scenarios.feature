# language: en
Feature: Claude Code adapter
  @CC-01
  Scenario: Install the commands in a new project
    Given a missing destination
    When init is run with agent claude without network access
    Then CLAUDE.md and ten dixi commands exist in .claude/commands
    And no hooks, settings, permissions or MCP servers are installed

  @CC-02
  Scenario: Do not overwrite existing commands
    Given a destination with its own .claude/commands/dixi.plan.md file
    When init is run with agent claude
    Then the operation fails with code 3 and the file does not change

  @CC-03
  Scenario: Commands with explicit limits
    Given a project initialized with agent claude in Spanish or English
    When each installed command is inspected
    Then it declares input, common limits and only existing dixi operations

  @CC-04
  Scenario: Detect a deleted command
    Given a project with agent claude missing the dixi.build command
    When check is run
    Then it fails with code 1 and identifies the missing file

  @CC-05
  Scenario: Adapter resources in the distribution
    Given the built wheel
    When its files are listed
    Then it contains the es and en commands

  @CC-06
  Scenario: Verifiable public example
    Given the example examples/notes
    When check and make verify are run
    Then both finish with code 0
