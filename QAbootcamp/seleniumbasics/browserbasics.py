import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_service=Service("/Users/viraj/Desktop/prepinsta/chromedriver")
driver= webdriver.Chrome(service=chrome_service)
driver.get("https://demoqa.com/")
print(driver.title)
print(driver.current_url)
driver.refresh()
driver.minimize_window()
driver.maximize_window()
driver.get("https://demoqa.com/elements")
driver.back()
time.sleep(5)
print(driver.current_url)
time.sleep(5)
driver.forward()
time.sleep(5)
print(driver.current_url)
driver.close()