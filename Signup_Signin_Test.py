from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

####   Not Finished    #####
driver = webdriver.Chrome()

driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")

try:
    create_account_link = driver.find_element(By.ID, "linkCreateAccount")
    create_account_link.click()

    username_input = driver.find_element(By.ID, "signupUsername")

    username_input.send_keys("short")
    driver.implicitly_wait(2)
    error_message = driver.find_element(By.CLASS_NAME, "form__input-error-message")
    assert "username must be at least 10 characters in length" in error_message.text
    driver.implicitly_wait(2)

    login_form = driver.find_element(By.ID, "Login")
    login_form.submit()

    driver.implicitly_wait(2)

    login_error_message = driver.find_element(By.CLASS_NAME, "form__message")
    assert "Invalid username or password" in login_error_message.text


finally:

    driver.quit()
