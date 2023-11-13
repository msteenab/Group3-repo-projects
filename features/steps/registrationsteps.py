from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('the user is on the registration page')
def registrationPage(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://your-website-url/register')