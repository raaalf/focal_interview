from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.error_notification_locator = (By.ID, "notistack-snackbar")

    def wait_to_load(self, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def wait_for(self, method, timeout=15):
        return WebDriverWait(self.driver, timeout).until(method)

    def get_error_messages(self):
        self.wait_for(EC.visibility_of_element_located(self.error_notification_locator))
        error_prompts = self.driver.find_elements(*self.error_notification_locator)
        return [error_prompt.text for error_prompt in error_prompts]

    def get_last_error_message(self):
        self.wait_for(EC.visibility_of_element_located(self.error_notification_locator))
        return self.driver.find_elements(*self.error_notification_locator)[-1].text
