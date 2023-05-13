import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_service=Service("/Users/viraj/Desktop/prepinsta/chromedriver")
driver= webdriver.Chrome(service=chrome_service)
driver.get("https://www.saucedemo.com/")

#ID,NAME,class_name,link_text,xpath,css_selector,tag_name,# writing xpath //tagname[@attribute='value']


username=driver.find_element(By.ID,"user-name")
#enter username
username.send_keys("standard_user")
password=driver.find_element(By.NAME,"password")
#enter assword
password.send_keys("secret_sauce")
login_btn=driver.find_element(By.XPATH,"//input[@id='login-button']")
#click on login button
login_btn.click()
cart=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
#check if cart icon is displayed after login
if cart.is_displayed():
    print("user logged in")
else:
    print("something went wrong")

add_bag_to_cart=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
#add bag to cart
add_bag_to_cart.click()
#goto cart
cart.click()
#check if bag is present
bag_check=driver.find_element(By.CLASS_NAME,"inventory_item_name")
if bag_check.is_displayed():
    print(bag_check.text)
else:
    print("item not in cart")

#click on checkout
driver.find_element(By.NAME,"checkout").click()

#populate first name
first_name=driver.find_element(By.XPATH,"//input[@data-test='firstName']")
first_name.send_keys("Viraj")
#populate last name
last_name=driver.find_element(By.ID,"last-name")
last_name.send_keys("Nayak")
#populate pincode name
pin_code=driver.find_element(By.NAME,"postalCode")
pin_code.send_keys("560103")

#click continue
continue_btn=driver.find_element(By.ID,"continue")
continue_btn.click()

#check if overview page
overview_title=driver.find_element(By.CLASS_NAME,"title")
compare="OVERVIEW"
if compare in overview_title.text:
    print(overview_title.text)
else:
    print("wrong page")

#click finish
finish_btn=driver.find_element(By.ID,"finish")
finish_btn.click()

#print final message
thank_you=driver.find_element(By.XPATH,"//h2[@class='complete-header']")

print(thank_you.text)
time.sleep(5)
driver.close()