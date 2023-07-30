from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be
import allure


class MobileLoginPage:

    def open(self):
        with allure.step('Open the login page'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/btn_sign_in')).click()

    def fill_login(self, environment, login):
        with allure.step('Fill the login'):
            if environment == 'local':
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View/android.view.View'
                                                 '/android.view.View[2]/android.view.View[3]/android.view.View[2]'
                                                 '/android.widget.EditText[1]')
                                ).wait_until(be.visible)
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View/android.view.View'
                                                 '/android.view.View[2]/android.view.View[3]/android.view.View[2]'
                                                 '/android.widget.EditText[1]')
                                ).send_keys(login)

            elif environment == 'browserstack':
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View'
                                                 '/android.view.View/android.view.View[1]/android.view.View'
                                                 '/android.view.View/android.widget.EditText[1]')
                                ).wait_until(be.visible)
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View'
                                                 '/android.view.View/android.view.View[1]/android.view.View'
                                                 '/android.view.View/android.widget.EditText[1]')).send_keys(login)

    def fill_password(self, environment, password):
        with allure.step('Fill the login'):
            if environment == 'local':
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View/android.view.View'
                                                 '/android.view.View[2]/android.view.View[3]/android.view.View[2]'
                                                 '/android.widget.EditText[2]')).send_keys(password)

            elif environment == 'browserstack':
                browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                                 '/android.widget.LinearLayout/android.webkit.WebView'
                                                 '/android.webkit.WebView/android.view.View/android.view.View'
                                                 '/android.view.View[1]/android.view.View/android.view.View'
                                                 '/android.widget.EditText[2]')).send_keys(password)

    def submit_form(self):
        with allure.step('Submit the form'):
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()

    def confirm_connect(self):
        with allure.step('Access connect'):
            browser.element((AppiumBy.XPATH, "//*[contains(@text, 'YES, ALLOW ACCESS')]")).wait_until(be.visible)
            browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()

    def close_notification_approve_window(self):
        with allure.step('Close notification approve window'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/btnClose')).wait_until(be.visible)
            browser.element((AppiumBy.ID, 'fm.last.android:id/btnClose')).click()

    def accept_cookie(self):
        with allure.step('Accept cookie (if necessary)'):
            if browser.element((AppiumBy.ID, 'fm.last.android:id/btn_accept_cookies')).is_displayed():
                browser.element((AppiumBy.ID, 'fm.last.android:id/btn_accept_cookies')).click()
