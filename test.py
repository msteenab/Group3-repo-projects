from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)  # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://cbarnc.github.io/Group3-repo-projects/")

# maximizing window
driver.maximize_window()

# click a button
# driver.find_element(By.XPATH, "/html/body/div/aside/section[2]/form/fieldset/button").click()


# find element by tag name
h2 = driver.find_element(By.TAG_NAME, "h2")
print(h2.text)

h3 = driver.find_element(By.TAG_NAME, "h3")
print(h3.text)

p = driver.find_element(By.TAG_NAME, "p")
print(p.text)

# time.sleep(2)

# typing in comment box
#driver.find_element(By.ID,"comments").send_keys("Love this Place!")

# returning title of page
#print("Page title is: ")
#print(driver.title)

# time before window closes
# time.sleep(13)

# Close Edge browser
driver.quit()
