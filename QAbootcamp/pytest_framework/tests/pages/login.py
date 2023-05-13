import time

from selenium.webdriver.common.by import By


class Login:

    username = (By.ID,"user-name")
    password = (By.ID,"password")
    login_btn = (By.ID,"login-button")
    error = (By.XPATH,"//h3[@data-test='error']")

    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        username_ele = self.driver.find_element(*self.username)
        username_ele.send_keys(username)

    def enter_password(self,password):
        password_ele = self.driver.find_element(*self.password)
        password_ele.send_keys(password)

    def click_login(self):
        login_ele= self.driver.find_element(*self.login_btn)
        login_ele.click()

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(3)

    def error_msg(self):
        error_ele = self.driver.find_element(*self.error)
        return error_ele.text
