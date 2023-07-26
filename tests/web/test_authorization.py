import os
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selene import have, be
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


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
    browser.element('.header-title-label-wrap').should(have.exact_text(login))
    browser.element('.auth-link').should(be.visible)


def test_logout(setup_browser):

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
    home_page.open()
    home_page.logout()

    # ASSERT
    browser.element('.site-auth--anon').should(be.visible)
