import requests

headers = {
    "X-QuakeToken": ""
}

data = {
    "query": "101.37.14.159",
    "start": 0,
    "size": 10
}

response = requests.post(url="https://quake.360.cn/api/v3/search/quake_service", headers=headers, json=data)
print(response.json())