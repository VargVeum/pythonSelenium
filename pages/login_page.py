from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support.wait import WebDriverWait

class TestPageLocators:
    email_input = By.CSS_SELECTOR, 'input[type="email"]',
    password_input = By.CSS_SELECTOR, 'input[type="password"]',
    submit_button = By.CSS_SELECTOR, 'button[type="submit"]',
    error = By.CSS_SELECTOR, 'mat-error[class="mat-error"]',
    load_management_link = By.CSS_SELECTOR, 'a[href="/tms/load-management"]'


class TestPage:

    def check_load_management_link(self):
        wait = WebDriverWait(self.driver, 10)
        element_locator = (TestPageLocators.load_management_link)
        element = wait.until(EC.visibility_of_element_located(element_locator))
        return None

    def check_error_text(self):
        wait = WebDriverWait(self.driver, 10)
        element_locator = (TestPageLocators.error)
        element = wait.until(EC.visibility_of_element_located(element_locator))
        return None


    def fill_email_input(self, text):
        email_input = self.driver.find_element(*TestPageLocators.email_input)
        email_input.clear()
        email_input.send_keys(text)
        return None

    def fill_password_input(self, text):
        password_input = self.driver.find_element(*TestPageLocators.password_input)
        password_input.clear()
        password_input.send_keys(text)
        return None

    def click_submit_button(self):
        submit_button = self.driver.find_element(*TestPageLocators.submit_button)
        submit_button.click()
        return None

    def is_submit_button_disabled(self):
        submit_button = self.driver.find_element(*TestPageLocators.submit_button)
        return submit_button.is_enabled()

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-carrier-tms.zuumapp.com/auth/login"

    def openPage(self):
        self.driver.get(self.url)
