import os
from helper.get_env_path import get_personal_env_path, test_data_path
from dotenv import load_dotenv
from helper.api_helpers.get_api_sig import get_sign
from helper.api_helpers.get_api_sk import get_sk
from helper.api_helpers.load_json_schema import load_json_schema
from jsonschema import validate
from helper.api_helpers.custom_session import project_url
import allure


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.CRITICAL)
def test_like_track():
    # ARRANGE

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    load_dotenv(test_data_path)
    track = os.getenv('TRACK')
    artist = os.getenv('ARTIST')

    sk = get_sk('http://ws.audioscrobbler.com/2.0/', api_key, login, password, api_secret)

    data = {
        'method': 'track.love',
        'track': track,
        'artist': artist,
        'api_key': api_key,
        'sk': sk
    }

    api_sign = get_sign(data, api_secret)

    # ACT
    with allure.step('Make a request'):
        response = project_url.post('', params={'method': 'track.love', 'track': track, 'artist': artist,
                                                'api_key': api_key, 'api_sig': api_sign, 'sk': sk
                                                }
                                    )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert '<lfm status="ok" />' in response.text


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.CRITICAL)
def test_get_favourite_tracks():
    # ARRANGE
    schema = load_json_schema('get_users_favourite_tracks.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    login = os.getenv('LOGIN')

    # ACT
    with allure.step('Make a request'):
        response = project_url.get('', params={'method': 'user.getLovedTracks', 'api_key': api_key, 'username': login,
                                               'format': 'json'
                                               }
                                   )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert response.json()['lovedtracks']
        validate(instance=response.json(), schema=schema)
