import os
import requests
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path, test_data_path
from helper.api_helpers.load_json_schema import load_json_schema
from jsonschema import validate
import allure


def test_successful_find_track(set_api_env):
    # ARRANGE
    base_url = set_api_env
    schema = load_json_schema('get_tracks.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('TRACK')

    # ACT
    with allure.step('Make a request'):
        response = requests.get(base_url, params={'method': 'track.search',
                                                  'track': track,
                                                  'api_key': api_key,
                                                  'format': 'json'}
                                )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) > 0
        validate(instance=response.json(), schema=schema)


def test_unsuccessful_find_track(set_api_env):
    # ARRANGE
    base_url = set_api_env
    schema = load_json_schema('get_tracks.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('INCORRECT_TRACK')

    # ACT
    with allure.step('Make a request'):
        response = requests.get(base_url, params={'method': 'track.search',
                                                  'track': track,
                                                  'api_key': api_key,
                                                  'format': 'json'}
                                )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) == 0
        validate(instance=response.json(), schema=schema)


def test_successful_find_artist(set_api_env):
    # ARRANGE
    base_url = set_api_env
    schema = load_json_schema('get_artists.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('ARTIST')

    # ACT
    with allure.step('Make a request'):
        response = requests.get(base_url, params={'method': 'artist.search',
                                                  'artist': artist,
                                                  'api_key': api_key,
                                                  'format': 'json'}
                                )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) > 0
        validate(instance=response.json(), schema=schema)


def test_unsuccessful_find_artist(set_api_env):
    # ARRANGE
    base_url = set_api_env
    schema = load_json_schema('get_artists.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('INCORRECT_ARTIST')

    # ACT
    with allure.step('Make a request'):
        response = requests.get(base_url, params={'method': 'artist.search',
                                                  'artist': artist,
                                                  'api_key': api_key,
                                                  'format': 'json'}
                                )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) == 0
        validate(instance=response.json(), schema=schema)
