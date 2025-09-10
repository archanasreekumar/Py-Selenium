from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page?utm_source=chatgpt.com")

drop_down = Select(driver.find_element(By.ID, "mySelect"))
drop_down.select_by_value("50%")
time.sleep(3)
drop_down.select_by_visible_text("Set to 75%")
time.sleep(3)
drop_down.select_by_index(3)
time.sleep(3)
driver.quit()

