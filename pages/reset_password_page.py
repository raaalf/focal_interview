from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.reset_confirmation_page import ResetConfirmationPage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input_locator = (By.ID, "password-reset-form-password")
        self.send_link_button_locator = (By.CSS_SELECTOR, "[data-testid='password-reset-submit-button']")
        self.back_button_locator = (By.CSS_SELECTOR, "button[type='button']")

    def wait_for_login_input(self):
        return self.wait_for(EC.visibility_of_element_located(self.email_input_locator))

    def enter_email(self, email):
        email_input = self.wait_for_login_input()
        email_input.clear()
        email_input.send_keys(email)

    def click_send_link(self):
        send_link_button = self.wait_for(EC.element_to_be_clickable(self.send_link_button_locator))
        send_link_button.click()

    def back_to_login_page(self):
        back_button = self.wait_for(EC.element_to_be_clickable(self.back_button_locator))
        back_button.click()
        self.wait_to_load()

    def reset_password(self, email):
        self.enter_email(email)
        self.click_send_link()
        self.wait_to_load()
        return ResetConfirmationPage(self.driver)
