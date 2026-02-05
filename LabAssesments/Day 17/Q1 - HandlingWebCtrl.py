from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()

driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")
time.sleep(2)

driver.find_element(By.ID, "input-firstname").send_keys("Rahul")
driver.find_element(By.ID, "input-lastname").send_keys("Tester")

email = f"rahul_{int(time.time())}@test.com"
driver.find_element(By.ID, "input-email").send_keys(email)

driver.find_element(By.ID, "input-telephone").send_keys("9876543210")

password = "Test@1234"
driver.find_element(By.ID, "input-password").send_keys(password)
driver.find_element(By.ID, "input-confirm").send_keys(password)

driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

driver.find_element(By.NAME, "agree").click()

driver.find_element(By.CSS_SELECTOR, "input.btn-primary").click()
time.sleep(2)

heading = driver.find_element(By.TAG_NAME, "h1").text
print("Result:", heading)

driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "dropdown"))
dropdown.select_by_visible_text("Option 2")
print("Dropdown option selected")

driver.quit()
