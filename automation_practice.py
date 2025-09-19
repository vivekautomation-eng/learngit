import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys("Vivek")
driver.find_element(By.ID,"email").send_keys("vt1@deloitte.com")
driver.find_element(By.ID,"phone").send_keys("9524282484")
ele=driver.find_element(By.ID,"colors")
driver.execute_script("arguments[0].scrollIntoView(false);",ele)
time.sleep(5)
drop=driver.find_element(By.ID,"country")
sele=Select(drop)
sele.select_by_value("india")
time.sleep(5)
