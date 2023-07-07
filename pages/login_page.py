from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input_locator = (By.ID, "realm-form-username")
        self.continue_button_locator = (By.CSS_SELECTOR, "[data-testid='realm-submit-button']")
        self.password_input_locator = (By.ID, "login-form-password")
        self.sign_in_button_locator = (By.CSS_SELECTOR, "[data-testid='login-submit-button']")
        self.remember_me_checkbox_locator = (By.CSS_SELECTOR, "input[type='checkbox']")
        self.reset_password_button_locator = (By.XPATH, '//button[normalize-space(text())="Forgot your password?"]')
        self.change_username_button_locator = (By.XPATH, '//button[normalize-space(text())="Change username"]')

    def goto(self):
        self.driver.get("https://action.staging.focal.dev/")
        self.wait_for_login_input()

    def wait_for_login_input(self):
        return self.wait_for(EC.visibility_of_element_located(self.username_input_locator))

    def enter_username(self, username):
        username_input = self.wait_for_login_input()
        username_input.clear()
        username_input.send_keys(username)

    def is_continue_button_disabled(self):
        return self.driver.find_element(*self.continue_button_locator).get_attribute('disabled') is not None

    def click_continue(self):
        continue_button = self.wait_for(EC.element_to_be_clickable(self.continue_button_locator))
        continue_button.click()

    def enter_password(self, password):
        password_input = self.wait_for(EC.visibility_of_element_located(self.password_input_locator))
        password_input.clear()
        password_input.send_keys(password)

    def is_sign_in_button_disabled(self):
        return self.driver.find_element(*self.sign_in_button_locator).get_attribute('disabled') is not None

    def click_sign_in(self):
        sign_in_button = self.wait_for(EC.element_to_be_clickable(self.sign_in_button_locator))
        sign_in_button.click()

    def select_remember_me(self):
        self.driver.find_element(self.remember_me_checkbox_locator).click()

    def click_change_username(self):
        change_username_button = self.wait_for(EC.element_to_be_clickable(self.change_username_button_locator))
        change_username_button.click()

    def click_reset_password(self):
        reset_password_button = self.wait_for(EC.element_to_be_clickable(self.reset_password_button_locator))
        reset_password_button.click()
        self.wait_to_load()
        return ResetPasswordPage(self.driver)

    def login(self, username, password):
        self.enter_username(username)
        self.click_continue()
        self.enter_password(password)
        self.click_sign_in()
        self.wait_to_load()
        return MainPage(self.driver)
