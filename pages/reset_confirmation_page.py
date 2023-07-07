from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ResetConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.message_title_locator = (By.CSS_SELECTOR, "h6[class*='MuiTypography-h6']")
        self.message_body_locator = (By.CSS_SELECTOR, "span[class*='MuiTypography-caption']")
        self.close_button_locator = (By.XPATH, '//button[normalize-space(text())="Close"]')

    def get_message_title(self):
        return self.driver.find_element(*self.message_title_locator).text

    def get_message_body(self):
        return self.driver.find_element(*self.message_body_locator).text

    def click_close(self):
        close_button = self.wait_for(EC.element_to_be_clickable(self.close_button_locator))
        close_button.click()
