from selene import have


class HomePage:

    def __init__(self, browser):
        self.browser = browser
        self.search_title = self.browser.element('.content-top-header')

    def accept_cookie(self):
        self.browser.element('#onetrust-accept-btn-handler').click()

    def open(self):
        self.browser.open('/home')

    def search(self, request):
        self.browser.element('.masthead-search-toggle').click()
        self.browser.element('.masthead-search-field').send_keys(request).press_enter()

    def logout(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.browser.all('.mimic-link').element_by(have.text('Logout')).click()

