import requests

headers = {
    'user-agent': USER_AGENT
}

r = requests.get('url', headers=headers)