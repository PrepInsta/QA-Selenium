import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Navigation:

    def __init__(self):
        chrome_service = Service("/Users/viraj/Desktop/prepinsta/chromedriver")
        options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": "/Users/viraj/Desktop/download"}
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(service=chrome_service, options=options)

    def get_driver(self):
        return self.driver

    def goto_toolsqa_page(self, page_name):
        url = "https://demoqa.com/"
        self.driver.get(url + page_name)

    def get_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.location_once_scrolled_into_view
        return element
