import requests
import json
from authentciation import access_token

room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMWNkYWI3NTAtZGVhNS0xMWVlLWIwOTctNGQ1ZjhkZTUxODFk'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))