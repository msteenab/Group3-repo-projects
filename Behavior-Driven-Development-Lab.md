### PREREQUISITES
- Must have basic knowledge of software testing
- Must have a basic level of knowledge of the python programming language
- Must have a basic level of knowledge of html

## BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly

- Install a web browser to run the web application
    - This can be:
        - Firefox (Recommended)
        - Chrome
        - Microsoft Edge
- Create a GitHub account
  - Clone the GitHub repository
- Install a code editor
- Download Behave
- Install Gherkin

Examples of code editors:
- VS Code
- Pycharm (Recommended)

### OVERVIEW
Behave is a Python library for behavior-driven development (BDD). BDD is a software development methodology that extends test-driven development (TDD) by encouraging collaboration between developers, testers, and non-technical stakeholders like business analysts and product owners. BDD focuses on the behavior of a software system from the user's perspective and emphasizes the use of natural language to describe and document the system's functionality.

For more information on GitHub: https://github.com/CbarNC/Group3-repo-projects/blob/Selenium/Selenium%20Lab.md

#### WHAT IS GHERKIN?
Gherkin is a plain-text, domain-specific language used to describe the behavior of software systems in a human-readable format. It is commonly associated with behavior-driven development (BDD) and is often used to write feature files that define the expected behavior of a software application from the user's perspective. Gherkin is designed to be easily understood by non-technical stakeholders, such as product owners, business analysts, and domain experts, as well as developers and testers.

#### WHAT ARE FEATURE FILES?
Feature files are written in plain text and contain scenarios that describe the expected behavior of a particular feature of your application. They typically use a structured format like Gherkin, which is a language for specifying behavior using keywords like "Given," "When," and "Then."

### Step 1: Install a code editor
#### Visual Studio Code
Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft

1. Visit the official Visual Studio Code website: https://code.visualstudio.com/.

2. On the homepage, click on the "Download" button for your operating system to download the installer.

3. Once the installer is downloaded, follow the installation instructions to install VS Code. You can choose the installation location and whether to add VS Code to your PATH during installation.

4. Once the installation is complete, you can launch Visual Studio Code by finding it in your Start menu or using the desktop shortcut.

#### Pycharm
PyCharm is a popular integrated development environment (IDE) specifically designed for Python development

1. Visit the JetBrains PyCharm Community page: https://www.jetbrains.com/pycharm/download/

2. On the download page, you'll see an option to download PyCharm Community. Click on the "Download" button for the Community edition.

3. Once the download is complete, run the installer.

4. Follow the installation wizard's instructions to install PyCharm Community. You can typically choose the installation location and whether to create desktop shortcuts during installation.

5. After installation, you can launch PyCharm Community by finding it in your application menu.

### Step 2: Install Behave
You can install Selenium using Python's package manager, pip. Open your command prompt or terminal and run the following command:

`pip install behave`

![installBehave](img.png)

Once installed, a "Successfully installed" message should be displayed.

- For more information on behave, visit their website at: https://behave.readthedocs.io/en/latest/

**Note:** If you find that you have problems installing selenium on your computer, please navigate to the [FAQ](#faq) section of this document

## Step 3 (Do It Yourself - Write a Gherkin Feature File)
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
- This feature file includes syntax on how a user can register for an account on our website

### Scenario 2 (Login Functionality)

```gherkin
Feature: Login Functionality
  Scenario: User can log in with valid credentials
    Given the user is on the login page
    When they enter valid username and password
    And click the "Login" button
    Then they should be redirected to the dashboard
```
- This feature file includes syntax on how a user can log into an account on our website

### Scenario 3 (Menu Display)

```gherkin
Feature: Menu Display
  Scenario: User can view the restaurant's menu
    Given the user is on the restaurant's homepage
    When they click on the "Menu" section
    Then they should see a list of dishes and their prices
    And close browser
```
- This feature file includes syntax on how a user can display the restaurant menu on our website

### Scenario 4 (Text Area | Contact Us)

```gherkin
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
```
- This feature file includes syntax on how a user can input text in the "contact us" text area on our website

### Scenario 5 (Radio Button | Contact Us)

```gherkin
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
```
- This feature file includes syntax on how a user can select different types of radio buttons in the "contact us" section on our website

## Step 4 (Do It Yourself - Implement Step Definitions

- In order for us to implement our feature files for automated testing, we have to create step definitions with the behave and selenium libraries in python

### Scenario 1 (Test Registration)
```Python
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@given('the user is on the registration page')
def user_on_registration(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/signIn.html')
    create_account_link = context.driver.find_element(By.ID, "linkCreateAccount")
    create_account_link.click()
    time.sleep(5)
    
@when('the user fills in their information')
def user_fills_information(context):
    confirm_username = context.driver.find_element(By.ID, "signupUsername")
    confirm_username.send_keys("ValidUser")
    time.sleep(5)
    confirm_email = context.driver.find_element(By.ID, "signupEmail")
    confirm_email.send_keys("johndoe@example.com")
    time.sleep(5)

@when('clicks the "Register" button')
def click_register(context):
    submit_confirm = context.driver.find_element(By.ID, "submit-button")
    submit_confirm.click()

@then('the user should be logged in')
def user_login(context):
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/signIn.html')
```
### BREAKDOWN 1 -

- **Import Statements**
    - `behave`: The behave library
    - `selenium`: The web testing library
    - `webdriver`: The WebDriver module for implementation
    - `By`: Module that allows for locating elements on a webpage
    - `Keys`: Module that allows for keyboard interactions
    - `time`: Module that deals with time 
- **Step Definitions** 
  - *user_on_registration*
    - The `@given` decorator, represents the context of the test
    - It opens a Chrome web browser using Selenium's `webdriver.Chrome()` and navigates to a specific URL
    - It finds an element on the page with the ID "linkCreateAccount" and clicks on it
    - It then adds a delay of 5 seconds using `time.sleep(5)`
  - *user_fills_information*
    - The `@when` decorator, represents the action of the user filling in their information
    - It finds elements on the page with the IDs "signupUsername" and "signupEmail" and enters values into them
    - It adds delays of 5 seconds between actions
  - *click_register*
    - The `@when` decorator, represents the action of the user clicking the "Register" button
    - It finds an element on the page with the ID "submit-button" and clicks on it
  - *user_login*
    - The `@then` decorator, represents the expected outcome of the test, where the user should be logged in
    - It navigates to the login page using `context.driver.get()`

### Scenario 2 (Test Login)

```Python
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('the user is on the login page')
def loginPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")

@when('they enter valid username and password')
def userPass(context):
    username_input = context.driver.find_elements(By.ID, 'username')
    password_input = context.driver.find_elements(By.ID, 'password')
    username_input.send_keys('test_user123')
    password_input.send_keys('password123')

@when('click the "Login" button')
def clickLogin(context):
    login_button = context.driver.find_element_by_id('login_button')
    login_button.click()

@then('they should be redirected to the dashboard')
def redirect(context):
    current_url = context.driver.current_url
    assert current_url == 'https://cbarnc.github.io/Group3-repo-projects/'
```
### BREAKDOWN 2 -

- **Step Definitions**
  - *loginPage*
    - The `@given` decorator, represents the context of the test
    - It opens a Chrome web browser using Selenium's `webdriver.Chrome()` and navigates to a specific URL
  - *userPass*
    - The `@when` decorator, represents the action of the user entering their username and password
    - It finds elements on the page with the IDs "username" and "password" and enters values into them
  - *clickLogin*
    - The `@when` decorator, represents the action of the user clicking the "Login" button
    - It finds an element on the page with the ID "login_button" and clicks on it
  - *redirect*
    - The `@then` decorator, represents the expected outcome of the test, where the user should be redirected to the dashboard
    - It navigates to the homepage using `context.driver.current_url`

### Scenario 3 (Test Menu Display)
```Python
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('the user is on the restaurant\'s homepage')
def homePage(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/")


@when('they click on the "Menu" section')
def openMenu(context):
    menuElements = context.driver.find_elements(By.CLASS_NAME, 'menu')
    assert len(menuElements) > 0, "No menu Elements on this page"


@then('they should see a list of dishes and their prices')
def menuList(context):
    context.driver.find_elements(By.CLASS_NAME, 'menu')


@then('close browser')
def closeBrowser(context):
    context.driver.close()

```
### BREAKDOWN 3 -

- **Step Definitions**
  - *homePage*
    - The `@given` decorator, represents the context of the test
    - It opens a Chrome web browser using Selenium's `webdriver.Chrome()` and navigates to a specific URL
  - *openMenu*
    - The `@when` decorator, represents the action of the user clicking the "Menu" section
    - It finds elements on the page with the class name "menu" and determines whether the menu page has items or not
  - *menuList*
    - The `@then` decorator, represents the action of the user seeing a list of menu dishes and their prices
    - It finds an element on the page with the class name 'menu'
  - *closeBrowser*
    - The `@then` decorator, represents the expected outcome of the test, where the browser should be closed
    - It closes the browser using `context.driver.close()`

## Step 5 (Do It Yourself - Run Behave Tests)
