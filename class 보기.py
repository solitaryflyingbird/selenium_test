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
iframe = driver.find_element(By.CSS_SELECTOR,'iframe')
driver.switch_to.frame(iframe)

ttt = driver.find_element(By.CLASS_NAME, "tx-content-container")

ttt.send_keys("ddd")