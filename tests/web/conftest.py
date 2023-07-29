import os
import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from helper.get_env_path import get_personal_env_path
from helper.attach_helpers import add_html, add_screenshot, add_video, add_logs
from dotenv import load_dotenv

# TODO: fully change conftest


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Browser for test',
        choices=['firefox', 'chrome'],
        default='chrome'
    )
    parser.addoption(
        '--browser_version',
        help='Version of browser',
        choices=['100.0'],
        default='100.0'
    )


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    options = Options()

    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    load_dotenv(get_personal_env_path())
    login = os.getenv('SELENOID_LOGIN')
    password = os.getenv('SELENOID_PASSWORD')

    browser.config.driver = webdriver.Remote(f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
                                             options=options)

    browser.config.base_url = 'https://www.last.fm'
    size = request.param
    browser.driver.set_window_size(size[0], size[1])

    yield browser

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
    add_video(browser)

    browser.quit()

