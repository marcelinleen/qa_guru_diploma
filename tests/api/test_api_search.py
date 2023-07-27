import os
import requests
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path, test_data_path


def test_successful_find_track(set_api_env):
    # ARRANGE
    base_url = set_api_env
    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('TRACK')

    # ACT
    response = requests.get(base_url, params={'method': 'track.search',
                                              'track': track,
                                              'api_key': api_key,
                                              'format': 'json'}
                            )

    # ASSERT
    assert response.status_code == 200
    assert int(response.json()['results']['opensearch:totalResults']) > 0


def test_unsuccessful_find_track(set_api_env):
    # ARRANGE
    base_url = set_api_env
    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    track = os.getenv('INCORRECT_TRACK')

    # ACT
    response = requests.get(base_url, params={'method': 'track.search',
                                              'track': track,
                                              'api_key': api_key,
                                              'format': 'json'}
                            )

    assert response.status_code == 200
    assert int(response.json()['results']['opensearch:totalResults']) == 0


def test_successful_find_artist(set_api_env):
    # ARRANGE
    base_url = set_api_env
    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('ARTIST')

    # ACT
    response = requests.get(base_url, params={'method': 'artist.search',
                                              'artist': artist,
                                              'api_key': api_key,
                                              'format': 'json'}
                            )

    # ASSERT
    assert response.status_code == 200
    assert int(response.json()['results']['opensearch:totalResults']) > 0


def test_unsuccessful_find_artist(set_api_env):
    # ARRANGE
    base_url = set_api_env
    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')
    load_dotenv(test_data_path)
    artist = os.getenv('INCORRECT_ARTIST')

    # ACT
    response = requests.get(base_url, params={'method': 'artist.search',
                                              'artist': artist,
                                              'api_key': api_key,
                                              'format': 'json'}
                            )

    # ASSERT
    assert response.status_code == 200
    assert int(response.json()['results']['opensearch:totalResults']) == 0
