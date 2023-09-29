import requests
import json

url = 'https:api.example.com/post'
headers = {'Content-Type' : 'application/json'} #헤더에 전송할 데이터의 형식이 json임을 명시
data = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}

response = requests.post(url, headers = headers, data = json.dumps(data))

if response.statud_code == 200:
    result = response.json()
    print("Server response:",result)
else:
    print(f"Error : {response.status_code}")