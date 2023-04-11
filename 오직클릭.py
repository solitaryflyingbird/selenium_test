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

driver.implicitly_wait(1) 
actions = ActionChains(driver)

URL = "https://gall.dcinside.com/board/write/?id=football_new8"
driver.get(URL)



try:
    time.sleep(21)

    button = driver.find_element(By.CSS_SELECTOR, '.btn_blue.btn_svc.write')
    button.click()

    time.sleep(1)
    #nickname_input.send_keys('ㅇㅇ')
    #password_input.send_keys('1111')
    time.sleep(1)
    x = driver.window_handles
    print(x)


    print("click")
    time.sleep(1227)



finally:
    print("quit")
    # Close the browser (you can use time.sleep() before this line if you want to keep the browser open for some time)
    driver.quit()