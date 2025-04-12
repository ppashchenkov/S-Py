import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver


@pytest.fixture
def driver():
    option = Options()
    option.add_argument("--windows-size=1920,1080")
    option.add_argument("--headless=new")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--disable-gpu")
    option.add_argument("--sandbox")
    option.add_argument("--incognito")
    option.add_argument("--disable-cache")
    option.add_argument("--user-agent=\"useragent\"")
    # option.add_experimental_option("prefs", {"download.default.directoy = ....."})
    driver = webdriver.Chrome(options=option)
    yield driver
    driver.quit()