import os
import allure
import pytest
from pages.web_pages.login_page import LoginPage
from pages.web_pages.home_page import HomePage
from selene import have, be
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


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
    with allure.step('Open the login page, assert the cookie'):
        login_page.open()
    # TODO maybe get rid of the cookie step
        home_page.accept_cookie()
    with allure.step('Fill the login and password'):
        login_page.fill_login(login)
        login_page.fill_password(password)
    with allure.step('Submit the form'):
        login_page.submit()

    # ASSERT
    with allure.step('Assert the login'):
        browser.element('.header-title-label-wrap').should(have.exact_text(login))
        browser.element('.auth-link').should(be.visible)


@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
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
    # TODO maybe get rid of the cookie step
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
