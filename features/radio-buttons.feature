Feature: Contact Us Box - Radio Buttons

  Scenario: User selects a contact method via radio buttons
    Given the user is on the Contact Us page
    When the user selects the "Email" option
    And the user enters their email "johndoe@example.com"
    And the user clicks the "Submit" button
    Then the email should be sent successfully

  Scenario: User selects a different contact method via radio buttons
    Given the user is on the Contact Us page
    When the user selects the "Phone" option
    And the user enters their phone number "123-456-7890"
    And the user clicks the "Submit" button
    Then the phone call should be initiated successfully