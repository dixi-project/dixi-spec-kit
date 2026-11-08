# language: en
Feature: Guided workflow with traceability and evidence
  As a person who develops with Dixi
  I want commands that keep my artifacts connected
  So that I can build and evolve features without losing context or controls

  @WF-01 @S01
  Scenario: Discover and specify with incomplete information
    Given an initialized project and an idea with no defined retention rules
    When the person walks through discover and specify
    Then vision, story and criteria are left linked
    And retention appears as a pending question and not as a confirmed decision

  @WF-02 @S02
  Scenario: Reuse design when preparing the plan
    Given a domain, a proposed ADR and a contract created by direct commands
    When the person runs plan on the feature that references them
    Then the plan uses the same identifiers and documents
    And it creates no contradictory copies and does not declare the ADR accepted

  @WF-02 @S03
  Scenario: Incorporate threats into the plan
    Given a feature with external input and a documented trust boundary
    When threat-model is run and its plan is prepared
    Then each applicable threat references a mitigation and a planned test
    And no planned test appears as executed

  @WF-03 @S04
  Scenario: Detect criteria without tasks and circular dependencies
    Given a plan with a criterion without a task and two tasks that depend on each other
    When tasks is run on that plan
    Then the uncovered criterion and the cycle are reported
    And the set is not declared ready to build

  @WF-04 @S05
  Scenario: Respect structural validation
    Given a level 3 story and its ADR pending human validation
    When build is requested for that story
    Then the pending gate is reported
    And no implementation is written and no human approval is recorded

  @WF-04 @S06
  Scenario: Build with tests first
    Given a validated task with a verifiable criterion and the gates resolved
    When build is run
    Then a new test fails because of the pending behavior
    And the red is recorded in a test commit before implementing
    And the final result includes the real verification evidence

  @WF-04 @S07
  Scenario: Preserve a frozen test
    Given a committed test that contradicts the new request
    When build detects that it would require changing that test
    Then it keeps the test unchanged
    And it asks the person to resolve the contradiction

  @WF-05 @S08
  Scenario: Analyze contradictory specs
    Given a business rule and a contract with incompatible behaviors
    When analyze is run
    Then the report identifies both artifacts and the contradiction
    And it does not modify the sources to resolve it silently

  @WF-05 @S09
  Scenario: Report incomplete verification
    Given a project without make verify and with a mandatory test not executed
    When verify is run
    Then the result is partial and lists what is missing
    And it does not declare complete verification or invent results

  @WF-05 @S10
  Scenario: Review with evidence from another revision
    Given a diff with an explicit base and evidence prior to a contract change
    When review is run
    Then the report marks the affected evidence as stale
    And it neither approves nor integrates the change

  @WF-06 @S11
  Scenario: Resume an interrupted write
    Given an execution interrupted after creating a story
    And a later local edit of that story
    When the operation is resumed with the same target
    Then the story identifier is reused
    And the local edit is preserved or a conflict is reported without overwriting it

  @WF-06 @S12
  Scenario: Check status without modifying files
    Given a project with partial work and no access to GitHub
    When status is run
    Then the real progress and the next step are shown
    And the project files remain identical

  @WF-06 @S13
  Scenario: Prevent a private handoff in a versioned path
    Given that .context is included in the Git index
    When handoff is run
    Then writing the private context is blocked
    And no push is made and tasks are not altered to declare them done

  @WF-07 @S14
  Scenario: Propose a compatible evolution
    Given the verified notes example and a request for an optional filter
    When change is run for that feature
    Then the affected specs, contract, tasks and tests are identified
    And a linked proposal is produced without applying the change automatically

  @WF-07 @S15
  Scenario: Propose an incompatible change
    Given a fixture that represents a published contract and an incompatible request
    When change is run
    Then the compatibility gate and the required decision are identified
    And the published contract and the frozen tests remain unmodified

  @WF-08 @S16
  Scenario: Run the workflow from installed resources
    Given the package installed in a clean environment with the supported agent
    When a person completes the notes example and prepares its review
    Then all commands find their resources inside the distribution
    And the evidence identifies the environment and the executed controls
    And the help only announces the included and verified commands

  @WF-09 @S17
  Scenario: Choose an integration without imposing its format on the core
    Given core resources and two adapters included in the distribution
    When equivalent projects are initialized choosing a different adapter in each one
    Then the canonical artifacts keep the same format and identifiers
    And only the integration resources and their configuration reflect the choice
    And the other agent's executable is neither installed nor authenticated

  @WF-09 @S18
  Scenario: Use the method without an agent integration
    Given a CLI installation with no agents installed
    When a project is initialized without selecting an integration
    Then the core, templates and operation guides are delivered
    And doctor does not require an agent and check can validate the structure
    And build is not presented as automation available without an integration

  @WF-10 @S19
  Scenario: Verify examples in languages other than the installer's runtime
    Given two equivalent examples in different languages and at least one different from the CLI runtime
    When the workflow of each example is run with each adapter intended to be announced
    Then their profiles connect the stack's checks with make verify
    And the evidence identifies language, system and version of each evaluated integration
    And the kit does not require converting the user's code to the installer's language

  @WF-10 @S20
  Scenario: Detect a mandatory control unavailable in an integration
    Given an adapter without a required test-protection mechanism
    And no documented and verified equivalent mechanism
    When doctor is consulted and build is requested
    Then doctor reports the limitation and build blocks the dependent operation
    And Markdown instructions are not presented as an implemented hook
