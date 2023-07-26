class LoginPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.open('/login')

    def fill_login(self, login):
        self.browser.element('#id_username_or_email').send_keys(login)

    def fill_password(self, password):
        self.browser.element('#id_password').send_keys(password)

    def submit(self):
        self.browser.element('[name="submit"]').click()
