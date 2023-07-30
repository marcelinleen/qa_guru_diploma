import allure


class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        with allure.step('Open the login page, assert the cookie'):
            self.browser.open('/login')

    def fill_login(self, login):
        with allure.step('Fill the login'):
            self.browser.element('#id_username_or_email').send_keys(login)

    def fill_password(self, password):
        with allure.step('Fill the password'):
            self.browser.element('#id_password').send_keys(password)

    def submit(self):
        with allure.step('Submit the form'):
            self.browser.element('[name="submit"]').click()
