from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True) # Keeps the webpage from automatically closing
driver = webdriver.Edge(options=options)
driver.get("https://3osmic.github.io/Group3-repo-projects/")
