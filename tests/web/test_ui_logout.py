import os
import allure
import pytest
from pages.web_pages.login_page import LoginPage
from pages.web_pages.home_page import HomePage
from selene import be
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True)
def test_logout(setup_browser):

    # ARRANGE
    browser = setup_browser
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    # ACT
    with allure.step('Open the login page, assert the cookie'):
        login_page.open()
        home_page.accept_cookie()
    with allure.step('Fill the login and password'):
        login_page.fill_login(login)
        login_page.fill_password(password)
    with allure.step("Submit the form and open user's page"):
        login_page.submit()
        home_page.open()
    with allure.step('Logout'):
        home_page.logout()

    # ASSERT
    with allure.step('Assert the logout'):
        browser.element('.site-auth--anon').should(be.visible)
