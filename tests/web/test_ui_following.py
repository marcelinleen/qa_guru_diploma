from pages.web_pages.user_page import UserPage
from pages.web_pages.following_page import FollowingPage
from helper.get_env_path import test_data_path, get_personal_env_path
from helper.web_helpers.get_web_log_in import get_web_log_in
from helper.api_helpers.check_following_list import clean_following_list, add_following
from dotenv import load_dotenv
from selene import have
import os
import allure
import pytest


@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_follow_user(setup_browser):
    # ARRANGE
    browser = setup_browser
    get_web_log_in(browser)

    user_page = UserPage(browser)
    follow_page = FollowingPage(browser)

    load_dotenv(get_personal_env_path())
    my_user_page = os.getenv('LOGIN')
    load_dotenv(test_data_path)
    user = os.getenv('ANOTHER_USERNAME')

    clean_following_list(browser, my_user_page, user)

    # ACT
    with allure.step('Open other user page'):
        user_page.open(user)
    with allure.step('Follow the user'):
        user_page.follow_user()
    with allure.step('Check the list of following users'):
        follow_page.open(my_user_page)

    # ASSERT
    with allure.step('Assert that user is added to following list'):
        browser.element('.user-list-item').should(have.text(user))


@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_unfollow_user(setup_browser):
    # ARRANGE
    browser = setup_browser
    get_web_log_in(browser)

    user_page = UserPage(browser)
    follow_page = FollowingPage(browser)

    load_dotenv(get_personal_env_path())
    my_user_page = os.getenv('LOGIN')
    load_dotenv(test_data_path)
    user = os.getenv('ANOTHER_USERNAME')

    add_following(browser, my_user_page, user)

    # ACT
    with allure.step("Open the user's page"):
        user_page.open(user)
    with allure.step('Unfollow the user'):
        user_page.unfollow_user()
    with allure.step('Open the following list'):
        follow_page.open(my_user_page)

    # ASSERT
    with allure.step('Assert the user is unfollowed'):
        browser.element('.user-list-item').should(have.no.text(user))
