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



def login(ID, PW):

    URL = "https://msign.dcinside.com/login?r_url=https%3A%2F%2Fm.dcinside.com"
    driver.get(URL)
    driver.find_element("name", "code").send_keys(ID)
    driver.find_element("name", "password").send_keys(PW)
    time.sleep(1)
    driver.find_element(By.ID, "loginAction").click()
    time.sleep(1)

def attack_start(URL):
    try:
        driver.get(URL)
        time.sleep(1)
        subject_input = driver.find_element("name", "subject")
        text_box = driver.find_element(By.ID, "textBox")
        subject_input.send_keys("실험중입니다.")
        text_box.send_keys("소농민.")
        button = driver.find_element(By.CLASS_NAME, "btn-temp")
        button.click()
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


ID_list = ["gltptdi5aoi0", "gltptdi5aoi1"]



for i in range(len(ID_list)):
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    driver.implicitly_wait(1) 
    login(ID_list[i], "emtksahdqt1@")
    URL = "https://m.dcinside.com/write/football_new8"
    attack_start(URL)
    time.sleep(10)
