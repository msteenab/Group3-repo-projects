import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/")

# maximizing window
driver.maximize_window()

# go to sign up page
element = driver.find_element(By.LINK_TEXT, "SIGN IN")

# click the element
element.click()

# click on sign up
create_account_link = driver.find_element(By.ID, "linkCreateAccount")
create_account_link.click()

# Create variables for login credentials.
username = "your username"
password = "your password"

# Find the username/email field and send the username to the input field.
uname = driver.find_element("id", "signupUsername")
uname.send_keys("CscTeam3")

# Verify that the login was successful.
error_message = "Incorrect username or password."
# Retrieve any errors found.
errors = driver.find_elements(By.CLASS_NAME, "form__input-error-message")

time.sleep(8)
# Close the driver
driver.close()
