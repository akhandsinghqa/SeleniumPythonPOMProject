from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):

    def test_home_page_title(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homepage.navigate_to_global_home()
        title = homepage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homepage.get_header_value()
        assert TestData.HOME_PAGE_HEADER in header

    def test_home_page_setting_icon(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        is_setting_icon = homepage.is_setting_icon_exist()
        assert is_setting_icon

    def test_home_page_account_name(self):
        self.loginpage=LoginPage(self.driver)
        homepage = self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = homepage.get_account_name_value()
        assert account_name.strip() == TestData.HOME_PAGE_ACCOUNT_NAME.strip()
