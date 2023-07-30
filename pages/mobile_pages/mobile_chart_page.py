from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
import allure


class ChartPage:

    def open(self):
        with allure.step('Open chart page'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/charts_graph')).click()

    def open_period_filter(self):
        with allure.step('Open period filter'):
            browser.element((AppiumBy.ID, 'fm.last.android:id/ivPeriodButton')).click()

    def set_last_30_days(self):
        with allure.step('Set last 30 days filter'):
            browser.element((AppiumBy.XPATH, "//*[contains(@text, 'Last 30 days')]")).click()
