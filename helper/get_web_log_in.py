import os
from pages.web_pages.login_page import LoginPage
from pages.web_pages.home_page import HomePage
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


def get_web_log_in(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    login_page.open()
    home_page.accept_cookie()
    login_page.fill_login(login)
    login_page.fill_password(password)
    login_page.submit()
