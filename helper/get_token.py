import requests


def get_token(api_key):

    response = requests.get('http://ws.audioscrobbler.com/2.0/', params={'method': 'auth.gettoken', 'api_key': api_key,
                                                                         'format': 'json'}
                            )
    return str(response.json()['token'])
