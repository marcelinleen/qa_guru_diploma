import os
import pytest
from pages.web_pages.home_page import HomePage
from pages.web_pages.search_results_page import SearchResultsPage
from selene import have, be
from helper.get_env_path import test_data_path
from dotenv import load_dotenv
import allure


@allure.story('Search')
@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_search_artist(setup_browser):
    # ARRANGE
    browser = setup_browser
    page = HomePage(browser)
    search_page = SearchResultsPage(browser)
    load_dotenv(test_data_path)
    artist = os.getenv('ARTIST')

    # ACT
    page.open()
    page.accept_cookie()
    page.search(artist)
    search_page.define_search_as_artist()

    # ASSERT
    with allure.step('Assert the results of search'):
        page.search_title.should(have.text(artist))
        browser.element('.artist-results').should(have.text(artist))


@allure.story('Search')
@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_search_album(setup_browser):
    # ARRANGE
    browser = setup_browser
    page = HomePage(browser)
    search_page = SearchResultsPage(browser)
    load_dotenv(test_data_path)
    album = os.getenv('ALBUM')

    # ACT
    page.open()
    page.accept_cookie()
    page.search(album)
    search_page.define_search_as_album()

    # ASSERT
    with allure.step('Assert the results of search'):
        page.search_title.should(have.text(album))
        browser.element('.album-results').should(have.text(album))


@allure.story('Search')
@allure.label('Test Type', 'UI')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize('setup_browser', [(1024, 640), (1920, 1080)], indirect=True)
def test_search_track(setup_browser):
    # ARRANGE
    browser = setup_browser
    page = HomePage(browser)
    search_page = SearchResultsPage(browser)
    load_dotenv(test_data_path)
    track = os.getenv('TRACK')

    # ACT
    page.open()
    page.accept_cookie()
    page.search(track)
    search_page.define_search_as_track()

    # ASSERT
    with allure.step('Assert the results of search'):
        page.search_title.should(have.text(track))
        browser.element(f'[title="{track}"]').should(be.visible)
