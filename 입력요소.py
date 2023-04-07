from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
# Replace with the path to your browser driver

driver = webdriver.Chrome(executable_path='path/to/chromedriver')
attack = 'https://gall.dcinside.com/mgallery/board/write/?id=whitehouse'
driver.get(attack)

elements = driver.find_elements(By.XPATH, "//*")
for element in elements:
    try:
        element.send_keys("ddd")
        print(element.text)
    except:
        try:
            element[1].send_keys("ddd")
            print(element.text)
        except:
            pass

print("end")
time.sleep(10)