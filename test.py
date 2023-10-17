from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/")

# click a button
button = driver.button = driver.find_element(By.CLASS_NAME, "my-button-class")
print(button)
