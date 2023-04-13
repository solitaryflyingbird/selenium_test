from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time, os, random, requests


options = Options()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-blink-features=AutomationControlled")
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
# Setting the driver path and requesting a page 
 


capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:chromeOptions'] = options.to_capabilities()
driver = webdriver.Chrome(executable_path='path/to/chromedriver', desired_capabilities=capabilities, options = options)
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

driver.get("https://gall.dcinside.com/mgallery/board/write/?id=covidvaccine")

# Create an ActionChains object
actions = ActionChains(driver)

# Move the mouse to a specific element on the page
element = driver.find_element(By.XPATH, '//html')
actions.move_to_element(element).perform()

# Get the current mouse position and print it to the console
x = driver.execute_script('return window.pageXOffset + arguments[0].getBoundingClientRect().left', element)
y = driver.execute_script('return window.pageYOffset + arguments[0].getBoundingClientRect().top', element)
print('Mouse position: ({}, {})'.format(x, y))

# Close the browser
driver.quit()
