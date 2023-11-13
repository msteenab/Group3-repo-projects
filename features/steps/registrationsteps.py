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

    context.webdriver.get('https://cbarnc.github.io/Group3-repo-projects/signIn.html')







