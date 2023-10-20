import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/")

# maximizing window
driver.maximize_window()

# typing in comment box
driver.find_element(By.ID,"comments").send_keys("Love this Place!")

# click a button
button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()
time.sleep(5)

# returning title of page
print("Page title is: ")
print(driver.title)

# time before window closes
time.sleep(7)

# Close Edge browser
driver.quit()
