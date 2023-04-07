from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver')
attack = 'https://gall.dcinside.com/mgallery/board/write/?id=whitehouse'
driver.get(attack)

element = driver.find_element_by_xpath("//button[@id='example-button']")

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
time.sleep(10)