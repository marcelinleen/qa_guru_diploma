from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from pages.mobile_pages.mobile_login_page import MobileLoginPage


def get_mobile_login(env, login, password):
    login_page = MobileLoginPage()

    login_page.open()
    login_page.fill_login(env, login)
    login_page.fill_password(env, password)
    login_page.submit_form()
    browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()
    browser.element((AppiumBy.ID, 'fm.last.android:id/btnClose')).click()

