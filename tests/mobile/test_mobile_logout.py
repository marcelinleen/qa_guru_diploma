import os
import allure
from dotenv import load_dotenv
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be
from helper.get_env_path import get_personal_env_path
from helper.mobile_helper.get_mobile_login import get_mobile_login
from pages.mobile_pages.mobile_user_menu import UserMenu


@allure.story('Logout')
@allure.label('Test Type', 'Mobile')
@allure.severity(allure.severity_level.NORMAL)
def test_mobile_logout(set_mobile_browser):
    # ARRANGE
    env = set_mobile_browser
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    get_mobile_login(env, login, password)
    user_menu = UserMenu()

    # ACT
    user_menu.open()
    user_menu.logout()

    # ASSERT
    with allure.step('Assert the logout'):
        browser.element((AppiumBy.ID, 'fm.last.android:id/btn_sign_in')).should(be.visible)
