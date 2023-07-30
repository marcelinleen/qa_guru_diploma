import allure


class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, username):
        with allure.step('Open user page'):
            self.browser.open(f'/user/{username}/')

    def follow_user(self):
        with allure.step('Follow the user'):
            self.browser.element('[data-analytics-action="FollowUser"]').click()

    def unfollow_user(self):
        self.browser.element('[data-analytics-action="UnfollowUser"]').click()

    def open_favourites(self):
        with allure.step('Open favourites tracks'):
            self.browser.element('.secondary-nav-item--loved').click()
