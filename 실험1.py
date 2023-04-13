from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time, os, random, requests


def move_to_element_smoothly(driver, element, duration=1, steps=50):
    action_chains = ActionChains(driver)
    start_x, start_y = (0,0)
    current_x, current_y = start_x, start_y
    target_x, target_y = start_x + element.size['width'] // 2, start_y + element.size['height'] // 2

    for step in range(1, steps + 1):
        t = step / steps
        next_x = start_x + (target_x - start_x) * t
        next_y = start_y + (target_y - start_y) * t
        action_chains.move_by_offset(next_x - current_x, next_y - current_y)
        current_x, current_y = next_x, next_y
        time.sleep(duration / steps)

    action_chains.perform()



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


URL = "https://gall.dcinside.com/board/write/?id=football_new8"
driver.get(URL)



try:
    time.sleep(1)
    nickname_input = driver.find_element("name", "name")
    password_input = driver.find_element("name", "password")
    subject_input = driver.find_element("name", "subject")
    nickname_input.clear()
    password_input.clear()
    nickname_input.send_keys('ㅇㅇ')
    password_input.send_keys('1111')
    subject_input.send_keys("소농민.")

    actions = ActionChains(driver)
    iframe = driver.find_element("name", "tx_canvas_wysiwyg")
    actions.move_to_element(iframe).perform()

    driver.switch_to.frame(iframe)
    
    
    main_input = driver.find_element(By.CLASS_NAME, "tx-content-container")



    
    move_to_element_smoothly(driver, password_input, duration=1, steps=50)
    



    main_input.click()
    time.sleep(0.1)
    
    
    main_input.send_keys("x")
    driver.switch_to.default_content()

    
    time.sleep(0.1)

    




    button = driver.find_element(By.CSS_SELECTOR, '.btn_blue.btn_svc.write')

    actions.move_to_element(button).perform()


    button.click()
    print(111)
    time.sleep(1)
    #nickname_input.send_keys('ㅇㅇ')
    #password_input.send_keys('1111')
    time.sleep(1)
    x = driver.window_handles


    time.sleep(1)

    print(x)
    print("click")
    time.sleep(1227)



finally:
    print("quit")
    # Close the browser (you can use time.sleep() before this line if you want to keep the browser open for some time)
    driver.quit()