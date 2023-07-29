from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser


class UserMenu:

    def open(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/ivAvatar')).click()

    def logout(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/tvLogout')).click()
