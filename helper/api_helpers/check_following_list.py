from pages.web_pages.user_page import UserPage
from helper.api_helpers.api_get_user_following import get_user_following_list
from selene import be


def clean_following_list(browser, username, another_username, api_key):

    user_page = UserPage(browser)
    user_page.open(another_username)

    following_list = get_user_following_list(username, api_key)

    if (another_username in following_list) or (browser.element('[data-analytics-action="UnfollowUser"]').is_displayed()):
        user_page.unfollow_user()


def add_following(browser, username, another_username, api_key):
    user_page = UserPage(browser)
    user_page.open(another_username)

    following_list = get_user_following_list(username, api_key)

    if (another_username not in following_list) or browser.element('[data-analytics-action="FollowUser"]').is_displayed():
        user_page.follow_user()
