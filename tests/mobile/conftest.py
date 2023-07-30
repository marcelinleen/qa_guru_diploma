import pytest
import json
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser
from appium import webdriver
from config import Settings
from dotenv import load_dotenv
from helper.get_env_path import get_app_path, get_mobile_env_path
from helper.attach_helpers import mobile_attach_video


def pytest_addoption(parser):
    parser.addoption(
        '--env',
        help='Environment for test',
        choices=['browserstack', 'local'],
        default='browserstack'
    )


@pytest.fixture(scope='function')
def set_mobile_browser(request):
    environment = request.config.getoption('--env')

    load_dotenv(get_mobile_env_path(environment))
    settings = Settings()
    options = UiAutomator2Options()

    if environment == 'browserstack':
        options.load_capabilities({
            "platformName": settings.platformName,
            "platformVersion": settings.platformVersion,
            "deviceName": settings.deviceName,

            # Set URL of the application under test
            "app": settings.app,

            # Set other BrowserStack capabilities
            'bstack:options': {
                "projectName": settings.projectName,
                "buildName": settings.buildName,
                "sessionName": settings.sessionName,
                'networkLogs': settings.networkLogs,

                # Set your access credentials
                "userName": settings.userName,
                "accessKey": settings.accessKey
            }
        })

    elif environment == 'local':
        options.load_capabilities({
            'appium:automationName': settings.automationName,
            'appium:app': get_app_path(settings.app),
            'platformName': settings.platformName,
            'appium:appWaitActivity': settings.appWaitActivity
        })

    browser.config.driver = webdriver.Remote(settings.remoteBrowser, options=options)

    yield environment

    if environment == 'browserstack':
        session_id = browser.execute_script('browserstack_executor: {"action": "getSessionDetails"}')
        video_url = json.loads(session_id)['video_url']
        mobile_attach_video(video_url)

    browser.quit()
