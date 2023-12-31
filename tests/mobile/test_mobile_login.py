import os
import allure
from dotenv import load_dotenv
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be
from pages.mobile_pages.mobile_login_page import MobileLoginPage
from helper.get_env_path import get_personal_env_path


@allure.story('Login')
@allure.label('Test Type', 'Mobile')
@allure.severity(allure.severity_level.BLOCKER)
def test_mobile_login(set_mobile_browser):
    # ARRANGE
    env = set_mobile_browser
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    login_page = MobileLoginPage()

    # ACT
    login_page.open()
    login_page.fill_login(env, login)
    login_page.fill_password(env, password)
    login_page.submit_form()
    login_page.confirm_connect()
    login_page.close_notification_approve_window()
    login_page.accept_cookie()

    # ASSERT
    with allure.step('Assert the login'):
        browser.element((AppiumBy.ID, 'fm.last.android:id/ivAvatar')).should(be.visible)
