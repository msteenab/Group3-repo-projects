from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('the user is on the restaurant\'s homepage')
def homePage(context):
    context.driver = webdriver.Chrome()

    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/")


@when('they click on the "Menu" section')
def openMenu(context):
    context.driver.get("https://cbarnc.github.io/Group3-repo-projects/menu.html")


@then('they should see a list of dishes and their prices')
def menuList(context):
    context.driver.find_elements(By.CLASS_NAME, 'menu')


@then(u'close browser')
def closeBrowser(context):
    context.driver.close()
