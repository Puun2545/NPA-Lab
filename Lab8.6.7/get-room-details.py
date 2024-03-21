import requests
import json
from authentciation import access_token

room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMWNkYWI3NTAtZGVhNS0xMWVlLWIwOTctNGQ1ZjhkZTUxODFk'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
 