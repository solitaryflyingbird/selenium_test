from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time, os, random, requests

options = Options()

rand_user_folder = 1
usercookiedir = os.path.abspath(f"./cookies/{rand_user_folder}")
if os.path.exists(usercookiedir) == False:
    os.mkdir(usercookiedir)

options.add_argument(f"--user-data-dir={usercookiedir}")
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
print(driver.get_cookies())






attack = "https://gall.dcinside.com/board/write/?id=football_new8"
driver.get(attack)



try:
    time.sleep(1)
    nickname_input = driver.find_element("name", "name")
    password_input = driver.find_element("name", "password")
    subject_input = driver.find_element("name", "subject")
    nickname_input.clear()
    password_input.clear()
    nickname_input.send_keys('ㅇㅇ')
    password_input.send_keys('1111')
    subject_input.send_keys("실험중입니다.")

    main_window = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            driver.close()
    driver.switch_to.window(main_window)

    
    iframe = driver.find_element("name", "tx_canvas_wysiwyg")
    driver.switch_to.frame(iframe)
    main_input = driver.find_element(By.CLASS_NAME, "tx-content-container")
    main_input.send_keys("x")
    driver.switch_to.default_content()


    button = driver.find_element(By.CSS_SELECTOR, '.btn_blue.btn_svc.write')
    button.click()
    print("click")
    time.sleep(1227)



finally:
    print("quit")
    # Close the browser (you can use time.sleep() before this line if you want to keep the browser open for some time)
    driver.quit()