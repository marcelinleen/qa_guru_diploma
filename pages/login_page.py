

class RegistrationPage:

    def __init__(self, browser):
        self.browser = browser

    # TODO: set base url
    def open(self):
        self.browser.open('https://www.last.fm/join')

    def fill_username(self, username):
        self.browser.element('#id_userName').send_keys(username)

    def fill_email(self, email):
        self.browser.element('#id_email').send_keys(email)

    def fill_and_confirm_password(self, password):
        self.browser.element('#id_password').send_keys(password)
        self.browser.element('#id_passwordConf').send_keys(password)

    def click_recapcha(self):
        self.browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.browser.element('.recaptcha-checkbox-unchecked').click()

    def terms_agree(self):
        self.browser.element('#id_terms').click()

    def submit(self):
        self.browser.element('[type="submit"]').click()
