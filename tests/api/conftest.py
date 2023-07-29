import pytest


@pytest.fixture(scope='function')
def set_api_env():
    base_url = 'http://ws.audioscrobbler.com/2.0/'

    yield base_url







