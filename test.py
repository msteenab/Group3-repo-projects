from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/")

# click a button
button = driver.find_element(By.CLASS_NAME, "my-button-class")
button.click()

# locate elements
element_by_id = driver.find_element(By.ID, "element_id")


