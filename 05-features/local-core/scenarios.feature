# language: en
Feature: Local core without agent dependency
  @LC-01
  Scenario: View the real capabilities
    Given a directory with no project and no agent
    When help and version are requested
    Then only available operations and a development version are announced

  @LC-02 @LC-04
  Scenario: Create and check a documentation-only project
    Given a missing destination and local es/en resources
    When init is run with agent none and then check and doctor
    Then the structure is valid and the baseline identifies the generated files
    And no agent is required and no verification of application code is claimed

  @LC-03
  Scenario: Preserve an occupied destination
    Given a destination with user files or a symbolic link
    When an attempt is made to initialize it
    Then a conflict is reported and the content remains identical

  @LC-04 @LC-05
  Scenario: Check untrusted data without executing instructions
    Given tampered metadata and links to unsafe paths
    When check is run
    Then errors are reported without reading outside the root or executing project code

  @LC-06
  Scenario: Install clean local artifacts
    Given a wheel and an sdist built from an explicit inventory
    When they are installed without an index in temporary environments
    Then the CLI generates a verifiable project
    And there are no private resources or external runtime dependencies in the artifacts
