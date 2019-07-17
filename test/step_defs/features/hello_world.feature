Feature: To test the Hello World Class

  Scenario: Hello world should return the correct message
    Given I create a hello world object with the message "Hi_Batman"
    Then the message "Hi_Batman" should be returned

  Scenario: Hello world should return the correct message
    Given I create a hello world object with the message "Hi_Batman"
    Then the message "Bye_Batman" should be returned