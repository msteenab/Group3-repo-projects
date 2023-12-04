from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")

try:
    create_account_link = driver.find_element(By.ID, "linkCreateAccount")

    create_account_link.click()



    time.sleep(2)

    confirm_input = driver.find_element(By.ID, "signupUsername")
    username_input = driver.find_element(By.ID, "signupUsername").send_keys("short")
    driver.implicitly_wait(2)


    confirm_continue = driver.find_element(By.ID, "submit-button")

    if "Continue" in confirm_continue.text:
        print("Button found and text is 'Continue'")
    else:
        print("Button found, but text does not match 'Continue'")

    confirm_continue.click()


    time.sleep(2)
    driver.implicitly_wait(2)
    error_message = driver.find_element(By.ID, "form_input-1")
    assert "username must be at least 10 characters in length" in error_message.text
    driver.implicitly_wait(2)


    login_form = driver.find_element(By.ID, "linkLogin")
    login_form.submit()

    login_username = driver.find_element(By.ID, "login-username").send_keys("wrong")
    driver.implicitly_wait(2)
    time.sleep(2)
    login_confirm = driver.find_element(By.ID, "login-submit")
    login_confirm.click()

    login_error_message = driver.find_element(By.ID, "login-error")
    assert "Invalid username or password" in login_error_message.text


finally:
    print("Test Successful")
    driver.quit()
