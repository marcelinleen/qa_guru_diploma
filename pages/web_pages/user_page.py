class UserPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, username):
        self.browser.open(f'/user/{username}/')

    def follow_user(self):
        self.browser.element('[data-analytics-action="FollowUser"]').click()

    def unfollow_user(self):
        self.browser.element('[data-analytics-action="UnfollowUser"]').click()

    def open_favourites(self):
        self.browser.element('.secondary-nav-item--loved').click()
