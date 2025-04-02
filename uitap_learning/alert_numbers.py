from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_service = Service()
driver = webdriver.Chrome()
waiter5 = WebDriverWait(driver, 5)

driver.get("http://localhost:9999")

sleep(3)

waiter5.until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.send_keys("45")

sleep(3)

alert.accept()

sleep(3)

waiter5.until(EC.alert_is_present())
alert.accept()

driver.quit()