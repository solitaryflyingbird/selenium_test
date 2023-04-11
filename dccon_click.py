from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
# Replace with the path to your browser driver


    dccon = driver.find_element(By.CLASS_NAME,"tx_dccon")
    dccon.click()
    time.sleep(3)