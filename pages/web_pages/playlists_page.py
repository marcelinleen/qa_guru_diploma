from selene import be


class PlaylistsPage:

    def __init__(self, browser):
        self.browser = browser

    def open(self, username):
        self.browser.open(f'/user/{username}/playlists')

    def import_playlist(self, link):
        self.browser.element('[data-analytics-action="import"]').click()
        self.browser.element('#id_uri').send_keys(link)
        self.browser.element('[type="submit"]').click()
        self.browser.element('.modal-share-content').wait_until(be.visible)

    def open_imported_playlist(self):
        self.browser.element('.buffer-standard').click()

    def close_import_modal(self):
        self.browser.element('.modal-dismiss').click()
