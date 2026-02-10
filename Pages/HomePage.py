from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    HEADER = (By.CSS_SELECTOR, "[data-test-id='todays-plan-widget']")
    ACCOUNT_NAME = (By.ID, "hs-global-toolbar-accounts")
    SETTING_ICON = (By.CSS_SELECTOR, "[data-test-id='hs-global-toolbar-settings-list-item']")
    HOME_ICON = (By.CSS_SELECTOR, "#global-home")

    # Constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_setting_icon_exist(self):
        return self.is_visible(self.SETTING_ICON)

    def get_header_value(self):
        self.do_click(self.HOME_ICON)
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)
        return "Header not visible. Please check again."

    def get_account_name_value(self):
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
        return "Account Name is not visible."
