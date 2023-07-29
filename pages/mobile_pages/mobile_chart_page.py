from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser


class ChartPage:

    def open(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/charts_graph')).click()

    def open_period_filter(self):
        browser.element((AppiumBy.ID, 'fm.last.android:id/ivPeriodButton')).click()

    def set_last_30_days(self):
        browser.element((AppiumBy.XPATH, "//*[contains(@text, 'Last 30 days')]")).click()
