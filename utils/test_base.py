import pytest


class TestBase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.driver = browser
        yield
        self.driver.quit()
