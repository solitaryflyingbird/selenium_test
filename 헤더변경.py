from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['goog:chromeOptions'] = options.to_capabilities()
driver = webdriver.Chrome(executable_path='path/to/chromedriver', desired_capabilities=capabilities)


attack = "https://gall.dcinside.com/board/write/?id=football_new8"

# 셀레니움 와이어로 헤더 변경
def interceptor(request):
    del request.headers['Referer']
    del request.headers['User-Agent']
    request.headers['Referer'] = 'https://gall.dcinside.com/board/write/?id=football_new8'
    request.headers['User-Agent'] = "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
driver.request_interceptor = interceptor

driver.get(attack)


def test(arr):
    for i in arr:
        try:
            x = driver.find_elements(By.ID, i)
            x.click()
            
        except:
            print("error", i)


try:

    time.sleep(1)
    nickname_input = driver.find_element("name", "name")
    password_input = driver.find_element("name", "password")
    subject_input = driver.find_element("name", "subject")
    nickname_input.send_keys('YourNickname')
    password_input.send_keys('YourPassword')
    subject_input.send_keys("실험중입니다.")

    
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