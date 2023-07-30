import os
import allure
import pytest
from pages.web_pages.login_page import LoginPage
from pages.web_pages.home_page import HomePage
from selene import have, be
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_login(setup_browser):

    # ARRANGE
    browser = setup_browser
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    # ACT
    login_page.open()
    home_page.accept_cookie()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.submit()

    # ASSERT
    with allure.step('Assert the login'):
        browser.element('.header-title-label-wrap').should(have.exact_text(login))
        browser.element('.auth-link').should(be.visible)

