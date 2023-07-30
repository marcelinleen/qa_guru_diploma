from pages.web_pages.user_page import UserPage
from helper.api_helpers.api_get_user_following import get_user_following_list


def clean_following_list(browser, username, another_username, api_key):

    following_list = get_user_following_list(username, api_key)

    if another_username in following_list:
        user_page = UserPage(browser)
        user_page.open(another_username)
        user_page.unfollow_user()


def add_following(browser, username, another_username, api_key):

    following_list = get_user_following_list(username, api_key)

    if another_username not in following_list:
        user_page = UserPage(browser)
        user_page.open(another_username)
        user_page.follow_user()
