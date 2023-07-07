import pytest

from utils.file_utils import get_test_data
from utils.test_base import TestBase
from pages.login_page import LoginPage


class TestResetPassword(TestBase):

    @pytest.fixture(autouse=True)
    def setup_login(self):
        self.login_page = LoginPage(self.driver)
        self.valid_credential = get_test_data('valid_credentials.json')[0]

    def test_password_reset_without_login_attempt(self):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.login_page.enter_username(self.valid_credential['username'])
        self.login_page.click_continue()
        # Go to reset password page
        self.reset_password_page = self.login_page.click_reset_password()
        # Fill email and reset password
        self.confirmation_page = self.reset_password_page.reset_password(self.valid_credential['email'])
        # Assert that we have correct message on confirmation page
        assert self.confirmation_page.get_message_title() == 'Email Sent'
        assert self.confirmation_page.get_message_body() == 'Check your email and open the link we sent to continue'

    def test_password_reset_with_return(self):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.login_page.login(self.valid_credential['username'], self.valid_credential['password'])
        # Go to reset password page
        self.reset_password_page = self.login_page.click_reset_password()
        # Fill email and reset password
        self.confirmation_page = self.reset_password_page.reset_password(self.valid_credential['email'])
        # Assert that reset was successful
        assert self.confirmation_page.get_message_title() == 'Email Sent'
        # Close confirmation page
        self.confirmation_page.click_close()
        # Check if we are on login page, second step
        assert self.login_page.is_sign_in_button_disabled()

    def test_cancellation_of_password_reset(self):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.login_page.enter_username(self.valid_credential['username'])
        self.login_page.click_continue()
        # Go to reset password page
        self.reset_password_page = self.login_page.click_reset_password()
        # Fill email and reset password
        self.reset_password_page.back_to_login_page()
        # Assert that we are back on login page step 2
        assert self.login_page.is_sign_in_button_disabled()

    @pytest.mark.parametrize("emails", get_test_data('invalid_emails.json'))
    def test_password_reset_without_login_attempt(self, emails):
        # Open the web page
        self.login_page.goto()
        # Perform login
        self.login_page.enter_username(self.valid_credential['username'])
        self.login_page.click_continue()
        # Go to reset password page
        self.reset_password_page = self.login_page.click_reset_password()
        # Fill email and reset password
        self.reset_password_page.reset_password(emails['email'])
        # Assert that we got error message
        assert self.reset_password_page.get_last_error_message() == 'Wrong argument (email) value. Possible []!'
