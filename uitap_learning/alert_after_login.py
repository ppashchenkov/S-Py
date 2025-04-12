import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


# def test_alert_login():
driver = webdriver.Chrome()
waiter5 = WebDriverWait(driver, 15)
driver.get("https://www.saucedemo.com")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# waiter5.until(EC.alert_is_present())
# alert = driver.switch_to.alert
# print("ALERT = ", alert.text)
# alert.accept()

time.sleep(115)

# assert True

driver.quit()