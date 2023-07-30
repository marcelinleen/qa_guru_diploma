import logging
import os
from helper.get_env_path import get_personal_env_path
from dotenv import load_dotenv
import requests
from helper.api_helpers.get_api_sig import get_sign
import allure
from helper.api_helpers.load_json_schema import load_json_schema
from jsonschema import validate


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.BLOCKER)
def test_api_login(set_api_env):
    # ARRANGE
    base_url = set_api_env
    schema = load_json_schema('post_create_session.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    data = {
        'method': 'auth.getMobileSession',
        'password': password,
        'username': login,
        'api_key': api_key
    }

    api_sign = get_sign(data, api_secret)

    # ACT
    with allure.step('Make a request'):
        response = requests.post(base_url, params={'method': 'auth.getMobileSession', 'password': password,
                                                   'username': login, 'api_key': api_key, 'api_sig': api_sign,
                                                   'format': 'json'
                                                   }
                                 )

    logging.info(response.status_code)
    logging.info(response.json())

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert response.json()['session']['name'] == login
        validate(instance=response.json(), schema=schema)
