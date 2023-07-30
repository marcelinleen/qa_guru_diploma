import os
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path, test_data_path
from helper.api_helpers.load_json_schema import load_json_schema
from jsonschema import validate
from helper.api_helpers.custom_session import project_url
import allure


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_find_track():
    # ARRANGE
    schema = load_json_schema('get_tracks.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('TRACK')

    # ACT
    with allure.step('Make a request'):
        response = project_url.get('', params={'method': 'track.search', 'track': track, 'api_key': api_key,
                                               'format': 'json'}
                                   )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) > 0
        validate(instance=response.json(), schema=schema)


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.CRITICAL)
def test_unsuccessful_find_track():
    # ARRANGE
    schema = load_json_schema('get_tracks.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('INCORRECT_TRACK')

    # ACT
    with allure.step('Make a request'):
        response = project_url.get('', params={'method': 'track.search', 'track': track, 'api_key': api_key,
                                               'format': 'json'}
                                   )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) == 0
        validate(instance=response.json(), schema=schema)


@allure.label('Test Type', 'API')
@allure.severity(allure.severity_level.CRITICAL)
def test_successful_find_artist():
    # ARRANGE
    schema = load_json_schema('get_artists.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('ARTIST')

    # ACT
    with allure.step('Make a request'):
        response = project_url.get('', params={'method': 'artist.search', 'artist': artist, 'api_key': api_key,
                                               'format': 'json'}
                                   )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) > 0
        validate(instance=response.json(), schema=schema)


def test_unsuccessful_find_artist():
    # ARRANGE
    schema = load_json_schema('get_artists.json')

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('INCORRECT_ARTIST')

    # ACT
    with allure.step('Make a request'):
        response = project_url.get('', params={'method': 'artist.search', 'artist': artist, 'api_key': api_key,
                                               'format': 'json'}
                                   )

    # ASSERT
    with allure.step('Assert the result'):
        assert response.status_code == 200
        assert int(response.json()['results']['opensearch:totalResults']) == 0
        validate(instance=response.json(), schema=schema)
