from pages.web_pages.user_page import UserPage
from helper.get_env_path import get_personal_env_path
from helper.web_helpers.get_web_log_in import get_web_log_in
from dotenv import load_dotenv
from selene import be
import os
import allure
import pytest


@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True)
def test_open_favourite_tracks(setup_browser):
    # ARRANGE
    browser = setup_browser
    get_web_log_in(browser)

    user_page = UserPage(browser)

    load_dotenv(get_personal_env_path())
    user = os.getenv('LOGIN')

    with allure.step('Open other user page'):
        user_page.open(user)

    with allure.step('Open favourites tracks'):
        user_page.open_favourites()

    # ASSERT
    with allure.step('Check the tracks is displayed'):
        browser.element('.content-top-header').should(be.visible)