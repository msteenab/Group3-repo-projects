from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('the user is on the login page')
def loginPage(context):
    context.driver = webdriver.Chrome()

    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/signIn.html")

@when('they enter valid username and password')
def userPass(context):
    username_input = context.driver.find_element_by_id('username')