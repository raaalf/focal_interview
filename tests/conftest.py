import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pytest_html


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser option: chrome, firefox, edge, or safari"
    )


@pytest.fixture(scope='function', autouse=True)
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        raise Exception(f'{browser} is not a supported browser')
    request.node._driver = driver
    yield driver
    driver.quit()


# @pytest.hookimpl(hookwrapper=True)
def pytest_exception_interact(node, call, report):
    if report.failed:
        if hasattr(node, '_driver'):
            web_driver = node._driver
            # If your screenshots directory does not exist, create it
            image_encoded = web_driver.get_screenshot_as_base64()
            if hasattr(report, 'extra'):
                report.extra.append(pytest_html.extras.image(image_encoded, 'Screenshot of the failure'))
            else:
                report.extra = [pytest_html.extras.image(image_encoded, 'Screenshot of the failure')]
