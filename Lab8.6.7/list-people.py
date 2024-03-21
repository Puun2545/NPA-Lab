import requests
import json
from authentciation import access_token

person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mMzI5ZjIzZi1mZjYwLTQwZjItYjI5Zi1iZjI5ZjI5ZjI5ZjA'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
