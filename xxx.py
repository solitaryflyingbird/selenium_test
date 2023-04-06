import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
service = Service(executable_path='path/to/chromedriver')
driver = webdriver.Chrome(service=service)

# Replace 'https://example.com' with the website you want to access
driver.get('https://gall.dcinside.com/board/lists?id=football_new8')

# Perform your actions on the website
# ...

# Keep the browser open for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()
