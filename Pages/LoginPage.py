from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    # By locators or Page Elements
    EMAIL = (By.ID, "username")
    EMAIL_SUBMIT_BUTTON = (By.XPATH, ".//button[@data-test-id='email-submit-button']")
    PASSWORD_BUTTON = (By.ID, "passwordBtn")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    ERROR_MESSAGE = (By.XPATH, ".//div[@data-test-id='error-alert-PASSWORD_DEPRECATED']")

    # Constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    # Page actions

    # This is used to get the page title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # This is to check is sign up link enabled
    def is_signup_link_enabled(self):
        return self.is_visible(self.EMAIL_SUBMIT_BUTTON)

    # This is used login to app
    def do_login(self, username, password):
        self.do_send_key(self.EMAIL, username)
        self.do_click(self.EMAIL_SUBMIT_BUTTON)
        self.do_click(self.PASSWORD_BUTTON)
        self.do_send_key(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    # This is used to get the login warning message
    def get_login_warning_message(self):
        return str(self.get_element_text(self.ERROR_MESSAGE))
