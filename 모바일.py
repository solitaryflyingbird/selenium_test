from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui
import time, os, random, requests
mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)



def attack_start():
    try:
        URL = "https://m.dcinside.com/write/football_new8"
        driver.get(URL)
        time.sleep(1)
        nickname_input = driver.find_element("name", "name")
        password_input = driver.find_element("name", "password")
        subject_input = driver.find_element("name", "subject")
        text_box = driver.find_element(By.ID, "textBox")

        nickname_input.clear()
        password_input.clear()
        nickname_input.send_keys('ㅇㅇ')
        password_input.send_keys('1111')
        subject_input.send_keys("실험중입니다.")
        text_box.send_keys("소농민.")

        button = driver.find_element(By.CLASS_NAME, "btn-temp")
        button.click()
        #driver.find_element(By.CLASS_NAME, "btn-temp").click()

    finally:
        print("quit")


options = Options()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-blink-features=AutomationControlled")
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
options.add_experimental_option("mobileEmulation", mobile_emulation)
# Setting the driver path and requesting a page 
W=360
H=640
options.add_argument(f"--window-size={W},{H}")
 


capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:chromeOptions'] = options.to_capabilities()
driver = webdriver.Chrome(executable_path='path/to/chromedriver', desired_capabilities=capabilities, options = options)
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

driver.implicitly_wait(1) 



attack_start()

time.sleep(5111)



