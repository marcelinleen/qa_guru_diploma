import json
import requests


def get_user_following_list(user, api_key):

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



