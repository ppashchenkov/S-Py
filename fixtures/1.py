import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def my_site(driver):
    driver.get("http://localhost:5000")
    return driver

def test_our_task(my_site: WebDriver):
    my_site.find_element(By.ID, "input").send_keys("test")







# Пример использования yield
def generator():
    for i in [1, 2, 3, 4]:
        yield i
        print("return control")

generator = generator()
print(next(generator))
print(next(generator))
print(next(generator))