import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

print("Running conftest first")

@pytest.fixture(scope="session")
def driver_setup():
    global driver
    chrome_service = Service("/Users/viraj/Desktop/prepinsta/chromedriver")
    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": "/Users/viraj/Desktop/"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=chrome_service, options=options)
    driver.maximize_window()

    yield driver
    driver.close()
    driver.quit()

