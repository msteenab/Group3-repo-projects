Feature: Contact Us Box - Text Area

  Scenario: User submits a message via the contact form
    Given the user is on the Contact Us page
    When the user fills in their name "John Doe"
    And the user enters their email "johndoe@example.com"
    And the user writes a message in the text area:
      """
      This is a test message.
      """
    And the user clicks the "Submit" button
    Then the message should be sent successfully