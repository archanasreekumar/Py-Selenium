import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.python.org")
# print the title of page
print(driver.title)

# Sleep to keep the browser open for 30sec


# Using search bar
search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
search_bar = driver.find_element(By.NAME, "q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
# time.sleep(30)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "content")))

# after submitting search check current URL
print(driver.current_url)

driver.close()
