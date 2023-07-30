from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
import allure


class UserMenu:

    def open(self):
        with allure.step('Open the side menu'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/ivAvatar')).click()

    def logout(self):
        with allure.step('Click on Logout point'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/tvLogout')).click()
