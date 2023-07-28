import os
import json
import requests
from dotenv import load_dotenv
from helper.get_env_path import get_personal_env_path


def get_user_following_list(user):

    load_dotenv(get_personal_env_path())
    api_key = os.getenv('API_KEY')

    response = requests.get('http://ws.audioscrobbler.com/2.0/', params={
        'method': 'user.getfriends',
        'user': user,
        'api_key': api_key,
        'format': 'json'
                                                                        }
                            )

    response_json = str(response.json())
    response_json = response_json.replace("\'", "\"")
    data = json.loads(response_json)
    following_list = []

    for user in data["friends"]["user"]:
        following_list.append(user['name'])

    return following_list



