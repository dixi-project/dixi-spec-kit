# language: en
Feature: Prepare procedures without imposing an agent
  @WP-01
  Scenario: View procedures without a project
    Given a directory with no project and no agent
    When the catalog and a recipe are requested in Spanish or English
    Then inputs, steps, outputs, gates and checks are shown

  @WP-02 @WP-03
  Scenario: Prepare an explicit target
    Given a B1 project and a compatible ID
    When an operation is prepared with a request
    Then the manifest contains the target and its ancestors with current hashes
    And it contains no document bodies and no unrelated branches

  @WP-02 @WP-03
  Scenario: Reject unsafe inputs
    Given a nonexistent target or an unsafe source
    When an attempt is made to prepare the operation
    Then an error is reported and no partial package is delivered

  @WP-04
  Scenario: Repeat without external effects
    Given a project without changes
    When the same request is prepared twice
    Then the packages are identical and the project does not change
    And no code is executed and the design is not claimed to be approved

  @WP-05
  Scenario: Use the installed distribution
    Given an original wheel and another rebuilt from sdist
    When each one is installed and a target is prepared
    Then both include the catalog and complete recipes
