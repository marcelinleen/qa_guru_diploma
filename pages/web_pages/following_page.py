
class FollowingPage:

    def __init__(self, browser):
        self.browser = browser
        self.following_list = self.browser.element('[class=container][class=page-content]')

    def open(self, username):
        self.browser.open(f'/user/{username}/following')

