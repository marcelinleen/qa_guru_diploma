from pages.web_pages.user_page import UserPage
from pages.web_pages.following_page import FollowingPage
from helper.get_env_path import test_data_path, get_personal_env_path
from helper.web_helpers.get_web_log_in import get_web_log_in
from helper.api_helpers.check_following_list import clean_following_list
from dotenv import load_dotenv
from selene import be
import os
import allure
import pytest


@allure.story('Follow user')
@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('setup_browser', [(1920, 1080)], indirect=True)
def test_follow_user(setup_browser):
    # ARRANGE
    browser = setup_browser
    get_web_log_in(browser)

    user_page = UserPage(browser)
    follow_page = FollowingPage(browser)

    load_dotenv(get_personal_env_path())
    my_user_page = os.getenv('LOGIN')
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    user = os.getenv('ANOTHER_USERNAME')

    clean_following_list(browser, my_user_page, user, api_key)

    # ACT
    user_page.open(user)
    user_page.follow_user()
    follow_page.open(my_user_page)

    # ASSERT
    with allure.step('Assert that user is added to following list'):
        browser.element('.user-list-item').should(be.visible)
