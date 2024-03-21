import requests
import json

access_token = 'ZDI5NjY3MmItZTAxMC00MTYxLTk2MjAtMzdmOTA1OWRiNGE1YTgxZTAzMTktMjY2_P0A1_a61a0b2b-feba-43a3-8a20-e8cc10a43c9a'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

params = {
    'email': '64070184@kmitl.ac.th'
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))

