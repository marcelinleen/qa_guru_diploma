import os
from helper.get_env_path import get_personal_env_path
from dotenv import load_dotenv
import requests
from helper.get_sign import get_sign


def test_get_auth(set_api_env):
    # ARRANGE
    base_url = set_api_env
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
    response = requests.post(base_url, params={'method': 'auth.getMobileSession', 'password': password,
                                               'username': login, 'api_key': api_key, 'api_sig': api_sign,
                                               'format': 'json'
                                               })

    # ASSERT
    assert response.status_code == 200
    assert response.json()['session']['name'] == login
