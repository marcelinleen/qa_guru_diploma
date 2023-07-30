import allure


class SearchResultsPage:

    def __init__(self, browser):
        self.browser = browser

    def define_search_as_artist(self):
        self.browser.element('.secondary-nav-item--artists').click()

    def define_search_as_album(self):
        self.browser.element('.secondary-nav-item--albums').click()

    with allure.step('Concrete search as track search'):
        def define_search_as_track(self):
            self.browser.element('.secondary-nav-item--tracks').click()
