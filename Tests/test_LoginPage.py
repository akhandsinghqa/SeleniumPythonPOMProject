from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):

    def setup_method(self):
        """Initializes the LoginPage once for all tests in this class."""
        self.login_page = LoginPage(self.driver)

    def test_signup_link_visible(self):
        assert self.login_page.is_signup_link_enabled(),"Sign Up Link should be visible."

    def test_login_page_title(self):
        title = self.login_page.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE , f"Expected this : {TestData.LOGIN_PAGE_TITLE} but got {title}"

    def test_login(self):
        self.login_page.do_login(TestData.USER_NAME, TestData.PASSWORD)
        warning = self.login_page.get_login_warning_message()
        assert TestData.WARNING_MESSAGE in warning,"Warning message did not match."
