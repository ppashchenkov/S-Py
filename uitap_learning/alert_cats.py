from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_service = Service()
driver = webdriver.Chrome()
waiter5 = WebDriverWait(driver, 5)

driver.get("http://uitestingplayground.com/alerts")

alert_id = 'alertButton'
driver.find_element(By.ID, alert_id).click()
waiter5.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()
print("Click Alert")

confirm_id = 'confirmButton'
driver.find_element(By.ID, confirm_id).click()
waiter5.until(EC.alert_is_present())
alert.accept()
waiter5.until(EC.alert_is_present())
alert.accept()
print("Click Confirm")

prompt_id = 'promptButton'
driver.find_element(By.ID, prompt_id).click()
waiter5.until(EC.alert_is_present())
alert.send_keys("ddd")
alert.accept()

waiter5.until(EC.alert_is_present())
text = driver.switch_to.alert.text
print("Text = ", text)
sleep(2)
alert.accept()

driver.quit()