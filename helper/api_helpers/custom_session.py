import json
import logging
import curlify
from requests import Session, Response
import allure
from allure_commons.types import AttachmentType


class CustomSession(Session):
    def __init__(self, base_url):
        self.base_url = base_url
        super().__init__()

    def request(self, method, url, **kwargs) -> Response:
        response = super(CustomSession, self).request(method=method, url=self.base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(f'Status code: {response.status_code}, CURL: {curl}')
        if 'application/json' in curl:
            response_type = response.json()
        else:
            response_type = response.text
        with allure.step(f'{method} {url}'):
            allure.attach(body=f'Status code: {response.status_code}, CURL: {curl}', name='request',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            allure.attach(body=json.dumps(response_type), name='Response Body', attachment_type=AttachmentType.JSON)
            return response


project_url = CustomSession('http://ws.audioscrobbler.com/2.0/')
