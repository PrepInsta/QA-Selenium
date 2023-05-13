import time
import pytest

from pages.login import Login


@pytest.fixture
def login_page(driver_setup):
    driver_setup.get("https://www.saucedemo.com/")
    login_obj = Login(driver_setup)
    return login_obj


@pytest.mark.loginsuccess
def test_login(driver_setup, login_page):
    login_page.login("standard_user", "secret_sauce")


@pytest.mark.loginfailed
def test_login_failed(driver_setup, login_page):
    login_page.login("standard_user", "wrong_password")
    assert False

@pytest.mark.errormsg
@pytest.mark.parametrize("username,password,error", [
    ("standard_user", "wrongpasword", "Epic sadface: Username and password do not match any user in this service"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")])
def test_login_error(driver_setup, login_page,username,password,error):
    login_page.login(username, password)
    assert login_page.error_msg() == error
    print(login_page.error_msg())

