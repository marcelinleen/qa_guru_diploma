import requests
from helper.get_api_sig import get_sign


def get_sk(base_url, api_key, login, password, api_secret):

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

    sk = response.json()['session']['key']
    return sk
