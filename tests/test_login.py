import pytest

from utils.file_utils import get_test_data
from utils.test_base import TestBase
from pages.login_page import LoginPage


class TestLogin(TestBase):

    @pytest.fixture(autouse=True)
    def setup_login(self):
        self.login_page = LoginPage(self.driver)
        self.valid_credential = get_test_data('valid_credentials.json')[0]

    @pytest.mark.parametrize("credentials", get_test_data('valid_credentials.json'))
    def test_login(self, credentials):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.main_page = self.login_page.login(credentials['username'], credentials['password'])
        # Assert that login was successful, and we are on main page
        assert self.main_page.is_page_loaded()

    @pytest.mark.parametrize("credentials", get_test_data('invalid_credentials.json'))
    def test_invalid_credentials(self, credentials):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.login_page.login(credentials['username'], credentials['password'])
        # Assert that login was unsuccessful and got error message
        assert self.login_page.get_last_error_message() == "Incorrect username/password. Please try again!"

    def test_empty_username(self):
        # Open the web page
        self.login_page.goto()
        # Lef login empty
        self.login_page.enter_username("")
        # Assert that Continue button is disabled
        assert self.login_page.is_continue_button_disabled()

    def test_empty_password(self):
        # Open the web page
        self.login_page.goto()
        # Fill login
        self.login_page.enter_username(self.valid_credential['username'])
        self.login_page.click_continue()
        # Left password empty
        self.login_page.enter_password("")
        # Assert that Sign in button is disabled
        assert self.login_page.is_sign_in_button_disabled()

    def test_change_username(self):
        # Open the web page
        self.login_page.goto()
        # Fill login and continue
        self.login_page.enter_username(self.valid_credential['username'])
        self.login_page.click_continue()
        self.login_page.enter_password(self.valid_credential['password'])
        # click on change username button
        self.login_page.click_change_username()
        self.login_page.wait_to_load()
        # check if we are back to step 1
        assert self.login_page.is_continue_button_disabled()
