### PREREQUISITES
- Must have basic knowledge of software testing
- Must have a basic level of knowledge of the python programming language
- Must have a basic level of knowledge of html

### BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly

- Install a web browser to run the web application
    - This can be:
        - Firefox (Recommended)
        - Chrome
        - Microsoft Edge
- Install a code editor
- Download Behave
- Install Gherkin

Examples of code editors:
- VS Code
- Pycharm (Recommended)

### OVERVIEW
Behave is a Python library for behavior-driven development (BDD). BDD is a software development methodology that extends test-driven development (TDD) by encouraging collaboration between developers, testers, and non-technical stakeholders like business analysts and product owners. BDD focuses on the behavior of a software system from the user's perspective and emphasizes the use of natural language to describe and document the system's functionality.

#### WHAT IS GHERKIN?
Gherkin is a plain-text, domain-specific language used to describe the behavior of software systems in a human-readable format. It is commonly associated with behavior-driven development (BDD) and is often used to write feature files that define the expected behavior of a software application from the user's perspective. Gherkin is designed to be easily understood by non-technical stakeholders, such as product owners, business analysts, and domain experts, as well as developers and testers.

#### WHAT ARE FEATURE FILES?
Feature files are written in plain text and contain scenarios that describe the expected behavior of a particular feature of your application. They typically use a structured format like Gherkin, which is a language for specifying behavior using keywords like "Given," "When," and "Then."

## (Do It Yourself)
Website used for these demonstrations: https://cbarnc.github.io/Group3-repo-projects/

### Scenario 1 (User Registration)

```gherkin

Feature: User Registration
  Scenario: User can register for an account
    Given the user is on the registration page
    When the user fills in their information
    And clicks the "Register" button
    Then the user should be logged in
```

### Scenario 2 (Login Functionality)

```gherkin
Feature: Login Functionality
  Scenario: User can log in with valid credentials
    Given the user is on the login page
    When they enter valid username and password
    And click the "Login" button
    Then they should be redirected to the dashboard
```

### Scenario 3 (Password Reset)

```gherkin
Feature: Password Reset
  Scenario: User can request a password reset
    Given the user is on the login page
    When they click the "Forgot Password" link
    And provide their email address
    And submit the request
    Then they should receive a password reset email
```

### Scenario 4 (Menu Display)

```gherkin
Feature: Menu Display
  Scenario: User can view the restaurant's menu
    Given the user is on the restaurant's homepage
    When they click on the "Menu" section
    Then they should see a list of dishes and their prices
```

### Scenario 5 (Restaurant Reviews)

```gherkin
Feature: Restaurant Reviews
  Scenario: User can read and write restaurant reviews
    Given the user is on the restaurant's page
    When they scroll down to the "Reviews" section
    And they read existing reviews
    And they write and submit their own review
    Then their review should be visible among the others
```


### Scenario 6 (Contact Information)

```gherkin
Feature: Contact Information
  Scenario: User can find restaurant contact details
    Given the user is on the restaurant's homepage
    When they navigate to the "Contact" page
    Then they should find the restaurant's address, phone number, and email
```
