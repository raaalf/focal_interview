from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.specific_element_locator = (By.ID, "i-am-on-main-page")

    def is_page_loaded(self):
        return self.driver.find_element(*self.specific_element_locator).is_displayed()
