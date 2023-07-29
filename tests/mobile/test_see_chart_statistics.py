import os
import allure
from dotenv import load_dotenv
from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import have
from helper.get_env_path import get_personal_env_path
from helper.mobile_helper.get_mobile_login import get_mobile_login
from pages.mobile_pages.mobile_chart_page import ChartPage


def test_mobile_logout(set_mobile_browser):
    # ARRANGE
    env = set_mobile_browser
    load_dotenv(get_personal_env_path())
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    get_mobile_login(env, login, password)
    chart_page = ChartPage()

    # ACT
    with allure.step('Open chart page'):
        chart_page.open()

    with allure.step('Set last 30 days filter'):
        chart_page.open_period_filter()
        chart_page.set_last_30_days()

    # ASSERT
    with allure.step('Assert the filtered results'):
        browser.element((AppiumBy.ID, 'fm.last.android:id/tvPeriod')).should(have.exact_text('Last 30 days'))
