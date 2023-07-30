from selene import be
class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, username):
        self.browser.open(f'/user/{username}/')

    def follow_user(self):
        self.browser.element('[data-analytics-action="FollowUser"]').click()
        self.browser.element('[data-analytics-action="UnfollowUser"]').wait_until(be.visible)

    def unfollow_user(self):
        self.browser.element('[data-analytics-action="UnfollowUser"]').click()
        self.browser.element('[data-analytics-action="FollowUser"]').wait_until(be.visible)
