from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert = driver.switch_to.alert
print("Alert message:", alert.text)
alert.accept()
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
confirm_alert = driver.switch_to.alert
print("Confirm message:", confirm_alert.text)
confirm_alert.dismiss()
time.sleep(1)

driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
prompt_alert = driver.switch_to.alert
prompt_alert.send_keys("Rahul")
prompt_alert.accept()
time.sleep(1)

result = driver.find_element(By.ID, "result").text
print("Result displayed:", result)

driver.quit()
