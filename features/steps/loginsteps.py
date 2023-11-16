from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('the user is on the login page')
def login_page(context):
    context.driver = webdriver.Chrome()

    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")


@when('they enter valid username and password')
def user_pass(context):
    username_input = context.driver.find_elements(By.ID, 'username')
    password_input = context.driver.find_elements(By.ID, 'password')

    username_input.send_keys('test_user123')
    password_input.send_keys('password123')


@when('click the "Login" button')
def click_login(context):
    login_button = context.driver.find_elements(By.ID, 'login_button')
    login_button.click()


@then('they should be redirected to the dashboard')
def redirect(context):
    current_url = context.driver.current_url
    assert current_url == 'https://cbarnc.github.io/Group3-repo-projects/'
