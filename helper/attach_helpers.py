import allure
import json
from allure_commons.types import AttachmentType


def mobile_attach_video(m_video_url):
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" + m_video_url \
           + "'></video></body></html>"
    allure.attach(html, 'video', AttachmentType.HTML, '.html')


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')


def add_video(browser):
    video_url = ("https://selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4")
    html = ("<html><body><video width='100%' height='100%' controls autoplay><source src='"
            + video_url
            + "' type='video/mp4'></video></body></html>")
    allure.attach(body=html, name='video_' + browser.driver.session_id, attachment_type=AttachmentType.HTML,
                  extension='.html')


def attach_body():
    with allure.step(f'{method} {url}'):
        allure.attach(body=f'Status code: {response.status_code}, CURL: {curl}', name='request',
                      attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=json.dumps(response_type), name='Response Body', attachment_type=AttachmentType.JSON)
