from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import be


class MobileLoginPage:

    def open(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/btn_sign_in')).click()

    def fill_login(self, environment, login):
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
                                             '/android.view.View/android.widget.EditText[1]')
                            ).send_keys(login)

    def fill_password(self, environment, password):
        if environment == 'local':
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                             '/android.widget.LinearLayout/android.webkit.WebView'
                                             '/android.webkit.WebView/android.view.View/android.view.View'
                                             '/android.view.View[2]/android.view.View[3]/android.view.View[2]'
                                             '/android.widget.EditText[2]')
                            ).send_keys(password)

        elif environment == 'browserstack':
            browser.element((AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.RelativeLayout'
                                             '/android.widget.LinearLayout/android.webkit.WebView'
                                             '/android.webkit.WebView/android.view.View/android.view.View'
                                             '/android.view.View[1]/android.view.View/android.view.View'
                                             '/android.widget.EditText[2]')
                            ).send_keys(password)

    def submit_form(self):
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()

    def confirm_connect(self):
        browser.element((AppiumBy.XPATH, "//*[contains(@text, 'YES, ALLOW ACCESS')]")).wait_until(be.visible)
        browser.element((AppiumBy.CLASS_NAME, 'android.widget.Button')).click()

    def close_notification_approve_window(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/btnClose')).wait_until(be.visible)
        browser.element((AppiumBy.ID, 'fm.last.android:id/btnClose')).click()

    def accept_cookie(self):
        if browser.element((AppiumBy, 'fm.last.android:id/btn_accept_cookies')).is_displayed():
            browser.element((AppiumBy, 'fm.last.android:id/btn_accept_cookies')).click()

