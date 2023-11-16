from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image


@given(u'user on contact us section')
def contactUs(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://cbarnc.github.io/Group3-repo-projects/')


@when(u'the selects the Yes Radio button')
def selectButton(context):
    radio_list = context.driver.find_elements(By.NAME, "T3C_member")
    for radioButton in radio_list:
        radioButton_t = radioButton.get_attribute("value")
        if radioButton_t == "yes":
            radioButton.click()
        time.sleep(2)


@then(u'the user should see radio button yes selected')
def radioStatus(context):
    url = "https://cbarnc.github.io/Group3-repo-projects/"
    context.driver.get(url)
    screenshot = Image.open("screenshot-2.png")
    screenshot.show()



