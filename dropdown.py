import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)
point=driver.find_element(By.ID,"PopUp")
driver.execute_script("arguments[0].scrollIntoView(true);",point)
time.sleep(3)
driver.find_element(By.ID,"alertBtn").click()
alert=driver.switch_to.alert
time.sleep(3)
alert.accept()
time.sleep(3)