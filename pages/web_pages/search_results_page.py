import allure


class SearchResultsPage:

    def __init__(self, browser):
        self.browser = browser

    def define_search_as_artist(self):
        with allure.step('Concrete search as artist search'):
            self.browser.element('.secondary-nav-item--artists').click()

    def define_search_as_album(self):
        with allure.step('Concrete search as album search'):
            self.browser.element('.secondary-nav-item--albums').click()

    def define_search_as_track(self):
        with allure.step('Concrete search as track search'):
            self.browser.element('.secondary-nav-item--tracks').click()
