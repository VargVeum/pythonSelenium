import time

from pages.login_page import TestPage
from selenium import webdriver
import pytest
from helpers.credentials import UserCredentials

@pytest.mark.login_negative_email
def test_login_negative_email():
    browser = webdriver.Firefox()

    # Our test
    test_page = TestPage(driver=browser)
    test_page.openPage()
    test_page.fill_email_input('testBLABLABLA')
    test_page.fill_password_input(UserCredentials.PASSWORD)
    test_page.is_submit_button_disabled()
    print('Test passed!')

    time.sleep(2)
    browser.close()

@pytest.mark.login_negative_password
def test_login_negative_password():
    driver = webdriver.Firefox()

    # Our test
    test_page = TestPage(driver=driver)
    test_page.openPage()
    test_page.fill_email_input(UserCredentials.EMAIL)
    test_page.fill_password_input('testBLABLABLA')
    test_page.click_submit_button()
    test_page.check_error_text()

    time.sleep(2)
    driver.close()

@pytest.mark.login_empty_data
def test_login_empty_data():
    driver = webdriver.Firefox()

    # Our test
    test_page = TestPage(driver=driver)
    test_page.openPage()
    test_page.fill_email_input('')
    test_page.fill_password_input('')
    test_page.is_submit_button_disabled()

    time.sleep(2)
    driver.close()

@pytest.mark.login_valid_credentials
def test_login_valid_credentials():
    driver = webdriver.Firefox()

    # Our test
    test_page = TestPage(driver=driver)
    test_page.openPage()
    test_page.fill_email_input(UserCredentials.EMAIL)
    test_page.fill_password_input(UserCredentials.PASSWORD)
    test_page.click_submit_button()
    test_page.check_load_management_link()

    time.sleep(2)
    driver.close()

