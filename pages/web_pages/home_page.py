from selene import have
import allure


class HomePage:

    def __init__(self, browser):
        self.browser = browser
        self.search_title = self.browser.element('.content-top-header')

    def accept_cookie(self):
        with allure.step('Assert the cookie'):
            self.browser.element('#onetrust-accept-btn-handler').click()

    def open(self):
        with allure.step('Open the main page'):
            self.browser.open('/home')

    def search(self, request):
        with allure.step('Make a search'):
            self.browser.element('.masthead-search-toggle').click()
            self.browser.element('.masthead-search-field').send_keys(request).press_enter()

    def logout(self):
        with allure.step('Logout'):
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.browser.all('.mimic-link').element_by(have.text('Logout')).click()
